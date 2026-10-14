#!/usr/bin/env python3
"""Porta de não regressão ciclo32: procedimentos especiais de dados abertos.

Testa IDs da matriz, artigos vigentes da Lei 14.129 e riscos do redline X6.
É teste documental, sem cálculo de prazo real nem concordância C0-J.
"""
import csv
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]/"modulos/T07/M03"
with (BASE/"MATRIZ_CICLO32_DADOS_ABERTOS_RECURSOS_ESPECIAIS.csv").open(encoding="utf-8-sig",newline="") as f:
    rows=list(csv.DictReader(f))
ids={r["id"] for r in rows}
if len(rows)!=12 or len(ids)!=12:raise AssertionError("Exigir 12 testes sem ID duplicado")
expected={f"DADOS{i:02d}" for i in range(1,13)}
if ids!=expected:raise AssertionError("ID faltante nos casos 01-12")
if any(r["estado"]!="Q_NAO_HOMOLOGADO" for r in rows):
    raise AssertionError("Resultado de pesquisa promovido indevidamente")
data={r["id"]:r for r in rows}
checks={
    "DADOS01":("ART30_C+P2","LAI_REGRAS_PRAZOS_PARA_PEDIDO"),
    "DADOS03":("ART32_C","ART32_VIGENTE_RESTAURADO"),
    "DADOS06":("ART35_C","RECURSO_10_DIAS"),
    "DADOS07":("ART35_PU","SUPERIOR_5_DIAS"),
    "DADOS08":("ART37_C","SUBSIDIARIEDADE"),
    "DADOS09":("ART42_C+P2","CANAL_CONDICIONAL"),
    "DADOS10":("ART43_II","PROVA_TECNICA"),
    "DADOS12":("LEI9784_ART59","LEI_GERAL_SUBSIDIARIA")
}
for k,(art,kind) in checks.items():
    if (data[k]["dispositivo"],data[k]["classe"])!=(art,kind):
        raise AssertionError(f"Regra especial ou natureza errada: {k}")
draft=(BASE/"MINUTA_CICLO32_X6_ESPECIALIDADE_DADOS_ABERTOS.md").read_text(encoding="utf-8")
for phrase in ("art.35", "art.37", "dez dias", "cinco dias", "reconsideração", "subsidiariamente", "R2", "DEC-016"):
    if phrase not in draft:raise AssertionError(f"Redline omite salvaguarda: {phrase}")
print("T07 ciclo32 OK: 12 testes Q, arts30/32/35/37/42/43 e Lei9784/56/59 distintos.")
print("Art35 10 dias para recurso e 5 dias autoridade superior; vedada substituição por prazo genérico.")
