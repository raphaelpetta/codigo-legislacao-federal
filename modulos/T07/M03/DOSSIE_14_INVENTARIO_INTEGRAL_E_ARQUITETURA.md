# T07.M03 — Ciclo 14: inventário artigo por artigo da Lei 9.784/1999 e arquitetura de codificação

**ID:** CLF-T07-M03-DOS14 · **Data de consulta:** 13/10/2026 · **Situação:** F0/F1 pesquisa documental ampliada; F2 pesquisa de integração; F5 testes iniciais. **NÃO é texto codificado integral nem minuta aprovada.**  
**Fonte-base da legislação vigente:** [Câmara — Lei 9.784/1999 atualizada](https://www2.camara.leg.br/legin/fed/lei/1999/lei-9784-29-janeiro-1999-322239-normaatualizada-pl.html), conferida com [cadastro legislativo](https://www2.camara.leg.br/legin/fed/lei/1999/lei-9784-29-janeiro-1999-322239-norma-pl.html) e [Planalto](https://www.planalto.gov.br/ccivil_03/leis/l9784.htm).  
**Fonte de jurisprudência:** [STJ — Súmula 633](https://scon.stj.jus.br/SCON/sumstj/doc.jsp?b=SUMU&h=true&i=1&l=10&livre=SUMULA+INPATH%28TIPO%29+AND+633+INPATH%28NUM%29&ordenacao=-%40NUM&p=false).

## 1. O resultado e, principalmente, seu limite

`INVENTARIO_ARTIGOS_INTEGRAL_14.csv` contém **80 posições** de artigo na lei consolidada: 70 posições originais numeradas 1–70, sete intercalares `49-A–49-G` (2021), duas `64-A–64-B` (2006) e uma `69-A` (2009). **O art. 49-C é inteiramente vetado** e permanece apenas como posição histórica; há **79 posições com algum conteúdo normativo** segundo o texto oficial consultado. O número **não equivale a 79 dispositivos com vigência jurídica independente**, pois os artigos têm caput, parágrafos e incisos e alguns destes foram vetados.

**Grau de cobertura:** inventário **completo no nível de artigo/posição** do texto consolidado consultado, não no nível de todas as unidades subordinadas. Ainda faltam transcrição literal e classificação de cada inciso, parágrafo, remissão textual, efeito temporal, precedente e legislação especial. O piloto anterior já transcreveu **21 unidades** dos arts. 1º–2º (C0 textual com equivalência jurídica Q), mas este ciclo **não transcreve a íntegra dos arts. 3º–70** nem declara equivalência jurídica do resto.

**Novas matrizes:** `HISTORICO_ALTERACOES_VETOS_14.csv` — 16 entradas de publicação, retificação, adições, vetos e norma especial externa; `MATRIZ_REMISSOES_INTERDEPENDENCIAS_14.csv` — 50 nexos de remissão expressa, interdependência e jurisprudência, **amostra crítica não exaustiva**.

## 2. Arquitetura legal atual: 18 capítulos e um intercalar (XI-A)

| Capítulo vigente | Abrangência | Núcleo de integração | Resultado para novo Livro |
|---|---|---|---|
| I — Disposições gerais | 1º–2º | Âmbito, poderes em função administrativa, conceitos, princípios e critérios | **Já espelhado textualmente**, sem selo jurídico C0 |
| II — Direitos dos administrados | 3º | Ciência, acesso, petições, alegações e advogado | **Preservação integral prioritária** |
| III — Deveres | 4º | Boa-fé, colaboração, verdade | Relação com direitos e apuração |
| IV — Início | 5º–8º | Iniciativa de ofício, petições e formulários | Integração com acesso e simplificação |
| V — Interessados | 9º–10 | Sujeitos individuais, coletivos e difusos | Definição usada em art.49-B e 58 |
| VI — Competência | 11–17 | Delegação, avocação, exclusões | A remissão à reserva de competências não pode sumir |
| VII — Impedimento e suspeição | 18–21 | Imparcialidade, abstenção e recurso | Direitos processuais essenciais |
| VIII — Forma, tempo e lugar | 22–25 | Forma dos atos, dias, prazo supletivo | Não confundir prazo com art.66 |
| IX — Comunicação | 26–28 | Intimação, ciência e nulidades | Referência **expressa** do art.49-D |
| X — Instrução | 29–47 | Prova, consulta, contraditório, pareceres, medida cautelar, relatório | Evitar fusões de normas que protegem direitos diferentes |
| XI — Dever de decidir | 48–49 | Dever expresso e prazo decisório | Regra geral distinta de prazo recursal |
| XI-A — Decisão coordenada | 49-A–49-G | Instância interinstitucional, exceções e ata | **2021**, com vetos: preservar somente texto positivo |
| XII — Motivação | 50 | Hipóteses exigidas e forma do fundamento | Conectar com art.2 VII, 38 e 64 |
| XIII — Desistência e extinção | 51–52 | Disponibilidade, interesse público e exaustão | Distinguir renúncia de extinção |
| XIV — Autotutela | 53–55 | Anulação, revogação, decadência e convalidação | **Art.54 e STJ633:** risco federativo alto |
| XV — Recursos e revisão | 56–65 e 64-A/64-B | Recurso, legitimidade, súmula vinculante, revisão sancionatória | **2006**; proteger vedação de agravamento em revisão |
| XVI — Prazos | 66–67 | Dias contínuos, prazos mensais, não suspensão | Exceção de feriados sem transportar CPC automaticamente |
| XVII — Sanções | 68 | Regime mínimo e defesa | Não universalizar sobre processos coordenados, que excluem sanções |
| XVIII — Disposições finais | 69–70 e 69-A | Especialidade/subsidiariedade, prioridades, vigência histórica | **Art.69** integra a regra geral; **art.70** não se transcreve como vigência do Código |

**Índice proposto, não escolhido:** conservar, por ora, todos os grupos funcionais do texto de origem (G1–G19) no futuro **Livro do Processo Administrativo Federal**, com possibilidade de reduzir repetição **após** auditar as 80 posições e as unidades subordinadas. **Não** são 19 capítulos aprovados do Código; são grupos de rastreabilidade comparada.

## 3. Versões, acréscimos e vetos — pontos que não podem ser mascarados

1. **1999:** publicação em 01/02/1999 e retificação em 11/03/1999; conferir se mudanças influenciam espelho literal da fonte original.
2. **Lei 11.417/2006:** introduziu **art.56 §3º, art.64-A e art.64-B**; a anotação legislativa destaca **vacatio própria de três meses**. Não datar seus efeitos artificialmente de 1999.
3. **Lei 12.008/2009:** introduziu **art.69-A**, com texto positivo em caput, incisos I, II, IV e §§1º–2º; **inciso III e §§3º–4º são vetados** na fonte oficial consultada. Não criar destinos codificados a partir de texto vetado.
4. **Lei 14.210/2021:** introduziu **Capítulo XI-A e arts.49-A a 49-G**. `49-A §§2º–3º`, `49-C integral` e `49-G §2º` aparecem como **vetados** no consolidado; são evidências históricas e não disposições de direito positivo a migrar.
5. **Legislação especial:** o cadastro legislativo lista a **Lei 13.988/2020** como **norma complementar**, e não como alteração de texto da Lei 9.784. Classificação importante: mesmo quando regime especial interage com a Lei geral, não passa a ser artigo dela por anexação editorial.
6. **Superveniência:** o texto oficial atualizado é fotografia da fonte no corte; seguir monitorando legislação posterior, decisões de controle e possível derrubada de veto. Campos `VIGENTE` significam apenas posição positiva na consolidação consultada, **não validação individual exaustiva de eficácia e aplicações setoriais**.

## 4. Dependências que impedem revogar só uma parte

### 4.1. Quem é abrangido?

Art.1º caput e §1º → Administração federal direta e indireta, Legislativo e Judiciário **quando exercem função administrativa**. Art.69 → procedimentos administrativos especiais têm disciplina própria e aplicam a Lei geral subsidiariamente. O **STJ, Súmula 633**, admite a aplicação subsidiária **notadamente do prazo decadencial de art.54** a entes subnacionais **na falta de norma local específica**. Não converter esse entendimento em **competência legislativa geral nacional automática** para o futuro CLF.

### 4.2. Coerência de direitos e participação

Arts.2º, 3º, 26, 29–30, 36–38, 44–46, 50, 63–65: comunicação, ciência, provas, audiências, motivação, recursos, sigilo e impossibilidade de agravar sanções por revisão. Remover direitos expressos sob pretexto de “unificar princípios” seria reforma material **M**, não consolidação neutra.

### 4.3. Definições de competência e administração coordenada

Arts.1º §2º, 9º, 11–15, 26, 49-A–49-G: definição de autoridade não autoriza delegado a editar ato normativo ou decidir recurso em conflito com o **art.13**. Decisão coordenada mantém responsabilidade originária de cada órgão e **não** se aplica a licitações, processos sancionatórios ou decisões envolvendo autoridades de Poderes distintos (art.49-A §6º I–III). Os arts.49-B e 49-D **remetem expressamente** aos arts.9º e 26. Qualquer renumeração tem de refazer essas remissões no texto normativo aprovado.

### 4.4. Prazo e garantia temporal

Art.24: cinco dias **supletivos** para atos processuais; art.44: até dez dias para manifestação ao fim da instrução; art.49: trinta dias para decisão após instrução, prorrogáveis; art.59: prazo recursal geral de dez dias; art.66: **dias contínuos**, salvo regime especial. A uniformização automática com prazo do CPC ou com dias úteis do outro dispositivo seria **mudança de mérito**, não correção editorial.

Art.53–55 e **STJ633**: decadência e revisão dos atos administrativos. Não transformar o art.54 em regra irrestrita de decadência para quaisquer entes e quaisquer matérias.

## 5. Revisão técnica para impedir redundâncias e contradições

Um Livro codificado de processo administrativo pode usar **regras gerais uma vez**, seguidas de disposições especiais só onde acrescentem consequência normativa:
- **G — âmbito e garantias básicas**: títulos sobre objeto, sujeitos, princípios e direitos; definição jurídica coerente de `este Livro`, nunca automaticamente `este Código`.
- **E — especializações necessárias**: decisão coordenada (49-A–G), procedimentos especiais (69), prioridade processual (69-A), revisão sancionatória (65).
- **X — exceções de valor material**: art.13 (matérias indelegáveis), art.49-A §6º (exclusões da decisão coordenada), hipóteses de sigilo, exceções legais de cobrança ou renúncia de competência.
- **T — transições autônomas**: processos pendentes, prazo, atos pretéritos, início de vigência, relações consolidadas e vetos.
- **D — documentação**: tabela de concordância e matriz de precedentes sem eficácia legislativa.

**A eliminação de duplicação textual só é C1 se houver prova jurídica de que nenhum direito, exceção, sujeito, prazo ou relação de especialidade se altera.** Caso contrário, marcar `M` e exigir rito/justificativa de reforma material.

## 6. Requisitos para a primeira transposição normativa integral

- **Gate A — mapa de artigo:** 80/80 posições mapeadas; posição 49-C marcada veto integral. **ALCANÇADO neste ciclo**.
- **Gate B — unidades subordinadas:** todos parágrafos/incisos e vetos, alterações e datas cotejados com fonte, sem lacunas. **AINDA ABERTO**.
- **Gate C — espelho literal da totalidade:** até aqui apenas 21 unidades arts.1º–2º espelhadas. **ABERTO**.
- **Gate D — equivalência jurídica e remissões:** todos `Q` até exame de contexto e setor; 50 remissões na matriz são amostra crítica, não relação exaustiva. **ABERTO**.
- **Gate E — fonte e vigência:** conferir versões legislativas, DOU, retificações, vetos, leis especiais e efeitos temporais. **PARCIAL**.
- **Gate F — revisão de reforma material:** detectar lacunas, riscos de antinomia e oportunidades de modernização após fotografia de direito constante. **AINDA NÃO DELIBERADO**.
- **Gate G — revogação e veículo formal:** somente com lei-base completamente transposta, processo constitucional válido e norma revogatória expressa e eficaz; **DEC-016 PENDENTE**.

## 7. Arquivos auditáveis e próxima sequência

- `INVENTARIO_ARTIGOS_INTEGRAL_14.csv` — 80 posições, 19 agrupamentos funcionais incluindo XI-A, classificação positiva/vetada.
- `HISTORICO_ALTERACOES_VETOS_14.csv` — 16 registros de histórico legislativo e normas vinculadas.
- `MATRIZ_REMISSOES_INTERDEPENDENCIAS_14.csv` — 50 vínculos críticos.
- `PILOTO_13_ARTIGOS_1_2_LEI9784.md` + concordância anterior — transcrição literal dos dois artigos iniciais, **não** texto juridicamente migrado.

**Próximo ciclo específico:** transcrever e auditar todos os elementos subordinados começando pelos **arts.3–17**, com correspondência e exame de direitos, competência e delegação; continuar com comunicação/instrução, depois decisão coordenada, recursos e finais. Qualquer algoritmo só valida integridade; **não** validará jurisprudência, efeitos temporais ou constitucionalidade.

**DEC-001** continua a finalidade de um Código Federal juridicamente único. **DEC-016 permanece pendente**, sem presumir que um corpus indexado e documental satisfaça a promulgação una.
