# T29.M01 — Pacote de continuidade da rodada 15 / F3-E (14/10/2026)

**Dono:** T29.M01, pesquisa documental e técnica. **Issue:** [#40](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/40), **PR:** [#41 draft](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/41), **branch:** `modulo/T29-M01-segurados-dependentes-f0-f1-20261014`. `main` CLF na abertura: `16fba172c875c7a0de388288fe70005c944021d6`. CF/1988 e EC103/2019 são direito vigente; CF alternativa não foi considerada promulgada. Nenhum módulo T29.M02/M05/M06 ou T01/T24 editado.

## FEITO
1. [Relatório F3-E](RELATORIO_F3E_SUIBE_ACESSO_LAI_E_LIMITE_EMPIRICO.md): quatro verificações sobre acesso público/dados, parecer de limites, TCU e fronteiras do CLF.
2. [Log F3-E de 10 verificações](F3E_LOG_ACESSO_SUIBE_LAI_TCU_10_VERIFICACOES.csv): catálogo público de indeferimentos, ficha de agosto (22/09/2026), dois downloads S3 **403**, ações da API CKAN inacessíveis no mecanismo web, falha DNS no ambiente local, indicação de licença ausente, dicionário não localizado, nenhum novo estado de cumprimento TCU provado, minuta LAI não enviada.
3. [Minuta específica LAI/SUIBE](F3E_MINUTA_PEDIDO_LAI_SUIBE_NAO_PROTOCOLADO.md): pedido de arquivos **existentes** julho/agosto 2026, URL funcional, dicionário de motivos, esquema, unidade observacional e versões. [Canal oficial INSS/Fala.BR](https://www.gov.br/inss/pt-br/acesso-a-informacao/sic-servico-de-informacao-ao-cidadao/como-utilizar). **Status expressamente NÃO PROTOCOLADO, sem prazo iniciado.**
4. [Protocolo técnico G0–G7](F3E_PROTOCOLO_TABULACAO_SUIBE_E_CRITERIOS_QUALIDADE.md): controle de origem, bytes/hash, cabeçalho, dicionário, colunas sensíveis, motivo único/múltiplo, denominadores por mesma competência/espécie/filiação, separação RGPS/BPC/BLE, não confundir motivo com ilicitude e estatística descritiva com causalidade. **Nenhuma tabulação executada**, pois não houve XLSX.

**Fontes centrais**: [INSS catálogo dados indeferidos](https://dadosabertos.inss.gov.br/dataset/beneficios-indeferidos-plano-de-dados-abertos-jun-2023-a-jun-2025), [recurso de agosto](https://dadosabertos.inss.gov.br/dataset/beneficios-indeferidos-plano-de-dados-abertos-jun-2023-a-jun-2025/resource/673c05c7-93a1-4d6c-9cdd-1d9208a4df20), [INSS orientação SIC/Fala.BR](https://www.gov.br/inss/pt-br/acesso-a-informacao/sic-servico-de-informacao-ao-cidadao/como-utilizar), [TCU 985/2026](https://btcu.apps.tcu.gov.br/api/obterDocumentoPdf/80248239). As 8 determinações TCU **EM CUMPRIMENTO** constavam assim em **maio/2026**, **não foi certificado seu estado em outubro/2026**.

## PENDENTE
- XLSX SUIBE e documentação de códigos: **sem bytes**, sem quantificação. Não reproduzir os mesmos downloads sem mudança de rota ou autorização; a informação de bloqueio já está registrada.
- Não houve envio de LAI, contato formal INSS, requisição automática por plugin, dados novos do CNIS ou microdados/estatística de motivo.
- Cumprimento posterior individualizado dos 8 itens ainda pendentes TCU e de outros acórdãos: **não localizado por prova nova nesta rodada**; não confundir ausência de ato encontrado com inexistência absoluta.
- F2-D/concordância jurídico-material, decisões de arquitetura A/B/C, DEC016, STF Tema1271, PSA e idade facultativa 14/16 seguem Q em seus respectivos donos.
- Nenhum F4/F5/C0/C1/M aprovado, nenhuma intervenção na `main` nem merge.

## PRÓXIMO — mudar efetivamente de atividade

**Opção de execução 1:** quando houver link público acessível ou documento encaminhado, processar SUIBE conforme G0–G7 e publicar somente agregados verificáveis.

**Opção de execução 2:** apresentar a minuta de pedido LAI via Fala.BR com consentimento/ação efetiva do interessado; registrar número do protocolo e aguardar resposta, sem inventar prazo ou afirmar envio.

**Opção de investigação independente (se o acesso persistir bloqueado):** preparar **F4-0** com alternativas normativas condicionais A/B, quadro de riscos e reserva de direitos, **sem escolher uma reforma, sem custos fictícios e sem executar novos inventários duplicados**. A definição final pertence à governança central e aos módulos titulares, com testes de não regressão sobre 51 cenários.

**Conclusão delimitada:** F3-E concluída **como investigação de acessibilidade e preparação de coleta**, não como medição dos motivos de indeferimento. PR permanece draft.
