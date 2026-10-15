#!/usr/bin/env python3
"""Valida a integridade documental da prévia T48.M03, nunca a equivalência jurídica."""
from __future__ import annotations
import csv
import hashlib
import io
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
meta = json.loads((ROOT / "produto/fontes/T48_M03_9474_17_v1.json").read_text(encoding="utf-8"))
raw = (ROOT / meta["source_path"]).read_bytes()
blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
assert blob == meta["source_blob_sha"], "Drift SHA fonte T48"
rows = list(csv.DictReader(io.StringIO(raw.decode("utf-8"))))
assert len(rows) == meta["count_expected"] == 17
assert len({r["id_origem"] for r in rows}) == len({r["id_destino_simbolico"] for r in rows}) == 17
assert len({r["artigo"] for r in rows}) == meta["articles_expected"] == 8
assert [r["artigo"] for r in rows if r["unidade"] == "C"] == list(map(str,range(1,9)))
assert all(r["texto_fonte_camara_html"] == r["texto_destino_documental"] for r in rows)
assert all(r["estado_juridico"] == "Q_SEM_C0_J" for r in rows)
assert meta["material_approved"] is False and meta["dec016"] == "PENDENTE"
assert meta["dou_facsimile_checked"] is False
v = (ROOT / meta["view_path"]).read_text(encoding="utf-8")
assert v.count("**Art. ") == 8
assert all(r["texto_destino_documental"] in v for r in rows)
assert "NÃO RATIFICADO" in v and "não devolução" in v
print("OK T48: 8 artigos, 17 unidades com hash; Q documental, sem C0-J")
