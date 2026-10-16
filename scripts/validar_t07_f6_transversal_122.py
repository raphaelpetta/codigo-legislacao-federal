#!/usr/bin/env python3
"""Validação DOCUMENTAL F6-Q do bloco 1–47; não certifica equivalência jurídica."""
import csv
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
D = ROOT / "integracao"

def read_csv(name):
    with (D / name).open(encoding="utf-8", newline="") as fd:
        return list(csv.DictReader(fd))

all_sources = read_csv("25_T07_CONCORDANCIA_TOTAL_215_F5Q_V4.csv")
matrix = read_csv("51_T07_GATE_TRANSVERSAL_122_ART1_47_20261015.csv")
tests = read_csv("52_T07_TESTES_TRANSVERSAIS_59_ART1_47_20261015.csv")
book = (D / "26_T07_LIVRO_COMPLETO_1_69A_F5Q_V4.md").read_text(encoding="utf-8")
by_id = {x["id_fonte"]: x for x in all_sources}
assert len(by_id) == len(all_sources) == 215
assert len(matrix) == 122
assert len({x["id_fonte"] for x in matrix}) == 122
assert {int(x["artigo_origem"]) for x in matrix} == set(range(1, 48))
assert len(tests) == 59
assert [r["id"] for r in tests] == [f"F11-{i:03d}" for i in range(1, 60)]
assert [r["escopo"] for r in tests[:47]] == [f"ART_{i}" for i in range(1, 48)]
assert all(r["escopo"] == "TRANSVERSAL" for r in tests[47:])
assert all(r["natureza_prova"] == "TESTE_INTERPRETATIVO_HIPOTETICO_NAO_CASO_REAL"
           for r in tests)
assert all(r["hipotese_hipotetica"] and r["resposta_cautelar"] and r["fundamento_e_limitacao"]
           for r in tests)
kinds = Counter()
risks = Counter()
changes = []
for x in matrix:
    orig = by_id[x["id_fonte"]]
    assert orig["artigo_origem"] == x["artigo_origem"]
    assert orig["subunidade_origem"] == x["unidade"]
    assert orig["destino_experimental"] == x["destino_ensaio"]
    assert orig["texto_destino_experimental"] in book, x["id_fonte"]
    assert orig["status_juridico"] == x["gate_juridico"] == "Q_SEM_C0_J"
    assert x["estado_trabalho"] == "NAO_APROVADO_NAO_PROMULGADO"
    assert x["nivel_prova"] == "TRIAGEM_F6_DOCUMENTAL_FONTES_PRIMARIAS_GATES_PENDENTES"
    assert x["questao_material"] and x["controle_especifico"] and x["direito_externo"]
    assert x["fonte_lei_base"] == orig["fonte_matriz"]
    cat = x["categoria_triangulacao"]
    kinds[cat] += 1
    risks[x["prioridade_risco"]] += 1
    if orig["texto_fonte_arquivado"] == orig["texto_destino_experimental"]:
        assert x["delta_lexical"] == "SEM_DELTA_LOCAL"
        assert cat == "C0_T_LOCAL_Q"
    else:
        changes.append(x["id_fonte"])
        if x["id_fonte"] in ("P13-01-P2-I", "P13-01-P2-II", "P13-01-P2-III"):
            assert x["delta_lexical"] == "HIFEN_PARA_DOIS_PONTOS"
            assert cat == "C1_PONTUACAO_EDITORIAL_Q"
        else:
            assert x["delta_lexical"] == "DESTA_LEI_PARA_DESTE_LIVRO"
            assert cat == "C1_REFERENTE_LEI_LIVRO_Q"
assert kinds == Counter({
    "C0_T_LOCAL_Q": 115,
    "C1_REFERENTE_LEI_LIVRO_Q": 4,
    "C1_PONTUACAO_EDITORIAL_Q": 3,
}), kinds
assert risks == Counter({"CRITICO":39, "ALTO":61, "MEDIO":22}), risks
assert set(changes) == {
    "P13-01-C", "P13-01-P1", "P13-01-P2",
    "P13-01-P2-I", "P13-01-P2-II", "P13-01-P2-III",
    "EXP17-36-C",
}
earlier = [x for x in all_sources if x["artigo_origem"].isdigit() and
           int(x["artigo_origem"]) <= 47]
historical = [x for x in all_sources if x["artigo_origem"] == "70"]
assert len(earlier) == 122
assert len(historical) == 1 and historical[0]["destino_experimental"] == "HIST-LEI9784-ART70"
assert len(all_sources) - len(earlier) - len(historical) == 92

report = (D / "53_T07_PARECER_TRANSVERSAL_ART1_47_20261015.md").read_text(encoding="utf-8")
alternatives = (D / "54_T07_MODELOS_TRANSVERSAIS_ART1_47_20261015.md").read_text(encoding="utf-8")
handoff = (D / "55_T07_CONTINUIDADE_20261015_RODADA11.md").read_text(encoding="utf-8")
for expected in ("DEC-016","Lei 13.726/2018","Lei 14.129/2021","LGPD", "Arts.36–37", "Arts.42–43",
                 "115", "122", "39", "59"):
    assert expected in report, expected
for r in range(7):
    assert f"## R{r}" in alternatives
assert "39 CRÍTICAS" in handoff
assert "CI" in handoff
print("T07 F6 1-47: 122/122; 115 C0-T, 4 referentes, 3 pontuacoes, 59 testes, prioridade 39/61/22; 92+122=214 positivos; 1 vigencia historica; NENHUM C0-J.")
