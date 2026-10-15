#!/usr/bin/env python3
"""CLF R18 — integridade documental e correção de proveniência, NÃO autentica DOU ou C0-J."""
from __future__ import annotations
import csv
import hashlib
import io
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFESTS = [
    ("produto/fontes/T27_M01_LEP_5_R18_v1.json", 3, 5),
    ("produto/fontes/T30_M01_LOAS_11_R18_v1.json", 2, 11),
    ("produto/fontes/T42_M01_LGT_24_R18_v1.json", 3, 24),
    ("produto/fontes/T31_M01_8080_7_R18_v1.json", 2, 7),
    ("produto/fontes/T29_M01_8213_11_R17_v1.json", 2, 11),
]

def verify_source(name: str, arts: int, units: int) -> None:
    m = json.loads((ROOT / name).read_text(encoding="utf-8"))
    raw = (ROOT / m["source_path"]).read_bytes()
    sha = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
    assert sha == m["source_blob_sha"], name
    rows = list(csv.DictReader(io.StringIO(raw.decode("utf-8")), strict=True))
    assert len(rows) == units == m["count_expected"], name
    assert len({r["id_origem"] for r in rows}) == units
    assert len({r["id_destino_simbolico"] for r in rows}) == units
    assert sum(r["unidade"] == "C" for r in rows) == arts
    assert len({r["artigo"] for r in rows}) == arts == m["articles_expected"]
    assert all(r["texto_fonte_editorial"] == r["texto_destino_documental"] for r in rows)
    assert all(r["estado_juridico"] == "Q_SEM_C0_J" for r in rows)
    assert all(r["classe_textual"] == "C0_T_CANDIDATO_SEM_DOU" for r in rows)
    assert not m["dou_facsimile_checked"] and not m["material_approved"]
    assert m["dec016"] == "PENDENTE"
    view = (ROOT / m["view_path"]).read_text(encoding="utf-8")
    assert sum(line.startswith("**Art. ") for line in view.splitlines()) == arts
    assert all(r["texto_destino_documental"] in view for r in rows)
    assert sha in view, name
    if name.endswith("8213_11_R17_v1.json"):
        assert all("lei-8213-24-julho-1991" in r["fonte_primaria"] for r in rows)
        assert "lei-15108-13-marco-2025" not in view
        assert m["provenance_correction_R18"]["source_text_changed"] is False
    if name.endswith("LOAS_11_R18_v1.json"):
        assert not any(r["unidade"] in ("IV", "V") for r in rows)
        assert {r["unidade"] for r in rows if r["unidade"].startswith("I-")} == {"I-a", "I-b", "I-c", "I-d", "I-e"}
    print(f"OK {name}: {arts} artigos, {units} unidades, blob {sha}")

for args in MANIFESTS:
    verify_source(*args)

index = json.loads((ROOT / "produto/fontes/indice_livros.json").read_text(encoding="utf-8"))
books = index["livros"]
assert len(books) == 36 and len({b["titulo"] for b in books}) == 23
assert sum(b["artigos"] for b in books) == 247
assert sum(b["registros_documentais"] for b in books) == 820
totals = defaultdict(lambda: [0, 0, 0])
for b in books:
    totals[b["titulo"]][0] += b["artigos"]
    totals[b["titulo"]][1] += b["registros_documentais"]
    totals[b["titulo"]][2] += 1
totals["T07"][1] -= 1
with (ROOT / "central/01_MATRIZ_AUDITORIA_48_TITULOS_20261015.csv").open(encoding="utf-8", newline="") as fd:
    rows = list(csv.DictReader(fd))
assert len(rows) == 48 and len({r["id_titulo"] for r in rows}) == 48
for row in rows:
    a,u,_ = totals.get(row["id_titulo"], [0,0,0])
    assert (int(row["artigos_na_vista"]), int(row["unidades_positivas_na_vista"])) == (a,u)
    assert row["C0_J_homologadas"] == "0"
assert sum(int(r["artigos_na_vista"]) > 0 for r in rows) == 23
assert sum(int(r["unidades_positivas_na_vista"]) for r in rows) == 819
code = (ROOT / "produto/CODIGO_DE_TRABALHO.md").read_text(encoding="utf-8")
assert sum(line.startswith("**Art. ") for line in code.splitlines()) == 247
header = code.split("## " + books[0]["titulo"] + " —", 1)[0]
generated = header + "".join(
    f"## {b['titulo']} — {b['modulo']} [{b['id']}; {b['estado']}]\n\n"
    + (ROOT / b["vista"]).read_text(encoding="utf-8").rstrip() + "\n\n"
    for b in books
)
assert generated.rstrip() + "\n" == code, "Código diferente da montagem reprodutível"
print("OK R18: 23 títulos, 36 vistas, 247 artigos, 819 unidades positivas e 1 histórico. SEM C0-J.")
