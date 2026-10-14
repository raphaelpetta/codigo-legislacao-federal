#!/usr/bin/env python3
"""Teste deterministico de triagem de prazos PAF 2026 (nao calculo de vencimento).

Discrimina ciencia regular, categoria da norma, mudanca LC227 e transicao
ADI RFB 2/2026. Nenhum calendario local/feriado/termo exato e inferido.
"""
import csv
import datetime as dt
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]/"modulos/T07/M03"
LEGACY=dt.date(2026,1,14)
END_TRANSITION=dt.date(2026,3,31)
HOLIDAY_SUSPENSION_END=dt.date(2026,1,20)
def classify(row):
    when=dt.date.fromisoformat(row["data_ciencia_informada"])
    regime=row["regime"]
    if regime=="INSS_PAT":
        return "PROVA_E_HIERARQUIA_PENDENTES"
    if regime=="SEI_GERAL":
        return "REGIME_LEI9784_ESPECIFICO"
    if not regime.startswith("PAF_"):
        return "REGIME_NAO_SUPORTADO"
    # Essa classificacao prova apenas que foi informado recebimento:
    # nao confirma juridicamente ciencia em qualquer procedimento.
    if row["comprovacao_recebimento"]!="SIM":
        return "CIENCIA_NAO_CERTIFICADA"
    if regime=="PAF_PEQUENO_VALOR" and row["tipo_ato"]=="RECURSO":
        return "EXCECAO_PEQUENO_VALOR_30_CORRIDOS"
    if when<LEGACY:
        return "PRAZO_LEGADO_COM_SUSPENSAO_SUPERVENIENTE"
    if when<=END_TRANSITION:
        return "TRANSICAO_20_UTEIS_OU_30_CORRIDOS_POSTERIOR"
    if row["tipo_ato"] in ("RECURSO","IMPUGNACAO","PAGAMENTO_AUTO"):
        return "20_DIAS_UTEIS"
    return "ATO_NAO_CONTEMPLADO"
def main():
    p=ROOT/"MATRIZ_CICLO31_REGRAS_TEMPORAIS_PAF_2026.csv"
    with p.open(encoding="utf-8-sig",newline="") as f:
        rows=list(csv.DictReader(f))
    if len(rows)!=15 or len({r["cenario"] for r in rows})!=15:
        raise AssertionError("15 cenarios exclusivos obrigatorios")
    fail=[]
    for r in rows:
        got=classify(r)
        if got!=r["classe_esperada"]:
            fail.append((r["cenario"],r["classe_esperada"],got))
        if r["estado"]!="Q_HIPOTESE_NAO_CASO_REAL":
            fail.append((r["cenario"],"Q","promovido"))
    if fail:raise AssertionError(f"Falhas de categorizações: {fail}")
    # Guardas criticas contra regras de ciência fiscal copiadas no SEI/INSS.
    assert classify({**rows[3],"regime":"SEI_GERAL"})=="REGIME_LEI9784_ESPECIFICO"
    assert classify({**rows[3],"regime":"INSS_PAT"})=="PROVA_E_HIERARQUIA_PENDENTES"
    assert classify({**rows[3],"comprovacao_recebimento":"NAO"})=="CIENCIA_NAO_CERTIFICADA"
    assert classify({**rows[3],"data_ciencia_informada":"2026-03-31"})=="TRANSICAO_20_UTEIS_OU_30_CORRIDOS_POSTERIOR"
    assert classify({**rows[3],"data_ciencia_informada":"2026-04-01"})=="20_DIAS_UTEIS"
    print("T07 Ciclo31: 15 cenarios corretos, 5 guardas entre regimes, nenhum prazo de vencimento fabricado, nenhum C0-J.")
    print("Lacunas: termo real ciencia, homologacao de feriados/expediente, suspensao e processo concreto.")
if __name__=="__main__": main()
