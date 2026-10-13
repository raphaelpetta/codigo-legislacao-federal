# Código da Legislação Federal — Pacote de implantação

**Versão:** 0.3 (13/10/2026)  
**Natureza:** documentação de projeto, **não legislação vigente**.  
**Escopo:** Código único de organização federal; constituição externa; normas estaduais/municipais em camadas associadas.

## Objetivo

Criar um corpo único de legislação federal geral e permanente, dividido em partes, títulos, livros, capítulos e dispositivos, acompanhado de matriz de origens e destinos, pesquisa de direito comparado, auditoria crítica e propostas de reforma. O produto final deve permitir implantação legislativa progressiva, respeitando as espécies e competências constitucionais.

## Passos de instalação no ChatGPT

1. Criar um Projeto dedicado ao Código (ou usar o já existente), separado da governança do anteprojeto constitucional, embora possa compartilhar uma interface de consulta.
2. Em **Configurações do projeto**, colar o conteúdo de `08_INSTRUCOES_DO_PROJETO.txt`.
3. Para contexto inicial, disponibilizar a Carta de Arquitetura, Registro de Decisões, Protocolo, Diretrizes Interdisciplinares, Plano Operacional, Índices e Status nas **Fontes do Projeto**. Conferir a versão na `main` do GitHub antes de cada ciclo; anexos não se atualizam automaticamente.
4. Criar um chat `CENTRAL | Governança e integração` e chats identificados por módulo, como `T29.M04 | Benefícios por incapacidade`.
5. Iniciar cada chat com o template `modelos/06_MODELO_DOSSIE_MODULO.md` e consultar `docs/16_PLANO_OPERACIONAL.md`; a primeira tarefa será `T01.M04`.
6. Ao finalizar um ciclo, criar branch/PR e enviar uma **proposta de integração** à frente central; alterações materiais, decisões e mudanças de índice só entram após revisão e aprovação pertinente.

**Importante:** um arquivo enviado ao Projeto não se torna automaticamente um documento compartilhado com edição simultânea entre chats. Usar substituição supervisionada de versões ou um repositório externo versionado. Uma resposta de um chat não atualiza por si só as fontes centrais.

## Arquivos

- `01_CARTA_ARQUITETURA.md`: regras estruturantes; documento normativo interno mais importante.
- `02_INDICE_48_TITULOS.csv`: hipótese inicial de 48 títulos agrupados em 8 partes.
- `03_CATALOGO_MODULOS.csv`: decomposição **preliminar** dos títulos em módulos de trabalho, sujeita a auditoria e revisão.
- `04_REGISTRO_DE_DECISOES.md`: decisões, propostas, pendências e versões.
- `05_PROTOCOLO_DE_TRABALHO.md`: procedimentos, portas de verificação, integrações e revisão independente.
- `06_MODELO_DOSSIE_MODULO.md`: modelo de análise e prompt de abertura de chats.
- `07_STATUS_E_DEPENDENCIAS.md`: dependências transversais e controle de integração.
- `08_INSTRUCOES_DO_PROJETO.txt`: instruções para colar na configuração do Projeto.

## Autoridade e precedência interna

1. Legislação constitucional e fontes jurídicas oficiais verificadas prevalecem no diagnóstico de direito **vigente**.
2. Decisões aprovadas e registradas no `04_REGISTRO_DE_DECISOES.md` orientam a **redação proposta**; não se confundem com direito vigente.
3. A Carta define o método e as regras de governança.
4. Índices e módulos são hipóteses organizacionais revisáveis.
5. O histórico da conversa auxilia a pesquisa, mas não substitui documentação central.

## Governança de versões

Manter `v0.1`, `v0.2` etc. no cabeçalho, data e resumo de alterações. Quando for necessária substituição de arquivos enviados às Fontes do Projeto, retirar ou arquivar a versão antiga para impedir que dois arquivos sejam tratados como simultaneamente vigentes. Sempre comunicar aos módulos afetados que a referência mudou.

## Interface com o projeto constitucional

O CLF e o projeto de modernização constitucional são **projetos independentes**, com decisões e versões próprias. A integração é uma **interface metodológica bilateral**, não uma fusão de projetos, repositórios ou textos normativos. O CLF continua a reconstruir o direito vigente sob a CF/1988; as hipóteses constitucionais futuras são estudadas separadamente e sem presunção de aprovação.

Antes de trabalhar em módulo afetado por escolhas constitucionais, consultar `docs/09_INTERFACE_CONSTITUCIONAL.md`, a matriz `catalogo/10_MATRIZ_COMPATIBILIDADE_CONSTITUCIONAL.csv`, o registro `governanca/12_REGISTRO_INTERFACE_CONSTITUCIONAL.md` e, quando cabível, o anexo `modelos/11_ANEXO_CONSTITUCIONAL_DOSSIE.md`.

Na abertura e no encerramento de um chat, anotar os **commits ou versões efetivamente consultados**, IDs de interface pertinentes, novas pendências e módulos afetados. Não tratar material de conversa, arquivos locais ou versões antigas como alteração automática do repositório. A nota `docs/11_NOTA_PARA_PROJETO_CONSTITUCIONAL.md` é um encaminhamento proposto, não uma decisão do projeto constitucional.

## Critério de prontidão operacional

Para iniciar um módulo basta que existam: repositório de referência consultável, regras de governança e pesquisa, template de dossiê, fonte constitucional do cenário A e registro das pendências. Não é necessário concluir antecipadamente o inventário de toda legislação federal.

Atenção especial: o projeto constitucional possui repositório próprio em https://github.com/raphaelpetta/modernizacao-constitucional-brasileira (implantação inicial `fa35da0ec5bfec0ae33515c2a48f264c55d3308c`, 13/10/2026). O guia e a transcrição do anteprojeto v0.1 são **referências históricas**, não Constituição proposta aprovada. Consultar a `main` e registrar o commit efetivamente lido; nenhuma escolha material é presumidamente aprovada.

## Atenção

Não consta neste pacote levantamento exaustivo de leis, jurisprudência nem classificação artigo a artigo. Os títulos, módulos e dependências são estrutura de planejamento. Não apresentar a cobertura como concluída.