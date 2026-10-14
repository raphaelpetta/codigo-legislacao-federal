# T29.M01 — F2-C: arquitetura conceitual unificada e auditoria de não regressão

**Corte e pesquisa:** 14/10/2026. **Status:** reconstrução conceitual do direito vigente, **não minuta legal, migração de dados nem decisão C0/C1/M**.  
**Issue:** [#40](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/40) · **PR draft:** [#41](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/41) · **branch:** `modulo/T29-M01-segurados-dependentes-f0-f1-20261014` · **`main` CLF no início:** `16fba172c875c7a0de388288fe70005c944021d6`.  
**Titular:** T29.M01; T29.M02/M03/M04/M05/M06/M07 apenas interfaces; T24.M01 de outra frente/PR38. Constitucionalmente, **CF/1988 com EC 103/2019** é direito vigente; o projeto de CF alternativa não foi lido nesta rodada e não foi incorporado como norma.

## 1. Decisão de método — não fundir efeitos distintos sob o substantivo “segurado”

A pessoa física pode ser simultaneamente segurada em atividades diferentes, filiada a RPPS por um cargo e RGPS por outra atividade, ter interrupções, períodos de graça, recolhimentos em aberto e direito adquirido independente de perda posterior da qualidade. Para pensão, há também pessoa dependente, relação com o instituidor e prova na data do óbito.

**Regra estrutural proposta apenas para F2:** `Pessoa → [Atividade] → [Vínculo ao Regime] → Filiação → [Intervalos de qualidade] → Fato gerador`; em paralelo `[Obrigações/Historico contributivo]`, `[Inscrição e prova]` e `[Relações de dependência]`. A decisão sobre benefícios consulta essas dimensões e a versão normativa aplicável, mas **não é calculada por um único campo “ativo”**.

Em consequência: a filiação obrigatória não pode depender automaticamente de inscrição ou do recolhimento de terceiro; filiação facultativa tem fato constitutivo distinto; qualidade não é carência; contribuição não é prova única de trabalho; dependente não equivale a titular de benefício concedido. **Esta é uma arquitetura de conceitos e remissões jurídicas**, não proposta de banco de dados exigível pelo Estado.

## 2. Os três artefatos desta rodada

| Artefato | Conteúdo e prova | Significado jurídico |
|---|---|---|
| [F2C_ESQUEMA_CONCEITUAL_15_ENTIDADES.csv](F2C_ESQUEMA_CONCEITUAL_15_ENTIDADES.csv) | **15 entidades**, ID lógico, atributos mínimos, cardinalidade, temporalidade, proprietário e invariantes | Modelo F2, não dispositivo CLF/lei aprovada |
| [F2C_CONCORDANCIA_FUNCIONAL_56_REGRAS.csv](F2C_CONCORDANCIA_FUNCIONAL_56_REGRAS.csv) | **56 entradas = 33 regras F2-A + 23 transições F2-B**, cada uma com origem, fonte/URL já localizada, conceito, exceção, titular e categoria de auditoria | Concordância funcional **pré-F6**, não C0/C1/M |
| [F2C_AUDITORIA_NAO_REGRESSAO_47_CASOS.csv](F2C_AUDITORIA_NAO_REGRESSAO_47_CASOS.csv) | **47 cenários anteriores reavaliados contra invariantes**: 20 F2-A + 27 F2-B; **40 controles conceituais condicionais; 7 Q explicitamente retidas** | Teste de coerência F2, não resultado jurisdicional nem implementação operativa |

IDs das entidades vão de `E01` a `E15`, vinculando pessoas, regimes, atividades, vínculos, filiação, inscrição, períodos de qualidade, eventos modificadores, contribuição, eventos protegidos, dependentes, prova, prestações e versões normativas.

**Especificação de titularidade:**
- **T29.M01:** pessoa/papel previdenciário, qualificação da atividade, vínculo ao RGPS, filiação, intervalos de qualidade e relação de dependência.
- **T29.M02:** responsável pelo recolhimento, bases e competências contributivas, custeio e controvérsia de quitação pós-morte.
- **T29.M03/M04/M05:** prestações, direitos adquiridos, carência por benefício, aposentadoria, incapacidade, pensão e salário-maternidade na classificação do catálogo.
- **T29.M06:** inscrição, prova, requerimento e instrução administrativa.
- **T29.M07:** fronteira RGPS/RPPS, sem unificação de regimes.
- **T01/governança:** temporalidade, vigência, cadastros de fontes, jurisprudência, texto constitucional vigente/futuro.

**Uma ressalva essencial:** a qualidade pode depender de *mais de um vínculo* da mesma pessoa no RGPS. Cada `PERIODO_QUALIDADE (E07)` é episódio fundamentado; a **qualidade global no RGPS em determinada data é uma avaliação derivada dos episódios válidos**, não o valor de um único vínculo escolhido arbitrariamente. Encerramento de um emprego não extingue a qualidade proporcionada por outra atividade simultânea. Sem essa projeção, o modelo seria juridicamente deficiente.

## 3. Concordância F2 — fonte, conceito, ressalva, titular

O arquivo de 56 linhas usa as fontes da F2-A/F2-B como **hipóteses de localização** e registra seu status de prova (lei, decreto, precedente, Q); não declara equivalência literal. Nenhuma linha cria novo número de artigo do CLF, revoga ou funde normas.

**Seis fronteiras que tornam a fusão juridicamente não trivial:**

1. **Lei8.213 art11 × Lei8.212 art12:** ambas classificam segurados, mas **não possuem todas as mesmas exceções, numerações e efeitos**. Um conceito compartilhado só poderá ser C1 se a equivalência entre qualidade e custeio estiver demonstrada; caso contrário é **M**, decisão a ser proposta na F4. A assimetria de PSA (Lei14.119/2021) é exemplo concreto.
2. **Filiação obrigatória × facultativa:** a primeira decorre de atividade; a segunda depende de ato volitivo, inscrição, primeiro recolhimento e requisitos próprios; **idade 14 na lei e 16 no Decreto3048 ainda Q**, sem correção editorial disfarçada.
3. **Qualidade × carência:** Lei8.213 arts15 e 27-A não podem se tornar um único requisito. O STF, nas **ADIs2110/2111**, declarou inconstitucional a exigência de carência do **art25 III para salário-maternidade**, não a necessidade de prova de filiação ou todos os requisitos de todas as prestações. Remissão ao art27-A não pode reintroduzir o requisito afastado.
4. **Qualidade na morte × direito já formado:** Lei8.213 art102 e **STJ Tema21/Súmula416** admitem pensão na hipótese em que o falecido preenchia os requisitos para aposentadoria mesmo após perder qualidade. Não resumir como `qualidade=false → pensão=false`.
5. **Desemprego como extensão da graça:** Lei8.213 art15§2 e **STJ Tema1360, REsps 2.169.736/RJ e 2.188.714/MT**, julgamento **11/03/2026**, DJEN **19/03/2026**, autorizam prova idônea em vez de inscrição exclusiva no Ministério; apenas silêncio de CNIS/CTPS é insuficiente.
6. **Dependente por guarda e vigência:** a história MP1523/1996 → Lei9528/1997 → **STJ Tema732** → EC103/2019 art23 §§4/6/7 → ADIs4878/5083 → Lei15108/2025 não pode se tornar rol ahistórico. **STF Tema1271/RE1442021** discute a regra constitucional de 2019 e, na ficha consultada em 14/10/2026, só constava repercussão geral, **sem tese final de mérito**.

**Fontes de conferência desta rodada (recorte efetivamente lido/revalidado):** [Lei8.213 compilada](https://www.planalto.gov.br/ccivil_03/leis/l8213compilado.htm), [Lei8.212 compilada](https://www.planalto.gov.br/ccivil_03/leis/l8212compilado.htm), [Decreto3048 compilado](https://www.planalto.gov.br/ccivil_03/decreto/d3048compilado.htm), [STJ Tema1360 ficha oficial](https://processo.stj.jus.br/repetitivos/temas_repetitivos/pesquisa.jsp?cod_tema_final=1360&cod_tema_inicial=1360&novaConsulta=true&tipo_pesquisa=T), [STJ Tema21/Súmula416](https://processo.stj.jus.br/repetitivos/temas_repetitivos/pesquisa.jsp?cod_tema_final=21&cod_tema_inicial=21&novaConsulta=true&tipo_pesquisa=T), [STF ADIs2110/2111 decisão](https://portal.stf.jus.br/processos/detalhe.asp?incidente=1795149), [STF Tema1271 ficha](https://portal.stf.jus.br/jurisprudenciaRepercussao/verAndamentoProcesso.asp?classeProcesso=RE&incidente=6661561&numeroProcesso=1442021&numeroTema=1271). **Original MP/DOU, STJ Tema732, TJ/TRF e ato IN RFB2110 foram remetidos de rodadas anteriores e não auditados integralmente de novo aqui.**

## 4. Auditoria da não regressão — o que os 47 casos demonstram

A verificação relacionou os **20 casos F2-A e 27 F2-B** com as entidades e as 56 regras/transições mapeadas. Cada linha possui fatos, resultado prévio, salvaguarda exigida, referência jurídica e status da conclusão.

**Resultado restrito:** **40** hipóteses preservaram condição e exceção essenciais no modelo `PASSA_CONTROLE_CONCEITUAL_CONDICIONAL`; **7** permanecem `PENDENTE_POR_Q`. “Passa” significa **não foi encontrada contradição ao representar os requisitos e exceções do caso no esquema**, **não** que um direito foi reconhecido por autoridade judiciária ou que a lei já pode ser codificada C1. Não foram executados cálculo de benefícios ou pesquisa estatística.

| Teste focal | Preservação exigida | Resultado |
|---|---|---|
| F2A-T01 / F2B-P01 | Trabalho efetivo com contribuição patronal não paga mantém hipótese de filiação obrigatória | Condicional à prova |
| F2A-T02 | Facultativo de 15 anos: 14 na lei / 16 no decreto | **Q aberta** |
| F2A-T05 / F2B-P09 | Mais de 120 contribuições + desemprego comprovado, possível graça ampliada | Condicional à prova e termo do §4 |
| F2A-T06 / F2B-P10 | CNIS/CTPS sem vínculo isolados não provam desemprego involuntário | Preservado com Tema1360 |
| F2B-P19 / P20 | CI que devia pagar por si × empregado com recolhimento patronal omitido | Condicional à fonte do dever |
| F2B-P18 | Carência maternal após ADIs2110/2111; possível carência disfarçada | **Q de concretização** |
| F2A-T09 / F2B-P21 | Direito à aposentadoria aperfeiçoado em vida preserva exceção pensão após perda | Preservado, requisitos a provar |
| F2A-T14 / T15 / T16 | Guarda em 2018 × 2023 × 2025 | 2018 condicionado; **2023/2025 Q Tema1271** |
| F2A-T10 | PSA não descaracteriza por si no custeio, falta espelho literal no benefício | **Q de efeitos prestacionais** |
| F2B-P26 | Termo da perda depende da competência e vencimento corretos | **Q sobre data concreta** |

**As sete Q retidas não devem ser convertidas em resoluções automáticas:** F2A-T02, T10, T15, T16, F2B-P15, P18 e P26. São resultados da revisão conceitual, não necessariamente a lista de todas as Q jurídicas do RGPS. Um conjunto de 47 casos **não demonstra cobertura exaustiva** de categorias, contribuições ou dependentes.

## 5. Invariantes que o futuro CLF não deve violar

**I01 — Filiação independente da inscrição para segurado obrigatório:** a atividade enquadrada e provada produz filiação nos termos legais; não criar requisito constitutivo de cadastro ou quitação patronal para todos.

**I02 — Multifiliação e competência:** um segurado pode ter vínculos simultâneos; pessoa, vínculo, regime e competência não são a mesma chave. Não contar o mesmo mês de trabalho duas vezes por simples multiplicidade de contratos.

**I03 — Qualidade temporal fundamentada:** manutenção por trabalho, benefício ou graça, com prazo legal e início/fim por competência; não classificar como sem qualidade a pessoa ainda protegida por outro vínculo.

**I04 — Histórico e carência separados:** direitos contribuídos não desaparecem magicamente após perda; aplicação da carência exige benefício juridicamente válido e controle constitucional (maternidade).

**I05 — Direito adquirido:** pessoa pode ter perdido a qualidade e ainda ter aposentadoria adquirida; dependentes podem ter direito a pensão na hipótese da Súmula416.

**I06 — Responsável pelo recolhimento:** CI que devia recolher e empregado com empresa inadimplente não se equiparam para regularização post mortem; titularidade do dever é externa a M01.

**I07 — Dependência por fato gerador:** a relação familiar, o marco da morte, a legislação/interpretação correspondente e a prova devem constar separadamente; inscrição posterior não elimina relação anterior.

**I08 — Proteção de criança e deficiência:** guarda, tutela, deficiência e dependência econômica não podem ser perdidas por simplificação do rol ou mera idade; STF Tema1271 ainda Q.

**I09 — Prova não tarifada indevidamente:** onde a tese permite outros meios idôneos, como no desemprego, não exigir registro único; isto não dispensa demonstração efetiva.

**I10 — Fontes e efeitos separados:** texto da lei, edição administrativa, decreto, súmula, controle de constitucionalidade e anteprojeto são versões/níveis diferentes; **Q não é revogação**, e vigência futura não se aplica antecipadamente.

## 6. Proposta estritamente metodológica de capítulos para uma futura F4/F5

Esta estrutura é apenas **candidata**, não número de artigos ou decisão de promulgação:

- Capítulo de definições e princípios de enquadramento RGPS: filiação obrigatória, simultânea e facultativa, múltiplos regimes e exceções.
- Capítulo de categorias e regras especiais: domésticos, individuais, avulsos, especiais e peculiaridades de economia familiar, cooperativas e PSA.
- Capítulo de inscrição e prova **por remissões ao M06**: documento da filiação, cadastro, dependentes e atividade rural.
- Capítulo de manutenção/perda: art15, causas, prazos, termo, desemprego, recuperação e proteção do direito adquirido.
- Capítulo de dependentes: classes, dependência, presunções, equiparados, deficiência, prova e excludentes.
- Remissões para **M02 (contribuição)**, **M03/M04/M05 (benefícios e carência)**, **M07 (RPPS)**, T01 (direito intertemporal), CF vigente e proteção da infância.

A estrutura só poderá virar texto C0/C1 se as concordâncias jurídicas estiverem certificadas; mover obrigação contributiva entre diplomas poderá exigir **M com reserva de competência/espécie**. **Não proposto revogar Lei8.212 ou Lei8.213**; a governança ainda discute veículo do Código único (DEC016).

## 7. FEITO / PENDENTE / PRÓXIMO

**FEITO:** desenho conceitual de **15 entidades**, concordância de **56 regras/transições**, rastreio de **47 testes** e dos **dez invariantes de proteção**, sem alterar outras frentes. Fontes oficiais revisadas para Tema1360, STF Tema1271, ADIs2110/2111 e Súmula416/Tema21; nenhuma tese de mérito inventada para Tema1271.

**PENDENTE:**
- Auditoria literal completa de todos dispositivos RGPS, inclusive distinções de filiação da Lei8212/Lei8213, regulamento, efeitos de normas revogadas e futuro salário-paternidade de 2027;
- Consultas especializadas dos módulos M02/M03/M05/M06/M07 para concordância do titular definitivo, especialmente contribuições post mortem, carência de benefício e guarda;
- STF Tema1271 sem julgamento final localizado no corte; Q facultativo 14/16, PSA e IN RFB2110 versão 2026, qualificação da remuneração inferior ao mínimo e datas de perda;
- Interfaces T01 e projeto CF futura não cotejados por dispositivo nessa rodada, governança da espécie/veículo legislativo do CLF (DEC016) sem decisão final;
- A auditoria dos 47 casos **não cobre necessariamente todos os ramos do RGPS**; nenhum texto ou equivalência C0/C1/M aprovado e **CI/revisão independente/merge** pendentes.

**PRÓXIMO recomendado — F3-A:** pesquisa crítica comparada e empírica sobre (i) unificação de conceito de segurado com contribuição/benefícios separados; (ii) mecanismos de proteção de períodos sem pagamento e prova do desemprego; (iii) registro de dependência e tutela/guarda; (iv) custo administrativo e segurança jurídica do cadastro, tomando sistemas com divisão clara de custeio e cobertura. Referências estrangeiras devem ser avaliadas com cuidado sobre os limites de federalismo, financiamento e proteção brasileira; não transplantar automaticamente.

**Porta de qualidade:** para F4, apresentar pelo menos duas arquiteturas rivais testadas pelos **47 casos**, concordância original→destino por artigo que se pretenda integrar, decisão central sobre M02/M05, e lista de Q vinculante/relevante; sem isto, permanecer `MODELO_VIGENTE_DOCUMENTADO_PARCIAL` e PR draft. Nenhum M ratificado ou fusão autorizada.
