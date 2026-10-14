#!/usr/bin/env python3
"""Porta de integridade F1-D7 (art.85 CPC): IDs, 35 remissões e temas.

Não examina equivalência C0-J nem estabelece jurisprudência automaticamente.
"""
import csv
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]/"modulos/T24/M01"
def load(name):
    with (BASE/name).open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))
a=load("MATRIZ_F1D7_36_HONORARIOS_JURISPRUDENCIA.csv")
b=load("GRAFO_F1D7_REMISSOES_EXPRESSAS_ART85.csv")
prior=load("MAPA_36_UNIDADES_ART85_REMISSOES_E_GATE.csv")
ids={x["id_origem"] for x in a}
if len(a)!=36 or len(ids)!=36:raise AssertionError(f"36 unidades únicas exigidas: {len(a)}")
if {x["id_norma_origem"] for x in prior}!=ids:raise AssertionError("Matriz F1-D7 difere dos 36 IDs F1-D6")
if any(x["status_juridico"]!="Q_SEM_C0_J" for x in a):raise AssertionError("Promoção prematura de status jurídico")
if len(b)!=35 or len({(r["id_origem"],r["id_destino_original"]) for r in b})!=35:
    raise AssertionError(f"Esperadas 35 arestas únicas, encontradas {len(b)}")
external_id="BR-LEI-2015-13105-ART-0077-C"
for edge in b:
    if edge["id_origem"] not in ids:raise AssertionError("Origem não mapeada: "+edge["id_origem"])
    if edge["id_destino_original"] not in ids|{external_id}:
        raise AssertionError("Destino órfão: "+edge["id_destino_original"])
    if edge["estado"]!="Q":raise AssertionError("Destino já promovido indevidamente")
def dest(unit):
    pref="BR-LEI-2015-13105-ART-0085-"+unit
    return {x["id_destino_original"].replace("BR-LEI-2015-13105-ART-0085-","")
        for x in b if x["id_origem"]==pref}
required={
    "P20":{"P2","P3","P4","P5","P6","P6A","P8","P8A","P9","P10"},
    "P11":{"P2","P3","P4","P5","P6"},
    "P12":{"P11","BR-LEI-2015-13105-ART-0077-C"},
    "P6A":{"P2","P3","P8"},
    "P8A":{"P8","P2"}
}
for u,exp in required.items():
    got=dest(u)
    if got!=exp:raise AssertionError(f"Remissão expressa em {u}: esperado {sorted(exp)} obtido {sorted(got)}")
m={x["unidade"]:x for x in a}
for unit,topic in [("P11","T1059"),("P7","T1190"),("P8","T1076"),("P8A","T1313"),("P3","STF1255")]:
    if topic not in m[unit]["temas_relacionados"].split(","):
        raise AssertionError(f"Falta controle jurisprudencial {topic} em {unit}")
print("F1-D7 OK: 36 unidades Q, 35 remissões, sem destinos órfãos; §20=10; §11=5; §12=2; temas 1059,1076,1190,1313,STF1255 registrados.")
print("Aprovação estrutural não prova C0-J, modulação de precedentes, cadeia DOU nem competência DEC016.")
