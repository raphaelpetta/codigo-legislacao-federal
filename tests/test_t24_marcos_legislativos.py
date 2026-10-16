#!/usr/bin/env python3
"""Porta adversarial T24 CPC 82/85 — textos de leis alteradoras oficiais, não C0-J.

Enunciados cotejados focalmente em 16/10/2026, independentes da transcrição:
- Lei 15.109/2025 art. 2º (CPC 82 §3º), publicação original Câmara:
  https://www2.camara.leg.br/legin/fed/lei/2025/lei-15109-13-marco-2025-797168-publicacaooriginal-174760-pl.html
- Lei 14.365/2022 art. 3º (CPC 85 §§6º-A, 8º-A e 20), publicação original Câmara:
  https://www2.camara.leg.br/legin/fed/lei/2022/lei-14365-2-junho-2022-792762-publicacaooriginal-165436-pl.html

Confere somente quatro enunciados, suas remissões, a classificação Q,
a matriz de destinos e a vista. NÃO autentica DOU em fac-símile, vigência
integral, precedentes, 75 unidades, revogação, C0-J, M ou DEC-016.
"""
from __future__ import annotations

import csv
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "produto/fontes/T24_CPC_82_97_TEXTO_ATUAL_75_Q.csv"
CROSS = ROOT / "produto/concordancia/T24_CPC_82_97_CONCORDANCIA_75_Q.csv"
VIEW = ROOT / "produto/vistas/T24_CPC_70_102_PREVIA_CONTINUA_Q.md"
MANIFEST = ROOT / "produto/fontes/T24_CPC_70_102_181_v1.json"

# Literais publicados nas leis modificadoras, não gerados do CSV do corpus.
OFICIAIS = {
    "82/P3": ("BR-LEI-2015-13105-ART-0082-P3", "LEI_15109_2025", "Nas ações de cobrança por qualquer procedimento, comum ou especial, bem como nas execuções ou cumprimentos de sentença de honorários advocatícios, o advogado ficará dispensado de adiantar o pagamento de custas processuais, e caberá ao réu ou executado suprir, ao final do processo, o seu pagamento, se tiver dado causa ao processo."),
    "85/P6A": ("BR-LEI-2015-13105-ART-0085-P6A", "LEI_14365_2022", "Quando o valor da condenação ou do proveito econômico obtido ou o valor atualizado da causa for líquido ou liquidável, para fins de fixação dos honorários advocatícios, nos termos dos §§ 2º e 3º, é proibida a apreciação equitativa, salvo nas hipóteses expressamente previstas no § 8º deste artigo."),
    "85/P8A": ("BR-LEI-2015-13105-ART-0085-P8A", "LEI_14365_2022", "Na hipótese do § 8º deste artigo, para fins de fixação equitativa de honorários sucumbenciais, o juiz deverá observar os valores recomendados pelo Conselho Seccional da Ordem dos Advogados do Brasil a título de honorários advocatícios ou o limite mínimo de 10% (dez por cento) estabelecido no § 2º deste artigo, aplicando-se o que for maior."),
    "85/P20": ("BR-LEI-2015-13105-ART-0085-P20", "LEI_14365_2022", "O disposto nos §§ 2º, 3º, 4º, 5º, 6º, 6º-A, 8º, 8º-A, 9º e 10 deste artigo aplica-se aos honorários fixados por arbitramento judicial."),
}


def conferido(texto: str, esperado: str, ident: str) -> None:
    if texto != esperado:
        raise ValueError("Divergência do enunciado oficial fixado em " + ident)


def ler_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle, strict=True))


class MarcoNormativoT24(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.origem = ler_csv(SOURCE)
        cls.destino = ler_csv(CROSS)
        cls.vista = VIEW.read_text(encoding="utf-8")
        cls.manifesto = json.loads(MANIFEST.read_text(encoding="utf-8"))
        cls.por_id = {r["id_origem"]: r for r in cls.origem}
        cls.correspondencias = {r["id_origem"]: r for r in cls.destino}

    def test_universo_75_permanece_q_e_composto(self) -> None:
        self.assertEqual(len(self.origem), 75)
        self.assertEqual(len(self.por_id), 75)
        self.assertEqual(len(self.destino), 75)
        self.assertEqual(len(self.correspondencias), 75)
        self.assertEqual(set(self.por_id), set(self.correspondencias))
        self.assertEqual([c["count"] for c in self.manifesto["components"]], [106, 75])
        self.assertEqual(self.manifesto["status_juridico"], "Q_SEM_C0_J")
        self.assertIs(self.manifesto["material_approved"], False)
        self.assertEqual(self.manifesto["dec016"], "PENDENTE")

    def test_quatro_alteracoes_conferem_com_publicacoes_originais(self) -> None:
        for unidade, (ident, lei, texto) in OFICIAIS.items():
            with self.subTest(unidade=unidade):
                origem = self.por_id[ident]
                self.assertEqual(origem["artigo"] + "/" + origem["subunidade"], unidade)
                self.assertEqual(origem["marco_alterador"], lei)
                self.assertEqual(origem["estado_juridico"], "Q_SEM_C0_J")
                self.assertIn("PENDENTE_COTEJO_DOU", origem["situacao_comparacao"])
                conferido(origem["texto_atual_manual"], texto, ident)
                self.assertEqual(self.vista.count(texto), 1, ident)

    def test_destinos_preservam_literal_e_origem_penalidade_sem_equivalencia(self) -> None:
        for unidade, (ident, lei, texto) in OFICIAIS.items():
            with self.subTest(unidade=unidade):
                item = self.correspondencias[ident]
                self.assertEqual(item["texto_origem_camara_transcrito"], texto)
                self.assertEqual(item["texto_destino_experimental"], texto)
                self.assertEqual(item["estado_juridico"], "Q_SEM_C0_J")
                self.assertEqual(item["destino_experimental"],
                                 "CLF-T24-CPC" + unidade.replace("/", "-").replace("82-", "082-").replace("85-", "085-"))
                self.assertEqual(item["marco"], lei)

    def test_alteracao_do_criterio_de_causalidade_ou_equidade_falha(self) -> None:
        for unidade, corte in (
            ("82/P3", ", se tiver dado causa ao processo."),
            ("85/P6A", ", salvo nas hipóteses expressamente previstas no § 8º deste artigo."),
            ("85/P8A", ", aplicando-se o que for maior."),
            ("85/P20", ", 8º-A,"),
        ):
            ident, _, original = OFICIAIS[unidade]
            self.assertIn(corte, original)
            with self.subTest(ident=ident):
                with self.assertRaisesRegex(ValueError, "Divergência"):
                    conferido(original.replace(corte, "", 1), original, ident)


if __name__ == "__main__":
    unittest.main()
