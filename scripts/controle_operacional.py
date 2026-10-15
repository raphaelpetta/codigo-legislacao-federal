#!/usr/bin/env python3
"""Confere fila cooperativa e gera painel de presenca normativa do checkout.
Nao verifica legalidade, aprovacao material, vigencia ou cobertura exaustiva.
--write reconstroi somente o painel derivado; --check compara sem alterar.
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CF = (ROOT / "redacao/indice.csv").is_file()
PROJECT = "CF" if CF else "CLF"
QUEUE = ROOT / "central/FILA_TRABALHO.csv"
OUTPUT = ROOT / "central/PAINEL_GERADO.csv"
FIELDS = [
    "id", "modulo", "recorte", "estado", "prioridade", "responsavel", "branch",
    "pr", "base_sha", "reserva_ate", "dependencias", "criterio_aceite", "ultima_entrega",
]
STATES = {"PRONTA", "RESERVADA", "EM_EXECUCAO", "EM_REVISAO", "BLOQUEADA", "CONCLUIDA"}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def rows(path: Path) -> list[dict[str, str]]:
    require(path.is_file(), "Arquivo ausente: " + str(path.relative_to(ROOT)))
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle, strict=True)
        names = reader.fieldnames or []
        require(len(names) == len(set(names)), "Cabecalho duplicado: " + str(path))
        data = list(reader)
        for n, row in enumerate(data, 2):
            require(None not in row and all(v is not None for v in row.values()),
                    f"CSV malformado: {path.name}:{n}")
        return data


def check_queue(allowed: set[str]) -> list[str]:
    with QUEUE.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle, strict=True)
        require(reader.fieldnames == FIELDS, "Esquema da fila divergente")
    entries = rows(QUEUE)
    ids: set[str] = set()
    warnings: list[str] = []
    for entry in entries:
        key = entry["id"].strip()
        require(re.fullmatch(PROJECT + r"-[A-Z0-9]+-\d{3}", key) is not None,
                "ID de tarefa invalido: " + key)
        require(key not in ids, "Tarefa duplicada: " + key)
        ids.add(key)
        module = entry["modulo"].strip()
        require(module == "OPS" or module in allowed or
                (not CF and re.fullmatch(r"T\d{2}\.M\d{2}", module) is not None
                 and module[:3] in allowed), "Modulo invalido: " + key)
        state = entry["estado"].strip()
        require(state in STATES, "Estado invalido: " + key)
        require(entry["prioridade"] in {"P0", "P1", "P2"}, "Prioridade invalida: " + key)
        require(entry["recorte"].strip() and entry["criterio_aceite"].strip(),
                "Tarefa sem recorte/criterio: " + key)
        sha = entry["base_sha"].strip()
        require(not sha or re.fullmatch(r"[a-f0-9]{40}", sha) is not None,
                "SHA-base invalido: " + key)
        if state == "PRONTA":
            require(not entry["responsavel"] and not entry["reserva_ate"],
                    "Tarefa PRONTA ainda reservada: " + key)
        if state in {"RESERVADA", "EM_EXECUCAO"}:
            require(bool(entry["responsavel"].strip() and entry["branch"].strip()
                         and entry["reserva_ate"].strip() and sha),
                    "Reserva sem responsavel/branch/SHA/prazo: " + key)
            timestamp = datetime.fromisoformat(entry["reserva_ate"].replace("Z", "+00:00"))
            require(timestamp.tzinfo is not None, "Reserva deve conter fuso: " + key)
            if timestamp < datetime.now(timezone.utc):
                warnings.append("RESERVA EXPIRADA (liberacao humana): " + key)
        if state in {"EM_REVISAO", "CONCLUIDA"}:
            require(entry["pr"].strip() and entry["ultima_entrega"].strip(),
                    "Revisao/conclusao sem evidencia/PR: " + key)
    require(bool(entries), "Fila vazia")
    return warnings


def make_panel() -> tuple[str, set[str]]:
    output = io.StringIO()
    writer = csv.writer(output, lineterminator="\n")
    if CF:
        modules = [r["id_modulo"] for r in rows(ROOT / "catalogo/MODULOS.csv")]
        require(len(modules) == 15 and len(set(modules)) == 15, "Catalogo M00-M14 invalido")
        counts: dict[str, Counter] = defaultdict(Counter)
        for r in rows(ROOT / "redacao/indice.csv"):
            module, state = r["modulo"], r["status"]
            require(module in modules and state in {"H", "P", "D"},
                    "Modulo/status CF-NOR invalidos")
            counts[module][state] += 1
        writer.writerow(["modulo", "unidades_na_fonte_atual", "H", "P", "D"])
        for module in modules:
            c = counts[module]
            writer.writerow([module, sum(c.values()), c["H"], c["P"], c["D"]])
        return output.getvalue(), set(modules)
    titles = [r["id_titulo"] for r in rows(ROOT / "catalogo/02_INDICE_48_TITULOS.csv")]
    require(len(titles) == 48 and len(set(titles)) == 48, "Catalogo de titulos invalido")
    index = json.loads((ROOT / "produto/fontes/indice_livros.json").read_text(encoding="utf-8"))
    require(index.get("schema_version") == 1, "Versao do manifesto invalida")
    books: set[str] = set()
    views: set[str] = set()
    counts: dict[str, Counter] = defaultdict(Counter)
    for book in index["livros"]:
        ident, title, view = book["id"], book["titulo"], book["vista"]
        require(ident not in books and view not in views, "Livro/vista duplicada: " + ident)
        books.add(ident)
        views.add(view)
        require(title in titles and book["estado"].startswith("INTEGRADO_EXPERIMENTAL"),
                "Titulo/estado do livro invalido: " + ident)
        require(re.fullmatch(r"[a-f0-9]{40}", book["origem_commit"]) is not None,
                "Commit setorial invalido: " + ident)
        path = ROOT / view
        require(path.is_file(), "Vista ausente: " + view)
        actual = re.findall(r"(?m)^\*\*Art\. [^\n]+", path.read_text(encoding="utf-8"))
        require(len(actual) == book["artigos"], "Artigos divergentes: " + ident)
        meta = json.loads((ROOT / book["manifesto"]).read_text(encoding="utf-8"))
        require(meta["setorial_commit"] == book["origem_commit"],
                "Manifesto de origem divergente: " + ident)
        require(meta["contagens_esperadas"]["fontes"] == book["registros_documentais"],
                "Universo documental divergente: " + ident)
        require(meta["aprovacao_material"] == "NAO",
                "Corpus experimental nao deve homologar por operacao: " + ident)
        counts[title]["books"] += 1
        counts[title]["articles"] += book["artigos"]
        counts[title]["sources"] += book["registros_documentais"]
    writer.writerow(["id_titulo", "livros_em_vista", "artigos_experimentais",
                     "registros_documentais_na_fonte"])
    for title in titles:
        c = counts[title]
        writer.writerow([title, c["books"], c["articles"], c["sources"]])
    return output.getvalue(), set(titles)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    opt = parser.add_mutually_exclusive_group()
    opt.add_argument("--check", action="store_true", help="Modo padrao: detectar drift")
    opt.add_argument("--write", action="store_true", help="Regerar apenas painel derivado")
    args = parser.parse_args()
    generated, allowed = make_panel()
    warnings = check_queue(allowed)
    if args.write:
        OUTPUT.write_text(generated, encoding="utf-8")
        print("REGERADO:", OUTPUT.relative_to(ROOT))
    else:
        require(OUTPUT.is_file() and OUTPUT.read_text(encoding="utf-8") == generated,
                "PAINEL DIVERGENTE: executar python scripts/controle_operacional.py --write")
        print("OK:", PROJECT, "fila e painel coerentes com as fontes do checkout")
    for warning in warnings:
        print("AVISO:", warning)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (ValueError, OSError, KeyError, csv.Error, json.JSONDecodeError) as exc:
        print("ERRO OPERACIONAL:", exc, file=sys.stderr)
        sys.exit(1)
