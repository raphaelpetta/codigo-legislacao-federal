# T29.M01 — F3-D: monitoramento efetivo do TCU e motivos de indeferimento no INSS

**Corte documental: 14/10/2026.** **Issue [#40](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/40)**; **PR [#41 draft](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/41)**; titular único desta pesquisa **T29.M01**, sem modificações em T29.M02/M05/M06 ou T01. **Produto F3, não aprovação C0/C1/M, F4 ou minuta F5.**

## 1. Resultado verificável e correção da F3-C

A F3-C havia identificado os Acórdãos 2.002/2024, 2.591/2024, 634/2025, 1.498/2026 e 2.207/2026, mas **não havia certificado cumprimento individual de itens**. A F3-D encontrou prova oficial de monitoramento específico do **Acórdão 634/2025**:

- [Acórdão **985/2026-TCU-Plenário**, publicado no BTCU de **04/05/2026**, código de autenticidade 80248239](https://btcu.apps.tcu.gov.br/api/obterDocumentoPdf/80248239), TC **023.720/2025-5**. **Três itens cumpridos:** 9.2.2, 9.2.6 e 9.2.10. **Oito itens EM CUMPRIMENTO:** 9.2.1, 9.2.3, 9.2.4, 9.2.5, 9.2.7, 9.2.8, 9.2.9 e 9.2.11. Determinou continuidade de monitoramento dos oito itens **em até 90 dias** após a deliberação; não pressupor que houve decisão conclusiva posterior apenas pelo transcurso.
- [Texto do Acórdão **634/2025**, encaminhado oficialmente à Câmara](https://www2.camara.leg.br/atividade-legislativa/comissoes/comissoes-permanentes/cffc/expedientes-recebidos/Aviso000.109_2026GABPRES.pdf/view), **página 19–20 do PDF**, lista **todos os onze objetos**, permitindo casar situação do item ao dever específico.
- [Acórdão **989/2025**, publicado no BTCU de 15/05/2025](https://btcu.apps.tcu.gov.br/api/obterDocumentoPdf/78082970), corrige o fundamento do item 9.2 (art. 4º da Resolução TCU 315/2020) e **inclui expressamente prazo de 180 dias**. A publicação de correção não determina, isoladamente, o termo inicial de intimação em cada situação.
- [Acórdão **2.207/2026**, 19/08/2026](https://pesquisa.apps.tcu.gov.br/doc/acordao-completo/2207/2026/Plen%C3%A1rio), em seu relatório, **ratifica e contextualiza** as três determinações cumpridas e oito em cumprimento, além de manter o reconhecimento inicial de benefícios na Lista de Alto Risco. Há progresso institucional, mas não plena normalização finalística.

**Matriz primária nova:** [F3D_MONITORAMENTO_TCU_985_2026_11_ITENS.csv](F3D_MONITORAMENTO_TCU_985_2026_11_ITENS.csv), com 11 IDs únicos, objeto, subitem, fonte original, fonte da correção de prazo e status oficial.

### Medidas já classificadas como cumpridas pelo TCU

| Subitem 634/2025 | Objeto | Situação TCU 985/2026 |
|---|---|---|
| **9.2.2** | Ajuste tempestivo de metas quando há indisponibilidade de sistemas | **CUMPRIDA** |
| **9.2.6** | Comunicação efetiva de incentivos à capacitação dos servidores | **CUMPRIDA** |
| **9.2.10** | Aprimorar informação sobre preenchimento correto dos requerimentos | **CUMPRIDA** |

### Medidas com cumprimento ainda em andamento

| Subitem | Objeto condensado |
|---|---|
| **9.2.1** | Compatibilização de metas, pontuação de exigências e complexidade da análise |
| **9.2.3** | Comunicação aos servidores das desconformidades encontradas pelo Supertec |
| **9.2.4** | Respostas tempestivas e claras do suporte técnico |
| **9.2.5** | Capacitação alinhada às necessidades dos servidores |
| **9.2.7** | Controles proativos e alertas para prevenir indeferimentos por falhas saneáveis |
| **9.2.8** | Avaliação sistemática da qualidade de análises automáticas |
| **9.2.9** | Indicadores e metas de qualidade do processamento automático |
| **9.2.11** | Ferramentas interativas para preenchimento correto e alertas de erro |

**Não extrapolar:** essa situação certificada refere-se ao **634/2025**, não a cada subitem dos Acórdãos **2.002/2024, 2.591/2024 ou 1.498/2026**; seus monitoramentos individualizados continuam pendentes no dossiê. A situação “em cumprimento” foi atribuída pelo **TCU**, não calculada pelo pesquisador. **Cumprimento reconhecido de três medidas não equivale** a prova de redução de indeferimentos indevidos. No Acórdão 2.207/2026, índice Icon **83,8%** ante meta **90,8%** no fim de 2025 e série Supertec com **até 16%** de indeferimentos indevidos nos recortes supervisionados, **não taxa nacional**.

## 2. SUIBE de indeferimentos: a localização é certa, a extração continua não concluída

Conferido o [dataset oficial INSS de benefícios indeferidos (PDA 2023–2027)](https://dadosabertos.inss.gov.br/dataset/beneficios-indeferidos-plano-de-dados-abertos-jun-2023-a-jun-2025), com ficha de recurso [**agosto/2026**, publicada **22/09/2026**](https://dadosabertos.inss.gov.br/dataset/beneficios-indeferidos-plano-de-dados-abertos-jun-2023-a-jun-2025/resource/673c05c7-93a1-4d6c-9cdd-1d9208a4df20). Há campos prometidos **motivo do indeferimento, espécie, filiação, UF, competência, data do indeferimento e DER**.

**Tentativas públicas efetivamente realizadas:** (i) download **agosto/2026** pelo link oferecido no catálogo → **HTTP 403 Forbidden**; (ii) download **julho/2026** pelo mesmo mecanismo → **HTTP 403 Forbidden**; (iii) endpoints de CKAN para `package_show` e `resource_show` não acessíveis no mecanismo de consulta; (iv) tentativa de acesso programático direto a catálogo/armazenamento no ambiente de execução → **falha de resolução DNS**, não obtenção de bytes. **Não houve obtenção, leitura, processamento, classificação nem contagem de linhas de arquivo XLSX**. Não tentar inferir distribuição a partir dos metadados, nem contornar restrições de acesso.

**Indicador que falta para F4:** frequência dos códigos de motivo por espécie/UF/filiação/competência, depois de obter dicionário de código e conferir se as categorias do SUIBE são comparáveis com o BEPS, sobretudo RGPS versus BPC/BLE. **Motivo administrativo NÃO equivale à correção jurídica do indeferimento**.

## 3. Nova alternativa de evidência pública, sem microdados: Transparência Previdenciária de março/2026

Foi lida a [apresentação oficial do INSS **Transparência Previdenciária — março/2026**, PDF, página 12 (índice 11)](https://www.gov.br/inss/pt-br/portal-de-transparencia/2026_03TransparnciaPrevidenciriav41.pdf). A lâmina **“Principais motivos de indeferimento”** identifica estes motivos de maior destaque *por espécie*, sem publicar os quantitativos individuais:

- **Auxílio por incapacidade temporária:** incapacidade laborativa não comprovada pela perícia;
- **BPC pessoa com deficiência:** não atendimento do requisito de deficiência;
- **BPC idoso:** renda acima do limite mencionado na lâmina (não converter descrição simplificada em regra jurídica sem exceções);
- **Salário-maternidade:** INSS afirma ausência de filiação ao RGPS na data do afastamento;
- **Aposentadorias:** insuficiência de idade ou tempo conforme regra aplicável;
- **Pensão por morte:** não comprovação de condição de companheiro(a).

A lâmina informa **796.798 indeferimentos** e indicador **47%** no período de **março/2026**, extração **13/04/2026**. **Não há contagem desagregada dos seis motivos na lâmina**, nem denominador descrito de forma suficiente para recalcular os 47% e qualificá-los como probabilidade de indeferimento de coorte de DER. Esses são **motivos declarados pelo INSS**, não prova de que cada negativa esteja correta ou incorreta. BPC é **assistencial** e não deve entrar na contagem estrita de RGPS.

**Matriz nova:** [F3D_MOTIVOS_INSS_TRANSPARENCIA_MAR2026_06.csv](F3D_MOTIVOS_INSS_TRANSPARENCIA_MAR2026_06.csv), com seis motivos e módulo de interface identificado, marcação **NAO_PUBLICADO_NA_LAMINA** para a quantidade de cada motivo.

**Implica para T29.M01:** filiação (salário-maternidade) e dependência familiar (pensão) aparecem como temas reais de negativa administrativa; não há prova ainda do volume que representam nem do percentual de negativas juridicamente indevidas por essas causas. É interface **M01/M05/M06**, não autorização para modificar prazo ou prova por decreto editorial.

## 4. Protocolo de análise reproduzível para quando dados forem acessíveis

**Unidade observacional antes de qualquer taxa:** cada linha da planilha será qualificada quanto a competência de **despacho/indeferimento**, espécie, código de motivo, UF, forma de filiação e DER, e quanto a eventuais registros duplicados ou múltiplos motivos por um benefício. A falta de identificador seguro exige declarar limitação de deduplicação, **não inventar unidade pessoa ou requerimento único**.

**Agrupamentos que ficam pendentes (não produzidos nesta rodada):**
1. `N(motivo, especie, filiacao, competência)` = número de registros que satisfazem os campos no **mesmo arquivo e universo**;
2. `percentual_dentro_especie` = numerador/denominador de todos os indeferimentos **da mesma espécie, competência e recorte**, se o registro for mutuamente exclusivo ou regra de múltiplos motivos for descrita;
3. série 2024–2026 com conferência de continuidade das etiquetas de motivo, versões do dicionário e mudanças de sistema;
4. cruzamento **apenas agregado e comparável** com BEPS, documentando divergências de universo, unidades e data de extração;
5. reconstrução de coortes por DER **somente se houver conjunto de entradas/saídas com chave, versões e completude**, não apenas arquivos de indeferimentos.

**Proibido inferir:** que uma distribuição de motivos é distribuição de **erros**, que ausência CNIS equivale à inexistência de filiação, que carência de salário-maternidade anterior ao julgamento do STF continua válida, que todos pedidos da competência de agosto tiveram seu desfecho no mesmo mês, ou que 47% se aplica a toda coorte no RGPS.

**Proteção de dados:** coletar apenas agregados publicáveis, evitar republicação de datas de nascimento ou outras colunas potencialmente identificadoras; conferir restrições de licença e LGPD aplicáveis ao material aberto.

## 5. Evidência ainda necessária — plano de execução, sem LAI protocolada

**Pedidos de dados candidatos ao INSS/Dataprev/CGU, não enviados nesta rodada:**

- restabelecimento ou disponibilização autorizada do XLSX de julho/agosto 2026 com dicionário de códigos, nome do layout e total de registros por arquivo, versão e data de extração;
- quadro agregado mensal 2024–2026 por **motivo, espécie, forma de filiação e UF**, com detalhamento RGPS/BPC/BLE;
- estatística de acerto/retificação CNIS por competência e tipo, protocolados/decididos/procedentes/improcedentes, prazo **DER original→resolução** e motivos mais frequentes;
- monitoramento por item dos **Acórdãos 2.002/2024, 2.591/2024, 1.498/2026** e eventual evolução **após** o 985/2026 quanto aos oito itens restantes do 634/2025, com provas de implementação de controles;
- dados de revisão de ofício e supervisão separados entre análise **manual, automática e médico-pericial**, com denominadores e definições para não extrapolar amostra.

**Não houve envio de e-mail, protocolo de LAI, contato com INSS ou decisão de reforma.**

## 6. Consequência para as alternativas F3-A

O diagnóstico já sustenta exigência de **prova auditável, comunicação idônea, cadastro corrigível e indicadores de qualidade separados de produtividade**, independentemente de optar por:

- **A:** conceitos gerais de sujeitos, qualidade e dependentes, com custeio e processo especializados;
- **B:** regimes separados, coordenados por definição e remissão expressas;
- **C:** fusão material integral — ainda elevada exposição a conflitos de responsabilidade contributiva, prova, categoria e exigências prestacionais.

**Não há estimativa causal de ganho fiscal, administrativa ou de redução de indeferimentos** de qualquer alternativa. A existência de medidas oficialmente cumpridas pelo INSS não prova o desempenho de uma codificação futura. Não iniciar F4 ou F5 como se as opções A/B/C estivessem aprovadas.

## 7. FEITO/PENDENTE/PRÓXIMO

**FEITO:** atualizou-se o estado de **11 determinações específicas do Acórdão 634/2025** via **TCU 985/2026 (3 cumpridas, 8 em cumprimento)**; localizada retificação TCU 989/2025 do prazo 180 dias; confirmados **seis motivos declarados pelo INSS** no PDF de março/2026; reiterado bloqueio real dos downloads SUIBE julho/agosto e qualidade distinta de metadados versus conteúdo.

**PENDENTE:** acesso legítimo aos microdados e códigos do SUIBE (sem taxas), dados de correção CNIS, monitoramentos posteriores do 985/2026, implementação por subitem de 2002/2591/1498; reprodução de critérios de controle do Supertec, reanálise de decisões e causas de erro com amostras; conciliação F2-D e Q material do módulo.

**PRÓXIMO sugerido — F3-E / porta de integração de dados:** obter acesso público funcional ou resposta institucional oficial sobre SUIBE, concluir estatística desagregada somente com arquivo verificado, e compatibilizar o registro de cumprimento do TCU com a separação M01/M05/M06. **Se fontes indisponíveis**, usar evidência já recuperada e abrir F4 apenas como **alternativas jurídicas condicionais, sujeitas a validação e ratificação central**, jamais com promessa numérica de eficiência.

**Estado:** análise F3-D concluída no recorte documental e com bloqueio de extração expressamente preservado. PR #41 continua draft, sem merge e sem texto C0/C1/M aprovado.
