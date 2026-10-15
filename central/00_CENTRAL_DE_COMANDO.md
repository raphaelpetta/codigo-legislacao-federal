# Central de comando — Código da Legislação Federal
**Corte:** 15/10/2026 · **Estado:** protocolo de execução proposto em PR, sem alteração legislativa ratificada.
**Comando CLF:** https://github.com/raphaelpetta/codigo-legislacao-federal/issues/48
**Interface CF:** https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/103
**Método em elaboração:** CLF PR #46; **fonte do Livro T07 atual:** PR #45 draft, HEAD `2a4d1eefa864f44435aec70ed0cc55a96b718b64`.

## Produto prioritário
O resultado pretendido é UM corpus codificado contínuo, organizado em Partes/Livros/Títulos e dispositivos, com fonte única rastreável; separa-se **produto normativo experimental** da forma jurídico-formal futura de positivação. A decisão **DEC-001** (Código único) mantém-se; a **DEC-016** (veículo de promulgação/espécies/iniciativa) permanece pendente. Nenhuma norma vigente é revogada pela redação do corpus.

**Primeira visualização verificável:** [prévia do Livro T07 — 78 artigos experimentais, 214 unidades textuais positivas](../produto/vistas/T07_PROCESSO_ADMINISTRATIVO_PREVIA.md). Essa prévia é uma **fotografia derivada da branch do PR #45** (fora da main), não novo texto fonte canônico. Alterações futuras devem ocorrer na matriz/fonte setorial, com nova versão compilada e cotejo; não editar duas cópias independentemente.

## Equilíbrio horizontal e desenvolvimento vertical
- **Horizontal:** inspecionar os 48 títulos e seus regimes funcionais como mapa PROVISÓRIO, não denominador de exaustividade; detectar áreas sem inventário e redistribuir atenção por tamanho, lacunas, risco, transições e interfaces.
- **Vertical:** concluir recortes comprováveis (fonte oficial/versão → alcance e especialidades → unidades e efeitos → texto condicional C0/C1/M/Q → integração ao Livro → controle jurídico N:N e transição). Distinguir `C0-T` (cópia textual) de `C0-J` (equivalência jurídica verificada). A existência de um Livro demonstrativo não certifica 214 dispositivos.
- **Rotação:** priorizar a expansão para T24/T25/T29/T43 e outros títulos não cobertos após recortes reais no T07. Não manter três entregas seguidas na mesma matéria se houver outra independente pronta, salvo justificativa explícita por garantia, dependência ou conclusão próxima. Normalmente trabalhar 1–2 recortes com profundidade por rodada.
- **Direito positivo:** legislação federal de competência adequada, natureza legal, vigência, versão, especialidade, regimes temporais e intertemporais. Nada presume recepção de opção constitucional futura, nem qualquer norma especial revogada por consolidação editorial.

## Portas de maturidade, independentes da aprovação
`NAO_MAPEADO` / `MAPEADO` / `RECONSTRUIDO` / `MINUTADO_H` / `INTEGRADO_EXPERIMENTAL` / `AUDITADO_NO_RECORTE`. Cada etapa requer evidência do universo **declarado**; não atribuir proporção de cobertura sem denominador aferido. Status jurídico `C0-T/C0-J/C1/M/Q` separado de etapa e da homologação. `Q` bem fundamentado não bloqueia trabalho independente. Decisão de reforma material/iniciativa/promulgação exige ratificação humana.

## Riscos e salvaguardas
- R1: remissão, tipografia, organização, somente após conferência de efeitos.
- R2: alteração de redação com interpretação material possível, âmbitos e interfaces.
- R3: direitos fundamentais, sanções, tributos, competência/iniciativa, processo, vulnerabilidade, prestações, privação de liberdade, finanças e transição.
- Em qualquer R3, comparar garantias e exceções origem→destino, efeitos, jurisprudência e melhor objeção; auditoria adversarial proporcional, sem pressupor que verificadores automatizados equivalem a conferência jurídica independente.
- Nunca tratar histórico/veto como texto vigente, criar cláusulas de revogação implícita, alterar objeto ou extensão do direito por conveniência editorial; não mesclar texto material na main como aprovado sem autorização.

## Ciclo operacional da central
1. Consultar SHAs reais da main CF e CLF, PRs, fontes, catálogos, status das decisões e issues #48/#103.
2. Identificar três tarefas realmente independentes: cobertura horizontal negligenciada, redação vertical com destino no corpus, bloqueio/decisão transversal.
3. Escolher por impacto verificável no texto e direitos, risco, amplitude, estágio real e dependências; registrar por que a escolha melhora o conjunto sem criar ranking artificial.
4. Registrar versão e proveniência por unidade. Entregar alteração textual concreta, ou reconstrução crítica necessária a um texto; se faltar dado indispensável, documentar Q e trocar de frente.
5. Cotejar diferenças, assegurar concordância N:N, testar remissões; atualizar o quadro de produto só com delta verdadeiro.
6. Encerrar com FEITO/PENDENTE/PRÓXIMO, PR/commit/CI e três próximas entregas desbloqueadas. CI com erro sem etapas não é falha jurídica: testar 1 vez e seguir tarefa não bloqueada.
7. Quinzenalmente reavaliar concentração por título e área, número de unidades com destino comprovado, riscos, qualidade de compilação, partes ainda descobertas e atrito de PR. Sem porcentagens fictícias.

## Primeiro conjunto de trabalhos
1. **T07:** converter o ensaio do PR #45 em fonte consolidável do corpus, após revisões e sem promover 214 unidades a C0-J; priorizar âmbito/ciência/devido processo e especialidades.
2. **T24 e T25:** produzir primeiros recortes textuais de jurisdição e Parte Geral Penal, preservando garantias e reserva legal; não aguardar esgotamento do T07.
3. **T29 e T43:** cobertura seletiva do previdenciário e governo digital para confronto com processo administrativo e direitos fundamentais.
4. **T01.M04:** DEC-016 e estudo autônomo da promulgação; não impede o texto experimental.
5. **Interfaces CF:** M07/M06 ↔ T07/T43, e M00/M03/M14 ↔ T01/DEC-016. Encaminhar à issue CF #103 só as dependências de substância.

[Central CF](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/103) · [Plano diretor CLF PR #46](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/46).

---

## Rodada 01 — entrega verificavel (15/10/2026)

A auditoria de todos os 48 titulos, cruzando o indice da `main`, a vista do PR #49, as frentes PRs #45/#38/#32/#41/#43 e o mapa de 48 fontes-ancora do PR #50, esta documentada em [02_AUDITORIA_GLOBAL_RODADA01_20261015.md](02_AUDITORIA_GLOBAL_RODADA01_20261015.md) e [01_MATRIZ_AUDITORIA_48_TITULOS_20261015.csv](01_MATRIZ_AUDITORIA_48_TITULOS_20261015.csv).

**Ponto de controle:** 6 titulos com pesquisa setorial diretamente evidenciada, 42 sem PR setorial individual demonstrado nesta auditoria; apenas T07 tem vista integral. A matriz de origem do PR #45 tem 215 IDs, sendo 203 C0-T locais, 11 C1 potenciais/Q, 1 historico, **zero C0-J**. A vista passou por cotejo textual integral e recebeu [manifesto Git](../produto/fontes/T07_M03_v4.json), [gerador](../scripts/gerar_produto_experimental.py) e workflow documental. A CI de Actions deste corte falhou sem etapas observaveis e **nao esta certificada**.

**Fila reavaliavel:** P0 T07 integridade e 11 C1; P1 T24/T25 transformacao em novos Livros, T29/T43 recortes de garantia e T01 DEC-016 paralela; P2 T12/T05/T13/T28/T37/T48 como abertura horizontal; nenhuma alteracao M aprovada ou merge. [Issue #48](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/48) permanece central executiva, interface [CF #103](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/103).

## Rodada 02 — corpus com dois componentes e nova frente civil (15/10/2026)

[Relatório completo FEITO/PENDENTE/PRÓXIMO](04_RODADA02_C0_T24_T13_20261015.md) · [Entrada do Código experimental](../produto/00_LEIA_O_CODIGO.md).

**Deltas efetivos:**
- [T07 — 11 pontos C1 com efeitos e alternativas](03_T07_GATE_C1_11_EFEITOS_20261015.csv), cinco críticos, três altos e três editoriais baixos, todos Q.
- [T24 — segundo Livro em vista PARCIAL](../produto/vistas/T24_PROCESSO_CIVIL_PREVIA_PARCIAL.md): 17 artigos/106 unidades (CPC 70–81 e 98–102), manifesto e SHA fixos, concordância 1:1, gerador e validação documental. Nenhum C0-J.
- [T13 — novo inventário civil](../modulos/T13/M01/INVENTARIO_CC_ART1_5_20261015.csv): 19 posições, 16 positivas e três históricas revogadas, interfaces LBI/T24; ainda sem vista.
- [Quadro corrigido](QUADRO_PRODUTO.csv): separa artigos e subunidades para impedir confusão de cardinalidades; total de **95 artigos visíveis / 320 unidades positivas Q nos dois recortes**, 0 C0-J. Pesquisa material demonstrada agora em sete títulos (T01, T07, T13, T24, T25, T29 e T43), sem alegar exaustividade dos outros 41.
- **CI GitHub Actions segue sem comprovação:** workflows de T07/T24 e integridade falham sem etapas visíveis; executar/checkar fora da CI e diagnosticar conta/runner antes do merge.

**Próxima seleção dinâmica:** complementar CPC 82–97 (art.85 integral), testar T07 art.69/1 e remissões, abrir terceiro Livro setorial T25, avançar T13 e interfaces de T43. Nenhuma norma aprovada ou reestruturação definitiva.

## Controles operacionais verificáveis (propostos no PR)
- [Fila com recortes, estados, critérios e reservas](FILA_TRABALHO.csv).
- [Painel calculado exclusivamente do produto no checkout](PAINEL_GERADO.csv) — **presença no produto, não cobertura jurídica global**.
- [Política de integração experimental, ratificação e concorrência](03_POLITICA_INTEGRACAO_E_CONCORRENCIA.md).
- [Verificador e gerador do painel](../scripts/controle_operacional.py) (`--write` / `--check`).
- [Validação local de contingência](../scripts/validar_operacao_local.sh); falha de Actions sem steps não valida nem invalida documentos.
- [Código único de trabalho](../produto/CODIGO_DE_TRABALHO.md). A compilação é uma vista derivada; não editar suas cópias de forma independente.

Os controles acima passam a ser definitivos somente após revisão e integração da documentação. O registro de tarefas não substitui a conferência dos PRs nem a revisão jurídica, e cada reserva é cooperativa.

## Integracao de governanca e do Codigo (atualizacao operacional)
Consultar o [plano de integracao PR #46/#49, T07 e T24](06_PLANO_INTEGRACAO_GOVERNANCA_E_CORPUS.md), a [fila persistente](FILA_TRABALHO.csv), as [portas de integracao experimental](03_POLITICA_INTEGRACAO_E_CONCORRENCIA.md), o [painel calculado](PAINEL_GERADO.csv) e o [indice dos Livros](../produto/fontes/indice_livros.json). O corpus contem T07 integral **somente no recorte da Lei 9.784/1999** e T24 **parcial** (CPC 70–81/98–102), sem homologacao C0-J nem DEC-016. Os workflows devem conferir os compiladores quando mudarem. Nao confundir texto publicado em PR com norma ratificada e nao repetir trabalho setorial ja presente.

## Rodada 03 — terceiro Livro Penal e controle de 75 unidades CPC (15/10/2026)

[Relatório FEITO/PENDENTE/PRÓXIMO](07_RODADA03_CPC75_T07_12_T25_39.md) · [Código de Trabalho unificado](../produto/CODIGO_DE_TRABALHO.md) · [Índice canônico das vistas](../produto/fontes/indice_livros.json).

- **Novo Livro na vista:** [T25 CP1–12](../produto/vistas/T25_PENAL_PARTE_GERAL_CP1_12_PREVIA.md), **12 artigos/39 unidades** a partir do PR #32 e SHA de origem fixado; [concordância](../produto/concordancia/T25_CP_ART1_12_39.csv), [manifesto](../produto/fontes/T25_CP1_12_v1.json) e gerador sob status Q, sem generalizar CP/CPM nem homologar texto M.
- **Expansão vertical sem simular incorporação:** [75 destinos CPC 82–97](../produto/concordancia/T24_82_97_GATE_75_SEM_TEXTO.csv), dos quais **36 do art.85**, mais [parecer de garantias e precedentes](../produto/concordancia/T24_82_97_NOTA_GATE_JURIDICO_20261015.md). As **75 unidades AINDA NÃO ESTÃO EM TEXTO OU NO CORPUS**; bloquear falsa contagem.
- **T07:** [12 hipóteses adversariais de efeitos](06_T07_DOZE_CASOS_ADVERSARIAIS_REMISSOES_E_ESPECIALIDADE.csv) para âmbito, referência, ciência digital e processo especial; todos os 11 C1 continuam Q.
- **Estado visível do Código experimental:** **3 componentes**, **107 artigos**, **359 unidades textuais positivas, 1 histórica**, **0 C0-J**, 48 títulos arquiteturais provisórios. O quadro e painel distinguem artigos, origens e texto; a fila indica T24-002 como trabalho de transcrição pendente, não homologação.
- **Portas:** DOU, cotejo independente do art85 e demais CPC82–97, contexto histórico do CP e art12, regimes especiais T07, CI do runner, DEC-016 e autorização material continuam pendentes. Nunca promover Q/C0-T em C0-J por CI ou mera concatenação.

**Próxima rodada:** T24 primeiro 48/75 posições de maior risco; T25 escopo CP art12 e efeitos 1984; T07 provas de subsidiariedade/ciência, com abertura horizontal periódica. Não se presumiu decisão CF futura.

## Rodada 04 — CPC 70–102 em texto contínuo (15/10/2026)

[Relatório FEITO/PENDENTE/PRÓXIMO](10_RODADA04_CPC181_T25_T07_20261015.md) · [Código experimental único](../produto/CODIGO_DE_TRABALHO.md).

- **Produto:** T24 passou de **17 artigos/106 unidades** para **33 artigos/181 unidades**, com [75 textos CPC82–97](../produto/fontes/T24_CPC_82_97_TEXTO_ATUAL_75_Q.csv) e [nova prévia contínua](../produto/vistas/T24_CPC_70_102_PREVIA_CONTINUA_Q.md). [Manifesto com duas origens e hashes](../produto/fontes/T24_CPC_70_102_181_v1.json) e [validador](../scripts/gerar_t24_cpc_181.py). 36 unidades art85, 4 acréscimos legislativos 2022/2025, **0 C0-J**. **A segunda revisão independente da transcrição de 75/75 permanece pendente.**
- **Código:** T07 78/214+1 histórica, T24 33/181 e T25 12/39 = **123 artigos visíveis, 434 unidades positivas e 1 histórica**. Nenhum equivale a percentagem do direito federal ou aprovação material.
- **T25:** [10 gates de proteção penal](08_T25_DEZ_GATES_ESPECIALIDADE_PENAL_20261015.csv), inclusive CP9 × Lei13445/2017 e CP12 sem extensão das regras penais a todo o CLF.
- **T07:** [10 gates de especialidade e ciência digital](09_T07_DEZ_PORTAS_ESPECIALIDADE_CIENCIA_20261015.csv); Lei14129 art43 exige comprovação de emissão **e** recebimento, ainda que não de leitura.
- **Controle operacional:** fila marca T24-001/002 em revisão Q e T24-003 com cotejo DOU/precedentes pendente. A execução de CI e a certificação C0-J **não** foram presumidas. Reserva concorrente T13 preservada; PR49 segue draft e DEC-016 pendente.

**Próxima rodada:** auditar independentemente 75 transcrições e marcos 2022/2025, remissões e jurisprudência; consolidar gates CP/T07; abrir título horizontal T05 ou outro título subrepresentado por fonte oficial.
