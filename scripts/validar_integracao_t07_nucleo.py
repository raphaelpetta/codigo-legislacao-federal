#!/usr/bin/env python3
"""Porta estrutural de F5-Q do T07. NÃO audita vigência, DOU, equivalência C0-J ou direito material."""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read_csv(path: str) -> list[dict[str, str]]:
    with (ROOT / path).open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def assert_ids(items: list[dict[str, str]], key: str, expected: int) -> None:
    ids = [x[key] for x in items]
    assert len(ids) == expected, (key, len(ids), expected)
    assert len(set(ids)) == expected, f"Duplicated ids in {key}"
    assert all(ids), f"Empty ID in {key}"


def read_section(path: str, start: str, end: str) -> str:
    full = (ROOT / path).read_text(encoding="utf-8")
    assert start in full and end in full, f"Missing section markers: {path}"
    return full.split(start, 1)[1].split(end, 1)[0]


def main() -> None:
    original = read_csv("modulos/T07/M03/CONCORDANCIA_INTEGRAL_ART1_ART2_13.csv")
    original40 = read_csv("modulos/T07/M03/CONCORDANCIA_LITERAL_ART3_17_15.csv")
    m22 = read_csv("integracao/05_CONCORDANCIA_T07_22_UNIDADES_20261014.csv")
    tests = read_csv("integracao/06_TESTES_ADVERSARIAIS_EXECUTADOS_T07_12.csv")
    m16 = read_csv("integracao/08_CONCORDANCIA_T07_SEGUNDO_NUCLEO_16_UNIDADES.csv")
    assert_ids(original, "id_unidade", 21)
    assert_ids(original40, "id_unidade", 40)
    assert_ids(m22, "id", 22)
    assert_ids(tests, "teste", 12)
    assert_ids(m16, "id_origem", 16)
    assert {t["teste"] for t in tests} == {f"G{i:02d}" for i in range(1, 13)}

    source = {r["id_unidade"]: r["texto_fonte_literal"] for r in original}
    main_norm = read_section(
        "integracao/03_PILOTO_T07_PRIMEIRO_NUCLEO_20261014.md",
        "## 2. Minuta F5-Q",
        "## 3. Concordância",
    )
    deltas = {}
    for row in m22:
        if row["id"] == "P19-69-C":
            assert row["origem"].lower().startswith("lei 9.784/1999 art. 69")
        else:
            assert row["id"] in source
            assert row["texto_origem"] == source[row["id"]]
        assert row["texto_destino"] in main_norm, row["id"]
        assert row["estado_juridico"] == "Q_SEM_C0_J", row["id"]
        deltas[row["delta"]] = deltas.get(row["delta"], 0) + 1
    assert deltas == {
        "REFERENTE_LEI_PARA_LIVRO": 3,
        "PONTUACAO_HIFEN_PARA_DOIS_PONTOS": 3,
        "SEM_DELTA_LOCAL": 15,
        "REPOSICIONAMENTO_E_REFERENTE_LEI_PARA_LIVRO": 1,
    }, deltas
    assert all(x["homologacao_juridica"] == "Q_NAO_HOMOLOGADO" for x in tests)

    norm16 = read_section(
        "integracao/09_T07_DIREITOS_INTERESSADOS_COMPETENCIA_F5Q.md",
        "## 2. Minuta experimental",
        "## 3. Controles jurídico-materiais",
    )
    source40 = {r["id_unidade"]: r["texto_fonte_literal"] for r in original40}
    for row in m16:
        assert row["id_origem"] in source40
        assert row["texto_origem"] == source40[row["id_origem"]]
        assert row["texto_destino"] in norm16, row["id_origem"]
        assert row["classe"] == "C0_T_LOCAL;C0_J_Q"
        assert row["homologacao"] == "NAO"
    assert set(x["id_origem"].split("-")[1] for x in m16) == {"3", "4", "9", "11"}

    # Rodada 03: validação dos 24 antes faltantes, 40 completos, 18 artigos e 16 testes.
    pending24 = read_csv("integracao/10_T07_COMPLEMENTO_24_UNIDADES_F5Q.csv")
    full40 = read_csv("integracao/11_T07_CONCORDANCIA_UNIFICADA_40_UNIDADES_F5Q.csv")
    tests16 = read_csv("integracao/13_TESTES_T07_REQUERIMENTOS_CAPACIDADE_COMPETENCIA.csv")
    assert_ids(pending24, "id_origem", 24)
    assert_ids(full40, "id_origem", 40)
    assert_ids(tests16, "teste", 16)
    assert {x["teste"] for x in tests16} == {f"G{i:02d}" for i in range(13, 29)}
    orig40 = {x["id_unidade"]: x for x in original40}
    full = {x["id_origem"]: x for x in full40}
    prev_ids = {x["id_origem"] for x in m16}
    new_ids = {x["id_origem"] for x in pending24}
    assert prev_ids.isdisjoint(new_ids), "Os 24 não podem duplicar os 16 anteriores"
    assert set(full) == prev_ids | new_ids == set(orig40), "Cobertura 40/40 incompleta"
    assert len({x["destino"] for x in full40}) == 40, "Destinos repetidos"
    for row in full40:
        assert row["texto_origem"] == orig40[row["id_origem"]]["texto_fonte_literal"]
        assert row["texto_destino"] == row["texto_origem"]
        assert row["status_juridico"] == "Q_C0J_NAO_VERIFICADO"
        assert row["situacao"] == "NAO_APROVADO_NAO_PROMULGADO"
        assert row["destino"].startswith("LPA-SEQ-")
    for row in pending24:
        assert row == full[row["id_origem"]], row["id_origem"]

    sequential = read_section(
        "integracao/12_T07_LIVRO_SEQUENCIAL_ARTS1_17_69_F5Q.md",
        "## I — Âmbito e princípios",
        "## VII — Problemas jurídicos que impedem aprovar a transposição",
    )

    def article_segment(n: int) -> str:
        prefix = f"**Art. LPA-SEQ-{n:03d}.**"
        assert sequential.count(prefix) == 1, prefix
        block = sequential.split(prefix, 1)[1]
        if n < 18:
            block = block.split(f"**Art. LPA-SEQ-{n + 1:03d}.**", 1)[0]
        return block

    assert sequential.count("**Art. LPA-SEQ-") == 18
    for row in full40:
        n = int(row["destino"].split("-")[2])
        assert row["texto_destino"] in article_segment(n), row["id_origem"]
    for row in m22:
        if row["id"] == "P19-69-C":
            n = 18
        else:
            n = int(row["id"].split("-")[1])
        assert row["texto_destino"] in article_segment(n), row["id"]
    assert "unidade fundacional competente" in article_segment(16), "Art.16 fonte não preservada"

    for row in tests16:
        n = int(row["artigo_lpa"].split("-")[2])
        assert row["expressao_direito_positivo_preservada"] in article_segment(n), row["teste"]
        assert row["marcador_textual_verificado"] == "SIM"
        assert row["status_homologacao"] == "Q_SEM_C0_J"
        assert row["status_teste_textual"] in {
            "PASSA_NO_RECORTE", "PASSA_COM_RESSALVA", "CONDICIONAL_DIREITO_EXTERNO"
        }
    assert len({x["id"] for x in m22} | set(full)) == 62
    print("OK rodada 03: 24 novos + 16 anteriores = 40/40; 62 unidades em 18 artigos; 16 testes estáticos.")

    # Rodada 04 — 15/10/2026: integração documental dos arts.18–28, sem C0-J.
    source215 = read_csv("modulos/T07/M03/MATRIZ_TRIAGEM_215_UNIDADES_CICLO20.csv")
    m33 = read_csv("integracao/15_T07_CONCORDANCIA_ART18_28_33_UNIDADES.csv")
    tests20 = read_csv("integracao/17_T07_TESTES_INTIMACAO_IMPARCIALIDADE_20.csv")
    assert_ids(source215, "id_espelho", 215)
    assert_ids(m33, "id_origem", 33)
    assert_ids(tests20, "id_teste", 20)
    assert {r["id_teste"] for r in tests20} == {f"N{i:02d}" for i in range(1,21)}
    src215 = {x["id_espelho"]: x for x in source215}
    assert set(x["id_origem"] for x in m33).isdisjoint(set(full)), "colisão de 33 vs 40"
    assert set(x["id_origem"] for x in m33).isdisjoint(set(x["id"] for x in m22)), "colisão 33 vs 22"
    for x in m33:
        assert x["id_origem"] in src215, x["id_origem"]
        assert x["texto_fonte_literal"] == src215[x["id_origem"]]["texto_fonte"], x["id_origem"]
        assert x["texto_destino_experimental"] == x["texto_fonte_literal"], x["id_origem"]
        assert x["equivalencia_juridica"] == "Q_NAO_AUDITADA", x["id_origem"]
        assert x["classificacao_editorial"] == "C0_T_LOCAL_NAO_C0_J"
        a = int(x["artigo_origem"])
        assert 18 <= a <= 28
        assert x["destino"].startswith(f"LPA-SEQ2-{a:03d}-")

    seq2 = read_section(
        "integracao/16_T07_LIVRO_SEQUENCIAL_ARTS1_28_69_F5Q_V2.md",
        "## I. Âmbito e princípios",
        "## X. Advertências de efeitos",
    )

    def seq2_article(n: int) -> str:
        head = f"**Art. LPA-SEQ2-{n:03d}.**"
        assert seq2.count(head) == 1, head
        body = seq2.split(head, 1)[1]
        if n < 29:
            # Seções podem aparecer antes do artigo seguinte; nenhum texto de origem é omitido.
            body = body.split(f"**Art. LPA-SEQ2-{n + 1:03d}.**", 1)[0]
        return body

    assert seq2.count("**Art. LPA-SEQ2-") == 29
    for x in m22:
        n = 29 if x["id"] == "P19-69-C" else int(x["id"].split("-")[1])
        assert x["texto_destino"] in seq2_article(n), x["id"]
    for x in full40:
        n = int(x["id_origem"].split("-")[1])
        assert x["texto_destino"] in seq2_article(n), x["id_origem"]
    for x in m33:
        n = int(x["artigo_origem"])
        assert x["texto_destino_experimental"] in seq2_article(n), x["id_origem"]
    assert len(set(x["id"] for x in m22) | set(full) | set(x["id_origem"] for x in m33)) == 95
    assert "três dias úteis quanto à data de comparecimento" in seq2_article(26)
    assert "comparecimento do administrado supre sua falta ou irregularidade" in seq2_article(26)
    assert "não importa o reconhecimento da verdade dos fatos" in seq2_article(27)
    assert "sem efeito suspensivo" in seq2_article(21)
    for row in tests20:
        n = int(row["origem_artigo"].split("art.")[1])
        assert row["fragmento_verificado"] in seq2_article(n), row["id_teste"]
        assert row["prova_texto"] == "SIM"
        assert row["homologacao"] == "Q_NENHUMA"
        assert row["origem_dados"] == "SIMULACAO_DOCUMENTAL_NAO_PROCESSO_REAL"
    print("OK rodada 04: 33/33 arts18-28; 95/215 origens; 29 artigos em v2; 20 contraprovas estáticas.")


    print("OK: 21 origens + art. 69 = 22 destinos, 12 testes, 16 unidades do bloco seguinte")
    print("IMPORTANTE: controle documental/estrutural, sem homologação de C0-J ou decisão DEC-016.")


if __name__ == "__main__":
    main()
