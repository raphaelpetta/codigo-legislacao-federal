#!/usr/bin/env python3
"""Auditoria de integridade documental do bloco T07 arts. 48–50, sem certificação jurídica."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
D = ROOT / "integracao"
def read(name):
    with (D / name).open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

gates = read("30_T07_MATRIZ_GATE_40_UNIDADES_20261015.csv")
vetos = read("31_T07_VETOS_9_ITENS_CONGRESSO_20261015.csv")
cases = read("33_T07_TESTES_ADVERSARIAIS_18_20261015.csv")
all_units = read("25_T07_CONCORDANCIA_TOTAL_215_F5Q_V4.csv")
by_id = {item["id_fonte"]: item for item in all_units}
assert len(all_units) == len(by_id) == 215
assert len(gates) == 40, f"Unidades auditadas incorretas: {len(gates)}"
assert len(vetos) == 9, f"Unidades vetadas incorretas: {len(vetos)}"
assert len(cases) == 18, f"Testes adversariais incorretos: {len(cases)}"
assert len({g["id_origem"] for g in gates}) == 40
assert len({g["destino_v4"] for g in gates}) == 40
assert len({x["id_veto_congresso"] for x in vetos}) == 9
assert len({x["id"] for x in cases}) == 18
assert {x["id"] for x in cases} == {f"A{i:02d}" for i in range(1, 19)}
changed = []
for row in gates:
    orig = by_id[row["id_origem"]]
    assert orig["destino_experimental"] == row["destino_v4"]
    assert orig["status_juridico"] == "Q_SEM_C0_J"
    assert row["situacao_C0J"] == "Q_PENDENTE_NAO_HOMOLOGADO"
    assert row["fonte_oficial"].startswith("https://")
    assert row["classificacao_local"] in ("C0_T_CANDIDATA_SEM_JURIDICO", "C1_POTENCIAL_REFERENTE_Q")
    assert row["risco_juridico"] in ("ALTO", "MEDIO", "BAIXO")
    assert row["gate_auditoria"]
    if row["classificacao_local"] == "C1_POTENCIAL_REFERENTE_Q":
        changed.append(row["id_origem"])
assert changed == ["C18-49-A-P1", "C18-49-B-C", "C18-49-D-C"], changed
assert all(x["resultado_congresso"] == "VETO_MANTIDO" for x in vetos)
assert {x["id_veto_congresso"] for x in vetos} == {f"54.21.{i:03d}" for i in range(1, 10)}
assert all(x["tratamento_clf"] == "HISTORICO_SEM_EFEITO_NORMATIVO" for x in vetos)
assert all(x["estado_prova"] == "TESTE_NORMATIVO_NAO_CASO_REAL" for x in cases)

report = (D / "29_T07_AUDITORIA_JURIDICA_DECISAO_MOTIVACAO_20261015.md").read_text(encoding="utf-8")
alternatives = (D / "32_T07_ALTERNATIVAS_CONVOCACAO_ATA_20261015.md").read_text(encoding="utf-8")
assert "DEC-016" not in alternatives or "NÃO" in alternatives
assert all(label in alternatives for label in ("## R0", "## M1", "## M2", "Art. DC-PROP-01.", "Art. DC-PROP-02."))
assert "40/40" in report and "Nove itens veto mantidos" in report
print("T07 F6: 40/40 origens Q, 3 referentes C1/Q, 9 vetos mantidos, 18 contraprovas, alternativas R0/M1/M2 não aprovadas.")
