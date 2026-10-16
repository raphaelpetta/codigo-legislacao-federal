# CLF — R26: auditoria integral de proveniência Git e QA ativo (15/10/2026)

**Base:** PR #72 draft, HEAD `2ce1ccb956bbc9bd2b8f7b470bd349fcee8b3765`; incremento experimental **0 artigos/0 unidades/0 títulos**. O objetivo da rodada é a integridade total da cadeia de origem, a classificação de pendências setoriais e a prevenção de **falso verde** nos scripts. Não houve fusão à main ou certificação de equivalência jurídica.

## 1. Contraprova remota dos 55 manifestos

Foi obtida por [GitHub Git Trees](https://api.github.com/repos/raphaelpetta/codigo-legislacao-federal/git/trees/b6abf84a15a7aa751e91567e99341711704e10a8?recursive=1) a árvore imutável do HEAD base R25 (**424 entradas, `truncated=false`**). Cada uma das **55 entradas do índice** foi confrontada com seu manifesto versionado, sua vista e o blob SHA de origem disponível.

| Categoria | Quantidade | Resultado |
|---|---:|---|
| Fonte local 1:1 | **52** | 52/52 caminhos e hashes SHA exatos; 0 divergências |
| Origem externa T07 | **1** | Texto e concordância PR #45 fixados no SHA; ausência local explícita |
| Origem externa T25 | **1** | Espelho 39 unidades PR #32 fixado no SHA; ausência local explícita |
| Origem composta T24 | **1** | 106 PR #38 +75 central =181; componentes separados e rastreados |
| **Total** | **55** | 55 manifestos/vistas encontrados; não são 55 origens locais |

**T07:** commit setorial `2a4d1eefa864f44435aec70ed0cc55a96b718b64`: ensaio `0eea9c97a110d278d6eb4efd37f4a8bbfd61ecb0`, concordância `c9cbf7d202ea9d01b9ffd48256bf3efeba6f226c`; ambos conferidos diretamente no PR45 pela R25. **215 registros, 214 positivos +1 histórico, 11 C1 Q**.

**T25:** commit setorial `3f0b56273caebfdbaba87ec4e87988da9f12c6c9`: espelho de 39 unidades `40b5c03d72f975aad1339c605399f7f66ec056d0`, conferido pela R25. A ausência da fonte local é **pendência setorial controlada** e não autoriza omitir a verificação no checkout original.

**T24 (composto):** manifesto `produto/fontes/T24_CPC_70_102_181_v1.json` descreve 106 unidades setoriais PR38 `3fdbfa10b8d288b1cef56c78b47cf3cb1eb28745` e 75 unidades editoriais locais, 33 artigos. A fonte externa PR38 SHA `a0562c236cda3a49b842417bb27417e84484f363` foi reconfirmada; submanifesto local `T24_M01_106_v1.json` mantém a mesma pinagem. **Cinco objetos locais** do manifesto composto tiveram SHAs idênticos à árvore: vista 106 `211f4acc8e3f34a3eb3b01856db3949a26cb07a0`; concordância 106 `b3542c54db70d9f5721fbe64ec372164b99b56ef`; fonte 75 `5a1b1123e29b95f5777ec2bffb8eda5b84e4a18b`; vista 75 `e35b35aafe13bd3740f3714eecc4c53afbc0cc1d`; concordância 75 `c2e722d62a46be10937c4ec17ec4d4dfbd270330`. **Nenhuma segunda transcrição jurídica independente dos 75** foi declarada.

## 2. Invariante técnico efetivamente melhorado

A versão anterior de `scripts/validar_corpus_ativo.py` aceitava automaticamente manifestos **sem SHA/caminho** como mera pendência, de forma genérica. Isso podia mascarar um novo Livro com fonte local perdida ou manifesto sem rastreabilidade. Agora o script exige origem local existente, hash Git verificável e contagem CSV quando declarada; trata **apenas T07/T25 e o composto T24** por portas formais conhecidas, exigindo SHAs e commits fixados. A ausência de fonte nova inesperada gera erro. A reconstrução das vistas do Código e a vedação de promoção C0-J/M/DEC016 permanecem.

O roteiro `validar_operacao_local.sh` passa a chamar os validadores **ativos** de corpus e gates jurídicos, sem rodar os verificadores R24/R25 de **snapshot 55/74** quando o corpus crescer; esses permanecem versionados para auditoria histórica. Os checkouts externos T07/T24/T25 continuam obrigatórios para fechamento de `OK DOCUMENTAL LOCAL` — não podem ser substituídos pelo controle de manifesto.

**Limite explícito:** os hashes da árvore foram conferidos remotamente e são evidência real. O novo Python ainda **não foi executado** neste checkout/CI; não registrar sucesso de execução antes de observá-lo. As verificações de SHA confirmam identidade de bytes, **não autenticidade do DOU, efeitos jurídicos ou competência normativa**.

## 3. CI — evidência P0 reiterada

Reconsulta ao run [38839253139](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38839253139), job `runner-smoke` `116775300440`: `completed/failure`, **0 steps**. Download do log retornou **HTTP 404, XML `BlobNotFound`**. A causa concreta da falha não foi demonstrada por essas respostas e não deve ser presumida como falha Python, orçamento/runner ou permissão antes de abrir as duas anotações do check-run na UI autenticada. [Incidente #66](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/66).

## Estado e próximo investimento

O corpus mantém **55 componentes Q, 37/48 títulos, 294 artigos, 985 unidades positivas +1 histórica**. **C0-J=0, M=0, DEC-016 pendente, sem merge, revogação, renumeração final ou promulgação**.

**Próximo:** (1) recuperar mensagem literal do CI e efetivar runner funcional; (2) rodar novos validadores em checkout completo e registrar stdout/exit status; (3) cotejar fontes DOU/julgados e resolver gates R3 de maior risco T07/T24/T25, sem transformar duplicação textual em certificação jurídica.
