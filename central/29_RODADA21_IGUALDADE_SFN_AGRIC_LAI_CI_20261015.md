# CLF — Rodada 21: igualdade racial, Sistema Financeiro Nacional, agricultura familiar e LAI

**Data/corte:** 15/10/2026. **Entrega:** [PR #68 draft](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/68) sobre [PR #67 draft](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/67), não mesclados. [Central CLF #48](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/48). Todos os novos textos são **Q (não homologados)**, sem decisões C0-J ou reforma M.

## FEITO — três títulos novos em áreas distintas

**T02 — Igualdade racial:** [vista Lei 12.288/2010, arts. 1º–2º](../produto/vistas/T02_IGUALDADE_RACIAL_LEI12288_ART1_2_PREVIA_Q.md), [espelho 9 unidades](../modulos/T02/M01_ESPELHO_EST_IGUALDADE_RACIAL_ART1_2_9_Q.csv), [manifesto fonte SHA](../produto/fontes/T02_M01_EIR_9_R21_v1.json). **2 artigos/9 unidades Q**, blob `48a99fe276610a940c4376a7d896b15c563b0b85`. [Câmara texto atualizado](https://www2.camara.leg.br/legin/fed/lei/2010/lei-12288-20-julho-2010-607324-normaatualizada-pl.html). Art. 1º com parágrafo único e seis definições, inclusive ações afirmativas e população negra por autodeclaração; art. 2º dever estatal e social de igualdade. **Não** presumir que a redação isolada do Estatuto resolve regimes concretos de concursos, coleta de dados raciais, avaliação, LBI ou precedentes de discriminação; T08/T33/T43 permanecem interfaces. DOU 21/07/2010 e alterações subsequentes (como Lei 14.553/2023 arts. 39/49) sem cotejo fac-símile.

**T21 — Sistema financeiro:** [vista Lei 4.595/1964, arts. 1º–2º](../produto/vistas/T21_SFN_LEI4595_ART1_2_PREVIA_Q.md), [espelho 7 unidades](../modulos/T21/M01_ESPELHO_LEI4595_ART1_2_7_Q.csv), [manifesto](../produto/fontes/T21_M01_SFN_7_R21_v1.json). **2 artigos/7 unidades Q**, blob `7876d9336c9fb8952333c7328503f122e55bc79b`. [Câmara Lei 4.595 atualizada](https://www2.camara.leg.br/legin/fed/lei/1960-1969/lei-4595-31-dezembro-1964-353886-normaatualizada-pl.html), [ficha com DOU e retificação](https://www2.camara.leg.br/legin/fed/lei/1960-1969/lei-4595-31-dezembro-1964-353886-norma-pl.html). Incisos II e IV art. 1º com denominações posteriores (**DL 278/1967** e **DL 1.940/1982**). O art. 2º é registro de criação histórica do CMN, não efeito de recriação por CLF. **LC 179/2021**, CF 192 e regulamentação do BCB/CMN exigem revisão de competências; art. 3º com revogações expressas fora do corpus. DOU 1964 e retificação 03/02/1965 não autenticados por imagem.

**T39 — Agricultura familiar:** [vista Lei 11.326/2006 arts. 1º–3º](../produto/vistas/T39_AGRICULTURA_FAMILIAR_ART1_3_PREVIA_Q.md), [espelho 17 unidades](../modulos/T39/M01_ESPELHO_AGRIC_FAMILIAR_ART1_3_17_Q.csv), [manifesto](../produto/fontes/T39_M01_AGF_17_R21_v1.json). **3 artigos/17 unidades Q**, blob `ee5eaa30cc0a36438afc4d6049489074a7466b0f`. [Câmara atualizada](https://www2.camara.leg.br/legin/fed/lei/2006/lei-11326-24-julho-2006-544830-normaatualizada-pl.html). Art. 3º: quatro requisitos e §1º sobre condomínio rural, §2º com seis categorias beneficiárias, §§3º–4º sobre critérios de crédito, com alterações **Lei 12.058/2009** e **Lei 12.512/2011**. O enquadramento não representa concessão automática, e critérios do caput não se transferem indevidamente aos grupos especiais do §2º. DOU 25/07/2006 e alteradoras sem cotejo fac-símile; Lei 14.828/2024 art. 5º XIII/XIV ainda fora.

## FEITO — vertical alternada

**T10 — LAI art. 4º:** [vista documental](../produto/vistas/T10_LAI_ART4_PREVIA_Q.md), [espelho 10 unidades](../modulos/T10/M01_ESPELHO_LAI_ART4_10_Q.csv), [manifesto](../produto/fontes/T10_M01_LAI_10_R21_v1.json). **1 artigo/10 unidades Q**, blob `47204e59ef75f24435ba1f43bbca9b49110a2248`; nove incisos definem informação, documento, sigilo, dado pessoal, tratamento, disponibilidade, autenticidade, integridade e primariedade. **T10 total: LAI arts. 1º–4º, 4 artigos/22 unidades Q.** LGPD e demais sigilos limitam a divulgação, sem afastar deveres de transparência.

## FEITO — corpus, controles e integridade

- [Código único experimental](../produto/CODIGO_DE_TRABALHO.md) e [índice de Livros](../produto/fontes/indice_livros.json): **274 artigos de origem / 938 unidades positivas textuais +1 histórico T07 = 939 registros**, **48 componentes em 32 de 48 títulos**, 16 ainda sem texto. Acréscimo da R21: **+8 artigos, +43 unidades e +3 títulos**.
- [Painel](PAINEL_GERADO.csv), [quadro](QUADRO_PRODUTO.csv), [matriz 48 títulos](01_MATRIZ_AUDITORIA_48_TITULOS_20261015.csv), [guia](../produto/00_LEIA_O_CODIGO.md), [fila de 66 tarefas](FILA_TRABALHO.csv) e [validador R21](../scripts/validar_r21_horizontal.py) no [roteiro local](../scripts/validar_operacao_local.sh). T13 reservado intacto; integração documental sem alterar constituição, competências, normas ou valores.
- **Nota de controle:** cotejo institucional em HTML não é cotejo fac-símile DOU. Correspondência fonte/código e execução efetiva Python/Actions são verificações diferentes. Scripts acrescidos **não comprovam execução bem-sucedida**.

### Resultado de QA remoto e CI no próprio PR #68

A leitura das **48 vistas em quatro grupos de 12** comprovou igualdade textual com `CODIGO_DE_TRABALHO.md`, 274 cabeçalhos de artigos e hashes coincidentes dos quatro espelhos R21 com os manifestos (9/7/17/10 unidades). A matriz dos 48 títulos tem 32 preenchidos, soma 274 artigos/938 unidades positivas; painel/guia/quadro e **66 tarefas com IDs únicos** conferidos. **Não é execução de Python nem certificação do DOU.**

No HEAD `8e2123e8a96d8c1e85d798202b91ffc0819c2cdb` do PR #68, o conector GitHub retornou **cinco workflows concluídos em `failure`**:
- [R20 diagnóstico do runner — run 38818337867](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38818337867);
- [T07 corpus — run 38818338238](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38818338238);
- [R19 QA autossuficiente — run 38818337802](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38818337802);
- [Integridade estrutural — run 38818337832](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38818337832);
- [T24 prévia — run 38818338092](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38818338092).

**Causa ainda não diagnosticada**: o teste anterior `runner-smoke`, sem checkout, também falhou e logs/steps retornaram 404/indisponíveis. A permanência dessas falhas não prova erros normativos nos recortes R21, mas **impede afirmar CI verde e bloqueará qualquer proposta de merge**.

## PENDENTE — CI P0, DOU e homologação jurídica

- No PR #67, os dois jobs do [diagnóstico de runner, run 38800172990](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38800172990), `runner-smoke` **sem checkout** e `corpus-r20` com checkout, tiveram **failure**. Também falharam checks anteriores de estrutura, T07, T24 e R19. O conector retorna **`404 BlobNotFound`** para logs e etapas vazias, de modo que não se pode atribuir causalidade certa ao script documental. **CI bloqueante.** Tarefas CLF-TRANSVERSAL-006/007/008/009 são P0, sem fechamento por presunção.
- DOU original e retificações (Lei 4.595/1964), alterações Lei 12.058/2009 e 12.512/2011, Lei 12.288/2010 e LAI 2011; análise jurídica de competência, dados pessoais, crédito, recepção e eficácia permanece pendente.
- **C0-J=0; M=0; DEC-016 pendente; revogações, renumeração definitiva e merges=0**. Nunca afirmar que 32 de 48 títulos correspondam à cobertura proporcional do direito federal.

## PRÓXIMO

1. Diagnosticar status de GitHub Actions pelo painel/runners/permissões, ou obter execução de checkout com logs acessíveis. **Gate P0 não liberado.**
2. Continuar abrindo 2–3 títulos ausentes de famílias não repetidas, com um aprofundamento vertical restrito.
3. Intensificar o cotejo DOU, recepção, vigência e remissões, submetendo eventuais C0-J somente à deliberação jurídica competente.

**Estado:** entrega documental real no PR #68, não homologada e não pronta para merge.
