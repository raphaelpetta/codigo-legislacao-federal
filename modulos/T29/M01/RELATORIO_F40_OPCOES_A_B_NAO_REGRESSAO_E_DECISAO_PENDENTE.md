# T29.M01 — F4-0 | Alternativas arquiteturais condicionais A/B para sujeitos do RGPS

**Data de corte:** 14/10/2026 · **Status:** PROPOSTAS DE ARQUITETURA, **NENHUMA ESCOLHIDA OU RATIFICADA** · **Issue** [#40](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/40) · **PR** [#41 (draft)](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/41). Base `main` do CLF observada: `16fba172c875c7a0de388288fe70005c944021d6`. CF/1988 e EC 103/2019 são direito vigente; CF alternativa não se presume promulgada. **Nenhum artigo do CLF foi redigido nesta rodada.**

**Titular desta pesquisa:** T29.M01. **Interfaces necessárias e não editadas:** M02 custeio/encargos; M03 aposentadorias; M04 incapacidade; M05 prestações familiares/pensão e salário-maternidade; M06 instrução/cadastro; M07 RPPS; T01 fontes, vigência e consolidação; arquitetura central/DEC-016.

## 1. O problema de escolha — único Código não significa conceito único de efeito

**Premissas vinculantes de governança:** [DEC-001](../../../governanca/04_REGISTRO_DE_DECISOES.md) escolheu **um Código da Legislação Federal tematicamente integrado**; [DEC-004/006/007/016](../../../governanca/04_REGISTRO_DE_DECISOES.md) mantêm espécie, competência, localização normativa, rastreabilidade e reforma substantiva sob controle. **As duas arquiteturas abaixo são estruturas internas de um Código integrado**, não propostas de voltar a manter leis autônomas como produto final.

[LC nº 95/1998, art. 13, §§1º–3º, e art. 14](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp95compilado.htm): consolidação pode mudar divisões/ordem/numeração e fundir normas **repetitivas ou de valor normativo idêntico**, desde que **preserve conteúdo e alcance**; incorporações exigem tratamento formal das leis incorporadas e justificativas de supressão. Daí não se conclui que toda enumeração parecida da Lei 8.212 e da Lei 8.213 seja idêntica, nem que seja legal editar dever contributivo por alteração de conceito de benefício. O veículo normativo do Código único **permanece DEC-016 pendente**; revisão de CF vigente e eventual Constituição futura é assunto de governança.

**Problema jurídico central:** sujeito do RGPS pode ter várias atividades/vínculos simultâneos e diferentes obrigações de recolhimento. Filiação, inscrição, qualidade em dado momento, carência, histórico contributivo e benefício **não são sinônimos**. O [art. 15 da Lei 8.213](https://www.planalto.gov.br/ccivil_03/leis/l8213cons.htm) mantém qualidade durante vários períodos de graça; [Tema 1.360/STJ (julgado 11/03/2026)](https://processo.stj.jus.br/repetitivos/temas_repetitivos/pesquisa.jsp?cod_tema_final=1360&cod_tema_inicial=1360&novaConsulta=true&tipo_pesquisa=T) admite prova do desemprego por outros meios idôneos, mas não só pela ausência de registros no CNIS/CTPS. Qualquer arranjo deve preservar essas diferenças.

## 2. Opção A — núcleo comum de qualificação subjetiva com especialidades explícitas

**Desenho:** núcleo no T29.M01 estabelece papéis `pessoa`, `segurado obrigatório/facultativo`, `vínculo`, `atividade`, `período de qualidade` e `dependente`, mas **não produz automaticamente obrigação tributária ou direito prestacional**. M02 define sujeito passivo/recolhimento/base; M03–M05 definem espécie, carência constitucionalmente válida e prestação; M06 define prova, registro e procedimento; M07 conserva RPPS; T01 conserva vigência e autoridade das fontes.

**Operacionalização candidata dentro do Código único** (não capítulos aprovados):
- núcleo conceitual: alcance por atividade, filiações simultâneas, critérios gerais e restritos de inscrição voluntária;
- capítulos funcionais de categorias/especial e qualidade temporal com exceções expressas;
- vínculo familiar/dependência com classes, requisitos, presunções e datas de evento;
- disposições **remissivas delimitadas** para custeio/prestação/inscrição, jamais regra genérica de prevalência não aprovada.

**Vantagens como hipótese:** menor duplicação textual, linguagem consistente e modelo apto a registrar múltiplos vínculos e grau de proteção sem confundir todos os efeitos. **Risco específico:** um conceito geral absorver exceção do segurado especial, equiparação de guarda, responsabilidade de CI pelo próprio recolhimento ou regra de prova e criar **reforma M disfarçada de C1**. A obrigação de custeio não se torna indiferenciada só porque os sujeitos são descritos num núcleo comum.

**Regra de exceção sem perder identidade:** em caso de dois dispositivos de mesma palavra e consequência diferente, núcleo definirá apenas **interseção de conteúdo demonstrado**; a diferença será texto especial mantido no módulo proprietário, ou Q até confronto literal e temporal concluído. Qualquer nova obrigação/benefício ex novo dependerá de decisão M formalmente aprovada e análise de impacto.

## 3. Opção B — blocos funcionais com conceitos coordenados e remissões

**Desenho:** dentro de **um único CLF**, conservar blocos completos por função (enquadramento/qualidade em M01, custeio M02, benefícios M03–M05, processo M06, RPPS M07). Cada bloco expõe o alcance de sua definição e regra de exceção; um capítulo de coordenação indica quando dois termos são equivalentes **e quando não são**.

**Operacionalização candidata:**
- dispositivos atuais de custeio e prestações teriam destinos primários distintos **no mesmo Código**, com um índice de correspondências e referências;
- conceitos semelhantes podem permanecer repetidos quando seus efeitos/alcances divergem; a duplicação só é fundida após prova de equivalência;
- mudanças futuras devem revisar dependências e referências a outros módulos, com vigência distinta de cada regra e auditoria de impactos.

**Vantagens como hipótese:** estratégia conservadora de transposição; menor probabilidade de atribuir incidentalmente ao segurado de benefício uma obrigação contributiva, ou de apagar proteção por exceção. **Risco específico:** persistir redundância, multiplicar remissões órfãs, dificultar leitura de pessoas com vínculos simultâneos e manter duas descrições que se afastam por reformas futuras.

**Importante:** B **não** mantém as Leis 8.212/8.213 juridicamente autônomas como produto final do CLF (isso contrariaria DEC-001). Trata-se de **localização interna distinta**, com revogações formais e instrumento legislativo competente **somente na fase de implementação aprovada**; na pesquisa, as leis vigentes permanecem vigentes.

## 4. Comparação e porta de escolha

| Critério | A: núcleo comum + exceção por módulo | B: blocos especializados coordenados |
|---|---|---|
| Unidade semântica | Alta *se* cada termo geral preservar todos os efeitos comprovados | Moderada; alcance delimitado por bloco e remissões |
| Risco de reforma acidental | Alto em categorias/filiação/carência se generalização sem ressalva | Menor na migração inicial, mas não zero |
| Complexidade de remissões | Alta nas regras especiais | Alta na coordenação dos blocos |
| Manutenção futura | Requer governança rígida de exceções e conceito-base | Requer governança rígida contra conceitos divergentes |
| Não regressão | Possível apenas com concordância literal e exceções | Possível apenas com concordância literal e harmonização de remissões |
| Exigência institucional | Acordo entre M01/M02/M05/M06/T01 antes de definição comum | Acordo dos mesmos módulos quanto a fronteiras e linguagem de coordenação |
| Custo administrativo e impacto fiscal | **Não estimados** | **Não estimados** |
| Estado | **HIPÓTESE F4-0** | **HIPÓTESE F4-0** |

**Terceira opção C de F3-A** (fusão integral de conceitos, custeio e prestações) permanece apenas contraponto de **risco jurídico alto**; esta F4-0 foi deliberadamente limitada às candidatas A e B, sem excluí-la por decisão do usuário.

## 5. Cotejo técnico executado (não simulação de artigo F5)

Foram produzidos dois artefatos de análise, **reutilizando** e **não duplicando** o histórico F2-C:

1. [F40_ENSAIO_A_B_51_CASOS_102_COTEJOS.csv](F40_ENSAIO_A_B_51_CASOS_102_COTEJOS.csv): **51 casos distintos da F2-C × 2 opções = 102 confrontos conceituais**. Cada linha inclui ID do caso, garantias G, reserva da revisão F2-C, risco próprio da opção, mecanismo de preservação e titular de revisão. **27 casos por opção** resultaram em `COMPATIBILIDADE_CONDICIONAL`, **9 por opção** em `COMPATIBILIDADE_CONDICIONAL_ALTO_RISCO` e **15 por opção** em `Q_JURIDICA_RETIDA_SEM_DECISAO`. Esses são **estados de desenho** determinados a partir das salvaguardas e reservas existentes, **não declarações de que texto legislativo foi aprovado, nem prova de superioridade empírica**. Todas as **20 invariantes G01–G20** da matriz de não regressão estão referenciadas no conjunto.
2. [F40_DESTINOS_CONCEITUAIS_A_B_34_ORIGENS_68.csv](F40_DESTINOS_CONCEITUAIS_A_B_34_ORIGENS_68.csv): **34 entradas de origem normativa da F2-C × 2 opções = 68 destinos funcionais candidatos**. **13 origens por opção permanecem Q** de equivalência/similaridade; **11 por opção** são somente localização conceitual de norma conhecida e **10 por opção** demandam validação de outras interfaces. **Nenhum destino recebeu número de artigo CLF, fusão literal, revogação ou classificação C1/M aprovada**.

**Interpretação da contagem:** 102 é o número de **cotejos de arquitetura**, **não 102 novos casos hipotéticos**. Os 51 casos são os mesmos de F2-C (47 de rodadas iniciais + N01–N04). Da mesma forma, os 68 destinos não são 68 disposições positivas novas nem equivalências certificadas. A revisão E15 de 47 casos continua controle cruzado, não outros 47.

### Garantias cujo descumprimento barrará qualquer arquitetura

**Categoria e contribuições:** G01 filiação obrigatória pela atividade, G02 faculdade com requisitos próprios, G03 múltiplos vínculos/RPPS, G04 inscrição não constitutiva universal, G05 economia familiar, G06 M02 como sede de dever contributivo, G11 diferença CI de recolhimento próprio e empregado, G17 PSA com assimetria entre as leis, G18 mandato eletivo e fatos 1997/2004.

**Qualidade e prova:** G07 períodos de graça conforme art.15, G08 [Tema1.360/STJ](https://scon.stj.jus.br/jurisprudencia/externo/informativo/?acao=pesquisarumaedicao&from=feed&livre=0881.cod.), G09 cálculo de termo da perda com vencimento, G10 direito adquirido/Lei8.213 art102/[Súmula416/STJ](https://scon.stj.jus.br/SCON/sumstj/toc.jsp?sumula=416.num.), G12 recuperação de filiação não é carência válida, G13 carência materna afastada pelas ADIs 2.110/2.111.

**Dependência e direitos futuros:** G14 classes de dependentes não equivalem à própria pensão; G15 proteção de guarda com recortes 1996/2019/2025 e Q sobre STF Tema1.271; G16 prova familiar e união estável; G19 **colisão de art.73-A** entre [Lei15.415/2026 (salário-maternidade, publicada 26/05/2026)](https://www2.camara.leg.br/legin/fed/lei/2026/lei-15415-25-maio-2026-799179-publicacaooriginal-179514-pl.html) e [Lei15.371/2026 (salário-paternidade, eficaz em 01/01/2027)](https://www2.camara.leg.br/legin/fed/lei/2026/lei-15371-31-marco-2026-798908-publicacaooriginal-178711-pl.html), sem presumir revogação/renumeração; G20 fonte e vigência devem acompanhar sempre o conteúdo.

### Questões jurídicas que continuam **Q**, qualquer que seja o arranjo

- idade para facultativo: **14 na lei / 16 no regulamento**; não resolver por simples uniformização;
- PSA da Lei8.212 art12 §9 VIII e falta de espelho idêntico na Lei8.213 art11 §8; não criar efeito prestacional/contributivo geral;
- guarda pós EC103 art23 §6 sob Tema1.271/STF; não atribuir tese final sem verificação;
- salário-maternidade: efeitos de STF ADIs2.110/2.111 e art27-A/caráter contributivo, sem reinstaurar carência inconstitucional;
- termo exato de perda de qualidade, créditos inferiores ao salário mínimo, retorno e carência por espécie;
- CI post mortem x empregado com recolhimento patronal ausente;
- colisão de numeração e vigência dos dois art.73-A criados em 2026;
- localização legislativa e tipo de instrumento para CLF integrado sob DEC-016.

## 6. Qual é a escolha de menor arrependimento? Apenas uma hipótese de pesquisa

**A** promove mais unidade conceitual e facilita o desenho modular já proposto, **desde que as definições gerais não criem automaticamente efeitos de M02/M05/M06**. **B** preserva melhor diferenças documentais durante a migração, **mas** corre risco de congelar redundância e incoerência no Código de apresentação unificada.

Uma **sequência evolutiva candidata** (que NÃO equivale a aprovar A ou B) seria:
1. auditar origens dentro de blocos B sem alterar conteúdo;
2. verificar equivalências **literalmente, funcionalmente e temporalmente**, inclusive casos G17/G19 de fonte conflitante;
3. promover ao núcleo A apenas conceitos já auditados, deixando as exceções de custeio/prestação com seus titulares;
4. quando diferenças reclamarem expansão/restrição de direitos, abrir **decisão material M** separada, com impacto e espécie própria.

Isso descreve estratégia de gerenciamento de risco, não voto ou opção normativa aceita. **Condições para escolha:** revisão independente do conjunto de casos e concordâncias, manifestação de M02/M05/M06/T01, DEC-016, matriz de efeitos e teste de custos/procedimentos quando houver mudança M. Não há dados SUIBE acessíveis que demonstrem impacto causal sobre indeferimentos/eficiência.

## 7. FEITO / PENDENTE / PRÓXIMO

**FEITO:** F4-0 **com duas opções explícitas e rivais**, **102 cotejos condicionais** dos 51 casos, **68 hipóteses de destino** para 34 origens e análise de riscos, observando 20 invariantes. Fontes legais e do STJ oficiais revisadas em 14/10/2026, sem reabrir F1 nem fazer nova tabulação inacessível do SUIBE.

**PENDENTE:** avaliação literal de todas as unidades para mostrar identidade de efeitos; harmonização oficial com módulos M02/M05/M06/T01 e G18/G19; F2-D de revisão adversarial independente ainda não concluída nesta linha; dados SUIBE e eventual LAI **não protocolada**; ausência de estimativas de custo/resultado não pode ser substituída por números teóricos. Nenhum artigo de lei proposto, minuta de CLF ou decisão C0/C1/M aprovada.

**PRÓXIMO — F4-1:** produzir matriz **da prova de equivalência** para um conjunto mínimo de origens (Lei8.213 arts10–17 versus Lei8.212 arts12–14, 30), por blocos subordinados a M02/M05 e temporalidade. Para as hipóteses mais difíceis (segurado especial/PSA, guarda, facultativo, maternidade, art73-A), submeter pedido de decisão intermodular central, sem resolver por edição. Se, e somente se, houver ratificação e auditoria jurídica suficiente, preparar versões alternativas F5 sob os mesmos testes, ainda sem inferir economia causal.

**Regras de conclusão:** A/B permanecem `HIPOTESE_F4_0_NAO_RATIFICADA`; `main` intacta, PR draft, nenhum módulo vizinho ou CF-projeto editado.
