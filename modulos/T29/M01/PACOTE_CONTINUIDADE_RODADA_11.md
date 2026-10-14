# T29.M01 — Pacote de continuidade, rodada 11 / F3-A (14/10/2026)

**Responsável desta frente:** T29.M01, pesquisa comparada institucional · **Issue:** [#40](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/40) · **PR:** [#41 draft](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/41).  
**Branch:** `modulo/T29-M01-segurados-dependentes-f0-f1-20261014`. **Base do `main` CLF verificada na abertura:** `16fba172c875c7a0de388288fe70005c944021d6`. **CF/1988 e EC103** como direito positivo; Constituição futura em projeto separado, **não examinada nesta rodada**. F3-A independe da F2-D adversarial pendente de outra frente; **não reproduzir os 47 casos, a concordância ou as matrizes F2-C**. T29.M02/M05/M06/M07 e T24.M01 não foram editados.

## FEITO — entregas e provas

- [F3A_MATRIZ_COMPARADA_17_MECANISMOS.csv](F3A_MATRIZ_COMPARADA_17_MECANISMOS.csv) — **17 recortes institucionais e normativos** de Alemanha (5), Espanha (3), Portugal (4), Uruguai (3) e OIT/benchmark global (2). Cada entrada com URL, mecanismo, grau de leitura e risco de transplante; **não afirmar auditoria integral das leis estrangeiras**.
- [RELATORIO_F3A_DIREITO_COMPARADO_E_OPCOES_PRELIMINARES.md](RELATORIO_F3A_DIREITO_COMPARADO_E_OPCOES_PRELIMINARES.md) — exame de equivalência funcional, restrições jurídicas e fiscais, três arquiteturas **candidatas** A/B/C, fontes oficiais, limites de inferência empírica.
- [F3A_TESTE_TRES_ARQUITETURAS_30_RISCOS.csv](F3A_TESTE_TRES_ARQUITETURAS_30_RISCOS.csv) — **3 arquiteturas × 10 riscos brasileiros = 30 confrontos qualitativos**, sem pontuar resultados, ratificar C0/C1/M ou alegar efeito causal.
- [F3A_AGENDA_EVIDENCIA_BRASIL_10_INDICADORES.csv](F3A_AGENDA_EVIDENCIA_BRASIL_10_INDICADORES.csv) — fontes oficiais candidatas para 10 indicadores sobre CNIS, prova, fila, indeferimentos, tempo, judicialização, impacto distributivo e custeio; **dados não extraídos** e lacunas explicitamente declaradas.
- README atualizado com FEITO/PENDENTE/PRÓXIMO e interface de F2-D/F4.

### Fontes lidas nesta rodada, com recortes

**Alemanha:**
[SGB IV §28a — cadastro empregador](https://www.gesetze-im-internet.de/sgb_4/__28a.html), [§28e — pagamento global contribuição](https://www.gesetze-im-internet.de/sgb_4/__28e.html), [SGB VI §56 — criação filhos](https://www.gesetze-im-internet.de/sgb_6/__56.html), [§58 — períodos reconhecidos](https://www.gesetze-im-internet.de/sgb_6/__58.html), [índice do SGB VI §§46–48](https://www.gesetze-im-internet.de/sgb_6/) — normas de períodos têm efeito específico à aposentadoria, não são idênticas a qualidade de segurado brasileira.

**Espanha:** [LGSS RDL 8/2015, arts.144 e 166, versão do BOE 31/07/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724&p=20260731&tn=0) — dever de contribuição ao começar trabalho; situações asimiladas a alta por desemprego/prestação e convênios sob condições; [glossário institucional convênio especial](https://www.seg-social.es/wps/portal/wss/internet/Glosario/11976) — contribuição por escolha em âmbito material delimitado.

**Portugal:** [Lei4/2007, arts.23, 98–100](https://diariodarepublica.pt/dr/detalhe/lei/4-2007-522781) — sistemas contributivo/não contributivo distintos, dados nacionais e preservação de direitos adquiridos/em formação; [Lei110/2009, arts.24–29, 132–133](https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575) — trabalhadores obrigatórios/independentes, exclusão por atividade, registro de empregador.

**Uruguai:** [BPS história laboral nominada](https://www.bps.gub.uy/11438/), [reconhecimento de atividade ausente](https://www.bps.gub.uy/11452/reconocimiento-de-servicios.html), [reconstrução documental](https://www.bps.gub.uy/15430/reconstruccion-de-la-historia-laboral.html), [cronograma de reconhecimento 2026](https://www.bps.gub.uy/20542/registro-de-anos-trabajados.html). **Não importar ao Brasil cronograma especial de 1996 nem restringir prova por inferência.**

**OIT:** [Recomendação202/2012](https://www.ilo.org/resource/ilo-social-protection-floors-recommendation-2012-no-202) e [Relatório Mundial 2024–26](https://www.ilo.org/resource/article/world-social-protection-report-2024-26-figures): piso de proteção distinto de seguro contributivo; dado de cobertura global **52,4% ao menos uma prestação**, meramente descritivo, **não prova de causalidade ou de eficácia da codificação**.

**Brasil, insumos F3-B identificados sem análise estatística:** [BEPS 2026 até agosto na data consultada](https://www.gov.br/previdencia/pt-br/assuntos/previdencia-social/Dados-estatisticos-previdencia-social-e-inss/boletins-da-previdencia-social/2026), [Painéis RGPS](https://www.gov.br/previdencia/pt-br/assuntos/previdencia-social/paineis-estatisticos), [Transparência INSS](https://www.gov.br/inss/pt-br/portal-de-transparencia) e resumo do TCU acerca de uso do CNIS em concessões, a conferir pelo acórdão completo.

## Achados e alternativas **não aprovadas**

- **Arquitetura A:** conceitos gerais compartilhados de filiação/qualidade/dependência, especialidade funcional de M02 custeio, M03–M05 benefícios, M06 processo, M07 RPPS. Candidata de boa inteligibilidade, mas exige concordância literal e acordo de proprietários; não é ainda C1.
- **Arquitetura B:** preservar regimes/códigos em blocos separados com capítulo explícito de correspondências. Menos rupturas formais, porém possível manutenção de duplicações e reformas futuras divergentes.
- **Arquitetura C:** unificação integral de filiação/custeio/benefícios. **Maior risco qualitativo**, especialmente PSA, CI, carência materna, guarda, multi-vínculos e direitos transitórios. Não defender como operação meramente editorial, requer **M** caso escolhida.
- **Trava externa:** colisão do art.73-A entre Leis15.415/2026 (materno, vigente) e15.371/2026 (paterno, eficaz em 2027) deve ficar na interface M05/M06/T01, não solucionada unilateralmente por M01.

## PENDENTE

1. **F3-A é estudo comparado seletivo**: sem levantamento integral de jurisprudência estrangeira, sem metanálise e sem dados nacionais com efeito causal; somente fontes e efeitos enumerados verificados.
2. **F3-B recomendada:** coleta/análise de dados de execução no RGPS e prova, CNIS, reclamações, indeferimentos e custos. Os **10 indicadores estão apenas catalogados**, nenhum percentual foi fabricado.
3. **F2-D paralela** deve harmonizar as diferenças dos 47 testes e 14 casos sob reserva conservadora (conforme README atual), sem repetir estudo comparado.
4. **Antes de F4/F5:** consultar titular de M02/M05/M06/T01 para custos e espécie, DEC-016; art.73-A com efeitos futuros, STF Tema1271, idade 14/16, PSA, carência materna, contribuição pós óbito; revisar fontes oficiais atualizadas e CF-projeto se reforma constitucional for cogitada.
5. F1 global ainda parcial, F2 conceitual preliminar, F3 comparado sem estimativas empíricas; nenhuma decisão C0/C1/M, nenhuma minuta F5, **PR #41 draft, `main` e demais módulos intocados**.
6. Verificar integridade do último SHA do PR após escrita e os status de CI; não inventar checks.

## PRÓXIMO — prioridade recomendada

**T29.M01 / F3-B — diagnóstico brasileiro de implementação do vínculo previdenciário.** Ler BEPS 2026, fontes CNIS/TCU e dados de processo com segmentação de motivos; estudar se documentação excessiva, erros cadastrais e repartição de competências explicam custo/litigiosidade. Não inferir causalidade de comparação entre países. Produzir matriz de indicadores e análise de opções A×B×C com hipóteses testáveis; preservar todos os **51 cenários distintos** e a reserva F2-D.

**Critério de aceite:** variáveis explicitadas, fontes com versão/competência, denominadores, desagregações disponíveis, limites dos dados e implicações de cada política; sem narrativa de eficiência não medida. Se os dados forem insuficientes, F4 poderá ser apenas opção com grande Q_EMPIRICA, nunca promessa de economia.
