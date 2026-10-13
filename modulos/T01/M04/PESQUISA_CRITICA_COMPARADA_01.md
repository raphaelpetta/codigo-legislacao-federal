# T01.M04 — Primeira auditoria crítica e comparada da arquitetura de codificação

**Data de referência:** 13/10/2026  
**Módulo:** T01.M04 — Consolidação e codificação  
**Estado:** pesquisa inicial auditável; F0 delimitado, F1 **parcial** e F2–F4 em desenvolvimento. **Não é proposta homologada, nem inventário exaustivo.**  
**Referências internas:** `docs/01_CARTA_ARQUITETURA.md`, `governanca/13_DIRETRIZES_PESQUISA_E_MODERNIZACAO.md`, `docs/16_PLANO_OPERACIONAL.md`; interfaces `IC-2026-010`, `IC-2026-026`, `IC-2026-027`, `IC-2026-034`.

## 1. Pergunta de pesquisa e distinções

Pergunta: **sob quais condições é possível converter as disposições gerais e permanentes da legislação federal brasileira em um Código tematicamente unitário, juridicamente válido, renovável e materialmente modernizado, sem perder direitos, competências, regimes especiais ou história das normas?**

É imprescindível separar:
1. **Compilação informacional**: exibição/reunião de textos originais e suas atualizações, sem inovar na forma legislativa.
2. **Consolidação a direito constante**: processo legislativo de unificação e revogação formal, preservando conteúdo, continuidade e efeitos, com ajustes admitidos; no Brasil, LC 95/1998, art. 13, §1º.
3. **Codificação sistemática**: reconstrução de conceitos, estrutura e disposição em uma arquitetura temática. Pode ser editorial, formalmente promulgada, e/ou incluir alterações materiais devidamente identificadas.
4. **Reforma material**: modificação consciente do conteúdo ou efeitos das normas, com justificativa, alternativa, transição e aprovação pelo órgão competente.
5. **Publicação codificada dinâmica**: interface consultável que acompanha versões efetivamente promulgadas; **não substitui, sem suporte jurídico, atos legislativos necessários**.

A distinção é **de efeitos**, não apenas de rótulos. Uma alteração linguisticamente pequena pode ser reforma M quando modifica a incidência da norma; uma reorganização extensa pode ser C1 se demonstrada rigorosa equivalência.

## 2. Achados normativos iniciais sob a CF/1988

### 2.1. Constituição: espécies e materialidade

A CF/1988, art. 59, prevê diferentes espécies de ato legislativo, e seu parágrafo único remete a lei complementar as regras de elaboração, redação, alteração e consolidação. Art. 69 exige maioria absoluta para leis complementares. A LC 95/1998 foi editada nessa competência.

**Conclusão preliminar:** a unidade editorial proposta pelo CLF é possível como arquitetura informacional; a **promulgação com efeitos próprios** deverá obedecer às reservas materiais, competências e ritos de cada regra. Não afirmar que o CLF pode ser promulgado integralmente em uma única lei ordinária; tampouco afirmar que uma lei complementar única é necessariamente inválida em todas as hipóteses.

A jurisprudência do STF distingue lei formalmente complementar e matéria materialmente ordinária: **ADI 2.926**, **RE 377.457 (Tema 71)** e **SV 62**; em matéria municipal, **ARE 1.521.802 (Tema 1.352)**. Isso demonstra que a espécie formal escolhida não torna automaticamente todo o conteúdo sujeito a uma reserva de LC. A **consequência para manutenção e alteração posterior de um eventual Código misto** precisa ser estudada; a existência dos precedentes não resolve, por si, a questão do Código único.

Fonte de síntese oficial do STF: https://portal.stf.jus.br/constituicao-supremo/artigo.asp?abrirArtigo=59&abrirBase=CF ; https://portal.stf.jus.br/jurisprudencia/sumariosumulas.asp?base=26&sumula=9347

### 2.2. LC 95/1998: consolidação permitida, limites e tensão editorial

Dispositivos lidos na versão compilada oficial: arts. 1º; 7º, I–IV; 9º; 12; 13, caput e §§1º–3º; 14, caput e §§1º–4º; 15–17; recorte verificado em 13/10/2026.

- **Art. 13, caput:** prevê codificações/consolidações organizadas em volumes de matérias conexas ou afins; a união de seu conteúdo compõe a Consolidação da Legislação Federal.
- **Art. 13, §1º:** integração da legislação pertinente a cada matéria em diploma único e revogação formal das leis incorporadas, sem modificação de alcance nem interrupção de força normativa.
- **Art. 13, §2º:** permite redistribuir artigos, fundir disposições repetidas/equivalentes, atualizar termos e outras operações **preservando** o conteúdo. O §3º exige justificativa qualificada para exclusão por inconstitucionalidade, não recepção e revogação implícita.
- **Art. 14:** levantamento, formulação de projeto, procedimento parlamentar e exclusão de medidas provisórias ainda não convertidas em lei.
- **Art. 15:** periodicidade de atualização e inclusão em coletâneas; texto conserva a expressão `Consolidação das Leis Federais Brasileiras`, ao passo que o art. 13, alterado em 2001, prefere `Consolidação da Legislação Federal`. **Diagnóstico:** descompasso terminológico aparente, ainda sem antinomia demonstrada.
- **Arts. 16–17:** acervo separado de decretos e atos infralegais e mecanismos de consolidação/atualização. **Nota:** não confundir força de regulamento com força de lei.

A LC 107/2001 alterou substancialmente o regime da LC 95, inclusive arts. 13–14. Uma tentativa de ler isoladamente a redação histórica de 1998 geraria diagnóstico incorreto.

**Potencial conflito com nosso objetivo:** a LC 95 é orientada a consolidar **por matérias** e preservar alcance. O CLF projeta um sistema mais amplo, de todo o direito federal permanente, **e deseja alterar materialmente seus regimes**. Isso não é antinomia já verificada: é escolha de desenho e procedimento que exigirá trilhas distintas para texto de direito constante e reforma.

Fonte oficial: https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp95compilado.htm e LC 107/2001 em https://www2.camara.leg.br/legin/fed/leicom/2001/leicomplementar-107-26-abril-2001-350137-publicacaooriginal-1-pl.html

### 2.3. LINDB e Decreto 12.002/2024

- **LINDB (Decreto-Lei 4.657/1942), arts. 1º–2º e 6º:** publicação/vacatio, revogação expressa/tácita, continuidade e proteção de situações constituídas. São regras gerais relevantes a interfaces T01.M01/M02; **não transplantar automaticamente tudo para M04**.
- **Decreto 12.002/2024, arts. 1º–2º:** disciplina elaboração, redação, alteração e consolidação e o fluxo de encaminhamento de atos; aplica-se a atos do Presidente e autoridades inferiores na administração pública federal direta, autárquica e fundacional. Não é estatuto geral do Poder Legislativo ou autorização para alterar leis por decreto.
- **Decreto 12.002/2024, arts. 62–63:** prevê consolidação e alterações a direito constante em sua esfera de aplicação; deve ser harmonizado com a LC 95 e normas hierarquicamente superiores.

Fontes: https://www.planalto.gov.br/ccivil_03/decreto-lei/del4657compilado.htm ; https://www2.camara.leg.br/legin/fed/decret/2024/decreto-12002-22-abril-2024-795527-normaatualizada-pe.html

### 2.4. Jurisprudência brasileira: duas advertências

- **ADI 5.127/DF (STF, julgamento 15/10/2015):** o Tribunal censurou emendas parlamentares sem pertinência temática em lei de conversão de medida provisória, com efeitos prospectivos especificados. O precedente é **específico do processo de conversão de MP**; não transforma toda exigência redacional da LC 95 em causa geral de inconstitucionalidade.
- **Tema 71 / SV 62 / ADI 2.926 / Tema 1.352:** a distinção entre forma complementar e conteúdo materialmente ordinário impede presumir uma hierarquia abstrata rígida entre LO e LC. Requer, contudo, estratégia de atualização e publicidade para textos que reúnam regras de reservas diferentes.

Fontes: https://noticias.stf.jus.br/postsnoticias/legislativo-nao-pode-incluir-em-lei-de-conversao-materia-estranha-a-mp-decide-stf/ ; https://portal.stf.jus.br/constituicao-supremo/artigo.asp?abrirArtigo=59&abrirBase=CF ; https://noticias.stf.jus.br/postsnoticias/beneficio-criado-por-lei-complementar-pode-ser-revogado-por-lei-ordinaria-decide-stf/

**Estado jurisprudencial:** pesquisa exploratória, não levantamento exaustivo de julgamentos sobre LC 95 ou codificação. Não inferir conclusões negativas pela ausência de outros precedentes neste dossiê.

## 3. Experiências comparadas — hipóteses para o CLF

| Modelo | Instituição/objeto | Mecanismo | Vantagem potencial | Limitação para transposição |
|---|---|---|---|---|
| **Estados Unidos** | `United States Code`, Office of the Law Revision Counsel (House) | Títulos temáticos; alguns formalmente promulgados (`positive law`), outros compilação editorial de leis distintas (`non-positive`). Títulos positivos são promulgados um por um | Navegação unificada; incorporação gradual e tabelas origem/destino; títulos com estatuto jurídico explícito | Não é um único estatuto de todos os ramos; não absorve regulamentos, tratados, leis estaduais; o próprio sistema separa natureza jurídica dos títulos |
| **França** | Comissão superior de codificação e textos codificados | Codificação `à droit constant` com estrutura coerente; reformas materiais podem ser propostas separadamente | Reduz risco de controversa mudança de mérito durante recodificação | Distinção legislativo/regulamentar e técnica de *ordonnances* dependem de desenho constitucional próprio |
| **Canadá** | `Legislation Revision and Consolidation Act`, ss. 30–31 | Consolidação publicada não opera como nova lei; versões oficiais constituem prova; texto original prevalece se incompatível | Transparência da origem e segurança da publicação eletrônica | É modelo de compilação autoritativa, não de substituição de todo o direito por um Código promulgado |
| **Inglaterra e País de Gales** | Law Commission | Projetos técnicos de consolidação e de reforma; tramitação legislativa dos resultados | Instituição permanente, priorização e consulta sobre problemas reais | Ambiente constitucional/parlamentar não pode ser transplantado automaticamente |
| **País de Gales (caso concreto, 2026)** | `Planning (Wales) Act 2026` | Código/ato consolidado de planejamento em versão clara e bilíngue, sem reforma substantiva global do setor | Exemplo recente de codificação temática e acesso mais consistente | Escopo reduzido em comparação com o CLF de toda a legislação federal |

**Fontes institucionais:** 
- EUA, OLRC: https://uscode.house.gov/codification/legislation.html ; https://uscode.house.gov/faq.html
- França, circular de 30/05/1996: https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000000742705 ; trabalhos da Comissão: https://www.legifrance.gouv.fr/contenu/menu/autour-de-la-loi/codification/rapports-annuels-de-la-commission-superieure-de-codification
- Canadá, Lei de revisão e consolidação: https://laws-lois.justice.gc.ca/eng/acts/s-20/fulltext.html
- Law Commission: https://lawcom.gov.uk/consolidation/
- País de Gales: https://lawcom.gov.uk/news/planning-wales-act-2026-receives-royal-assent/

**Leitura crítica:** a distinção `codificação fiel` × `reforma material` aparece nas práticas francesa e norte-americana, mas isso **não autoriza** tratar nosso Código como apenas consolidação neutra. Precisamos de processo com decisão explícita e documentação para reformar, sem afastar a transposição fiel quando apropriada.

## 4. Hipóteses de desenho institucional para comparar

| Alternativa | Descrição | Benefício potencial | Risco ou ônus |
|---|---|---|---|
| **A. Compilação única** | Portal temático público que agrega leis existentes e alterações, sem revogações | Iniciar rapidamente e evitar conflito de espécie | Unidade apenas informacional; direito continua formalmente fragmentado |
| **B. Consolidação por blocos a direito constante** | Leis de consolidação por matéria, acompanhadas de índice único | Conformidade mais direta com LC 95; implementação progressiva | Mantém pluralidade de diplomas; transformação material independente |
| **C. Código arquitetural único com promulgação modular** | Índice e dispositivos de trabalho integrados; atos legislativos formalmente competentes para cada bloco | Preserva visão de um Código único e adapta constitucionalidade, com trilhas distintas de reforma | Precisa desenhar a autoridade jurídica de cada título e o efeito de futuras alterações |
| **D. Código promulgado em espécie singular** | Tentar aprovar todo o corpo em um só instrumento | Unidade formal mais intensa | Reserva de LC e outras competências, manutenção posterior e processos distintos exigem análise jurídica profunda, sem garantia de viabilidade |
| **E. Redesenho constitucional** | Constituição alternativa fornece mecanismo explícito para Código, espécies e atualização | Pode remover atritos estruturais do cenário A | Não existe direito vigente novo; escolha B incerta, depende de deliberação e transição |

**Hipótese preferencial para aprofundar (não decisão):** C, associada a A como publicação/consulta, com B como trilha inicial de transposições fiéis, combinando reforma M aprovada em procedimento apropriado. O objetivo continua sendo **um Código sistemático**, não apenas vários códigos independentes. Verificar se a ideia de “promulgação modular” preserva unidade jurídica suficiente ou exigiria reforma constitucional.

## 5. Questões e problemas identificados

1. **P01 — Natureza e espécies:** como expressar, num Código único, reservas materiais e ritos diferentes? Tema não resolvido pela mera escolha de lei complementar geral.
2. **P02 — Segurança de consolidações:** verificar se renumerações, fusões e alterações vocabulares efetivamente preservam todos os efeitos, inclusive interpretações estáveis.
3. **P03 — Atualizações legislativas:** estabelecer forma pela qual leis futuras alteram o corpo comum sem reabrir dispersão. Separar `texto em vigor`, `texto de trabalho` e `proposta ainda não aprovada`.
4. **P04 — Consolidação x reforma:** manter duas trilhas explícitas (equivalência provada e decisão material).
5. **P05 — Intertemporalidade:** identificar efeitos da norma original sobre processos, fatos pretéritos, direitos adquiridos e transições.
6. **P06 — Diagnóstico da LC 95, art. 13 x art. 15:** descompasso terminológico; **incoerência editorial preliminar**, não contradição de comando demonstrada.
7. **P07 — Lugar dos atos infralegais, tratados e atos temporários:** acervo próprio e links, com identificação hierárquica; ainda sem inventário completo.
8. **P08 — Risco de codificação jurisprudencial:** não positivação automática de tese ou interpretação somente por ser consolidada; distinguir necessidade e alternativas.
9. **P09 — Constitucionalidade de decisões editoriais:** suprimir dispositivo por alegada não recepção/revogação tácita demanda fonte, justificativa, autoridade competente e controle de reversibilidade.
10. **P10 — Informação legislativa e direito de acesso:** autenticidade, fonte oficial, ID persistente, dados de vigência, explicação de relações 1:N/N:1 e revisão de versões.

Os problemas acima são *candidatos a auditoria*, não afirmações de lacuna normativa real.

## 6. Recomendações de método para T01.M04

- **Dupla perspectiva A/B:** CF/1988 vigente como parâmetro legal; anteprojeto constitucional como cenário condicional versionado. A nova Constituição ainda não aprovou mecanismo de Código único.
- **Dois trilhos editoriais no mesmo Código:** (i) base de equivalência C0/C1; (ii) propostas de reforma M/Q com sua decisão, motivação e efeitos. Não converter M em simples “reorganização”.
- **Tabela de proveniência obrigatória:** origem, versão temporal, natureza e competência, destino, tipo de correspondência e razão jurídica.
- **Não suprimir regimes especiais por limpeza formal:** normas de proteção, exceções históricas e regras de transição demandam teste de efeito real.
- **Pergunta de validação:** é possível provar que uma alteração aparentemente editorial **não** mudou quem tem direito, quem deve, quem decide, como se prova, quando começa/termina e que sanção cabe?
- **Separar o direito comparado do transplante:** nenhum modelo estrangeiro “comprova” melhor solução no Brasil sem cotejo federativo e constitucional.
- **Abrir consulta especializada futura**, especialmente sobre forma jurídica do Código único e sua atualização, se transformado em proposta institucional real.

## 7. Programa do próximo ciclo (F1 → F4)

1. Completar inventário dos recortes LC 95, LC 107, Decreto 12.002, LINDB e CF (com alterações históricas, vigência, normas interpostas e regulamentares).
2. Inventariar jurisprudência brasileira qualificada de espécies normativas, alterações editoriais, revogação e segurança jurídica, com ratio, data e situação vinculante.
3. Selecionar pequenos **casos-testes** e preencher concordância origem/destino, preferindo dispositivos reais da LC 95; classificar C0/C1/M/Q e testar transição.
4. Examinar os mecanismos regimentais de tramitação de consolidações e a possibilidade jurídica de reforma sob instrumentos separados.
5. Preparar **quadro de alternativas** com parecer adversarial de cada cenário (A–E), sobretudo arquitetura C sob CF/1988.
6. Elaborar proposta de Título 01/Capítulo específico **somente depois** de auditar a equivalência ou decidir expressamente a reforma material.

**Porta de qualidade:** manter `F1 PARCIAL` até demonstrar cobertura das fontes e dispositivos do recorte; ainda não classificar o módulo como `INVENTARIADO`, `AUDITADO`, `REDIGIDO` ou `INTEGRADO`.
