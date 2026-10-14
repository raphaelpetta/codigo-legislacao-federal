# T29.M01 — Continuidade rodada 08: F2-A modelo vigente (14/10/2026)

**Proprietário:** T29.M01 — Segurados e dependentes RGPS. **Issue** [#40](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/40); **PR draft** [#41](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/41); **branch** `modulo/T29-M01-segurados-dependentes-f0-f1-20261014`.  
**Base main observada no início:** `16fba172c875c7a0de388288fe70005c944021d6`. CF/1988 e EC103/2019 são direito positivo; Constituição futura é projeto separado e não foi importada. **T24.M01 pertence a outra frente PR38**, sem alterações; demais T29.M02/M05 são interfaces, não foram alterados.

## FEITO

| Entrega | Arquivo | Teste comprovado |
|---|---|---|
| Modelo de direito vigente **33 regras** com pressuposto, efeito, lei/precedente, dono e Q | [F2A_MATRIZ_MODELO_VIGENTE.csv](F2A_MATRIZ_MODELO_VIGENTE.csv) | 33 IDs únicos, 10 colunas, não faltam campos |
| **20 hipóteses respondidas** com fundamento e limites (não decisões judiciais de casos reais) | [F2A_TESTES_20_CASOS.csv](F2A_TESTES_20_CASOS.csv) | 20 IDs únicos, 8 colunas, **27 IDs de regra válidos referenciados**, zero referência quebrada |
| Relatório de reconstrução de ingresso, manutenção, especial e dependentes + fluxograma textual | [RELATORIO_F2A_MODELO_VIGENTE_E_20_TESTES.md](RELATORIO_F2A_MODELO_VIGENTE_E_20_TESTES.md) | Diferencia legislação, regra infralegal, precedente, Q e cenário hipotético |
| Registro no README de rodada 08 e estratégia F2-B | [README.md](README.md) | Continuidade e proibição de fusão editorial sem prova |

**Distribuição das regras:** ING ingresso 10, INS inscrição 4, QUA manutenção 9, ESP especial 3, DEP dependência 6, TIME corte temporal 1 (total **33**). **Testes respondidos:** ingresso 4, qualidade 5, especial 2, dependência 7, inscrição 2 (total **20**). Cobertura: 27 das 33 regras exercitadas, 6 não atingidas explicitamente por esses testes — não alegar cobertura completa de exceções.

**Fontes lidas nesta rodada, recortes:**
- [Lei8.213/1991 compilada — arts. 10–17, 27, 102](https://www.planalto.gov.br/ccivil_03/leis/l8213cons.htm); [Lei8.212/1991 compilada — arts. 12–14 e art.30 I](https://www.planalto.gov.br/ccivil_03/leis/l8212compilado.htm).
- [Decreto3.048/1999 atualizado — arts. 9–13,18,20,22](https://www2.camara.leg.br/legin/fed/decret/1999/decreto-3048-6-maio-1999-368532-normaatualizada-pe.html): filiação obrigatória automática pela atividade e facultativo por inscrição/primeira contribuição; inscrição de dependentes no requerimento; prazo de graça.
- [STJ **Tema1360**, notícia institucional publicada em **16/07/2026**](https://www.stj.jus.br/sites/portalp/Paginas/Comunicacao/Noticias/2026/16072026-Repetitivo-fixa-tese-sobre-prova-de-desemprego-para-extensao-do-periodo-de-graca-previdenciaria.aspx): para art15§2 da Lei8213, desemprego involuntário provado por meios idôneos além do registro no Ministério do Trabalho; **ausência isolada de anotações na CTPS/CNIS não é suficiente**. A nota institucional relata tese repetitiva, não inteiro teor.
- [STJ **Súmula416**, texto oficial](https://scon.stj.jus.br/SCON/sumstj/toc.jsp?sumula=416.num.): exceção pensão após perda da qualidade quando aposentadoria já tinha requisitos cumpridos em vida (Lei8213 art102§2).
- STF/STJ já documentados nas rodadas anteriores: Tema732 (guarda antes EC103), ADIs4878/5083, Tema1271 (mérito não localizado na consulta anterior), Tema691 (mandato), ADIs2110/2111 (carência salário-maternidade); não alegar verificação integral nova nesta rodada. Lei15108/2025 inclusão de guarda e Lei14119/2021 PSA mantidos como fonte positiva.

**Resultados sistêmicos novos:** filiação obrigatória pelo trabalho **não é igual a inscrição ou recolhimento**; facultativa requer ato volitivo e primeiro pagamento, idade 14 (lei) vs 16 (decreto) é Q; período de graça soma hipóteses e tem **prova não exclusivamente administrativa** conforme Tema1360; perder qualidade não extingue automaticamente pensão se aposentadoria já aperfeiçoada (Súmula416); art16 classe e dependência econômica, guarda e prova possuem requisitos diversos e transições.

## PENDENTE

1. **F2-A é primeiro modelo e não F2 integral**: regra especial, idas/voltas de filiação, qualidade de segurado na recuperação, exceções prestacionais por benefício, os 6 IDs ainda não exercitados, conflitos legislativos de 1996/2019/2025, regime histórico inteiro da Lei8213 ainda a revisar em F1 residual.
2. **STF Tema1271** guarda e EC103 art23§6: consultar de novo antes de texto CLF e não presumir decisão; **STJ Tema732/ADIs4878/5083** não equivalem automaticamente a julgamento da EC.
3. **Idade facultativo 14/16** e argumentos do TRF3 em situação de salário-maternidade após ADIs2110/2111: não transformar carência já invalidada em presunção de fraude apenas por uma contribuição.
4. **PSA:** art12§9 VIII da Lei8212 sem espelho literal Lei8213 art11§8 e versão 2026 da IN RFB2110 art9§5 IX ainda não certificada; aplicação prestacional não definitivamente resolvida.
5. **O art15§4 exige calendário de vencimentos de custeio para cálculo de data precisa da perda**: modelo não inventa datas nem aplica 36 meses como prazo automático sem mais de 120 contribuições/desemprego idôneo.
6. **STJ Tema1360 fonte consultada é nota institucional, não inteiro teor de acórdão**; conferir acórdãos REsp2169736 e REsp2188714, eventual modulação, antes da conversão legislativa.
7. **Lei15371/2026 publicada, vigência futura 01/01/2027**: não tratar novo salário-paternidade como benefício vigente em out/2026.
8. **CI do último SHA, revisão material independente e integração central** pendentes; nenhum dispositivo C0/C1/M ou veículo DEC016 aprovado. PR continua **draft**, main não alterada.

## PRÓXIMO — F2-B independente do histórico de MPs

**F2-B:** modelo de sucessão temporal do vínculo/qualidade e reconhecimento do direito no evento, com ênfase em art15 §§1–4, Decreto3048 art13, Lei8213 art102, art16 §5, e efeitos da perda/recuperação no enquadramento/qualidade. Incluir casos de múltiplos vínculos e dependência com óbito em distintos marcos. **Critério:** testar as 6 regras ainda não exercitadas onde pertinentes e apontar toda exceção de direito adquirido, não regressão e limites de competência dos módulos T29.M02/M05, sem inventar requisito de carência ou filiação.

**Fila após F2:** F3 pesquisa crítica comparada, F4 alternativas com riscos, F5 só com decisão aprovada; completar F1 literal restante quando necessário por subunidade jurídica relevante.

## CONTROLE
- [x] Conferido PR41, base main e pacote rodada07 antes de escrever.
- [x] Consultadas fontes atuais de 2026 e precedentes específicos para F2-A.
- [x] 33 registros e 20 testes validados em conteúdo recuperado do GitHub: **sem duplicatas, faltas, referência inexistente ou dimensão divergente**.
- [x] Fontes de custeio, prestação, RPPS e outras frentes apenas referidas.
- [ ] CI do HEAD final e revisão jurídico-material independente.
- [ ] Autorização de integração ou reforma M.
