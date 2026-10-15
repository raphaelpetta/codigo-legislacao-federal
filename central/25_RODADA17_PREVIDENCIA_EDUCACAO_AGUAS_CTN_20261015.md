# CLF — Rodada 17: previdência, educação, recursos hídricos e competência tributária

**Corte:** 15/10/2026. **Entrega:** [PR #62 draft](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/62), empilhado no PR #61 (sem merge na main). [Issue central #48](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/48). **Natureza exclusiva: texto documental experimental Q, sem equivalência C0-J.**

## FEITO — três títulos antes vazios, conteúdo real

**T29 — Previdência Social.** [Lei 8.213/1991 arts. 1º–2º](../produto/vistas/T29_PREVIDENCIA_LEI8213_ART1_2_PREVIA_Q.md), **2 artigos/11 unidades Q**, [espelho](../modulos/T29/M01_ESPELHO_LEI8213_ART1_2_11_Q.csv), [manifesto Git SHA](../produto/fontes/T29_M01_8213_11_R17_v1.json); SHA `600524864bc83a50f6c57f80b17bf9905eaf55f5`. Fonte Câmara HTML atualizada [Lei 8.213](https://www2.camara.leg.br/legin/fed/lei/2025/lei-15108-13-marco-2025-797167-normaatualizada-pl.html), Planalto Lei 8.213 compilada. Art. 1º finalidade contributiva e proteção de eventos; art. 2º oito princípios + parágrafo único de participação. **Cautela:** a referência a desemprego involuntário no art. 1º não insere seguro-desemprego no RGPS (art. 9º §1º); a EC 103/2019 e demais regras especiais de cobertura exigem auditoria. Arts. 3º em diante/CNPS não integrados. DOU/vetos não conferidos em fac-símile.

**T33 — Educação.** [LDB Lei 9.394/1996 arts. 1º–3º](../produto/vistas/T33_EDUCACAO_LDB_ART1_3_PREVIA_Q.md), **3 artigos/20 unidades Q**, [espelho](../modulos/T33/M01_ESPELHO_LDB_ART1_3_20_Q.csv), [manifesto SHA](../produto/fontes/T33_M01_LDB_20_R17_v1.json); blob `678542153cac1414afc25e554103c9665dae213c`. Fonte [Câmara LDB atualizada](https://www2.camara.leg.br/legin/fed/lei/1996/lei-9394-20-dezembro-1996-362578-normaatualizada-pl.html). Art. 1º conceitos de educação em família/sociedade e educação escolar, art. 2º fins, art. 3º quinze incisos de princípios; **VIII** redação da Lei 14.644/2023 e **XV** acrescido pela Lei 15.001/2024. Arts. 4º e seguintes/dever de educar e organização dos sistemas fora do recorte. DOU 1996/alteradoras ainda não autenticados por imagem.

**T38 — Recursos hídricos.** [Lei 9.433/1997 arts. 1º–3º](../produto/vistas/T38_RECURSOS_HIDRICOS_9433_ART1_3_PREVIA_Q.md), **3 artigos/21 unidades Q**, [espelho](../modulos/T38/M01_ESPELHO_LEI9433_ART1_3_21_Q.csv), [manifesto SHA](../produto/fontes/T38_M01_9433_21_R17_v1.json), blob `023c98ee9d2bc8fb7c02cfbe40b631eeacdd788a`. Fonte [Câmara Lei 9.433 atualizada](https://www2.camara.leg.br/legin/fed/lei/1997/lei-9433-8-janeiro-1997-374778-normaatualizada-pl.html), Planalto. Água domínio público e escassez com prioridade de consumo humano e animais, usos múltiplos e gestão descentralizada. Art. 2º IV acrescido pela Lei 13.501/2017. **Lei 15.269/2025 art. 4º** alterou art. 2º II, acrescentou V, alterou art. 3º III e acrescentou VII; art. 24 IV define produção de efeitos a partir da publicação para estes, não confundir com outros incisos da alteradora que têm efeitos diferidos para 2026/2027. DOU e vetos da Lei 9.433 ainda pendentes.

## FEITO — uma frente vertical contida

**T12 — CTN (Lei 5.172/1966), arts. 6º–8º**, **3 artigos/7 unidades Q** adicionais: [vista](../produto/vistas/T12_CTN_ART6_8_PREVIA_Q.md), [espelho](../modulos/T12/M01_ESPELHO_CTN_ART6_8_7_Q.csv), [manifesto](../produto/fontes/T12_M01_CTN_7_R17_v1.json), blob `2aab1646c0e1ff8548e6aa9545d33dfe38f16f20`. Contrastar competência tributária indelegável, distribuição do produto da arrecadação e atribuição de execução administrativa. **Art. 7º remete à Constituição histórica art. 18 §3º**, não vigente em 2026; não substituir sem controle de alteração. Normas gerais do CTN recepcionadas sob reserva constitucional de lei complementar, DEC-016 ainda pendente. T12 agora **arts. 1º–8º, 8 artigos/14 unidades Q**.

## FEITO — consolidação transversal e integridade

- [Código único de trabalho](../produto/CODIGO_DE_TRABALHO.md) e [índice](../produto/fontes/indice_livros.json) ampliados para **237 artigos/772 unidades positivas +1 histórico T07, 32 vistas documentais em 20 títulos**; 28 de 48 títulos ainda sem texto.
- [Painel](PAINEL_GERADO.csv), [quadro](QUADRO_PRODUTO.csv), [matriz de 48 títulos](01_MATRIZ_AUDITORIA_48_TITULOS_20261015.csv), [guia](../produto/00_LEIA_O_CODIGO.md), [fila de 45 tarefas](FILA_TRABALHO.csv) e [verificador R17](../scripts/validar_r17_horizontal.py) com [roteiro offline](../scripts/validar_operacao_local.sh) sincronizados. **+11 artigos, +59 unidades Q, +3 títulos novos**.
- Em GitHub, podem ser conferidos SHAs dos quatro arquivos origem e seus manifestos, contagens de artigos e 32 vistas do Código. **Isso não equivale a ter executado Python/Actions nem a atestar equivalência legal do DOU.**
- Sem uso da reserva T13, sem mescla, renumeração definitiva, revogação ou alteração do projeto CF.

## PENDENTE

1. DOU fac-símile origens e alterações, recepção e efeitos temporais (EC 103/2019, leis educacionais 2013–2024, Lei 15.269/2025, reforma tributária EC 132/2023). C0-J ainda zero por título.
2. Coerência dos regimes: previdenciário contributivo versus seguro-desemprego, educação com competências estaduais/municipais, recursos hídricos CF 21 XIX e natureza pública da água, CTN lei complementar recepcionada e delegação meramente administrativa.
3. Execução comprovada dos scripts Python/Actions, cadeia de PRs draft #49/#53–#62 e gates jurídicos antes de propor merge, sem prejuízo do controle de veto Lei 4.320 art. 3º herdado da R16.
4. **28 títulos sem texto**: contagem de títulos não é percentual do volume do direito positivo federal.

## PRÓXIMO

- Abrir 2–3 títulos ainda vazios por alto ganho marginal e fontes verificáveis, e somente uma expansão vertical alternada.
- Realizar auditoria DOU por diplomática, retificações e vetos, com confronto de especialidades e efeitos, evitando falsa certificação apenas por cópia de HTML.
- Executar testes em checkout independente ou CI autorizado e guardar provas, com DEC-016 ainda sob deliberação.

**Estado formal:** C0-J=0, M=0, DEC-016 pendente; revogação, fusão, renumeração definitiva e merge não autorizados.
