# T25 — Continuidade 07: Código Penal Militar, arts. 1º–40

**Sessão/corte:** 14/10/2026, America/Sao_Paulo; M01/M02, interfaces M03/T26/T27. **Responsável funcional:** pesquisa penal T25. **Issue [#31](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/31)**; **PR [#32](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/32)** (rascunho); **branch** `modulo/T25-parte-geral-f0-f1`.

**SHAs e estado:** CLF `main` ao iniciar e na checagem anterior a este arquivo = `16fba172c875c7a0de388288fe70005c944021d6`; última referência HEAD do ciclo 06 `b2fa9e0e1b833426b02bdf9a9453838a73e2683e`; ao encerrar este arquivo conferir HEAD e CI do ciclo 07. Constituição alternativa `main` somente consultada por controle de versão = `b9dbdc540310ed5dc34fb1e5f314c46af343dc98`, **não** utilizada para afirmar direito vigente ou importar decisão.

## 1. FEITO — apenas na branch penal (não integrado à main)

| Entrega | Arquivo/situação | Origem/destino/C0–C1–M–Q |
|---|---|---|
| 40 artigos CPM 1–40, 96 posições descritivas com IDs não repetidos, fontes/recortes e alterações selecionadas de 2023 | `INVENTARIO_CPM_ART1_40_CICLO07.csv` | DL 1.001/1969 redação atualizada Câmara; **NÃO transcrição literal, C0-J pendente; todas propostas de destino Q** |
| Jurisprudência: 7 referências/precedentes selecionados STF/STM/STJ, incluindo STJ 2019 e 2026 | `JURISPRUDENCIA_CPM_ART1_40_CICLO07.csv` | fontes distinguem notícia institucional, enunciado, informativo e **pistas em PDF**, sem dizer que houve leitura do inteiro teor |
| Reconstituição de três blocos CPM e contraste com CP, 7 problemas Q e 14 testes | `DOSSIE_07_CPM_ART1_40_CRITICA_E_PRECEDENTES.md` | alternativas A/B/C em F4 exploratório; nenhum M nem C1 ratificado; nenhuma revogação |
| Atualização de índice, status e próximo subciclo | `README.md` e este pacote | rastreabilidade, não lei |

**Fontes oficiais consultadas, em 14/10/2026:**
- Câmara **CPM arts. 1–40 e notas de 2017/2023**, https://www2.camara.leg.br/legin/fed/declei/1960-1969/decreto-lei-1001-21-outubro-1969-376258-normaatualizada-pe.html ; Planalto **Lei 14.688/2023**, https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14688.htm .
- Câmara **CP comum arts. 1–31**, https://www2.camara.leg.br/legin/fed/declei/1940-1949/decreto-lei-2848-7-dezembro-1940-412868-normaatualizada-pe.html .
- STF, notícia oficial **HC 88.261** (08/05/2007), https://noticias.stf.jus.br/postsnoticias/stm-tera-de-recalcular-pena-aplicada-a-condenado-por-latrocinio/ — **não inteiro teor**.
- STJ **CC 161.898/MG** (13/02/2019), Informativo 642, https://scon.stj.jus.br/jurisprudencia/externo/informativo/?acao=pesquisarumaedicao&from=feed&livre=0642.cod. ; **CC 140.852/GO**, 27/11/2019, ementa; **CC 218.865/DF**, 08/04/2026, e **AREsp 3.046.912/RS**, 07/04/2026, Informativos 884 e 886 (pesquisa) https://processo.stj.jus.br/jurisprudencia/externo/informativo/?acao=pesquisar&b=INFJ&livre=%22crime+militar%22&operador=e&thesaurus=JURIDICO .
- STM: pesquisa institucional sobre art.30 PU (ementa de 2021) e **publicação de 2009 em PDF localizada mas não visualmente analisada**; detalhes e limitações na matriz jurisprudencial. Nenhum julgamento foi classificado como vinculante por falta de fundamento e exame completos.

## 2. PENDENTE / NÃO VERIFICADO

- Histórico literal **CPM de 1969 e modificadoras até 2026**, com status de cada subunidade. Os 96 registros são **índice descritivo** e não prova de identidade histórica. CPM art.21 revogado, art.9 II.f revogado e §3º vetado identificados como **não normas em vigor**, sem transposição.
- Conclusões de efeitos penais da tentativa militar (CPM 30 PU), da retroatividade de medidas de segurança (CPM 3), do erro escusável (CPM 35), da ordem de superior (CPM 38 §2) e da coação moral (CPM 40), sob CF/1988, especialmente culpabilidade, proporcionalidade, individualização, legalidade e devido processo. Nenhuma conclusão de constitucionalidade global.
- Necessidade de estudar **CPM arts.41–45** e interfaces posteriores para o estado de necessidade; sem isso, comparação de CPM 39/40 com CP 22–24 é incompleta.
- Consultar inteiros teores de STF HC 88.261, STJ CC 218.865 e precedentes STM relevantes, inclusive opiniões divergentes; pesquisa amostral não autoriza consenso ou efeito vinculante.
- Efeitos intertemporais específicos da Lei 13.491/2017, Lei 14.688/2023, divisão Tribunal do Júri/Justiça Militar (2026), limites do conceito de crime militar; competência `T26` não resolvida.
- **Lei 7.209/1984**: fac-símile da publicação original do DOU 13/07/1984 ainda não inspecionado; diferenças aparentes em CP 3/4/12 permanecem Q.
- **DEC-016**, veículo legislativo e eventual constituição alternativa: nenhuma deliberação ratificada. Nenhuma minuta/reestruturação efetiva no corpus CLF e nenhuma cláusula de revogação.
- CI estrutural no HEAD do presente ciclo: verificar depois de salvar; aprovação de teste estrutural não comprova validade jurídica.

## 3. PRÓXIMO PASSO EXECUTÁVEL

**Prioritário:** T25.M02/T25.M01, **ampliar inventário CPM arts.41–45** (atenuantes e justificantes) e reconstruir confrontação dos efeitos **CPM arts.35–45 × CP arts.20–25**, com quatro eixos: erro de proibição e de tipo, coação/ordem superior, necessidade exculpante vs justificante, exigibilidade de conduta diversa. **Insumos:** texto Câmara CPM/CP; Lei 14.688/2023; STF/STJ/STM com íntegra dos julgados relevantes e versão temporal.

**Entregável/aceite:** matriz `dispositivo origem × hipótese fática × solução CPM × solução CP × fonte e época × diferença material × categoria Q ou M proposta`, com 10–15 testes adversariais, melhor argumento contrário, e indicação clara de limite constitucional. **Não escolher modelo C ou redigir normas como aprovadas** antes da comparação.

**Fila:** investigar pena de tentativa militar com dados de uso e precedentes STM, relação da lei penal especial com competência e CPPM, exame de texto DOU da Lei 7.209/1984.

## 4. COORDENAÇÃO E CONTROLE

**Módulos:** T01.M01/M04 (vigência e método), T02 e CF/1988 (direitos, art.5º XXXIX/XL/XLVI), T25.M01–M03/M06, T26 (processo, júri, competência e prova), T27 (medidas de segurança, execução), T05, T23/T47/T48 (tratados/extraterritorialidade), T45 (instituições militares/policiais). A CF proposta permanece fonte de cenário futuro, sem alteração nesta branch. **A/B/C:** hipóteses Q, o modelo C é apenas candidato condicional. **Classificação:** C0-T não realizado para CPM; C0-J não provado; C1 não aprovado; M não aprovado.

- [x] Consultadas branch, `main`, PR e versão CF.
- [x] 40 artigos e 96 unidades descritivas verificadas por IDs únicos (não declaração de cobertura histórica exaustiva).
- [x] Fontes e limites de precedentes descritos, inclusive PDFs não examinados.
- [x] FEITO / PENDENTE / PRÓXIMO documentados.
- [ ] Conferir CI do HEAD depois deste arquivo e registrar resultado na PR.

**Protocolo:** `governanca/18_PROTOCOLO_CONTINUIDADE_POR_RODADA.md`.
