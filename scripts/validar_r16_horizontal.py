#!/usr/bin/env python3
"""CLF R16 — valida fontes Q, matriz, painel e montagem. Não certifica DOU nem C0-J."""
from __future__ import annotations
import csv
import hashlib
import io
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NEW = [
    ("produto/fontes/T11_M01_4320_11_R16_v1.json", 2, 11),
    ("produto/fontes/T22_M01_9610_5_R16_v1.json", 4, 5),
    ("produto/fontes/T31_M01_8080_6_R16_v1.json", 3, 6),
    ("produto/fontes/T08_M01_8112_10_R16_v1.json", 1, 10),
]


def verify_one(path: str, expected_arts: int, expected_units: int) -> None:
    mf = json.loads((ROOT / path).read_text(encoding="utf-8"))
    raw = (ROOT / mf["source_path"]).read_bytes()
    digest = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
    assert digest == mf["source_blob_sha"], path
    records = list(csv.DictReader(io.StringIO(raw.decode("utf-8")), strict=True))
    assert len(records) == expected_units == mf["count_expected"]
    assert sum(r["unidade"] == "C" for r in records) == expected_arts
    assert len({r["artigo"] for r in records}) == expected_arts == mf["articles_expected"]
    assert len({r["id_origem"] for r in records}) == expected_units
    assert len({r["id_destino_simbolico"] for r in records}) == expected_units
    assert all(r["texto_fonte_editorial"] == r["texto_destino_documental"] for r in records)
    assert all(r["estado_juridico"] == "Q_SEM_C0_J" for r in records)
    assert all(r["classe_textual"] == "C0_T_CANDIDATO_SEM_DOU" for r in records)
    assert not mf["dou_facsimile_checked"] and not mf["material_approved"]
    assert mf["dec016"] == "PENDENTE"
    view = (ROOT / mf["view_path"]).read_text(encoding="utf-8")
    assert view.count("**Art. ") == expected_arts
    assert all(r["texto_destino_documental"] in view for r in records)
    assert "NÃO RATIFICADA" in view and "C0-J=0" in view
    print(f"OK {path}: {expected_arts} artigos/{expected_units} unidades; SHA={digest}")


def verify_index_code_matrix() -> None:
    idx = json.loads((ROOT / "produto/fontes/indice_livros.json").read_text(encoding="utf-8"))
    books = idx["livros"]
    assert len(books) == 28
    assert len({b["titulo"] for b in books}) == 17
    assert sum(b["artigos"] for b in books) == 226
    assert sum(b["registros_documentais"] for b in books) == 714
    totals = defaultdict(lambda: [0, 0, 0])
    for b in books:
        totals[b["titulo"]][0] += b["artigos"]
        totals[b["titulo"]][1] += b["registros_documentais"]
        totals[b["titulo"]][2] += 1
    totals["T07"][1] -= 1  # Histórico fora das unidades positivas.
    with (ROOT / "central/01_MATRIZ_AUDITORIA_48_TITULOS_20261015.csv").open(
        encoding="utf-8", newline=""
    ) as fd:
        matrix = list(csv.DictReader(fd))
    assert len(matrix) == 48
    assert len({r["id_titulo"] for r in matrix}) == 48
    for r in matrix:
        a, u, _ = totals.get(r["id_titulo"], [0, 0, 0])
        assert int(r["artigos_na_vista"]) == a
        assert int(r["unidades_positivas_na_vista"]) == u
        assert int(r["C0_J_homologadas"]) == 0
    assert sum(int(r["artigos_na_vista"]) for r in matrix) == 226
    assert sum(int(r["unidades_positivas_na_vista"]) for r in matrix) == 713
    assert sum(int(r["artigos_na_vista"]) > 0 for r in matrix) == 17
    with (ROOT / "central/PAINEL_GERADO.csv").open(encoding="utf-8", newline="") as fd:
        panel = list(csv.DictReader(fd))
    assert len(panel) == 48
    for r in panel:
        a, u, n = totals.get(r["id_titulo"], [0, 0, 0])
        assert int(r["livros_em_vista"]) == n
        assert int(r["artigos_experimentais"]) == a
        assert int(r["registros_documentais_na_fonte"]) == u + (1 if r["id_titulo"] == "T07" else 0)
    code = (ROOT / "produto/CODIGO_DE_TRABALHO.md").read_text(encoding="utf-8")
    assert sum(line.startswith("**Art. ") for line in code.splitlines()) == 226
    for b in books:
        title = f"## {b['titulo']} — {b['modulo']} [{b['id']}; {b['estado']}]"
        assert title in code
        assert (ROOT / b["vista"]).read_text(encoding="utf-8").strip() in code
    print("OK corpus R16: 17 títulos, 28 componentes, 226 artigos, 713 unidades Q e um histórico.")


if __name__ == "__main__":
    for item in NEW:
        verify_one(*item)
    verify_index_code_matrix()
    print("OK integridade documental, NÃO HOMOLOGADO (DOU/CI/C0-J).")
