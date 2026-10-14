# T29.M01 — Pacote de continuidade, rodada 06 / F1-E (14/10/2026)

**Responsável:** T29.M01 — Segurados e dependentes RGPS · **Issue:** [#40](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/40) · **PR:** [#41 draft](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/41).  
**Branch:** `modulo/T29-M01-segurados-dependentes-f0-f1-20261014`; **CLF main observada na abertura:** `16fba172c875c7a0de388288fe70005c944021d6`.  
**Reserva:** direito positivo = CF/1988 + EC103/2019; projeto constitucional separado e **não reavaliado** nesta rodada; T24.M01/PR38 é de outro proprietário, sem edição de seus arquivos. **DEC016** sobre promulgação do Código único continua pendente.

## FEITO — documentos e correções verificáveis

| Entrega | Evidência | Natureza |
|---|---|---|
| Retificação documental da data da retirada de menor sob guarda: começa em **MP1.523/1996, DOU 14/10/1996**, não somente Lei9.528/1997 | [MP original lida integralmente](https://www2.camara.leg.br/legin/fed/medpro/1996/medidaprovisoria-1523-11-outubro-1996-359451-publicacaooriginal-1-pe.html), **art.2º** (Lei8213 art16§2), **art.5º** (vigência) | Fonte oficial primária; reedições ainda Q |
| Acréscimo de precedente qualificado fundamental: **STJ Tema732, REsp 1.411.258/RS**, julgado 11/10/2017, DJe21/02/2018, trânsito09/03/2023 | [STJ banco de repetitivos](https://processo.stj.jus.br/repetitivos/temas_repetitivos/pesquisa.jsp?cod_tema_final=732&cod_tema_inicial=732&novaConsulta=true&tipo_pesquisa=T) | Tese protetiva pré-EC103; não decide especificamente validade EC103§6 |
| Atualização dos intervalos C10/C11 do cadastro anterior de 18 cenários | [F1C_CASOS_TEMPORAIS_18.csv](F1C_CASOS_TEMPORAIS_18.csv) | Correção conservando IDs; hipótese depende de fatos e reedições |
| Matriz seletiva de **19 marcos e fontes** em 4 eixos, com situação positiva e pendências | [F1E_CADEIAS_FONTE_19_EVENTOS.csv](F1E_CADEIAS_FONTE_19_EVENTOS.csv) | Rastreabilidade, não 19 normas novas |
| Relatório corretivo sobre período de guarda, IN RFB e fontes 1997/2004 | [RELATORIO_F1E_RETIFICACAO_MP1996_TEMA732_E_FONTES.md](RELATORIO_F1E_RETIFICACAO_MP1996_TEMA732_E_FONTES.md) | Análise histórico-jurídica, sem C0/C1/M |

**Outras fontes públicas efetivamente examinadas:**
- [Câmara — ficha MP1.523/1996](https://www2.camara.leg.br/legin/fed/medpro/1996/medidaprovisoria-1523-11-outubro-1996-359451-norma-pe.html): histórico de reedição/perda de eficácia, conversão Lei9528;
- [Senado — Lei9506/1997, DOU31/10/1997](https://legis.senado.leg.br/norma/551382); [LexML Lei10887/2004, DOU21/06/2004](https://www.lexml.gov.br/urn/urn%3Alex%3Abr%3Afederal%3Alei%3A2004-06-18%3B10887); [Senado Res26/2005, DOU22/06/2005](https://planalto.gov.br/ccivil_03/_ato2004-2006/2005/congresso/ressf26-05.htm);
- [RFB IN2110/2022](https://normas.receita.fazenda.gov.br/sijut2consulta/consulta/link.action?idAto=126687&visao=original), publicação DOU19/10/2022, texto indexado art9§5 IX e histórico de IN2185/2024,2289/2025,2321/2026; **versão consolidada atual do inciso ainda não comprovada por auditoria de cada ato alterador**;
- [STF Tema1271](https://portal.stf.jus.br/jurisprudenciaRepercussao/verAndamentoProcesso.asp?classeProcesso=RE&incidente=6661561&numeroProcesso=1442021&numeroTema=1271): última movimentação exibida 16/04/2026, repercussão geral sem mérito novo identificado; [STF ADIs4878/5083 ementa](https://portal.stf.jus.br/jurisprudenciaRepercussao/verPronunciamento.asp?pronunciamento=10615600), DJe06/08/2021.

**Controle:** na rodada as diferenças entre texto oficial, tese STJ, tese STF, proposta CLF, regulamento, direito temporal e Q foram mantidas; não foi produzida norma final nem deliberação de M. Os dados atuais permanecem **F1 parcial**, não F1 de todo T29. Os testes específicos de integridade serão declarados somente depois da conferência do último SHA.

## PENDENTE / NÃO VERIFICADO

1. **Cadeia de reedições MP 1523/1996 até Lei9528/1997**, inclusive textos, cláusulas de convalidação, lapsos de eficácia/temporalidade; não afirmar continuidade ininterrupta sem prova.
2. **Tema1271 STF**, mérito e efeitos EC103§6, §4 e §7; ADIs4878/5083 não equivalem a julgamento do mérito da emenda; lei de 2025 não anula EC por si só.
3. **IN RFB2110 art9§5 IX versão 2026**: RFB disponibiliza texto original e atos alteradores, mas confronto por inciso específico ainda não concluído. PSA não autoriza perda automática de qualidade prestacional nem isenção tributária geral.
4. **Segurado facultativo 14/16**: lei, decreto, TRF3 caso único e ADIs2110/2111; distinção entre filiação, prova de fraude, carência e salário-maternidade ainda exige revisão.
5. **H/j do mandato**, controles de competência tributária, não retroatividade e benefícios; Tema691/STF resolve validade contributiva pós2004 em seu recorte, não todo histórico.
6. Os **198 registros de F1-A** permanecem inventário funcional, não certificação de 198 textos vigentes. F2–F9 e CF alternativa não redigidos nem aprovados.
7. **CI/checks último commit, revisão independente, governança central e merge** pendentes. PR draft.

## PRÓXIMO — atividade prioritária única

**T29.M01/F1-F:** confrontar cada **reedição e conversão da MP1523/1996 até 1997** com exemplar original e DOU, mapear texto do art16§2, vigência e convalidações, diferenciando intervalo de eficácia dos efeitos protetivos Tema732/ADIs. **Entregável:** linha temporal certificada por ato + testes de casos de óbito perto das transições. **Critério:** nenhum subperíodo definido só pela data da Lei9528 e nenhum período desprotegido por apagamento do Tema732; divergência sem prova preservada Q.

**Fila:** auditoria estrita das IN RFB2185/2289/2321 quanto a art9§5 IX; acompanhamento Tema1271 e interpretação judicial, início F2 modelo vigente apenas após F1 de núcleos protetivos suficientemente consolidado.

**Proprietário e interfaces:** T29.M01; T29.M02 custeio, M05 pensão, M06 processo, T12 fiscal, T32 criança; sem editar módulos alheios. **Não há promulgação, revogação ou C0/C1/M aprovado.**
