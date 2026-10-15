#!/usr/bin/env python3
"""Verifica/gera 39 subunidades CP 1-12 da fonte setorial fixada no PR32.
Nao homologa C0-J, reforma M, revogacao ou extensao de norma penal.
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
META = ROOT / "produto/fontes/T25_CP1_12_v1.json"


def need(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def marker(unit: str) -> str:
    if unit == "paragrafo_unico":
        return "Parágrafo único."
    m = re.fullmatch(r"paragrafo_([0-9]+)", unit)
    if m:
        return "§ " + m.group(1) + "º"
    m = re.fullmatch(r"inciso_([IVXLC]+)", unit)
    if m:
        return m.group(1) + " –"
    m = re.fullmatch(r"inciso_[IVXLC]+_alinea_([a-z])", unit)
    if m:
        return m.group(1) + ")"
    m = re.fullmatch(r"paragrafo_[0-9]+_alinea_([a-z])", unit)
    if m:
        return m.group(1) + ")"
    m = re.fullmatch(r"paragrafo_unico_alinea_([a-z])", unit)
    if m:
        return m.group(1) + ")"
    raise ValueError("Unidade nao reconhecida: " + unit)


def extract_id(identifier: str) -> tuple[int, str]:
    m = re.fullmatch(r"CP-([0-9]{2})-(.+)", identifier)
    need(m is not None, "ID penal invalido: " + identifier)
    return int(m.group(1)), m.group(2)


def build(meta: dict, source: list[dict[str, str]]) -> str:
    need(len(source) == meta["count_expected"], "Quantidade de registros nao e 39")
    orig_ids = [z["id_fonte"] for z in source]
    need(len(orig_ids) == len(set(orig_ids)), "IDs de origem duplicados")
    need(all(z["equivalencia_juridica"] == "Q" and z["categoria_espelho"] == "C0-T"
             and z["texto_literal_sem_rotulo"] for z in source),
         "Fonte nao corresponde a classificacao documental permitida")
    need(meta["status_juridico"] == "Q_SEM_C0_J" and meta["dec016"] == "PENDENTE"
         and meta["material_approved"] is False,
         "Gate juridico foi alterado")
    text = meta["header"]
    last = 0
    for z in source:
        art, unit = extract_id(z["id_fonte"])
        need(art >= last and art <= meta["articles_expected"], "Ordem artigo invalida")
        if art != last:
            need(art == last + 1 and unit == "caput", "Artigo ou caput faltante")
            text += "**Art. CP-" + str(art).zfill(3) + ".** " + z["texto_literal_sem_rotulo"] + "\n\n"
            last = art
        else:
            text += "**" + marker(unit) + "** " + z["texto_literal_sem_rotulo"] + "\n\n"
    need(last == meta["articles_expected"], "Artigos insuficientes")
    return text + meta["footer"]


def verify_crosswalk(meta: dict, source: list[dict[str, str]]) -> None:
    path = ROOT / meta["concordance_path"]
    need(path.is_file(), "Matriz de concordancia ausente")
    cross = list(csv.DictReader(io.StringIO(path.read_text(encoding="utf-8"))))
    need(len(cross) == len(source), "Concordancia incompleta")
    expected = {z["id_fonte"]: z for z in source}
    need(len({a["id_origem"] for a in cross}) == len(cross)
         and len({a["id_destino_provisorio"] for a in cross}) == len(cross),
         "IDs duplicados na matriz")
    for row in cross:
        original = expected.get(row["id_origem"])
        need(original is not None, "Origem inexistente")
        n, unit = extract_id(row["id_origem"])
        should = "CLF-T25-CP" + str(n).zfill(3) + "-" + unit.upper()
        need(row["id_destino_provisorio"] == should, "Destino simbolico diferente")
        need(row["texto_destino"] == original["texto_literal_sem_rotulo"]
             and row["texto_espelho_literal"] == original["texto_literal_sem_rotulo"],
             "Texto modificado na matriz")
        need(row["estado_juridico"] == "Q_SEM_C0_J", "Equivalencia C0-J indevida")


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--setorial-root", type=Path, default=ROOT)
    group = p.add_mutually_exclusive_group()
    group.add_argument("--write", action="store_true")
    group.add_argument("--check", action="store_true")
    args = p.parse_args()
    meta = json.loads(META.read_text(encoding="utf-8"))
    source_path = args.setorial_root / meta["source_path"]
    need(source_path.is_file(), "Checkout do PR32 no SHA declarado ausente")
    contents = source_path.read_bytes()
    need(blob_sha(contents) == meta["source_blob_sha"], "Fonte setorial mudou")
    source = list(csv.DictReader(io.StringIO(contents.decode("utf-8"))))
    verify_crosswalk(meta, source)
    generated = build(meta, source)
    out = ROOT / meta["view_path"]
    if args.write:
        out.write_bytes(generated.encode("utf-8"))
        print("T25 vista regenerada, 39 Q e zero C0-J")
        return 0
    need(out.is_file() and out.read_bytes() == generated.encode("utf-8"),
         "Drift entre vista T25 e origem fixada")
    print("OK documental T25: 39 origens/destinos, 12 artigos CP, sem C0-J")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (ValueError, OSError, KeyError, csv.Error) as e:
        print("FALHA T25:", e, file=sys.stderr)
        sys.exit(1)
