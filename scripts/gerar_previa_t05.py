#!/usr/bin/env python3
"""Recompila/valida T05.M06 (Lei 9709 arts.1–2) com sete registros documentais Q.
Nao certifica DOU, vigencia, alcance do Codigo nem aprovacao material.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import io
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "produto/fontes/T05_M06_9709_7_v1.json"


def check(value: bool, reason: str) -> None:
    if not value:
        raise ValueError(reason)


def blob(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def render(meta: dict) -> str:
    check(meta["status_juridico"] == "Q_SEM_C0_J"
          and meta["material_approved"] is False
          and meta["dec016"] == "PENDENTE", "Gate material T05 nao preservado")
    source_path = ROOT / meta["source_path"]
    check(source_path.is_file(), "Espelho T05 ausente")
    raw = source_path.read_bytes()
    check(blob(raw) == meta["source_blob_sha"], "Espelho T05 modificado")
    rows = list(csv.DictReader(io.StringIO(raw.decode("utf-8"))))
    check(len(rows) == meta["count_expected"] == 7, "Unidades T05 diferentes de sete")
    check(len({x["id_origem"] for x in rows}) ==
          len({x["id_destino_simbolico"] for x in rows}) == 7, "IDs duplicados")
    check([x["artigo"] for x in rows] == ["1"]*4 + ["2"]*3,
          "Ordem e cardinalidade 1º/2º alteradas")
    check([x["unidade"] for x in rows] ==
          ["C", "I", "II", "III", "C", "P1", "P2"], "Ordem subunidades alterada")
    text = meta["header"]
    for x in rows:
        check(x["texto_fonte_tse"] == x["texto_destino_literal"]
              and x["status_juridico"] == "Q_SEM_C0_J",
              "Drift texto/status da Lei 9709")
        if x["unidade"] == "C":
            text += "**Art. " + x["artigo"] + ".** " + x["texto_fonte_tse"] + "\n\n"
        else:
            label = ("§ " + x["unidade"][1:] + "º"
                     if x["unidade"].startswith("P") else x["unidade"] + " –")
            text += "**" + label + "** " + x["texto_fonte_tse"] + "\n\n"
    text += meta["footer"]
    check(len(re.findall(r"(?m)^\*\*Art\. \d+\.\*\*", text)) == 2,
          "Artigos nao inteiros")
    return text


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--check", action="store_true")
    group.add_argument("--write", action="store_true")
    args = parser.parse_args()
    meta = json.loads(MANIFEST.read_text(encoding="utf-8"))
    text = render(meta)
    path = ROOT / meta["view_path"]
    if args.write:
        path.write_text(text, encoding="utf-8")
        print("REGERADO T05.M06 2 artigos / 7 unidades, Q")
        return 0
    check(path.is_file() and path.read_bytes() == text.encode("utf-8"),
          "Drift vista T05.M06")
    print("OK T05.M06: 7 origens e destinos, dois artigos, Q sem C0-J")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, KeyError, UnicodeError, csv.Error) as exc:
        print("FALHA T05:", exc, file=sys.stderr)
        sys.exit(1)
