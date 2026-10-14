#!/usr/bin/env python3
"""T43 F1-I: 14 destinos de artigos alteradores; cinco já sobrescritos em 2023."""
import csv
from pathlib import Path
f=Path(__file__).resolve().parents[1]/"modulos/T43/M04/MATRIZ_F1I_14_DESTINOS_LEI14129_51_54.csv"
with f.open(encoding="utf-8-sig",newline="") as h:rows=list(csv.DictReader(h))
assert len(rows)==14 and len({r["id_destino"] for r in rows})==14,"14 destinos únicos obrigatórios"
assert {r["dispositivo_alterador"] for r in rows}=={"Lei14129 art51","Lei14129 art52","Lei14129 art53","Lei14129 art54"}
changed=[r for r in rows if r["situacao_no_texto_consolidado"]=="SUBSTITUIDA_2023"]
assert len(changed)==5,"cinco posições com ato posterior: 4 da Lei7116 e 1 da Lei13460"
assert {r["id_destino"] for r in changed}=={"Lei7116-art3-g","Lei7116-art3-P1","Lei7116-art3-P2","Lei7116-art3-P3","Lei13460-art10A-P1"}
assert all(r["status_clf"]=="Q_NAO_HOMOLOGADO" for r in rows)
assert all("Lei14534/2023" in r["alterador_texto_hoje"] for r in changed)
print("T43 F1-I OK: 14 destinos, 5 sobrescritos em 2023 e 9 sem alteração posterior identificada neste recorte, todos Q.")
