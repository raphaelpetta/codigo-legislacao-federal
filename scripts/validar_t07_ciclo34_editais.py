#!/usr/bin/env python3
"""T07 ciclo34: diferenciar nulidade edital MS27227 de requisito Tema1329."""
import csv
from pathlib import Path
p=Path(__file__).resolve().parents[1]/"modulos/T07/M03/MATRIZ_CICLO34_CONTRASTE_EDITAL_STJ.csv"
with p.open(encoding="utf-8-sig",newline="") as f:r=list(csv.DictReader(f))
assert len(r)==12 and len({x["id"] for x in r})==12
d={x["id"]:x for x in r}
assert {f"A{i:02d}" for i in range(1,13)}==set(d)
assert d["A01"]["conclusao_ou_controle"]=="NULIDADE_RECONHECIDA"
assert d["A04"]["conclusao_ou_controle"]=="NULIDADE_NAO_AUTOMATICA"
assert d["A05"]["conclusao_ou_controle"]=="NULIDADE_ADMISSIVEL"
assert d["A06"]["conclusao_ou_controle"]=="REVISAR_REDACAO_9760_2019"
assert d["A07"]["conclusao_ou_controle"]=="REVISAR_REDACAO_11373_2023"
assert all(x["fase"]=="Q_NAO_HOMOLOGADO" for x in r)
assert all(x["url_fonte"].startswith("https://processo.stj.jus.br/") for x in r)
print("T07 ciclo34 OK: 12 contraprovas, 2 resultados distintos com limites de procedimento, redação, prejuízo; Q.")
