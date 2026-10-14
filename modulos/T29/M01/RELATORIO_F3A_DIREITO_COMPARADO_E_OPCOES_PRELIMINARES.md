# T29.M01 — F3-A: pesquisa crítica comparada sobre filiação, proteção e arquitetura de normas

**Data de corte:** 14/10/2026. **Issue:** [#40](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/40) · **PR draft:** [#41](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/41).  
**Objeto:** comparar soluções de **Alemanha, Espanha, Portugal e Uruguai** com a orientação da **OIT**, para testar como o CLF poderia separar enquadramento/filiação, qualidade e períodos de cobertura, dever contributivo, prova/cadastro, dependência e prestação. **Esta F3 NÃO decide F4, NÃO produz minuta F5 e NÃO classifica juridicamente dispositivo como C0/C1/M.**  
**Coordenação:** F2-C usa **P19** como modelo funcional de referência *provisório*, **E15** como controle de rastreio, sem duplicar os 47 testes. Total existente **51 hipóteses distintas** (47 antigas e quatro novas). [Nota de reconciliação F2-C](NOTA_F2C_RECONCILIACAO_DUAS_TRILHAS.md).

## 1. Método e limites da comparação

Critérios: (i) **mesmo problema jurídico**, sem supor sistemas equivalentes; (ii) norma vigente e órgão institucional responsável; (iii) reconhecimento e prova de períodos sem recolhimento; (iv) distinção entre titular da proteção e devedor da contribuição; (v) tratamento de pessoas com vários vínculos, dependentes e direitos adquiridos; (vi) custo institucional, risco de perda de proteção, fraude e exigências de implementação. Seleção de países: **Alemanha** (regras gerais + livro específico previdenciário), **Espanha** (categoria jurídica de situações equiparadas à alta), **Portugal** (codificação contributiva + lei de bases e proteção dos direitos em formação), **Uruguai** (proximidade regional e retificação documentada de histórico laboral).

**Fontes primárias e institucionais, efetivamente consultadas:** 17 mecanismos mapeados em [F3A_MATRIZ_COMPARADA_17_MECANISMOS.csv](F3A_MATRIZ_COMPARADA_17_MECANISMOS.csv), indicando URL, dispositivo, tipo de evidência e ressalva. Os textos foram examinados por dispositivos/trechos específicos, **não** foi feita auditoria integral das leis estrangeiras, das suas alterações ou de decisões judiciais estrangeiras. A existência de norma **não prova causalmente** benefício social, economia administrativa ou redução de litígios.

### O limite comum
Atenção às palavras próximas que designam institutos distintos: `Versicherungspflicht`/ `Meldung` alemães, `alta` espanhola, `vinculação` portuguesa e `historia laboral` uruguaia **não são traduções da qualidade de segurado do art.15 Lei8.213**. A comparação identifica **métodos de organização**, não permite importar prazos ou requisitos para o RGPS.

## 2. Quatro experiências e lições para o CLF

### 2.1 Alemanha — regras gerais comuns sem apagar o regime das pensões

O **SGB IV §28a** impõe ao empregador a comunicação de início/fim e fatos relevantes do trabalho segurado; **§28e(1)** atribui, como regra, ao empregador o pagamento das contribuições sociais globais do empregado. A divisão em livros permite distinguir obrigações de cadastro/custeio das prestações de aposentadoria e sobrevivência, tratadas no **SGB VI**.

O **SGB VI §56** reconhece períodos pela criação de filhos nos primeiros três anos, sob condições de atribuição e exclusões; **§58** distingue `Anrechnungszeiten` (períodos creditáveis) em determinadas situações de doença, maternidade e desemprego, e há normas específicas para pensões de sobrevivência (§§46–48). Isso é **diferente** de simplesmente manter qualidade durante uma graça. A proteção não precisa ser reduzida ao pagamento efetivo no último mês, porém os requisitos podem ser específicos à prestação e ao tempo de aposentadoria.

**Fontes oficiais:**
- [SGB IV §28a](https://www.gesetze-im-internet.de/sgb_4/__28a.html), [§28e](https://www.gesetze-im-internet.de/sgb_4/__28e.html);
- [SGB VI §56](https://www.gesetze-im-internet.de/sgb_6/__56.html), [§58](https://www.gesetze-im-internet.de/sgb_6/__58.html), [índice de §§46–48](https://www.gesetze-im-internet.de/sgb_6/).

**Transferência plausível:** técnica editorial `livro geral de sujeitos/registro, regras especiais de tempo e benefícios`, capaz de preservar o trabalhador mesmo diante da inadimplência patronal **nos termos da lei brasileira**, sem importar direitos alemães à aposentadoria automaticamente. **Risco de transplante:** criar créditos previdenciários por cuidado de filhos à semelhança alemã seria **reforma material M com impacto financeiro e constitucional**, não simples consolidação. O regime alemão de registro do desemprego não revoga o **STJ Tema1360** e a prova brasileira.

### 2.2 Espanha — alta e situações asimiladas: proteção por razões diferentes

A **LGSS espanhola (Real Decreto Legislativo 8/2015)**, no **art.144(1)**, vincula o nascimento do dever de contribuição ao começo da prestação de trabalho, ressalvado o próprio efeito jurídico da solicitação de afiliação/alta. O **art.166** regula situações equiparadas à alta: desemprego total durante recebimento de prestação, certos períodos de férias e hipóteses delimitadas de convênio especial, com efeitos **apenas para contingências e condições determinadas**. O glossário da Seguridad Social explica que o convênio especial tem contribuição a cargo do próprio interessado para coberturas específicas, entre elas aposentadoria e morte/sobrevivência, com condições próprias.

**Fontes oficiais:** [BOE consolidado LGSS, arts.144 e 166 (corte documental 31/07/2026)](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724&p=20260731&tn=0) e [Seguridad Social, glossário convenio especial](https://www.seg-social.es/wps/portal/wss/internet/Glosario/11976).

**Transferência plausível:** modelar `episódios de proteção com fundamento específico` — atividade, prestação, graça, convênio — mantendo requisitos por espécie. **Risco:** as situações asimiladas espanholas **não** dão direito universal idêntico a todas prestações; criar categoria geral de equiparação com cobertura integral, inclusive pensão, poderia aumentar ou reduzir direitos conforme redação e seria M. O Brasil já dispõe de filiação facultativa e períodos de graça; requer estudo do **ganho marginal** antes de introduzir figura espanhola nova.

### 2.3 Portugal — lei de bases + código contributivo + direitos adquiridos

A **Lei 4/2007**, arts.23–26, distingue **sistema de proteção social de cidadania, sistema previdencial e complementar**. Seus **arts.98–99** tratam de sistema nacional de informação, troca de dados e identificação, enquanto **art.100** protege direitos adquiridos e em formação, prazos de garantia cumpridos e parâmetros relevantes de pensões anteriores. Isso fornece uma referência de **transparência e direito intertemporal explícito**.

O **Código dos Regimes Contributivos**, da Lei 110/2009, arts.24–29, disciplina categorias de trabalhadores remunerados, exclusões circunscritas à **atividade coberta por outro regime**, proteção por eventualidade e **comunicação da admissão pelo empregador**. Arts.132–133 tratam especificamente de independentes. O Código contributivo não deve ser confundido com a lei total dos benefícios.

**Fontes oficiais:** [Lei 4/2007 no Diário da República, arts.23,98–100](https://diariodarepublica.pt/dr/detalhe/lei/4-2007-522781); [Lei 110/2009 consolidada, arts.24–29, 132–133](https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34514575).

**Transferência plausível:** prever **base conceitual comum com titularidade jurídica delimitada**; manter custeio e benefício separados, e **disposições transitórias de proteção**. **Risco:** o Brasil tem RGPS, RPPS federativos e regime de assistência, além de diferentes espécies de lei, de modo que uma unificação indiscriminada sob mesma numeração e espécie colidiria com a governança e com DEC-016 do CLF. O modelo português **não determina** qual espécie normativa brasileira deve ser usada.

### 2.4 Uruguai — história laboral corrigível por prova, não cadastro infalível

O **BPS** registra em história laboral nominada serviços e remunerações desde **01/04/1996**; mantém procedimento de **reconhecimento de anos trabalhados** faltantes, exigindo documentos conforme se trate de empregado ou não dependente. Para períodos anteriores a abril/1996, permite **reconstrução documental** com apoio de empresas e de diversos meios de prova. A orientação de 2026 especifica prazos de solicitação para gerações e extensões: esses prazos **não devem ser transplantados** ao Brasil sem estudar impactos sobre acesso.

**Fontes oficiais:** [BPS histórico nominativo](https://www.bps.gub.uy/11438/), [reconhecimento](https://www.bps.gub.uy/11452/reconocimiento-de-servicios.html), [reconstrução pré-1996](https://www.bps.gub.uy/15430/reconstruccion-de-la-historia-laboral.html), [cronograma e normas 2026](https://www.bps.gub.uy/20542/registro-de-anos-trabajados.html).

**Transferência plausível:** reforçar **procedimento formal de contestação e correção do CNIS**, com prova documentada, histórico de alterações, transparência ao segurado e mecanismo de decisão/impugnação (titular T29.M06); em M01 a qualificação por atividade não deve nascer somente do cadastro. **Risco:** impor prazo decadencial semelhante ao uruguaio para reconstruir trabalho antigo poderia **restringir proteção** no RGPS; é potencial M, não ajuste C1. Não inferir da existência do serviço uruguaio sua eficácia em reduzir litígio ou fraude.

### 2.5 OIT — pluralidade de instrumentos e piso de proteção

A [Recomendação nº 202/2012 da OIT](https://www.ilo.org/resource/ilo-social-protection-floors-recommendation-2012-no-202) orienta pisos nacionais de proteção à saúde e renda em infância, idade ativa e velhice, **sem impor única forma de administração ou financiamento**. A [FAQ da OIT sobre Convenção 102](https://www.ilo.org/frequently-asked-questions-social-security-minimum-standards-convention) destaca mecanismos contributivos e não contributivos complementares.

A OIT estima em seu [Relatório Mundial de Proteção Social 2024–2026 (números de 2024)](https://www.ilo.org/resource/article/world-social-protection-report-2024-26-figures) **52,4%** da população mundial coberta por ao menos **uma** prestação de proteção social — **não** por todas as contingências. A cifra é **global e descritiva**, sem estabelecer que um modelo de codificação cause maior cobertura, e não substitui estatísticas brasileiras de CNIS, acesso e litigiosidade.

**Para CLF:** evitar que simplificação do seguro contributivo gere exclusão silenciosa de pessoas que necessitam de assistência e proteção do Estado. Entretanto, **não absorver BPC/SUAS dentro das regras do RGPS** por simples fusão conceitual. Recomendações da OIT e escolhas constitucionais específicas requerem qualificação distinta.

## 3. Comparação de três arquiteturas rivais para estudo F4

| Arquitetura | Como seria no CLF | Ganho possível | Risco primário | Diagnóstico F3 (não decisão) |
|---|---|---|---|---|
| **A — núcleo comum e especialidade por função** | M01 define sujeitos/filiação, qualidade e dependência; M02 custeio; M03–M05 benefício; M06 prova e processo; M07 RPPS | Evita conflito conceitual e mantém efeitos diferenciados com remissões rastreáveis; semelhante à técnica por livros do SGB, **não à identidade normativa alemã** | Conceitos de mesma palavra podem ter alcance diferente; risco de falsa equivalência C1 | **Candidata forte para F4**, mas só após auditoria do inventário e aprovação das interfaces |
| **B — regimes separados com capítulo de coordenação** | Mantém mais de uma matriz legal de custeio e prestações, com catálogo de definições e remissões expressas | Menor transformação formal imediata e menos riscos ao financiamento; aproxima-se de organização portuguesa | Mantém duplicações e exige coordenação constante de alterações futuras | **Alternativa conservadora** com proteção de transições |
| **C — unificação integral de filiação, custeio e benefícios** | Todas regras consolidadas num único bloco e conceitos pretensamente idênticos | Pode reduzir dispersão textual e pesquisa, se sustentada por ampla reorganização | Confusão de segurado especial/PSA, dever de CI, carência, RPPS e guarda; alto risco de reforma M involuntária | **Não recomendar como C1**; exige programa M específico e avaliação constitucional/fiscal |

A opção A **não é automaticamente a melhor em custo ou desjudicialização**; essa vantagem seria hipótese empírica a testar. A opção B pode oferecer segurança jurídica incremental, enquanto a C exigiria robusta justificativa de reforma material. Os sistemas estrangeiros **não** fornecem experimento causal que escolha a opção vencedora brasileira.

## 4. Matriz de riscos de transplantação e indicadores que faltam

**Riscos jurídicos (prioridade):**
1. **Segurado especial/PSA:** uma definição única retirada de apenas uma das Leis 8.212/8.213 perderia ressalvas e prova rural.
2. **Facultativo de 14/15 anos:** a discrepância lei/decreto deve continuar Q, sem importar corte de idade de país estrangeiro.
3. **Desemprego:** reconhecer cobertura em episódios por fonte, mas preservar **STJ Tema1360** — meios idôneos além de registro estatal; não aceitar CNIS/CTPS vazio isolado como prova suficiente.
4. **Maternidade:** não reintroduzir carência derrubada nas **ADIs2110/2111** sob nome de tempo de filiação ou convênio voluntário; comprovação real continua necessária.
5. **Contribuinte individual pós-óbito:** segregar responsabilidade contributiva de empregado e CI antes de permitir/restringir regularização.
6. **Dependência e guarda:** **Tema732/STJ**, STF ADIs 4878/5083, **EC103 art23§6 e Tema1271 ainda Q** — não copiar regimes estrangeiros familiares sem a Constituição brasileira.
7. **Lei 15.415/2026 × Lei 15.371/2026:** dois dispositivos com mesmo número **art.73-A** e diferentes marcos de eficácia 2026/2027: resolver por fonte/versão/efeito, não por sobrescrita da versão "mais recente". Interface **M05/M06/T01**, não solução unilateral do M01.
8. **Direitos adquiridos e em formação:** a técnica portuguesa estimula cláusulas transitórias expressas; Lei 8.213 art102 e STJ Súmula416 não podem desaparecer.

**Indicadores brasileiros que precisam de coleta antes de F4 substantiva:** erros de CNIS corrigidos e tempo para correção; percentual de indeferimentos por falta de prova de vínculo versus falta de recolhimento; incidência de revisões judiciais; proporção de trabalhadores intermitentes/informais; concessões durante período de graça; segurados especiais sem prova rural formal; custo por requerimento e custos de interoperabilidade; efeitos sobre gênero e famílias de baixa renda. **Nenhum valor é inferido nesta F3; ausência de dados é Q_EMPIRICA.** A avaliação causal de reformas exige desenhos mais fortes que correlação entre países.

## 5. Instrumentos de governança para as próximas decisões

**F3 concluída no recorte de organização jurídico-institucional, não pesquisa comparada exaustiva de todos benefícios ou países.** O modelo P19 da F2-C, a concordância de 34 fontes e os **51 testes distintos** seguem como material de entrada. A trilha E15/56 regras/47 testes foi preservada como auditoria e não aumenta contagens artificialmente.

**PENDENTE para F4:** revisão independentemente fundamentada de equivalências de dispositivos das Leis8.212/8.213; parecer dos donos M02/M05/M06 e T01 sobre fronteiras, crédito contributivo e art73-A; cotejo CF vigente/projeto separado quando se cogitar alteração M; colher dados administrativos brasileiros e estudo de impacto; validar direitos em todos 51 casos, sobretudo os **12 sinalizados pela trilha P** e Q adicionais E. Nenhuma arquitetura decidida pelo usuário, nenhuma classificação C0/C1/M ratificada.

**PRÓXIMO recomendado — F3-B ou F4-A apenas se houver base**: estudo brasileiro de implementação (CNIS/prova/tempo administrativo/litigiosidade) e testes comparativos A×B×C com matriz de custos e riscos **qualitativos**, sem alegar ganho empiricamente demonstrado. O PR permanece **draft** e `main` não foi alterada.
