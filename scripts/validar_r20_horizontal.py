#!/usr/bin/env python3
"""CLF R20 — integridade documental Q, testável no checkout do próprio PR."""
from __future__ import annotations
import csv
import hashlib
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES = (
    ("produto/fontes/T10_M01_LAI_12_R20_v1.json", 3, 12),
    ("produto/fontes/T35_M01_INOV_16_R20_v1.json", 1, 16),
    ("produto/fontes/T45_M01_SUSP_3_R20_v1.json", 3, 3),
    ("produto/fontes/T20_M01_CDC_8_R20_v1.json", 1, 8),
)
for path, articles, units in SOURCES:
    m = json.loads((ROOT / path).read_text(encoding="utf-8"))
    raw = (ROOT / m["source_path"]).read_bytes()
    sha = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
    assert sha == m["source_blob_sha"], path
    rows = list(csv.DictReader(io.StringIO(raw.decode("utf-8")), strict=True))
    assert len(rows) == units == m["count_expected"], path
    assert len({r["artigo"] for r in rows}) == articles == m["articles_expected"]
    assert sum(r["unidade"] == "C" for r in rows) == articles
    assert len({r["id_origem"] for r in rows}) == units
    assert len({r["id_destino_simbolico"] for r in rows}) == units
    assert all(r["estado_juridico"] == "Q_SEM_C0_J" for r in rows)
    assert all(r["texto_fonte_editorial"] == r["texto_destino_documental"] for r in rows)
    assert not m["dou_facsimile_checked"] and not m["material_approved"]
    assert m["dec016"] == "PENDENTE"
    view = (ROOT / m["view_path"]).read_text(encoding="utf-8")
    assert sum(line.startswith("**Art. ") for line in view.splitlines()) == articles
    assert all(r["texto_destino_documental"] in view for r in rows)
    assert sha in view
    if "CDC_8_R20" in path:
        assert {r["unidade"] for r in rows} == {"C", "I", "II", "III", "IV", "V", "VI", "VII"}
    if "INOV_16_R20" in path:
        assert len(rows) == 16 and {r["unidade"] for r in rows} >= {"PU", "XIV"}
    print(f"OK {path}: {articles} artigos/{units} unidades, SHA {sha}", flush=True)

idx = json.loads((ROOT / "produto/fontes/indice_livros.json").read_text(encoding="utf-8"))
books = idx["livros"]
assert len(books) == 44
assert len({b["titulo"] for b in books}) == 29
assert sum(b["artigos"] for b in books) == 266
assert sum(b["registros_documentais"] for b in books) == 896
totals = {}
for b in books:
    a, u, n = totals.get(b["titulo"], (0, 0, 0))
    totals[b["titulo"]] = (a + b["artigos"], u + b["registros_documentais"], n + 1)
a, u, n = totals["T07"]
totals["T07"] = (a, u - 1, n)

with (ROOT / "central/01_MATRIZ_AUDITORIA_48_TITULOS_20261015.csv").open(encoding="utf-8", newline="") as f:
    matrix = list(csv.DictReader(f))
assert len(matrix) == 48 and len({r["id_titulo"] for r in matrix}) == 48
for r in matrix:
    a, u, n = totals.get(r["id_titulo"], (0, 0, 0))
    assert int(r["artigos_na_vista"]) == a
    assert int(r["unidades_positivas_na_vista"]) == u
    assert int(r["C0_J_homologadas"]) == 0
assert sum(int(r["artigos_na_vista"]) > 0 for r in matrix) == 29
assert sum(int(r["unidades_positivas_na_vista"]) for r in matrix) == 895
with (ROOT / "central/PAINEL_GERADO.csv").open(encoding="utf-8", newline="") as f:
    panel = list(csv.DictReader(f))
assert len(panel) == 48
for r in panel:
    a, u, n = totals.get(r["id_titulo"], (0, 0, 0))
    assert int(r["livros_em_vista"]) == n
    assert int(r["artigos_experimentais"]) == a
    assert int(r["registros_documentais_na_fonte"]) == u + (1 if r["id_titulo"] == "T07" else 0)

code = (ROOT / "produto/CODIGO_DE_TRABALHO.md").read_text(encoding="utf-8")
assert sum(line.startswith("**Art. ") for line in code.splitlines()) == 266
first = books[0]
header = f"## {first['titulo']} — {first['modulo']} [{first['id']}; {first['estado']}]"
assert header in code
prefix = code[:code.index(header)]
generated = prefix + "".join(
    f"## {b['titulo']} — {b['modulo']} [{b['id']}; {b['estado']}]\n\n"
    + (ROOT / b["vista"]).read_text(encoding="utf-8").rstrip() + "\n\n"
    for b in books
)
assert generated.rstrip() + "\n" == code, "Código divergente das 44 vistas"
print("OK R20 44 vistas, 29 títulos, 266 artigos, 895 unidades textuais positivas +1 histórico")
print("ATENÇÃO: QA documental NÃO homologa DOU, C0-J, M, DEC-016 ou vigência")
