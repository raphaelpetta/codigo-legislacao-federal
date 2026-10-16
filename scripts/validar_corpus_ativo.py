#!/usr/bin/env python3
"""CLF — validador de manifestos ativos, adaptativo ao índice de Livros.

Valida integridade documental dos livros do snapshot corrente, sem homologar
DOU, vigência, equivalência jurídica C0-J, decisões judiciais ou CI.
Referências a origens setoriais externas exigem checkouts próprios.
"""
from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
index = json.loads((ROOT / "produto/fontes/indice_livros.json").read_text(encoding="utf-8"))
books = index["livros"]
assert books, "sem livros"
assert len({book["id"] for book in books}) == len(books), "id duplicado"

n_manifestos = 0
n_fontes = 0
pendencias: list[str] = []
for book in books:
    view = ROOT / book["vista"]
    manifest_path = ROOT / book["manifesto"]
    assert view.is_file() and manifest_path.is_file(), book["id"]
    text = view.read_text(encoding="utf-8")
    assert sum(line.startswith("**Art. ") for line in text.splitlines()) == book["artigos"], book["id"]
    m = json.loads(manifest_path.read_text(encoding="utf-8"))
    n_manifestos += 1
    if m.get("material_approved") is True or m.get("dec016") not in (None, "PENDENTE"):
        raise AssertionError("promocao indevida: " + book["id"])
    rel = m.get("source_path")
    sha = m.get("source_blob_sha")
    if rel and sha:
        source = Path(rel)
        if source.is_absolute() or ".." in source.parts:
            raise AssertionError("caminho externo nao declarado: " + book["id"])
        if (ROOT / source).is_file():
            raw = (ROOT / source).read_bytes()
            actual = hashlib.sha1(
                b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw
            ).hexdigest()
            assert actual == sha, "hash divergente " + book["id"]
            if source.suffix.lower() == ".csv" and isinstance(m.get("count_expected"), int):
                with (ROOT / source).open(encoding="utf-8", newline="") as f:
                    records = list(csv.DictReader(f))
                assert len(records) == m["count_expected"], "linhas divergentes " + book["id"]
            n_fontes += 1
        else:
            pendencias.append(book["id"] + ": fonte nao presente neste checkout")
    else:
        pendencias.append(book["id"] + ": origem externa/manifesto sem blob local")

code = (ROOT / "produto/CODIGO_DE_TRABALHO.md").read_text(encoding="utf-8")
first = books[0]
anchor = f"## {first['titulo']} — {first['modulo']} [{first['id']}; {first['estado']}]"
assert anchor in code
prefix = code[:code.index(anchor)]
reconstructed = prefix + "".join(
    f"## {b['titulo']} — {b['modulo']} [{b['id']}; {b['estado']}]\n\n"
    + (ROOT / b["vista"]).read_text(encoding="utf-8").rstrip() + "\n\n"
    for b in books
)
assert reconstructed.rstrip() + "\n" == code, "drift nas vistas"
assert sum(line.startswith("**Art. ") for line in code.splitlines()) == sum(b["artigos"] for b in books)
print(f"SNAPSHOT: {n_manifestos} manifestos, {n_fontes} fontes locais com hash, {len(pendencias)} dependencias externas")
for note in pendencias:
    print("PENDENTE ORIGEM EXTERNA:", note)
print("QA documental; NAO comprova autenticidade DOU, C0-J, CI ou conclusao dos checkouts externos.")
