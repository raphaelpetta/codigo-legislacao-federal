#!/usr/bin/env python3
"""T07 ciclo36: prova de aplicação do período 2014 ao caso ICMBio 039245-B.

Separar AR do auto, edital para alegações finais, prejuízo alegado e provado,
decisão do STJ e datas desconhecidas. Sem inventar prazo ou timestamp.
"""
import csv,datetime as dt
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]/"modulos/T07/M03"
def read(f):
    with (BASE/f).open(encoding="utf-8-sig",newline="") as h:return list(csv.DictReader(h))
a=read("MATRIZ_CICLO36_ICMBIO_REsp2154295_CASO_REAL.csv")
p=read("MATRIZ_CICLO35_SEIS_PERIODOS_AMBIENTAL_2008_2026.csv")
assert len(a)==12 and len({r["id"] for r in a})==12
assert len(p)==6
def period(s):
    date=dt.date.fromisoformat(s)
    return next((r["periodo"] for r in reversed(p) if date>=dt.date.fromisoformat(r["inicio_vigencia_inclusive"])),None)
facts={r["id"]:r for r in a}
for k in ("FATO01","FATO02"):
    assert period(facts[k]["data"])=="P1"
assert period("2014-04-01")=="P1"
assert period("2026-10-14")=="P5"
assert facts["FATO01"]["data"]=="2014-03-25"
assert facts["FATO02"]["data"]=="2014-05-05"
assert facts["FATO03"]["data"]=="DATA_EXATA_NAO_INFORMADA"
assert facts["FATO04"]["natureza_prova"]=="INFERENCIA_DA_HIPOTESE_JULGADA"
assert facts["FATO12"]["natureza_prova"]=="LACUNA_DOCUMENTAL"
assert facts["FATO09"]["data"]=="2025-10-08"
assert facts["FATO10"]["data"]=="2025-10-21"
assert "Afastou nulidade" in facts["FATO11"]["fato_documentado"]
assert all(r["status_c0j"]=="Q" and r["periodo_art122"]=="P1" for r in a)
assert all("202402374928" in r["url_inteiro_teor_stj"] for r in a)
print("T07 C36 OK: caso real ICMBio 039245-B/2014, 12 marcos e lacunas, regime P1 de 2008–2019.")
print("AR do auto de infração e edital de alegações finais mantidos separados; ausência de prova concreta de prejuízo sob Tema1329.")
