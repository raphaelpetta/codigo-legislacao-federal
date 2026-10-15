#!/usr/bin/env python3
"""R11: integridade documental dos espelhos Q; nunca homologa fonte DOU/C0-J."""
from __future__ import annotations
import csv
import hashlib
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFESTS = [
    ("produto/fontes/T28_M01_CLT_7_R11_v1.json", 3, 7),
    ("produto/fontes/T37_M01_6938_19_R11_v1.json", 2, 19),
    ("produto/fontes/T48_M03_9474_8_R11_v1.json", 5, 8),
]


def check(path: str, expected_articles: int, expected_records: int) -> None:
    manifest = json.loads((ROOT / path).read_text(encoding="utf-8"))
    source = (ROOT / manifest["source_path"]).read_bytes()
    git_sha = hashlib.sha1(b"blob " + str(len(source)).encode() + b"\0" + source).hexdigest()
    assert git_sha == manifest["source_blob_sha"], f"Blob divergente: {path}"
    rows = list(csv.DictReader(io.StringIO(source.decode("utf-8")), strict=True))
    assert len(rows) == expected_records == manifest["count_expected"], path
    caputs = [row for row in rows if row["unidade"] == "C"]
    assert len(caputs) == expected_articles == manifest["articles_expected"], path
    assert len(set(row["artigo"] for row in rows)) == expected_articles, path
    assert len(set(row["id_origem"] for row in rows)) == expected_records, path
    assert len(set(row["id_destino_simbolico"] for row in rows)) == expected_records, path
    assert all(row["texto_fonte_editorial"] == row["texto_destino_documental"] for row in rows)
    assert all(row["estado_juridico"] == "Q_SEM_C0_J" for row in rows)
    assert all(row["classe_textual"] == "C0_T_CANDIDATO_SEM_DOU" for row in rows)
    assert manifest["dou_facsimile_checked"] is False
    assert manifest["material_approved"] is False and manifest["dec016"] == "PENDENTE"
    view = (ROOT / manifest["view_path"]).read_text(encoding="utf-8")
    assert view.count("**Art. ") == expected_articles
    assert all(row["texto_destino_documental"] in view for row in rows)
    assert "NÃO RATIFICADA" in view and "C0-J" in view
    print(f"OK R11 {path}: {expected_articles} artigos; {expected_records} unidades; SHA {git_sha}")


if __name__ == "__main__":
    for args in MANIFESTS:
        check(*args)
    print("OK R11 total incremental: 10 artigos e 34 unidades Q; nenhuma equivalência jurídica certificada")
