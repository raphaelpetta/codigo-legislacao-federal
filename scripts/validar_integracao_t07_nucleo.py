#!/usr/bin/env python3
"""Porta estrutural de F5-Q do T07. NÃO audita vigência, DOU, equivalência C0-J ou direito material."""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read_csv(path: str) -> list[dict[str, str]]:
    with (ROOT / path).open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def assert_ids(items: list[dict[str, str]], key: str, expected: int) -> None:
    ids = [x[key] for x in items]
    assert len(ids) == expected, (key, len(ids), expected)
    assert len(set(ids)) == expected, f"Duplicated ids in {key}"
    assert all(ids), f"Empty ID in {key}"


def read_section(path: str, start: str, end: str) -> str:
    full = (ROOT / path).read_text(encoding="utf-8")
    assert start in full and end in full, f"Missing section markers: {path}"
    return full.split(start, 1)[1].split(end, 1)[0]


def main() -> None:
    original = read_csv("modulos/T07/M03/CONCORDANCIA_INTEGRAL_ART1_ART2_13.csv")
    original40 = read_csv("modulos/T07/M03/CONCORDANCIA_LITERAL_ART3_17_15.csv")
    m22 = read_csv("integracao/05_CONCORDANCIA_T07_22_UNIDADES_20261014.csv")
    tests = read_csv("integracao/06_TESTES_ADVERSARIAIS_EXECUTADOS_T07_12.csv")
    m16 = read_csv("integracao/08_CONCORDANCIA_T07_SEGUNDO_NUCLEO_16_UNIDADES.csv")
    assert_ids(original, "id_unidade", 21)
    assert_ids(original40, "id_unidade", 40)
    assert_ids(m22, "id", 22)
    assert_ids(tests, "teste", 12)
    assert_ids(m16, "id_origem", 16)
    assert {t["teste"] for t in tests} == {f"G{i:02d}" for i in range(1, 13)}

    source = {r["id_unidade"]: r["texto_fonte_literal"] for r in original}
    main_norm = read_section(
        "integracao/03_PILOTO_T07_PRIMEIRO_NUCLEO_20261014.md",
        "## 2. Minuta F5-Q",
        "## 3. Concordância",
    )
    deltas = {}
    for row in m22:
        if row["id"] == "P19-69-C":
            assert row["origem"].lower().startswith("lei 9.784/1999 art. 69")
        else:
            assert row["id"] in source
            assert row["texto_origem"] == source[row["id"]]
        assert row["texto_destino"] in main_norm, row["id"]
        assert row["estado_juridico"] == "Q_SEM_C0_J", row["id"]
        assert row["homologacao"] if "homologacao" in row else True
        deltas[row["delta"]] = deltas.get(row["delta"], 0) + 1
    assert deltas == {
        "REFERENTE_LEI_PARA_LIVRO": 3,
        "PONTUACAO_HIFEN_PARA_DOIS_PONTOS": 3,
        "SEM_DELTA_LOCAL": 15,
        "REPOSICIONAMENTO_E_REFERENTE_LEI_PARA_LIVRO": 1,
    }, deltas
    assert all(x["homologacao_juridica"] == "Q_NAO_HOMOLOGADO" for x in tests)

    norm16 = read_section(
        "integracao/09_T07_DIREITOS_INTERESSADOS_COMPETENCIA_F5Q.md",
        "## 2. Minuta experimental",
        "## 3. Controles jurídico-materiais",
    )
    source40 = {r["id_unidade"]: r["texto_fonte_literal"] for r in original40}
    for row in m16:
        assert row["id_origem"] in source40
        assert row["texto_origem"] == source40[row["id_origem"]]
        assert row["texto_destino"] in norm16, row["id_origem"]
        assert row["classe"] == "C0_T_LOCAL;C0_J_Q"
        assert row["homologacao"] == "NAO"
    assert set(x["id_origem"].split("-")[1] for x in m16) == {"3", "4", "9", "11"}

    print("OK: 21 origens + art. 69 = 22 destinos, 12 testes, 16 unidades do bloco seguinte")
    print("IMPORTANTE: controle documental/estrutural, sem homologação de C0-J ou decisão DEC-016.")


if __name__ == "__main__":
    main()
