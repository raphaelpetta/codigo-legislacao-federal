#!/usr/bin/env python3
"""Controle puramente estrutural do ensaio T07 v4 (sem certificação jurídica)."""
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV = ROOT / "integracao/25_T07_CONCORDANCIA_TOTAL_215_F5Q_V4.csv"
BOOK = ROOT / "integracao/26_T07_LIVRO_COMPLETO_1_69A_F5Q_V4.md"

with CSV.open(encoding="utf-8", newline="") as stream:
    rows = list(csv.DictReader(stream))
text = BOOK.read_text(encoding="utf-8")
assert len(rows) == 215, f"Esperadas 215 unidades, encontradas {len(rows)}"

articles = []
for i in range(1, 70):
    articles.append(str(i))
    if i == 49:
        articles.extend(["49-A", "49-B", "49-D", "49-E", "49-F", "49-G"])
    if i == 64:
        articles.extend(["64-A", "64-B"])
    if i == 69:
        articles.append("69-A")
assert len(articles) == 78

seen_ids = set()
seen_origins = set()
by_article = {}
history = []
for item in rows:
    ident = item["id_fonte"]
    art = item["artigo_origem"]
    unit = item["subunidade_origem"]
    pair = (art, unit)
    assert ident and ident not in seen_ids, f"ID vazio/repetido: {ident}"
    assert pair not in seen_origins, f"Dispositivo duplicado: {pair}"
    seen_ids.add(ident)
    seen_origins.add(pair)
    assert item["status_juridico"] == "Q_SEM_C0_J", ident
    assert item["situacao"] == "NAO_APROVADO_NAO_PROMULGADO", ident
    assert item["texto_fonte_arquivado"] and item["fonte_matriz"], ident

    if art == "70":
        history.append(item)
        assert ident == "C19-70-C", ident
        assert item["destino_experimental"] == "HIST-LEI9784-ART70", ident
        assert item["categoria_preliminar"] == "HISTORICO", ident
        continue

    assert art in articles, f"Posicao de artigo desconhecida: {art}"
    expected = f"LPA-SEQ4-{articles.index(art) + 1:03d}-{unit}"
    assert item["destino_experimental"] == expected, (ident, expected)
    assert item["texto_destino_experimental"] in text, f"Destino textual ausente: {ident}"
    by_article.setdefault(art, set()).add(unit)

assert len(history) == 1, f"Registros de vigencia historica: {len(history)}"
assert len(rows) - len(history) == 214
assert all("C" in by_article.get(art, set()) for art in articles), "Artigo sem caput"
assert "49-C" not in by_article, "49-C integralmente vetado foi recuperado"

found = re.findall(r"\*\*Art\. LPA-SEQ4-(\d{3})\.\*\*", text)
expected_articles = [f"{i:03d}" for i in range(1, 79)]
assert found == expected_articles, f"Artigos fora da sequencia esperada: {found}"
assert "**Art. LPA-SEQ4-079." not in text
assert "HIST-LEI9784-ART70" in text
assert "DEC-016" in text
assert "Q_SEM_C0_J" in text
for art in ("49-A", "49-B", "49-D", "69"):
    assert art in by_article

# Legística do art. 49-A § 6º, sem alterar o conteúdo da fonte.
art49a = text.split("**Art. LPA-SEQ4-050.**", 1)[1].split("**Art. LPA-SEQ4-051.**", 1)[0]
assert "**§ 6º** Não se aplica a decisão coordenada aos processos administrativos:" in art49a
for unit, body in (("I", "de licitação;"), ("II", "relacionados ao poder sancionador; ou"), ("III", "em que estejam envolvidas autoridades de Poderes distintos.")):
    assert f"**{unit} –** {body}" in art49a, f"Subinciso §6 ausente: {unit}"
    assert f"**§ 6º, {unit} –**" not in art49a, f"Marcador invalido: {unit}"


# Legística do parágrafo único do art. 2 da Lei 9.784; preservam-se textos e IDs.
art2 = text.split("**Art. LPA-SEQ4-002.**", 1)[1].split("## II. Direitos e deveres", 1)[0]
assert "**Parágrafo único.** Nos processos administrativos serão observados, entre outros, os critérios de:" in art2
for indice in ("I", "II", "III", "IV", "V", "VI", "VII", "VIII",
               "IX", "X", "XI", "XII", "XIII"):
    assert f"**{indice} –**" in art2, indice
    assert f"**PU-{indice} –**" not in art2, indice

print("T07 v4: 215 unidades, 214 com destino textual + 1 historica, 78 artigos em ordem, nenhuma homologacao declarada.")
