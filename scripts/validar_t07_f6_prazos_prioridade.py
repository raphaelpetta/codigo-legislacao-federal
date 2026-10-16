#!/usr/bin/env python3
"""Validação estrutural do T07 arts. 66–69-A e encerramento documental 48–69-A.

NÃO autentica DOU, não substitui auditoria jurídica e NÃO homologa C0-J.
"""
import csv
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
D = ROOT / "integracao"

def read(name):
    with (D / name).open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

originals = read("25_T07_CONCORDANCIA_TOTAL_215_F5Q_V4.csv")
gate = read("45_T07_MATRIZ_GATE_13_UNIDADES_PRAZOS_PRIORIDADE_20261015.csv")
tests = read("46_T07_TESTES_PRAZOS_ESPECIALIDADE_PRIORIDADE_33_20261015.csv")
veto = read("47_T07_VETOS_2009_ART69A_NAO_APRECIADOS_20261015.csv")
ids = {x["id_fonte"]: x for x in originals}
book = (D / "26_T07_LIVRO_COMPLETO_1_69A_F5Q_V4.md").read_text(encoding="utf-8")
assert len(originals) == len(ids) == 215
assert len(gate) == len({x["id_fonte"] for x in gate}) == 13
assert len(tests) == len({x["id"] for x in tests}) == 33
assert len(veto) == len({x["id_veto_cn"] for x in veto}) == 3
assert {x["artigo"] for x in gate} == {"66","67","68","69","69-A"}
assert {x["destino_ensaio"] for x in gate} == {
    "LPA-SEQ4-074-C", "LPA-SEQ4-074-P1", "LPA-SEQ4-074-P2", "LPA-SEQ4-074-P3",
    "LPA-SEQ4-075-C", "LPA-SEQ4-076-C", "LPA-SEQ4-077-C",
    "LPA-SEQ4-078-C", "LPA-SEQ4-078-I", "LPA-SEQ4-078-II",
    "LPA-SEQ4-078-IV", "LPA-SEQ4-078-P1", "LPA-SEQ4-078-P2",
}
changes = []
for row in gate:
    a = ids[row["id_fonte"]]
    assert a["artigo_origem"] == row["artigo"], row["id_fonte"]
    assert a["subunidade_origem"] == row["unidade"], row["id_fonte"]
    assert a["destino_experimental"] == row["destino_ensaio"]
    assert a["texto_destino_experimental"] in book, row["id_fonte"]
    assert a["status_juridico"] == row["equivalencia_juridica"] == "Q_SEM_C0_J"
    assert row["situacao"] == "NAO_APROVADO_NAO_PROMULGADO"
    assert row["problema_gate"] and row["testes_adversariais"] and row["direito_externo"]
    assert row["fonte_oficial"].startswith("https://")
    if a["delta_local"] == "SEM_DELTA_LOCAL":
        assert row["categoria_preliminar"] == "C0_T_APENAS_Q"
        assert a["texto_fonte_arquivado"] == a["texto_destino_experimental"]
    else:
        changes.append(row["id_fonte"])
        assert row["categoria_preliminar"] == "C1_POTENCIAL_REMISSAO_Q"
assert changes == ["P19-69-C"], changes
assert ids["P19-69-C"]["texto_fonte_arquivado"].endswith("desta Lei.")
assert ids["P19-69-C"]["texto_destino_experimental"].endswith("deste Livro.")
assert [x["id"] for x in tests] == [f"G{i:02d}" for i in range(1,34)]
assert all(x["natureza_prova"] == "SIMULACAO_JURIDICA_SEM_AUTOS_CONCRETOS" for x in tests)
assert {x["id_veto_cn"] for x in veto} == {"31.09.004","31.09.005","31.09.006"}
assert {x["unidade"] for x in veto} == {"III","P3","P4"}
assert all(x["registro_status_20261015"] == "VETO_APOSTO_2009_EM_TRAMITACAO"
           and x["resultado_apreciacao"] == "NAO_APRECIADO"
           and x["integracao_clf"] == "HISTORICO_NAO_PROMULGADO_SEM_MERGE" for x in veto)
assert "§ 3º" not in book.split("**Art. LPA-SEQ4-078.**",1)[1].split("## XVI.",1)[0]
assert "§ 4º" not in book.split("**Art. LPA-SEQ4-078.**",1)[1].split("## XVI.",1)[0]

earlier = [a for a in originals if a["artigo_origem"].isdigit() and int(a["artigo_origem"]) <= 47]
history = [a for a in originals if a["artigo_origem"] == "70"]
assert len(earlier) == 122
assert len(history) == 1 and history[0]["destino_experimental"] == "HIST-LEI9784-ART70"
assert len(originals) - len(earlier) - len(history) == 92

report = (D / "48_T07_PARECER_PRAZOS_SANCOES_ESPECIALIDADE_PRIORIDADE_20261015.md").read_text(encoding="utf-8")
alts = (D / "49_T07_MODELOS_PRAZOS_ESPECIALIDADE_PRIORIDADE_20261015.md").read_text(encoding="utf-8")
handoff = (D / "50_T07_CONTINUIDADE_20261015_RODADA10.md").read_text(encoding="utf-8")
for marker in ("31.09.004", "31.09.005", "31.09.006", "não apreciados",
               "Lei Brasileira de Inclusão", "DEC-016"):
    assert marker in report, marker
for marker in ("## R0", "## R1", "## R2", "## R3", "## R4", "## R5"):
    assert marker in alts, marker
assert "122 unidades positivas" in handoff
assert "92 unidades" in handoff
print("T07 F6 final: 13 unidades Q (12 C0-T, 1 C1), 33 testes, 3 itens VET31 NAO APRECIADOS; 92 F6 / 122 previas +1 historica =215; 0 C0-J.")
