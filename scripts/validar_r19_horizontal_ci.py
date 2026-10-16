#!/usr/bin/env python3
"""CLF R19: QA autossuficiente de textos e índice no checkout da branch. NÃO autentica DOU/C0-J."""
from __future__ import annotations
import csv
import hashlib
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ADDS = [
    ("produto/fontes/T14_M01_CC_13_R19_v1.json", 6, 13),
    ("produto/fontes/T26_M01_CPP_2_R19_v1.json", 2, 2),
    ("produto/fontes/T41_M01_CTB_7_R19_v1.json", 2, 7),
    ("produto/fontes/T20_M01_CDC_15_R19_v1.json", 1, 15),
]

def source(mf_path: str, articles: int, units: int) -> None:
    m = json.loads((ROOT / mf_path).read_text(encoding="utf-8"))
    raw = (ROOT / m["source_path"]).read_bytes()
    sha = hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw).hexdigest()
    assert sha == m["source_blob_sha"], mf_path
    rows = list(csv.DictReader(io.StringIO(raw.decode("utf-8")), strict=True))
    assert len(rows) == units == m["count_expected"]
    assert len({r["id_origem"] for r in rows}) == units
    assert len({r["id_destino_simbolico"] for r in rows}) == units
    assert sum(r["unidade"] == "C" for r in rows) == articles
    assert len({r["artigo"] for r in rows}) == articles == m["articles_expected"]
    assert all(r["texto_fonte_editorial"] == r["texto_destino_documental"] for r in rows)
    assert all(r["estado_juridico"] == "Q_SEM_C0_J" for r in rows)
    assert not m["dou_facsimile_checked"] and not m["material_approved"]
    assert m["dec016"] == "PENDENTE"
    view = (ROOT / m["view_path"]).read_text(encoding="utf-8")
    assert sum(x.startswith("**Art. ") for x in view.splitlines()) == articles
    assert all(r["texto_destino_documental"] in view for r in rows)
    assert sha in view
    if mf_path.startswith("produto/fontes/T41"):
        assert not any(r["unidade"] == "P4" for r in rows), "§ 4º vetado do art. 1º CTB"
        assert any(r["unidade"] == "PU" and "estabelecimentos privados de uso coletivo" in r["texto_destino_documental"] for r in rows)
    if mf_path.startswith("produto/fontes/T20"):
        assert {"II-a", "II-b", "II-c", "II-d"} <= {r["unidade"] for r in rows}
        assert {"IX", "X"} <= {r["unidade"] for r in rows}
    print(f"OK: {mf_path}: {articles} artigos, {units} unidades, SHA {sha}")

for args in ADDS:
    source(*args)

idx = json.loads((ROOT / "produto/fontes/indice_livros.json").read_text(encoding="utf-8"))
books = idx["livros"]
assert len(books) >= 40 and len({b["titulo"] for b in books}) >= 26
assert sum(b["artigos"] for b in books) >= 258
assert sum(b["registros_documentais"] for b in books) >= 857
by_title = {}
for b in books:
    a, u, views = by_title.get(b["titulo"], (0, 0, 0))
    by_title[b["titulo"]] = (a + b["artigos"], u + b["registros_documentais"], views + 1)
a, u, views = by_title["T07"]
by_title["T07"] = (a, u - 1, views)

with (ROOT / "central/01_MATRIZ_AUDITORIA_48_TITULOS_20261015.csv").open(encoding="utf-8", newline="") as f:
    matrix = list(csv.DictReader(f))
assert len(matrix) == 48 and len({r["id_titulo"] for r in matrix}) == 48
for r in matrix:
    a, u, _ = by_title.get(r["id_titulo"], (0, 0, 0))
    assert int(r["artigos_na_vista"]) == a, r["id_titulo"]
    assert int(r["unidades_positivas_na_vista"]) == u, r["id_titulo"]
    assert int(r["C0_J_homologadas"]) == 0
assert sum(int(r["artigos_na_vista"]) > 0 for r in matrix) == len(by_title)
assert sum(int(r["unidades_positivas_na_vista"]) for r in matrix) == sum(u for _, u, _ in by_title.values())

with (ROOT / "central/PAINEL_GERADO.csv").open(encoding="utf-8", newline="") as f:
    panel = list(csv.DictReader(f))
assert len(panel) == 48
for r in panel:
    a, u, views = by_title.get(r["id_titulo"], (0, 0, 0))
    assert int(r["livros_em_vista"]) == views, r["id_titulo"]
    assert int(r["artigos_experimentais"]) == a, r["id_titulo"]
    assert int(r["registros_documentais_na_fonte"]) == u + (1 if r["id_titulo"] == "T07" else 0), r["id_titulo"]

path = ROOT / "produto/CODIGO_DE_TRABALHO.md"
actual = path.read_text(encoding="utf-8")
assert sum(ln.startswith("**Art. ") for ln in actual.splitlines()) == sum(b["artigos"] for b in books)
first = books[0]
anchor = f"## {first['titulo']} — {first['modulo']} [{first['id']}; {first['estado']}]"
assert anchor in actual
head = actual[:actual.index(anchor)]
expected = head + "".join(
    f"## {b['titulo']} — {b['modulo']} [{b['id']}; {b['estado']}]\n\n"
    + (ROOT / b["vista"]).read_text(encoding="utf-8").rstrip() + "\n\n"
    for b in books
)
assert expected.rstrip() + "\n" == actual, "Código divergente das vistas indexadas"
assert not (ROOT / "produto/fontes/T29_M01_8213_11_R17_v1.json").read_text(encoding="utf-8").find('"provenance_correction_R18"') == -1
print(f"OK DOCUMENTAL CLF R19: fontes R19 verificadas; corpus atual {len(by_title)} títulos, {len(books)} vistas, {sum(b['artigos'] for b in books)} artigos.")
print("Este teste não certifica vigência, DOU, efeitos jurídicos, C0-J, M ou DEC-016.")
