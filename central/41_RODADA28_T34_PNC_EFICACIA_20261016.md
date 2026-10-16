# CLF — R28 (16/10/2026): Estatuto de Museus, PNC e eficácia urbana

**Origem:** PR #76 draft, HEAD `c75e84b17160fafa3df9493b718bcc32f4028fd7`. R28 empilhada, não altera main, não valida C0-J nem promove reforma M.

## FEITO — expansão seletiva com gate jurídico de temporalidade

- **T34 novo:** Lei **11.904/2009**, Estatuto de Museus, arts. **1º–2º**, **2 artigos/10 unidades Q** com [vista](../produto/vistas/T34_MUSEUS_LEI11904_ART1_2_PREVIA_Q.md), [espelho](../modulos/T34/M01_ESPELHO_MUSEUS_LEI11904_ART1_2_10_Q.csv), [manifesto SHA](../produto/fontes/T34_M01_MUSEUS_10_R28_v1.json). Direitos culturais, função social, acesso universal, proteção de acervos e inclusão de processos museológicos. Lei não se aplica automaticamente a bibliotecas, arquivos ou coleções visitáveis (art. 6º); competência e DOU pendentes.
- **PNC e remissão:** o art. 2º, PU da Lei 11.904 faz referência ao Plano Nacional de Cultura. A Lei 12.343/2010 teve a duração do Plano estendida a **14 anos** pela Lei 14.468/2022, encerrada em **2024** conforme [MinC](https://www.gov.br/cultura/pt-br/assuntos/noticias-defeso-eleitoral/plano-nacional-de-cultura-como-foi-construida-a-proposta-que-deve-guiar-as-politicas-culturais-na-proxima-decada/). A aprovação do [PL 5.894/2025 na Câmara em 01/09/2026](https://www.camara.leg.br/proposicoesWeb/fichadetramitacao?idProposicao=2586419) **não equivale a lei promulgada**. Nem o fim de prazo do plano implica revogação automática do Estatuto de Museus, nem o projeto futuro pode ser transposto ao corpo normativo.
- **Auditoria de eficácia T36 consolidada:** [sete gates R28](40_R28_MUSEUS_PNC_URBANISMO_VIGENCIA_20261016.csv) documentam a eficácia do inciso XXI do Estatuto da Cidade pela [Lei 15.333/2026](https://www2.camara.leg.br/legin/fed/lei/2026/lei-15333-7-janeiro-2026-798636-publicacaooriginal-177719-pl.html) após 90 dias da publicação de 08/01/2026 e a **vacatio anual** da [Lei 15.432/2026](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/lei/l15432.htm), publicada em edição extra de 14/06/2026, que adia incisos XXII e XXIII e outras alterações/revogações para junho de 2027. Não somar como atuais nem antecipar revogação de Lei 12.587/2012.
- **Corpus recomposto:** 58 componentes Q em **40/48 títulos**, **301 artigos de origem / 1032 unidades positivas +1 histórico T07 (1033 registros)**; incremento +2 artigos/+10 unidades/+1 título. **Oito títulos sem texto**, T13 reservado. Índice, Código, matriz e painel 48 títulos, quadro, guia e fila 79 tarefas/79 IDs únicos.
- **QA novo:** [`validar_r28_cultura_eficacia.py`](../scripts/validar_r28_cultura_eficacia.py) no roteiro de operação, com SHA Git, dez unidades, separação de PNC expirado/projeto novo/lei vigente/eficácia futura. A presença do script não certifica execução Python.

## PENDENTE

- **Prova DOU**: original de janeiro de 2009, legislação 2010/2022/2024/2026 e DOU da Lei 15.432 edição extra, mais inteiros teores e jurisprudência de efeitos. Texto HTML oficial não equivale a fac-símile.
- **CI P0 [#66](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/66)**: workflows anteriores falharam antes dos steps, inclusive runner-smoke sem checkout; annotations não legíveis pela conexão, sem causalidade demonstrada.
- **C0-J=0, M=0, DEC-016 pendente; sem revogação, renumeração definitiva, promulgação ou merge.**

**Próximo:** recuperar mensagem causal do CI, executar QA no checkout real, auditar efeitos das remissões em títulos múltiplos e continuar pelo ganho marginal, não por expansão mecânica.

## Auditoria remota realizada após abertura do PR #78

- Comparação da árvore Git no HEAD base R27 `c75e84b17160fafa3df9493b718bcc32f4028fd7` (**437 entradas**) com o commit de abertura R28 `f467d506b4d386121a0608e0d3592b0edb9dd745` (**444 entradas**), ambas `truncated=false`: os **57 pares vista/manifesto preexistentes mantiveram SHA inalterado**; o novo T34 aparece com vista e manifesto próprios.
- QA remoto da fonte T34: blob do espelho `588635b0615e9b121bb031e1740ae043b7ef336d` **idêntico ao manifesto**; **10/10 registros Q**, **2/2 artigos**, 8 unidades no art. 2º (caput, I–VI, PU). Sua vista foi encontrada integralmente no bloco correspondente do Código único, que conta **301 cabeçalhos**; índice 58 livros/40 títulos, 1.033 registros incluindo o histórico T07; matriz/painel **48/48** reconciliados; fila **79 IDs únicos**, matriz R28 **7 gates únicos**. Reserva T13 intocada.
- CI no SHA de abertura: cinco runs `completed/failure`, incluindo [diagnóstico 38851762757](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38851762757). `runner-smoke` **sem checkout**, job `116814316185`, e `corpus-r20` **com checkout**, job `116814316266`, concluíram `failure` com **zero steps** cada. Seis check-runs, cada qual com duas annotations, mas o conteúdo não foi recuperado pela conexão disponível. **Sem diagnóstico causal nem CI verde**.
- A verificação de SHA e coerência documental **não equivale a execução do Python** do novo validador nem a cotejo DOU ou C0-J. As declarações jurídicas desta rodada continuam condicionadas à auditoria material.
