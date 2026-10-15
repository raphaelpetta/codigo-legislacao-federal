# T25.M01 — Ciclo 05: âmbito das regras gerais penais, subsistemas e acervo histórico de 1984

**Corte de consulta:** 14/10/2026, fuso de Brasília. **PR:** [#32](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/32) (rascunho), [issue #31](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/31). **Baseline `main`:** `16fba172c875c7a0de388288fe70005c944021d6`. **Estágios:** F1 das interações selecionadas, F2 parcial e F4 comparação de alternativas **sem decisão material**, nenhuma redação de artigos CLF aprovada.

## 1. Resultado novo: cadeia autêntica identificada, não conferida

A fonte primária do objeto da reforma foi **localizada**, no acervo mantido pela Imprensa Nacional:
- pasta [Seção 1, ano de 1984](https://incombeta.in.gov.br/web/dou/dou/-/document_library/kcmautn6AnNs/view/421773);
- arquivo **`DO_1_19840713_135.PDF`**, datado de **13/07/1984**, edição 135, [ficha documental da Imprensa Nacional](https://incombeta.in.gov.br/web/dou/dou/-/document_library/kcmautn6AnNs/view_file/432123), com PDF de cerca de **14,9 MB**;
- localização da Lei 7.209/1984 no diário: DOU **Seção 1, p. 10.217, col. 1**, segundo [ficha oficial do Senado](https://legis.senado.leg.br/norma/549085) e [Câmara](https://www2.camara.leg.br/legin/fed/lei/1980-1987/lei-7209-11-julho-1984-356852-norma-pl.html).
- Para controle auxiliar existe [anexo da Lei 7.209/1984 no Planalto (PDF histórico da tabela estrutural)](https://www.planalto.gov.br/ccivil_03/leis/1980-1988/anexo/ANL7209.pdf), **que é apenas índice da Parte Geral, não o texto dos arts.1º–12**.

**Limite estrito de prova:** o acervo oficial foi navegado até a ficha da edição, mas o arquivo integral de aproximadamente 14,9 MB **não pôde ser descarregado nem examinado visualmente**. Portanto, esta rodada NÃO demonstrou o teor do fac-símile de 13/07/1984. Continuam em `Q` as diferenças vistas nas versões eletrônicas da Lei 7.209/1984 nos arts. 3º (`embora, decorrido`), 4º (`praticado a crime`) e 12 (`aplicam especial se`). A semelhança de versões de Câmara, Planalto e Senado **não prova erro na impressão original**: cópias digitais podem ter origem comum. Não alterar o espelho C0-T baseado no texto compilado moderno sem cotejo da publicação autêntica.

**Tarefa viabilizada, ainda pendente:** abrir/baixar esse exemplar específico e inspecionar a página 10.217 e seguintes; fotografar/assinalar a localização de cada dispositivo contestado; registrar no CSV texto do DOU versus transcrição informatizada e evolução editorial com data.

## 2. Relações entre direito penal comum, contravencional, militar, eleitoral e setorial

Arquivo [`MATRIZ_RELACOES_REGIME_GERAL_CICLO05.csv`](MATRIZ_RELACOES_REGIME_GERAL_CICLO05.csv): **16 relações artigo-a-artigo** classificadas por hipótese jurídica e indicação de fonte oficial. Não são 16 leis nem 16 exceções. A matriz diferencia **verdadeira especialidade quanto à aplicação penal (arts.1º–12)**, remissão repetitiva, dispositivo de outra parte material, capítulo processual/executório e sistema penal especializado autônomo.

### 2.1. Contravenções: lei de introdução e exceções claras

- [DL 3.688/1941, arts. 1º–4º](https://www.planalto.gov.br/ccivil_03/decreto-lei/del3688.htm): o art.1º manda aplicar regras gerais do CP às contravenções salvo regra própria. O art.2º limita a aplicação da lei brasileira às contravenções no território nacional: **exceção territorial efetiva** à aplicação usual da extraterritorialidade dos crimes. O art.4º não pune tentativa de contravenção, mas se conecta ao **CP art.14 (T25.M02), fora do recorte T25.M01**; não inflar contagem de derrogações aos arts.1º–12.
- [DL 3.914/1941, art.1º](https://www.planalto.gov.br/ccivil_03/decreto-lei/del3914.htm): norma de introdução **externa ao Código Penal** classifica crime e contravenção por espécies de pena. Necessário inventariar sua incidência em penas contemporâneas antes de definir a arquitetura única.

### 2.2. Tortura: extraterritorialidade material própria

- [Lei 9.455/1997, art.2º](https://www2.camara.leg.br/legin/fed/lei/1997/lei-9455-7-abril-1997-349431-normaatualizada-pl.html) alcança fatos cometidos fora do território se vítima brasileira ou se agente estiver em local sob jurisdição brasileira. Isso **não corresponde ao mero art.7º, §2º, do CP**. A redação coordenada deve conservar condições próprias, ressalvando obrigações internacionais e demais garantias; não pressupor que o legislador tenha escrito jurisdição universal irrestrita.

### 2.3. Código Penal Militar: segundo núcleo de normas penais gerais

A leitura atualizada da [Câmara — DL 1.001/1969, arts.1º–17](https://www2.camara.leg.br/legin/fed/declei/1960-1969/decreto-lei-1001-21-outubro-1969-376258-normaatualizada-pe.html) mostrou que a Parte Geral militar inclui **sistema articulado próprio**, não apenas uma lista de delitos ou exceção pontual ao CP:

| Tema | CP comum | CPM e consequência para o CLF |
|---|---|---|
| Legalidade | CP art.1º | CPM art.1º com núcleo semelhante: candidato à regra geral comum **somente após prova de abrangência** |
| Sucessão de leis | CP art.2º | CPM art.2º, **com redação de 2023**, inclusive §2º exige comparar leis no conjunto de normas aplicáveis: diferenças e cadeia temporal a auditar |
| Medida de segurança | CP parte geral em conjunto | CPM art.3º disciplina lei aplicável à medida de segurança: alto risco constitucional/intertemporal; **não incorporar automaticamente** |
| Lei temporária e tempo do delito | CP arts.3º–4º | CPM arts.4º–5º, paralelismo aparente a testar |
| Lugar do delito | CP art.6º | CPM art.6º explicita local da conduta devida em **crimes omissivos**, diferença que pode produzir efeitos |
| Territorialidade/extraterritorialidade | CP arts.5º–7º | CPM art.7º e §§ definem incidência militar no exterior, inclusive hipótese de processo/julgamento estrangeiro, com limite em tratados; **regime especial estrutural** |
| Pena cumprida no exterior | CP art.8º | CPM art.8º, redação análoga; coordenação possível sem inferir equivalência |
| Regra de subsidiariedade | CP art.12 | CPM art.17: regras gerais **deste Código Penal Militar** aplicam-se a lei **penal militar especial**; outro referente normativo |

**Consequência metodológica:** simplesmente revogar os artigos gerais do CPM e dizer que a Parte Geral unificada se aplica a todos os crimes pode mudar a legalidade, o regime de sanções e a incidência territorial/militar. O CPM tem também vinculação com o regime de competência constitucional da Justiça Militar, normas de tempo de guerra e tratados. **Alternativa de incorporação só após auditoria de todo o CPM e interface T26/T27.**

### 2.4. Código Eleitoral e outras leis: reafirmação ≠ derrogação

- [Código Eleitoral, Lei 4.737/1965, art.287](https://www.tse.jus.br/legislacao/codigo-eleitoral/codigo-eleitoral-1/codigo-eleitoral-lei-nb0-4.737-de-15-de-julho-de-1965): **reafirma** a aplicação das regras gerais do CP; não cria automaticamente um regime concorrente de teoria do delito. Há, entretanto, sanções/regras eleitorais próprias (arts.283–286) e ressalva setorial no art.288 que exigem classificação independente, sobretudo diante da legislação posterior. **Não se atestou todo o regime penal eleitoral.**
- [CTB, Lei 9.503/1997, art.291](https://www.planalto.gov.br/ccivil_03/leis/l9503compilado.htm) e [ECA, Lei 8.069/1990, art.226](https://www.planalto.gov.br/ccivil_03/leis/l8069compilado.htm) reiteram incidência das regras comuns, com disposições próprias de rito ou tutela. Remover remissões eventualmente redundantes é hipótese editorial condicionada à prova de que alcance permanece igual.
- [Lei 13.445/2017, arts.100–105](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2017/lei/l13445.htm): completa regime de execução de pena estrangeira (ligação com CP art.9º) e **não** constitui, por sua natureza, uma exceção geral ao art.12.

## 3. Três alternativas de arquitetura normativa (`Q`, nenhuma escolhida)

**Modelo A — conservar mais de uma Parte Geral:** código penal comum e militar mantêm princípios paralelos; o CLF incorpora o conteúdo com remissões coordenadas. **Vantagem:** minimiza riscos de inovação acidental; **custo:** redundância e eventual divergência não explicada. Não pressupõe que o CLF deva ser mais curto a qualquer preço.

**Modelo B — Parte Geral compartilhada + exceções completas nos módulos militares/eleitorais/contravencionais:** regras de legalidade, tempo, responsabilidade e sanções comuns aparecem uma vez; dispositivos efetivamente diferentes ficam no regime especial, com critério de competência e subsidiariedade. **Vantagem:** evita repetição estrutural; **risco:** revisão extensa de normas do CPM e de efeitos jurídicos, inclusive crimes militares de tempo de guerra, e alteração de referentes `deste Código`. Exige controle C0/C1/M por efeito e norma de transição.

**Modelo C — regras penais comuns e subpartes de regimes gerais especiais:** núcleo comum + subpartes gerais penal militar/contravencional/eleitoral, cada qual com exceções sistematizadas e regra de incidência precisa. **Vantagem:** conserva unidade do CLF e autonomia jurídica dos subsistemas; **custo:** maior número de divisões editoriais e necessidade de hierarquia de remissões. Pode oferecer equilíbrio, mas essa avaliação é **hipótese de pesquisa, não recomendação ratificada**.

### Teste explícito do art.12 do CP (sem minuta homologada)

O enunciado `as regras gerais deste Código` **não pode ser transferido literalmente para um CLF com múltiplas partes não penais** sem testar o novo referente. Proposta apenas de **critério semântico** (não texto normativo fechado): formular âmbito das **regras gerais de direito penal** identificado por seção/título e sua relação com regimes penais especiais; preservar em locus verificável as exceções relevantes; não generalizar a todos os módulos normas sobre processo, punição administrativa ou execução.

## 4. Testes adversariais prioritários

| Caso | Regra a preservar | Risco na integração |
|---|---|---|
| C05-01 | Tentativa de contravenção não é punível (LCP art.4º) | ampliar CP art.14 sem ressalva |
| C05-02 | Contravenção fora do território enfrenta art.2º da LCP | estender extraterritorialidade comum |
| C05-03 | Tortura no exterior com vítima brasileira | impor condições não previstas da regra comum sem análise |
| C05-04 | Crime militar no exterior com julgamento estrangeiro | apagar CPM art.7º ou desconsiderar tratados |
| C05-05 | Mudança benigna de lei penal militar na vigência da Lei 14.688/2023 | ignorar versão de 2023 do CPM art.2º |
| C05-06 | Crime omissivo militar com garantia de agir em outro lugar | confundir CP 6º e CPM 6º sem teste de resultado |
| C05-07 | Lei penal militar especial sem disciplina expressa | substituir `CPM art.17` por CP art.12 ampliando escopo |
| C05-08 | Crime eleitoral com causa genérica de exclusão de culpabilidade | ignorar art.287 do Código Eleitoral ou criar ressalva indevida |
| C05-09 | Remissão de CTB para CP/CPP | confundir regra penal material com rito |
| C05-10 | Lei posterior descriminaliza crime militar comum | examinar CPM art.2 e CP 2º com legalidade e retroatividade, não apenas prevalência lex specialis |
| C05-11 | Medida de segurança militar com lei nova | CPM art.3º, CF/1988 e jurisprudência exigem verificação antes da unificação |
| C05-12 | Lei 7.209/1984 digital apresenta `aplicam especial se` | não homologar em C0-T histórico sem inspecionar DOU 1984 |
| C05-13 | CLF único usa `deste Código` para aplicação de parte penal | evitar alcance a toda norma não penal do código |
| C05-14 | Pena estrangeira com transferência de execução | CP 8º–9º + Lei 13.445 + T23/T26/T27, sem falsa absorção |

## 5. Encaminhamento e dependências

**FEITO:** edição do DOU **localizada em fonte oficial**, 16 relações seletivas documentadas (CP, LCP, CPM, CE, CTB, ECA, tortura, DL 3.914 e Migração), três modelos comparados, 14 testes.

**PENDENTE:** leitura visual do DOU 1984 e autenticação histórica de divergências; jurisprudência sobre a incidência extraterritorial militar e contravencional, CPM medidas de segurança, normas eleitorais posteriores, cadeia 2023 CPM e efeitos constitucionais; inventário exaustivo de Parte Geral militar e de fontes penais especiais; minuta legislativa e sua concordância; não há `C0-J`, `C1` ou `M` validado.

**PRÓXIMO:** T25.M01/T25.M02 (com interface T01/T26/T27): obter fac-símile da edição 135 do DOU 13/07/1984, comprovar textualmente os 3 pontos divergentes e realizar **teste de arquitetura Modelos A/B/C** com 14 cenários e avaliação da competência/função de cada norma. A escolha final depende de decisão material expressa e da compatibilidade com DEC-016; não alterar o registro central nem a proposta constitucional unilateralmente.

**Princípios constitucionais a proteger:** CF/1988, art.5º XXXIX/XL, art.22 I, organização da justiça militar e art.124 (com análise de alcance), além de tratados e garantias relevantes. O projeto de Constituição alternativa é somente cenário independente.
