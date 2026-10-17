#!/usr/bin/env python3
"""Cotejo triangular das remissões T07 em fontes documentais, SEM certificar C0-J."""
from __future__ import annotations
import csv
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
MAPA=ROOT/"modulos/T07/M03_MAPA_TRIPLA_REMISSAO_R32.json"
MATRIX=ROOT/"central/03_T07_GATE_C1_11_EFEITOS_20261015.csv"
TRIAGE=ROOT/"modulos/T07/M03/MATRIZ_TRIAGEM_215_UNIDADES_CICLO20.csv"
CASES=ROOT/"central/06_T07_DOZE_CASOS_ADVERSARIAIS_REMISSOES_E_ESPECIALIDADE.csv"
VIEW=ROOT/"produto/vistas/T07_PROCESSO_ADMINISTRATIVO_PREVIA.md"
QUEUE=ROOT/"governanca/19_FILA_QUESTOES_DELIBERAVEIS.json"
TRILHA=ROOT/"modulos/T07/M03_TRILHA_PREPARATORIA_DEC019_Q.json"
IDS={"EXP17-36-C","C18-49-B-C","C18-49-D-C"}
OTHER={"P13-01-C","P13-01-P1","P13-01-P2","P13-01-P2-I",
       "P13-01-P2-II","P13-01-P2-III","C18-49-A-P1"}
RISKS={"EXP17-36-C":"CRITICO","C18-49-B-C":"ALTO","C18-49-D-C":"CRITICO"}

def demand(test,message):
    if not test: raise ValueError(message)

def readcsv(path):
    with path.open(encoding="utf-8-sig",newline="") as stream:
        return list(csv.DictReader(stream,strict=True))

def check(m,source,triage,cases,view,queue,route):
    demand(m.get("schema_version")==1 and m.get("id")=="T07-R32-TRIPLA-REMISSAO",
           "Identidade e schema do mapa")
    demand(m.get("dec016")=="PENDENTE" and m.get("dec019")=="DUPLA_CAMADA_APROVADA"
           and m.get("dec020")=="ART69_REFERENTE_PREPARATORIO_APROVADO"
           and m.get("condicao")=="APENAS_PROVA_DOCUMENTAL_SEM_EQUIVALENCIA_JURIDICA",
           "Não transformar auditoria em aprovação normativa")
    demand(m.get("fonte_setorial_pr")==45
           and m.get("fonte_setorial_sha")=="2a4d1eefa864f44435aec70ed0cc55a96b718b64",
           "Proveniência do corpus T07 divergente")
    bysource={x["id_origem"]:x for x in source}
    bytriage={x["id_espelho"]:x for x in triage}
    bycase={x["id_teste"]:x for x in cases}
    demand(len(source)==11 and len(bysource)==11,"Universo dos 11 C1 inconsistente")
    demand(len(triage)==215 and len(bytriage)==215,"Matriz de triagem T07 de 215 unidades alterada")
    rem=m.get("remissoes")
    demand(isinstance(rem,list) and len(rem)==3,"Três remissões necessárias")
    demand({x.get("origem_id") for x in rem}==IDS,"Fontes do trio trocadas/duplicadas")
    used=set()
    for x in rem:
        oid=x["origem_id"]
        line=bysource[oid]
        demand(line["artigo_origem"]==x["origem_artigo"]
               and line["classe_risco"]==RISKS[oid]
               and line["classe_local"]=="C1_POTENCIAL_Q"
               and line["estado_juridico"]=="Q_SEM_C0_J"
               and line["status"]=="GATE_ABERTO","Original C1 alterado: "+oid)
        demand(x["alvo_citacao"] in line["texto_origem"]
               and x["alvo_experimental"] in line["texto_previa"]
               and line["texto_origem"]!=line["texto_previa"],"Referente textual não corresponde: "+oid)
        demand(x.get("classe_juridica")=="Q_SEM_C0_J"
               and x.get("estado_auditoria")=="VINCULO_DOCUMENTAL_VERIFICAVEL_SEM_HOMOLOGACAO",
               "Promoção de equivalência indevida: "+oid)
        demand(x.get("protecao") and len(x["protecao"])>25,"Garantia não registrada: "+oid)
        demand(x["alvo_lei"] in {"9","26","37"}
               and x["id_artigo_experimental_alvo"] not in used,"Alvo inválido/duplicado")
        used.add(x["id_artigo_experimental_alvo"])
        target=bytriage.get(x["destino_unidade_fonte"])
        origin=bytriage.get(oid)
        demand(target is not None and origin is not None,"Concordância/triagem sem origem ou alvo: "+oid)
        demand(target["estado_auditoria_juridica"]=="NAO_AUDITADA_JURIDICAMENTE"
               and target["equivalencia_juridica"]=="Q"
               and origin["estado_auditoria_juridica"]=="NAO_AUDITADA_JURIDICAMENTE"
               and origin["equivalencia_juridica"]=="Q",
               "Cotejo documental não demonstra auditoria jurídica independente: "+oid)
        demand(("art."+x["alvo_lei"]+" unidade C") in target["origem_unidade"]
               and x["cabecalho_fonte_alvo"] in target["texto_fonte"],
               "Lei de origem alvo diferente da citada: "+oid)
        def text_of(ident):
            match=re.search(r"^\*\*Art\. "+re.escape(ident)+r"\.\*\* (.*)$",view,re.M)
            return match.group(1) if match else None
        view_src=text_of(x["id_artigo_experimental_origem"])
        view_dst=text_of(x["id_artigo_experimental_alvo"])
        demand(view_src and view_dst,"Destino ou fonte ausente da prévia Q: "+oid)
        demand(x["alvo_experimental"] in view_src
               and x["cabecalho_fonte_alvo"] in view_dst,
               "Prévia Q aponta para artigo/conteúdo incompatível: "+oid)
        scenarios=x.get("cenario_ids")
        demand(isinstance(scenarios,list) and bool(scenarios)
               and len(set(scenarios))==len(scenarios),"Cenário adversarial ausente/duplicado")
        for sid in scenarios:
            sc=bycase.get(sid)
            demand(sc is not None and sc["id_c1_fonte"]==oid and sc["resultado"]=="Q",
                   "Cenário adversarial não protege original: "+sid)
    demand(set(m.get("outros_c1_ainda_sem_fecho",[]))==OTHER
           and len(m["outros_c1_ainda_sem_fecho"])==7,"As outras sete C1 não foram preservadas")
    remaining={*IDS,*OTHER,"P19-69-C"}
    demand(remaining==set(bysource),"Uma das onze C1 desapareceu")
    a69=m.get("art69_ja_deliberado",{})
    demand(a69.get("origem_id")=="P19-69-C"
           and a69.get("decisao")=="DEC-020"
           and a69.get("estado")=="CONFIRMADA_PREPARATORIA_FC2"
           and a69.get("classe_juridica")=="Q_SEM_C0_J"
           and a69.get("fechamento_juridico")=="NAO","DEC020 não fecha C1 jurídico")
    demand(m.get("contagens")=={"total_c1":11,"triple_remissoes":3,"art69_procedimental":1,
                               "outros_c1":7,"homologados_c0j":0,"reformas_m_aprovadas":0},
           "Contagem/resultado formal indevido")
    demand(queue.get("dec016")=="PENDENTE" and len(queue["questoes"])>=5,
           "Fila ou DEC016 fora do corte")
    items={x["id"]:x for x in queue["questoes"]}
    if "QD-2026-006" in items:
        new=items["QD-2026-006"]
        demand(new["subquestao_de"]=="QD-2026-003"
               and new["maturidade"]=="APTO_A_DELIBERAR"
               and new["decisao"]["estado"]=="SUBMETIDA"
               and new["fechamento"]=="FC1_APTO_A_ESCOLHA"
               and new["classe_juridica"]=="Q_SEM_C0_J",
               "Nova questão de escopo não pode aprovar os três referentes por inércia")
    demand(items["QD-2026-003"]["maturidade"]=="PESQUISA_FOCAL"
           and items["QD-2026-003"]["decisao"]["estado"]=="NAO_SUBMETIDA"
           and items["QD-2026-005"]["decisao"]["registro_decisao"]=="DEC-020"
           and items["QD-2026-005"]["fechamento"]=="FC2_ESCOLHA_CONFIRMADA",
           "Pesquisa de remissões não aprova a questão-mãe/DEC020")
    demand(route.get("estado_juridico")=="Q_SEM_C0_J"
           and route.get("efeito_legal")=="NENHUM"
           and route.get("dec016")=="PENDENTE"
           and route.get("estado_outros_10")=="GATE_ABERTO","Trilha E/P inconsistente")
    return {"vinculos_documentais":3,"c1_preservados_q":11,
            "outras_c1_em_pesquisa":7,"aprovacoes_normativas":0,
            "dec016":"PENDENTE"}

def main():
    try:
        m=json.loads(MAPA.read_text(encoding="utf-8"))
        q=json.loads(QUEUE.read_text(encoding="utf-8"))
        r=json.loads(TRILHA.read_text(encoding="utf-8"))
        result=check(m,readcsv(MATRIX),readcsv(TRIAGE),readcsv(CASES),
                     VIEW.read_text(encoding="utf-8"),q,r)
        print("OK R32 REMISSOES T07: "+json.dumps(result,ensure_ascii=False,sort_keys=True))
    except (OSError,ValueError,KeyError,TypeError,csv.Error) as ex:
        raise SystemExit("FALHA R32 REMISSOES T07: "+str(ex))
if __name__=="__main__": main()
