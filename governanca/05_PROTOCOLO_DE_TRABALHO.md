# Protocolo de desenvolvimento, auditoria e integração

**ID:** CLF-GOV-005 | **Versão:** 0.1 | **Data:** 13/10/2026

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