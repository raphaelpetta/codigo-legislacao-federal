#!/usr/bin/env python3
"""Gera e verifica vista T24 a partir de 106 subunidades do PR #38.

Exemplo: python3 scripts/gerar_previa_t24.py --setorial-root setorial --check
O diretorio 'setorial' deve conter o checkout do SHA fixado no manifesto.
Usa apenas a biblioteca-padrao e NAO certifica vigencia ou equivalencia juridica.
"""
from __future__ import annotations

import argparse
import csv
import difflib
import hashlib
import io
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "produto/fontes/T24_M01_106_v1.json"


def blob_sha(dados: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(dados)).encode() + b"\0" + dados).hexdigest()


def require(condicao: bool, msg: str) -> None:
    if not condicao:
        raise ValueError(msg)


def marker(unidade: str) -> str:
    if unidade == "caput":
        return "caput"
    if unidade == "par.un.":
        return "Parágrafo único."
    match = re.fullmatch(r"§([0-9]+)(?:\.([IVXLC]+))?", unidade)
    if match:
        return match.group(2) + " –" if match.group(2) else "§ " + match.group(1) + "º"
    if re.fullmatch(r"[IVXLC]+", unidade):
        return unidade + " –"
    raise ValueError("Marcador não previsto no espelho: " + unidade)


def target_id(item: dict[str, str]) -> str:
    slug = re.sub(r"[^A-Za-z0-9]", "_", item["unidade"].replace("§", "P")).upper()
    return "CLF-T24-CPC" + item["artigo"].zfill(3) + "-" + slug


def build(meta: dict, orig: list[dict[str, str]]) -> str:
    require(len(orig) == meta["count_expected"], "Quantidade de unidades mudou")
    orig_ids = [a["id_origem"] for a in orig]
    require(all(orig_ids) and len(set(orig_ids)) == len(orig_ids), "IDs de origem vazios ou duplicados")
    require(all(a.get("texto_atual_manual") for a in orig), "Texto atual não transcrito")
    require(all(a.get("estado_proposta_clf") == "NAO_C0_NAO_C1_NAO_M" for a in orig),
            "O setorial modificou estado jurídico; revisar manifesto")
    require(meta["status_juridico"] == "Q_SEM_C0_J" and not meta["material_approved"]
            and meta["dec016"] == "PENDENTE", "Gates materiais obrigatórios alterados")
    classes = Counter(a["classificacao_comparacao"] for a in orig)
    require(dict(classes) == meta["classes_expected"], "Classificação original/atual divergente")
    grupos: dict[int, list[dict[str, str]]] = {}
    for a in orig:
        n = int(a["artigo"])
        grupos.setdefault(n, []).append(a)
    require(len(grupos) == meta["articles_expected"], "Número de artigos diverge")

    parts = [meta["header"], ""]
    usados: set[int] = set()
    for sec in meta["sections"]:
        parts.extend(["## " + sec["heading"], ""])
        for n in range(sec["start"], sec["end"] + 1):
            require(n in grupos, f"Artigo faltante: {n}")
            usados.add(n)
            z = grupos[n]
            require(z[0]["unidade"] == "caput"
                    and sum(a["unidade"] == "caput" for a in z) == 1,
                    f"Caput ausente ou duplicado em {n}")
            parts.extend([f"**Art. {n}.** " + z[0]["texto_atual_manual"], ""])
            for item in z[1:]:
                parts.extend(["**" + marker(item["unidade"]) + "** "
                              + item["texto_atual_manual"], ""])
    require(set(grupos) == usados, "Artigo fora das seções especificadas")
    return "\n".join(parts + [meta["footer"].rstrip(), ""])


def verify_crosswalk(orig: list[dict[str, str]], meta: dict) -> None:
    path = ROOT / meta["concordance_path"]
    require(path.is_file(), "Matriz de concordância ausente")
    concord = list(csv.DictReader(io.StringIO(path.read_text(encoding="utf-8"))))
    require(len(concord) == len(orig), "Concordância sem cobertura 1:1")
    require(len({x["destino_simbolico"] for x in concord}) == len(concord),
            "Destino simbólico duplicado")
    require(len({x["id_origem"] for x in concord}) == len(concord),
            "Origem duplicada na concordância")
    source_by_id = {x["id_origem"]: x for x in orig}
    for x in concord:
        a = source_by_id.get(x["id_origem"])
        require(a is not None, "Origem inexistente na concordância: " + x["id_origem"])
        require(x["destino_simbolico"] == target_id(a), "Destino simbólico não determinístico")
        require(x["texto_origem_transcrito"] == a["texto_atual_manual"]
                and x["texto_destino_experimental"] == a["texto_atual_manual"],
                "Mudança de texto não documentada na concordância: " + a["id_origem"])
        require(x["status_juridico"] == "Q_SEM_C0_J"
                and x["categoria_transposicao"] == "Q_NAO_C0_T_CERTIFICADO",
                "Equivalência não certificada marcada indevidamente")


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--setorial-root", type=Path, default=ROOT)
    mode = p.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    args = p.parse_args()
    meta = json.loads(MANIFEST.read_text(encoding="utf-8"))
    src = args.setorial_root / meta["source_path"]
    require(src.is_file(), "Checkout setorial ausente no SHA do manifesto")
    raw = src.read_bytes()
    require(blob_sha(raw) == meta["source_blob_sha"], "Blob setorial alterado ou SHA errado")
    items = list(csv.DictReader(io.StringIO(raw.decode("utf-8"))))
    verify_crosswalk(items, meta)
    rendered = build(meta, items)
    view = ROOT / meta["view_path"]
    if args.write:
        view.parent.mkdir(parents=True, exist_ok=True)
        view.write_bytes(rendered.encode("utf-8"))
        print("Vista T24 recompilada a partir da origem, sem homologação")
        return 0
    require(view.is_file(), "Vista inexistente")
    if view.read_bytes() != rendered.encode("utf-8"):
        delta = difflib.unified_diff(view.read_text(encoding="utf-8").splitlines(),
                                     rendered.splitlines(), fromfile="vista",
                                     tofile="gerada", lineterm="")
        print("\n".join(list(delta)[:70]), file=sys.stderr)
        raise ValueError("DRIFT vista T24 x origem setorial")
    print("OK T24: 106 origens, 106 destinos, 17 artigos, todos Q; C0-J=0")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, UnicodeError, KeyError) as e:
        print("FALHA documental T24:", e, file=sys.stderr)
        sys.exit(1)
