# CLF — Rodada 19: bens civis, CPP, trânsito, política de consumo e CI

**Corte:** 15/10/2026. **PR [#64 draft](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/64)**, dependente do [#63 draft](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/63), sem merge à main. [Central #48](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/48). Todos os textos são **documentais Q (C0-J=0)**, não uma nova promulgação nem norma material ratificada.

## FEITO — três títulos abertos com texto, uma expansão vertical

### T14 — Código Civil: bens móveis e imóveis
- [Vista CC arts. 79–84](../produto/vistas/T14_CODIGO_CIVIL_BENS_ART79_84_PREVIA_Q.md), [espelho CSV](../modulos/T14/M01_ESPELHO_CC_ART79_84_13_Q.csv), [manifesto com hash](../produto/fontes/T14_M01_CC_13_R19_v1.json). **6 artigos/13 unidades positivas Q**, Git blob `91480c28b4de6c96237275b6394d00301bc8ac38`.
- [Câmara, texto atualizado da Lei 10.406/2002](https://www2.camara.leg.br/legin/fed/lei/2002/lei-10406-10-janeiro-2002-432893-normaatualizada-pl.html), com cotejo Planalto. Art. 79 define bens imóveis; art. 80 direitos imóveis para efeitos legais; art. 81 bens que não perdem caráter imóvel; arts. 82–84 bens móveis, energias, direitos patrimoniais e materiais de construção.
- **Reserva T13 completamente intocada**. A qualificação de bens não altera domínio, direitos fundamentais de propriedade, regimes especiais de energia, registro, sucessões nem contratos. DOU original/alteradoras ainda não conferidos em fac-símile.

### T26 — Processo penal: CPP arts. 2º–3º
- [Vista CPP 2º–3º](../produto/vistas/T26_CPP_ART2_3_PREVIA_Q.md), [espelho](../modulos/T26/M01_ESPELHO_CPP_ART2_3_2_Q.csv), [manifesto](../produto/fontes/T26_M01_CPP_2_R19_v1.json). **2 artigos/2 unidades Q**, blob `0e1b41936cc5aeb1ee89f2e7c4fa479d82076282`.
- [Câmara CPP atualizado](https://www2.camara.leg.br/legin/fed/declei/1940-1949/decreto-lei-3689-3-outubro-1941-322206-normaatualizada-pe.html), cotejo Planalto. Aplicação imediata da lei processual aos atos futuros (sem invalidar os anteriores), extensão/analogia/princípios limitados pelo sistema acusatório e legalidade; não transportar esse princípio para retroatividade penal gravosa.
- **CPP art. 1º fora** devido a remissões históricas a Constituição, tribunais especiais e crimes de imprensa; **art. 3º-A e seguintes fora** (juiz das garantias/Lei 13.964/2019/ADIs STF). Separar texto Q, norma material e efeitos constitucionais.

### T41 — Trânsito: CTB arts. 1º–2º
- [Vista CTB 1º–2º](../produto/vistas/T41_CTB_ART1_2_PREVIA_Q.md), [espelho](../modulos/T41/M01_ESPELHO_CTB_ART1_2_7_Q.csv), [manifesto](../produto/fontes/T41_M01_CTB_7_R19_v1.json). **2 artigos/7 unidades Q**, blob `735aa3938fd9a2c2cc24ab0a4e3e594902ee73b6`.
- [Câmara, Lei 9.503/1997 atualizada](https://www2.camara.leg.br/legin/fed/lei/1997/lei-9503-23-setembro-1997-372348-normaatualizada-pl.html), [ficha de veto/retificação](https://www2.camara.leg.br/legin/fed/lei/1997/lei-9503-23-setembro-1997-372348-norma-pl.html). Art. 1º §§1º–3º e 5º, **§4º vetado não reproduzido como texto positivo**. Art. 2º parágrafo único redação **Lei 13.146/2015**, acrescentando estacionamento de estabelecimentos privados de uso coletivo.
- Não presumir competência normativa exclusiva de um órgão sobre toda via nem indenização automática sem exame do nexo, atuação e competência. DOU original 24/09/1997, veto/retificação e LBI pendentes de fac-símile.

### T20 — CDC art. 4º, expansão vertical contida
- [Vista CDC art. 4º](../produto/vistas/T20_CDC_ART4_PREVIA_Q.md), [espelho 15×15](../modulos/T20/M01_ESPELHO_CDC_ART4_15_Q.csv), [manifesto](../produto/fontes/T20_M01_CDC_15_R19_v1.json). **1 artigo/15 unidades Q**, blob `8e1bf3acead4943d06f87805bef8382dd0f3b441`.
- [Câmara, CDC atualizado](https://www2.camara.leg.br/legin/fed/lei/1990/lei-8078-11-setembro-1990-365086-normaatualizada-pl.html). Caput com redação **Lei 9.008/1995**; inciso II contém **quatro alíneas subordinadas**, IX/X acrescidos pela **Lei 14.181/2021** (educação financeira e combate ao superendividamento). Não presumir que o art. 4º por si atribua direito à repactuação sem art. 54-A e seguintes. **T20 total: CDC 1º–4º, 4 artigos/21 unidades Q**.

## FEITO — corpus e controle transversal
- [Código único experimental](../produto/CODIGO_DE_TRABALHO.md), [índice dos Livros](../produto/fontes/indice_livros.json), [painel](PAINEL_GERADO.csv), [quadro](QUADRO_PRODUTO.csv), [matriz 48 títulos](01_MATRIZ_AUDITORIA_48_TITULOS_20261015.csv), [guia](../produto/00_LEIA_O_CODIGO.md) e [fila 56 tarefas](FILA_TRABALHO.csv) atualizados: **258 artigos de origem, 856 unidades positivas Q +1 registro histórico T07 = 857 registros de fonte**, **40 vistas em 26 de 48 títulos**, 22 títulos sem texto. **+11 artigos, +37 unidades, +3 títulos**, sem contar veto ou histórico no denominador positivo.
- **QA remoto verificado:** comparação exata das 40 vistas com o Código em quatro blocos de 10; 258 cabeçalhos; hashes das quatro novas fontes iguais aos manifestos; contagens 13/2/7/15 corretas; matriz soma 258 artigos/856 unidades, 26 preenchidos, painel e quadro coincidem; 56 IDs únicos de fila, T13 reservado.
- [Validador R19](../scripts/validar_r19_horizontal_ci.py) e [workflow autossuficiente](../.github/workflows/clf-r19-autossuficiente.yml) criados para procurar superar dependência de checkouts setoriais antigos. **A mera criação dos arquivos e QA remoto não implica que o CI tenha aprovado.**

## PENDENTE — achado de CI P0 comprovado, diagnóstico incompleto

Quatro workflows do GitHub Actions associados à versão R19 **terminaram com conclusão `failure`**, incluindo o novo workflow independente:

| Workflow | Run | Estado |
|---|---:|---|
| CLF R19 — QA documental autossuficiente | [38792002923](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38792002923) | failure |
| Integridade estrutural CLF | [38792002924](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38792002924) | failure |
| Corpus experimental T07 | [38792002953](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38792002953) | failure |
| Prévia T24 | [38792002886](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38792002886) | failure |

As três últimas falhas **já ocorriam** em PRs #62 e #63, não demonstrando causalidade da R19; porém a falha do novo teste autossuficiente também não pôde ser diagnosticada. Na consulta, o job do workflow R19 foi concluído em `failure`, com `steps=null` e lista vazia de etapas; a tentativa de buscar logs respondeu **404 BlobNotFound**. **Não é possível saber se a falha decorre do executor, das permissões, da configuração YAML, do script ou do conteúdo sem logs ou execução independente.**

- **P0 bloqueante:** manter `CLF-TRANSVERSAL-006` e `CLF-TRANSVERSAL-007` abertos, investigar execução e logs no GitHub, rodar verificador em checkout válido e corrigir o problema demonstrado. Não alegar CI verde nem autorizar merge.
- **Proveniência:** texto Câmara/Planalto cotejado em HTML, sem DOU fac-símile original e alteradoras; revisão C0-J, intertemporalidade, espécie e competências ainda pendentes.
- **Governança:** C0-J=0; M aprovada=0; DEC-016 pendente; revogação, renumeração definitiva e merge=0.

## PRÓXIMO
1. **Resolver ou isolar com prova** as quatro falhas de Actions: consultar runs/logs pelo GitHub UI ou exportar execução local documentada do script autossuficiente; realizar ajustes apenas após diagnóstico.
2. Manter expansão horizontal em títulos ausentes, alternando áreas (T02/T10/T21/T35/T39/T45 candidatos) sem retomar concentração setorial, com frente vertical pequena e fontes oficiais.
3. Definir plano de cotejo DOU por diploma e gate normativo de recepção, eficácia, renumeração e interfaces, preservando a reserva T13 e a autonomia do projeto constitucional CF.

**Resultado material:** entrega documental real em PR #64, mas **CI reprovado e equivalência jurídica não ratificada**.