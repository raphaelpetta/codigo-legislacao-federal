#!/usr/bin/env python3
"""CLF R15: integridade documental do corpus; sem declaração de autenticidade do DOU ou C0-J."""
from __future__ import annotations
import csv
import hashlib
import io
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NEW_SOURCES = [
    ("produto/fontes/T09_M01_14133_11_R15_v1.json", 2, 11),
    ("produto/fontes/T12_M01_CTN_7_R15_v1.json", 5, 7),
    ("produto/fontes/T43_M01_LGPD_16_R15_v1.json", 3, 16),
    ("produto/fontes/T25_M01_CP_10_R15_v1.json", 2, 10),
]


def verify_source(path: str, articles: int, units: int) -> None:
    m = json.loads((ROOT / path).read_text(encoding="utf-8"))
    raw = (ROOT / m["source_path"]).read_bytes()
    git_sha = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
    assert git_sha == m["source_blob_sha"], f"Git blob alterado: {path}"
    records = list(csv.DictReader(io.StringIO(raw.decode("utf-8")), strict=True))
    assert len(records) == units == m["count_expected"]
    assert len({x["id_origem"] for x in records}) == units
    assert len({x["id_destino_simbolico"] for x in records}) == units
    assert len({x["artigo"] for x in records}) == articles == m["articles_expected"]
    assert sum(x["unidade"] == "C" for x in records) == articles
    assert all(x["texto_fonte_editorial"] == x["texto_destino_documental"] for x in records)
    assert all(x["estado_juridico"] == "Q_SEM_C0_J" for x in records)
    assert all(x["classe_textual"] == "C0_T_CANDIDATO_SEM_DOU" for x in records)
    assert m["dou_facsimile_checked"] is False
    assert m["material_approved"] is False and m["dec016"] == "PENDENTE"
    view = (ROOT / m["view_path"]).read_text(encoding="utf-8")
    assert view.count("**Art. ") == articles
    assert all(x["texto_destino_documental"] in view for x in records)
    assert "NÃO RATIFICADA" in view and "C0-J=0" in view
    print(f"OK {path}: artigos {articles}, unidades {units}, SHA {git_sha}")


def verify_index_matrix_and_code() -> None:
    idx = json.loads((ROOT / "produto/fontes/indice_livros.json").read_text(encoding="utf-8"))
    b = idx["livros"]
    assert len(b) == 24 and len({x["titulo"] for x in b}) == 14
    assert sum(x["artigos"] for x in b) == 216
    assert sum(x["registros_documentais"] for x in b) == 682
    values = defaultdict(lambda: [0, 0])
    for v in b:
        values[v["titulo"]][0] += v["artigos"]
        values[v["titulo"]][1] += v["registros_documentais"]
    values["T07"][1] -= 1
    expected = (ROOT / "produto/CODIGO_DE_TRABALHO.md").read_text(encoding="utf-8")
    assert expected.count("**Art. ") == 216
    for v in b:
        header = f"## {v['titulo']} — {v['modulo']} [{v['id']}; {v['estado']}]"
        assert header in expected
        body = (ROOT / v["vista"]).read_text(encoding="utf-8").strip()
        assert body in expected
    with (ROOT / "central/01_MATRIZ_AUDITORIA_48_TITULOS_20261015.csv").open(encoding="utf-8", newline="") as fd:
        rows = list(csv.DictReader(fd))
    assert len(rows) == 48
    assert len({x["id_titulo"] for x in rows}) == 48
    for x in rows:
        a, u = values.get(x["id_titulo"], [0, 0])
        assert int(x["artigos_na_vista"]) == a
        assert int(x["unidades_positivas_na_vista"]) == u
        assert x["C0_J_homologadas"] == "0"
    assert sum(int(x["artigos_na_vista"]) for x in rows) == 216
    assert sum(int(x["unidades_positivas_na_vista"]) for x in rows) == 681
    assert sum(int(x["artigos_na_vista"]) > 0 for x in rows) == 14
    print("OK índice/matriz/código R15: 216 artigos, 681 unidades, 14 títulos, 34 lacunas.")


if __name__ == "__main__":
    for spec in NEW_SOURCES:
        verify_source(*spec)
    verify_index_matrix_and_code()
    print("OK documental R15; autenticidade DOU, legalidade e C0-J permanecem pendentes.")
