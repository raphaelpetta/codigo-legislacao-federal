# Protocolo de execução por camadas e risco — CLF

**ID:** CLF-GOV-020 · **Data:** 15/10/2026 · **Estado:** proposta operacional, sem reforma normativa ratificada. Complementa CLF-GOV-005, 017, 018 e 019.

## Finalidade
Produzir corpus codificado único progressivamente utilizável como **proposta**, sem sacrificar a classificação C0/C1/M/Q, rastreabilidade origem→destino, vigência, direitos, competência, transição nem controle de decisões. A classificação de 48 títulos/273 módulos é hipótese organizacional revisável; não há prova atual de inventário exaustivo.

## Trilhas paralelas
1. **Cobertura:** inventário de fontes normativas oficiais por identificador, data e dispositivo; reconciliação de versões e remissões; atribuição provisória a módulos; lacunas expressas em vez de ausência inferida.
2. **Reconstrução e reforma:** reconstruir direito vigente, interpretação juridicamente relevante e funcionamento material; comparar manutenção, correção de execução, reforma pontual e mudança estrutural de modo proporcional ao risco.
3. **Corpus experimental:** produzir **texto único de trabalho** com identificadores estáveis, C0/C1/M/Q por dispositivo e variantes condicionais. Nenhuma transposição é juridicamente equivalente só por ser literal, nem a redação experimental revoga lei.
4. **Validação e positivação:** testar direitos, especialidades, competência, iniciativa, espécies, quóruns, eficácia, precedentes e transição. A implementação formal é uma trilha própria, ligada a DEC-016, sem bloquear as anteriores.

## Separação dos produtos, sem redução de DEC-001
**Corpus codificado único:** produto jurídico-editorial completo e rastreável, com remissões, normas gerais e especiais e reformas explicitadas; objetivo DEC-001 permanece integral. **Plano de positivação:** matriz de veículos legal-constitucionais sob CF/1988 e, distintamente, sob Constituição hipotética; atos competentes, reservas de iniciativa, votação, veto, revogação, vacatio e continuidade. DEC-016 está `PENDENTE`. **Não** converter corpus documental em lei nem dizer que múltiplos diplomas satisfazem definitivamente DEC-001 sem deliberação.

## Estados de progresso (independentes da ratificação)
`NAO_EXAMINADO`, `MAPEADO` (recorte e fontes com ressalvas), `RECONSTRUIDO` (direito vigente e efeitos no recorte), `PROPOSTO` (alternativas e minuta), `INTEGRADO_PROVISORIO` (corpus experimental e concordância), `AUDITADO_NO_RECORTE` (verificações exigidas feitas). Registrar recorte/percentual apenas com denominador comprovável. A marca `PLANEJADO` do catálogo legado é **fotografia inicial e não representa trabalhos em PR**; consultar `catalogo/04_FRENTES_EM_EXECUCAO.csv` e os próprios PRs atuais.

## Risco por efeito
- **R1:** identificação e reprodução documental com mínima alteração aparente; conferência de fonte, versão, estrutura e rastreabilidade; **sem certificação de equivalência jurídica automática**.
- **R2:** consolidação técnica ou redação com risco interpretativo e interações setoriais; exigir teste jurídico/temporal, especialidades e jurisprudência pertinentes.
- **R3:** alteração material em direitos, sanções, competências, tributação, processo e garantias, desigualdade, grupos vulneráveis, transição irreversível; exigir crítica adversarial independente, impacto, casos reais, controles constitucionais e revisão humana para validação de alto risco.

Classificação por **efeito** e promoção para R3 quando houver possível perda de proteção, não por facilidade de coletar documentos. A técnica de pesquisa permanece interdisciplinar, com profundidade proporcional, sem ornamentação comparativa.

## Saída de pesquisa e bloqueios
Responder: o que se verificou? quais alternativas com objeções sérias? o que falta com potencial de mudar a conclusão? qual destino dos dispositivos/garantias? C0/C1/M/Q por efeito? qual decisão requer usuário? Saídas `APTO_PARA_PROPOR`, `PESQUISA_FOCAL`, `DEPENDENCIA_MATERIAL`, `INVARIANTE_EXECUTAVEL` ou `SUBMETER_ESCOLHA`. Não converter ignorância em certeza; não repetir pesquisa sem nova hipótese decisiva.

Decisão/credencial/CI bloqueia apenas a operação dependente. Registrar e seguir por outra unidade independente, preferencialmente com fila de três tarefas executáveis. No máximo uma tentativa diagnóstica por ciclo para erro técnico persistente sem hipótese nova. Manter em princípio **duas frentes substantivas ativas no CLF** e uma de interface CF–CLF, salvo fundamentação em produtividade.

## Inventário parcialmente automatizado e auditoria
Coletar, onde possível, metadados e textos oficiais com proveniência (`id_fonte`, versão, dispositivo, URL, data consulta, hash, alterações, destino, grau de verificação); deduplicar por identidade e versão, sem presumir vigência. Distinguir extração de textos, reconstrução histórica da norma, interpretação e equivalência material; marcar lacunas `A_VERIFICAR`. Auditoria por amostra pode testar a **qualidade do extrator**, mas não autoriza declarar disposições não conferidas como equivalentes ou vigentes. Nunca publicar credenciais ou dados pessoais.

## Como encerrar uma unidade
`MAPEADA` não equivale a `AUDITADA`. Antes de encerrar juridicamente o recorte, comprovar universo de fontes declarado, vigência e efeitos, destino de cada unidade, preservação de direitos/obrigações e exceções, testes materiais adequados, plano de transição e revisão independente cabível. Aceitar conclusão `Q` bem delimitada e prosseguir em outras partes; `Q` não é revogação, autorização de merge normativo ou equivalência C0-J.

## Integração e métricas
Em cada rodada, priorizar **ganho substantivo de cobertura ou integração**, registrar FEITO/PENDENTE/PRÓXIMO, fontes, SHAs e PR. PR de pesquisa pode ser integrado após revisão sem aprovar proposta legislativa. Evitar anexos cronológicos repetidos ao quadro geral; usar painel compacto das frentes e Git como histórico. Medir por unidades normativas/efeitos com denominador efetivamente aferido, não por número bruto de módulos ou testes. Revisar status a cada quinze dias e auditar a capacidade operacional observada antes de fixar prazo global.

**Interface CF:** operar conforme [CF-GOV-017](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/blob/main/governanca/17_EXECUCAO_CAMADAS_E_AUDITORIA.md), sem importar propostas constitucionais como direito vigente. Link futuro condicionado à integração dos respectivos PRs.
