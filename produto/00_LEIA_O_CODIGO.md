# Código da Legislação Federal — corpus único experimental (vista de trabalho)

**Corte:** 15/10/2026 · **Estado:** minutas editoriais em PR **draft**, não legislação vigente, nem texto homologado, nem revogações ou atos de promulgação. **DEC-001**: objetivo de corpus único mantido. **DEC-016**: veículo/espécie/iniciativa/veto/transição **pendente**.


## Vista única gerada do corpus efetivamente integrado

[Ler o **Código experimental integrado em texto corrido**](CODIGO_DE_TRABALHO.md), gerado por `python3 scripts/gerar_codigo_integrado.py --write` a partir do [índice de Livros](fontes/indice_livros.json), conferível com `--check`. **Contém T05 (15 artigos da Lei 9.709), T07, T24 (CPC 70–102), T25, T28 (CLT arts. 1º–3º), T37 (PNMA arts. 1º–4º) e T48 (Lei 9.474/1997, arts. 1º–10 e 17–21)**, todos experimentais Q, sem efeitos legais ou homologação C0-J.

## Ponto de leitura: Código de Trabalho e onze componentes experimentais em sete títulos

**[Abrir Código de Trabalho unificado (T05 + T07 + T24 + T25 + T28 + T37 + T48, NÃO RATIFICADO)](CODIGO_DE_TRABALHO.md)** — arquivo reconstruível a partir do [índice de Livros](fontes/indice_livros.json) e das vistas fixadas. Nenhum conteúdo experimental foi convertido em norma vigente; a Parte V permanece um recorte incompleto do CPC. Ver [gerador do Código](../scripts/gerar_codigo_integrado.py) e [controle operacional](../scripts/controle_operacional.py).

**Parte II — Instituições e participação política**
- [T05.M06, suplemento documental dos arts. 3º–15 da Lei 9.709/1998: 13 artigos e 23 unidades Q](vistas/T05_DEMOCRACIA_DIRETA_LEI9709_ART3_15_PREVIA_Q.md), [espelho 23×23](../modulos/T05/M06_ESPELHO_LEI9709_ART3_15_23_Q.csv) e [manifesto SHA](fontes/T05_M06_9709_23_v1.json). **DOU pendente**, divergências arts. 2º/3º/8º IV abertas; art. 15 tem efeito temporal original de 1998. O título T05 passa a ter **15 artigos e 30 unidades documentais Q** de uma única lei, em duas vistas. Nenhum C0-J.
- [T05.M06, democracia direta: Lei 9.709/1998 arts. 1º–2º, 2 artigos e 7 unidades Q](vistas/T05_DEMOCRACIA_DIRETA_LEI9709_ART1_2_PREVIA.md), [espelho 7×7](../modulos/T05/M06_ESPELHO_LEI9709_ART1_2_7_Q.csv), [manifesto](fontes/T05_M06_9709_7_v1.json) e [inventário dos seis módulos eleitorais](../modulos/T05/M00_INVENTARIO_SEIS_MODULOS_20261015.csv). [Dossiê de recepção constitucional e anualidade eleitoral 2026](../modulos/T05/NOTA_ABERTURA_2026_RECEPCAO_ANUALIDADE_20261015.md): a mudança do art. 5º do Código Eleitoral em 2026 não foi aplicável às eleições de 2026, segundo o TSE. O Código Eleitoral integral **não** foi transposto; os arts. 3º–15 da Lei 9.709 foram integrados **apenas como reprodução experimental Q**.

**Parte III — Administração Pública e Finanças**
- [Livro de Processo Administrativo Federal — T07.M03, prévia integral de 78 artigos](vistas/T07_PROCESSO_ADMINISTRATIVO_PREVIA.md). Proveniência: PR #45, fonte fixa, [manifesto](fontes/T07_M03_v4.json); 214 unidades positivas (203 C0-T local, 11 C1 potenciais/Q), 1 registro histórico, nenhuma unidade C0-J homologada.
- [Auditoria dos 11 C1 potenciais T07](../central/03_T07_GATE_C1_11_EFEITOS_20261015.csv), com efeitos, alternativas conservadoras, provas faltantes e riscos. Os destinatários, o âmbito e a subsidiariedade dos processos especiais permanecem Q.

**Parte V — Direito Internacional Privado, Justiça e Sanções**
- [Livro de Processo Civil — T24.M01, prévia contínua CPC 70–102: **33 artigos e 181 unidades Q**](vistas/T24_CPC_70_102_PREVIA_CONTINUA_Q.md). Combina 106 unidades setoriais do PR #38 e [75 transcrições editoriais](fontes/T24_CPC_82_97_TEXTO_ATUAL_75_Q.csv) em [manifesto de duas proveniências](fontes/T24_CPC_70_102_181_v1.json), com [verificador](../scripts/gerar_t24_cpc_181.py). O cotejo visual com a Câmara foi documentado, mas persistem revisão independente arquivada por extração e cotejo DOU; C0-J=0 e o CPC externo ao recorte não foi transposto.

**Parte VI — Trabalho e relações laborais**

- [T28.M01 — CLT, arts. 1º–3º, **3 artigos e 7 unidades Q**](vistas/T28_CLT_ART1_3_PREVIA_Q.md), [espelho 7×7](../modulos/T28/M01_ESPELHO_CLT_ART1_3_7_Q.csv) e [manifesto/hash](fontes/T28_M01_CLT_7_R11_v1.json). Distinção entre decreto-lei de aprovação e CLT, requisitos para relação de emprego, grupo econômico após a Lei 13.467/2017. **PEC 221/2019, fim da escala 6×1:** dois turnos aprovados no Senado em 14/10/2026; **sem promulgação comprovada em 15/10/2026**, portanto não altera a versão do Código como norma vigente. Sem C0-J.

**Parte VII — Território, ambiente e infraestrutura**

- [T37.M01 — Política Nacional do Meio Ambiente, Lei 6.938/1981 arts. 1º–2º, 2 artigos e 13 unidades Q](vistas/T37_PNMA_ART1_2_PREVIA_Q.md); [espelho 13×13](../modulos/T37/M01_ESPELHO_PNMA_ART1_2_13_Q.csv) e [manifesto](fontes/T37_M01_6938_13_R10_v1.json). **Inciso XI acrescido pela Lei 15.512/2026**, publicado em 23/09/2026 e vigente desde então: prioridade para crianças e adolescentes no acesso à natureza. O texto de origem é reprodução da versão **atualizada** da Câmara, com cotejo do Planalto, não da versão de 1981. Preservadas as palavras e a remissão constitucional do art. 1º; nenhum C0-J, DOU fac-símile e recepção CF ainda pendentes.

- [T37.M01 — Lei 6.938/1981, arts. 3º–4º, **2 artigos e 19 unidades Q adicionais**](vistas/T37_PNMA_ART3_4_PREVIA_Q.md), [espelho 19×19](../modulos/T37/M01_ESPELHO_PNMA_ART3_4_19_Q.csv) e [manifesto](fontes/T37_M01_6938_19_R11_v1.json). Poluição tem cinco alíneas integrantes da definição, não cinco ilícitos autônomos; art. 3º IV inclui poluidor direto/indireto; art. 4º sete objetivos e competências federativas. **Total T37: 4 artigos/32 unidades Q**, sem ampliação de competência ou saneamento textual tácito.

**Parte VIII — Proteção internacional e migração**

- [T48.M03 — Lei 9.474/1997, arts. 17º–21º, **5 artigos e 8 unidades Q adicionais**](vistas/T48_REFUGIO_ART17_21_PREVIA_Q.md), [espelho 8×8](../modulos/T48/M03_ESPELHO_REFUGIO_ART17_21_8_Q.csv) e [manifesto](fontes/T48_M03_9474_8_R11_v1.json). Declarações, intérprete, ACNUR, sigilo, protocolo e direito de permanência até decisão final. **Total T48: 15 artigos/29 unidades Q**, com **lacuna expressa dos arts. 11º–16º** e dos arts. 22º e seguintes. Sem C0-J.

- [T48.M03 — Lei 9.474/1997 arts. 9º–10, **2 artigos e 4 unidades Q adicionais**](vistas/T48_REFUGIO_LEI9474_ART9_10_PREVIA_Q.md), [espelho 4×4](../modulos/T48/M03_ESPELHO_LEI9474_ART9_10_4_Q.csv), [manifesto](fontes/T48_M03_9474_4_R10_v1.json). Art. 9º registra a oitiva do solicitante; art. 10 estabelece suspensão **pela entrada irregular**, arquivamento **condicionado** e fluxos à Polícia Federal. No recorte anterior T48 tinha 10 artigos/21 unidades; a vista posterior R11 acrescenta cinco artigos e oito unidades, mantendo lacunas. C0-J segue zero.

- [T48.M03 — Lei 9.474/1997, arts. 1º–8º, **8 artigos e 17 unidades Q**](vistas/T48_REFUGIO_LEI9474_ART1_8_PREVIA_Q.md), [fonte e espelho 17×17](../modulos/T48/M03_ESPelho_LEI9474_ART1_8_17_Q.csv), [manifesto](fontes/T48_M03_9474_17_v1.json) e [verificador](../scripts/gerar_previa_t48.py). Enquadra refugiados, extensão familiar, exclusões, documentos, pedido fronteiriço, art. 7º não devolução e art. 8º ingresso irregular. **Não** harmoniza automaticamente art. 7º §2º com a Lei 13.445/2017, art. 49 §4º e tratados; DOU original de 1997 ainda sem fac-símile cotejado; nenhum C0-J. Os demais dispositivos, além dos arts. 1º–10, não foram transpostos.

**Livro Penal T25.M01 (núcleo CP 1º–12)**
- [Prévia parcial do Livro Penal: 12 artigos, 39 unidades](vistas/T25_PENAL_PARTE_GERAL_CP1_12_PREVIA.md), derivada do PR #32 em commit fixado: [manifesto](fontes/T25_CP1_12_v1.json), [concordância 39 × 39](concordancia/T25_CP_ART1_12_39.csv) e [verificador documental](../scripts/gerar_previa_t25.py). **Nenhuma C0-J aprovada; CP art.12 tem gate de especialidade e referente `deste Código`, CPM não integrado.**

**Controle adicional R10 do CPC85:** [9 cenários adversariais de honorários](../modulos/T24/M01/T24_MATRIZ_09_CENARIOS_HONORARIOS_R10.csv), [nota temporal e de escopo](../modulos/T24/M01/T24_NOTA_CENARIOS_R10_20261015.md). Distingue STJ1076/1313/1413, RPV e modulação 1190, STF1255 sem julgamento de mérito verificado e STJ1454 afetado, não julgado. Sem alteração literal do CPC.

**Revisão jurisprudencial T24.M01:** [matriz de nove gates CPC 85 e temas STJ/STF](../modulos/T24/M01/T24_GATES_09_TEMAS_STJ_STF_HONORARIOS_R09.csv) e [nota de aplicação restrita e transição](../modulos/T24/M01/T24_NOTA_R09_HONORARIOS_JURISPRUDENCIA_20261015.md). Tema 1076 ≠ 1313 (saúde pública), Tema 1190 tem modulação; STF1255 pendente de confirmação de mérito. **Não** modifica 181 transcrições CPC Q.

**Rastro da ampliação T24**
- [Primeira prévia 106 unidades](vistas/T24_PROCESSO_CIVIL_PREVIA_PARCIAL.md), [prévia intermediária 75](vistas/T24_CPC_82_97_PREVIA_75_Q.md), [concordância 75 × 75](concordancia/T24_CPC_82_97_CONCORDANCIA_75_Q.csv). A antiga [matriz sem texto](concordancia/T24_82_97_GATE_75_SEM_TEXTO.csv) é preservada como histórico de estágio; não representa a cobertura atual.

**Controle jurídico do T05 já integrado:** [parecer da Rodada 08 com STF ADI 2650, ADPF 819 e ADO 70](../modulos/T05/M06_PARECER_R08_CONSTITUCIONALIDADE_TEXTO_E_TEMPORALIDADE_20261015.md) e [15 gates de fontes e efeitos](../modulos/T05/M06_AUDITORIA_15_GATES_CONSTITUCIONAIS_E_FONTES_R08.csv). A cláusula do art. 15 da Lei 9.709 é texto de origem com **eficácia histórica**, não cláusula de vigência do futuro CLF. O corpus permanece **138 artigos/464 posições documentais**, sem homologação C0-J; a cifra não representa 464 comandos prospectivos vigentes.

**Preparação T05 adicional, FORA do Código de Trabalho:** [23 posições da Lei 9.709/1998 arts. 3º–15](../modulos/T05/M06_CONCORDANCIA_F0_ART3_15_23_SEM_TEXTO_LITERAL.csv), **com resumos não literais e destinos simbólicos**, mais [controle de três fontes institucionais](../modulos/T05/M06_NOTA_TRES_FONTES_E_GATES_9709_20261015.md) e [12 casos Código Eleitoral 1965/2026](../modulos/T05/M01_MATRIZ_RECEPCAO_ELEITORADO_CE4_5_71_72_2026.csv). Estes 23 + 12 são pesquisas **Q**, não subunidades normativas adicionais integradas.

**Em pesquisa, ainda fora do corpus de leitura:** T01.M04 (formalização/DEC-016), T29 (RGPS), T43 (Governo Digital) e [T13.M01, inventário inicial de 19 unidades CC 1–5](../modulos/T13/M01/NOTA_ABERTURA_CAPACIDADE_CIVIL_20261015.md), entre outras frentes a abrir. Nenhuma dessas pesquisas constitui Livro completo de CLF. O mapa de 48 títulos é provisório, não universo exaustivo da legislação.

## Convenção de proveniência e montagens

- **Fontes canônicas setoriais fixadas por commit**: `integracao/25_...` e `26_...` no PR #45 (T07); `modulos/T24/M01/F1C2_ESPELHO_UNIFICADO_106.csv` no PR #38 (T24: 106 unidades), mais 75 transcrições editoriais locais em CSV com hashes (T24: 82–97). Os arquivos `vistas/` não são fonte paralela editável.
- **T05**: `python3 scripts/gerar_previa_t05.py --check`, com sete unidades e hash da origem editorial local. A transposição documental mantém Q, e o conflito de grafia da publicação original da Lei 9.709 art. 2º segue pendente de DOU.
- **T07**: `python3 scripts/gerar_produto_experimental.py --setorial-root setorial --check` (com o checkout de origem T07 declarado no manifesto); `--write` regenera somente a vista derivada.
- **T24 setorial**: `python3 scripts/gerar_previa_t24.py --setorial-root setorial --check` confere as 106 unidades originais. **T24 integrado**: `python3 scripts/gerar_t24_cpc_181.py --check` confere os dois conjuntos, 33 artigos, 181 destinos, quatro marcos legislativos e hashes de blob; `--write` regenera apenas a vista contínua.
- **CI documental separada:** workflows [T07](../.github/workflows/conferir-produto-experimental.yml), [T24-106](../.github/workflows/conferir-t24-previsao.yml), [T24-181](../.github/workflows/conferir-t24-181.yml) e [T25](../.github/workflows/conferir-t25-previa.yml). Execuções anteriores do GitHub Actions exibiram **failure sem etapas visíveis**; controle independente de correspondência T24 foi efetuado por leitura dos arquivos. **Não declarar CI aprovado nem C0-J**.
- **Produto atual:** [Código de Trabalho unificado](CODIGO_DE_TRABALHO.md) é compilado automaticamente dos onze componentes parciais indicados em [indice_livros.json](fontes/indice_livros.json), usando `python3 scripts/gerar_codigo_integrado.py --check` ou `--write`. **Produto futuro:** versão comentada com variantes, concordância N:N geral, remissões controladas, lacunas e transições. A compilação atual não constitui código completo, índice jurídico exaustivo ou renumeração final.

## Estado acumulado após rodada 11

**Código experimental Q:** 160 artigos e 532 unidades textuais documentais positivas de origem, mais um registro histórico T07; 11 componentes em 7 títulos. Lei 9.474/1997 artigos 11–16 permanecem ausentes, e PEC 221/2019 não foi homologada nem promulgada na fonte consultada até 15/10/2026. [Código único](CODIGO_DE_TRABALHO.md) · [índice](fontes/indice_livros.json) · [painel](../central/PAINEL_GERADO.csv). Nenhuma C0-J, nenhuma M, DEC-016 pendente.

## Estado acumulado após rodada 10

**Corpus único experimental Q:** **150 artigos / 498 unidades de origem com texto documental**, mais **1 registro histórico T07**; oito componentes em seis títulos (T05, T07, T24, T25, T37, T48). Inclui art. 15 da Lei 9.709 como unidade textual temporal histórica de 1998, sem transferir vigência ao CLF. Sem qualquer C0-J/M ratificadas, DEC-016 pendente. [Painel derivado](../central/PAINEL_GERADO.csv) e [Código único](CODIGO_DE_TRABALHO.md). Métricas descrevem apenas recortes experimentais, **não** cobertura do direito federal.

## Estado acumulado após rodada 09

**Código experimental em branch R09:** 146 artigos / 481 unidades documentais de origem, mais um registro histórico T07, distribuídos por seis componentes técnicos em cinco títulos. T05 art. 15 é cláusula temporal histórica no universo textual de 481, não comando novo de vigência. Nenhum C0-J, nenhuma M aprovada, nenhuma DEC-016 resolvida. Painel recalculado em [central/PAINEL_GERADO.csv](../central/PAINEL_GERADO.csv), sem percentuais fictícios de legislação nacional.

## Indicadores, não confundir denominadores

| Objeto | Artigos visíveis na prévia | Unidades positivas | Unidade histórica | C0-J homologadas |
|---|---:|---:|---:|---:|
| T05 — Lei 9.709/1998 (arts. 1º–15; art. 15 com vigência histórica) | 15 | 30 | 0 | 0 |
| T07 — Lei 9.784/1999 | 78 | 214 | 1 | 0 |
| T24 — CPC (arts. 70–102 contínuos) | 33 | 181 | 0 | 0 |
| T25 — CP (arts. 1º–12) | 12 | 39 | 0 | 0 |
| T28 — CLT (arts. 1º–3º) | 3 | 7 | 0 | 0 |
| T37 — PNMA (arts. 1º–4º, redação vigente 2026) | 4 | 32 | 0 | 0 |
| T48 — Lei 9.474/1997 (arts. 1º–10 e 17–21) | 15 | 29 | 0 | 0 |
| **Total atual das vistas** | **160** | **532** | **1** | **0** |

As 532 unidades são **registros textuais de origens e recortes distintos**, não porcentagem de cobertura do direito federal, artigos renumerados ou normas juridicamente certificadas.

[Central CLF #48](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/48) · [Auditoria dos 48 títulos](../central/01_MATRIZ_AUDITORIA_48_TITULOS_20261015.csv) · [Central CF #103](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/103).
