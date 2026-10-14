# T29.M01 — F3-B: diagnóstico empírico brasileiro da filiação, cadastro, prova e decisão administrativa

**Data de corte:** 14/10/2026. **Issue:** [#40](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/40) · **PR:** [#41 draft](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/41). **Dono da pesquisa F3-B:** T29.M01; interfaces M02 custeio, M05 benefícios, M06 procedimento, T01 informação normativa. **Não fazer reformas C0/C1/M, não editar módulo alheio nem `main`.**  
**Âmbito:** situação do RGPS no INSS, com ressalva de que algumas estatísticas incluem **RGPS, acidentes, assistência (BPC) e benefícios de legislação específica**. Pesquisa documental e análise de identificação de dados, **não avaliação causal** nem uso de microdados.

## 1. Evidência oficial mais recente obtida e unidade de observação

[BEPS — agosto/2026, publicado em 30/09/2026 (PDF)](https://www.gov.br/previdencia/pt-br/assuntos/previdencia-social/Dados-estatisticos-previdencia-social-e-inss/boletins-da-previdencia-social/2026/beps082026_final.pdf), edição 32 n° 8; lidos **quadro 1 p.4, quadro 24 p.48, quadro 25 p.49 e notas conceituais p.53** (páginas impressas 01, 24, 25). **Os números foram conferidos visualmente nos quadros oficiais**, além do texto de extração.

| Dado BEPS, agosto/2026 | Valor | Natureza da medida |
|---|---:|---|
| Benefícios concedidos pelo INSS | **844.389** | Fluxo de concessões despachadas no mês, incluindo previdenciários, assistenciais e especiais |
| Concedidos previdenciários | **716.161** | Subconjunto dentro dos 844.389 (quadro 9-A) |
| Concedidos assistenciais | **127.938** | Fora do conceito estrito de benefício do RGPS |
| Benefícios de Legislação Específica | **290** | Fora da categoria estrita de RGPS |
| Requerimentos indeferidos | **882.589** | Despachos não concessivos realizados no mês; **não significa 882.589 pedidos protocolados e negados em agosto** |
| Indeferidos relativos a espécies sujeitas a perícia | **615.211** | Classificação por espécie pericial, **não comprova que cada negativa se deveu a parecer pericial** |
| Concedidos relativos a espécies sujeitas a perícia | **491.400** | Outro fluxo mensal, **não a mesma coorte de entrada dos indeferidos** |
| Tempo médio de concessão no mês | **33 dias** | Média dos benefícios concedidos com despacho normal; pode partir da **Data de Regularização da Documentação (DRD)**, não exclusivamente DER |
| Tempo médio de concessão em julho/2026 | **40 dias** | Série anterior da mesma publicação; mudança **não prova causa** |
| Requerimentos ainda em análise, agosto | **1.251.813** | **Estoque** de processos pendentes de despacho, perícia ou documentação, não fluxo de entradas |
| Aguardando análise INSS/perícia inicial | **873.976** | Subconjunto do estoque: 638.566 até 45 dias, 235.410 acima de 45 |
| Aguardando exigência documental do segurado | **377.837** | Subconjunto: 228.780 até 45 dias, 149.057 acima de 45 |
| Total dos estoques acima de 45 dias | **384.467** | Soma das duas categorias de pendência, não tempo médio de concessão |

**Definições oficiais essenciais:** BEPS p.53 descreve `requeridos` pela DER; `indeferidos` pelo despacho negativo; `em análise` como estoque sem DDB ou aguardando documento; `tempo médio de concessão` como dias entre **DER ou DRD**, se houver exigência, e DDB, sem despachos recursais/judiciais. Assim, **não produzir “taxa de indeferimento” com indeferidos de agosto dividido por concessões+indeferimentos de agosto como se fosse resultado da coorte de entrada**. O mesmo vale para inferir que a fila passou de **1,8 milhão em junho/2026** (notícia INSS com definições próprias) para 1,25 milhão em agosto sem comparar os universos, extrações e mudanças metodológicas.

**Fontes:** [BEPS/ago-2026](https://www.gov.br/previdencia/pt-br/assuntos/previdencia-social/Dados-estatisticos-previdencia-social-e-inss/boletins-da-previdencia-social/2026/beps082026_final.pdf); [Portal Transparência Previdenciária, dados até julho/2026 na página consultada](https://www.gov.br/inss/pt-br/portal-de-transparencia/portal-de-transparencia); [INSS, notícia 30/06/2026 sobre fila de 1,8 milhão](https://www.gov.br/inss/pt-br/noticias/fila-do-inss-atinge-menor-patamar-em-21-meses-com-1-8-milhao-de-requerimentos/). **A apresentação do BEPS é a publicação agosto/2026, não indicadores de outubro de 2026**.

## 2. CNIS e automação: três achados de auditoria independentes

### TCU Acórdão 2.002/2024 — automação e melhor direito

[TCU notícia oficial de 30/09/2024, Acórdão 2.002/2024-Plenário, TC 007.138/2022-9](https://portal.tcu.gov.br/imprensa/noticias/auditoria-avalia-controles-internos-do-inss-para-concessao-de-aposentadoria): auditoria da conformidade e dos controles do reconhecimento inicial de aposentadorias com base nas **contas de 2021**, analisada em 2024. Indicou **70% dos casos verificados com pendências do CNIS desconsideradas** nos processos automáticos e **31% de tarefas não concluídas automaticamente** no período auditado. O material público examinado **não fornece denominadores completos da amostra**; números **NÃO equivalem** à proporção de concessões erradas em todo o INSS nem a uma medição nacional em 2026. A ausência do extrato CNIS e falhas de explicação da decisão também foram registradas.

**Achado jurídico:** processo automatizado pode reconhecer prestação ou valor inferior mesmo com vínculo/prova existente. O sistema deve distinguir **base cadastral**, **fato de trabalho** e **direito material**; motivação e possibilidade de retificar dados são salvaguardas.

### TCU Acórdão 2.591/2024 — qualidade do histórico

[TCU notícia de 10/12/2024, TC 010.781/2022-6](https://portal.tcu.gov.br/imprensa/noticias/fiscalizacao-avalia-uso-do-cadastro-nacional-de-informacoes-sociais-na-concessao-de-beneficios-previdenciarios): fiscalização de registros de vínculos, remunerações e contribuições identificou ausência/inconsistência de dados, inclusive CNPJ inexistente, CPF nulo e datas incompatíveis. Determinou plano de ação/estudo para aumentar consistência entre histórico CNIS e sistemas de concessão. **Não foi extraído percentual nacional de registros defeituosos.**

**Alerta normativo:** a notícia menciona exemplos de benefícios concedidos sem carência legal de salário-maternidade; por se tratar de dados históricos e divulgação posterior ao julgamento **STF ADIs 2110/2111**, isso **não revalida** exigência de carência declarada inconstitucional. Sistemas e auditorias devem guardar **versão temporal correta da norma e autoridade vinculante**; não converter exemplo administrativo em regra CLF.

### TCU Acórdão 1.498/2026 — progresso da automação insuficientemente demonstrado

[TCU notícia oficial de 11/06/2026, TC 007.094/2025-6](https://portal.tcu.gov.br/imprensa/noticias/tcu-fiscaliza-sistema-de-concessao-automatica-de-beneficios-do-inss): fiscalização concluiu que metas de menor fila/tempo **ainda não tinham comprovação suficiente de êxito**, e o INSS encontrava dificuldades para ampliar meta de **50% de concessões automáticas**. **50% é uma meta citada**, não taxa universal observada. O TCU verificou que automatismos priorizavam dados sem pendência e não comunicavam ao requerente omissões potencialmente capazes de aumentar o benefício.

O Tribunal determinou ajustar fluxos de análise, a fim de **liberar a parcela/valor incontroverso do direito e notificar pendências capazes de elevar a prestação**. É um dado institucional sobre o desenho desejável, **não prova de implementação ou de redução observada de filas** até outubro. **A F3-B não leu o inteiro teor dos três acórdãos; esta afirmação baseia-se nos resumos institucionais oficiais, com IDs, sessão e links para decisão integral para F3-C.**

## 3. Judicialização, tempo e possibilidade de interoperabilidade

**Estudo CNJ/Insper de 2020, séries históricas:** [CNJ, *Ações previdenciárias: pesquisa registra causas da revisão judicial de decisões administrativas*](https://www.cnj.jus.br/acoes-previdenciarias-pesquisa-registra-causas-da-revisao-judicial-de-decisoes-administrativas/) analisa **9.253.045 processos administrativos** (2018–2019), **593.772 concessões decorrentes de decisão judicial** no mesmo recorte e milhões de processos judiciais históricos, encontrando relação da demora, recursos administrativos, perícia e contexto local com judicialização. **Não transportar esses números como fluxo de 2026** nem afirmar que mudança editorial no CLF causaria redução de processos.

**CNJ 2026:** [fórum de conciliação previdenciária noticiado em 2026](https://www.cnj.jus.br/forum-do-cnj-deve-fortalecer-conciliacao-em-questoes-previdenciarias/) reporta cerca de **4,5 milhões** de processos pendentes e aumento de **23%** nos novos casos de 2025 em relação a 2024 no painel. **Universo processual e momento distintos** do estoque de pedidos INSS; não somar nem comparar diretamente.

**PrevJud, nota CNJ de 26/08/2026:** [CNJ PrevJud](https://www.cnj.jus.br/inss-prevjud-acelera-resposta-judicial-e-concessao-de-beneficios/) registra **2 milhões de ordens judiciais encaminhadas** desde 2024 e **88,32% respondidas**, resultado de interoperabilidade de cumprimento. **Ordens não equivalem a processos únicos**, `resposta` não é `concessão` nem prova de mérito correto. Poderia ser indicador operacional para M06, não solução material para o RGPS M01.

## 4. O que os números não revelam — lacunas críticas

[F3B_BASE_INDICADORES_E_LIMITES_27.csv](F3B_BASE_INDICADORES_E_LIMITES_27.csv) separa **27 observações quantitativas, qualificações de auditoria e lacunas**, cada uma com fonte, período, unidade, universo, valor disponível ou `NAO_LOCALIZADO`, grau de verificação, responsabilidade e ressalva.

**Não localizados em série pública desagregada nesta pesquisa:** (a) número de requerimentos de retificação CNIS, taxa de procedência e tempo mediano; (b) motivos de negativa separados em filiação, contribuição, carência, prova, perícia e qualidade de segurado, com base em **coortes de DER**; (c) custo administrativo por requerimento por categoria e custo de erro/recálculo; (d) reversões administrativas e judiciais causadas *especificamente* por erro de cadastro; (e) comparação longitudinal consistente do tempo total DER → decisão definitiva/implantação.

**Consequência:** não há base para dizer que qualquer das arquiteturas A, B e C reduzirá, por exemplo, 20% dos indeferimentos ou 30% do contencioso. A auditoria de fonte primária encontrou **problemas reais de cadastro, prova e automação**, mas não estima efeitos de uma alteração do CLF. **Dados ausentes são Q_EMPIRICA, não zero.**

## 5. Dez hipóteses de reforma testáveis, com interface intermodular

| Hipótese | Indicador de resultado e desenho possível | Fronteira responsável |
|---|---|---|
| H01 — preservar vínculo obrigatório comprovável independentemente do CNIS | Taxa de reconhecimento de trabalho após retificação, reversões por falta de registro | M01/M06 |
| H02 — informação sobre pendências antes de concessão definitiva | Frequência de concessão inferior ao melhor direito apurado, notificação e correção | M05/M06 |
| H03 — valor incontroverso pago sem impedir revisão para cima | Duração DER→primeiro crédito e DER→decisão final por coorte, custos e reversões | M05/M06 |
| H04 — motivação explicável das decisões automáticas | Taxa de reclamações e decisões revisadas por vícios de fundamentação | M06 |
| H05 — unificar conceito de segurado sem unificar cobrança | Erros de enquadramento e efeitos fiscais, teste jurídico Lei8212/8213 | M01/M02 |
| H06 — prova plural do desemprego | Decisões sob Tema1360/STJ, intensidade de prova e decisões revertidas | M01/M06 |
| H07 — auditoria temporal da regra aplicada | Casos que confundem ADIs2110/2111 e art27-A, ou versões 2026/2027 art73-A | M05/T01/M06 |
| H08 — preservar multiligações e segurado especial | Erros de classificação rural/PSA e vínculos simultâneos com revisão material | M01/M02/M05 |
| H09 — dependência preservada conforme óbito e norma | Revisões por reconhecimento de guarda/Tema732 vs Tema1271 e prova | M01/M05 |
| H10 — acesso a histórico interoperável e contestável | Intervalo entre reclamação CNIS e decisão; taxa de acerto e erro pós-correção | M06/Dataprev |

**Método proposto para avaliação futura:** coortes de requerimentos por data DER, benefício/categoria, UF, existência de pendência CNIS, nível de digitalização, regra temporal e pessoa responsável pelo recolhimento; distinguir `tempo ao crédito`, `tempo à decisão completa`, `acerto material`, `custo` e `reversão`. Implementações em etapas, avaliação de tendências anteriores e comparação com grupos não tratados quando justificável; sem confundir mudanças de composição de pedidos com efeito de lei. Garantir anonimização e limites de LGPD. **Nenhum piloto foi executado.**

## 6. Confronto com A × B × C (F3-A)

**A — núcleo comum de sujeitos + especialidades por função:** melhora *hipoteticamente* rastreabilidade e coordenação entre registro, custeio e benefícios, se acompanhada de regras que preservem filiação pelo trabalho, prova externa ao CNIS, histórico temporário/versões e notificação das inconsistências. **Risco central:** confundir definição comum com equivalência material; precisa de tabela de exceções e aceitação de proprietários M02/M05/M06.

**B — regimes separados com capítulo de coordenação:** pode corrigir sistemas e procedimento sem refazer arquitetura material de proteção, e permitir evolução incremental. **Risco:** divergências de conceito custeio/benefício continuam, exigindo atualização contínua de remissões.

**C — unificação integral:** auditorias mostram o perigo de automatizar regras generalizantes sobre dados imperfeitos. Modelo sem revisão de titularidade contributiva, trabalho rural e dependência pode produzir erro sistemático. **Não é C1 e deve depender de programa de reforma M com análise fiscal/constitucional**. Nenhum resultado empírico permite estimar custo líquido de C.

**Resultado argumentativo:** o estudo empírico favorece **estudar A e B como candidatas com piloto de dados/cadastro e proteção**, deixando C como alternativa de alto risco jurídico-administrativo. Trata-se de **juízo de engenharia jurídica baseado em risco**, **não decisão normativa, não evidência experimental de superioridade**.

## 7. FEITO / PENDENTE / PRÓXIMO

**FEITO:** BEPS 08/2026 com **quadros 1/24/25 e definições confrontados visualmente**, 27 registros de indicadores e lacunas; TCU **2002/2024, 2591/2024 e 1498/2026** lidos por fontes institucionais; CNJ/Insper 2020 e CNJ/PrevJud 2026 identificados; diagnóstico de não comparabilidade das métricas e dez hipóteses mensuráveis. A F3-A estrangeira mantém-se separada. Nenhum dado individual, processo privado ou module alheio acessado.

**PENDENTE:** ver íntegra dos três acórdãos TCU, microdados e discriminação de motivos/retificações CNIS; bases coortizadas DER, concessão, apelação/recurso e implantação; qualidade de decisões automáticas por espécie, período e sexo/UF; F2-D conserva 14 Q de revisão conservadora; STF Tema1271, PSA, facultativo 14/16 e colisão art73-A pendentes em seus donos. **Não houve auditoria causal nem cálculo de custos reais da reforma**.

**PRÓXIMO — F3-C (e não F4/F5 ainda):** confrontar determinações específicas dos acórdãos TCU com sua implantação e com indicadores de qualidade da decisão, coletar dados por LAI/portal sobre acerto CNIS e motivos de negativa; discutir interfaces M02/M05/M06/T01. Depois, montar F4 com **duas opções formalmente rivais**, salvaguardas testadas nos 51 casos do T29.M01 e **Q empírica explicitamente retida**. F4 apenas se usuário/coordenação autorizar, sem escolha material presumida.

**Status:** F3-B documentada no escopo das fontes, F1 global ainda parcial, F2 ainda requer conciliação F2-D, F3 comparativa/empírica parcial, PR **draft**, sem merge/decisão C0/C1/M.
