#!/usr/bin/env python3
"""Monta o Código experimental a partir de vistas declaradas no índice de Livros.
Somente vista derivada: não edita textos setoriais, não homologa equivalência jurídica.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "produto/fontes/indice_livros.json"
OUTPUT = ROOT / "produto/CODIGO_DE_TRABALHO.md"
HEADER = (
    "# Código da Legislação Federal — corpus único de trabalho (NÃO RATIFICADO)\n\n"
    "> Compilação **experimental** derivada de produto/fontes/indice_livros.json "
    "e das vistas versionadas. Não editar este arquivo; regenerar a partir das fontes. "
    "O texto não é lei vigente, não homologa C0-J, não produz revogação nem resolve "
    "a DEC-016. Livros ainda não integrados são lacunas no quadro de cobertura, "
    "não disposições fictícias.\n\n"
)


def build() -> str:
    index = json.loads(INDEX.read_text(encoding="utf-8"))
    if index.get("schema_version") != 1:
        raise ValueError("Índice de Livros incompatível")
    books = index.get("livros", [])
    if not books:
        raise ValueError("Não há Livro no corpus experimental")
    output = [HEADER]
    known = set()
    for book in books:
        ident = book["id"]
        if ident in known or not book["estado"].startswith("INTEGRADO_EXPERIMENTAL"):
            raise ValueError("Livro repetido ou não experimental: " + ident)
        known.add(ident)
        rel = Path(book["vista"])
        if rel.is_absolute() or ".." in rel.parts:
            raise ValueError("Caminho de vista não confiável: " + str(rel))
        src = ROOT / rel
        if not src.is_file():
            raise ValueError("Vista ausente: " + str(rel))
        output.append(f"## {book['titulo']} — {book['modulo']} "
                      f"[{ident}; {book['estado']}]\n\n")
        output.append(src.read_text(encoding="utf-8").rstrip() + "\n\n")
    return "".join(output).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--check", action="store_true", help="Verifica arquivo gerado")
    group.add_argument("--write", action="store_true", help="Recria vista derivada")
    args = parser.parse_args()
    text = build()
    if args.write:
        OUTPUT.write_text(text, encoding="utf-8")
        print("GERADO:", OUTPUT.relative_to(ROOT))
    elif not OUTPUT.is_file() or OUTPUT.read_text(encoding="utf-8") != text:
        raise ValueError("DRIFT: regenere produto/CODIGO_DE_TRABALHO.md")
    else:
        print("OK: Código experimental coincide com as vistas do índice.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, KeyError, ValueError, json.JSONDecodeError) as e:
        print("FALHA CORPUS:", e, file=sys.stderr)
        sys.exit(1)
