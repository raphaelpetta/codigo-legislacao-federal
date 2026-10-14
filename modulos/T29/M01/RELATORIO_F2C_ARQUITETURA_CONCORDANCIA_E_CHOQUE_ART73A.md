# T29.M01 — F2-C: arquitetura subjetiva do RGPS, concordância jurídica e controle de não regressão

**Corte:** 14/10/2026 · **Estado:** F2-C preliminar; não é código executável, minuta legislativa F5 nem conclusão de equivalência C0/C1. **Issue:** [#40](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/40) · **PR:** [#41 draft](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/41) · **baseline CLF main:** `16fba172c875c7a0de388288fe70005c944021d6`. **Dono:** T29.M01; não alterar outros módulos, especialmente T24.M01/PR38 e T29.M02/M05. CF/1988 e EC103/2019 são direito vigente; CF-projeto separada.

## 1. Resultado: o que se pode unificar e o que não se pode

A **unidade de tratamento jurídico** não é simplesmente o CPF, o CNIS ou a contribuição. O enquadramento depende de **pessoa + atividade + vínculo + categoria + período de vigência**, somado a **dependente + relação + classe + prova + data de evento**. Histórico contributivo, devedor/retentor e prestações são componentes autônomos com interfaces.

**Modelo de primeira passagem:** [F2C_MODELO_ENTIDADES_E_VINCULOS.csv](F2C_MODELO_ENTIDADES_E_VINCULOS.csv), **19 entidades lógicas**, sem armazenamento de dados pessoais reais e sem implementação de software. Não implica criação de 19 categorias legais no futuro Código: o desenho representa elementos que uma norma codificada precisaria manter distintos para não alterar o direito.

**Proposta de estrutura lógica, NÃO de texto legislativo:**

```text
PESSOA FÍSICA (P01)
 ├── ATIVIDADES / SITUAÇÕES (P03) ──> VÍNCULOS (P04) ──> REGIME (P02)
 │                                     ├── CATEGORIAS POR INTERVALO (P05)
 │                                     ├── INSCRIÇÃO / CADASTRO (P07)
 │                                     ├── QUALIDADE POR INTERVALO (P06)
 │                                     ├── HISTÓRICO CONTRIBUTIVO (P08) [M02]
 │                                     └── OBRIGAÇÃO DE RECOLHER (P09) [M02]
 ├── GRUPO DE ECONOMIA FAMILIAR (P10) ──> EVENTUAL SEGURADO ESPECIAL
 ├── RELAÇÕES DE DEPENDÊNCIA (P11) ──> CLASSES/EQUIPARAÇÕES (P12)
 ├── PROVAS (P13) [M06] ──> FATOS JURÍDICOS COM REFERÊNCIA TEMPORAL
 └── EVENTOS PROTEGIDOS (P14) ──> PRETENSÃO PRESTACIONAL (P15) [M03/M04/M05]
                                      └── PROCEDIMENTO/DECISÃO (P16) [M06]

CADA REGRA/CONCLUSÃO:
 ├── FONTE + VERSÃO + PUBLICAÇÃO + VIGÊNCIA + AUTORIDADE (P17)
 ├── REGRA MATERIAL E EXCEÇÕES (P18)
 └── DIREITO ADQUIRIDO / PROTEÇÃO REMANESCENTE (P19)
```

**Chaves de prevenção de falsos equivalentes:**
- Uma pessoa pode ter vários vínculos no mesmo dia (dois empregos, ou RPPS por cargo e RGPS por atividade diferente). O número de vínculos não duplica automaticamente tempo de contribuição.
- Inscrição não é prova exclusiva de vínculo obrigatório, e o recolhimento patronal não o constitui; filiação facultativa possui regime volitivo próprio.
- Uma pessoa pode perder a qualidade sem perder a possibilidade de usar histórico contributivo em nova filiação e sem extinguir aposentadoria já aperfeiçoada.
- Qualidade, carência, base contributiva e benefício têm critérios diferentes; não reutilizar um só atributo `status_ativo` para decidir tudo.
- A classe de dependência e a prova são avaliadas na data pertinente, com proteção de deficiência, guarda, tutela e união estável. Procedimento posterior não cria automaticamente parentesco inexistente.
- Qualquer regra deve carregar **data do fato** e **versão da fonte**, inclusive se um número de dispositivo se repete no tempo.

## 2. Concordância normativa e destino

A [F2C_CONCORDANCIA_ORIGEM_CONCEITO_DESTINO.csv](F2C_CONCORDANCIA_ORIGEM_CONCEITO_DESTINO.csv) contém **34 grupos de comparação**. Cada linha identifica fontes, conceito, entidades, garantias, **dono candidato** e estado probatório; não afirma que duas normas foram cotejadas literalmente por todos os seus parágrafos ou que foram aprovadas como um único artigo CLF.

| Grupo | Normas e risco | Encaminhamento, não aprovado |
|---|---|---|
| Categorias obrigatórias | Lei 8.213 art.11 e Lei 8.212 art.12; espécies, benefícios, custeio e cronologias distintas | **M01** qualifica o segurado; **M02** retém sujeitos, bases e obrigação contributiva. Futura definição única apenas com prova de equivalência |
| Facultativo | Lei 8.213 art.13, 8.212 art.14, Decreto3.048 art.11 | Divergência de **14/16 anos** é **Q de hierarquia**, não padronização C1 |
| Segurado especial | Lei 8.213 art.11 §§8–12 e Lei 8.212 art.12 §§9–13 | Preservar todos os vetos/limites e **PSA (Lei14.119/2021)** sem presumir igual texto ou benefício |
| Prazo de graça e prova | Lei 8.213 art.15, Decreto3.048 e **STJ Tema1360** | **M01** mantém a qualidade; **M06** regula prova/rito; não exigir registro ministerial como prova exclusiva |
| Carência e recuperação | Lei 8.213 art.27-A, art.25 III e **STF ADIs2110/2111** | Nova filiação não restabelece carência de salário-maternidade invalidada; titularidade da prestação é de outro módulo, a designar |
| Dependentes e pensão | Lei 8.213 art.16, art.74 ss., EC103 art.23, STJ Tema732, STF ADIs4878/5083 e Tema1271 | **M01** dependência; **M05** pensão, duração e rateio; questão EC103 sobre guarda continua Q |
| Mandato eletivo | Alíneas **h** de 1997 e **j** de 2004 em 8.212/8.213; ResSen26/2005, Tema691 STF | Não apagar data, fonte e eficácia da contribuição de 1997 sob argumento de redações iguais |
| Direito após perda | Lei 8.213 art.102 §§1/2 e **Súmula416 STJ** | Direito adquirido e possibilidade excepcional de pensão não desaparecem por `qualidade=false` |
| Direito com número conflitante | Leis **15.371/2026 e 15.415/2026**, ambas alteram **art.73-A** da Lei8.213 | **Q intermodular prioritária de numeração e eficácia futura**, sem remapeamento de artigos pelo M01 |

**Titularidade preliminar:** o cadastro arquitetural indica **T29.M05 para pensão e auxílio-reclusão**, **M06 para procedimento** e **M04 para incapacidade/carências específicas**. **Não está ratificado o destino definitivo das normas sobre salário-maternidade/paternidade**, que atravessam proteção familiar, benefícios e procedimento. Não editar pastas vizinhas nem chamar sua localização candidata de decisão tomada.

## 3. Achado legislativo crítico de 2026: dois art. 73-A diferentes

**Comprovação em leis promulgadas e edições oficiais:**

1. A [Lei **15.371**, de **31/03/2026**, publicada no DOU de 01/04/2026](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/lei/l15371.htm), **art.8º**, acrescentou à Lei 8.213 uma Subseção VII-A de **salário-paternidade**, cujo primeiro dispositivo é **art.73-A**. **Art.14** determina que a Lei entre em vigor em **01/01/2027**. Em 14/10/2026, texto promulgado **não vigente**.
2. A [Lei **15.415**, de **25/05/2026**, publicada DOU **26/05/2026**](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/lei/l15415.htm), **art.1º**, inseriu também **art.73-A** na Lei 8.213, porém para **salário-maternidade**: prazo até 30 dias de requerimento administrativo direto; em caso de descumprimento, **concessão provisória e automática**, análise posterior para conversão ou cessação; valores provisórios irrepetíveis salvo comprovada má-fé. **Art.2º** fixa vigência na publicação: **vigente desde 26/05/2026**.

**Diagnóstico:** a colisão é de **número e local de inserção** entre dois comandos distintos, ambos expressamente promulgados, sendo um já vigente e o outro com vacatio até 2027. A ordem de promulgação e os diferentes marcos temporais são incontroversos nos textos oficiais; **o efeito intertemporal quando a Lei15.371 entrar em vigor ainda é Q jurídica**, e não está autorizada a conclusão automática de que a lei posterior de maio (15.415) revogou preventivamente a inserção futura, nem de que a lei de março (15.371) suprimirá sem mais o direito materno em janeiro.

**Consequências de arquitetura:**
- **Bloqueio G19:** identificar normas por **ato-fonte + dispositivo modificador + dispositivo de destino + vigência**, nunca apenas `Lei8213:art73-A`.
- **Bloqueio G20:** registrar norma publicada, vigente, em vacatio, revogada/suspensa e objeto de controvérsia como estados distintos.
- **Teste N02:** requerimento de maternidade em julho/2026 sob Lei15.415: prazo e concessão provisória hoje vigentes.
- **Teste N03:** pedido de paternidade em janeiro/2027: exige enfrentar colisão de dois comandos do art73-A antes de atribuir identificador normativo definitivo; a proposta de codificação poderá recomendar **saneamento formal explícito**, nunca fazê-lo editorialmente sem decisão/veículo.
- **Teste N04:** concessão provisória materna não equivale a conclusão definitiva dos requisitos, nem autoriza repetição dos valores fora da hipótese legal de má-fé.

A [compilação da Lei 8.213 no Planalto](https://www.planalto.gov.br/ccivil_03/leis/l8213compilado.htm) e a [edição atualizada da Câmara](https://www2.camara.leg.br/legin/fed/lei/1991/lei-8213-24-julho-1991-363650-normaatualizada-pl.html) já exibem o art73-A vigente de maternidade e anotam o futuro capítulo da paternidade; isso **não substitui** exame técnico da vigência de ambos nem permite inventar solução de revogação. O módulo dono da prestação e governança devem ser informados **sem alteração unilateral de seus arquivos**.

## 4. Garantias de não regressão e testes

A matriz [F2C_INVARIANTES_DE_NAO_REGRESSAO.csv](F2C_INVARIANTES_DE_NAO_REGRESSAO.csv) fixa **20 garantias de controle G01–G20**: filiação por atividade, facultativo, concorrência, inscrição, segurado especial, responsabilidade de custeio, prazos de graça, prova do desemprego, termo de perda, direito adquirido, CI pós-morte, retomada de carência, salário-maternidade após ADIs, hierarquia dos dependentes, guarda, prova familiar, PSA, mandato, colisão legislativa e identificador normativo versionado.

O [arquivo F2C_REGRESSAO_47_CENARIOS.csv](F2C_REGRESSAO_47_CENARIOS.csv) contém **todos os 47 IDs anteriores de teste** (`F2A-T01..20`, `P01..27`) com cenário, resposta prévia, garantias de preservação e ressalvas. A revisão marcou:
- **35** cenários como `PRESERVADO_COM_CONDICIONANTES`: há rota conceitual válida, mas faltam os fatos e a decisão concretos;
- **12** como `PRESERVADO_COM_QUESTAO_JURIDICA`: a rota não é automática e depende da solução de Q, especialmente idade facultativa, PSA, guarda e carência materna;
- **0** cenários omitidos ou com ID alterado. **Isso é regressão conceitual/documental; não significa que 47 benefícios tenham sido computados/concedidos, nem validação jurídica independente de cada saída.**

A matriz [F2C_TESTES_ADICIONAIS_COLISAO_2026.csv](F2C_TESTES_ADICIONAIS_COLISAO_2026.csv) registra **4 novos cenários**: mandato 2000/2006 com alínea h/j e Tema691, maternidade 2026 sob art73-A da Lei15415, paternidade 2027 na colisão art73-A e concessão provisória de maternidade. Os invariantes G18–G20, que não constavam dos antigos 47 cenários, agora também têm teste próprio.

**Validação estrutural executada:** 19 entidades, 34 concordâncias, 20 garantias, 47 regressões e 4 novos testes; nenhum ID duplicado, referência a entidade/garantia inexistente, linha malformada ou campo vazio; **todos os 47 IDs de origem foram reencontrados** nas planilhas das rodadas F2-A/F2-B. Os resultados não certificam equivalência normativa para C0/C1.

## 5. Pendências e separação de competências

- **M01 (escopo desta frente):** pessoa, vínculo, categoria, qualidade, grupo especial, classe/equiparação e definição de dependente.
- **M02/T12:** quem contribui, retém, paga; incidência, base, PSA e regularização do contribuinte individual, remuneração abaixo do mínimo, efeitos de extemporaneidade contributiva.
- **M03/M04/M05:** preenchimento dos requisitos de aposentadoria, incapacidade, pensão, carências válidas, salários-maternidade/paternidade e cálculo/duração, com **destino final de maternidade/paternidade a definir pela governança**.
- **M06:** inscrição/prova administrativa como procedimento, concessão provisória 30 dias Lei15415, instrução, recurso, eventual reembolso; não determinar inclusão de dependente apenas por documento cadastral.
- **CF/projeto CF e governança:** EC103 art23 §§4/6/7 e STF Tema1271 pendente na última consulta de 14/10/2026; DEC016 sobre veículo formal do Código único; saneamento do choque de art73-A só por mecanismo constitucional e legal apropriado.
- **F1 residual:** as 198 unidades de F1-A eram classificações funcionais, não transcrições certificadas; o art73-A duplo e alterações supervenientes reforçam por que fonte, data e identidade não podem ser reduzidas a uma única versão atual.

## 6. Próximos passos

**FEITO:** F2-C conceitual com cinco matrizes interligadas e 51 cenários (47 de regressão mais 4 novos), arquitetura de titulares e Q, identificação do art73-A duplicado em 2026.

**PENDENTE:** decisão formal sobre proprietários de salário-maternidade/paternidade; destino e eventual saneamento legislativo da colisão, interpretação intertemporal de 2027; controle de Tema1271; guarda pósEC103; idade 14/16; pagamento PSA e base contributiva; efeitos da carência do art27-A; auditoria jurídica independente e CI. Nenhuma C0/C1/M aprovada.

**PRÓXIMO — F2-D / revisão adversarial interna:** auditar a concordância das 34 linhas quanto a possíveis falsas equivalências e lacunas; exigir para cada hipótese de futura unificação **origem, versão, exceções, reserva de competência e resultado de não regressão**, com atenção especial à colidência art73-A e aos efeitos de 2027. Seguir para **F3** (comparação internacional) e **F4** (alternativas institucionais) após tornar F2 suficientemente estável; **não produzir ainda minuta F5**.

**Estado da branch:** documentação no PR #41 draft. Nenhuma alteração em `main`, T24.M01, T29.M02 ou T29.M05, nem comunicação automática presumida a outra frente; a abertura de issue central de integração fica sujeita a coordenação para não duplicar trabalhos.
