#!/usr/bin/env python3
"""Validador documental Q do suplemento da Lei 9.709/1998, arts. 3-15."""
import csv
import hashlib
import io
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
meta = json.loads((ROOT / "produto/fontes/T05_M06_9709_23_v1.json").read_text(encoding="utf-8"))
data = (ROOT / meta["source_path"]).read_bytes()
blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
assert blob == meta["source_blob_sha"], "Fonte Q alterada sem atualizar manifesto"
rows = list(csv.DictReader(io.StringIO(data.decode("utf-8"))))
assert len(rows) == meta["count_expected"] == 23
assert len({r["id_origem"] for r in rows}) == 23
assert len({r["id_destino_simbolico"] for r in rows}) == 23
assert len({r["artigo"] for r in rows}) == meta["articles_expected"] == 13
assert all(r["texto_fonte_camara_html"] == r["texto_destino_documental"] for r in rows)
assert all(r["status_juridico"] == "Q_SEM_C0_J" for r in rows)
assert meta["material_approved"] is False and meta["dec016"] == "PENDENTE"
preview = (ROOT / meta["view_path"]).read_text(encoding="utf-8")
assert len(re.findall(r"(?m)^\*\*Art\. \d+\.\*\*", preview)) == 13
assert all(r["texto_destino_documental"] in preview for r in rows)
print("OK T05 23 unidades/13 artigos documentais Q; sem C0-J")
