# T24.M01 — Rodada 04 / F1-C: pacote de continuidade

**Corte:** 14/10/2026 · **Frente:** T24.M01 · **Issue:** [#37](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/37) · **PR:** [#38 (draft)](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/38).  
**CLF main verificada na abertura:** `16fba172c875c7a0de388288fe70005c944021d6`. **Branch:** `modulo/T24-M01-jurisdicao-sujeitos-f0-f1-20261014`.  
**CF futura:** cenário condicional de projeto distinto; SHA histórico visto em rodada anterior, mas **não inspecionado/revalidado** aqui. Direito vigente: CF/1988 (referências constitucionais do módulo, não auditoria artigo a artigo).

## FEITO — entregas demonstráveis

| Produto | Evidência GitHub | Escopo de comprovação |
|---|---|---|
| [Concordância crítica de 106 origens](F1C_CONCORDANCIA_CRITICA_106.csv) | Commit `51ad8cd42815593a8cf1e09b34f574847e84b57d` | 3 subunidades com **pares literais de alteração**; 103 demais apenas localização e status Q, não C0 |
| [Reconciliadas 26 prioridades com 106 unidades](F1C_RECONCILIACAO_26_PARA_106.csv) | Commit `763ef12b0d047c2f8f20fa59380c74394652bc8d` | 26 grupos localizados, 49 vinculações unidade/grupo sem perda de identificadores; não é texto de destino |
| [Pesquisa e análise de lei, temporalidade e jurisprudência](RELATORIO_F1C_CADEIA_JURISPRUDENCIA_TESTES.md) | Commit `4ae4d96c459a15226eec092ebea0650ea3dace52` | CPC 75 III/§5º, 77 VII, Leis 14.195/2021 e 14.341/2022; STJ Tema 1178, Súmula 481, REsp 1088068/MG, AREsp 2974466/RJ, informativo AREsp 2762026/PR |
| 12 contraprovas documentais | Relatório F1-C | Hipóteses aplicadas à normativa/precedentes; **não testes de uma minuta CLF existente** |

**Fontes jurídicas consultadas, em 14/10/2026:** CPC original/atualizado na Câmara, art. 44 e 58 da Lei 14.195/2021, arts. 12–15 Lei 14.341/2022, Lei 13.146/2015 arts. 84–85, Tema 1178 ficha STJ, Súmula 481, inteiro teor REsp 1.088.068/MG, inteiro teor AREsp 2.974.466/RJ, informativo AREsp 2.762.026/PR. Endereços oficiais e recortes no relatório.

**Diferenças históricas provadas:** art. 75 III (nova redação) e §5º (acréscimo) com DOU 19/05/2022; art. 77 VII (acréscimo) com DOU 27/08/2021. Preservar efeitos temporais e delimitação de representação municipal; art. 77 §2º menciona apenas IV/VI. Demais unidades não receberam rótulo de equivalência.

## PENDENTE / NÃO VERIFICADO

- **103 pares literais não certificados**: não houve extração/normalização integral dos HTML oficiais para comparação por string e auditoria das leis modificativas de cada unidade; **o documento F1-C é parcial**.
- **Jurisprudência:** integral do AREsp 2.762.026/PR, pesquisa de contraexemplos de 2026 e extensão do regime de saneamento art. 76; conferir consequências em leis de custas e microssistemas especiais.
- **Arquitetura:** destino normativo aprovado em T24.M01 vs T24.M02/M04/T06/T13/T32/T01; tipos C0/C1/M ainda não definidos no projeto.
- **CF:** aplicação da CF/1988 vigente sem comparação com conteúdo atual da proposta constitucional; diferenças só por eventual nota de interface.
- **Governança:** PR é documental e **não foi integrado**; CI/checks e revisão adversarial independente no SHA terminal devem ser conferidos. O projeto permanece `PLANEJADO`, com F1 global em aberto. Nenhuma norma ou revogação CLF aprovada.
- **Conflito concorrente:** conservar `F1B_SUBUNIDADES_PRIORITARIAS.csv`, `F1B_MATRIZ_SUBUNIDADES_70-81_98-102.csv` e relatórios de ambas as pesquisas; não reescrever arquivos concorrentes sem revisão central.

## PRÓXIMO PASSO — prioridade executável única

**T24.M01 / F1-C2:** concluir paridade **literal** e sequência temporal **das 103 unidades ainda sem par de textos** no CPC arts. 70–81 e 98–102.  
**Insumos:** publicação original Câmara 2015, consolidada Câmara/Planalto datada 2026, leis modificadoras e DOU.  
**Entregável:** tabela de cada subunidade com texto original/atual, diferença normalizada, ato modificador, data de eficácia, fonte, hash/controle de versão, vínculo ao grupo F1-B e destino de trabalho.  
**Critério de aceite:** todas as 106 unidades com pares literais confirmados ou Q documental justificado; revisão dos efeitos jurídicos, fontes oficiais e interfaces; não classificar C0 apenas pelo resultado de um diff automatizado.

**Fila futura:** F1-D CPC arts. 82–97 e 103–187; comparação com juizados e T06; revisão central de reserva de espécie/iniciativa.

## COORDENAÇÃO / CONTROLE

- Interfaces principais: T01 (regra geral), T03/T06 (entes e Justiça), T13/T32 (capacidade/curatela), T14/T17 (direitos reais e família), T24.M02 (atos/cadastro/custas), T24.M04 (recursos e gratuidade), T24.M05 (execução).
- Propostas jurídicas continuam **Q**, sem M aprovada; textos reproduzidos correspondem ao **direito positivo** publicado, não à minuta CLF.
- Dados da matriz foram conferidos na execução: 106 origens distintas, 3 mudanças com literal, 103 Q; mapa de 26 prioridades tem 26 grupos encontrados e 49 correspondências.
- Atualização do PR: comentário de coordenação a inserir e rechecagem do SHA. CI pendente.

- [x] Chequei `main` e PRs concorrentes.
- [x] Confrontei textos publicados dos três dispositivos alterados.
- [x] Preservei inventários paralelos e documentos anteriores.
- [x] Registrei FEITO/PENDENTE/PRÓXIMO e fontes.
- [ ] Equivalência literal integral certificada.
- [ ] CI revisada no último SHA e integração autorizada.
