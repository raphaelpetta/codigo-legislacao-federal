#!/usr/bin/env python3
"""Verifica integridade documental R13, sem homologar DOU, vigência ou equivalência C0-J."""
from __future__ import annotations
import csv
import hashlib
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES = [
    ("produto/fontes/T03_M01_LC140_15_R13_v1.json", 3, 15),
    ("produto/fontes/T48_M03_9474_16_R13_v1.json", 16, 16),
]


def verify(name: str, articles: int, units: int) -> None:
    mf = json.loads((ROOT / name).read_text(encoding="utf-8"))
    raw = (ROOT / mf["source_path"]).read_bytes()
    actual_sha = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
    assert actual_sha == mf["source_blob_sha"], "Source Git SHA drift"
    lines = list(csv.DictReader(io.StringIO(raw.decode("utf-8")), strict=True))
    assert len(lines) == units == mf["count_expected"]
    assert len({v["id_origem"] for v in lines}) == units
    assert len({v["id_destino_simbolico"] for v in lines}) == units
    assert len([v for v in lines if v["unidade"] == "C"]) == articles
    assert len({v["artigo"] for v in lines}) == articles
    assert all(v["texto_fonte_editorial"] == v["texto_destino_documental"] for v in lines)
    assert all(v["estado_juridico"] == "Q_SEM_C0_J" for v in lines)
    assert all(v["classe_textual"] == "C0_T_CANDIDATO_SEM_DOU" for v in lines)
    assert mf["dou_facsimile_checked"] is False
    assert mf["material_approved"] is False and mf["dec016"] == "PENDENTE"
    view = (ROOT / mf["view_path"]).read_text(encoding="utf-8")
    assert view.count("**Art. ") == articles
    assert "NÃO RATIFICADO" in view and "C0-J=0" in view
    assert all(v["texto_destino_documental"] in view for v in lines)
    print(f"OK R13 {name}: {articles} artigos/{units} unidades; git blob {actual_sha}")


if __name__ == "__main__":
    for spec in SOURCES:
        verify(*spec)
    print("OK R13 documental +19 artigos/31 unidades Q; NÃO EQUIVALE A C0-J")
