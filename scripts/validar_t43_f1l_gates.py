#!/usr/bin/env python3
"""F1-L — gates jurídicos e preservação das 14 subunidades de destino.

Não transforma o cotejo textual F1-J/K em C0-J. Uma classificação de
risco jurídico é um insumo para parecer humano sobre a futura forma legal.
"""
import csv
from collections import Counter
from pathlib import Path
B=Path(__file__).resolve().parents[1]/"modulos/T43/M04"
def read(name):
    with (B/name).open(encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f))
old=read("MATRIZ_F1I_14_DESTINOS_LEI14129_51_54.csv")
gates=read("MATRIZ_F1L_GATES_JURIDICOS_14_DESTINOS.csv")
five=read("F1J_COTEJO_LITERAL_5_POSICOES_2021_2023.csv")
nine=read("F1K_NOVE_DESTINOS_LITERAL_2021_2026.csv")
ids={r["id_destino"] for r in old}
assert len(ids)==14 and len(old)==14
assert len(gates)==14 and len({r["id_destino"] for r in gates})==14
assert {r["id_destino"] for r in gates}==ids,"Perda de unidades de destino"
id5={r["id_destino"] for r in five}
id9={r["id_destino"] for r in nine}
assert len(id5)==5 and len(id9)==9 and id5.isdisjoint(id9) and id5|id9==ids
for r in gates:
    k=r["id_destino"]
    assert r["redacao_pos_lei14534"]==("REDACAO_2023" if k in id5 else "REDACAO_2021"),k
    assert r["estado_c0j"]=="Q_REQUIRES_REVISAO_JURIDICA"
    assert r["estrategia_normativa_provisoria"].startswith("SE_PRESERVAR_NA_LEI_")
    assert r["competencia_a_examinar"] and r["perda_que_deve_ser_evitar"]
    assert r["gate_auditoria"] and r["risco_material"]
assert "LGPD" in next(r for r in gates if r["id_destino"]=="Lei7116-art3-P2")["gate_auditoria"]
for k in ("Lei12527-art12-C","Lei12527-art12-P1","Lei12527-art12-P2"):
    assert "ALTO" in next(r for r in gates if r["id_destino"]==k)["risco_material"]
assert "COMPETENCIA" in next(r for r in gates if r["id_destino"]=="Lei13460-art10A-P3")["gate_auditoria"]
print("T43 F1-L OK: 14/14 destinos identificados, 5 redações de 2023 e 9 de 2021, todos Q jurídicos.")
print("Quatro leis de destino; garantias de LAI, LGPD/biometria, CPF, assinatura e autonomia federativa protegidas como gates.")
