#!/usr/bin/env python3
"""Confere a trilha documental DEC-019/T07 contra onze deltas C1 canônicos (não certifica direito)."""
from __future__ import annotations
import csv
import json
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
IDS={"P13-01-C","P13-01-P1","P13-01-P2","P13-01-P2-I","P13-01-P2-II","P13-01-P2-III",
     "P19-69-C","EXP17-36-C","C18-49-A-P1","C18-49-B-C","C18-49-D-C"}
RISK={"CRITICO":5,"ALTO":3,"BAIXO":3}
def require(value,message):
    if not value: raise ValueError(message)
def check(route,rows,queue):
    require(route.get("id")=="TP-2026-002" and route.get("titulo")=="T07.M03","trilha/id")
    require(route.get("fonte_pr")==45 and route.get("fonte_commit")=="2a4d1eefa864f44435aec70ed0cc55a96b718b64","fonte setorial")
    require(route.get("camada_preparatoria")=="DEC-019"
            and route.get("estado_juridico")=="Q_SEM_C0_J"
            and route.get("veiculo")=="A_VERIFICAR"
            and route.get("iniciativa")=="A_VERIFICAR"
            and route.get("quorum")=="A_VERIFICAR"
            and route.get("revisao_independente")=="PENDENTE"
            and route.get("revogacoes")=="NENHUMA"
            and route.get("efeito_legal")=="NENHUM"
            and route.get("dec016")=="PENDENTE"
            and route.get("dec001")=="PRESERVADA"
            and route.get("origens_preservadas") is True
            and route.get("estado_outros_10")=="GATE_ABERTO","trilha promove decisão/veículo/efeito")
    require(len(route.get("fontes",[]))>=2
            and all(x.startswith("https://") for x in route["fontes"]),"fontes")
    source={r["id_origem"]:r for r in rows}
    require(len(rows)==11 and set(source)==IDS,"universo CSV não corresponde aos onze C1")
    require({risk:sum(r["classe_risco"]==risk for r in rows) for risk in RISK}==RISK,"riscos alterados")
    mapped=route.get("unidades_c1")
    require(isinstance(mapped,list) and len(mapped)==11,"número de referências da trilha")
    ids=set()
    for x in mapped:
        id=x.get("id_origem")
        require(id in IDS and id not in ids,"origem inválida/duplicada")
        ids.add(id)
        require(x.get("estado")=="Q_SEM_C0_J"
                and x.get("prova_formal")=="A_VERIFICAR"
                and x.get("revogacao")=="NAO_PROPOSTA","C1 promovida indevidamente: "+id)
        r=source[id]
        require(r["classe_local"]=="C1_POTENCIAL_Q"
                and r["estado_juridico"]=="Q_SEM_C0_J"
                and r["status"]=="GATE_ABERTO"
                and r["texto_origem"]!=r["texto_previa"],"delta original violado: "+id)
    require(ids==IDS,"concordância sem cobertura")
    art=source["P19-69-C"]
    require(art["artigo_origem"]=="69" and "subsidiariamente" in art["texto_origem"]
            and "desta Lei" in art["texto_origem"] and "deste Livro" in art["texto_previa"],
            "art. 69 ou seu referente alterados")
    items={q["id"]:q for q in queue["questoes"]}
    child=items.get("QD-2026-005");parent=items.get("QD-2026-003")
    require(route.get("questao_desta_rodada")=="QD-2026-005"
            and route.get("unidade_da_questao")=="P19-69-C"
            and route.get("status_questao")=="SUBMETIDA","sem orientação decidida")
    require(child and parent and child.get("subquestao_de")=="QD-2026-003"
            and child["maturidade"]=="APTO_A_DELIBERAR"
            and child["fechamento"]=="FC1_APTO_A_ESCOLHA"
            and child["decisao"]["estado"]=="SUBMETIDA"
            and child["classe_juridica"]=="Q_SEM_C0_J"
            and parent["maturidade"]=="PESQUISA_FOCAL"
            and parent["decisao"]["estado"]=="NAO_SUBMETIDA"
            and parent["fechamento"]=="FC0_ABERTO","filha não pode homologar T07/questão-mãe")
    require(queue.get("dec016")=="PENDENTE","DEC-016 resolvida sem aprovação")
    return {"c1_q":len(mapped),"risco_critico":5,"risco_alto":3,"risco_baixo":3,"submetida":"QD-2026-005","aprovacoes_novas":0}
def main():
    try:
        route=json.loads((ROOT/"modulos/T07/M03_TRILHA_PREPARATORIA_DEC019_Q.json").read_text(encoding="utf-8"))
        queue=json.loads((ROOT/"governanca/19_FILA_QUESTOES_DELIBERAVEIS.json").read_text(encoding="utf-8"))
        with (ROOT/"central/03_T07_GATE_C1_11_EFEITOS_20261015.csv").open(encoding="utf-8-sig",newline="") as f:
            rows=list(csv.DictReader(f,strict=True))
        print("OK DEC019 T07: "+json.dumps(check(route,rows,queue),ensure_ascii=False,sort_keys=True))
    except (ValueError,OSError,KeyError,TypeError,csv.Error) as ex:
        sys.exit("FALHA TRILHA T07: "+str(ex))
if __name__=="__main__":main()
