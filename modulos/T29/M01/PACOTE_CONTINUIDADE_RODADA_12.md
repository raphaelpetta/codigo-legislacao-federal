# T29.M01 — Pacote de continuidade da rodada 12 (F3-B)

**Data/corte:** 14/10/2026. **Responsabilidade:** T29.M01 — pesquisa brasileira de implementação, sem invadir M02, M05, M06, T01 ou T24. **Issue:** [#40](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/40) · **PR draft:** [#41](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/41) · **branch:** `modulo/T29-M01-segurados-dependentes-f0-f1-20261014`. **Baseline `main` ao abrir a frente:** `16fba172c875c7a0de388288fe70005c944021d6`. Texto de CF alternativa **não** pesquisado; CF/1988/EC103 é parâmetro positivo.

## FEITO

1. [**F3B_BASE_INDICADORES_E_LIMITES_27.csv**](F3B_BASE_INDICADORES_E_LIMITES_27.csv): 27 observações quantitativas, achados de auditoria e lacunas, com **período, unidade, universo, classe de prova, fonte URL e cautela explícita**. Auditoria estrutural: 27 linhas, 14 campos, 27 identificadores lógicos únicos, nenhuma omissão, três identidades numéricas confirmadas. **Não são 27 indicadores nacionais mensurados**; incluem dados antigos, achados qualitativos, metas e Q_EMPIRICA.
2. [**RELATORIO_F3B_EVIDENCIAS_INSS_CNIS_TCU_CNJ_2026.md**](RELATORIO_F3B_EVIDENCIAS_INSS_CNIS_TCU_CNJ_2026.md): quadros BEPS, controle visual das tabelas originais, decisões TCU identificadas e achados CNJ, interpretação de erros cadastrais e custo/benefício, dez hipóteses de avaliação, confronto A/B/C da F3-A.

**Fonte estatística principal**: [BEPS agosto/2026 (edição em 30/09/2026)](https://www.gov.br/previdencia/pt-br/assuntos/previdencia-social/Dados-estatisticos-previdencia-social-e-inss/boletins-da-previdencia-social/2026/beps082026_final.pdf), conferidos **quadro 1 página impressa 01, quadro 24 p.24, quadro 25 p.25, conceitos ao fim do PDF**:
- **844.389 concessões** em agosto, sendo **716.161 previdenciárias**, **127.938 assistenciais** e **290 BLE**;
- **882.589 indeferimentos** no mês, dos quais **615.211** de espécies sujeitas a perícia. **Não é taxa de indeferimento de coorte, nem prova de que todas negativas sejam causadas por perícia**;
- **1.251.813 pendências**, sendo **873.976** aguardando INSS/perícia inicial e **377.837** exigência documental do segurado; **384.467** com mais de 45 dias segundo quadro;
- **33 dias** tempo médio de concessão agosto contra **40** julho, mas a definição oficial conta **DER ou DRD (após exigência)** até DDB e **não inclui o estoque sem despacho**. Não confundir tempo líquido/tempo total.
- **Três somas conferidas**: 716.161 + 127.938 + 290 = 844.389; 873.976 + 377.837 = 1.251.813; 384.467 + 867.346 = 1.251.813.

**Fontes auditoria e governança**:
- [TCU Acórdão 2.002/2024 (notícia 30/09/2024)](https://portal.tcu.gov.br/imprensa/noticias/auditoria-avalia-controles-internos-do-inss-para-concessao-de-aposentadoria): 70% dos casos **do recorte auditado** desconsideraram pendências CNIS; 31% tarefas não concluídas automaticamente no período da auditoria. **Não extrapolar para todos benefícios/2026**, nem equiparar falta de automatização a erro.
- [TCU Acórdão 2.591/2024 (notícia 10/12/2024)](https://portal.tcu.gov.br/imprensa/noticias/fiscalizacao-avalia-uso-do-cadastro-nacional-de-informacoes-sociais-na-concessao-de-beneficios-previdenciarios): falhas concretas de integridade CNIS/compatibilidade de registros e sistemas; **sem percentual nacional mensurado**.
- [TCU Acórdão 1.498/2026 (notícia 11/06/2026)](https://portal.tcu.gov.br/imprensa/noticias/tcu-fiscaliza-sistema-de-concessao-automatica-de-beneficios-do-inss): meta de 50% automatização (**não taxa observada**); recomendação/determinação de permitir correção de dados e conceder valor incontroverso sem impedir melhora posterior; **implantação não demonstrada**.
- [CNJ/Insper 2020](https://www.cnj.jus.br/acoes-previdenciarias-pesquisa-registra-causas-da-revisao-judicial-de-decisoes-administrativas/): 9.253.045 processos administrativos e 593.772 concessões judiciais no estudo **2018–2019**; **não são dados atuais**.
- [CNJ PrevJud 26/08/2026](https://www.cnj.jus.br/inss-prevjud-acelera-resposta-judicial-e-concessao-de-beneficios/): aproximadamente 2 milhões de ordens encaminhadas desde 2024, 88,32% respondidas; **ordens não são causas únicas nem deferimentos materiais**.

## PENDENTE

- **Não lidos os inteiros teores dos três acórdãos TCU**, apenas notícias institucionais e recorte identificador, que não fornecem íntegra de métodos, denominadores ou implementação.
- Não há série pública recuperada nesta rodada sobre **retificação CNIS** (solicitações, procedência, mediana de conclusão), motivos de indeferimento por prova/filiação/carência, controle longitudinal de coortes de DER ou custos atribuíveis ao CLF. **Não imputar zero às lacunas**, não inventar porcentagens de economia ou redução de judicialização.
- Não comparar diretamente os **1.251.813** do quadro 25 BEPS/ago com **1,8 milhão** anunciado pelo INSS em junho antes de equalizar universo/extração/critério; não confundir **DRD→DDB** com DER→decisão definitiva.
- Menção no TCU/2024 a carência de salário-maternidade não altera o resultado vinculante das **STF ADIs 2.110/2.111**; versões temporais administrativas precisam ser auditadas.
- **F2-D** de conciliação dos 47 casos e 14 reservas segue linha separada da F3-B; **51 casos distintos** permanecem conjunto de teste F2. F1 ainda parcial, F4/F5 não iniciados.
- Interfaces M02 custeio, M05 prestações, M06 processo, T01 temporalidade e governança (DEC016) **não consultados para alterações**; **nenhuma redação M/C0/C1 aprovada**.
- CI/checks do HEAD final e revisão externa pendentes até verificação.

## PRÓXIMO — F3-C antes de decidir reforma

**T29.M01/F3-C:** localizar íntegra dos acórdãos TCU 2.002/2024, 2.591/2024, 1.498/2026, checar decisões e execução de planos de ação; buscar bases de retificação CNIS, razões de negativa, reversão administrativa e dados por coorte no INSS/CGU/CNJ, podendo exigir solicitação de acesso institucional futura (não efetuada). Produzir **matriz de indicadores realmente identificados e lacunas para LAI**, estimativas somente se houver base e denominadores.

**Critérios de aceite:** rastreabilidade temporal da fonte, tipos de beneficiário separados (RGPS/BPC/BLE), métodos estatísticos e universo explícitos, não atribuir ganho causal à codificação sem avaliação; F4 apenas com arquitetura A/B/C testada quanto a direitos e custos, 51 casos protegidos e Q mantidas. PR permanece **draft**, `main` não alterada por esta frente.
