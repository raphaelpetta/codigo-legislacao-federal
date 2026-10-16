#!/usr/bin/env python3
"""CLF: integridade documental do snapshot ATIVO, sem homologacao juridica.

Fontes setoriais externas T07/T25 e o bloco composto T24 sao portas
explicitas; nenhum manifesto sem origem pode ser aceito silenciosamente.
Nenhum resultado deste teste autentica DOU, competencia, efeito ou C0-J.
"""
from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

R = Path(__file__).resolve().parents[1]
books = json.loads((R / "produto/fontes/indice_livros.json").read_text(encoding="utf-8"))["livros"]
assert books and len({b["id"] for b in books}) == len(books)
assert all(b["estado"].startswith("INTEGRADO_EXPERIMENTAL") for b in books)

def safe(path: str) -> Path:
    p = Path(path)
    assert not p.is_absolute() and ".." not in p.parts and str(p) not in ("", "."), path
    return R / p

def blob_sha(p: Path) -> str:
    raw = p.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw).hexdigest()

def check_blob(path: str, digest: str) -> None:
    p = safe(path)
    assert p.is_file(), f"arquivo local ausente: {path}"
    assert blob_sha(p) == digest, f"hash divergente: {path}"

def check_csv_count(path: str, expected: int) -> None:
    with safe(path).open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f, strict=True))
    assert len(rows) == expected, f"contagem divergente: {path} ({len(rows)} != {expected})"

n_local = 0
n_external = 0
n_composite = 0
n_composite_objects = 0
for book in books:
    m = json.loads(safe(book["manifesto"]).read_text(encoding="utf-8"))
    view = safe(book["vista"])
    assert view.is_file(), book["id"]
    text = view.read_text(encoding="utf-8")
    assert sum(t.startswith("**Art. ") for t in text.splitlines()) == book["artigos"], book["id"]
    path_in_manifest = m.get("view_path", m.get("vista_relativa"))
    if path_in_manifest is not None:
        assert path_in_manifest == book["vista"], book["id"]
    legal = m.get("legal_status", m.get("status_juridico", m.get("estado_juridico")))
    assert legal in (None, "Q_SEM_C0_J"), (book["id"], legal)
    assert m.get("dec016") == "PENDENTE", book["id"]
    assert m.get("material_approved", False) is not True
    assert m.get("aprovacao_material", "NAO") != "SIM"
    if book["titulo"] == "T07" and m.get("texto_blob_sha"):
        assert m["setorial_commit"] == "2a4d1eefa864f44435aec70ed0cc55a96b718b64"
        assert m["texto_blob_sha"] == "0eea9c97a110d278d6eb4efd37f4a8bbfd61ecb0"
        assert m["concordancia_blob_sha"] == "c9cbf7d202ea9d01b9ffd48256bf3efeba6f226c"
        assert m["contagens_esperadas"]["fontes"] == 215
        assert m["contagens_esperadas"]["historicas"] == 1
        n_external += 1
    elif book["manifesto"] == "produto/fontes/T25_CP1_12_v1.json":
        assert m["setorial_commit"] == "3f0b56273caebfdbaba87ec4e87988da9f12c6c9"
        assert m["source_blob_sha"] == "40b5c03d72f975aad1339c605399f7f66ec056d0"
        assert m["count_expected"] == 39
        assert m["articles_expected"] == 12
        n_external += 1
    elif book["titulo"] == "T24" and m.get("components"):
        components = m["components"]
        assert len(components) == 2
        assert {c["name"] for c in components} == {"PR38_106", "CLF_75"}
        assert sum(c["count"] for c in components) == m["count_expected"] == book["registros_documentais"]
        assert sum(c["articles"] for c in components) == m["articles_expected"] == book["artigos"]
        assert m["setorial_commit"] == "3fdbfa10b8d288b1cef56c78b47cf3cb1eb28745"
        sub = json.loads(safe("produto/fontes/T24_M01_106_v1.json").read_text(encoding="utf-8"))
        assert sub["source_blob_sha"] == "a0562c236cda3a49b842417bb27417e84484f363"
        assert sub["setorial_commit"] == m["setorial_commit"] and sub["count_expected"] == 106
        for c in components:
            for loc, h in [("path", "git_blob"),
                           ("concordance_path", "concordance_git_blob"),
                           ("view_part_path", "view_part_git_blob")]:
                if c.get(loc):
                    check_blob(c[loc], c[h])
                    n_composite_objects += 1
            if c["name"] == "CLF_75":
                check_csv_count(c["path"], 75)
                check_csv_count(c["concordance_path"], 75)
            elif c["name"] == "PR38_106":
                check_csv_count(c["concordance_path"], 106)
        n_composite += 1
    else:
        path = m.get("source_path")
        sha = m.get("source_blob_sha")
        assert path and sha, f"fonte sem SHA/caminho: {book['id']}"
        check_blob(path, sha)
        if str(path).endswith(".csv") and isinstance(m.get("count_expected"), int):
            check_csv_count(path, m["count_expected"])
        n_local += 1

first = books[0]
code = (R / "produto/CODIGO_DE_TRABALHO.md").read_text(encoding="utf-8")
anchor = f"## {first['titulo']} — {first['modulo']} [{first['id']}; {first['estado']}]"
prefix = code[:code.index(anchor)]
expected = prefix + "".join(
    f"## {b['titulo']} — {b['modulo']} [{b['id']}; {b['estado']}]\n\n"
    + safe(b["vista"]).read_text(encoding="utf-8").rstrip() + "\n\n"
    for b in books
)
assert expected.rstrip() + "\n" == code
assert sum(t.startswith("**Art. ") for t in code.splitlines()) == sum(b["artigos"] for b in books)
assert n_local + n_external + n_composite == len(books)
print(f"R26 QA SNAPSHOT: {len(books)} manifestos; {n_local} fontes locais, "
      f"{n_external} origens setoriais externas, {n_composite} composto "
      f"com {n_composite_objects} objetos Git locais cotejados.")
print("FONTES EXTERNAS ainda requerem checkouts imutaveis T07/T24/T25.")
print("QA DOCUMENTAL != DOU, CI verde, equivalencia juridica C0-J ou DEC016.")
