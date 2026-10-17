#!/usr/bin/env python3
"""R33: audita sete deltas C1 em dados locais; não constitui validação C0-J."""
import csv
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PATHS={
    "map":ROOT/"modulos/T07/M03_MAPA_SETE_C1_R33.json",
    "source":ROOT/"central/03_T07_GATE_C1_11_EFEITOS_20261015.csv",
    "triage":ROOT/"modulos/T07/M03/MATRIZ_TRIAGEM_215_UNIDADES_CICLO20.csv",
    "cases":ROOT/"central/06_T07_DOZE_CASOS_ADVERSARIAIS_REMISSOES_E_ESPECIALIDADE.csv",
    "view":ROOT/"produto/vistas/T07_PROCESSO_ADMINISTRATIVO_PREVIA.md",
    "queue":ROOT/"governanca/19_FILA_QUESTOES_DELIBERAVEIS.json",
    "route":ROOT/"modulos/T07/M03_TRILHA_PREPARATORIA_DEC019_Q.json",
}
EXPECTED={
"P13-01-C":("CRITICO","AMBITO","Este Livro estabelece","T07-E01"),
"P13-01-P1":("CRITICO","OUTROS_PODERES","Os preceitos deste Livro também se aplicam","T07-E02"),
"P13-01-P2":("ALTO","DEFINICAO_E_ESCOPO","Para os fins deste Livro, consideram-se","T07-E03"),
"P13-01-P2-I":("BAIXO","PONTUACAO_DEFINICAO","órgão:","T07-E03"),
"P13-01-P2-II":("BAIXO","PONTUACAO_DEFINICAO","entidade:","T07-E03"),
"P13-01-P2-III":("BAIXO","PONTUACAO_DEFINICAO","autoridade:","T07-E03"),
"C18-49-A-P1":("ALTO","DECISAO_COORDENADA","Para os fins deste Livro, considera-se decisão coordenada","T07-E07"),
}
SOURCE_TEXT={"P13-01-C":"Esta Lei","P13-01-P1":"desta Lei","P13-01-P2":"desta Lei",
             "C18-49-A-P1":"desta Lei"}
TYPO={"P13-01-P2-I":("órgão - ","órgão: "),
      "P13-01-P2-II":("entidade - ","entidade: "),
      "P13-01-P2-III":("autoridade - ","autoridade: ")}

def rows(path):
    with path.open(encoding="utf-8-sig",newline="") as f:
        return list(csv.DictReader(f,strict=True))

def insist(ok,msg):
    if not ok: raise ValueError(msg)

def check(m,source,triage,cases,view,queue,route):
    insist(m.get("id")=="T07-R33-SETE-C1"
           and m.get("schema_version")==1
           and m.get("carater")=="AUDITORIA_DOCUMENTAL_NAO_JURIDICA"
           and m.get("dec016")=="PENDENTE"
           and m.get("equivalencia_juridica")=="Q_SEM_C0_J"
           and m.get("t07_origem_commit")=="2a4d1eefa864f44435aec70ed0cc55a96b718b64",
           "Mapa R33 não é uma autorização para alteração legislativa")
    src={x["id_origem"]:x for x in source}
    tri={x["id_espelho"]:x for x in triage}
    case={x["id_teste"]:x for x in cases}
    insist(len(source)==len(src)==11 and len(triage)==len(tri)==215,
           "Universo original de 11 C1 / 215 unidades mudou")
    seven=m.get("sete")
    insist(isinstance(seven,list) and len(seven)==7
           and {x.get("id_origem") for x in seven}==set(EXPECTED),
           "Sete C1 não estão completos")
    for entry in seven:
        id=entry["id_origem"]
        risk,delta,preview,scenario=EXPECTED[id]
        s=src[id]; t=tri[id]
        insist(s["classe_risco"]==risk and s["tipo_delta"]==delta
               and s["classe_local"]=="C1_POTENCIAL_Q"
               and s["estado_juridico"]=="Q_SEM_C0_J"
               and s["status"]=="GATE_ABERTO"
               and s["texto_origem"]!=s["texto_previa"],
               "Classe/risco/status do original alterado: "+id)
        insist(t["texto_fonte"]==s["texto_origem"]
               and t["estado_auditoria_juridica"]=="NAO_AUDITADA_JURIDICAMENTE"
               and t["equivalencia_juridica"]=="Q"
               and t["status_efeito_normativo"]=="NENHUM",
               "Triagem de 215 não é C0-J/espelho literal: "+id)
        insist(entry["risco"]==risk and entry["cenario_principal"]==scenario
               and entry["classe_juridica"]=="Q_SEM_C0_J"
               and entry["estado"]=="PESQUISA_FOCAL"
               and entry["necessita_revisao_independente"] is True
               and len(entry["invariante"])>30,
               "Risco/direito/status não rastreado: "+id)
        insist(preview in view and preview in s["texto_previa"],
               "Prévia de Livro diferente do delta catalogado: "+id)
        insist(scenario in case and case[scenario]["resultado"]=="Q"
               and case[scenario]["id_c1_fonte"]==
                   ("P13-01-P2" if id in TYPO else id),
               "Contraprova não corresponde à origem: "+id)
        if id in SOURCE_TEXT:
            insist(SOURCE_TEXT[id] in s["texto_origem"],
                   "Referente original mudou: "+id)
        if id in TYPO:
            original,proposed=TYPO[id]
            insist(original in s["texto_origem"] and proposed in s["texto_previa"]
                   and s["texto_origem"].replace(original,proposed,1)==s["texto_previa"],
                   "Delta tipográfico não é exclusivamente pontuação: "+id)
    insist("**Art. LPA-SEQ4-001.** Este Livro estabelece" in view
           and "**§ 1º** Os preceitos deste Livro também se aplicam" in view
           and "**§ 2º** Para os fins deste Livro, consideram-se:" in view,
           "Tríplice escopo não corresponde à prévia")
    insist("**Art. LPA-SEQ4-050.**" in view
           and "**§ 4º** A decisão coordenada não exclui a responsabilidade originária" in view
           and "**§ 6º** Não se aplica a decisão coordenada aos processos administrativos:" in view
           and "**I –** de licitação;" in view
           and "**II –** relacionados ao poder sancionador; ou" in view
           and "**III –** em que estejam envolvidas autoridades de Poderes distintos." in view,
           "Exclusões/responsabilidade coordenada desapareceram da prévia")
    insist(m.get("grupo_unidades")==["P13-01-C","P13-01-P1","P13-01-P2"]
           and m.get("scoping_group")=="QD-2026-006"
           and m.get("fechamento_grupo")=="FC2_ESCOLHA_PREPARATORIA_A_CONFIRMADA_SEM_C0J",
           "Questão não pode aprovar incisos, norma ou art49-A")
    insist(m.get("restante")=={"remissoes_t07_r32":["EXP17-36-C","C18-49-B-C","C18-49-D-C"],
                              "art69_dec020":"P19-69-C","total_c1":11,
                              "fechos_juridicos":0,"revogacoes":0,"reformas_m_aprovadas":0},
           "Dez C1/DEC020 foram promovidos ou desapareceram")
    items={x["id"]:x for x in queue["questoes"]}
    child=items.get("QD-2026-006"); parent=items.get("QD-2026-003")
    insist(queue.get("dec016")=="PENDENTE" and len(items)==6
           and child and child["subquestao_de"]=="QD-2026-003"
           and child["maturidade"]=="APTO_A_DELIBERAR"
           and child["decisao"]["estado"]=="CONFIRMADA"
           and child["decisao"].get("registro_decisao")=="DEC-021"
           and child["decisao"].get("alternativa_escolhida")==child["alternativas"][0]
           and child["fechamento"]=="FC2_ESCOLHA_CONFIRMADA"
           and child["classe_juridica"]=="Q_SEM_C0_J"
           and parent["maturidade"]=="PESQUISA_FOCAL"
           and parent["fechamento"]=="FC0_ABERTO",
           "Submissão QD006 não aprova o art1 ou a questão mãe")
    approved=m.get("decisao_preparatoria",{})
    insist(approved.get("id")=="DEC-021" and approved.get("questao")=="QD-2026-006"
           and approved.get("alternativa")=="A"
           and approved.get("status")=="CONFIRMADA_FC2_SOMENTE_PREPARATORIO"
           and approved.get("evidencia")=="https://github.com/raphaelpetta/codigo-legislacao-federal/issues/48#issuecomment-6242003768"
           and approved.get("sem_efeito_juridico") is True
           and approved.get("unidades_cobertas")==["P13-01-C","P13-01-P1","P13-01-P2"]
           and set(approved.get("fora_do_escopo",[]))==
             {"P13-01-P2-I","P13-01-P2-II","P13-01-P2-III","C18-49-A-P1"},
           "DEC021 não aprova art49A, os incisos ou direito positivo")
    insist(route.get("estado_juridico")=="Q_SEM_C0_J"
           and route.get("efeito_legal")=="NENHUM"
           and route.get("dec016")=="PENDENTE"
           and route.get("decisao_preparatoria",{}).get("id")=="DEC-020",
           "Camada P e DEC020 preservadas")
    return {"c1_em_analise":7,"escopo_aptas":3,"pontuacao_aguarda":3,
            "coordenada_aguarda":1,"c1_q_total":11,"homologacoes_novas":0}

def main():
    try:
        m=json.loads(PATHS["map"].read_text(encoding="utf-8"))
        q=json.loads(PATHS["queue"].read_text(encoding="utf-8"))
        route=json.loads(PATHS["route"].read_text(encoding="utf-8"))
        result=check(m,rows(PATHS["source"]),rows(PATHS["triage"]),
                     rows(PATHS["cases"]),PATHS["view"].read_text(encoding="utf-8"),q,route)
        print("OK R33 SETE C1: "+json.dumps(result,ensure_ascii=False,sort_keys=True))
    except (OSError,ValueError,KeyError,TypeError,csv.Error) as exc:
        raise SystemExit("FALHA R33 SETE C1: "+str(exc))
if __name__=="__main__": main()
