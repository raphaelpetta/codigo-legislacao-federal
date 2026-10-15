#!/usr/bin/env python3
"""Document integrity of CLF R12 sources/views; not legal equivalence or DOU authentication."""
from __future__ import annotations
import csv
import hashlib
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPECS = [
    ("produto/fontes/T03_M01_LC140_10_R12_v1.json", 3, 10),
    ("produto/fontes/T37_M01_6938_9_R12_v1.json", 2, 9),
    ("produto/fontes/T48_M03_9474_23_R12_v1.json", 6, 23),
]


def verify(path: str, n_articles: int, n_units: int) -> None:
    manifest = json.loads((ROOT / path).read_text(encoding="utf-8"))
    raw = (ROOT / manifest["source_path"]).read_bytes()
    digest = hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw).hexdigest()
    assert digest == manifest["source_blob_sha"], f"Drift Git SHA: {path}"
    entries = list(csv.DictReader(io.StringIO(raw.decode("utf-8")), strict=True))
    assert len(entries) == manifest["count_expected"] == n_units
    assert len({r["id_origem"] for r in entries}) == n_units
    assert len({r["id_destino_simbolico"] for r in entries}) == n_units
    assert len([r for r in entries if r["unidade"] == "C"]) == n_articles
    assert len({r["artigo"] for r in entries}) == n_articles
    assert all(r["texto_fonte_editorial"] == r["texto_destino_documental"] for r in entries)
    assert all(r["estado_juridico"] == "Q_SEM_C0_J" for r in entries)
    assert all(r["classe_textual"] == "C0_T_CANDIDATO_SEM_DOU" for r in entries)
    assert manifest["dou_facsimile_checked"] is False
    assert manifest["material_approved"] is False
    assert manifest["dec016"] == "PENDENTE"
    view = (ROOT / manifest["view_path"]).read_text(encoding="utf-8")
    assert view.count("**Art. ") == n_articles
    assert all(r["texto_destino_documental"] in view for r in entries)
    assert "NÃO RATIFICADO" in view and "C0-J=0" in view
    print(f"OK R12 {path}: artigos={n_articles}; unidades={n_units}; SHA={digest}")


if __name__ == "__main__":
    for spec in SPECS:
        verify(*spec)
    print("OK R12: 11 artigos e 42 unidades novas Q, não C0-J")
