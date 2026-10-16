#!/usr/bin/env python3
"""T24 F1-D12: prevenir subcontagem do grafo por dependencias em §4 I/II."""
import csv
from pathlib import Path
root=Path(__file__).resolve().parents[1]/"modulos/T24/M01"
def load(p):
    with (root/p).open(encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f))
base=load("GRAFO_F1D7_REMISSOES_EXPRESSAS_ART85.csv")
new=load("MATRIZ_F1D12_DEZ_REMISSOES_P4_INCISOS.csv")
old={(x["id_origem"],x["id_destino_original"]) for x in base}
added={(x["id_fonte"],x["id_destino"]) for x in new}
assert len(base)==35 and len(old)==35
assert len(new)==10 and len(added)==10
assert not (old & added),"Remissão adicional já estava no grafo antigo"
assert len(old|added)==45,"45 pares distintos previstos para esta cobertura ampliada"
ids=lambda u:f"BR-LEI-2015-13105-ART-0085-{u}"
required={(ids(s),ids(f"P3-{i}")) for s in ("P4-I","P4-II") for i in ("I","II","III","IV","V")}
assert added==required
assert all(x["status"]=="Q_CONFIRMAR_DIREITO" for x in new)
print("T24 F1-D12 OK: grafo anterior 35 pares + 10 adicionais = 45 pares distintos, contextuais, C0-J Q.")
print("Duas citações repetidas de §§2-3 no §11 não são pares novos; a contagem não afirma exaustividade.")
