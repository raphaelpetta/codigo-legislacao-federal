# T07.M03 — Ciclo 38: integração probatória com T43 F1-L e controle de atos especiais
**Corte:** 14/10/2026. PR #39 (draft). Documento de coordenação com [T43 PR #43](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/43), sem ratificar arquitetura R2, reforma material ou equivalência C0-J. Pressuposto: a lei especial define os efeitos da comunicação; o Governo Digital define requisitos tecnológicos quando aplicáveis.

## FEITO — cinco verificações cruzadas documentais
| Hipótese | Prova instrumental sob T43 | Efeito jurídico sob T07 / lei especial | Risco evitado |
|---|---|---|---|
| DTE fiscal em 2015 ([CARF 1301-008.239](DOSSIE_CICLO33_CARF_1301_008239.md)) | Termo de abertura de **mensagem** autenticado, e não mera abertura posterior de anexo | Ciência e duração do prazo segundo Decreto 70.235 na redação incidente em 2015 | Projetar sobre 2015 o novo prazo da LC 227/2026 |
| Edital ambiental ICMBio em 2014 ([REsp 2.154.295/RS](DOSSIE_CICLO36_ICMBIO_TEMA1329_CASO_REAL.md)) | Documentos separados: AR do **auto de infração**, edital posterior de **alegações finais**, registro de prejuízo alegado/provado | Tema 1.329/STJ exige prejuízo demonstrado para nulidade dos atos posteriores na hipótese histórica; data exata do edital permanece lacuna | Converter o AR do auto em recibo das alegações ou presumir nulidade universal |
| Edital ambiental de março de 2025 ([ciclo 37](DOSSIE_CICLO37_EDITAL_IBAMA_2025.md)) | Edital coletivo publicado, com individualização por processo e alegação de diligências anteriores | Verificar redações vigentes do art. 122 e art. 96, §4º, **atos e diligências de cada autuado**; não certificar ciência pelo título da publicação | Tratar endereço desconhecido declarado como prova individual irrefutável ou assumir que o edital de 2025 segue regime de 2014 |
| Recurso especial de dados abertos ([Lei 14.129 art. 35](MINUTA_CICLO32_X6_ESPECIALIDADE_DADOS_ABERTOS.md)) | Registro de decisão negativa e prova da comunicação, com resguardo de identidade e dados | Prazo especial **10 dias da ciência** e **5 dias para manifestação da autoridade superior**, sem equiparar à reconsideração a quo da Lei 9.784 | Apagar especialidade ao fundir T07 e T43 |
| CPF e interoperabilidade ([T43 F1-L](https://github.com/raphaelpetta/codigo-legislacao-federal/blob/modulo/T43-M04-governo-digital-f0-f1-20261014/modulos/T43/M04/RELATORIO_F1L_AVALIACAO_JURIDICA_14_DESTINOS.md)) | Necessidade, finalidade, integridade, proteção de dados pessoais, identificação do responsável e acesso controlado aos registros | Notificações e atos eletrônicos não tornam **públicos** dados biométricos e outros elementos protegidos; preservar LAI/LGPD e autonomia federativa | Confundir auditabilidade de entrega com difusão irrestrita da prova ou dispensar competência |

## Protocolo de prova mínimo proposto — hipótese de engenharia, não obrigação já promulgada
Para cada episódio coletar (quando disponível e admissível): identificador de procedimento; norma e redação vigente na **data do ato**; ato específico a comunicar; meio utilizado; prova de envio e de entrega/consulta, com fonte e integridade; identificação de destinatário e diligências feitas quando relevantes; critério legal da ciência; regra de contagem e eventuais suspensões; fatos concretos de defesa/prejuízo; e conclusão estritamente relativa àquele procedimento. Classificar falta de documento como **lacuna**, não como data presumida.

A obtenção, guarda e divulgação desses registros deve aplicar proteção de dados e sigilo. A **estrutura exata** dos campos é potencial inovação técnica, sob análise T43; sua adoção geral não deriva automaticamente de qualquer decisão judicial ou da Lei 14.129/2021.

## Testes negativos para eventual X2/X6
1. Recusar `ENVIADO = CIENTE` sem suporte da lei especial e prova exigível.
2. Recusar `EDITAL = SEMPRE_NULO` ou `EDITAL = SEMPRE_VALIDO`; controlar data, ato, regime e prejuízo quando relevante.
3. Recusar `AR_DO_AUTO = AR_DAS_ALEGACOES_FINAIS`.
4. Recusar `MES_LEGISLACAO_ATUAL = REDACAO_VIGENTE_NA_DATA_DO_ATO`.
5. Recusar `LOG_AUDITAVEL = DADO_PESSOAL_PUBLICO`.
6. Recusar que regra de prazo geral substitua o prazo especial e a identidade da autoridade que decide (Lei 14.129 art. 35 versus Lei 9.784).
7. Recusar transportar de 2026 para 2015 prazos fiscais ou efeitos eletrônicos de 2024 para edital ambiental de 2014.

## FEITO / PENDENTE / PRÓXIMO
**FEITO:** integração documental com quatro cenários administrativos e os 14 destinos normativos examinados em T43 F1-L, preservando especialidade e limites da prova. **PENDENTE:** autos e recibos individuais, confronto de legislação específica em cada caso e sua vigência, LGPD e LAI em detalhamento, diálogo formal T43/T01 e `DEC-016`; **todos Q**. **PRÓXIMO:** testar os sete bloqueios contra casos documentados e submeter eventuais campos novos a análise M expressa antes de qualquer redação final. Sem merge ou revogação.
