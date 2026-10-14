#!/usr/bin/env python3
"""Ciclo33: verificar integridade da cadeia factual do CARF 1301-008.239.

Não tenta calcular prazo de 2015 nem homologar logs originais, apenas
checa as datas reportadas pelo acórdão e as lacunas.
"""
import csv
from datetime import date
from pathlib import Path
F=Path(__file__).resolve().parents[1]/"modulos/T07/M03/MATRIZ_CICLO33_CARF_1301_008239_EVENTOS.csv"
with F.open(encoding="utf-8-sig",newline="") as h:rows=list(csv.DictReader(h))
a={x["evento_id"]:x for x in rows}
if len(rows)!=6 or len(a)!=6:raise AssertionError("Exatamente seis eventos")
expected={
 "CARF2026-001":("TERMO_CIENCIA_ABERTURA_MENSAGEM","2015-02-12"),
 "CARF2026-002":("VENCIMENTO_RECONHECIDO","2015-03-16"),
 "CARF2026-003":("MANIFESTACAO_APRESENTADA","2015-04-22"),
 "CARF2026-004":("JULGAMENTO","2026-05-20"),
 "CARF2026-005":("PUBLICACAO","2026-06-18"),
 "CARF2026-006":("ABERTURA_DO_ANEXO","NAO_INFORMADA")
}
for k,v in expected.items():
    if (a[k]["tipo_evento"],a[k]["data"])!=v:raise AssertionError("Evento divergente: "+k)
if not date(2015,2,12)<date(2015,3,16)<date(2015,4,22)<date(2026,5,20)<date(2026,6,18):
    raise AssertionError("Ordem dos eventos incoerente")
if a["CARF2026-006"]["nivel_evidencia"]!="NAO_COMPROVADA":raise AssertionError("Log de anexo fabricado")
if any(x["c0_j"]!="Q" for x in rows):raise AssertionError("Caso promovido a C0-J")
print("T07 ciclo33 OK: 5 datas e 1 ausencia documental, 6 eventos Q.")
print("As datas de vencimento foram reconhecidas pelo CARF, NAO recalculadas sob LC227/2026.")
