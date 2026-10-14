# T29.M01 — Pacote de continuidade da rodada 14 / F3-D (14/10/2026)

**Responsável:** T29.M01, pesquisa/diagnóstico · **Issue [#40](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/40)** · **PR [#41 draft](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/41)** · **branch:** `modulo/T29-M01-segurados-dependentes-f0-f1-20261014`. `main` CLF observada na abertura: `16fba172c875c7a0de388288fe70005c944021d6`. **CF/1988/EC103 vigente; CF alternativa não tratada como norma atual.** Nenhum outro módulo editado.

## FEITO

- [F3D_MONITORAMENTO_TCU_985_2026_11_ITENS.csv](F3D_MONITORAMENTO_TCU_985_2026_11_ITENS.csv): **11 determinações do Acórdão 634/2025-TCU** rastreadas a objeto, fonte, retificação de prazo e situação. **TCU 985/2026 (BTCU 04/05/2026)** declarou **cumpridas** 9.2.2, 9.2.6, 9.2.10; **em cumprimento** 9.2.1, 9.2.3, 9.2.4, 9.2.5, 9.2.7, 9.2.8, 9.2.9, 9.2.11. [BTCU oficial do Acórdão 985/2026](https://btcu.apps.tcu.gov.br/api/obterDocumentoPdf/80248239).
- [TCU 989/2025 (BTCU 15/05/2025)](https://btcu.apps.tcu.gov.br/api/obterDocumentoPdf/78082970): **correção do prazo para 180 dias** e fundamento do item 9.2 do Acórdão 634/2025; objetos individualizados [no texto oficial encaminhado à Câmara, p.19–20 do PDF](https://www2.camara.leg.br/atividade-legislativa/comissoes/comissoes-permanentes/cffc/expedientes-recebidos/Aviso000.109_2026GABPRES.pdf/view).
- [F3D_MOTIVOS_INSS_TRANSPARENCIA_MAR2026_06.csv](F3D_MOTIVOS_INSS_TRANSPARENCIA_MAR2026_06.csv): **seis motivos administrativos em seis grupos** listados na [apresentação INSS março/2026, página 12 do PDF](https://www.gov.br/inss/pt-br/portal-de-transparencia/2026_03TransparnciaPrevidenciriav41.pdf); **796.798 indeferimentos, indicador 47% em março/2026**, sem contagem individual por cada motivo e sem denominador da apresentação suficiente para taxa de coorte. BPC é assistencial, distinto do RGPS.
- [RELATORIO_F3D_MONITORAMENTO_TCU_MOTIVOS_INSS_E_BLOQUEIO_SUIBE.md](RELATORIO_F3D_MONITORAMENTO_TCU_MOTIVOS_INSS_E_BLOQUEIO_SUIBE.md): auditoria de continuidade, origens e limites probatórios, protocolo de eventual análise estatística e perguntas concretas a órgãos. Errata incluída no [relatório F3-C](RELATORIO_F3C_TCU_INDEFERIMENTOS_MICRODADOS_2026.md) reconhecendo o monitoramento efetivamente localizado.
- Download público dos [XLSX de julho/2026 e agosto/2026 do INSS](https://dadosabertos.inss.gov.br/dataset/beneficios-indeferidos-plano-de-dados-abertos-jun-2023-a-jun-2025) testado a partir dos links oficiais: **ambos 403 Forbidden**. Metadados oficiais acessíveis. Endpoints CKAN não acessíveis pela pesquisa; ambiente de execução sem resolução externa. **Zero linhas XLSX lidas, zero frequências inventadas e zero LAI protocoladas**.

## PENDENTE

1. **SUIBE:** obter, por acesso público autorizado ou resposta institucional, planilhas e **dicionário de motivos** com universo, competencia, espécie, filiação, UF; não tratar motivo como erro jurídico nem dividir despachos de agosto por novas DER do mesmo mês como coorte.
2. **TCU:** os 8 itens marcados **EM CUMPRIMENTO** em maio/2026 devem ter situação revalidada por eventual novo acórdão específico. A notícia **2207/2026** confirma risco geral persistente, mas **não altera por si a classificação de cada subitem**. Monitoramentos individualizados de **TCU 2002/2024, 2591/2024 e 1498/2026** permanecem sem certificação neste dossiê.
3. **CNIS:** dados agregados de pedidos de acerto (RAC), procedência, tempo e efeito sobre concessões não localizados; F3-B já identifica bases BEPS e limitações.
4. **F2-D** é conciliação de outra linha, não repetir 51 cenários nem fundir dois inventários. T29.M02/M05/M06 e T01 permanecem responsáveis por contribuição, benefícios, procedimento e temporalidade; nenhum arquivo modificado.
5. F4/F5 e classificação C0/C1/M não aprovados; sem cálculo de impacto fiscal, atribuição causal de economia ou modificação legislativa.

## PRÓXIMO

**F3-E — coleta focal:** buscar versão autorizada dos XLSX SUIBE e dicionário; executar tabulação por **motivo × espécie × filiação × mês do despacho** com denominadores internos verificados, preservando privacidade e versões dos códigos. Se permanecer bloqueado, preparar/sugerir **pedido LAI para dados agregados e documentação técnica**; nunca afirmar que foi protocolado sem ação efetiva.

**Governança:** antes de F4, documentar situação de cumprimento dos oito itens restantes do 634/2025 e dos acórdãos de automação com revisão jurídico-material de M05/M06/T01. A estrutura A/B/C é **hipótese**, não decisão. **PR draft, sem merge e sem alteração `main`.**

**Critério:** dados com fonte, data de extração, universo, método, proveniência e limitações; sem duplicação entre F2/F3 nem dados falsos.
