# Carta de arquitetura do Código da Legislação Federal

**ID:** CLF-GOV-001  
**Versão:** 0.1  
**Estado:** minuta inicial de governança, sujeita a revisão  
**Atualizado:** 13/10/2026

## 1. Objetivo e limites

1. Construir **um Código único** com localização temática de toda a legislação federal geral e permanente e, gradualmente, redação legislativa consolidada e modernizada.
2. Tratar **Constituição** como fonte superior externa ao corpo infraconstitucional.
3. Distinguir legislação federal propriamente dita de normas nacionais aprovadas pela União; registrar a espécie normativa, competência e limites constitucionais de cada disposição.
4. Tratar normas estaduais e municipais como camadas federadas de consulta, não como texto legislativo federal.
5. Manter acervo separado para normas temporárias, individuais, orçamentárias, revogadas, regulamentos e tratados com suas qualificações jurídicas. O acervo integral será pesquisável.
6. Conservar unidade sistemática mesmo quando diferentes partes precisem de atos legislativos distintos para implementação.

## 2. Estrutura preliminar

O Código está **provisoriamente** organizado em **8 partes e 48 títulos**, especificados em `02_INDICE_48_TITULOS.csv`. O inventário completo ainda poderá revelar títulos insuficientes, redundantes ou mal situados.

A unidade editorial final é parte > título > livro > capítulo > seção > dispositivo. A unidade de trabalho é o **regime jurídico** (`Txx.Myy`), independentemente das fronteiras dos diplomas atuais.

## 3. Quatro categorias de alterações

- **C0 — Transposição fiel:** manter alcance e efeitos, mudando apenas a localização; exigir correspondência com fonte oficial.
- **C1 — Reforma técnica a direito constante:** redigir/organizar de modo diferente com pretensão de equivalência, sujeita a testes; se falhar, classificar como M ou Q.
- **M — Reforma material proposta:** mudança jurídica intencional; exigir motivação, alternativas, implicações intertemporais e direitos afetados.
- **Q — Questão controvertida:** sem solução estabilizada; não ocultar e não decidir editorialmente como se fosse direito pacífico.

Nenhuma supressão é silenciosa. Toda disposição original deve ter destino rastreável: incorporada, fundida, mantida fora do corpo permanente, revogada por ato competente ou pendente de decisão.

## 4. Princípios jurídicos de elaboração

- Constitucionalidade, competência, reserva de espécie legislativa, direitos fundamentais e segurança jurídica.
- Não confundir interpretação editorial com decisão jurisdicional ou revogação legislativa.
- Preservar efeitos anteriores e transições quando pertinentes.
- Uma localização primária para cada disposição, com referências temáticas cruzadas; preservar regimes protetivos integrados sempre que necessário.
- Remissões devem apontar a identificadores verificáveis; código proposto não substitui fonte original antes da formalização legislativa.
- Uso transparente de evidências e de direito comparado: distinguir fatos, hipóteses, valores e opções legislativas.

## 5. Governança

- **Chat central:** recebe propostas de alteração arquitetural, registra decisões e integra módulos.
- **Chat de módulo:** reconstrói o regime vigente, inventaria as fontes, propõe e testa reformas, sem editar decisões de outro módulo.
- **Revisão de integração:** examina dependências, contradições, remissões, conflitos e efeitos intertemporais.
- **Registro central:** apenas mudanças aprovadas podem alterar a versão de referência compartilhada.

Quando um módulo precisa modificar norma central ou módulo vizinho, produzir uma solicitação de mudança identificando razão e impacto; nunca reescrever silenciosamente.

## 6. Critério de qualidade

Todo módulo deve ter inventário, análise de vigência, dossiê de pesquisa, diagnóstico, alternativas, minuta codificada, tabela artigo-a-artigo de correspondência, testes jurídicos e revisão adversarial.

`REDIGIDO` não significa `VALIDADO` nem `LEGISLADO`. Projetos gerados por IA são propostas e precisam de conferência independente para utilização oficial.

## 7. Atualização

Alterações nesta carta ou no índice geral exigem número de versão, motivação, lista de módulos afetados e nota de migração. Nenhuma mudança arquiva direitos, obrigações ou textos anteriores sem documentação correspondente.