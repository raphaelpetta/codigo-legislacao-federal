#!/usr/bin/env python3
"""CLF R17: valida integridade documental Q, não autentica DOU ou C0-J."""
from __future__ import annotations
import csv
import hashlib
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NEW = [
    ("produto/fontes/T29_M01_8213_11_R17_v1.json", 2, 11),
    ("produto/fontes/T33_M01_LDB_20_R17_v1.json", 3, 20),
    ("produto/fontes/T38_M01_9433_21_R17_v1.json", 3, 21),
    ("produto/fontes/T12_M01_CTN_7_R17_v1.json", 3, 7),
]

for name, arts, units in NEW:
    m = json.loads((ROOT / name).read_text(encoding="utf-8"))
    raw = (ROOT / m["source_path"]).read_bytes()
    digest = hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw).hexdigest()
    assert digest == m["source_blob_sha"], name
    rows = list(csv.DictReader(io.StringIO(raw.decode("utf-8")), strict=True))
    assert len(rows) == units == m["count_expected"]
    assert len({r["artigo"] for r in rows}) == arts == m["articles_expected"]
    assert sum(r["unidade"] == "C" for r in rows) == arts
    assert len({r["id_origem"] for r in rows}) == units
    assert len({r["id_destino_simbolico"] for r in rows}) == units
    assert all(r["texto_fonte_editorial"] == r["texto_destino_documental"] for r in rows)
    assert all(r["estado_juridico"] == "Q_SEM_C0_J" for r in rows)
    assert not m["dou_facsimile_checked"] and not m["material_approved"]
    assert m["dec016"] == "PENDENTE"
    view = (ROOT / m["view_path"]).read_text(encoding="utf-8")
    assert view.count("**Art. ") == arts
    assert all(r["texto_destino_documental"] in view for r in rows)
    print(f"OK {name}: {arts} artigos/{units} unidades, blob {digest}")

idx = json.loads((ROOT / "produto/fontes/indice_livros.json").read_text(encoding="utf-8"))
books = idx["livros"]
assert len(books) == 32
assert len({b["titulo"] for b in books}) == 20
assert sum(b["artigos"] for b in books) == 237
assert sum(b["registros_documentais"] for b in books) == 773
totals = {}
for b in books:
    a, u = totals.get(b["titulo"], (0, 0))
    totals[b["titulo"]] = (a + b["artigos"], u + b["registros_documentais"])
totals["T07"] = (totals["T07"][0], totals["T07"][1] - 1)
with (ROOT / "central/01_MATRIZ_AUDITORIA_48_TITULOS_20261015.csv").open(encoding="utf-8", newline="") as fd:
    mx = list(csv.DictReader(fd))
assert len(mx) == 48 and len({r["id_titulo"] for r in mx}) == 48
for r in mx:
    a, u = totals.get(r["id_titulo"], (0, 0))
    assert (int(r["artigos_na_vista"]), int(r["unidades_positivas_na_vista"])) == (a, u)
    assert int(r["C0_J_homologadas"]) == 0
assert sum(int(r["artigos_na_vista"]) for r in mx) == 237
assert sum(int(r["unidades_positivas_na_vista"]) for r in mx) == 772
code = (ROOT / "produto/CODIGO_DE_TRABALHO.md").read_text(encoding="utf-8")
assert sum(line.startswith("**Art. ") for line in code.splitlines()) == 237
for b in books:
    header = f"## {b['titulo']} — {b['modulo']} [{b['id']}; {b['estado']}]"
    assert header in code and (ROOT / b["vista"]).read_text(encoding="utf-8").strip() in code
print("OK R17: 20 títulos, 32 vistas, 237 artigos, 772 unidades Q +1 histórico. Sem homologação.")
