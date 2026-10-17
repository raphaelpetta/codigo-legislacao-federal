# CLF-GOV-019 — Construção, deliberação e fechamento progressivos

**Vigência operacional:** 16/10/2026 · **Decisão metodológica:** DEC-018, confirmada expressamente pelo usuário. **Aplicação:** projeto CLF, sem alterar a CF independente. **Natureza:** rito de gestão do anteprojeto; não ato legislativo, homologação jurídica, aprovação de mudança M nem encerramento de DEC-016.

## 1. Princípio

Pesquisa, redação, auditoria, integração, deliberação e fechamento **coexistem**. A pergunta de cada rodada é: *qual avanço concreto oferece o maior ganho marginal global para a qualidade e a conclusão do CLF, considerados riscos, custos, direitos e dependências?* Evitar tanto acumular minutas sem decisão quanto decidir sem condições de segurança. Fechamento de recorte não fecha automaticamente Livro ou Código.

O protocolo **F0–F9 permanece íntegro** como método de produção; a deliberação de questão madura é **ramo disponível em qualquer fase**, sem exigir que todo o módulo tenha terminado F9. A fila decisória tem uma unidade própria: questão identificável (expressão, artigo, efeito, bloco ou escolha transversal) com fronteira e interfaces claras. A pesquisa continua nas partes ainda não deliberáveis, horizontal e verticalmente, sem interromper outros trabalhos.

## 2. Seleção dinâmica de trabalhos H/V/I/D/F

A cada rodada verificar o SHAs da `main` e ramos setoriais, o estado de corpus e a fila de questões. Comparar opções reais:

- **H — Horizontal:** abranger fontes/títulos/regimes ainda descobertos insuficientemente.
- **V — Vertical:** corrigir fonte, vigência, especialidade, remissão, direitos, implementação, precedente ou melhor objeção.
- **I — Integração:** reduzir divergências/PRs, regenerar produtos, corrigir cadeia de proveniência e testar CI.
- **D — Deliberação:** estruturar e encaminhar alternativas de **questão madura**, inclusive manter regra vigente/não legislar.
- **F — Fechamento:** estabilizar redação de opção aprovada e, quando cabível, completar revisão jurídico-material e integração no anteprojeto deliberado.

Justificar sucintamente escolha **e alternativa preterida** considerando ganho normativo/social, custo efetivo (inclusive despesas futuras evitadas, quando pertinente), risco/gravidade, maturidade da fonte, efeito desbloqueador, esforço e reversibilidade. **Sem quotas fixas** nem prioridade automática por número de artigos ou PRs. Preferir pesquisa **focal**, direcionada à incerteza que pode modificar a decisão. Pesquisa extra sem potencial material de alterar a escolha não deve bloquear deliberação; dúvida que afete segurança jurídica, competência, direito ou efeitos impede **fechamento indevido**, embora permita discussão condicionada.

## 3. Três eixos independentes por questão

**Maturidade:** `TRIAGEM` (delimitar); `PESQUISA_FOCAL` (incerteza relevante e verificável); `APTO_A_DELIBERAR` (alternativas, contrafactual de manutenção, efeitos, objeção, garantias, dependências e fonte suficiente); `BLOQUEADO_POR_DEPENDENCIA` (identificar exatamente o fato/decisão que impede etapa). Uma questão **parcialmente** madura pode ser dividida em subquestões, sem declarar que a decisão completa está apta.

**Decisão:** `NAO_SUBMETIDA`; `SUBMETIDA`; `CONFIRMADA`; `CONFIRMADA_CONDICIONAL`; `REJEITADA`; `REABERTA`. Toda confirmação material ou estrutural relevante exige manifestação **expressa e específica** do usuário e registro de alternativa escolhida, limites, efeitos e evidência de aprovação. Ao apenas registrar o método DEC-018 não se aprova qualquer dispositivo. **Letra isolada** autoriza rodada operacional, nunca decisão normativa, escolha de veículo DEC-016, C0-J/M ou mudança de direitos. Ausência de resposta mantém `SUBMETIDA` ou `NAO_SUBMETIDA`, nunca aprovação tácita.

**Fechamento editorial-jurídico (gerencial, independente de F0–F9):**
- `FC0_ABERTO`: questão identificada, sem opção material aprovada.
- `FC1_APTO_A_ESCOLHA`: condições documentadas para submeter alternativas; não constitui decisão.
- `FC2_ESCOLHA_CONFIRMADA`: opção específica aprovada para o **projeto**, com limites, justificativa e registro. Não prova sua validade legal.
- `FC3_REDACAO_ESTABILIZADA`: texto e concordância de opção aprovada, com teste adversarial proporcional, referenciados por SHA; pode ser reaberto fundamentadamente.
- `FC4_AUDITORIA_JURIDICA_INDEPENDENTE`: revisão humana independente ou evidência independente identificada sobre os efeitos pertinentes, portas A/B/C e eventuais Q residuais; não equivale, por automatismo, a C0-J.
- `FC5_INTEGRADO_ANTEPROJETO_DELIBERADO`: interface e versão consolidadas, efeitos/rastreio preservados, decisão do projeto rastreável. Não significa promulgado, vigente ou revogado.

O nível gerencial não substitui classe textual/jurídica `C0-T/C0-J/C1/M/Q`, nem status do Livro `INTEGRADO_EXPERIMENTAL_Q`. A `main` pode continuar incorporando material **Q experimental**, sem qualquer FC2 ou FC5. Um FC2 condicionante não suprime bloqueios de FC3–FC5. Questão estrutural sem texto de lei pode ser fechada em sua dimensão organizacional com prova própria, sem classificar C0-J.

## 4. Qualidade, competência e efeitos

A deliberação recebe uma **ficha mínima**: questão precisa, versão da fonte oficial e da `main`, status vigente e histórico, âmbito, espécies e iniciativa, alternativas reais (manter, correção de aplicação, editorial, reforma pontual, não legislar, estrutural quando pertinentes), contrafactual, recomendações, melhores objeções, direitos/garantias, custo global proporcional, efeito temporal e de revogação, remissões/interseções, compatibilidade CF/1988, cenário constitucional futuro explicitamente condicionado, confiança, evidências, impacto e próximo teste.

Manter as **Portas A/B/C** da política existente. R1 para efeitos editoriais menores, R2 para possível alteração de âmbito, R3 para direitos, sanção/penal, processo, tributo, previdência, saúde, iniciativa, vulnerabilidade e transição. **Autorrevisão de IA, hash, teste unitário ou CI verde não equivalem a revisão jurídica independente.** Para FC4 e fechamento material é necessária prova independente específica; dúvida relevante pode continuar Q mesmo depois de decisão de política legislativa.

A coordenação técnica pode produzir diagnósticos, escolher próximo recorte, recomendar e **integrar melhoria não substantiva após CI**. Escolhas relevantes de política normativa, espécie, competência, supressão de garantia, texto material novo, renumeração definitiva, revogação e DEC-016 exigem deliberação expressa do usuário. C0-J exige conferência jurídica independente e aprovação expressa aplicável, não resulta da fila. DEC-016 permanece **PENDENTE** até deliberação própria; a DEC-001 continua objetivo, não presunção de constitucionalidade de veículo único.

## 5. Fila, trilha de decisão e reabertura

**Fonte única:** [`19_FILA_QUESTOES_DELIBERAVEIS.json`](19_FILA_QUESTOES_DELIBERAVEIS.json). Os itens distinguem `maturidade`, `decisao.estado`, `fechamento`, `classe_juridica`, riscos, dependências, alternativas, melhor objeção, próximos insumos e fontes. **Não duplicar** decisões confirmadas em outra tabela gerencial; para confirmação formal de premissa/procedimento ou escolha normativa relevante, usar `04_REGISTRO_DE_DECISOES.md` e referenciá-lo na ficha. Subquestões recebem IDs novos e remissão à questão-mãe. Evitar inundar o usuário com microdecisões: agrupar lote pequeno e coerente.

Aptidão não constitui aprovação. Avanço FC2 exige escolha específica e prova de manifestação; FC3 exige referência à redação, versão e testes; FC4 exige prova independente; FC5 exige registro de integração e compatibilidade. A rotina [`validar_fila_deliberacao.py`](../scripts/validar_fila_deliberacao.py) impede **erros estruturais e promoção silenciosa desses estados**, mas não autentica juridicamente fontes, manifestações ou análises. Os controles podem ser endurecidos com teste próprio à medida que itens amadurecerem, sem relaxar garantias.

Decisão confirmada será premissa operacional da proposta **somente dentro de seu objeto e condições**. Reabrir exige `motivo_reabertura`, fato superveniente ou erro concreto, a decisão afetada, consequências para outros módulos, parecer contrário e proposta de novo estado; registrar evento `REABERTA`, preservando referência e texto anterior. Não reabrir apenas por preferir outra redação. Reabrir não apaga decisão nem prova pretérita.

## 6. Implantação prospectiva e pilotos

A presente implantação cria o rito e semeia **três candidatas não deliberadas**: QD-2026-001 (**DEC-016/T01.M04**, estrutural); QD-2026-002 (**T05.M06, Lei 9.709 arts. 1–2**, revisão documental e fecho conservador); QD-2026-003 (**T07.M03**, efeitos C1/âmbito). Nenhuma está automaticamente `APTO_A_DELIBERAR` e nenhum lote é homologado por semeadura. Os demais módulos e PRs experimentais não são reclassificados retroativamente. É possível abrir nova questão quando ela realmente oferece maior ganho marginal global.

O primeiro ciclo pós-implantação deve produzir **um dossiê decisório delimitado** com fonte/versionamento atualizados, alternativa de conservação e reforma se cabível, objeção mais forte e gate; atualizar sua maturidade no mesmo PR de decisão, sem afirmar aprovação material. Rodadas posteriores continuam H/V/I/D/F conforme ganho marginal. A implantação não transfere poderes nem altera direitos positivos.

**Referências:** [política A/B/C](POLITICA_CONSOLIDACAO_E_FECHAMENTO_20261015.md), [protocolo de trabalho](05_PROTOCOLO_DE_TRABALHO.md), [registro DEC](04_REGISTRO_DE_DECISOES.md), [continuidade por rodada](18_PROTOCOLO_CONTINUIDADE_POR_RODADA.md), [diretrizes de modernização](13_DIRETRIZES_PESQUISA_E_MODERNIZACAO.md) e [central #48](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/48).
