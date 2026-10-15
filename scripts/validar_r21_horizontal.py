#!/usr/bin/env python3
"""CLF R21 — QA de corpus Q sem certificação normativa, DOU ou C0-J."""
from __future__ import annotations
import csv
import hashlib
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES = [
    ("produto/fontes/T02_M01_EIR_9_R21_v1.json", 2, 9),
    ("produto/fontes/T21_M01_SFN_7_R21_v1.json", 2, 7),
    ("produto/fontes/T39_M01_AGF_17_R21_v1.json", 3, 17),
    ("produto/fontes/T10_M01_LAI_10_R21_v1.json", 1, 10),
]

for mpath, a, n in SOURCES:
    m = json.loads((ROOT / mpath).read_text(encoding="utf-8"))
    raw = (ROOT / m["source_path"]).read_bytes()
    digest = hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw).hexdigest()
    assert digest == m["source_blob_sha"], mpath
    records = list(csv.DictReader(io.StringIO(raw.decode("utf-8")), strict=True))
    assert len(records) == m["count_expected"] == n
    assert len({r["id_origem"] for r in records}) == n
    assert len({r["id_destino_simbolico"] for r in records}) == n
    assert sum(r["unidade"] == "C" for r in records) == a
    assert len({r["artigo"] for r in records}) == m["articles_expected"] == a
    assert all(r["texto_fonte_editorial"] == r["texto_destino_documental"] for r in records)
    assert all(r["estado_juridico"] == "Q_SEM_C0_J" for r in records)
    assert not m["dou_facsimile_checked"] and not m["material_approved"]
    assert m["dec016"] == "PENDENTE"
    view = (ROOT / m["view_path"]).read_text(encoding="utf-8")
    assert sum(line.startswith("**Art. ") for line in view.splitlines()) == a
    assert all(r["texto_destino_documental"] in view for r in records)
    assert digest in view
    if mpath.startswith("produto/fontes/T02"):
        assert {"PU", "I", "II", "III", "IV", "V", "VI"} <= {r["unidade"] for r in records}
    if mpath.startswith("produto/fontes/T39"):
        assert {"P2-I", "P2-II", "P2-III", "P2-IV", "P2-V", "P2-VI", "P3", "P4"} <= {r["unidade"] for r in records}
    if mpath.startswith("produto/fontes/T10"):
        assert {"I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"} <= {r["unidade"] for r in records}
    print(f"OK {mpath}: {a} artigos/{n} unidades, SHA={digest}")

index = json.loads((ROOT / "produto/fontes/indice_livros.json").read_text(encoding="utf-8"))
books = index["livros"]
assert len(books) == 48
assert len({b["titulo"] for b in books}) == 32
assert sum(b["artigos"] for b in books) == 274
assert sum(b["registros_documentais"] for b in books) == 939
counts = {}
for b in books:
    a, u, n = counts.get(b["titulo"], (0, 0, 0))
    counts[b["titulo"]] = (a + b["artigos"], u + b["registros_documentais"], n + 1)
a, u, n = counts["T07"]
counts["T07"] = (a, u - 1, n)

with (ROOT / "central/01_MATRIZ_AUDITORIA_48_TITULOS_20261015.csv").open(encoding="utf-8", newline="") as f:
    matrix = list(csv.DictReader(f))
assert len(matrix) == 48 and len({r["id_titulo"] for r in matrix}) == 48
for r in matrix:
    a, u, _ = counts.get(r["id_titulo"], (0, 0, 0))
    assert int(r["artigos_na_vista"]) == a
    assert int(r["unidades_positivas_na_vista"]) == u
    assert int(r["C0_J_homologadas"]) == 0
assert sum(int(r["unidades_positivas_na_vista"]) for r in matrix) == 938
assert sum(int(r["artigos_na_vista"]) > 0 for r in matrix) == 32
with (ROOT / "central/PAINEL_GERADO.csv").open(encoding="utf-8", newline="") as f:
    panel = list(csv.DictReader(f))
assert len(panel) == 48
for r in panel:
    a, u, n = counts.get(r["id_titulo"], (0, 0, 0))
    assert int(r["livros_em_vista"]) == n
    assert int(r["artigos_experimentais"]) == a
    assert int(r["registros_documentais_na_fonte"]) == u + (1 if r["id_titulo"] == "T07" else 0)

code = (ROOT / "produto/CODIGO_DE_TRABALHO.md").read_text(encoding="utf-8")
assert sum(line.startswith("**Art. ") for line in code.splitlines()) == 274
first = books[0]
anchor = f"## {first['titulo']} — {first['modulo']} [{first['id']}; {first['estado']}]"
assert anchor in code
prefix = code[:code.index(anchor)]
generated = prefix + "".join(
    f"## {b['titulo']} — {b['modulo']} [{b['id']}; {b['estado']}]\n\n"
    + (ROOT / b["vista"]).read_text(encoding="utf-8").rstrip() + "\n\n"
    for b in books
)
assert generated.rstrip() + "\n" == code
print("OK R21: 48 vistas, 32 títulos, 274 artigos, 938 unidades positivas +1 histórica")
print("QA DOCUMENTAL, NÃO HOMOLOGA DOU, CI, C0-J, M, DEC-016 OU VIGÊNCIA")
