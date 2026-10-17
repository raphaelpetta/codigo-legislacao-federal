# Plano operacional de execução modular e integração do CLF

**ID:** CLF-OPS-016 | **Versão:** 0.4 | **Data:** 16/10/2026  
**Natureza:** governança operacional do anteprojeto; não direito vigente nem deliberação legislativa.

## 1. Fonte de verdade e organização

- **GitHub:** `raphaelpetta/codigo-legislacao-federal`; `main` guarda apenas material integrado e versionado. O estado atual é uma base de pesquisa e não um Código concluído.
- **Projetos e chats do ChatGPT:** espaços de trabalho para investigar, redigir e revisar. Não sincronizam automaticamente nem são autoridade superior ao commit registrado no GitHub.
- **Projeto constitucional:** repositório independente `raphaelpetta/modernizacao-constitucional-brasileira`, com implantação inicial identificada pelo commit `fa35da0ec5bfec0ae33515c2a48f264c55d3308c`. Comparar CF/1988 vigente, anteprojeto futuro e CLF. O material histórico v0.1 não equivale a decisões ratificadas. Usar também a interface recíproca `integracao/01_INTERFACE_CLF.md` do projeto constitucional.
- **Fontes jurídicas:** textos legais e decisões oficiais datados prevalecem para **descrever o direito brasileiro**, mas não constituem, por si, uma escolha normativa de reforma. Dados, relatórios e doutrina devem ter referência de procedência.

Nunca presumir que o conteúdo de um arquivo anexado às Fontes do ChatGPT esteja sincronizado com `main`. Em cada frente de trabalho, conferir os documentos centrais no repositório e identificar o commit consultado. Em caso de indisponibilidade da conexão, apontar limitações e evitar gravação baseada em contexto parcial.

## 2. Estrutura de responsabilidades

| Frente | Responsabilidade | Não pode fazer sem integração |
|---|---|---|
| **CENTRAL — Arquitetura e integração** | Avaliar estrutura, decisões, terminologia compartilhada, dependências e alterações intermodulares | Aprovar unilateralmente escolhas materiais ou constitucionais reservadas ao usuário |
| **T01 — Núcleo de normas gerais** | Técnica, vigência, fontes, consolidação, interpretação, publicação | Alterar silenciosamente regimes setoriais |
| **Txx.Myy — Especializada** | Inventariar, analisar, comparar, propor minuta, concordância e testes no seu recorte | Reescrever por conta própria decisões centrais e outros módulos |
| **REVISÃO — Adversarial e integridade** | Identificar contradições, desvios de fontes, incongruências sistêmicas e efeitos não intencionais | Tornar hipótese em regra vinculante ou marcar pesquisa incompleta como validada |
| **INTERFACE CONSTITUCIONAL** | Registrar incompatibilidades e devolutivas condicionais ao anteprojeto | Importar decisões não aprovadas entre os dois projetos |

Um mesmo usuário ou assistente pode ocupar várias frentes, mas cada mudança substantiva precisa de registro e rastreabilidade.

## 3. Fluxo de trabalho obrigatório

1. **Abrir tarefa:** issue GitHub ou referência `CR-AAAA-NNN`, com módulo, recorte, resultados esperados e dependências.
2. **Fixar versão:** anotar commit da `main`, versões de anteprojetos, data de corte normativa e fontes consultáveis.
3. **F0 — Delimitação:** definir o regime funcional, fronteiras, exclusões, institutos e módulos relacionados. Status `PLANEJADO`.
4. **F1 — Inventário demonstrável:** localizar leis e dispositivos vigentes/revogados/temporários relevantes, alterações e fontes oficiais, classificando lacunas de pesquisa. A lista não é exaustiva enquanto não conferida.
5. **F2 — Modelo do direito vigente:** reconstruir normas, precedentes, autoridades, direitos, obrigações, procedimentos e efeitos reais; separar decisões firmadas e posições controversas.
6. **F3 — Pesquisa crítica proporcional:** história, direito comparado, tribunais brasileiros e internacionais, evidência jurídica/empírica, administração real e atores afetados.
7. **F4 — Auditoria de problemas e escolhas:** registrar lacunas, antinomias aparentes ou demonstradas, obsolescência, jurisprudencialização, falhas institucionais, custos e alternativas — inclusive manutenção.
8. **F5 — Redação da minuta:** texto na arquitetura única do Código, marcando `C0/C1/M/Q` por dispositivo e efeitos.
9. **F6 — Concordância:** mapear cada disposição de origem para seu(s) destino(s), razões das supressões e propostas sem antecedente legal; não confundir ausência de destino com revogação.
10. **F7–F8 — Testes e crítica adversarial:** constitucionalidade A/B quando pertinente, competências, direitos, não regressão não examinada, sanções, procedimentos, transição e possíveis abusos.
11. **F9 — Proposta de integração:** PR de branch de módulo, resumo de mudanças, fontes e pendências, referências a decisões e interfaces. Revisão central e aprovação de escolhas relevantes.
12. **Integração e rechecagem:** registrar alterações aceitas, atualizar concordância, índices, dependências e versão; reabrir módulos impactados.

**DEC-018 — ramo contínuo de deliberação:** durante F0–F9, **cada questão identificável** pode ser registrada em [fila canônica](../governanca/19_FILA_QUESTOES_DELIBERAVEIS.json) e encaminhada a decisão tão logo tenha maturidade suficiente, sem esperar todo o módulo. Utilizar [CLF-GOV-019](../governanca/19_PROCEDIMENTO_CONSTRUCAO_DELIBERACAO_FECHAMENTO.md), distinguindo maturidade, decisão expressa, fechamento FC0–FC5 e classe jurídica C0-T/C0-J/C1/M/Q. Comparar H/V/I/D/F por ganho marginal global; continuar a pesquisa focal da parte bloqueada enquanto outras partes avançam. CI/PR não homologam direitos.

**Portas:** `PLANEJADO` → `INVENTARIADO` → `AUDITADO` → `REDIGIDO` → `REVISADO` → `INTEGRADO` → `ESTABILIZADO`. Os status intermediários não são equivalentes a validade legal e não podem ser pulados sem documentação.

## 4. Um padrão para cada sessão

**Na abertura**, conferir: escopo `Txx.Myy`, commit-base, Carta, Registro de Decisões, Protocolo, Diretrizes de Pesquisa, índice/catalogo, documentos do próprio módulo, interfaces constitucionais e fontes oficiais pertinentes.

**Durante**, anotar dispositivo e proveniência, evitar inventar fontes/consensos, registrar controvérsias e propostas de alteração transversal.

**Na entrega**, produzir: avanço factual, arquivos modificados, fontes efetivamente examinadas, lista de pendências, alterações C0/C1/M/Q, conflitos, testes, riscos, módulos afetados, PR/issue e recomendação de próximos passos.

**Abertura de novo chat sugerida:**

> Estamos no projeto CLF. Este chat é dedicado ao módulo Txx.Myy — [regime]. Consulte a branch main do repositório raphaelpetta/codigo-legislacao-federal e registre o commit usado. Leia docs/01, governanca/04, /05, /07, /13, docs/16, os catálogos e o dossiê relevante. Distinga direito vigente, controvérsia, proposta e hipótese constitucional. Execute F0 e F1 antes de escrever normas. Trabalhe em branch própria e submeta PR para integração; não altere o centro ou outros módulos silenciosamente.

Não pressupor que um novo chat possua acesso garantido ao GitHub. Se não conseguir abrir os arquivos centrais, não tomar decisões substantivas irreversíveis.

## 5. Git, GitHub e aprovações

- **`main`** é baseline estável de planejamento e textos aceitos, não atestado de verificação jurídica.
- **Branches:** `modulo/Txx-Myy-assunto`, `governanca/assunto`, `integracao/assunto` ou `revisao/assunto`.
- **PRs:** cada tema com escopo pequeno, caminhos afetados, mudanças de sentido e classes C0/C1/M/Q, fontes, testes e pendências. Evitar vários chats editando a mesma versão do mesmo arquivo simultaneamente.
- **Decisões normativas e arquiteturais relevantes:** expor alternativas e obter aprovação expressa do usuário antes de registrar como `CONFIRMADA_PELO_USUARIO` ou consolidar texto material como aceito.
- **Melhorias editoriais e ferramentas internas:** podem ser integradas após auditoria técnica, sem fingir que validam o conteúdo substantivo.
- **Conflitos:** nunca forçar atualização destrutiva; atualizar a branch, revisar diffs, reconciliar as alterações e reexecutar verificações.
- **Histórico e provenance:** não apagar decisões substituídas sem marcador e motivo.
- **Issues:** organizar tarefas por módulo e bloqueios; `README`/Status mostram panorama resumido, não substituem issues.

## 6. Formatos e rastreabilidade

Os CSVs fornecem catálogos e quadros de trabalho legíveis por humanos e programas. Seus campos e identificadores devem seguir `governanca/17_PADRAO_DADOS_E_PROVENIENCIA.md`. Usar Markdown para dossiês e decisões, e tabelas estruturadas para inventário e concordância. Toda norma incorporada deve conservar dispositivo original e versão de origem, destino, resultado C0/C1/M/Q e explicação dos efeitos intertemporais.

Identificadores `Txx.Myy` nomeiam **módulos de trabalho**, não são números definitivos dos artigos publicados. Ao renumerar dispositivos, preservar correspondência e identificador de trabalho para evitar remissões órfãs.

## 7. Entregas mínimas de um piloto

O primeiro módulo piloto é **T01.M04 — Consolidação e codificação**, com foco em:
- LC 95/1998 (especialmente regras de consolidação), LINDB e Decreto 12.002/2024 **dentro dos limites de aplicação de cada ato**;
- confronto entre compilação, consolidação a direito constante, codificação e reforma material;
- problemas de espécie normativa, competências, revogações e unidade sistemática;
- arts. 64–66, 174 e ADCT T1/T17 do anteprojeto constitucional **apenas como hipóteses condicionais**;
- dossiê F0/F1, matriz de fontes, alternativas, técnica de integração e primeiro teste de concordância.

**Critério de conclusão do piloto:** conseguir seguir uma disposição de origem oficial até uma proposta CLF e demonstrar por que seu efeito foi preservado ou alterado, quais variantes dependem de Constituição futura e quais decisões continuam abertas. Não usar a existência de minuta anterior em chats como prova de inventário concluído.

Depois do piloto: T01.M03 (redação), T01.M05 (publicação e versões), T01.M01/M02 (vigência e interpretação), seguido de um piloto material T07.M03 (processo administrativo geral). A ordem pode mudar mediante diagnóstico e registro.

## 8. Questões deliberadamente não resolvidas

- Espécies e atos de positivação de um Código realmente único sob CF/1988 ou eventual Constituição futura;
- exaustividade dos 48 títulos/273 módulos; localização de estatutos protetivos, regimes transversais, direito indígena e tradicionais;
- migração e auditoria das minutas anteriormente discutidas;
- sincronização de arquivos entre chats e os dois repositórios já existentes, pois o GitHub não atualiza automaticamente Fontes do ChatGPT;
- qualidade jurídica de cada dispositivo, vigência atualizada e direito comparado setorial.

**Estado operacional apto a iniciar módulos** não equivale a eliminar essas questões. Elas devem alimentar o inventário, não bloquear toda a pesquisa.
