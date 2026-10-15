# T25 — Continuidade do ciclo 11: A2/B2 e regressão jurídico-material

**Corte normativo/consulta:** 14/10/2026 (America/Sao_Paulo). **Frentes:** T25.M02 (culpabilidade e ilicitude), interface técnica T25.M03 (penas e dosimetria). **Issue:** [#31](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/31). **PR:** [#32](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/32), `draft`; **branch:** `modulo/T25-parte-geral-f0-f1`. **Main CLF consultada antes e depois de gravar estudos:** `16fba172c875c7a0de388288fe70005c944021d6`, inalterada nesta rodada. **Main da proposta constitucional (somente controle de versão):** `2a770a8136f8ca4877e865be3e3b7745a6d4b168`; não se consultou conteúdo novo para decidir normas positivas. **HEAD anterior:** `32289f92de804ea1e45e7480cb38abaccc21b1a5` do ciclo10. Verificar SHA e CI do presente ciclo após o último commit.

## 1. FEITO — documentos efetivamente gravados na branch, não incorporados à main

| Entrega | Arquivo | Situação e categoria |
|---|---|---|
| Redação A2 compartilhada com correção de faculdade, ressalva CPM47 e regras de pena | `MINUTA_A2_NUCLEO_COMUM_CICLO11.md` | **10 artigos provisórios + 3 dispositivos de pena (A2-D1–3)**; mudanças M identificadas, não ratificadas; problemas remanescentes Q |
| Redação B2 setorial militar, com duas opções exclusivas CPM35 | `MINUTA_B2_SUBPARTE_MILITAR_CICLO11.md` | **11 artigos provisórios + opções B2-DP/B2-DM/DEx e transição**; não equivalência jurídica C0-J |
| Nova passagem pelos mesmos dez fatos do ciclo10 | `MATRIZ_REGRESSAO_10_CASOS_A2_B2_CICLO11.csv` | dez registros `P10-01..10`, incluindo referência a um caso STM e nove testes sintéticos; respostas Q condicionadas |
| Comparação técnica do que mudou em texto, riscos e decisões | `DOSSIE_11_REGRESSAO_A2_B2_E_DOSIMETRIA.md` | F4/F5-EXPERIMENTAL, não minuta final |
| Índice e handoff completo | `README.md` e `CONTINUIDADE_11.md` | rastreabilidade |

**Fontes realmente consultadas:** [CP comum compilado, arts.20–25 e CP21/erro evitável](https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848compilado.htm); [CPM compilado, arts.35–47,73,76,77](https://www.planalto.gov.br/ccivil_03/decreto-lei/del1001compilado.htm); [Lei 14.688/2023, especialmente CPM77 PU](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14688.htm). O [STM Ap 7000232-60.2024.7.00.0000, publicado na revista do STM](https://revista.stm.jus.br/index.php/periodicos/article/download/jurisprudencia-05-v34-n1-2024/88/238) foi **examinado no ciclo 09**, e apenas seus dados já documentados foram usados como teste referencial nesta rodada. Não se verificou inteiro teor novo de tribunal nem se declarou corrente jurisprudencial majoritária sem prova.

**Correções com efeito mensurável:**
- `PA3` da primeira minuta A previa `reduzirá` por erro evitável; `A2-03` prevê **`poderá`**, preservando a facultatividade do CP21 no texto compartilhado. A escolha obrigatória continua hipótese alternativa **M**, não incluída em A2.
- `PA9` apontava a regra militar do CPM47 II sem escrevê-la; `A2-09 PU` agora a **redige** com classes hierárquicas relevantes e ressalva de outros tipos. **Ainda não C0-J.**
- Redução do erro CPM35: **A2-D1** é causa especial facultativa na 3ª fase com 1/6–1/3 (M); **B2-DP** é atenuante com piso na 2ª fase (M/Q); **B2-DM** é causa especial com 1/5–1/3 na 3ª fase, podendo atravessar piso (M/Q). **B2-DP e B2-DM são incompatíveis** e ambas permanecem hipóteses.
- Excesso doloso: **A2-D2/B2-DEx** escolhem atenuante de 1/5–1/3 na segunda fase dentro do piso, **nova definição M**, não extraível literalmente do CPM46.

**Resultados da regressão dos dez casos:** correção de erros formais em P10-02 (facultatividade) e P10-10 (qualidade hierárquica); distinção dos desenhos de pena em P10-04 e P10-09, ainda com resultados de pena individual indeterminados; persistência de diferença M em P10-01/P10-03 (erro inevitável militar), P10-07 (beneficiário de exculpação) e P10-08 (ampliação do excesso escusável a civis). Não se atribuiu novo julgamento a tribunal nem estimativa de probabilidade de êxito.

## 2. PENDENTE / NÃO VERIFICADO

1. **Escolha material explícita** entre atenuante sujeita ao mínimo, causa especial de diminuição que o ultrapassa, e seus requisitos para CPM35, com confrontação de CPM73/76/77, CP21 e STF Tema158. Nem voto isolado do STM nem tese geral STF basta para escolher.
2. **Minuta A2 ainda incompleta** em erro sobre descriminantes, proporcionalidade da justificante, dever militar de enfrentar perigo, e dose de intervenção em comando militar (CPM42 PU).
3. **Minuta B2 ainda incompleta** na substituição de espécie de pena do CPM35, efeitos temporais, hipóteses completas de CPM41/42 PU e interpretação constitucional de CPM40. O texto de B2-DP ou B2-DM não pode virar texto final sem decisão.
4. **Prova C0-J ausente:** diferenças no alcance de CPM35/39/40/42/45/46/47 e crimes militares da Parte Especial; A2 e B2 contêm alterações M possíveis e sínteses que podem deslocar sentido. C0-T restrito ao CP1–12 do ciclo03, não se aplica às novas redações.
5. **Normas temporais e rito:** falta cláusula formal de preservação do efeito benigno, identificação da legislação aplicável em todas as datas, competência constitucional militar/Tribunal do Júri, condições de prova, consequências civis e execução.
6. **Proveniência histórica:** DOU 1984 Lei7.209 fac-símile localizado mas ainda não inspecionado; CPM 1969/2023 cadeia original e retificações não reconstruídas por completo.
7. **Governança:** DEC-016 e arquitetura final do Código Federal pendentes; CF alternativa independente, sem incorporação; PR draft sem merge.
8. **CI:** conferir conclusão do teste estrutural no SHA final desta rodada. Qualquer resultado favorável vale **somente** para arquivos/esquemas, não para constitucionalidade nem validação penal.

## 3. PRÓXIMO — T25.M03 como frente técnica independente

**Ciclo 12 prioritário:** iniciar **matriz integral por dispositivo de dosimetria** confrontando **CP arts.59–68 × CPM arts.69–77**, com original e alteradores 2023, pena-base, agravantes, atenuantes, concurso de circunstâncias, majorantes e minorantes, espécies e limites. Exigir fonte e vigência por dispositivo, efeito e marco temporal. Revisar art35 e art46 nas três hipóteses A2-D1/B2-DP/B2-DM (e A2-D2/B2-DEx) em uma **única matriz**, com cálculos exemplificativos apenas quando elementos do tipo, fase e fração forem determinados.

**Critério de aceite:** inventário sem omissão de subunidades, quadro de **mesma pena-base hipotética** mostrando efeitos diferentes de piso por fase, exame de precedentes STF/STJ/STM e hipóteses de discrepância de espécie da pena, observando proibição de combinação arbitrária de leis e intertemporalidade. Não redigir uma opção de pena como escolha do usuário nem homologar alteração M sem deliberação.

**Fila:** expandir para concurso de crimes/penas, substituições e medidas de segurança T25.M03/T27; reauditar hipóteses militares especiais e constitucionalidade, apoiar elaboração de cláusulas de transição após DEC-016.

## 4. COORDENAÇÃO

**Módulos envolvidos:** T01.M01/M04 (veículo, vigência, revogação), T02 (garantias), T16 (consequências civis), T25.M01–M03, T26 (competência/prova), T27 (execução), T45 (hierarquia), T23/T47/T48 (tratados). **CF vigente:** art.5º, garantias e competências; **CF projetada** fonte separada e não vigente.

- [x] Repositório, PR e `main` conferidos; nenhuma edição do corpus principal.
- [x] A2 e B2 gravadas, com alternativas de dosimetria expressas e divergências materiais classificadas.
- [x] Dez casos anteriores reexaminados com IDs estáveis.
- [x] Fontes, resultados, pendências e próximo critério de aceite registrados.
- [ ] CI estrutural do HEAD final confirmada e comentário atualizado na PR.

**Regra:** `governanca/18_PROTOCOLO_CONTINUIDADE_POR_RODADA.md`.
