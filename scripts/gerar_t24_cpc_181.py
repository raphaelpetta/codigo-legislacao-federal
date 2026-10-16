#!/usr/bin/env python3
"""Verifica/regenera prévia contínua T24 CPC 70-102 por duas fontes documentais.
Não certifica DOU, jurisprudência, C0-J, competência ou DEC-016.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import io
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "produto/fontes/T24_CPC_70_102_181_v1.json"


def check(ok: bool, reason: str) -> None:
    if not ok:
        raise ValueError(reason)


def blob(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def data_at(path: str, wanted_blob: str) -> bytes:
    p = ROOT / path
    check(p.is_file(), "Fonte/controle ausente: " + path)
    raw = p.read_bytes()
    check(blob(raw) == wanted_blob, "DRIFT de blob: " + path)
    return raw


def csv_rows(raw: bytes) -> list[dict[str, str]]:
    return list(csv.DictReader(io.StringIO(raw.decode("utf-8"))))


def render(meta: dict) -> str:
    comps = meta["components"]
    check(len(comps) == 2 and [x["count"] for x in comps] == [106, 75],
          "Componentes inesperados")
    check(meta["material_approved"] is False and meta["status_juridico"] == "Q_SEM_C0_J"
          and meta["dec016"] == "PENDENTE", "Gate juridico perdido")
    old = data_at(comps[0]["path"], comps[0]["git_blob"]).decode("utf-8")
    piece = data_at(comps[1]["view_part_path"], comps[1]["view_part_git_blob"]).decode("utf-8")
    source = csv_rows(data_at(comps[1]["path"], comps[1]["git_blob"]))
    old_cross = csv_rows(data_at(comps[0]["concordance_path"],
                                 comps[0]["concordance_git_blob"]))
    cross = csv_rows(data_at(comps[1]["concordance_path"],
                             comps[1]["concordance_git_blob"]))
    check(len(source) == len(cross) == 75 and len(old_cross) == 106,
          "Cardinalidade das fontes 106+75 invalida")
    check(len({x["id_origem"] for x in cross}) == len({x["destino_experimental"] for x in cross}) == 75,
          "Duplicacao na matriz de destino 75")
    check(len({x["id_origem"] for x in old_cross}) == 106,
          "Duplicacao nas origens 106")
    by_orig = {row["id_origem"]: row for row in source}
    for row in cross:
        a = by_orig.get(row["id_origem"])
        check(a is not None, "Origem nao encontrada")
        check(row["texto_origem_camara_transcrito"] == a["texto_atual_manual"]
              and row["texto_destino_experimental"] == a["texto_atual_manual"],
              "Mudanca invisivel de texto: " + row["id_origem"])
        check(row["estado_juridico"] == "Q_SEM_C0_J"
              and a["estado_juridico"] == "Q_SEM_C0_J", "Homologacao indevida")
        expected_id = ("CLF-T24-CPC" + a["artigo"].zfill(3) + "-" + a["subunidade"])
        check(row["destino_experimental"] == expected_id, "ID destino inconsistente")
    expected_additions = {
        ("82", "P3"): "LEI_15109_2025",
        ("85", "P6A"): "LEI_14365_2022",
        ("85", "P8A"): "LEI_14365_2022",
        ("85", "P20"): "LEI_14365_2022",
    }
    actual_additions = {(x["artigo"], x["subunidade"]): x["marco_alterador"] for x in source
                        if x["marco_alterador"] != "SEM_ACRESCIMO_ASSINALADO_NESTA_FONTE"}
    check(actual_additions == expected_additions, "Marcos 2022/2025 perdidos")
    check(len([x for x in source if x["artigo"] == "85"]) == 36,
          "CPC85 perdeu um dos 36 itens")
    check(len([x for x in source if x["artigo"] == "82"]) == 4
          and len([x for x in source if x["artigo"] == "95"]) == 8,
          "Perdas na faixa critica 48")

    first = old.index("## Capacidade processual")
    second = old.index("## Gratuidade da justiça")
    end = old.index("---\n\n## Lacunas e condições")
    midstart = piece.index("## Das despesas, dos honorários")
    midend = piece.index("---\n\n## Portas jurídicas")
    sections = [old[first:second].rstrip(), piece[midstart:midend].rstrip(),
                old[second:end].rstrip()]
    compiled = meta["header"] + "\n\n".join(sections) + "\n\n" + meta["footer"]
    numbers = [int(z) for z in re.findall(r"(?m)^\*\*Art\. (\d+)\.\*\*", compiled)]
    check(numbers == list(range(70, 103))
          and len(numbers) == meta["articles_expected"] == 33,
          "Artigos CPC70–102 nao contiguos")
    check(len(old_cross) + len(cross) == meta["count_expected"] == 181,
          "181 origens nao asseguradas")
    return compiled


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    args = parser.parse_args()
    meta = json.loads(MANIFEST.read_text(encoding="utf-8"))
    text = render(meta)
    dest = ROOT / meta["view_path"]
    if args.write:
        dest.write_text(text, encoding="utf-8")
        print("REGERADO CPC 70-102, 181 registros Q e 0 C0-J")
    else:
        check(dest.is_file() and dest.read_bytes() == text.encode("utf-8"),
              "DRIFT: previa T24 181 diverge de manifesto e fontes")
        print("OK documental T24: 33 artigos, 181 unidades, 75 transcritas e 106 setoriais; Q")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, KeyError, UnicodeError, csv.Error) as error:
        print("FALHA T24 integrado:", error, file=sys.stderr)
        sys.exit(1)
