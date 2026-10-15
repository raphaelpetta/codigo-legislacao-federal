# Código da Legislação Federal — corpus único experimental (vista de trabalho)

**Corte:** 15/10/2026 · **Estado:** minutas editoriais em PR **draft**, não legislação vigente, nem texto homologado, nem revogações ou atos de promulgação. **DEC-001**: objetivo de corpus único mantido. **DEC-016**: veículo/espécie/iniciativa/veto/transição **pendente**.


## Vista única gerada do corpus efetivamente integrado

[Ler o **Código experimental integrado em texto corrido**](CODIGO_DE_TRABALHO.md), gerado por `python3 scripts/gerar_codigo_integrado.py --write` a partir do [índice de Livros](fontes/indice_livros.json), conferível com `--check`. **Contém T01 (LINDB arts. 2º–5º), T03 (LC 140 arts. 1º–6º), T05, T07, T08 (Lei 8.112 arts. 1º–4º), T20 (CDC arts. 1º–3º), T24, T25, T28 (CLT arts. 1º–6º), T37 e T48**, com 37 títulos ainda sem texto, todos experimentais Q, sem efeitos legais ou homologação C0-J.

## Ponto de leitura: Código de Trabalho e vinte componentes experimentais em onze títulos

**[Abrir Código de Trabalho unificado (T01 + T03 + T05 + T07 + T08 + T20 + T24 + T25 + T28 + T37 + T48, NÃO RATIFICADO)](CODIGO_DE_TRABALHO.md)** — arquivo reconstruível a partir do [índice de Livros](fontes/indice_livros.json) e das vistas fixadas. Nenhum conteúdo experimental foi convertido em norma vigente; a Parte V permanece um recorte incompleto do CPC. Ver [gerador do Código](../scripts/gerar_codigo_integrado.py) e [controle operacional](../scripts/controle_operacional.py).

**Parte I — Normas gerais**

- [T01.M01 — LINDB arts. 2º–5º, 4 artigos/7 unidades Q](vistas/T01_LINDB_ART2_5_PREVIA_Q.md); [espelho 7×7](../modulos/T01/M01_ESPELHO_LINDB_ART2_5_7_Q.csv), [manifesto SHA](fontes/T01_M01_LINDB_7_R14_v1.json). Revogação, não repristinação, integração judicial e fins sociais. **Art. 1º ainda fora do recorte**, incluindo o § 2º **revogado em 2009**, que não foi somado como norma positiva; DOU 1942/1943, T23 e DEC-016 pendentes.

**Parte II — Federação e organização territorial**

- [T03.M01 — LC 140/2011, arts. 1º–3º, **3 artigos/10 unidades Q**](vistas/T03_LC140_ART1_3_PREVIA_Q.md); [espelho 10×10](../modulos/T03/M01_ESPELHO_LC140_ART1_3_10_Q.csv) e [manifesto](fontes/T03_M01_LC140_10_R12_v1.json). **Lei complementar**, tutela de competência comum art. 23 CF; atuação **supletiva ≠ subsidiária**, preservada a repartição federativa. LC não é rebaixada a lei ordinária por anexação editorial ao Código; DEC-016 pendente.

- [T03.M01 — LC 140/2011, arts. 4º–6º: **3 artigos/15 unidades Q adicionais**](vistas/T03_LC140_ART4_6_PREVIA_Q.md), [espelho 15×15](../modulos/T03/M01_ESPELHO_LC140_ART4_6_15_Q.csv), [manifesto SHA](fontes/T03_M01_LC140_15_R13_v1.json). Consórcios, convênios, comissões paritárias, fundos e delegações; art. 5º exige **órgão ambiental capacitado e conselho de meio ambiente** no ente destinatário. **Total T03: 6 artigos/25 unidades Q**, LC federal preservada enquanto espécie distinta, DEC-016 pendente.

**Parte II — Eleições e participação política**
- [T05.M06, suplemento documental dos arts. 3º–15 da Lei 9.709/1998: 13 artigos e 23 unidades Q](vistas/T05_DEMOCRACIA_DIRETA_LEI9709_ART3_15_PREVIA_Q.md), [espelho 23×23](../modulos/T05/M06_ESPELHO_LEI9709_ART3_15_23_Q.csv) e [manifesto SHA](fontes/T05_M06_9709_23_v1.json). **DOU pendente**, divergências arts. 2º/3º/8º IV abertas; art. 15 tem efeito temporal original de 1998. O título T05 passa a ter **15 artigos e 30 unidades documentais Q** de uma única lei, em duas vistas. Nenhum C0-J.
- [T05.M06, democracia direta: Lei 9.709/1998 arts. 1º–2º, 2 artigos e 7 unidades Q](vistas/T05_DEMOCRACIA_DIRETA_LEI9709_ART1_2_PREVIA.md), [espelho 7×7](../modulos/T05/M06_ESPELHO_LEI9709_ART1_2_7_Q.csv), [manifesto](fontes/T05_M06_9709_7_v1.json) e [inventário dos seis módulos eleitorais](../modulos/T05/M00_INVENTARIO_SEIS_MODULOS_20261015.csv). [Dossiê de recepção constitucional e anualidade eleitoral 2026](../modulos/T05/NOTA_ABERTURA_2026_RECEPCAO_ANUALIDADE_20261015.md): a mudança do art. 5º do Código Eleitoral em 2026 não foi aplicável às eleições de 2026, segundo o TSE. O Código Eleitoral integral **não** foi transposto; os arts. 3º–15 da Lei 9.709 foram integrados **apenas como reprodução experimental Q**.

**Parte III — Administração Pública e Finanças**

- [T08.M01 — Lei 8.112/1990, arts. 1º–4º, 4 artigos/5 unidades Q](vistas/T08_RJU_LEI8112_ART1_4_PREVIA_Q.md), [espelho 5×5](../modulos/T08/M01_ESPELHO_LEI8112_ART1_4_5_Q.csv) e [manifesto SHA](fontes/T08_M01_8112_5_R14_v1.json). Regime dos servidores civis **federais** (não estados ou municípios), cargo público, e exceção legal à vedação de prestação gratuita. Constituição art. 37, ADI 2.135, vetos/DOU1990/1991/1998 pendentes.
- [Livro de Processo Administrativo Federal — T07.M03, prévia integral de 78 artigos](vistas/T07_PROCESSO_ADMINISTRATIVO_PREVIA.md). Proveniência: PR #45, fonte fixa, [manifesto](fontes/T07_M03_v4.json); 214 unidades positivas (203 C0-T local, 11 C1 potenciais/Q), 1 registro histórico, nenhuma unidade C0-J homologada.
- [Auditoria dos 11 C1 potenciais T07](../central/03_T07_GATE_C1_11_EFEITOS_20261015.csv), com efeitos, alternativas conservadoras, provas faltantes e riscos. Os destinatários, o âmbito e a subsidiariedade dos processos especiais permanecem Q.

**Parte IV — Relações privadas, consumidores e mercados**

- [T20.M01 — CDC arts. 1º–3º, 3 artigos/6 unidades Q](vistas/T20_CDC_ART1_3_PREVIA_Q.md), [espelho 6×6](../modulos/T20/M01_ESPELHO_CDC_ART1_3_6_Q.csv), [manifesto SHA](fontes/T20_M01_CDC_6_R14_v1.json). Normas de ordem pública e interesse social; consumidor final, coletividade equiparada, fornecedor e serviços financeiros remunerados; relações trabalhistas excluídas da definição de serviço do § 2º. Interfaces T16/T21 e DOU/vetos sem homologação.

**Parte V — Direito Internacional Privado, Justiça e Sanções**
- [Livro de Processo Civil — T24.M01, prévia contínua CPC 70–102: **33 artigos e 181 unidades Q**](vistas/T24_CPC_70_102_PREVIA_CONTINUA_Q.md). Combina 106 unidades setoriais do PR #38 e [75 transcrições editoriais](fontes/T24_CPC_82_97_TEXTO_ATUAL_75_Q.csv) em [manifesto de duas proveniências](fontes/T24_CPC_70_102_181_v1.json), com [verificador](../scripts/gerar_t24_cpc_181.py). O cotejo visual com a Câmara foi documentado, mas persistem revisão independente arquivada por extração e cotejo DOU; C0-J=0 e o CPC externo ao recorte não foi transposto.

**Parte VI — Trabalho e relações laborais**

- [T28.M01 — CLT, arts. 1º–3º, **3 artigos e 7 unidades Q**](vistas/T28_CLT_ART1_3_PREVIA_Q.md), [espelho 7×7](../modulos/T28/M01_ESPELHO_CLT_ART1_3_7_Q.csv) e [manifesto/hash](fontes/T28_M01_CLT_7_R11_v1.json). Distinção entre decreto-lei de aprovação e CLT, requisitos para relação de emprego, grupo econômico após a Lei 13.467/2017. **PEC 221/2019, fim da escala 6×1:** dois turnos aprovados no Senado em 14/10/2026; **sem promulgação comprovada em 15/10/2026**, portanto não altera a versão do Código como norma vigente. Sem C0-J.

- [T28.M01 — CLT, arts. 4º–6º: 3 artigos/14 unidades Q adicionais](vistas/T28_CLT_ART4_6_PREVIA_Q.md), [espelho 14×14](../modulos/T28/M01_ESPELHO_CLT_ART4_6_14_Q.csv), [manifesto SHA](fontes/T28_M01_CLT_14_R14_v1.json). Tempo à disposição, oito incisos subordinados ao § 2º do art. 4º, igualdade remuneratória e subordinação por meios telemáticos. **Total T28: 6 artigos/21 unidades Q**. Controle Leis 12.551/2011, 13.467/2017 e 14.611/2023 pendente.

**Parte VII — Território, ambiente e infraestrutura**

- [T37.M01 — Política Nacional do Meio Ambiente, Lei 6.938/1981 arts. 1º–2º, 2 artigos e 13 unidades Q](vistas/T37_PNMA_ART1_2_PREVIA_Q.md); [espelho 13×13](../modulos/T37/M01_ESPELHO_PNMA_ART1_2_13_Q.csv) e [manifesto](fontes/T37_M01_6938_13_R10_v1.json). **Inciso XI acrescido pela Lei 15.512/2026**, publicado em 23/09/2026 e vigente desde então: prioridade para crianças e adolescentes no acesso à natureza. O texto de origem é reprodução da versão **atualizada** da Câmara, com cotejo do Planalto, não da versão de 1981. Preservadas as palavras e a remissão constitucional do art. 1º; nenhum C0-J, DOU fac-símile e recepção CF ainda pendentes.

- [T37.M01 — Lei 6.938/1981, arts. 3º–4º, **2 artigos e 19 unidades Q adicionais**](vistas/T37_PNMA_ART3_4_PREVIA_Q.md), [espelho 19×19](../modulos/T37/M01_ESPELHO_PNMA_ART3_4_19_Q.csv) e [manifesto](fontes/T37_M01_6938_19_R11_v1.json). Poluição tem cinco alíneas integrantes da definição, não cinco ilícitos autônomos; art. 3º IV inclui poluidor direto/indireto; art. 4º sete objetivos e competências federativas. **Total T37: 4 artigos/32 unidades Q**, sem ampliação de competência ou saneamento textual tácito.

- [T37.M01 — PNMA, arts. 5º–6º, **2 artigos/9 unidades Q adicionais**](vistas/T37_PNMA_ART5_6_PREVIA_Q.md), [espelho 9×9](../modulos/T37/M01_ESPELHO_PNMA_ART5_6_9_Q.csv) e [manifesto](fontes/T37_M01_6938_9_R12_v1.json). SISNAMA: Conselho de Governo, CONAMA, órgão central, IBAMA/ICMBio, órgãos seccionais estaduais e locais municipais. **Inciso I alterado pela Lei 15.190/2025, art. 63, vigência após 180 dias**; não usar redação original. **Total T37: 6 artigos/41 unidades documentais Q**.

**Parte VIII — Proteção internacional e migração**

- [T48.M03 — Lei 9.474/1997, arts. 22–37, **16 artigos/16 unidades Q adicionais**](vistas/T48_REFUGIO_ART22_37_PREVIA_Q.md), [espelho 16×16](../modulos/T48/M03_ESPELHO_REFUGIO_ART22_37_16_Q.csv) e [manifesto SHA](fontes/T48_M03_9474_16_R13_v1.json). Motivação, sigilo, recurso e permanência durante sua análise; art. 32 tem ressalva à proteção de não devolução exigindo cotejo com tratados e Lei 13.445; arts. 33–37 estabelecem efeitos na extradição e expulsão, com proibição de destino de risco. **Total T48: 37 artigos/68 unidades Q**, agora contínuos de 1–37; arts. 38–49 ainda não integrados.

- [T48.M03 — CONARE, Lei 9.474/1997 arts. 11–16, **6 artigos/23 unidades Q adicionais**](vistas/T48_REFUGIO_ART11_16_PREVIA_Q.md), [espelho 23×23](../modulos/T48/M03_ESPELHO_REFUGIO_ART11_16_23_Q.csv) e [manifesto](fontes/T48_M03_9474_23_R12_v1.json). Competências em primeira instância, composição original, quórum mínimo de quatro membros com voto e ACNUR **voz sem voto**. Agora os **arts. 1º–21 estão representados em sequência documental contínua**, total T48 **21 artigos/52 unidades Q**. Permanecem excluídos arts. 22–49 e a verificação da organização administrativa atual.

- [T48.M03 — Lei 9.474/1997, arts. 17º–21º, **5 artigos e 8 unidades Q adicionais**](vistas/T48_REFUGIO_ART17_21_PREVIA_Q.md), [espelho 8×8](../modulos/T48/M03_ESPELHO_REFUGIO_ART17_21_8_Q.csv) e [manifesto](fontes/T48_M03_9474_8_R11_v1.json). Declarações, intérprete, ACNUR, sigilo, protocolo e direito de permanência até decisão final. Na Rodada 11 o T48 totalizava 15 artigos/29 unidades; a lacuna 11–16 foi preenchida na vista da Rodada 12, a R13 integrou posteriormente os arts. 22–37, ainda sem os arts. 38–49. Sem C0-J.

- [T48.M03 — Lei 9.474/1997 arts. 9º–10, **2 artigos e 4 unidades Q adicionais**](vistas/T48_REFUGIO_LEI9474_ART9_10_PREVIA_Q.md), [espelho 4×4](../modulos/T48/M03_ESPELHO_LEI9474_ART9_10_4_Q.csv), [manifesto](fontes/T48_M03_9474_4_R10_v1.json). Art. 9º registra a oitiva do solicitante; art. 10 estabelece suspensão **pela entrada irregular**, arquivamento **condicionado** e fluxos à Polícia Federal. No recorte anterior T48 tinha 10 artigos/21 unidades; a vista R11 acrescentou cinco artigos e oito unidades; a rodada R12 completou 11–16 e eliminou essa lacuna documental. C0-J segue zero.

- [T48.M03 — Lei 9.474/1997, arts. 1º–8º, **8 artigos e 17 unidades Q**](vistas/T48_REFUGIO_LEI9474_ART1_8_PREVIA_Q.md), [fonte e espelho 17×17](../modulos/T48/M03_ESPelho_LEI9474_ART1_8_17_Q.csv), [manifesto](fontes/T48_M03_9474_17_v1.json) e [verificador](../scripts/gerar_previa_t48.py). Enquadra refugiados, extensão familiar, exclusões, documentos, pedido fronteiriço, art. 7º não devolução e art. 8º ingresso irregular. **Não** harmoniza automaticamente art. 7º §2º com a Lei 13.445/2017, art. 49 §4º e tratados; DOU original de 1997 ainda sem fac-símile cotejado; nenhum C0-J. O recorte posterior de 17–21 e o bloco 11–16 da R12 completaram documentalmente 1–21, permanecendo fora os arts. 38–49 após a expansão R13.

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
- **Produto atual:** [Código de Trabalho unificado](CODIGO_DE_TRABALHO.md) é compilado automaticamente dos dezesseis componentes parciais indicados em [indice_livros.json](fontes/indice_livros.json), usando `python3 scripts/gerar_codigo_integrado.py --check` ou `--write`. **Produto futuro:** versão comentada com variantes, concordância N:N geral, remissões controladas, lacunas e transições. A compilação atual não constitui código completo, índice jurídico exaustivo ou renumeração final.

## Estado acumulado após rodada 14 — prioridade horizontal corrigida

**Corpus experimental Q em PR draft:** **204 artigos de origem / 637 unidades positivas de fonte +1 histórico T07**, em **20 componentes e 11 títulos**. **Três novos títulos reais**: T01 LINDB (2–5), T08 RJU (1–4) e T20 CDC (1–3); aprofundamento contido do T28 CLT (4–6). **37 de 48 títulos ainda sem texto de lei**. [Matriz de auditoria reconciliada](../central/01_MATRIZ_AUDITORIA_48_TITULOS_20261015.csv), sem contagem dupla do histórico. Nenhuma C0-J, M aprovada, revogação ou merge, e DEC-016 permanece pendente. Nenhum bloco é promulgado como novo Código.

## Estado acumulado após rodada 13

**Código de trabalho Q:** **190 artigos de origem / 605 unidades documentais textuais + 1 registro histórico T07**, em 16 componentes de oito títulos. **T03 LC 140/2011 arts. 1º–6º** e **T48 Lei 9.474/1997 arts. 1º–37** são as expansões; T48 arts. 38º–49º permanecem fora. Remissões sobre não devolução, direito ao recurso e restrições de delegação ambiental precisam de revisão por efeito e fontes DOU. **C0-J=0, M=0, DEC-016 pendente, revogação/merge=0**; texto temporal histórico da Lei 9.709 art. 15 consta dentre as unidades Q, sem eficácia futura do CLF.

## Estado acumulado após rodada 12

**Corpus único Q em PR draft R12:** **171 artigos e 574 unidades documentais textuais de origem**, mais **um registro histórico T07**, distribuídos em 14 componentes e oito títulos (T03, T05, T07, T24, T25, T28, T37, T48). T03 é lei **complementar**; T37 mantém repartição federativa; T48 inclui Lei 9.474 arts. 1–21, ainda sem arts. 22–49. **C0-J=0, M=0, DEC-016 pendente, merges=0.** A contagem inclui texto temporal histórico da Lei 9.709 art. 15 como documento, não como norma futura do CLF.

## Estado acumulado após rodada 11

**Código experimental Q:** 160 artigos e 532 unidades textuais documentais positivas de origem, mais um registro histórico T07; 11 componentes em 7 títulos. Lei 9.474/1997 artigos 11–16 permanecem ausentes, e PEC 221/2019 não foi homologada nem promulgada na fonte consultada até 15/10/2026. [Código único](CODIGO_DE_TRABALHO.md) · [índice](fontes/indice_livros.json) · [painel](../central/PAINEL_GERADO.csv). Nenhuma C0-J, nenhuma M, DEC-016 pendente.

## Estado acumulado após rodada 10

**Corpus único experimental Q:** **150 artigos / 498 unidades de origem com texto documental**, mais **1 registro histórico T07**; oito componentes em seis títulos (T05, T07, T24, T25, T37, T48). Inclui art. 15 da Lei 9.709 como unidade textual temporal histórica de 1998, sem transferir vigência ao CLF. Sem qualquer C0-J/M ratificadas, DEC-016 pendente. [Painel derivado](../central/PAINEL_GERADO.csv) e [Código único](CODIGO_DE_TRABALHO.md). Métricas descrevem apenas recortes experimentais, **não** cobertura do direito federal.

## Estado acumulado após rodada 09

**Código experimental em branch R09:** 146 artigos / 481 unidades documentais de origem, mais um registro histórico T07, distribuídos por seis componentes técnicos em cinco títulos. T05 art. 15 é cláusula temporal histórica no universo textual de 481, não comando novo de vigência. Nenhum C0-J, nenhuma M aprovada, nenhuma DEC-016 resolvida. Painel recalculado em [central/PAINEL_GERADO.csv](../central/PAINEL_GERADO.csv), sem percentuais fictícios de legislação nacional.

## Indicadores, não confundir denominadores

| Objeto | Artigos visíveis na prévia | Unidades positivas | Unidade histórica | C0-J homologadas |
|---|---:|---:|---:|---:|
| T01 — LINDB (arts. 2º–5º) | 4 | 7 | 0 | 0 |
| T03 — LC 140/2011 (arts. 1º–6º) | 6 | 25 | 0 | 0 |
| T05 — Lei 9.709/1998 (arts. 1º–15; art. 15 com vigência histórica) | 15 | 30 | 0 | 0 |
| T07 — Lei 9.784/1999 | 78 | 214 | 1 | 0 |
| T08 — Lei 8.112/1990 (arts. 1º–4º) | 4 | 5 | 0 | 0 |
| T20 — CDC (arts. 1º–3º) | 3 | 6 | 0 | 0 |
| T24 — CPC (arts. 70–102 contínuos) | 33 | 181 | 0 | 0 |
| T25 — CP (arts. 1º–12) | 12 | 39 | 0 | 0 |
| T28 — CLT (arts. 1º–6º) | 6 | 21 | 0 | 0 |
| T37 — PNMA (arts. 1º–6º, redação vigente 2026) | 6 | 41 | 0 | 0 |
| T48 — Lei 9.474/1997 (arts. 1º–37) | 37 | 68 | 0 | 0 |
| **Total atual das vistas** | **204** | **637** | **1** | **0** |

As 637 unidades são **registros textuais de origens e recortes distintos**, não porcentagem de cobertura do direito federal, artigos renumerados ou normas juridicamente certificadas.

[Central CLF #48](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/48) · [Auditoria dos 48 títulos](../central/01_MATRIZ_AUDITORIA_48_TITULOS_20261015.csv) · [Central CF #103](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/103).
