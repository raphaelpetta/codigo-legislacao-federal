# Código da Legislação Federal — Pacote de implantação

**Versão:** 0.1 (13/10/2026)  
**Natureza:** documentação de projeto, **não legislação vigente**.  
**Escopo:** Código único de organização federal; constituição externa; normas estaduais/municipais em camadas associadas.

## Objetivo

Criar um corpo único de legislação federal geral e permanente, dividido em partes, títulos, livros, capítulos e dispositivos, acompanhado de matriz de origens e destinos, pesquisa de direito comparado, auditoria crítica e propostas de reforma. O produto final deve permitir implantação legislativa progressiva, respeitando as espécies e competências constitucionais.

## Passos de instalação no ChatGPT

1. Criar um Projeto dedicado ao Código (ou usar um projeto dedicado já existente, se não misturar projetos constitucionais independentes).
2. Em **Configurações do projeto**, colar o conteúdo de `08_INSTRUCOES_DO_PROJETO.txt`.
3. Adicionar os arquivos 01 a 07 às **Fontes do Projeto**, preferencialmente separadamente (o ZIP é apenas um transporte).
4. Criar um chat `CENTRAL | Governança e integração` e chats identificados por módulo, como `T29.M04 | Benefícios por incapacidade`.
5. Iniciar cada chat com o template contido em `06_MODELO_DOSSIE_MODULO.md`.
6. Ao finalizar um ciclo, enviar uma **proposta de integração** ao chat central; apenas depois da aprovação registrar mudanças no índice, no diário de decisões e no estado da integração.

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

## Atenção

Não consta neste pacote levantamento exaustivo de leis, jurisprudência nem classificação artigo a artigo. Os títulos, módulos e dependências são estrutura de planejamento. Não apresentar a cobertura como concluída.