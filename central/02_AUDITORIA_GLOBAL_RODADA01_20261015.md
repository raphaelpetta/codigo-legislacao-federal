# CLF — auditoria global e plano executivo da Central (rodada 01)

**Corte documental:** 15/10/2026 · **Classificação:** evidência operacional em branch draft, não homologação legislativa.
**Vínculos:** [issue CLF #48](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/48), [PR CLF #49](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/49), [central CF #103](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/103).
**Matriz primária desta rodada:** [48 títulos auditados](01_MATRIZ_AUDITORIA_48_TITULOS_20261015.csv). Toda a cobertura abaixo se refere somente à **evidência de pesquisa e produto demonstrada nas branches consultadas**, e não à fração total das leis federais brasileiras.

## 1. Baselines, pesquisas e produto verificados

- `main` CLF (árvore de corte `16fba172c875c7a0de388288fe70005c944021d6`): índice provisório de **48 títulos / 8 partes / 273 módulos**. Material documental setorial em `modulos/T01/M04` e `modulos/T07/M03` não equivale a um Código redigido.
- [PR #45](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/45), HEAD `2a4d1eefa864f44435aec70ed0cc55a96b718b64`: fonte setorial T07, `integracao/25_...` e `integracao/26_...`. **215 IDs de origem**, **214 destinos positivos distintos**, **1 registro histórico art. 70**, **78 artigos experimentais**. Classes preliminares: **203 C0-T locais**, **11 C1 potenciais/Q**, **1 histórico**. **215/215 Q_SEM_C0_J**, nenhuma M homologada e nenhuma revogação.
- [PR #49](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/49), branch `coord/central-clf-produto-vivo-20261015`: única vista de Livro integral, T07; arquivo original continha cabeçalho de cautelas seguido do **texto setorial exato** do PR #45. A partir desta rodada, manifesto e gerador controlam esta correspondência.
- [PR #46](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/46), draft: governança, progressividade, `DEC-018` e plano diretor. Reconciliar metodologicamente, sem sobrescrever ou pressupor merge.
- [PR #50](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/50), draft: fontes-âncora **candidatas para os 48 títulos**, não inventário verificado de dispositivos, vigência ou conteúdo.
- [PR #38](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/38) T24, [#32](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/32) T25, [#41](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/41) T29 e [#43](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/43) T43 têm pesquisas e inventários setoriais em **draft**, sem livros completos no corpus.
- [PR #47](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/47): interface T07–T43 × CF M07, com gates de destinatários, ciência e canais alternativos; ainda sem decisão constitucional ratificada.

**Cobertura de evidência (não do direito positivo):** seis títulos (T01, T07, T24, T25, T29, T43) com pesquisa setorial claramente identificada nesta auditoria; **42 sem PR setorial individual comprovado nesta amostra** (não significa ausência absoluta de pesquisa). Dos 48, **um** possui Livro em vista experimental e **47** ainda não. C0-J homologadas no produto: **zero**. O fato de PR #50 sugerir leis para todos os títulos não os torna materialmente inventariados.

## 2. Auditoria específica do Livro T07 — condições de integração

**Integridade textual:** a prévia existente do PR #49 concatena exatamente um cabeçalho editorial e o texto do PR #45. Manifesto `produto/fontes/T07_M03_v4.json` fixa PR, commit, caminho e **SHA de blob Git** do livro e da concordância; gerador `scripts/gerar_produto_experimental.py` confere 215 registros, 78 artigos consecutivos, unicidade de IDs e destinos, as classes textuais, estado jurídico Q e equivalência integral da vista gerada. `--write` somente regenera a vista derivada; jamais edita a origem setorial. O workflow dedicado depende de checkout do commit fixado. **Gate automatizado não é certificação jurídica.**

**As 11 alterações C1 potenciais**, exigindo prova individual de efeito de referente ou expressão, pertencem a: art. 1º caput, §§1º–2º, três definições do §2º; art. 36 caput (remissão art. 37); art. 49-A §1º, 49-B caput e 49-D caput; art. 69 caput. Correspondência individual no CSV setorial:
`P13-01-C`, `P13-01-P1`, `P13-01-P2`, `P13-01-P2-I`, `P13-01-P2-II`, `P13-01-P2-III`, `EXP17-36-C`, `C18-49-A-P1`, `C18-49-B-C`, `C18-49-D-C`, `P19-69-C`.

**Portas jurídicas irrenunciáveis** (a verificar por dispositivo e efeito):
1. **Âmbito e especialidade:** Lei 9.784/1999, arts. 1º e 69. A lei geral federal é apenas subsidiária diante de processos administrativos especiais; a mudança `desta Lei` → `deste Livro` pode modificar alcance se a nova posição sistemática abranger destinatários distintos.
2. **Processo e garantias:** direitos de participação, contraditório, ampla defesa, motivação, competência indelegável, prazos, recursos e revisão de sanção, direito à prova e tratamento de vulnerabilidades; competência e tipos sancionatórios de regimes especiais não são absorvidos silenciosamente.
3. **Comunicação digital e dados:** Lei 14.129/2021, arts. 2º, 42–43, e regime de opção pelo canal; comprovação de envio/recebimento não é presunção universal de leitura, ciência ou tempestividade. Conferir LGPD, LAI, normativos específicos e destinatários de cada modalidade.
4. **Cronologia:** preservar efeitos de versões de 1999/2006/2009/2021, vetos, edições e controvérsias de vigência; art. 70 original é **histórico**, não cláusula nova de vigência. LINDB e direito intertemporal condicionam invalidação e alteração de orientação.
5. **Codificação:** LC 95/1998, arts. 13–14, impõe pressupostos específicos para uma consolidação sem mudança de alcance e com justificação documental. O projeto reformista deve distinguir redação editorial C0, adaptação C1 e alteração material M, preservando eventuais veículos competentes.

Fontes oficiais iniciais (conferência focal nesta rodada, **não cotejo DOU linha a linha**): [Lei 9.784/1999 atualizada, Câmara](https://www2.camara.leg.br/legin/fed/lei/1999/lei-9784-29-janeiro-1999-322239-normaatualizada-pl.html), [Lei 14.129/2021, Planalto](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14129.htm), [LC 95/1998 atualizada, Câmara](https://www2.camara.leg.br/legin/fed/leicom/1998/leicomplementar-95-26-fevereiro-1998-363948-normaatualizada-pl.html).

**Resultado jurídico:** a prévia é apta à **visualização experimental, vinculada à versão fixada**. Não é apta a ser aprovada como C0-J, a produzir revogações, substituir integralmente regimes especiais ou dispensar decisão de espécie, competência e iniciativa. A DEC-016 bloqueia a **positivação**, não o ensaio documental.

## 3. Fila dinâmica — cobertura horizontal com entregas verticais

| Faixa | Frente e evidência disponível | Próxima entrega normativa/documental concreta | Porta de risco |
|---|---|---|---|
| **P0** | T07.M03 / PR #45–#49 | Regeneração controlada, C1 11/11, pareceres por efeito, matriz de especialidade e transições | Risco de referentes, efeitos sobre administrados, direito a defesa |
| **P1-A** | T24.M01 / PR #38 | Escolher bloco conservador de CPC com espelho literal e localização primária; primeiro segundo Livro de ensaio | Contraditório, gratuidade, honorários, tutela coletiva, remissões |
| **P1-B** | T25 / PR #32 | Escolher núcleo Parte Geral CP/CPM com separação de regimes; primeira minuta de Livro penal | Legalidade estrita, retroatividade benigna, culpabilidade, dosimetria |
| **P1-C** | T29.M01 / PR #41 | Recorte RGPS 8.212/8.213: harmonização somente após prova da assimetria e efeitos temporais | Direito adquirido, fontes de custeio, benefícios, transições |
| **P1-D** | T43.M04 / PR #43, #47 | Versão de um bloco digital com âmbito, ciência e garantia de canal alternativo | Acessibilidade, dados sensíveis, prova de comunicação |
| **P1-E** | T01.M04 / main, PR #46 | Matriz de viabilidade e atos necessários para DEC-016, separada da redação do corpus | CF vigente, reserva de LC/LO, iniciativa e sanção/veto |
| **P2 — expansão** | T12, T05, T13, T28, T37, T48 (fontes candidatas PR #50) | Abrir inventários oficiais com primeira faixa limitada em tributário, eleitoral, civil, trabalho, ambiental e migratório, em rodadas alternadas | Transições tributárias, anualidade eleitoral, garantias laborais, competências ambientais |

**Rotação entre as oito partes:** T01 (I), T05 (II), T07 (III), T13 (IV), T24/T25 (V), T28/T29 (VI), T37/T43 (VII), T48 (VIII) são pontos de entrada *candidatos*, não quotas iguais nem decisões de arquitetura. Nenhuma parte fica invisível porque só haja pesquisa setorial em seis títulos.

**Critério reavaliável ao início de cada rodada:** (a) lacuna demonstrada relativa ao universo do recorte, não aos 273 módulos; (b) disponibilidade de fonte oficial e de pesquisa reaproveitável; (c) risco de supressão de garantias; (d) potencial de formar texto novo no corpus; (e) dependências com outros Livros e CF; (f) custo de execução e bloqueios externos. Evitar novas séries exclusivamente em T07 se outra frente já dispõe de texto suficiente para minuta de ensaio.

**Meta de produto no ciclo seguinte:** segundo recorte em vista integrada (priorizar T24 ou T25 conforme porte/verificabilidade) **e** inventário efetivo de ao menos um título ainda sem frente setorial comprovada (por exemplo T05/T13/T28/T37/T48), com universo declarado e fonte oficial. Não atribuir números de cobertura até medir o denominador. Para textos normativos C1/M, usar variantes com solução conservadora baseline e deliberação expressa.

## 4. Estado do produto, formalização e interface CF

- **DEC-001:** corpus único temático, com fonte original por unidade e versões recompiláveis; confirmado.
- **DEC-016:** veículo, iniciativa, espécie, sanção/veto, revogações expressas, eficácia e garantias intertemporais; **PENDENTE**. Manter trilhas paralelas de positivação por atos competentes sem impor solução.
- **DEC-018 / PR #46:** progressividade metodológica, não licença para homologar conteúdo jurídico.
- **CF #103:** levantar apenas dependências relevantes de CF M07/M06 e temas de direitos/sanções; registrar texto CF vigente versus hipóteses da revisão e aguardar deliberação constitucional independente. O CLF não pode pressupor norma CF futura aprovada.
- **Controle de integração:** PRs #45/#46/#49/#50 modificam branches distintas; reconciliar antes de merges. Nenhum PR draft vale como `main` e CI estrutural não equivale a revisão de mérito. CI recentemente reportada como **falha antes da execução das etapas** no PR #45; necessidade de reavaliar em HEADs atuais.

## 5. FEITO / PENDENTE / PRÓXIMO

**FEITO nesta rodada (branch do PR #49):** auditoria documental e cruzamento dos 48 títulos com fontes-âncora do PR #50 e frentes setoriais; verificação de correspondência literal integral prévia–fonte setorial; catálogo de 11 deltas C1; manifesto com dois blob SHAs; gerador e workflow de validação independente; matriz tabular e este plano com fontes e riscos.

**PENDENTE:** executar workflow (ambiente CI), demonstrar equivalência C0-J por recorte, confirmar DOU e remissões externas, completar inventários oficiais dos 42 títulos sem evidência setorial individual nesta auditoria, reconciliar branches/PRs, aprovar reformas M e decidir DEC-016. Nenhuma alteração material foi homologada.

**PRÓXIMO:** verificar CI do PR #49 sem atribuir sucesso presumido; resolver primeiro gate dos 11 C1; selecionar transposição com base literal de T24 e segundo título ainda não iniciado (T05/T28/T37); publicar handoff atualizado na issue #48; encaminhar à CF #103 somente dependências jurídicas com ID e hipótese, sem decisões de mão única.
