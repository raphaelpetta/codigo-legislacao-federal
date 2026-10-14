# T29.M01 — F3-C: decisões TCU, cumprimento e descoberta de microdados de indeferimentos

**Corte:** 14/10/2026 · **Issue** [#40](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/40) · **PR** [#41 draft](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/41). **Proprietário:** T29.M01 somente pesquisa, interfaces de processo M06, benefícios M05, contribuição M02 e normas T01. **Não produz F4 nem C0/C1/M, não modifica módulos vizinhos.**

## 1. Retificação substantiva da F3-B: os motivos de indeferimento estão em dados abertos

A F3-B registrava corretamente que **não foi obtida** desagregação de indeferimentos por fundamento no boletim BEPS, mas a conclusão não pode ser extrapolada para “ausência de fonte pública”. Localizou-se o [conjunto de dados de benefícios indeferidos do INSS (SUIBE, PDA 2023–2027)](https://dadosabertos.inss.gov.br/dataset/beneficios-indeferidos-plano-de-dados-abertos-jun-2023-a-jun-2025). O metadado oficial identifica **competência do indeferimento, espécie, motivo do indeferimento, data de nascimento, sexo, clientela, forma de filiação, UF, data de indeferimento, ramo de atividade, agência e DER**. Há arquivos mensais de 2023 até [agosto/2026, recurso cadastrado em 22/09/2026](https://dadosabertos.inss.gov.br/dataset/beneficios-indeferidos-plano-de-dados-abertos-jun-2023-a-jun-2025/resource/673c05c7-93a1-4d6c-9cdd-1d9208a4df20).

**Limite de acesso:** a tentativa de descarregar o XLSX diretamente do armazenamento S3 exposto pelo portal retornou **HTTP 403** na pesquisa. **Não houve leitura ou agregação do conteúdo do arquivo**; não temos contagens por motivo, dicionário oficial de códigos ou cruzamento efetivo por filiação/UF. A correção F3-C é de **localização e viabilidade da fonte**, não análise estatística concluída.

**Distinção necessária:** um campo `motivo indeferimento` codificado pelo INSS representa a **classificação administrativa**, não prova de que o fundamento foi juridicamente correto. Para medir indeferimento **indevido** é necessário cotejar auditoria supervisionada ou reversão com a decisão e sua prova, não usar o rótulo da base como verdade do mérito.

**Matriz complementar:** [F3C_FONTES_MICRODADOS_E_LACUNAS_09.csv](F3C_FONTES_MICRODADOS_E_LACUNAS_09.csv), nove fontes/variáveis/status de leitura, com uma nova base pública efetivamente encontrada; o histórico de F3-B deve ser lido com esta errata.

## 2. Releitura de deliberações TCU por dispositivo e dever

As decisões anteriores já permitem identificar deveres verificáveis, e não apenas manchetes genéricas de “erro no CNIS”:

| Acórdão (sessão) | Tipo de comando | Objeto e subitem | O que ainda falta |
|---|---|---|---|
| [2.002/2024, 25/09/2024](https://pesquisa.apps.tcu.gov.br/doc/acordao-completo/2002/2024/Plen%C3%A1rio) | Determinação, **365 dias** da contagem juridicamente aplicável | **9.1.1** comprovar ciência de comunicação eletrônica no processo; **9.1.2** juntada do extrato CNIS na aposentadoria automática; **9.1.3** plano de tratamento de pendências, revisão amostral, impacto em tempo/renda e monitoramento | Não localizei certificação **por subitem** de que todos esses controles já funcionem. Vencimento teórico do prazo não prova cumprimento |
| [2.591/2024, 04/12/2024](https://pesquisa.apps.tcu.gov.br/doc/acordao-completo/2591/2024/Plen%C3%A1rio) | Determinações, **180 dias** para estudo/planos específicos | **9.1.1** estudo e cronograma para alinhar tempo CNIS e sistemas; **9.1.2.1–2** plano de correção de vínculos anacrônicos e automatismos de consistência; **9.1.3** revisão de registros materialmente inconsistentes | Separar apresentação de estudo de implantação; critérios devem respeitar decisões STF, inclusive carência materna afastada |
| [634/2025, 26/03/2025](https://pesquisa.apps.tcu.gov.br/doc/acordao-completo/634/2025/Plen%C3%A1rio) | Ciência de achado e determinações operacionais | **9.1** reconheceu indeferimentos automáticos indevidos no recorte; **9.2.1–2** adequar metas e pontuação à complexidade e à indisponibilidade dos sistemas | O acompanhamento posterior relata pendências estruturais e melhora insuficiente |
| [1.498/2026, 10/06/2026](https://portal.tcu.gov.br/imprensa/noticias/tcu-fiscaliza-sistema-de-concessao-automatica-de-beneficios-do-inss) | Determinação descrita por notícia oficial, prazo **180 dias** | Adequar automação para notificar pendências capazes de melhorar a prestação e liberar valor incontroverso | Em 14/10/2026 ainda não decorridos integralmente 180 dias da sessão; início formal de contagem requer intimação/publicação. Não alegar descumprimento certificado |
| [2.207/2026, 19/08/2026](https://pesquisa.apps.tcu.gov.br/doc/acordao-completo/2207/2026/Plen%C3%A1rio) | Acompanhamento de riscos | **9.1** manter concessão/pagamento na Lista de Alto Risco e **9.3** autorizar novo acompanhamento; relatório inclui resultados de supervisão e pendências dos acórdãos anteriores | Alto risco persistente não implica que **cada subitem** de cada acórdão esteja tecnicamente descumprido |

[Matriz F3-C de 17 comandos/achados](F3C_MATRIZ_TCU_17_DELIBERACOES.csv) descreve natureza, subitem, objeto, recorte e **estado de implementação**. O portal de texto do TCU é uma aplicação JavaScript e as páginas de `open` não devolveram a íntegra renderizada: foram consultados **trechos indexados de acórdãos, voto e relatório e notícias oficiais**, e **não foi possível validar o conteúdo completo fac-similar ou todos os anexos, atos de intimação e decisões de monitoramento**. Por isso “não certificado” não é “não cumprido”.

### Achado adicional: acórdão de 2025 sobre indeferimentos

No [Acórdão 634/2025](https://pesquisa.apps.tcu.gov.br/doc/acordao-completo/634/2025/Plen%C3%A1rio), o TCU relatou que **10,94%** dos indeferimentos **automáticos de janeiro a maio de 2024, no recorte de auditoria**, eram indevidos por descumprimento do art. 29-A §2º da Lei 8.213 e art.19 §1º do Decreto 3.048. O posterior [Acórdão 2.207/2026](https://pesquisa.apps.tcu.gov.br/doc/acordao-completo/2207/2026/Plen%C3%A1rio), ao retomar a auditoria, registra **13,20% de indeferimentos manuais indevidos** em seu recorte e **28,64% de inconsistências com risco** no fluxo automático. **Não somar percentuais, confundir bases nem projetá-los aos 882.589 indeferimentos BEPS de agosto/2026.**

## 3. Novo monitoramento de agosto/2026: evidência de progresso institucional, mas não saneamento comprovado

[TCU Acórdão 2.207/2026 — TC 007.351/2026-7, sessão 19/08/2026](https://pesquisa.apps.tcu.gov.br/doc/acordao-completo/2207/2026/Plen%C3%A1rio) examina o risco de **indeferimento indevido e concessão intempestiva**:

- **Índice de Conformidade do Reconhecimento de Direitos (Icon/ICRD): 83,8% em dezembro de 2025**, versus meta de **90,8%**;
- **supervisões do Supertec: 99,9%**, versus meta de **93,9%**;
- nas análises manuais supervisionadas pelo Supertec, a proporção de indeferimentos indevidos variou predominantemente **11%–13,5% até meados de 2025**, atingindo aproximadamente **16%** nos ciclos iniciados em outubro/2025 e janeiro/2026;
- o TCU cita **iniciativas**: reforço de supervisão, revisão de ofício, capacitação, planejamento de 2026 e aperfeiçoamento de automação; reconhece **persistência de gargalos** e manteve o tema na **Lista de Alto Risco**.

Isso diferencia **volume de supervisões** de **qualidade das decisões**, demonstrando que um indicador de produtividade superior à meta pode coexistir com conformidade aquém do planejado. Os valores de 83,8%, 99,9% e 16% têm **denominadores e unidades diferentes**; não são taxa nacional única, e o percentual Supertec não equivale a 99,9% de benefícios corretos.

**Não foi encontrada nesta rodada decisão oficial que certificasse individualmente cumprimento integral do 2.002/2024, 2.591/2024 ou 1.498/2026.** O 2.207/2026 atesta **avanço parcial e risco remanescente**. A própria existência de relatórios de acompanhamento não prova a implantação específica de comprovante de ciência, extrato CNIS e notificação do melhor benefício.

## 4. Novo mapa de lacunas e coleta

**Disponível como arquivo mensal público, não processado aqui:** códigos administrativos do motivo de indeferimento por espécie, competência, DER, UF, forma de filiação. Necessário baixar/ler recurso XLSX, conferir total e dicionário de código e compatibilizar com BEPS/fluxos de despacho; observar RGPS versus BPC/BLE. **Não é suficiente** para taxa de erro material sem auditoria de decisões.

**Disponível como regras de procedimento, sem estatística encontrada:** [Portaria Dirben/INSS 990/2022, atualizada em 2024](https://portalin.inss.gov.br/portaria990), sobre **RAC/acerto de vínculos e remunerações**, assinatura, prova e correções do CNIS. É um procedimento e não fornece, nesta consulta, o total e o tempo mediano de acertos.

**Não encontrado em série detalhada agregada:** número de pedidos de retificação CNIS, deferimentos e tempo de decisão por tipo; tempo integral DER→decisão final, incluindo exigências, recursos e implantação; reversão por falha cadastral; custos administrativos e efeitos de eventual mudança legislativa. Não atribuir zero ou estimativas inventadas às lacunas. Plano de dados abertos 2025–2027 e LAI são canais de obtenção, **não houve pedido LAI enviado nesta rodada**.

**Demanda de dados futura — especificação suficiente para LAI ou acesso a bases:**
1. Por competência mensal **jan/2024 até set/2026**, pedir total de **RAC CNIS** protocolados, concluídos/deferidos/parciais/indeferidos, motivo, tipo de vínculo e mediana DER→decisão, com dados **agregados/anônimos** e indicação da metodologia.
2. Requerer **dicionário oficial** dos códigos de motivo de indeferimento e suas alterações de versão para cruzar com o recurso público SUIBE; recortes por espécie, UF, competência e forma de filiação.
3. Para cada subitem TCU, solicitar relatório de **implementação/monitoramento**, evidências de sistema e indicadores de resultado, distinguindo “estudo entregue”, “funcionalidade implementada” e “auditada em produção”.
4. Pedir indicadores separados de **tempo DER→primeira decisão, DRD→DDB, DER→implantação/primeiro pagamento** e respectivas distribuições por espécie/coorte.

## 5. Efeitos para arquiteturas A/B/C, sem solução legislativa disfarçada

**A — núcleo comum de sujeitos e módulos funcionais especializados:** demanda contrato de interfaces M01–M02–M05–M06 para não transformar inconsistência de CNIS em ausência de filiação. Sinal mais favorável: uniformização de **atributos e versão da fonte**, com responsabilidade preservada e procedimento de acerto; nenhuma evidência causal de redução de custos.

**B — blocos separados com coordenação:** facilita intervenções operacionais sem reforma generalizada, porém mantém duplicações de classificação e regras que exigem concordância constante; correção de dados e notificação do melhor direito são igualmente necessárias.

**C — fusão integral:** com dados heterogêneos e amostras TCU que apontam erro de automatismos, unificar normativamente filiação, dever de recolhimento, qualidade e benefícios como uma única condição elevaria riscos jurídicos; qualquer alteração seria **M**, necessitando avaliação fiscal e constitucional. Não existe prova de ganho líquido.

**Nenhuma das três escolhas foi aprovada**. Os **51 cenários distintos F2-C** permanecem a referência para testes de direitos, com Q da guarda após EC103/Tema1271, idade facultativa 14/16, PSA, carência maternal e colisão art73-A 2026/2027. As correções e serviços prestacionais específicos pertencem a T29.M06/M05; M01 apenas documenta fronteiras.

## 6. FEITO / PENDENTE / PRÓXIMO

**FEITO:** corrigida a alegação de indisponibilidade de motivos de indeferimento, localizando base oficial INSS 2023–ago/2026; **17** determinações/achados TCU rastreados por subitem em **cinco acórdãos**; **9** fontes/lacunas de microdados; novos índices específicos de qualidade de 2025/2026 e base de indeferimentos indevidos com interpretação por universo; classificação expressa de situação do prazo e situação de implantação.

**PENDENTE:** leitura íntegra acessível dos acórdãos e anexos em modo não JS, monitoramentos individualizados de cumprimento, obtenção do recurso XLSX de agosto/2026 (HTTP 403), contagens de indeferimentos por motivos, indicadores de retificação CNIS, dicionários e custos; sem avaliação causal. Ainda não houve decisão legislativa C0/C1/M, revogação, alteração constitucional ou mudanças em outros módulos.

**PRÓXIMO — F3-D focal (antes de F4):** recuperação técnica autorizada dos arquivos públicos SUIBE indeferidos 2024–2026 e de seu dicionário, contagem por motivo/espécie/filiação com denominador explícito, e eventual consulta de monitoramento ou LAI com provas de execução por subitem das decisões TCU. Se downloads permanecerem inacessíveis, divulgar a **lacuna** e fazer proposta de coleta, sem estimativa inventada. F4 só se houver revisão jurídico-adversarial da concordância com módulos donos; caso contrário, manter A/B/C como hipóteses abertas.
