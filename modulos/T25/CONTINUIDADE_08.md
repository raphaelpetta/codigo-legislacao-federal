# T25 — Pacote de continuidade 08 | Erro, coação e causas de exclusão do crime

**Data de trabalho e corte de fontes:** 14/10/2026, America/Sao_Paulo. **Frente:** T25.M02, com dependências M01/M03/T26/T27/T45. **Issue:** [#31](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/31) · **PR rascunho:** [#32](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/32) · **branch:** `modulo/T25-parte-geral-f0-f1`.

**Estado inicial e concorrência:** CLF `main` verificada antes dos commits e novamente antes deste pacote = `16fba172c875c7a0de388288fe70005c944021d6`; nenhuma alteração externa de T25 localizada. Último HEAD registrado no ciclo 07 = `5fa0b482f691c208c5b97a48ed08e7082d896002`; atualizar conferência do HEAD/CI após este arquivo. Projeto constitucional alternativo `main` = `b9dbdc540310ed5dc34fb1e5f314c46af343dc98`, somente cheque de versão, **não** fonte de direito vigente.

## 1. FEITO, salvo em branch e NÃO na main

| Entrega | Arquivo | Natureza, categoria e limite |
|---|---|---|
| Inventário CPM arts.41–45 com **11 subunidades e IDs únicos** | `INVENTARIO_CPM_ART41_45_CICLO08.csv` | F1 descritivo; amplia 96 posições CPM1–40 do ciclo 07, sem transcrição literal C0-T nem equivalência C0-J |
| Cotejo funcional CP 20–25 × CPM 35–45 por **20 cenários** | `MATRIZ_COMPARATIVA_ERRO_COACAO_NECESSIDADE_CICLO08.csv` | F2/F4 parcial, testes hipotéticos e categorias **Q**, sem escolhas de reforma |
| **6** referências judiciais com limitações de fonte | `JURISPRUDENCIA_CULPABILIDADE_CPM_CICLO08.csv` | ementas/resumos institucionais, súmula STM3, ficha STF ADPF779; não exame universal de inteiros teores |
| Estudo jurídico comparado de efeitos e melhor objeção, 6 novas fichas `Q` | `DOSSIE_08_ERRO_COACAO_NECESSIDADE.md` | PROB-T25-0027–0032; alternativas apenas futuras |
| Índice do módulo T25 atualizado e documento de coordenação | `README.md`; este `CONTINUIDADE_08.md` | registro de continuidade, sem decisão `C1`/`M`/revogação |

**Fontes primárias efetivamente examinadas, consulta 14/10/2026:**
1. Senado — CPM texto consolidado arts.35–46: https://legis.senado.leg.br/norma/524625/publicacao/34620431 ; Câmara — CPM norma atualizada: https://www2.camara.leg.br/legin/fed/declei/1960-1969/decreto-lei-1001-21-outubro-1969-376258-normaatualizada-pe.html .
2. Planalto — CP arts.20–25: https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848compilado.htm .
3. Planalto — Lei 14.688/2023, CPM art.38 §2º e veto de **parágrafo proposto** ao art.42, sem revogar o art.42 PU preexistente: https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14688.htm .
4. STM — Revista de Doutrina e Jurisprudência, [Apelação 7000232-60.2024.7.00.0000, publicação de 29/01/2026](https://revista.stm.jus.br/index.php/periodicos/article/view/jurisprudencia-05-v34-n1-2024), ficha/resumo, com **aparente tensão** entre a ementa `erro inescusável` e referência ao cabimento do art.35 para adequar resposta penal; exige leitura dos votos. 
5. STM — Súmula 3 (institucional): https://www.stm.jus.br/1-instancia/4-cjm-mg/212-stm/cat7-servicos/stm-servicos-judiciais ; Apelação 7000206-62.2024.7.00.0000, julgado 14/11/2024, ementa oficial de pesquisa https://jurisprudencia.stm.jus.br/consulta.php?fq_assunto_pesquisa__2=SUSPENS%C3%83O+CONDICIONAL+DA+PENA&fq_assunto_pesquisa__3=DIREITO+PENAL+MILITAR&fq_assunto_pesquisa__4=SUSPENS%C3%83O&fq_data_autuacao=d%282024%2F04%29&q=%2A&q_or=&rows=25&search_fil=&search_filter_option=jurisprudencia&start=0 .
6. STF — [ADPF 779, j.01/08/2023, DJe 06/10/2023, fonte oficial](https://portal.stf.jus.br/constituicao-supremo/artigo.asp?abrirArtigo=226&abrirBase=CF), **refere diretamente CP23/25, não julgou textualmente CPM45 PU**.

## 2. Achados prioritários, com seus limites

- **CPM art.35 versus CP21:** consequência e requisito distintos sobre erro escusável/inevitável; reserva especial quanto a dever militar. Levantar constitucionalidade e possibilidade de consciência de ilicitude, não presumir que haja precedente definitivo solucionando toda hipótese.
- **CPM arts.36–37 versus CP20:** excluir dolo e culpa não é mesmo mecanismo em cada texto; condições do erro exigem comparação por fato, incluído erro evitável sem modalidade culposa.
- **CPM38/40/41 versus CP22:** ordens manifestamente criminosas não protegem subordinado na nova redação 2023; coação exclusivamente física/material em violação de dever militar tem ressalva material; art41 possui cláusulas de redução facultativa com redação que precisa exegese própria.
- **CPM39 justificativa exculpante versus CPM42–43 justificante**, comparadas com CP24: alcance de pessoas protegidas, inferioridade do mal causado, natureza culpável/ilícita com efeitos para terceiros.
- **CPM42 PU** ainda aparece vigente na compilação de 2026 com excludente de comando em emergência e uso de meios violentos; **não** atribuir veto de texto legislativo novo em 2023 à revogação do parágrafo original.
- **CPM45 PU** não pune excesso escusável por surpresa/perturbação; **CPM46** ainda oferece hipótese de atenuação para excesso doloso, fora do inventário de 41–45; não produzir equivalência parcial enganosa.
- **STM Súmula3:** texto apenas afasta alegações pessoais/familiares **desacompanhadas de provas** para deserção/insubmissão. Não inferir vedação absoluta de exculpação, inversão automática do ônus geral da acusação nem força vinculante de decisão STF.

## 3. PENDENTE / NÃO VERIFICADO

- Cotejo autêntico histórico 1969→2023→2026 por cada artigo CPM35–46 e efeitos temporais; nenhuma prova C0-J ou C1 para o CLF.
- Íntegra e votos da Apelação STM 7000232-60.2024.7.00.0000, com aparente tensão entre ementa e conclusão na ficha 2026; divergência não resolvida.
- Jurisprudência aprofundada STF/STM/STJ sobre CPM35, CPM40, CPM42 PU, CPM45 PU; ausência de demonstração de precedente vinculante global.
- Comparação com CPM46–47, CP20–25 + normas extrapenais e efeitos civis, direito penal internacional e tratados de direitos humanos, garantias probatórias.
- Avaliação de constitucionalidade (culpabilidade, igualdade, proporcionalidade, vedação de tortura, presunção de inocência), incluindo aplicação a operações militares e dever legal de enfrentar perigo, sem decisões implícitas.
- DOU de 1984 da Lei 7.209/1984 localizado em ciclo anterior, mas fac-símile não inspecionado; anomalias textuais de CP3/4/12 permanecem.
- Modelo A/B/C: C continua **hipótese**; nenhuma minuta CLF, reforma M aprovada, cláusula transitória ou revogação proposta. DEC-016 não decidida. Interface Constituição alternativa **não importada**.
- Teste estrutural CI do HEAD deste commit: confirmar após gravação, sem equiparar QA a validação jurídica.

## 4. PRÓXIMO PASSO EXECUTÁVEL

**T25.M02 — Ciclo 09:** ampliar o recorte CPM **46–47** e a jurisprudência específica do **STM 7000232-60.2024.7.00.0000** (íntegra e votos majoritários/dissidentes), confrontando `erro inescusável` e art.35; identificar usos jurisprudenciais de CPM40 (coação moral), CPM42 PU (coação violenta em emergência) e CPM45 PU (excesso escusável). Testar **duas redações experimentais concorrentes**: (i) núcleo geral de culpabilidade/ilicitude com ressalvas militares objetivas; (ii) subparte penal militar autônoma mais restrita, identificando para cada frase **C0/C1/M/Q** sem presumir equivalência.

**Critério de aceite:** pelo menos 10 novos casos ou testes estruturados, fonte/autoria/data e contraditório jurídico; cada solução deve registrar consequência para sujeito comum e militar, impacto processual (T26), civil (T16), de execução (T27), constitucional (T02/CF), vigência temporal e ressalvas internacionais.

## 5. COORDENAÇÃO

**Interdependências:** T01.M01/M04; T02; T16 (efeitos civis), T23/T47/T48 (tratados), T25.M01/M02/M03/M06, T26 (procedimento e prova), T27 (execução), T45 (hierarquia/segurança e militar). **CF vigente:** direitos do art.5, legislação infraconstitucional e competências militares; projeto CF alternativo é cenário condicional separado.

**Categorias:** `C0-T` feito apenas para texto CP1–12 de compilação em ciclo03 (não CPM); `C0-J` não provado; `C1` e `M` não aprovadas; hipóteses atuais `Q`. **PR draft, main não alterada nesta frente.**

- [x] Branch, PR e `main` conferidos antes e durante a rodada.
- [x] 11 unidades de CPM41–45, 20 testes e 6 referências documentados.
- [x] Fontes e diferenças constitucionais versus normativas distinguidas.
- [x] FEITO, PENDENTE e PRÓXIMO gravados na mesma branch.
- [ ] Confirmar GitHub Actions do HEAD de continuidade e registrar resultado na PR.

**Protocolo:** `governanca/18_PROTOCOLO_CONTINUIDADE_POR_RODADA.md`.
