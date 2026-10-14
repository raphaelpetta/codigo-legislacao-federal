#!/usr/bin/env python3
"""T07 ciclo35: integridade da sucessão do art122 e da remissão ao art96 §4.

Classifica o período por DATA DO ATO DE INTIMAÇÃO, não data do julgamento.
Não decide validade da intimação, ciência, prova ou nulidade em caso concreto.
"""
import csv
from datetime import date,timedelta
from pathlib import Path
F=Path(__file__).resolve().parents[1]/"modulos/T07/M03/MATRIZ_CICLO35_SEIS_PERIODOS_AMBIENTAL_2008_2026.csv"
with F.open(encoding="utf-8-sig",newline="") as f:rows=list(csv.DictReader(f))
assert len(rows)==6 and [r["periodo"] for r in rows]==[f"P{i}" for i in range(6)]
start=[date.fromisoformat(r["inicio_vigencia_inclusive"]) for r in rows]
assert start==[date.fromisoformat(x) for x in (
"2008-07-23","2008-12-11","2019-10-08","2022-05-24","2023-01-02","2024-09-20")]
for i,r in enumerate(rows):
    if i<len(rows)-1:
        d=date.fromisoformat(r["fim_vigencia_inclusive"])
        assert d+timedelta(days=1)==start[i+1],(i,d,start[i+1])
    else:assert r["fim_vigencia_inclusive"]==""
assert all(r["estado_conferencia"]=="Q_INTEPRETACAO_POR_CASO" for r in rows)
def period(iso):
    d=date.fromisoformat(iso)
    return next((row["periodo"] for row in reversed(rows) if d>=date.fromisoformat(row["inicio_vigencia_inclusive"])),None)
tests=[("2008-07-22",None),("2008-07-23","P0"),("2008-12-10","P0"),
       ("2008-12-11","P1"),("2019-10-07","P1"),("2019-10-08","P2"),
       ("2022-05-23","P2"),("2022-05-24","P3"),("2023-01-01","P3"),
       ("2023-01-02","P4"),("2024-09-19","P4"),("2024-09-20","P5"),
       ("2026-10-14","P5")]
for dt,expected in tests:assert period(dt)==expected,(dt,expected,period(dt))
assert "ART96_P4" in rows[5]["unidade_decreto6514"]
assert "Decreto 12189/2024" in rows[5]["ato_modificador_ou_origem"]
print("T07 ciclo35 OK: 6 períodos contíguos, 13 fronteiras, art122 e mudança da REMISSÃO art96§4 em 2024.")
print("Não se infere validade de edital, ciências ou prejuízo apenas do período.")
