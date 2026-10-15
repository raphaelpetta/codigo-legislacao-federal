#!/usr/bin/env python3
"""Check R10 source↔view documentary integrity; does not attest normative equivalence or DOU."""
from __future__ import annotations

import csv
import hashlib
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFESTS = (
    ROOT / "produto/fontes/T48_M03_9474_4_R10_v1.json",
    ROOT / "produto/fontes/T37_M01_6938_13_R10_v1.json",
)


def check(path: Path) -> tuple[int, int, str]:
    mf = json.loads(path.read_text(encoding="utf-8"))
    raw = (ROOT / mf["source_path"]).read_bytes()
    blob = hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") + b"\x00" + raw).hexdigest()
    assert blob == mf["source_blob_sha"], "Git blob differs from manifest"
    rows = list(csv.DictReader(io.StringIO(raw.decode("utf-8")), strict=True))
    assert len(rows) == mf["count_expected"]
    assert len({r["id_origem"] for r in rows}) == len(rows)
    assert len({r["id_destino_simbolico"] for r in rows}) == len(rows)
    caps = [r for r in rows if r["unidade"] == "C"]
    assert len(caps) == mf["articles_expected"]
    assert len({r["artigo"] for r in rows}) == mf["articles_expected"]
    assert all(r["texto_fonte_editorial"] == r["texto_destino_documental"] for r in rows)
    assert all(r["classe_textual"] == "C0_T_CANDIDATO_SEM_DOU" for r in rows)
    assert all(r["estado_juridico"] == "Q_SEM_C0_J" for r in rows)
    assert mf["dou_facsimile_checked"] is False
    assert mf["material_approved"] is False and mf["dec016"] == "PENDENTE"
    view = (ROOT / mf["view_path"]).read_text(encoding="utf-8")
    assert view.count("**Art. ") == mf["articles_expected"]
    assert all(r["texto_destino_documental"] in view for r in rows)
    assert "NÃO RATIFICADA" in view and "C0-J" in view
    return len(caps), len(rows), blob


def main() -> None:
    result = [check(p) for p in MANIFESTS]
    assert result[0][:2] == (2, 4)
    assert result[1][:2] == (2, 13)
    print("OK R10: 4 artigos/17 unidades de origem Q; 2 manifestos/hash; C0-J não verificada")
    for path, (articles, units, blob) in zip(MANIFESTS, result):
        print(f"  {path.name}: {articles} artigos; {units} registros; Git blob {blob}")


if __name__ == "__main__":
    main()
