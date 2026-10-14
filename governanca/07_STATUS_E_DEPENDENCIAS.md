# Estado de integração e mapa inicial de dependências

**ID:** CLF-GOV-007 | **Versão:** 0.3 | **Data:** 13/10/2026

## Estado global

- Índice de 48 títulos: **PROVISÓRIO — não auditado exaustivamente**.
- Catálogo de módulos: **PROVISÓRIO — não auditado exaustivamente**.
- Carta de arquitetura: **MINUTA INICIAL**.
- Código codificado e consolidado: **a construir**.
- Infraestrutura GitHub: **operacional**, com PR #1 e PR #2 integrados; plano operacional e validação automática em implantação sob PR específico.
- Auditoria técnica dos catálogos: **48 títulos, 273 módulos e 34 interfaces**, sem IDs duplicados, divergências de contagem ou referências a títulos/módulos inexistentes na checagem inicial (13/10/2026); **não** é validação de abrangência jurídica.
- Pesquisa interdisciplinar e modernização: diretrizes operacionais em `governanca/13_DIRETRIZES_PESQUISA_E_MODERNIZACAO.md`.
- Dossiê piloto `T01.M04`: **PLANEJADO**; escopo F0 inicial em `modulos/T01/M04/README.md`, sem inventário F1 ou minuta aprovada.
- Título 01: há extensa discussão e minutas anteriores em chats; **ainda não migradas para o dossiê modular e não estabilizadas**.
- Todos os demais títulos: **PLANEJADO**, sem pretensão de cobertura material.

## Dependências transversais iniciais (hipóteses de trabalho)

| Fonte / regime | Destino / regime | Questão de integração |
|---|---|---|
| T01 — Aplicação da lei | Todos | Vigência, revogação, tempo, transição e publicação |
| T13 — Pessoas | T17, T20, T29, T32 | Capacidade, representação, personalidade |
| T15 — Obrigações e contratos | T16, T20, T09 | Regra geral e exceções de contratos e reparação |
| T07 — Processo administrativo | T10, T12, T29, T31, T37 | Aplicação subsidiária e processos especiais |
| T24 — Processo civil | T17, T20, T29, T32 | Tutela jurisdicional, prova e execução |
| T25 — Direito penal | T05, T20, T32, T37, T45 | Tipos penais atualmente dispersos em leis especiais |
| T10 — Responsabilização pública | T07, T09, T37 | Sanções administrativas e cumulatividade |
| T12 — Direito tributário | T11, T18, T29 | Fiscalidade, empresa e contribuições |
| T32 — Proteções integradas | T13, T17, T24, T25, T26, T31, T33 | Estatutos com matéria civil, processual, penal e setorial |
| T43 — Direito digital | T07, T20, T31, T42 | Dados pessoais e regulação transversal |
| T14 — Direitos reais | T36, T37, T39 | Propriedade, uso territorial e ambiente |
| T23 — Direito internacional privado | T13, T15, T17, T24, T47, T48 | Lei aplicável, atos estrangeiros e tratados |

A tabela indica ligações a verificar, não afirma relações normativas já demonstradas.

## Fila de integração

| Solicitação | Tema | Estado | Próxima verificação |
|---|---|---|---|
| CR-2026-001 | Migrar o material anterior sobre LINDB, LC 95 e técnica legislativa para T01 como Código único | PENDENTE | Inventariar minutas e eliminar divisão indevida como leis estruturantes autônomas |
| CR-2026-002 | Examinar títulos e módulos sob perspectiva de inclusão de direitos de povos indígenas e comunidades tradicionais | PENDENTE | Revisar arquitetura com fontes constitucionais e específicas |
| CR-2026-003 | Definir origem e destino de atos temporários, individualizados, tratados e regulamentos | PENDENTE | Inventário de tipos de fontes e acervos |

## Interface com o projeto constitucional (v0.1)

Foi preparado um protocolo bilateral em `docs/09_INTERFACE_CONSTITUCIONAL.md`, acompanhado de uma matriz inicial de **34 interfaces**, em `catalogo/10_MATRIZ_COMPATIBILIDADE_CONSTITUCIONAL.csv`, e de um registro de solicitações em `governanca/12_REGISTRO_INTERFACE_CONSTITUCIONAL.md`. A matriz é uma triagem estrutural, **não** uma auditoria jurídica artigo a artigo nem deliberação constitucional. Os dossiês afetados podem utilizar `modelos/11_ANEXO_CONSTITUCIONAL_DOSSIE.md`.

O CLF continua independente do projeto constitucional, com decisões, versões e registros separados. A CF/1988 é a referência do direito positivo vigente; a versão futura da Constituição é cenário condicional e pode mudar inteiramente. Toda sessão que utilizar a interface deve fixar versões ou commits das fontes efetivamente consultadas e registrar pedidos de reavaliação sem aprovação automática de nenhum projeto.

**Dependências iniciais prioritárias:** processo legislativo e técnica normativa (IC-2026-010 e IC-2026-026), recepção e transição (IC-2026-027 e IC-2026-034), repartição federativa e financiamento (IC-2026-006). Estas pendências continuam identificadas, não resolvidas.

## Repositório constitucional confirmado

O projeto constitucional dispõe de `main` independente em https://github.com/raphaelpetta/modernizacao-constitucional-brasileira. O commit de implantação verificado em 13/10/2026 é `fa35da0ec5bfec0ae33515c2a48f264c55d3308c`. Sua interface recíproca está em `integracao/01_INTERFACE_CLF.md`. A matriz CLF de 34 interfaces é **triagem histórica relativa ao anteprojeto v0.1**, não correspondência de IDs permanentes do texto que será elaborado.

## Parecer de viabilidade jurídico-formal do Código único (pesquisa preliminar)

O módulo T01.M04 produziu o parecer `modulos/T01/M04/PARECER_04_VIABILIDADE_FORMAL_CODIGO_UNICO.md`, matriz de **15 casos de espécies/iniciativas** e caso-teste histórico `CASO_TESTE_01_LO_LC_E_SV62.md`.

**Achado:** a LC 95 e o STF admitem codificações e normas materialmente ordinárias em LC formal, mas **a lei complementar universal não está demonstrada**: há reservas de espécie e iniciativa, atos privativos das Casas e regras temporais/territoriais. Alternativa C (corpus único com veículos de promulgação juridicamente próprios) é a abordagem **operacional provisória** mais defensável sob CF/1988, porém **não é sinônimo de Código juridicamente uno em diploma formal**. O objetivo `DEC-001` se mantém. **DEC-016 permanece PENDENTE.** Possível novo regime constitucional continua hipótese do projeto próprio `M00.01` / `CF-IC-001`.

A próxima porta de qualidade exige analisar casos concretos de LC/LO, iniciativas reservadas e poder de revisão formal antes de escolher espécie jurídica de promulgação. O parecer **não autoriza** consolidar a minuta experimental 02 como proposta aceita.

## Três testes constitucionais reais — resultado focalizado

Em `modulos/T01/M04/TESTE_05_TRES_CASOS_CONSTITUCIONAIS.md` foram registrados **3 casos e 12 cenários** estruturados em `modulos/T01/M04/RESULTADOS_TESTE_05.csv`: (A) CTN arts. 173–174 / CF art. 146, III, b / STF SV 8; (B) LC 70/1991 / Lei 9.430/1996 / STF Tema 71 e SV 62; (C) Lei 11.416/2006 (PL 5845/2005 de autoria STF) / CF art. 96, II, b / STF ADI 1.835.

**Resultado:** espécie formal, reserva material, iniciativa e possibilidade de atualização **não se confundem**. Não há aprovação de um veículo legislativo universal: **DEC-016 continua PENDENTE**, e `DEC-001` (Código único como objetivo) é preservada.

**Atualização normativa detectada:** **LC 236, de 04/09/2026**, entrou em vigor na publicação e modificou o CTN, inclusive o art. 174. É necessária devolutiva a `T12.M01` (normas gerais tributárias) e `T12.M02` (administração/processo tributário) para conferir disposições novas e vetadas, efeitos temporais, mediação e arbitragem. Nunca transpor redação anterior como se fosse atual.

**Questão jurídica não solucionada:** se a transposição verdadeiramente neutra de matéria originalmente submetida à iniciativa judicial pode tramitar por projeto parlamentar de consolidação com base na LC 95, art. 14, §2º. A análise da **reforma material M** é distinta; não importar automaticamente uma resposta para a transposição `C0`. Pesquisar jurisprudência específica.

## Reserva de iniciativa e consolidação a direito constante — investigação focal

O parecer `modulos/T01/M04/PARECER_06_INICIATIVA_RESERVADA_E_CONSOLIDACAO_FIEL.md` e os nove casos em `modulos/T01/M04/CENARIOS_INICIATIVA_CONSOLIDACAO_06.csv` distinguem compilação informacional, remissão não inovadora, incorporação em lei-base, revogação e reedição formal, e reforma material.

**Achado:** LC 95, art. 14, §2º, prevê iniciativa parlamentar de projetos de consolidação, mas essa autorização **não prova por si** afastamento de reservas de iniciativa constitucional. STF ADI 724 e Tema 917 recomendam interpretação não ampliativa da reserva; ADI 1.835 confirma proteção para inovação em regime judicial; ADI 2.867 impede convalidação do vício efetivo por mera sanção. A pesquisa focal **não identificou precedente diretamente decisivo** quanto a *revogação/reedição literal* de lei da iniciativa judicial por parlamentar: risco **alto e não encerrado**.

**Nova fonte institucional de pesquisa:** nota técnica de maio/2025 sobre consolidação de leis na LBI sem revogar a lei-base, de consultores legislativos da Câmara, **não posição oficial nem jurisprudência**; reforça a alternativa de incorporar leis externas em diploma preexistente. Alternativa útil para transição, **mas não satisfaz sozinha a unidade formal integral DEC-001**.

**DEC-016 e issue #14:** permanecem em pesquisa/pendência. Exigir auditoria autônoma de iniciativa em qualquer proposta `C0` relativa a matérias reservadas, independentemente de haver ou não mudança semântica.

## Desenhos alternativos para promulgação formal do Código único (pesquisa, não decisão)

A pesquisa T01.M04 incorporou `modulos/T01/M04/MODELOS_07_PROMULGACAO_E_ATUALIZACAO_CODIGO.md`, `MATRIZ_MODELOS_PROMULGACAO_07.csv` (**18 cenários**) e `ESBOCOS_CONSTITUCIONAIS_07_CP_CE.md` (**duas minutas constitucionais concorrentes, ambas NÃO APROVADAS**). A análise compara P0 (consulta), P1 (LC global), P2 (positivação modular preparatória), P3 (procedimento coordenado de codificação com ato único), P4 (espécie constitucional Código com regime por matéria) e P5 (reforma estrutural de espécies/reservas).

**Conclusão operacional:** P2 permite avançar na investigação e redação de um corpus integrado sob CF/1988, porém NÃO prova unidade jurídico-formal plena. As hipóteses P3/P4 merecem exame prioritário em M00.02 da Constituição alternativa, **sem importar nenhuma como escolha ratificada**. A iniciativa reservada, os quóruns setoriais, a sanção/veto, a votação final, as competências próprias das Casas e transição continuam pontos bloqueadores de uma promulgação formalmente una.

**DEC-001 permanece objetivo confirmado. DEC-016 permanece PENDENTE.** Os resultados servem à revisão da arquitetura e não aprovam nenhum artigo constitucional proposto.

## Teste de ciclo legislativo completo CP/CE — SIM08 (13/10/2026)

A pesquisa comparou a formação e atualização de um Código formalmente único em `modulos/T01/M04/SIMULACAO_08_PROCESSO_COMPLETO_CP_CE.md`. Os arquivos `MATRIZ_ETAPAS_CP_CE_08.csv` (**72 estados: CP/CE × 3 componentes × S00–S11**) e `FALHAS_E_DECISOES_CP_CE_08.csv` (**20 falhas adversariais**) identificam onde uma hipótese de aprovação **NÃO** se transforma em legislação real.

Três fontes: **CTN art. 174**, com atenção à LC 236/2026 e seus **vetos parciais reais**; **Lei 9.784/1999, art. 2º** (componente legal materialmente ordinário e garantias de direitos); **Lei 11.416/2006, arts. 11–13** (iniciativa judicial quando incida a reserva). **LC 70/1991 permanece apenas precedente histórico** (SV 62), não disposição vigente de teste.

**Resultado:** CP consegue desenhar trâmite por componentes, mas não define suficientemente o ato jurídico de promulgação una (falha em S07). CE define a identidade de espécie Código como hipótese constitucional, porém continua **bloqueado** quanto a sanção/veto, promulgação parcial, dependência entre substituição/revogação e ausência de iniciativa reservada. Isso é avaliação de **minutas ainda incompletas**, não juízo de impossibilidade de futuros desenhos. Também não foi dada força normativa a alguma simulação. `DEC-001` confirmado; `DEC-016` **PENDENTE**.

**Interface constitucional:** remeter resultados à M00.02/M03.01/M14 via `CF-IC-001`, sem transplantar decisões. Next: soluções rivais de veto e promulgação (V1, V2); revisão de direitos, vacatio e fontes autênticas; teste de equivalência C0 por origem/destino real.

## V1/V2: veto, revogação e cobertura jurídica (ciclo 09)

Foram incorporados à pesquisa \`modulos/T01/M04/ANALISE_09_VETO_REVOGACAO_E_COBERTURA.md\`, \`HIPOTESES_NORMATIVAS_09_V1_V2.md\` e \`MATRIZ_VETO_DEPENDENCIAS_09.csv\` (**24 cenários**, quatro registros factuais sobre o veto 48/2026 e 20 hipóteses). Os fatos oficiais incluem os vetos \`48.26.006–008\` a trechos propostos para CTN art. 174 e \`48.26.014\` à cláusula do art. 2º que revogaria Lei 9.430/1996 art. 44 §2º; **não** se demonstrou dependência jurídica causal entre essas disposições específicas. **VET 48/2026 não apreciado no corte de 13/10/2026**.

**V1 (hipótese preferencial para teste):** unidades de veto da CF art. 66 §2º e dependência de eficácia/revogação aprovada previamente por Legislativo competente, evitando decisão discricionária de editor. **Falha grave ainda aberta:** o próprio dispositivo condicional pode ser vetado. **V2 (comparação):** veto de bloco normativo previamente delimitado por lei constitucional nova, com risco acrescido de veto estratégico e necessidade de reforma constitucional expressa. Nenhuma hipótese assegura, sozinha, promulgação formal do Código ou iniciativa constitucionalmente válida.

**Cobertura incompleta:** a falta de projeto de lei de iniciativa judicial para matéria reservada não importa incorporação nem revogação da lei anterior, apenas remissão externa e registro de lacuna de cobertura. \`DEC-001\` objetivo único mantido; \`DEC-016\` e questão de iniciativa \`#14\` seguem pendentes. Encaminhamento \`CF-IC-001\` a M03.01/M00.02/M14 sem adoção de normas.

## Próximo ciclo recomendado

1. Integrar, após revisão, o plano `docs/16_PLANO_OPERACIONAL.md`, o padrão `governanca/17_PADRAO_DADOS_E_PROVENIENCIA.md` e o piloto de T01.M04.
2. Abrir e acompanhar tarefas rastreáveis de T01.M04 (F0/F1), revisão de fontes e validação do inventário.
3. Revisar as pendências constitucionais IC-2026-010, 026, 027 e 034 sem antecipar decisões normativas do outro projeto.
4. Prosseguir só então para redação de normas do T01, sem marcar `INVENTARIADO` ou `REDIGIDO` antes das respectivas verificações.

## Registro resumido para integração futura

- Atualizar versões dos documentos centrais em operação controlada.
- Consolidar propostas aceitas e arquivar o histórico de decisões substituídas.
- Identificar módulos impactados e promover rechecagem das interfaces.
- Nunca converter automaticamente uma hipótese de classificação em decisão jurídica sobre vigência.

## Ciclo 10: veto e condição no mesmo artigo (pesquisa, não deliberação)

A análise `modulos/T01/M04/TESTE_10_UNIDADE_TEXTUAL_VETO_V1.md`, as minutas rivais M0–M3 e a `MATRIZ_UNIDADE_VETO_10.csv` (36 simulações, sem efeitos jurídicos) comparam unidades de veto sob CF art. 66 §2º, LC 95 e LINDB. V1 com revogação e condição no mesmo artigo indiviso mitiga veto da condição isolada, mas não impede veto integral de R, veto parcial do substituto S ou efeitos de derrubada posterior de veto. M2 testa vínculos menores entre cada norma revogada e subunidade substitutiva. Os riscos intertemporais, iniciativa, espécie e não repristinação persistem. DEC-001 preservada; DEC-016 PENDENTE; nenhuma cláusula aprovada.

## Ciclo 11: concordancia normativa e documental

Dossie `modulos/T01/M04/DOSSIE_11_CONCORDANCIA_NORMATIVA_E_DOCUMENTAL.md`: separa texto legislativo N, concordancia documental D e registro publico de eventos P. Prototipos A/D (revogacoes em artigos expressos, tabela explicativa) e B (anexo normativo estatico, ainda Q quanto a LC95 art9 e CF art66 par2). Amostras: 12 nexos hipoteticos, 16 correspondencias informativas e 20 testes adversariais, sem efeito juridico. Revogacao por tabela digital dinamica foi rejeitada. DEC-001 preservada; DEC-016 pendente. Interface CF-IC-001 aberta.

## Ciclo 12: auditoria literal e vetos de anexos (pesquisa)

O parecer `modulos/T01/M04/PARECER_12_ANEXOS_VETOS_E_COTEJO_ARTIGO_A_ARTIGO.md` examinou três casos legislativos reais: AN01 VET 37/2026 (anexo do símbolo de acessibilidade vetado via artigo de substituição, ainda não apreciado no corte); AN02 VET 35/2023 (parágrafos sobre tabela remuneratória vetados, vetos derrubados em 2024, com promulgação posterior do anexo); AN03 VET 9/2026 (dotações individualizadas de anexos orçamentários vetadas sob regime especial). São **práticas legislativas**, não precedentes vinculantes do STF sobre linha de anexo comum.

A `AUDITORIA_LITERAL_DISPOSITIVOS_12.csv` mantém 24 transcrições origem/espelho experimental, todas literais e **Q quanto à equivalência jurídica**, sem promulgação. `EVENTOS_ANEXOS_VETOS_12.csv` registra 11 eventos documentados; `TESTES_CONTEXTUAIS_12.csv` contém 18 contraprovas. O QA impede que igualdade de strings seja indevidamente promovida a C0 jurídico. O problema de força normativa/veto de tabela comum continua na issue #23; `DEC-001` é o objetivo e `DEC-016` segue PENDENTE.

## T07.M03 — Ciclo 13: primeiro piloto completo de normas gerais de processo administrativo (13/10/2026)

Novo módulo experimental `modulos/T07/M03/` com `PILOTO_13_ARTIGOS_1_2_LEI9784.md`, **21 unidades** literalmente espelhadas dos arts. 1º e 2º da Lei 9.784/1999 (inclusive §2º com 3 definições e parágrafo único com 13 incisos), **16 dependências sistêmicas** e **30 contraprovas de veto, contexto e transição**. O espelho integral é `C0-T` (igualdade textual), mas o estado de equivalência jurídica permanece `Q`, e nenhum dispositivo foi promulgado ou revogado.

**Obstáculo estrutural comprovado:** `Esta Lei` não pode ser automaticamente reinterpretada como `este Código`; arts. 3º–70 e alterações posteriores, sobretudo art. 69 (processos especiais) e arts. 49-A–49-G (decisão coordenada), dependem do âmbito do art. 1º e dos princípios do art. 2º. A Súmula 633/STJ reconhece subsidiariedade federativa em hipóteses delimitadas, não competência de imposição automática do Código federal. **R0**, revogação isolada dos arts. 1º–2º, é controle negativo; **R1**, revogação integral futura e condicionada, não está pronta. Preservar `DEC-001` como objetivo e `DEC-016` pendente; sincronizar com T01.M04 e interface CF-IC-001.

## T07.M03 — Ciclo 14: inventário por artigo da Lei 9.784/1999 (13/10/2026)

O dossiê `modulos/T07/M03/DOSSIE_14_INVENTARIO_INTEGRAL_E_ARQUITETURA.md` e os arquivos `INVENTARIO_ARTIGOS_INTEGRAL_14.csv` (**80 posições**, 79 com texto positivo, 49-C integralmente vetado), `HISTORICO_ALTERACOES_VETOS_14.csv` (**16 eventos e fontes**) e `MATRIZ_REMISSOES_INTERDEPENDENCIAS_14.csv` (**50 vínculos relevantes**) estendem o piloto à **totalidade das posições de artigo** da Lei 9.784/1999 na versão oficial consultada. O controle automático verifica a presença das 70 posições numéricas e das 10 intercalares, evita promover `Q` a `C0-J`, diferencia veto integral/parcial e exige IDs de fontes/dependências.

**Não é espelho literal da lei inteira:** faltam transcrição e cotejo de todas as subunidades dos arts.3º–70, auditoria de vigência temporal e de regimes especiais. Alterações de 2006, 2009 e 2021/vetos explicitados; art.69 permanece condicionante de especialidade, art.70 fórmula de vigência histórica, art.54 exige atenção à Súmula633/STJ. Próximo passo: inventário e espelho literal **arts.3º–17** e depois demais blocos, sem revogar a lei de origem. `DEC-001` preservada; `DEC-016` PENDENTE.

## T07.M03 — Ciclo 15: transcrição textual arts. 3º–17 (13/10/2026)

O `modulos/T07/M03/DOSSIE_15_COTEJO_ART3_17.md` e `CONCORDANCIA_LITERAL_ART3_17_15.csv` ampliaram o piloto para **40 unidades** de texto integral dos **15 artigos 3º–17**, todas `Q` quanto à equivalência jurídica, com transposição inexistente. Com os arts.1º–2º do ciclo 13, são **61 unidades textuais** de **17 artigos** espelhadas. Foram confrontados STF SV5 (assistência de advogado em PAD e limites de aplicação), direito de informação/participação, requerimento, interessados, reservas de delegação, avocação excepcional e publicidade. O art.16 conserva a formulação textual da fonte (“unidade fundacional”), anotada para cotejo histórico; nenhuma correção editorial foi convertida em lei.

A **80 posições** do inventário do ciclo 14 continuam abrangência em nível de artigo, sem aferição exaustiva de subunidades dos arts.18º–70. **Não** revogar legislação de origem, não declarar `C0-J` e não homologar espécie jurídica do Código. `DEC-001` objetivo; `DEC-016` pendente.

## T07.M03 — Ciclo 16: 33 unidades nos arts.18–28 da Lei 9.784/1999 (14/10/2026)

O piloto `modulos/T07/M03/PILOTO_16_ARTIGOS_18_28.md` e `CONCORDANCIA_LITERAL_ART18_28_16.csv` contêm **33 unidades** integralmente espelhadas de **11 artigos**, abrangendo impedimentos, suspeição, formalidades, prazos supletivos, intimações e defesa. Foram adicionados **30 testes adversariais** e **20 remissões/dependências** com jurisprudência primária do STJ (MS 7.181/DF, proteção do contraditório na arguição de suspeição; Informativo extraordinário 14/2024, necessidade de análise concreta do prejuízo por vício de intimação). O art. 26 §5º não dispensa genericamente prazo de defesa; art. 26 §4º não transforma edital em meio universal de ciência, e art. 27 impede presunção de confissão ou renúncia pelo não comparecimento. Preservar ainda art.41, 49-D, 59 e 66 e a aplicação subsidiária do art.69.

**Total textual experimental:** **94 unidades de 28 artigos**, sendo 21 (arts.1–2), 40 (arts.3–17) e 33 (arts.18–28). Ainda falta transcrever arts.29–70 e suas unidades subordinadas; **não** existe percentual de equivalência jurídica validado. `DEC-001` segue finalidade de Código uno; `DEC-016` permanece **PENDENTE**. `C0-T` não é `C0-J`, nenhuma alteração legislativa aprovada.

## T07.M03 — Ciclo 17: Capítulo X integral em espelho (14/10/2026)

O piloto [`modulos/T07/M03/PILOTO_17_INSTRUCAO_ART29_47.md`](../modulos/T07/M03/PILOTO_17_INSTRUCAO_ART29_47.md) e `CONCORDANCIA_LITERAL_ART29_47_17.csv` contêm **28 unidades textuais dos arts.29–47 (19 artigos)**, todas `C0-T` literal e **`Q` quanto à equivalência jurídica**, sem normas promulgadas. Foram adicionados **36 testes adversariais** e **34 relações críticas**. O exame distinguiu ônus da prova (36) do dever oficial de instrução e obtenção de documentos (29/37); consulta e audiência pública (31/32) com direito a resposta; arquivamento do pedido por falta de documento necessário (40), que não implica confissão geral; antecedência da prova (41); diferença entre **parecer obrigatório vinculante e não vinculante** (42 §§1º/2º); substituição de laudo técnico (43), manifestação final (44), cautelar motivada por risco iminente (45), privacidade e acesso (46), relatório do instrutor (47). STJ REsp 1.747.877/GO (Informativo Extraordinário 8/2023) foi relacionado à efetiva produção de provas em processo sancionador, sem extensão automática a todo procedimento.

**Acumulado: 122 unidades textuais de 47 artigos originais**, contra inventário de 80 posições totais. A auditoria **não certifica `C0-J`**, não estabelece revogação da Lei 9.784/1999 e não resolve promulgação do Código uno (`DEC-016` PENDENTE). Próxima etapa: arts.48–49 e 49-A–49-G, art.50, depois 51–70 e intercalares (64-A/B, 69-A), distinguindo vetos históricos e especialidade do art.69. `DEC-001` permanece finalidade de Código formalmente uno.

## T07.M03 — Ciclo 18: decisão coordenada e motivação (14/10/2026)

**FEITO:** `PILOTO_18_DECISAO_COORDENADA_MOTIVACAO.md` e quatro matrizes incorporam **40 unidades positivas** dos arts. 48, 49, 49-A, 49-B, 49-D a 49-G e 50; **seis unidades vetadas** em registro histórico, inclusive art. 49-C integralmente vetado; **36 testes adversariais** e **30 dependências**. O parecer diferencia dever de decidir, autoridade convocante cuja disciplina projetada foi vetada, competência originária, exclusões da decisão coordenada, ata e motivação por remissão (Súmula 674/STJ), sem presumir regra de mérito não promulgada.

**ACUMULADO:** 162 unidades experimentais espelhadas da Lei 9.784/1999; todas `Q` em equivalência jurídica, `NAO_PROMULGADO` e sem revogação da legislação vigente. O inventário de 80 posições é cobertura por artigo, não por todas as subunidades.

**PENDENTE:** transcrição completa das disposições 51–70 e 64-A/64-B/69-A; revisão de remissões, direitos, especialidades, iniciativa, quóruns, vetos, transição e eventual cláusula de revogação integral. `DEC-001` preserva a finalidade do Código juridicamente uno; `DEC-016` permanece pendente.

**PRÓXIMO:** fechar o espelho da Lei 9.784, depois realizar auditoria C0-J e separar reformas de mérito `M`, sem aprovação automática.
