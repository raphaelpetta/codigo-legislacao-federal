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