# Código da Legislação Federal — corpus único experimental (vista de trabalho)

**Corte:** 15/10/2026 · **Estado:** minutas editoriais em PR **draft**, não legislação vigente, nem texto homologado, nem revogações ou atos de promulgação. **DEC-001**: objetivo de corpus único mantido. **DEC-016**: veículo/espécie/iniciativa/veto/transição **pendente**.


## Vista única gerada do corpus efetivamente integrado

[Ler o **Código experimental integrado em texto corrido**](CODIGO_DE_TRABALHO.md), gerado por `python3 scripts/gerar_codigo_integrado.py --write` a partir do [índice de Livros](fontes/indice_livros.json), conferível com `--check`. **Contém T05 (democracia direta, 2 artigos), T07, T24 (CPC 70–102 contínuo) e T25**, todos experimentais Q, sem efeitos legais ou homologação C0-J.

## Ponto de leitura: Código de Trabalho e quatro componentes experimentais

**[Abrir Código de Trabalho unificado (T05 + T07 + T24 + T25, NÃO RATIFICADO)](CODIGO_DE_TRABALHO.md)** — arquivo reconstruível a partir do [índice de Livros](fontes/indice_livros.json) e das vistas fixadas. Nenhum conteúdo experimental foi convertido em norma vigente; a Parte V permanece um recorte incompleto do CPC. Ver [gerador do Código](../scripts/gerar_codigo_integrado.py) e [controle operacional](../scripts/controle_operacional.py).

**Parte II — Instituições e participação política**
- [T05.M06, democracia direta: Lei 9.709/1998 arts. 1º–2º, 2 artigos e 7 unidades Q](vistas/T05_DEMOCRACIA_DIRETA_LEI9709_ART1_2_PREVIA.md), [espelho 7×7](../modulos/T05/M06_ESPELHO_LEI9709_ART1_2_7_Q.csv), [manifesto](fontes/T05_M06_9709_7_v1.json) e [inventário dos seis módulos eleitorais](../modulos/T05/M00_INVENTARIO_SEIS_MODULOS_20261015.csv). [Dossiê de recepção constitucional e anualidade eleitoral 2026](../modulos/T05/NOTA_ABERTURA_2026_RECEPCAO_ANUALIDADE_20261015.md): a mudança do art. 5º do Código Eleitoral em 2026 não foi aplicável às eleições de 2026, segundo o TSE. O Código Eleitoral integral e Lei 9.709 arts.3º–15 **não** foram transpostos.

**Parte III — Administração Pública e Finanças**
- [Livro de Processo Administrativo Federal — T07.M03, prévia integral de 78 artigos](vistas/T07_PROCESSO_ADMINISTRATIVO_PREVIA.md). Proveniência: PR #45, fonte fixa, [manifesto](fontes/T07_M03_v4.json); 214 unidades positivas (203 C0-T local, 11 C1 potenciais/Q), 1 registro histórico, nenhuma unidade C0-J homologada.
- [Auditoria dos 11 C1 potenciais T07](../central/03_T07_GATE_C1_11_EFEITOS_20261015.csv), com efeitos, alternativas conservadoras, provas faltantes e riscos. Os destinatários, o âmbito e a subsidiariedade dos processos especiais permanecem Q.

**Parte V — Direito Internacional Privado, Justiça e Sanções**
- [Livro de Processo Civil — T24.M01, prévia contínua CPC 70–102: **33 artigos e 181 unidades Q**](vistas/T24_CPC_70_102_PREVIA_CONTINUA_Q.md). Combina 106 unidades setoriais do PR #38 e [75 transcrições editoriais](fontes/T24_CPC_82_97_TEXTO_ATUAL_75_Q.csv) em [manifesto de duas proveniências](fontes/T24_CPC_70_102_181_v1.json), com [verificador](../scripts/gerar_t24_cpc_181.py). O cotejo visual com a Câmara foi documentado, mas persistem revisão independente arquivada por extração e cotejo DOU; C0-J=0 e o CPC externo ao recorte não foi transposto.

**Livro Penal T25.M01 (núcleo CP 1º–12)**
- [Prévia parcial do Livro Penal: 12 artigos, 39 unidades](vistas/T25_PENAL_PARTE_GERAL_CP1_12_PREVIA.md), derivada do PR #32 em commit fixado: [manifesto](fontes/T25_CP1_12_v1.json), [concordância 39 × 39](concordancia/T25_CP_ART1_12_39.csv) e [verificador documental](../scripts/gerar_previa_t25.py). **Nenhuma C0-J aprovada; CP art.12 tem gate de especialidade e referente `deste Código`, CPM não integrado.**

**Rastro da ampliação T24**
- [Primeira prévia 106 unidades](vistas/T24_PROCESSO_CIVIL_PREVIA_PARCIAL.md), [prévia intermediária 75](vistas/T24_CPC_82_97_PREVIA_75_Q.md), [concordância 75 × 75](concordancia/T24_CPC_82_97_CONCORDANCIA_75_Q.csv). A antiga [matriz sem texto](concordancia/T24_82_97_GATE_75_SEM_TEXTO.csv) é preservada como histórico de estágio; não representa a cobertura atual.

**Em pesquisa, ainda fora do corpus de leitura:** T01.M04 (formalização/DEC-016), T29 (RGPS), T43 (Governo Digital) e [T13.M01, inventário inicial de 19 unidades CC 1–5](../modulos/T13/M01/NOTA_ABERTURA_CAPACIDADE_CIVIL_20261015.md), entre outras frentes a abrir. Nenhuma dessas pesquisas constitui Livro completo de CLF. O mapa de 48 títulos é provisório, não universo exaustivo da legislação.

## Convenção de proveniência e montagens

- **Fontes canônicas setoriais fixadas por commit**: `integracao/25_...` e `26_...` no PR #45 (T07); `modulos/T24/M01/F1C2_ESPELHO_UNIFICADO_106.csv` no PR #38 (T24: 106 unidades), mais 75 transcrições editoriais locais em CSV com hashes (T24: 82–97). Os arquivos `vistas/` não são fonte paralela editável.
- **T05**: `python3 scripts/gerar_previa_t05.py --check`, com sete unidades e hash da origem editorial local. A transposição documental mantém Q, e o conflito de grafia da publicação original da Lei 9.709 art. 2º segue pendente de DOU.
- **T07**: `python3 scripts/gerar_produto_experimental.py --setorial-root setorial --check` (com o checkout de origem T07 declarado no manifesto); `--write` regenera somente a vista derivada.
- **T24 setorial**: `python3 scripts/gerar_previa_t24.py --setorial-root setorial --check` confere as 106 unidades originais. **T24 integrado**: `python3 scripts/gerar_t24_cpc_181.py --check` confere os dois conjuntos, 33 artigos, 181 destinos, quatro marcos legislativos e hashes de blob; `--write` regenera apenas a vista contínua.
- **CI documental separada:** workflows [T07](../.github/workflows/conferir-produto-experimental.yml), [T24-106](../.github/workflows/conferir-t24-previsao.yml), [T24-181](../.github/workflows/conferir-t24-181.yml) e [T25](../.github/workflows/conferir-t25-previa.yml). As execuções GitHub Actions desta rodada exibiram **failure sem etapas visíveis**; controle independente de correspondência T24 foi efetuado por leitura dos arquivos. **Não declarar CI aprovado nem C0-J**.
- **Produto atual:** [Código de Trabalho unificado](CODIGO_DE_TRABALHO.md) é compilado automaticamente dos quatro componentes parciais indicados em [indice_livros.json](fontes/indice_livros.json), usando `python3 scripts/gerar_codigo_integrado.py --check` ou `--write`. **Produto futuro:** versão comentada com variantes, concordância N:N geral, remissões controladas, lacunas e transições. A compilação atual não constitui código completo, índice jurídico exaustivo ou renumeração final.

## Indicadores, não confundir denominadores

| Objeto | Artigos visíveis na prévia | Unidades positivas | Unidade histórica | C0-J homologadas |
|---|---:|---:|---:|---:|
| T05 — Lei 9.709/1998 (arts. 1º–2º) | 2 | 7 | 0 | 0 |
| T07 — Lei 9.784/1999 | 78 | 214 | 1 | 0 |
| T24 — CPC (arts. 70–102 contínuos) | 33 | 181 | 0 | 0 |
| T25 — CP (arts. 1º–12) | 12 | 39 | 0 | 0 |
| **Total atual das vistas** | **125** | **441** | **1** | **0** |

As 441 unidades são **registros textuais de origens e recortes distintos**, não porcentagem de cobertura do direito federal, artigos renumerados ou normas juridicamente certificadas.

[Central CLF #48](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/48) · [Auditoria dos 48 títulos](../central/01_MATRIZ_AUDITORIA_48_TITULOS_20261015.csv) · [Central CF #103](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/103).
