# T24.M01 — Complemento coordenado ao pacote de continuidade da rodada 03 (F1-B)

**Data de corte:** 14/10/2026. **Issue:** [#37](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/37). **PR:** [#38 — rascunho](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/38). **Base:** `main` `16fba172c875c7a0de388288fe70005c944021d6`. **Branch:** `modulo/T24-M01-jurisdicao-sujeitos-f0-f1-20261014`. **CF proposta:** somente referência condicional anterior, não objeto desta auditoria.

**Coexistência de frentes no mesmo PR:** durante a rodada observou-se que os arquivos `F1B_MATRIZ_17_ARTIGOS.csv`, `F1B_SUBUNIDADES_PRIORITARIAS.csv`, `RELATORIO_F1B_SUJEITOS_E_GRATUIDADE.md` e `PACOTE_CONTINUIDADE_RODADA_03.md` **já haviam sido produzidos por outra execução no mesmo PR**, cobrindo **26 registros prioritários**, sem inventário literal integral. Este pacote é **complementar** e não os substitui. Para evitar sobrescrita e conflitos, os novos arquivos têm nomes próprios; a coordenação deverá confrontar as duas seleções antes de aceitar uma versão canônica.

## FEITO (complemento desta execução)

| Entrega | Arquivo (branch, não main) | Verificação |
|---|---|---|
| Mapa abrangente de **17 artigos CPC (70–81; 98–102), com 106 unidades funcionais (73+33)** e localização por incisos/parágrafos | [F1B_MATRIZ_SUBUNIDADES_70-81_98-102.csv](F1B_MATRIZ_SUBUNIDADES_70-81_98-102.csv), commit `9c9f810902958309287358f7906af51d34210e6e` | Teste da leitura do CSV: 17 artigos na sequência esperada; 106 IDs únicos; distribuição 73+33; três mudanças identificadas |
| Relatório sobre **art. 75 III e §5º (Lei 14.341/2022)** e **art. 77 VII (Lei 14.195/2021)**; capacity, litisconsórcio conjugal, curador, sanções, gratuidade, precedentes | [RELATORIO_F1B_SUJEITOS_GRATUIDADE.md](RELATORIO_F1B_SUJEITOS_GRATUIDADE.md), commit `d0a8f88c021853d6c7e7e28b439ad4ceac3a2417` | Cotejo documental original/compilado Câmara; lei modificadora Câmara/Planalto; STJ Tema 1.178, Súmula 481, AREsp 2.762.026/PR e LBI 84–85 |
| Identificação de dez problemas/testes adversariais relevantes e necessidade de distinguir sancionamentos | Relatório | **Testes propostos, não executados**; Q, não M aprovada |

**Fontes verificadas em 14/10/2026:** CPC 2015 publicação original e edição atualizada da Câmara, arts. 70–81 e 98–102; Lei 14.341/2022, arts. 3º, 12–15; Lei 14.195/2021, art. 44; LBI arts. 84–85; STJ Tema 1.178 (tese/trânsito), Súmula 481 e Informativo de AREsp 2.762.026/PR. Todas as URLs e limitações estão no relatório. Não foi lida nesta rodada a redação integral do anteprojeto de CF.

## PENDENTE / NÃO VERIFICADO

1. As **106 unidades são resumos de função jurídica**, não reproduções literais controladas: não se alega cotejo por string, equivalência jurídico-material C0/C1, cobertura total das modificações históricas ou autorização de revogação.
2. **Confrontar** os quatro arquivos F1-B da pesquisa concorrente (17 artigos, 26 subunidades prioritárias) com a matriz de 106 subunidades: confirmar toda divergência de origem, remissão, alteração e evidência antes da integração. Unicidade de IDs apenas documental não prova semântica.
3. Ler acórdãos integrais e jurisprudência posterior específica sobre curadoria, saneamento da representação e gratuidade; distinguir precedente da Quarta Turma de repetitivo da Corte Especial.
4. Incorporar, com interfaces T03/T06/T13/T14/T17/T24.M02/M04/T32/T43, os regimes especiais, espécies normativas e causas de suspensão/exigibilidade de custas.
5. Revalidar o SHA de `main` e todos os checks/CI do **último commit** antes de qualquer integração. Não houve aprovação normativa.

## PRÓXIMO (única prioridade)

**F1-C coordenada:** cotejo literal/histórico dos **17 artigos** (originais/compilados, cadeia de alterações e DOU), resolução de possíveis diferenças entre o arquivo de **26 prioridades** e o arquivo de **106 unidades funcionais**, jurisprudência dos arts. 72/76/99–102 e teste adversarial das garantias. **Aceite:** prova de cada texto/subunidade, cadeia e transição, tabela de origem–destino sem omissões, ressalva Q quando incerto, e decisão central sobre localização; marcar C0/C1 só depois da equivalência comprovada.

## COORDENAÇÃO E CONTROLE

**Frente primária:** T24.M01. **Módulos impactados:** T03, T06, T13, T14, T16, T17, T18, T24.M02/M04/M05/M06, T32, T43 e T01. **CF/1988 é o direito positivo; CF proposta é apenas hipótese.** Este pacote não altera registro de decisões, índice nem `main`.

**Controle técnico executado:** leitura do próprio CSV via conexão GitHub confirmou 17 artigos, 106 linhas/IDs distintos, distribuição 73/33 e os três registros de alteração. **Controle não executado:** diff literal e equivalência jurídica; CI do SHA final ainda não confirmada.
