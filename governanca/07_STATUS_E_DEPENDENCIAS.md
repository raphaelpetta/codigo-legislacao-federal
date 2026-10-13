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