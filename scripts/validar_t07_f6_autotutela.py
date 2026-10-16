#!/usr/bin/env python3
"""Validação de estrutura F6 T07 art. 51–55; NÃO certifica equivalência jurídica."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
D = ROOT / "integracao"

def load(file):
    with (D / file).open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))

base = load("25_T07_CONCORDANCIA_TOTAL_215_F5Q_V4.csv")
gate = load("36_T07_MATRIZ_GATE_9_UNIDADES_AUTOTUTELA_20261015.csv")
tests = load("37_T07_TESTES_AUTOTUTELA_22_20261015.csv")
assert len(base) == 215
base_by_id = {x["id_fonte"]: x for x in base}
assert len(base_by_id) == 215, "Duplicidade no indice T07"

ids = ["C19-51-C", "C19-51-P1", "C19-51-P2",
       "C19-52-C", "C19-53-C",
       "C19-54-C", "C19-54-P1", "C19-54-P2",
       "C19-55-C"]
assert len(gate) == len(ids) == 9
assert [x["id_fonte"] for x in gate] == ids
assert {x["destino_experimental"] for x in gate} == {
    "LPA-SEQ4-057-C", "LPA-SEQ4-057-P1", "LPA-SEQ4-057-P2",
    "LPA-SEQ4-058-C", "LPA-SEQ4-059-C",
    "LPA-SEQ4-060-C", "LPA-SEQ4-060-P1", "LPA-SEQ4-060-P2",
    "LPA-SEQ4-061-C",
}

book = (D / "26_T07_LIVRO_COMPLETO_1_69A_F5Q_V4.md").read_text(encoding="utf-8")
for x in gate:
    original = base_by_id[x["id_fonte"]]
    assert original["texto_fonte_arquivado"] == original["texto_destino_experimental"], x["id_fonte"]
    assert original["texto_destino_experimental"] in book, x["id_fonte"]
    assert original["delta_local"] == "SEM_DELTA_LOCAL", x["id_fonte"]
    assert original["destino_experimental"] == x["destino_experimental"]
    assert original["status_juridico"] == "Q_SEM_C0_J"
    assert x["classe_textual"] == "C0_T_SEM_DELTA_C0_J_Q"
    assert x["gate_juridico"] == "Q_SEM_HOMOLOGACAO"
    assert x["deliberacao_material"] == "M_NAO_DELIBERADA"
    assert x["problema_juridico"] and x["cenarios"] and x["interfaces"]
    assert x["fonte_principal"].startswith("https://")

assert len(tests) == 22
assert [x["id"] for x in tests] == [f"D{i:02d}" for i in range(1, 23)]
assert all(x["prova"] == "TESTE_HIPOTETICO_SEM_AUTOS_CONCRETOS" for x in tests)
assert all(x["razao_e_limite"] and x["base_normativa"] for x in tests)

report = (D / "35_T07_AUDITORIA_ART51_55_LINDB_20261015.md").read_text(encoding="utf-8")
alts = (D / "38_T07_ALTERNATIVAS_AUTOTUTELA_LINDB_20261015.md").read_text(encoding="utf-8")
handoff = (D / "39_T07_CONTINUIDADE_20261015_RODADA08.md").read_text(encoding="utf-8")
for tag in ("Tema 138", "Tema 445", "Tema 839", "Súmula 633", "103-A"):
    assert tag in report, tag
for tag in ("## R0", "## R1", "## R2", "## R3", "SEM APROVAÇÃO"):
    assert tag in alts, tag
assert "C0-J=**0 homologado**" in handoff
assert "DEC-016" in report and "DEC-016" in handoff

print("T07 F6 autotutela: 9/9 C0-T Q, 22 cenarios hipoteticos, 4 modelos nao aprovados; nenhuma homologacao.")
