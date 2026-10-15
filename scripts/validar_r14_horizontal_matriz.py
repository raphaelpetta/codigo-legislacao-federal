#!/usr/bin/env python3
"""CLF R14: verificação documental de 4 novos recortes Q e 48 títulos.
Não autentica DOU nem homologa C0-J. Requer checkout completo dos arquivos.
"""
from __future__ import annotations
import csv
import hashlib
import io
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPECS = [
    ("produto/fontes/T01_M01_LINDB_7_R14_v1.json", 4, 7),
    ("produto/fontes/T08_M01_8112_5_R14_v1.json", 4, 5),
    ("produto/fontes/T20_M01_CDC_6_R14_v1.json", 3, 6),
    ("produto/fontes/T28_M01_CLT_14_R14_v1.json", 3, 14),
]


def check_source(manifest_path: str, articles: int, units: int) -> None:
    manifest = json.loads((ROOT / manifest_path).read_text(encoding="utf-8"))
    raw = (ROOT / manifest["source_path"]).read_bytes()
    git_sha = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
    assert git_sha == manifest["source_blob_sha"], manifest_path
    rows = list(csv.DictReader(io.StringIO(raw.decode("utf-8")), strict=True))
    assert len(rows) == units == manifest["count_expected"]
    assert len({r["id_origem"] for r in rows}) == units
    assert len({r["id_destino_simbolico"] for r in rows}) == units
    assert len({r["artigo"] for r in rows}) == articles == manifest["articles_expected"]
    assert sum(r["unidade"] == "C" for r in rows) == articles
    assert all(r["texto_fonte_editorial"] == r["texto_destino_documental"] for r in rows)
    assert all(r["estado_juridico"] == "Q_SEM_C0_J" for r in rows)
    assert all(r["classe_textual"] == "C0_T_CANDIDATO_SEM_DOU" for r in rows)
    assert manifest["dou_facsimile_checked"] is False
    assert manifest["material_approved"] is False and manifest["dec016"] == "PENDENTE"
    view = (ROOT / manifest["view_path"]).read_text(encoding="utf-8")
    assert view.count("**Art. ") == articles
    assert all(r["texto_destino_documental"] in view for r in rows)
    assert "NÃO RATIFICADA" in view and "C0-J=0" in view
    print(f"OK {manifest_path}: artigos {articles}, unidades {units}, SHA {git_sha}")


def check_corpus_and_matrix() -> None:
    idx = json.loads((ROOT / "produto/fontes/indice_livros.json").read_text(encoding="utf-8"))
    books = idx["livros"]
    assert len(books) == 20
    assert len({b["titulo"] for b in books}) == 11
    assert sum(b["artigos"] for b in books) == 204
    assert sum(b["registros_documentais"] for b in books) == 638
    texts = defaultdict(lambda: [0, 0])
    for b in books:
        texts[b["titulo"]][0] += b["artigos"]
        texts[b["titulo"]][1] += b["registros_documentais"]
    texts["T07"][1] -= 1  # Registro histórico, não positivo.
    assert sum(v[1] for v in texts.values()) == 637
    with (ROOT / "central/01_MATRIZ_AUDITORIA_48_TITULOS_20261015.csv").open(
        encoding="utf-8", newline=""
    ) as fd:
        matrix = list(csv.DictReader(fd))
    assert len(matrix) == 48
    assert len({r["id_titulo"] for r in matrix}) == 48
    for r in matrix:
        a, u = texts.get(r["id_titulo"], [0, 0])
        assert int(r["artigos_na_vista"]) == a, r["id_titulo"]
        assert int(r["unidades_positivas_na_vista"]) == u, r["id_titulo"]
        assert r["C0_J_homologadas"] == "0"
    assert sum(int(r["artigos_na_vista"]) for r in matrix) == 204
    assert sum(int(r["unidades_positivas_na_vista"]) for r in matrix) == 637
    assert sum(int(r["artigos_na_vista"]) > 0 for r in matrix) == 11
    print("OK matriz: 48 títulos, 11 positivos, 37 sem texto, 204 artigos, 637 unidades.")


if __name__ == "__main__":
    for args in SPECS:
        check_source(*args)
    check_corpus_and_matrix()
    print("OK R14 documental: C0-J não aferido juridicamente; CI precisa ser executado.")
