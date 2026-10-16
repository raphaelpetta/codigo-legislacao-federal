# CLF — R30 em 16/10/2026: Sociedade por ações e auditoria intersetorial

**Origem:** PR #79 draft, HEAD `b9672a6653f16c28c34be4ef87bd51950c99485a`. R30 permanece dependente, sem fusão à main ou homologação jurídica.

## FEITO

- **T18 novo:** [Lei 6.404/1976, arts. 1º–3º](../produto/vistas/T18_SA_LEI6404_ART1_3_PREVIA_Q.md), **3 artigos/8 unidades Q**, [espelho 1:1](../modulos/T18/M01_ESPELHO_LEI6404_ART1_3_8_Q.csv), [manifesto Git SHA](../produto/fontes/T18_M01_SA_8_R30_v1.json). A Câmara [original](https://www2.camara.leg.br/legin/fed/lei/1970-1979/lei-6404-15-dezembro-1976-368447-publicacaooriginal-1-pl.html) e [atualizada](https://www2.camara.leg.br/legin/fed/lei/1970-1979/lei-6404-15-dezembro-1976-368447-normaatualizada-pl.html) trazem o mesmo conteúdo substantivo dos oito dispositivos do recorte. Não confundir HTML com DOU fac-símile ou homologação.
- **Nove gates substantivos:** [matriz R30](44_R30_AUDITORIA_T18_T34_T36_CI_20261016.csv) distingue responsabilidade por preço de emissão de deveres por abuso e administração; objeto social estatutário de autorização estatal; denominação empresarial de marca; ações e CVM de companhia aberta; regime S.A. de sociedade de economia mista versus LREF art2; T34 veto art5 §3 histórico sem positivo e T36 XXI eficaz/XXII/XXIII sujeitos a vacatio para 2027, além do incidente CI.
- **Produto integrado:** 60 componentes Q em **41/48 títulos**, **308 artigos de origem/1051 unidades positivas +1 histórico T07 =1052 registros**; +3 artigos/+8 positivas/+1 título. Sete títulos vazios, T13 reservado. Índice/código, matriz/painel 48/48, quadro e guia, fila **83 tarefas/83 IDs distintos**.
- **QA proposto:** script `scripts/validar_t18_sociedades_ativo.py` chama oito unidades, SHA, texto 1:1, 3 artigos e 9 gates; invocado em `scripts/validar_operacao_local.sh`, e script de gates ativos incorpora matriz R30. Sua criação não prova execução Python em Actions.

## PENDENTE

- **C0-J=0; M=0; DEC-016 pendente; sem revogação, renumeração definitiva, positivação ou merge.**
- CI P0 [#66](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/66) ainda sem diagnóstico causal (jobs de smoke sem checkout já falhavam antes dos steps); anotações inacessíveis pelo conector.
- DOU de 1976, jurisprudência e exceções, disciplina CVM, sociedades estatais, regime registral e mutações do direito comercial devem ser auditados juridicamente antes de promover o recorte a C0-J.

**Próxima decisão executiva:** obter mensagem literal do CI, executar QA em checkout de três fontes setoriais, controlar efeitos materiais dos dispositivos e escolher entre profundidade/horizontalidade segundo ganho marginal.

## QA remoto pós-abertura do PR #80

- A árvore Git da base R29 (450 entradas) e a árvore do commit de abertura R30 (457 entradas) têm `truncated=false`. A verificação cruzada confirma **59/59 pares preexistentes vista/manifesto inalterados por SHA**; o T18 possui objetos novos próprios, sem substituição de componentes anteriores.
- **T18:** espelho Git blob `4ed0705c0fbe55ebe5af99ab483a1c62ae04c673` idêntico ao manifesto, 8/8 linhas Q de origem, três artigos de origem, correspondência da vista em seu bloco do Código, **308 cabeçalhos positivos de artigo**, índice 60 componentes/41 títulos, matriz e painel com **48/48 registros** coerentes e C0-J=0, fila **83 tarefas/83 IDs distintos**, nove gates R30 sem duplicação, T13 reservado.
- **CI no commit de abertura R30 `134950d701e3a4e05c3e1ff0fb3947c6faa20a67`:** cinco workflows `completed/failure`. No [run de diagnóstico 38870390405](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38870390405), `runner-smoke` **sem checkout** (job `116872836780`) e `corpus-r20` **com checkout** (job `116872836512`) falharam com **zero steps**. Seis checks exibem duas annotations cada, sem acesso ao texto causal pela conexão atual. **Não se comprovou CI verde nem execução do novo Python**, independentemente de sucesso da auditoria remota por Git.
- **Portas independentes:** fonte institucional HTML e Git SHA provam identidade documental, não cotejo do DOU em fac-símile, eficácia e interpretação jurídica vinculante, nem autorização para M, C0-J ou solução DEC-016.
