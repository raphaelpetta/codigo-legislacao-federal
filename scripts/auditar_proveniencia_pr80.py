#!/usr/bin/env python3
"""Auditoria documental forense de todos os manifestos do PR #80.

Confronta os arquivos e hashes da fotografia PR80 com commits históricos
explicitamente alegados. NÃO comprova DOU, vigência ou equivalência C0-J.
Uma origem local atual válida não prova que já existia no commit alegado.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import subprocess

SHA = re.compile(r"^[0-9a-f]{40}$")
ROOT_REPO = Path(__file__).resolve().parents[1]
PIN_PR80 = "d1d733561944d67d3d3ffa13c32763784d5cdb6c"

def demand(condition: bool, reason: str) -> None:
    if not condition:
        raise ValueError(reason)

def safe(root: Path, rel: str) -> Path:
    demand(isinstance(rel, str) and bool(rel) and
           not Path(rel).is_absolute() and '..' not in Path(rel).parts,
           f"Caminho documental inseguro: {rel!r}")
    result = (root / rel).resolve()
    demand(result.is_relative_to(root.resolve()),
           f"Fonte fora do checkout: {rel}")
    return result

def blob(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

def git(repo: Path, *args: str) -> str | None:
    p = subprocess.run(["git", "-C", str(repo), *args],
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                       text=True, check=False)
    return p.stdout.strip() if p.returncode == 0 else None

def historical_blob(repo: Path, commit: str, relative: str) -> tuple[str, str | None]:
    demand(bool(SHA.fullmatch(commit)), f"Commit declarado inválido: {commit!r}")
    if git(repo, "cat-file", "-e", commit + "^{commit}") is None:
        return "COMMIT_NAO_RESOLVIDO", None
    obj = git(repo, "rev-parse", "--verify", commit + ":" + relative)
    if obj is None or not SHA.fullmatch(obj):
        return "CAMINHO_NAO_EXISTIA_NO_COMMIT", None
    return "PRESENTE_NO_COMMIT", obj

def inspect(root: Path, *, require_head: str | None = None) -> dict:
    root = root.resolve()
    demand(root.is_dir(), f"Checkout PR80 ausente: {root}")
    head = git(root, "rev-parse", "HEAD")
    demand(head is not None and SHA.fullmatch(head), "Checkout Git íntegro obrigatório")
    if require_head:
        demand(head == require_head, f"HEAD experimental divergiu: {head}")
    index = json.loads(safe(root, "produto/fontes/indice_livros.json").read_text(encoding="utf-8"))
    demand(index.get("schema_version") == 1 and isinstance(index.get("livros"), list),
           "Índice PR80 inválido")
    books = index["livros"]
    demand(len(books) == 60, f"Universo PR80 distinto de 60: {len(books)}")
    seen, entries = set(), []
    for book in books:
        ident = book["id"]
        demand(ident not in seen, f"Livro duplicado: {ident}")
        seen.add(ident)
        manifest_path = book["manifesto"]
        m = json.loads(safe(root, manifest_path).read_text(encoding="utf-8"))
        view = safe(root, book["vista"])
        demand(view.is_file(), f"Vista ausente: {ident}")
        count = sum(x.startswith("**Art. ") for x in view.read_text(encoding="utf-8").splitlines())
        demand(count == book["artigos"], f"Artigos divergentes: {ident}")
        demand(str(book.get("estado", "")).startswith("INTEGRADO_EXPERIMENTAL"),
               f"Estado editorial indevidamente promovido: {ident}")
        demand(m.get("material_approved") is not True and m.get("aprovacao_material") != "SIM"
               and m.get("dec016") in (None, "PENDENTE"), f"Homologação sem autorização: {ident}")
        legal = next((m.get(k) for k in ("legal_status", "estado_juridico", "status_juridico")
                      if m.get(k)), None)
        demand(legal == "Q_SEM_C0_J", f"Natureza jurídica não Q: {ident}")
        src_rel, expected = m.get("source_path"), m.get("source_blob_sha")
        declared = m.get("source_commit") or book.get("origem_commit") or m.get("setorial_commit")
        if declared is not None:
            demand(bool(SHA.fullmatch(str(declared))), f"SHA de commit malformado: {ident}")
        outcome = {
            "id": ident, "titulo": book["titulo"], "manifesto": manifest_path,
            "origem_declarada": declared, "source_path": src_rel,
            "blob_declarado": expected, "situacao": "", "blob_atual": None,
            "blob_no_commit_alegado": None, "nota": "",
        }
        if m.get("components"):
            comps = m["components"]
            demand(isinstance(comps, list) and comps, f"Composto vazio: {ident}")
            for comp in comps:
                for filename, digest in (("path", "git_blob"),
                                         ("concordance_path", "concordance_git_blob"),
                                         ("view_part_path", "view_part_git_blob")):
                    if comp.get(filename) and comp.get(digest):
                        local_file = safe(root, comp[filename])
                        demand(local_file.is_file() and blob(local_file) == comp[digest],
                               f"Drift em componente local {ident}: {comp[filename]}")
            outcome["situacao"] = "COMPOSTO_MULTIPLAS_FONTES_PENDENTE"
            outcome["nota"] = "Componentes locais por blob; fonte externa e revisão DOU não certificadas"
        elif src_rel and expected:
            demand(bool(SHA.fullmatch(str(expected))), f"Blob inválido: {ident}")
            file = safe(root, src_rel)
            if not file.is_file():
                outcome["situacao"] = "FONTE_SETORIAL_EXTERNA"
                outcome["nota"] = "Fonte não existe na árvore PR80; exige checkout externo e gate setorial"
            else:
                actual = blob(file)
                outcome["blob_atual"] = actual
                demand(actual == expected, f"BLOB ATUAL DIVERGE do manifesto: {ident} {src_rel}")
                if not declared:
                    outcome["situacao"] = "SEM_ANCORA_HISTORICA_DECLARADA"
                    outcome["nota"] = "Blob atual íntegro; sem commit original identificável"
                else:
                    result, historical = historical_blob(root, declared, src_rel)
                    outcome["blob_no_commit_alegado"] = historical
                    outcome["situacao"] = ({
                        "COMMIT_NAO_RESOLVIDO": "COMMIT_HISTORICO_NAO_VERIFICAVEL",
                        "CAMINHO_NAO_EXISTIA_NO_COMMIT": "ANCORA_ANTERIOR_AO_ARQUIVO",
                    }.get(result) if result != "PRESENTE_NO_COMMIT" else
                        ("ANCORA_COM_BLOB_IDENTICO" if historical == expected else
                         "ANCORA_COM_BLOB_DIFERENTE"))
                    outcome["nota"] = ({
                        "ANCORA_COM_BLOB_IDENTICO": "Hash atual também existe no commit declarado",
                        "ANCORA_COM_BLOB_DIFERENTE": "Commit continha outra versão, não esta fotografia",
                        "ANCORA_ANTERIOR_AO_ARQUIVO": "O caminho não existia no commit declarado",
                        "COMMIT_HISTORICO_NAO_VERIFICAVEL": "Objeto não resolvido no checkout Git completo",
                    }[outcome["situacao"]])
        elif m.get("texto_relativo") and m.get("texto_blob_sha") and m.get("concordancia_relativa"):
            outcome["situacao"] = "FONTE_SETORIAL_EXTERNA"
            outcome["nota"] = "Texto e concordância T07 permanecem na fonte setorial; verificar por checkout externo"
        else:
            # Não inventar SHA nem classificar como verificada fonte sem hash.
            outcome["situacao"] = "SEM_ESPELHO_LOCAL_COM_HASH"
            outcome["nota"] = "Manifesto sem fonte literal local e hash auditável neste checkout"
        entries.append(outcome)
    counts = dict(sorted(Counter(e["situacao"] for e in entries).items()))
    return {
        "schema_version": 1, "snapshot_pr80_sha": head,
        "natureza": "AUDITORIA_DE_PROVENIENCIA_DOCUMENTAL_NAO_C0_J",
        "quantidade_livros": len(entries),
        "quantidade_titulos": len({e["titulo"] for e in entries}),
        "status_juridico": "Q_SEM_C0_J", "dec016": "PENDENTE",
        "contagens_por_situacao": counts, "livros": entries,
    }

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--experimental-root", required=True, type=Path)
    parser.add_argument("--head", default=PIN_PR80)
    parser.add_argument("--report", type=Path)
    a = parser.parse_args()
    try:
        report = inspect(a.experimental_root, require_head=a.head)
        if a.report:
            a.report.parent.mkdir(parents=True, exist_ok=True)
            a.report.write_text(json.dumps(report, ensure_ascii=False, indent=2,
                                          sort_keys=True) + "\n", encoding="utf-8")
        print("AUDITORIA PR80 CONCLUIDA (NÃO C0-J): " +
              json.dumps({k: v for k, v in report.items() if k != "livros"},
                         ensure_ascii=False, sort_keys=True))
        for item in report["livros"]:
            if item["situacao"] not in ("ANCORA_COM_BLOB_IDENTICO",):
                print("PENDENCIA: " + item["id"] + " | " + item["situacao"] +
                      " | commit=" + str(item["origem_declarada"]) +
                      " | fonte=" + str(item["source_path"]))
    except (ValueError, OSError, TypeError, KeyError, json.JSONDecodeError) as exc:
        parser.exit(1, f"FALHA DE INTEGRIDADE PR80: {exc}\n")

if __name__ == "__main__":
    main()
