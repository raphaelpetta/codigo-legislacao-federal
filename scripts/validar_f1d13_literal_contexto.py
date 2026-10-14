#!/usr/bin/env python3
"""T24 F1-D13: classificar 45 arestas sem confundir remissão textual e contexto.

São dependências de pesquisa, não equivalência C0-J; subunidade §11 pode
conter ocorrências repetidas dos mesmos dois destinos.
"""
import csv
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]/"modulos/T24/M01"
def read(path):
    with (ROOT/path).open(encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f))
a=read("GRAFO_F1D7_REMISSOES_EXPRESSAS_ART85.csv")
b=read("MATRIZ_F1D12_DEZ_REMISSOES_P4_INCISOS.csv")
c=read("MATRIZ_F1D13_45_PARES_LITERAL_CONTEXTO.csv")
old={(x["id_origem"],x["id_destino_original"]) for x in a}
new={(x["id_fonte"],x["id_destino"]) for x in b}
all_pairs={(x["id_origem"],x["id_destino"]) for x in c}
assert len(a)==35 and len(b)==10 and len(c)==45 and len(all_pairs)==45
assert all_pairs==old|new and not(old&new),"Nao perder pares nem duplicar arestas"
assert all(x["estado_c0j"]=="Q_NAO_HOMOLOGADO" for x in c)
context=[x for x in c if x["categoria_ligacao"]=="CONTEXTO_CAPUT_E_INCISOS"]
assert len(context)==10 and {(r["id_origem"],r["id_destino"]) for r in context}==new
groups=[x for x in c if x["categoria_ligacao"]=="DESDOBRAMENTO_GRUPO_EXPRESSO"]
assert len(groups)==8,"§3 e §8 devem desdobrar 4 incisos cada"
p11=[x for x in c if x["id_origem"].endswith("-P11")]
assert len(p11)==5 and {x["categoria_ligacao"] for x in p11}=={"DESDOBRAMENTO_INTERVALO_EXPRESSO"}
p20=[x for x in c if x["id_origem"].endswith("-P20")]
assert len(p20)==10 and {x["categoria_ligacao"] for x in p20}=={"ENUMERACAO_LITERAL_DESTINOS"}
outside=[x for x in c if not x["id_destino"].startswith("BR-LEI-2015-13105-ART-0085-")]
assert len(outside)==1 and outside[0]["id_destino"]=="BR-LEI-2015-13105-ART-0077-C"
print("T24 F1-D13 OK: 45 pares distintos; 10 contexto caput, 8 grupos, 5 intervalo §11, 10 enumerados §20, uma externa art77.")
print("§11 repete §§2º e 3º em outra frase: ocorrências extras não são novos pares.")
