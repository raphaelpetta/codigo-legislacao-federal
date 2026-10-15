# T25.M01 — Pacote obrigatório de continuidade, ciclo 05

**Data e corte:** 14/10/2026, Brasília. **Sessão:** T25.M01 — legislação penal geral, regimes setoriais e fonte histórica. **Responsável funcional:** frente penal, coordenação do CLF via [issue #31](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/31) e [PR #32 (draft)](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/32).

**Versões:** `main` CLF ao iniciar = `16fba172c875c7a0de388288fe70005c944021d6`; conferida novamente após os documentos, mesma SHA. O commit desde o ciclo 04 (`1974be2...16fba17`) tocou apenas T07.M03, governança/status e validador, **não** T25. A branch de pesquisa `modulo/T25-parte-geral-f0-f1` não foi atualizada/rebaseada contra essa `main` (revisar antes de integrar). Constituição em elaboração: `main` `a763f5edf058a6622cd3d239efa6bf8e77b46e09`; conferida somente como referência de versão, sem estudo material ou decisão importada.

## 1. FEITO — entregas persistidas na BRANCH, não na main

| Entrega | Arquivo/artefato | Estado e tipo |
|---|---|---|
| Achado da edição original do DOU 13/07/1984, Seção 1, edição 135, com Lei 7.209 na p.10217 | [Ficha do arquivo da Imprensa Nacional](https://incombeta.in.gov.br/web/dou/dou/-/document_library/kcmautn6AnNs/view_file/432123) e [Senado](https://legis.senado.leg.br/norma/549085) | **Arquivo localizado, SEM leitura do fac-símile**, portanto sem validação da textualidade de 1984 |
| Análise contrastiva CP e Parte Geral do Código Penal Militar (arts.1º–17) | `DOSSIE_05_HISTORICO_E_SUBSISTEMAS_PENAIS.md` | Lei 14.688/2023 alterou CPM art.2º; paralelismos e diferenças relevantes documentados; nenhum juízo final de constitucionalidade |
| Matriz de 16 relações selecionadas entre CP, LCP, CPM, Eleitoral e outras leis | `MATRIZ_RELACOES_REGIME_GERAL_CICLO05.csv` | 16 relações, NÃO 16 leis ou 16 derrogações; fontes oficiais individuais; `Q` quanto à proposta futura |
| Três modelos de arquitetura A/B/C e 14 casos de teste | `DOSSIE_05_HISTORICO_E_SUBSISTEMAS_PENAIS.md` | alternativas não aprovadas; efeitos jurídicos não calculados exaustivamente |
| Índice T25.M01 | `README.md` | versão documental cumulativa ciclos 01–05 |

**Fontes efetivamente lidas:**
1. [Câmara CP Militar DL 1.001/1969 atualizado, arts.1º–17, 2023 Lei 14.688](https://www2.camara.leg.br/legin/fed/declei/1960-1969/decreto-lei-1001-21-outubro-1969-376258-normaatualizada-pe.html).
2. [TSE Código Eleitoral, arts.283–288, 2026](https://www.tse.jus.br/legislacao/codigo-eleitoral/codigo-eleitoral-1/codigo-eleitoral-lei-nb0-4.737-de-15-de-julho-de-1965).
3. [Lei das Contravenções DL 3.688/1941 arts.1º–4º](https://www.planalto.gov.br/ccivil_03/decreto-lei/del3688.htm), [Lei de Introdução CP/LCP, DL 3.914/1941 art.1º](https://www.planalto.gov.br/ccivil_03/decreto-lei/del3914.htm).
4. [Lei de Tortura 9.455/1997 art.2º, Câmara atualizada](https://www2.camara.leg.br/legin/fed/lei/1997/lei-9455-7-abril-1997-349431-normaatualizada-pl.html).
5. [CTB art.291](https://www.planalto.gov.br/ccivil_03/leis/l9503compilado.htm), [ECA art.226](https://www.planalto.gov.br/ccivil_03/leis/l8069compilado.htm), [Lei de Migração 13.445/2017 arts.100–105](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2017/lei/l13445.htm), em recortes selecionados.
6. **Arquivo histórico encontrado, NÃO LIDO visualmente:** [Imprensa Nacional, DOU 13/07/1984, DO_1_19840713_135.PDF (14,9 MB)](https://incombeta.in.gov.br/web/dou/dou/-/document_library/kcmautn6AnNs/view_file/432123); [Planalto anexo Lei 7.209/1984](https://www.planalto.gov.br/ccivil_03/leis/1980-1988/anexo/ANL7209.pdf) é apenas índice estrutural, não o texto do DOU.

## 2. PENDENTE / NÃO VERIFICADO

| Questão | Evidência faltante | Bloqueia |
|---|---|---|
| Fac-símile original 1984 | PDF identificado, mas acesso ao arquivo integral de 14,9 MB excedeu limite de visualização/disponibilidade na sessão; fazer leitura de páginas 10.217 e subsequentes | Validação `C0-T` relativa ao DOU de 1984 |
| CP arts.3º,4º,12, diferenças digitais | comparar fotografia do DOU com Câmara/Senado/Planalto transcritos, corrigir origem de erros | História autêntica e C0-J |
| Regime penal militar completo | CPM 1–17 somente; verificar efeitos das mudanças Lei 14.688/2023, inconstitucionalidades e direito de tratados | Escolha A/B/C e minuta de Parte Geral |
| Direito penal eleitoral e LCP | conferir jurisprudência e legislação posterior que altera alcance e medidas | Remissões universais |
| CP art.12 e CPM art.17 | demonstrar que mudança da expressão `deste Código` não altera referente jurídico, inclusive leis penais militares especiais e contravenções | C1 ou consolidação jurídica |
| Compatibilidade constitucional | CF art.5º XXXIX/XL; art.22 I; Justiça Militar e tratados, com interfaces específicas | C0-J e M |
| Consulta ao anteprojeto de CF | versão SHA verificada, conteúdo não lido | Só eventual cenário de Constituição futura |
| Redação/revogação | Nenhuma norma CLF redigida ou aprovada nesta sessão; diferenças teóricas Q | Integração legislativa, DEC-016 |
| CI e PR | Checar a execução do validador no último SHA após gravar este arquivo; resultado estrutural não comprova equivalência jurídica | Integração da PR |

## 3. PRÓXIMO PASSO EXECUTÁVEL

**Tarefa prioritária:** obter/visualizar a edição `DO_1_19840713_135.PDF` no acervo da Imprensa Nacional, localizar p. 10.217 e seguintes, comparar a redação autêntica com as três versões digitais do CP **arts. 3º, 4º, 12**; registrar prova visual/página e atualizar a concordância documental. **Critério de aceitação:** por dispositivo, texto do fac-símile, página e coluna, versus texto da Câmara atualizado, natureza de cada divergência comprovada ou `A_VERIFICAR`; não alterar regime penal por conjectura.

**Em paralelo, na fila:** estudo da Parte Geral militar sob Lei 14.688/2023 e comparação dos Modelos A/B/C para art.12 do CP/17 CPM com 14 testes, interações T25.M02/M03, leis eleitorais, contravenções e legislação especial, antes de decidir regra geral integrada.

## 4. COORDENAÇÃO

**Módulos:** T01.M01/M04; T02; T05 (eleitoral); T23/T47/T48 (tratados e migração); T25.M01–M07; T26/T27; T32, T37, T41, T45. **CF vigente:** art.5 XXXIX/XL, art.22 I e competência da Justiça Militar, respeitando os limites materiais e direitos. **CF em construção:** projeto independente, não direito vigente. **Categoria de alteração:** `C0-T` apenas da versão compilada arts.1º–12 (ciclo 03); nenhuma equivalência `C0-J` comprovada, nenhuma revisão editorial `C1` aprovada, nenhuma reforma `M` escolhida; hipóteses `Q`.

- [x] Verificada `main`, PR e alteração concorrente antes e durante a rodada.
- [x] Local da fonte autêntica identificado e limite de leitura declarado.
- [x] Matriz de relações com fonte, dispositivo, destino provisório e interface.
- [x] Pesquisa distinta de validação jurídica/aprovação de reforma.
- [x] Pacote FEITO/PENDENTE/PRÓXIMO salvo em branch.
- [ ] CI último SHA, verificar após este commit.

**Regra de continuidade:** `governanca/18_PROTOCOLO_CONTINUIDADE_POR_RODADA.md`.
