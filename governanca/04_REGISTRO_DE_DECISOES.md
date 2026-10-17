# Registro central de decisões e questões pendentes

**ID:** CLF-GOV-004 | **Versão:** 0.5 | **Data:** 16/10/2026

> Estados possíveis: `CONFIRMADA_PELO_USUARIO`, `HIPOTESE_DE_TRABALHO`, `PENDENTE`, `SUBSTITUIDA`. As confirmações dizem respeito às **premissas do projeto**, não ao direito vigente.

| ID | Estado | Questão | Deliberação ou hipótese | Efeito | Versão |
|---|---|---|---|---|---|
| DEC-001 | CONFIRMADA_PELO_USUARIO | Produto final | **Um único Código da Legislação Federal** tematicamente integrado, não mero conjunto de leis autônomas. | Forma de apresentação e integração | 0.1 |
| DEC-002 | CONFIRMADA_PELO_USUARIO | Construção | Desenvolvimento **modular, integrado**, com contexto compartilhado entre chats. | Governança do projeto | 0.1 |
| DEC-003 | HIPOTESE_DE_TRABALHO | Estrutura geral | 8 partes, 48 títulos **provisórios**, sujeitos a inventário completo. | Índice | 0.1 |
| DEC-004 | HIPOTESE_DE_TRABALHO | Natureza jurídica | Constituição externa; normas de diferentes espécies podem coexistir na consulta, mas exigem atos competentes para positivação. | Redação e implementação | 0.1 |
| DEC-005 | HIPOTESE_DE_TRABALHO | Fonte normativa | Legislação geral/permanente no corpo do Código, com acervo histórico/temporal/individualizado separado. | Cobertura | 0.1 |
| DEC-006 | HIPOTESE_DE_TRABALHO | Citações cruzadas | Uma localização primária para cada disposição; remissões para outras áreas; exceções para regimes integrados. | Arquitetura | 0.1 |
| DEC-007 | HIPOTESE_DE_TRABALHO | Matriz de mudanças | C0/C1/M/Q; nenhum artigo desaparece sem destino documentado. | Auditoria | 0.1 |
| DEC-008 | HIPOTESE_DE_TRABALHO | Método de IA | Chat de módulo propõe; chat central integra; decisões versionadas; dependências checadas. | Fluxo de trabalho | 0.1 |
| DEC-009 | PENDENTE | Título 01 | Migrar resultados das auditorias anteriores para um Título 01 **único**, sem tratar duas leis autônomas como organização final. | Primeiro piloto | 0.1 |
| DEC-010 | PENDENTE | Inventário | Confirmar a cobertura efetiva de cada título/lei com fontes atuais; não presumir classificação exaustiva. | Fase inicial | 0.1 |
| DEC-011 | SUBSTITUIDA | Infraestrutura externa | Deliberação de implantação superada parcialmente: GitHub conectado e adotado, mas sincronização com Fontes do ChatGPT continua manual ou sob consulta ao repositório. Ver DEC-015. | Operação | 0.3 |
| DEC-012 | PENDENTE | Direitos indígenas e tradicionais | Analisar necessidade de título próprio ou estrutura especializada dentro de outro título. | Arquitetura | 0.1 |
| DEC-013 | CONFIRMADA_PELO_USUARIO | Objetivo reformista e pesquisa crítica | Além da compilação e consolidação, auditar e propor modernização substantiva da CF e do CLF, com perspectiva histórica, comparada, jurisprudencial, interdisciplinar e exame de lacunas e contradições. A profundidade será proporcional à matéria. | Método de pesquisa e política de reforma | 0.2 |
| DEC-014 | CONFIRMADA_PELO_USUARIO | Interface com revisão constitucional | Estabelecer integração metodológica entre CLF e projeto constitucional sem fundir versões ou importar hipóteses como decisões aprovadas. | Interface bilateral, sem reforma constitucional automática | 0.2 |
| DEC-015 | CONFIRMADA_PELO_USUARIO | Repositório operacional | Usar o GitHub `raphaelpetta/codigo-legislacao-federal` como repositório versionado de referência; chats produzem análises e PRs, sem sincronização presumida. | Governança operacional e controle de versões | 0.3 |
| DEC-016 | PENDENTE | Veículos legislativos do Código único | Definir solução jurídica para unidade normativa e editorial sem ignorar competências, reservas e espécies exigidas pela CF/1988 ou alternativa constitucional futura. | T01.M04 e interface constitucional | 0.3 |
| DEC-017 | HIPOTESE_DE_TRABALHO | Sequência do piloto | Iniciar T01.M04, prosseguir por T01.M03/M05/M01/M02 e aplicar piloto material T07.M03, sujeito a revisão conforme resultados. | Roadmap inicial | 0.3 |
| DEC-018 | CONFIRMADA_PELO_USUARIO | Procedimento contínuo de construção, deliberação e fechamento progressivos | Adotar coexistência de pesquisa F0–F9, auditoria, integração, deliberação por questão madura e fechamento condicionado; selecionar H/V/I/D/F pelo maior ganho marginal global. Decisões materiais e estruturais relevantes exigem aprovação expressa específica; letra isolada não é aprovação. | Governança do projeto CLF; criar fila de questões, níveis independentes de maturidade, decisão e fechamento, revisão adversarial e reabertura fundamentada; **não** ratifica M, C0-J, DEC-016 ou texto normativo. | 0.4 |
| DEC-019 | CONFIRMADA_PELO_USUARIO | QD-2026-004: arquitetura **preparatória** de dupla camada, alternativa A | Adotar o **Código editorial único** de trabalho e, em paralelo, **trilhas específicas de futura positivação por espécie normativa, iniciativa, competência, quórum, vetos, vigência e transição**, sem revogação constitutiva por catálogo/portal, sem equivalência C0-J presumida e sem absorção automática das leis de origem. Diretriz de preparação, não eleição definitiva do instrumento formal. | Operar modelos e registros de veículo por componente, sem alterar direito, aprovar qualquer reforma M ou resolver DEC-016; **DEC-001 preservada** como objetivo de Código único inclusive quanto à eventual viabilidade formal, a examinar. Subquestão QD-2026-004 FC2; pai QD-2026-001 e DEC-016 pendentes. | 0.5 |

## Modelo de entrada nova

```
ID: DEC-NNN
Data: AAAA-MM-DD
Estado: HIPOTESE_DE_TRABALHO | CONFIRMADA_PELO_USUARIO | PENDENTE | SUBSTITUIDA
Proposta:
Fundamentos:
Alternativas examinadas:
Impacto sobre títulos/módulos:
Documentos e versões afetados:
Decisão e responsável:
```

**DEC-018 — base de aprovação:** manifestação expressa do usuário em 16/10/2026, após apresentação do modelo de construção, deliberação e fechamento progressivos: “certo. vamos adotar entao. implemente-o”. Aprovação **procedimental**, registrada neste PR; não pode ser interpretada como aceitação tácita das alternativas listadas na fila. [Procedimento](19_PROCEDIMENTO_CONSTRUCAO_DELIBERACAO_FECHAMENTO.md) e [fila](19_FILA_QUESTOES_DELIBERAVEIS.json). **DEC-016 permanece PENDENTE.**

**DEC-019 — aprovação específica (16/10/2026):** após o dossiê QD-2026-004 e a pergunta A/B/C, o usuário declarou literalmente: **“Aprovo expressamente a alternativa A da QD-2026-004 como diretriz preparatória do CLF, preservadas a DEC-001 e a pendência da DEC-016.”** [Registro de transcrição na central #48](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/48#issuecomment-6228937676) — **fonte secundária de auditoria criada pela coordenação**, e não permalink autenticado da mensagem do chat. A fonte primária da aprovação é a mensagem direta do usuário neste diálogo. Ver [diretriz de dupla camada](20_DIRETRIZ_DUPLA_CAMADA_DEC019.md). DEC-016 segue **PENDENTE**, por decisão do próprio usuário.

**Regra:** decisões novas não são introduzidas apenas porque um chat as propôs. O chat central avalia e o usuário aprova escolhas estruturais ou materiais relevantes.