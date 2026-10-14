# T29.M01 — Pacote de continuidade / Rodada 05: F1-D

**Corte:** 14/10/2026; **responsável:** T29.M01 — Segurados e dependentes do RGPS.  
**Issue:** [#40](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/40) · **PR:** [#41 draft](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/41) · **branch:** `modulo/T29-M01-segurados-dependentes-f0-f1-20261014`.  
**Baseline `main` CLF verificada na abertura:** `16fba172c875c7a0de388288fe70005c944021d6`. A frente T24.M01 é de outro responsável (PR #38), nenhuma alteração externa ao T29.M01. **CF/1988 com EC103 vigente; CF futura em projeto independente não revalidada nesta rodada.**

## FEITO

| Entrega | Evidência | Valor de prova |
|---|---|---|
| 19 posições de cotejo por versão/núcleo (6 idade, 6 guarda, 4 mandato, 3 PSA) | [F1D_ESPELHO_NUCLEOS_19.csv](F1D_ESPELHO_NUCLEOS_19.csv) | 18 posições com texto/trecho do direito positivo ou regulamento e **1 ausência estrutural expressamente marcada**; identificação de fonte, data, tipo e Q, sem comparação automática/hashes |
| Relatório de cadeia histórica e 9 testes de perda de direitos | [RELATORIO_F1D_COTEJO_LITERAL_HISTORICO.md](RELATORIO_F1D_COTEJO_LITERAL_HISTORICO.md) | Análise de documentos originais de 1991, emendas 1997/2004/2021/2025, EC103 e Decreto3048; críticas C0/C1/M |
| Controle do histórico anterior (198 índices + 78 relações) | `F1A_MATRIZ_GRANULAR_8213_8212.csv`, `F1A_PARALELOS_8213_ART11_8212_ART12.csv`, F1B/F1C | Documentação preservada, sem segunda auditoria redundante |

**Fontes oficiais efetivamente consultadas, com recortes:**

- Câmara: publicações originais de **1991** Leis 8.212 **art.14/12** e 8.213 **art.13/11/16 §2**, e atualizada/Planalto compilado com as mesmas posições.
- Planalto: Lei 9.506/1997 **art.13 §§1–2**, Lei 10.887/2004 **arts.11/12** (alíneas j), Lei 9.528/1997 (nova redação art.16 §2), Lei15.108/2025 **arts.1/2** (DOU14/03/2025), Lei14.119/2021 **art.23** (PSA), Resolução Senado26/2005 **arts.1/2**, EC103/2019 **art.23 §§4/6/7**, Leis 8.212/8.213 compiladas.
- Câmara: Decreto3.048/1999 atualizado **art.11 caput e art.18 §2**, para confronto com leis de 14 anos.
- Receita Federal: identificação de IN RFB2110/2022 e cópia de texto art.9 §5 IX da **edição original** em reprodução secundária. **Versão oficial anotada 2026 não teve texto recuperado**, portanto a equivalência exata atual **não foi certificada**.
- STF Tema1271 (RE1442021) consultado: ficha oficial reconhece repercussão e exibe como última movimentação **16/04/2026** concluso ao relator após parecer PGR; **não identificado mérito definitivo** na consulta. Os demais precedentes constam dos relatórios F1-B/F1-C; não declarar releitura integral dos acórdãos nessa rodada.

**Achados confirmados:** `14 anos` nas duas leis desde 1991, sem identidade literal de toda estrutura contributiva; `16 anos` Decreto3048, distinto. Guarda judicial incluída 1991, excluída da letra 1997, incluída 2025, dependente de EC103 art23 §§4/6/7 e controvérsia Tema1271; `h` 1997 e `j` 2004 idênticas na redação, diferentes em eficácia e precedentes; ResSen26/2005 suspendeu só Lei8212 art12 I h. Lei14.119/2021 incluiu **apenas** 8212 art12 §9 VIII em PSA, sem correspondente inciso VIII na 8213 art11 §8. 

## PENDENTE / NÃO VERIFICADO

1. **F1-D é cotejo manual seletivo**, sem hashing de fontes oficiais e sem fac-símile DOU para todos marcos (datas `A_CONFERIR_DOU` no CSV). A palavra literal na matriz refere transcrição manual das versões; não é certificado por dois leitores, e ausência de inciso não é redação legislativa.
2. A IN RFB2110 possui alterações posteriores e fonte oficial inacessível por extração nessa consulta: precisa verificar edição **vigente em 14/10/2026** antes de usá-la como prova de regulação atual; alcance de benefício INSS ainda Q.
3. Tema1271 STF e compatibilidade da Lei15.108 com EC103; ADIs4878/5083 inteiro teor/modulação; RE351717/Tema691 efeitos temporalmente específicos.
4. Facultativo 14/16: julgado TRF3 5002988-56.2025.4.03.6322 e ADIs2110/2111 exigem controle de possível carência de maternidade disfarçada; estudo de outros precedentes ainda pendente.
5. **198 registros** F1-A são funcionais/descritivos, não 198 normas certificadas. Demais partes do RGPS não auditadas. Não aprovar C0/C1/M por identidade textual de termos e não presumir abrangência completa.
6. Conciliação dos destinos M01/M02/M05/M07 e implicações tributárias/constitucionais é objeto de governança; **nenhum módulo vizinho alterado**.
7. CI/checks último SHA, revisão material independente e autorização de merge ainda pendentes. PR draft, `main` intocada.

## PRÓXIMO — atividade prioritária única

**T29.M01/F1-E:** autenticar as cadeias temporais e enfrentar o significado jurídico de quatro fronteiras com evidências independentes: fac-símiles DOU/legislação 1997/2004/2021/2025; acórdãos STF ADIs4878/5083, RE351717, Tema691/Tema1271; repercussão da IN RFB2110 em texto oficial atualizado até 2026; jurisprudência e atos INSS sobre facultativo adolescente e PSA.

**Insumos:** fontes já localizadas no relatório F1-D, acórdãos integrais e publicações autênticas. **Entregável:** matriz de versão/efeito e parecer adversarial de preservação da filiação e dependência antes de propor a estrutura única do T29. **Critério de aceite:** cada controvérsia com fonte e competência temporal delimitadas; quando faltar fonte, Q e não "resolvido"; classes C0/C1/M apenas se demonstradas.

**Fila posterior:** completar a auditoria literal de todos os dispositivos realmente vigentes e seus modificadores; F2 modelo do RGPS e F3 pesquisa comparada.

## CONTROLE

**Proprietário único:** T29.M01; interfaces T29.M02/M03/M05/M06/M07, T12, T28, T32, T38, T01 e DEC016; Constituição atual vigente distinta do anteprojeto. **Nenhum texto CLF proposto, nenhuma revogação feita, nenhum M aprovado.**

- [x] Verifiquei `main`, PR41 e PRs abertos na abertura.
- [x] Confrontei publicações originais e atualização das leis para o recorte focal.
- [x] Separei texto legal, regulamento, precedentes, questão constitucional e lacunas documentais.
- [x] Registrei FEITO/PENDENTE/PRÓXIMO com critério de aceite.
- [ ] Auditoria independente e revisão do DOU fac-símile.
- [ ] Validação CI final/integração autorizada.
