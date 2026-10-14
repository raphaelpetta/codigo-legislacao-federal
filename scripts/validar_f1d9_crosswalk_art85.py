#!/usr/bin/env python3
"""Garantia de completude de 35 remissoes do CPC85 antes da renumeracao CLF.

Exige que referencias ao art77 continuem EXTERNAS e que simbolos HON.X
sejam apenas identificadores estaveis, nunca numero legislativo aprovado.
"""
import csv
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]/"modulos/T24/M01"
def load(path):
    with (BASE/path).open(encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f))
a=load("MAPA_36_UNIDADES_ART85_REMISSOES_E_GATE.csv")
b=load("GRAFO_F1D7_REMISSOES_EXPRESSAS_ART85.csv")
c=load("F1D9_CROSSWALK_35_REMISSOES_SIMBOLICAS.csv")
m={row["id_norma_origem"]:f"T24.M01.HON.{row['subunidade']}" for row in a}
if len(m)!=36 or len(a)!=36:raise AssertionError("Precisam ser preservadas 36 unidades art85 únicas")
if len(b)!=35 or len(c)!=35:raise AssertionError("35 arestas e 35 traduções exigidas")
refs={(r["id_origem"],r["id_destino_original"]) for r in b}
got={(r["id_fonte"],r["id_referido_fonte"]) for r in c}
if got!=refs:raise AssertionError("Crosswalk omitiu ou acrescentou remissões")
external="BR-LEI-2015-13105-ART-0077-C"
outside=[]
for r in c:
    if r["secao_simbolica_origem"]!=m[r["id_fonte"]]:
        raise AssertionError("Origem simbolica adulterada: "+r["id_fonte"])
    dest=r["id_referido_fonte"]
    if dest in m:
        if r["secao_simbolica_destino"]!=m[dest] or r["situacao_referencia"]!="INTERNA_SIMBOLICA":
            raise AssertionError("Destino interno incorreto: "+dest)
    else:
        outside.append(dest)
        if dest!=external or r["situacao_referencia"]!="EXTERNA_PENDENTE_DESTINO":
            raise AssertionError("Art77 precisa ficar pendente, fora de art85")
    if r["estado_juridico"]!="Q_NENHUM_NUMERO_NORMATIVO_DEFINIDO":
        raise AssertionError("Jamais promover identificador simbolico a C0-J")
if outside!=[external]:raise AssertionError(f"Exatamente uma referencia externa art77: {outside}")
p20=[r for r in c if r["id_fonte"].endswith("-P20")]
if len(p20)!=10:raise AssertionError("§20 exige dez destinos especificos")
print("T24 F1-D9 OK: 36 IDs, 35 remissoes, 34 internas e art77 externa pendente, §20 com 10 destinos.")
print("Destinos HON.* sao IDs conceituais, NAO numeracao CLF nem equivalencia juridica.")
