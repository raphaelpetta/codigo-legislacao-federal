#!/usr/bin/env python3
"""Valida integridade gerencial da fila DEC-018; NÃO certifica direito ou decisões."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
MAT={"TRIAGEM","PESQUISA_FOCAL","APTO_A_DELIBERAR","BLOQUEADO_POR_DEPENDENCIA"}
DEC={"NAO_SUBMETIDA","SUBMETIDA","CONFIRMADA","CONFIRMADA_CONDICIONAL","REJEITADA","REABERTA"}
FC={"FC0_ABERTO","FC1_APTO_A_ESCOLHA","FC2_ESCOLHA_CONFIRMADA",
    "FC3_REDACAO_ESTABILIZADA","FC4_AUDITORIA_JURIDICA_INDEPENDENTE",
    "FC5_INTEGRADO_ANTEPROJETO_DELIBERADO"}
APPROVED={"CONFIRMADA","CONFIRMADA_CONDICIONAL"}
CLOSED={"FC2_ESCOLHA_CONFIRMADA","FC3_REDACAO_ESTABILIZADA",
        "FC4_AUDITORIA_JURIDICA_INDEPENDENTE","FC5_INTEGRADO_ANTEPROJETO_DELIBERADO"}

def demand(condition,message):
    if not condition: raise ValueError(message)

def validate(record, decision_register):
    demand(record.get("schema_version")==1 and record.get("registro")=="CLF-GOV-019-FILA",
           "Schema fila")
    demand(record.get("adocao_metodologica")=="DEC-018"
           and record.get("deliberacao_material_automatica") is False
           and record.get("dec016")=="PENDENTE", "Promoção automática ou DEC-016 não autorizada")
    demand("| DEC-018 | CONFIRMADA_PELO_USUARIO |" in decision_register,
           "DEC-018 sem confirmação procedural no registro central")
    demand("| DEC-016 | PENDENTE |" in decision_register,
           "DEC-016 modificada sem deliberação própria")
    items=record.get("questoes")
    demand(isinstance(items,list) and items,"Sem questões na fila")
    ids=set()
    for item in items:
        ident=item.get("id")
        demand(isinstance(ident,str) and re.fullmatch(r"QD-[0-9]{4}-[0-9]{3}",ident)
               and ident not in ids,"ID questão ausente/duplicada")
        ids.add(ident)
        for key in ("objeto","escopo","melhor_objecao","criterio_aptidao","proximo_passo",
                    "data_corte","versao_base"):
            demand(isinstance(item.get(key),str) and bool(item[key].strip()),
                   f"{ident}: campo ausente {key}")
        demand(item.get("maturidade") in MAT
               and item.get("fechamento") in FC
               and item.get("classe_juridica")=="Q_SEM_C0_J",
               f"{ident}: maturidade/fechamento/classe jurídica incompatível")
        demand(item.get("risco") in {"R1","R2","R3"}
               and all(item.get(k) in {"BAIXO","MEDIO","ALTO"} for k in
                       ("ganho_potencial","desbloqueio","esforco")),
               f"{ident}: avaliação qualitativa inconsistente")
        demand(isinstance(item.get("alternativas"),list) and len(item["alternativas"])>=2
               and len(set(item["alternativas"]))==len(item["alternativas"])
               and all(isinstance(x,str) and x.strip() for x in item["alternativas"]),
               f"{ident}: alternativas reais insuficientes")
        for k in ("referencias","dependencias"):
            demand(isinstance(item.get(k),list) and len(item[k])>0
                   and all(isinstance(x,str) and x.strip() for x in item[k]),
                   f"{ident}: {k} vazio")
        d=item.get("decisao")
        demand(isinstance(d,dict) and d.get("estado") in DEC,
               f"{ident}: decisão não tipada")
        stage=item["fechamento"]
        if d["estado"] in APPROVED:
            demand(item["maturidade"]=="APTO_A_DELIBERAR",
                   f"{ident}: questão confirmada sem aptidão documentada")
            demand(isinstance(d.get("alcance"),str) and bool(d["alcance"].strip()),
                   f"{ident}: confirmação sem limites da escolha")
        if ident=="QD-2026-004" and d.get("registro_decisao")=="DEC-019":
            demand(d.get("alternativa_escolhida")==item["alternativas"][0]
                   and item["alternativas"][0].startswith("A — Dupla camada:")
                   and d.get("estado")=="CONFIRMADA"
                   and stage=="FC2_ESCOLHA_CONFIRMADA"
                   and d.get("tipo_evidencia")=="TRANSCRICAO_SECUNDARIA_MENSAGEM_USUARIO"
                   and d.get("transcricao_aprovacao")==
                   "Aprovo expressamente a alternativa A da QD-2026-004 como diretriz preparatória do CLF, preservadas a DEC-001 e a pendência da DEC-016."
                   and d.get("evidencia_aprovacao")=="https://github.com/raphaelpetta/codigo-legislacao-federal/issues/48#issuecomment-6228937676"
                   and "| DEC-019 | CONFIRMADA_PELO_USUARIO |" in decision_register,
                   f"{ident}: DEC-019 não corresponde ao escopo da aprovação A")

        if ident=="QD-2026-005":
            demand(d.get("registro_decisao")=="DEC-020"
                   and d.get("estado")=="CONFIRMADA"
                   and stage=="FC2_ESCOLHA_CONFIRMADA"
                   and item.get("classe_juridica")=="Q_SEM_C0_J"
                   and d.get("alternativa_escolhida")==item["alternativas"][0]
                   and d.get("aprovador")=="USUARIO"
                   and d.get("transcricao_aprovacao")=="escolho a A"
                   and d.get("tipo_evidencia")=="TRANSCRICAO_SECUNDARIA_MENSAGEM_USUARIO"
                   and d.get("evidencia_aprovacao")==
                   "https://github.com/raphaelpetta/codigo-legislacao-federal/issues/48#issuecomment-6231927148"
                   and "| DEC-020 | CONFIRMADA_PELO_USUARIO |" in decision_register,
                   "QD005 deve refletir somente aprovação expressa A da DEC020")
        if d["estado"]=="SUBMETIDA":
            demand(item["maturidade"]=="APTO_A_DELIBERAR"
                   and stage=="FC1_APTO_A_ESCOLHA",
                   f"{ident}: questão submetida sem aptidão e FC1")
        if item["maturidade"]=="APTO_A_DELIBERAR" or d["estado"]=="SUBMETIDA":
            demand(isinstance(item.get("ref_dossie"),str)
                   and item["ref_dossie"].startswith("modulos/")
                   and item["ref_dossie"].endswith(".md")
                   and '..' not in Path(item["ref_dossie"]).parts
                   and isinstance(item.get("pergunta_deliberacao"),str)
                   and len(item["pergunta_deliberacao"].strip())>20
                   and isinstance(item.get("evidencias_maturidade"),list)
                   and len(item["evidencias_maturidade"])>=2
                   and all(isinstance(a,str) and a.startswith("https://") for a in item["evidencias_maturidade"]),
                   f"{ident}: falta dossiê, pergunta expressa ou fontes independentes para aptidão")
            parent=item.get("subquestao_de")
            if parent is not None:
                demand(any(x.get("id")==parent and x.get("id")!=ident for x in items),
                       f"{ident}: subquestão sem questão-mãe")

        if item["maturidade"]=="APTO_A_DELIBERAR":
            demand(stage!="FC0_ABERTO",f"{ident}: aptidão não materializada em FC1")
        if stage=="FC1_APTO_A_ESCOLHA":
            demand(item["maturidade"]=="APTO_A_DELIBERAR"
                   and d["estado"] not in {"CONFIRMADA","CONFIRMADA_CONDICIONAL"},
                   f"{ident}: FC1 contradiz a aptidão/decisão")
        if stage in CLOSED:
            demand(d["estado"] in APPROVED, f"{ident}: fechamento material sem decisão expressa")
        if d["estado"] in APPROVED:
            demand(stage in CLOSED
                   and d.get("alternativa_escolhida") in item["alternativas"]
                   and d.get("aprovador")=="USUARIO"
                   and isinstance(d.get("evidencia_aprovacao"),str)
                   and d["evidencia_aprovacao"].startswith("https://")
                   and isinstance(d.get("registro_decisao"),str)
                   and re.fullmatch(r"DEC-[0-9]{3}",d["registro_decisao"])
                   and "| "+d["registro_decisao"]+" | CONFIRMADA_PELO_USUARIO |" in decision_register,
                   f"{ident}: escolha sem prova expressa/registro DEC")
        else:
            demand(stage not in CLOSED
                   and d.get("alternativa_escolhida") is None
                   and d.get("aprovador") is None
                   and d.get("evidencia_aprovacao") is None
                   and d.get("registro_decisao") is None,
                   f"{ident}: aprovação fictícia ou fechamento sem decisão")
        if d["estado"]=="REABERTA":
            demand(isinstance(d.get("motivo_reabertura"),str)
                   and bool(d["motivo_reabertura"].strip()),f"{ident}: reabertura sem motivo")
        if stage in {"FC3_REDACAO_ESTABILIZADA","FC4_AUDITORIA_JURIDICA_INDEPENDENTE",
                     "FC5_INTEGRADO_ANTEPROJETO_DELIBERADO"}:
            demand(isinstance(item.get("evidencia_redacao"),str)
                   and bool(item["evidencia_redacao"].strip()),f"{ident}: FC3 sem versão da redação")
        if stage in {"FC4_AUDITORIA_JURIDICA_INDEPENDENTE","FC5_INTEGRADO_ANTEPROJETO_DELIBERADO"}:
            demand(isinstance(item.get("revisao_independente"),str)
                   and bool(item["revisao_independente"].strip()),
                   f"{ident}: FC4 sem prova de revisão independente")
        if stage=="FC5_INTEGRADO_ANTEPROJETO_DELIBERADO":
            demand(isinstance(item.get("integracao_sha"),str)
                   and bool(re.fullmatch("[0-9a-f]{40}",item["integracao_sha"])),
                   f"{ident}: FC5 sem commit de integração")
    if "| DEC-019 | CONFIRMADA_PELO_USUARIO |" in decision_register:
        selected=next((x for x in items if x["id"]=="QD-2026-004"),None)
        parent=next((x for x in items if x["id"]=="QD-2026-001"),None)
        demand(selected is not None
               and selected["decisao"].get("registro_decisao")=="DEC-019"
               and selected["decisao"]["estado"]=="CONFIRMADA"
               and selected["fechamento"]=="FC2_ESCOLHA_CONFIRMADA"
               and parent is not None
               and parent["maturidade"]=="PESQUISA_FOCAL"
               and parent["fechamento"]=="FC0_ABERTO"
               and parent["decisao"]["estado"]=="NAO_SUBMETIDA"
               and "| DEC-001 | CONFIRMADA_PELO_USUARIO |" in decision_register,
               "DEC-019 não pode fechar DEC-016/parent nem afastar DEC-001")
    if "| DEC-020 | CONFIRMADA_PELO_USUARIO |" in decision_register:
        parent=next((x for x in items if x["id"]=="QD-2026-003"),None)
        demand(parent is not None
               and parent["maturidade"]=="PESQUISA_FOCAL"
               and parent["fechamento"]=="FC0_ABERTO"
               and parent["decisao"]["estado"]=="NAO_SUBMETIDA"
               and "| DEC-019 | CONFIRMADA_PELO_USUARIO |" in decision_register,
               "DEC020 não encerra T07 inteiro nem altera DEC019")
    demand({"QD-2026-001","QD-2026-002","QD-2026-003"}.issubset(ids),
           "Pilotos da adoção metodológica omitidos")
    return {"questoes":len(items),
            "submetidas":sum(x["decisao"]["estado"]=="SUBMETIDA" for x in items),
            "confirmadas":sum(x["decisao"]["estado"] in APPROVED for x in items),
            "aptas":sum(x["maturidade"]=="APTO_A_DELIBERAR" for x in items),
            "fechadas":sum(x["fechamento"] in CLOSED for x in items)}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root",type=Path,default=ROOT)
    args=parser.parse_args()
    try:
        root=args.root.resolve()
        record=json.loads((root/"governanca/19_FILA_QUESTOES_DELIBERAVEIS.json").read_text(encoding="utf-8"))
        decisions=(root/"governanca/04_REGISTRO_DE_DECISOES.md").read_text(encoding="utf-8")
        result=validate(record,decisions)
        for item in record["questoes"]:
            if item["maturidade"]=="APTO_A_DELIBERAR":
                dossie=(root/item["ref_dossie"]).resolve()
                demand(dossie.is_relative_to(root)
                       and dossie.is_file(),f'{item["id"]}: dossiê de aptidão inexistente')
        print("OK FILA DEC-018 - sem aprovação normativa automática: "+
              json.dumps(result,ensure_ascii=False,sort_keys=True))
    except (OSError,ValueError,KeyError,TypeError,json.JSONDecodeError) as e:
        parser.exit(1,"FALHA FILA DELIBERAÇÃO: "+str(e)+"\n")
if __name__=="__main__":main()
