# Protocolo de desenvolvimento, auditoria e integração

**ID:** CLF-GOV-005 | **Versão:** 0.2 (operacional) | **Data:** 13/10/2026

## 1. Antes de iniciar qualquer módulo

1. Ler `01_CARTA_ARQUITETURA.md`, `04_REGISTRO_DE_DECISOES.md`, `02_INDICE_48_TITULOS.csv` e as linhas relevantes do `03_CATALOGO_MODULOS.csv`.
2. Definir o recorte do regime jurídico, interfaces com outros módulos e data de corte da pesquisa.
3. Consultar fontes normativas oficiais vigentes; indicar data de atualização e dispositivos realmente lidos. Não afirmar cobertura integral sem inventário demonstrado.
4. Ler a versão atual do Título 01 quando regras gerais forem afetadas; não reproduzir mecanicamente propostas antigas.

## 2. Ciclo do módulo

**F0 — Escopo:** problema, fronteiras, dependências, outros regimes atingidos.

**F1 — Inventário:** listar fontes originais e alterações, vigência, efeitos transitórios, normas especiais e lacunas de cobertura. Cada lei e artigo do recorte recebe destino preliminar.

**F2 — Modelo vigente:** reconstruir pressupostos, sujeitos, obrigações, competências, sanções, procedimentos e exceções, distinguindo texto legal de interpretação jurisprudencial.

**F3 — Pesquisa crítica:** direito comparado, doutrina e estudos empíricos pertinentes; testar validade e contexto das referências; evitar transplantação automática.

**F4 — Decisões:** apresentar alternativas com consequências e incertezas. Marcar conflitos não resolvidos `Q`.

**F5 — Minuta:** redigir na estrutura do Código, preservar conceitos compartilhados; marcar C0/C1/M/Q por dispositivo ou bloco.

**F6 — Concordância:** tabela de origem x destino x classificação x fundamento. Sem fonte sem destino e sem destino sem fonte ou reforma expressa.

**F7 — Testes:** simulações intertemporais, constitucionalidade, competências, exceções, remissões, direitos adquiridos, procedimentos, sanções e redundâncias.

**F8 — Revisão adversarial:** tentar identificar exclusão de direitos, agravamento involuntário, confusão entre fontes, ambiguidades e normas conflitantes.

**F9 — Proposta de integração:** entregar nota de mudanças, conflitos, arquivos versionados e impacto em módulos vizinhos; NÃO atualizar unilateralmente os documentos centrais.

## 3. Portas de qualidade

- `PLANEJADO`: escopo preliminar, sem pesquisa suficiente.
- `INVENTARIADO`: fontes relevantes registradas, com lacunas explícitas.
- `AUDITADO`: direito vigente e alternativas reconstruídos e documentados.
- `REDIGIDO`: minuta e concordância completas.
- `REVISADO`: passou por teste adversarial; pendências declaradas.
- `INTEGRADO`: interfaces verificadas; alterações centrais aprovadas.
- `ESTABILIZADO`: congelado na versão de referência, sujeito a mudanças rastreadas.

`ESTABILIZADO` é um status do **anteprojeto**. Não equivale a validado pelo STF, aprovado pelo Congresso ou vigente.

## 4. Revisões cruzadas obrigatórias

Sempre verificar relação com:
- T01 (vigência, interpretação, consolidação e publicação);
- Constituição (competência, espécie, direitos fundamentais);
- procedimentos gerais (administrativos, civis ou penais);
- sanções e responsabilidade;
- legislação especial de proteção de pessoas;
- normas transitórias e compatibilidade de efeitos passados.

## 5. Processo de alteração transversal

Um módulo propõe `CR-AAAA-NNN` com:
- texto vigente e proposto;
- motivo e evidência;
- categorias C0/C1/M/Q;
- módulos dependentes;
- impacto histórico e transitório;
- testes que precisariam ser repetidos;
- efeito sobre índice, glossário e remissões.

O chat central registra a decisão no `04_REGISTRO_DE_DECISOES.md`, incrementa a versão dos documentos necessários e comunica os módulos atingidos. Não editar vários arquivos de referência com mudanças simultâneas não reconciliadas.

## 6. Regras de prova

- Citar fontes oficiais para legislação e jurisprudência, inclusive número, dispositivo e data de consulta.
- Não inventar acórdãos, números de processo, leis, dispositivos nem resultados empíricos.
- Distinguir direito vigente, inferência jurídica, interpretação controversa e proposta de política legislativa.
- Não afirmar que uma regra foi revogada tacitamente só por haver aparente conflito.
- Usar o texto completo relevante; resumos de conversa são auxiliares.

## 7. Diretriz transversal: pesquisa crítica e reforma

A orientação substantiva detalhada consta de `governanca/13_DIRETRIZES_PESQUISA_E_MODERNIZACAO.md` (v0.2 proposta). Cada módulo investigará, na profundidade proporcional ao risco e à matéria: (i) evolução histórica e institucional; (ii) doutrina e jurisprudência brasileira, internacional e comparada relevantes; (iii) modelos jurídicos estrangeiros e condições de transplante; (iv) evidências jurídicas, políticas, econômicas, sociais e científicas; (v) funcionamento real e problemas de implementação; (vi) lacunas, antinomias aparentes ou reais, obsolescências, redundâncias e jurisprudencialização de questões ainda não legisladas.

A etapa F3 não é uma formalidade comparatista: exige critérios claros de seleção de fontes e aferição de pertinência. Na F4, comparar **manter, corrigir aplicação, reforma pontual, alternativa não legislativa e reforma estrutural** quando cabíveis. Testar o melhor argumento contrário. Registrar grau de confiança e a distinção entre fato, inferência, juízo jurídico e escolha normativa.

Quando o módulo identificar ausência legislativa, não presumir que há lacuna no direito; distinguir decisão consciente de não legislar, interpretação que supre questão, falha de execução e lacuna efetiva. Jurisprudência não é automaticamente texto codificado; depende de estabilidade, natureza do entendimento e adequação de positivação.

A pesquisa pode justificar alterações materiais amplas `M`, inclusive novos institutos, simplificação ou eliminação de estruturas, mas **nunca ocultar** essas mudanças sob `C0` ou `C1`. O diagnóstico integral não obriga a reforma: manutenção fundamentada é resultado legítimo.

Aplicar análise ex ante proporcional ao impacto, revisão institucional e eventual indicadores para avaliação posterior de reformas significativas. Tratar direitos, igualdade, devido processo e legitimidade democrática como parâmetros próprios, não redutíveis a cálculo monetário.

No interfaceamento com o projeto constitucional independente, a CF/1988 continua referência exclusiva do direito vigente e o anteprojeto é cenário condicional, sem importar decisões de outro projeto.

**Atualização metodológica em uso:** reconhecer essas regras no roteiro F0–F9 e no dossiê de cada módulo; eventual modificação de escolhas relevantes exige governança e registro central, não atualização automática por chats.

## 10. Prestação de contas e continuidade obrigatórias por rodada (14/10/2026)

Aplicar em TODOS os módulos e pesquisas a [regra de continuidade](18_PROTOCOLO_CONTINUIDADE_POR_RODADA.md): ao final de cada ciclo registrar no mesmo PR/branch **FEITO / PENDENTE OU NÃO VERIFICADO / PRÓXIMO PASSO EXECUTÁVEL**, com versão `main` antes/depois, fonte normativa, C0/C1/M/Q, conflitos, estado CI, módulos afetados e interface CF. Usar [modelo de continuidade](../modelos/20_PACOTE_CONTINUIDADE.md); concluir texto na conversa sem gravar arquivo não equivale a persistir handoff. O estado documental não é prova de conclusão jurídica nem de revogação segura.

## Complemento transversal de progressividade decisória — 15/10/2026

Em F4, F8 e F9 aplicar [CLF-GOV-019](19_PROGRESSIVIDADE_DECISORIA.md): existe presunção de submeter à decisão a opção suficientemente fundamentada, sem pesquisa indefinida de alternativas sem potencial material de mudar a escolha. Quando faltar prova decisiva ou houver dependência, delimitar lacuna e critério de saída. Garantias, classificação C0/C1/M/Q, C0-J, concordância origem–destino, regimes especiais, veículo normativo e DEC-016 continuam exigindo validação própria. Não equiparar minuta, CI, merge ou preferência a aprovação jurídica ou material.
