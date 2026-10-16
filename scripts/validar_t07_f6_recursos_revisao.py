#!/usr/bin/env python3
"""Validação puramente documental do T07 arts. 56–65: não certifica direito vigente."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
D = ROOT / "integracao"

def read(name):
    with (D / name).open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

sources = read("25_T07_CONCORDANCIA_TOTAL_215_F5Q_V4.csv")
gate = read("40_T07_MATRIZ_30_UNIDADES_RECURSOS_REVISAO_20261015.csv")
scenarios = read("41_T07_TESTES_RECURSOS_REVISAO_32_20261015.csv")

by_id = {x["id_fonte"]: x for x in sources}
assert len(sources) == len(by_id) == 215, "Registros principais duplicados/ausentes"
assert len(gate) == 30
assert len(scenarios) == 32
assert len({r["id_fonte"] for r in gate}) == 30
assert len({r["destino_v4"] for r in gate}) == 30

arts = {"56", "57", "58", "59", "60", "61", "62", "63",
        "64", "64-A", "64-B", "65"}
assert {r["artigo_origem"] for r in gate} == arts

book = (D / "26_T07_LIVRO_COMPLETO_1_69A_F5Q_V4.md").read_text(encoding="utf-8")
for item in gate:
    ident = item["id_fonte"]
    a = by_id[ident]
    assert a["destino_experimental"] == item["destino_v4"], ident
    assert a["artigo_origem"] == item["artigo_origem"], ident
    assert a["subunidade_origem"] == item["unidade"], ident
    assert a["texto_fonte_arquivado"] == a["texto_destino_experimental"], ident
    assert a["texto_destino_experimental"] in book, ident
    assert a["delta_local"] == "SEM_DELTA_LOCAL", ident
    assert a["status_juridico"] == item["equivalencia_juridica"] == "Q_SEM_C0_J"
    assert item["classe_textual"] == "C0_T_LOCAL"
    assert item["estado_reforma"] == "NAO_APROVADO_NAO_PROMULGADO"
    assert item["risco"] in ("MEDIO", "ALTO", "CRITICO")
    assert item["quesito_juridico_f6"] and item["testes_relevantes"]
    assert item["fonte_normativa"].startswith("https://")
    assert item["direito_externo"] and item["grupo"]

assert [x["id"] for x in scenarios] == [f"R{i:02d}" for i in range(1, 33)]
assert all(x["hipotese_hipotetica"] and x["fundamento_e_limite"] and
           x["status_prova"] == "TESTE_JURIDICO_DOCUMENTAL_SEM_CASO_REAL"
           for x in scenarios)
assert all(x["conclusao_condicional"] for x in scenarios)

report = (D / "42_T07_PARECER_RECURSOS_REVISAO_20261015.md").read_text(encoding="utf-8")
alts = (D / "43_T07_ALTERNATIVAS_RECURSO_E_REVISAO_20261015.md").read_text(encoding="utf-8")
handoff = (D / "44_T07_CONTINUIDADE_20261015_RODADA09.md").read_text(encoding="utf-8")
for expected in ("Súmula Vinculante 21", "RMS 21.981", "MS 11.554",
                 "64-A", "64-B", "DEC-016", "dias úteis"):
    assert expected in report, expected
for name in ("## R0", "## R1", "## R2", "## R3", "## R4", "## R5"):
    assert name in alts, name
for marker in ("C0-J=0", "32 testes", "DEC-016"):
    assert marker in handoff, marker

print("T07 F6 recursos: 30/30 sem delta lexical, 32 testes hipotéticos, seis alternativas, 0 C0-J e 0 reforma aprovada.")
