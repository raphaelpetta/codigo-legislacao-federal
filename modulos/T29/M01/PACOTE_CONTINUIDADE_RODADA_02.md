# T29.M01 — Continuidade da rodada 02 (F1-A granular)

**Corte:** 14/10/2026. **Responsável funcional:** T29.M01 (RGPS, segurados e dependentes).  
**Issue:** [#40](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/40) · **PR:** [#41 (draft)](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/41).  
**CLF main na abertura:** `16fba172c875c7a0de388288fe70005c944021d6`; **branch:** `modulo/T29-M01-segurados-dependentes-f0-f1-20261014`.  
**Outro módulo reservado:** T24.M01 / PR #38 é responsabilidade de outra frente; nenhuma alteração nessa área. **Interface CF:** direito positivo = CF/1988 com EC 103/2019; proposta constitucional em repositório separado, conferir o SHA atual antes da integração, sem importação de hipóteses.

## FEITO

| Produto | Arquivo / último commit de criação | Alcance e validação |
|---|---|---|
| Mapeamento individualizado dos **198 registros de dispositivos/subunidades** da Lei 8.213 arts. 10–17 (117) e Lei 8.212 arts. 12–14 (81) | [F1A_MATRIZ_GRANULAR_8213_8212.csv](F1A_MATRIZ_GRANULAR_8213_8212.csv) — `989dd05d892613d0b642621757fb6c39059c32d7` | 198 linhas, 14 colunas, 0 IDs duplicados, URLs presentes; status factual com ressalvas; **não C0** |
| Mapa de **78 paralelos e diferenças funcionais** entre art. 11 Lei 8.213 e art. 12 Lei 8.212 | [F1A_PARALELOS_8213_ART11_8212_ART12.csv](F1A_PARALELOS_8213_ART11_8212_ART12.csv) — `ff969ff630940def8c8a5b81de12e791ccbd9159` | 78 linhas sem problema de dimensão; evitar fusão automática |
| Relatório de 8 achados e 12 testes críticos | [RELATORIO_F1A_AUDITORIA_GRANULAR_E_ASSIMETRIAS.md](RELATORIO_F1A_AUDITORIA_GRANULAR_E_ASSIMETRIAS.md) — `f7fbd090d6c436267acb54aacdd4fef9e263827d` | Evidências normativas oficiais, Q explícitos, sem proposta material aprovada |
| README atualizado | [README.md](README.md) — `c65b4d73f59eb6d15e5e613b2b30d8cb851a47ef` | Links e status F1-A, histórico anterior conservado |

**Fontes efetivamente consultadas em 14/10/2026:**
- **Câmara dos Deputados**, texto original de 25/07/1991 e texto consolidado de ambas Leis 8.212 e 8.213 (arts. selecionados); **Planalto**, versões compiladas para temas sensíveis; original e atualizado foram examinados **por recortes e subunidades**, sem cópia literal integral de 198 pares ou certificação de diff;
- **Lei 15.072/2024**, arts. 2º–4º, altera art. 11/12 em 2024 com veto (DOU 27/12/2024); **Lei 15.108/2025** arts. 1º–2º, altera art. 16 §2º da Lei 8.213 (DOU 14/03/2025); **Lei 14.119/2021** art. 23, acrescenta art. 12 §9º VIII na Lei 8.212, **sem espelho expresso em 8.213 art. 11 §8º**;
- **Senado**, Resolução 26/2005 suspende art. 12 I h da Lei 8.212, mas alínea j é de outro ato; **STF**, ADIs 4.878/5.083, notícia institucional da decisão de junho de **2021** e precedente relatado oficialmente; **STJ**, Tema 1115, julgado 23/11/2022, DJe 07/12/2022 (tese e informação institucional);
- **Decreto 3.048/1999**, art. 11 e §2º regras sobre idade 16; **INSS** tipos de filiação; **Leis 8.213 art. 13 e 8.212 art. 14** referem 14 anos, sem solução de hierarquia até aqui;
- **Lei 15.371/2026**, publicada DOU 01/04/2026, vigência futura em **01/01/2027** — interface M02/M05/T28, **não vigente para concessões em 14/10/2026**.

## PENDENTE / NÃO VERIFICADO

1. Os 198 registros são **mapeamentos funcionais**, com alguns grupos e subdivisões, **não transcrições integrais** ou prova de cadeia modificativa exaustiva. Marcas `ORIGINAL_IDENTIFICADO`, `ACRESCIDO`, `ALTERADO` e `VETADO` sinalizam eventos verificados na anotação de compilação, **não auditoria de todos os atos oficiais**. Há publicação/republicação (1996 e 1998), MP, retificações e vetos a confirmar contra DOU.
2. A **assimetria serviços ambientais** entre art. 12 §9º VIII (Lei 8.212) e art. 11 §8º (Lei 8.213) tem prova textual e da Lei 14.119/2021, mas **significado jurídico e interpretação administrativa/judicial ainda Q**.
3. **14/16 anos** segurado facultativo exige análise constitucional e jurisprudencial rigorosa: não afirmar que o decreto revogou lei ou que filiação entre 14–16 é automaticamente válida.
4. **Menor sob guarda** exige dispositivo integral das ADIs, jurisprudência em período intermediário e definição de condição de dependência e benefício prestacional em T29.M05.
5. **Mandatos eleitorais**: confirmar escopo da Resolução 26/2005 e efeitos da Lei 10.887/2004 sobre h/j, nas duas leis, incluindo contribuições em cada competência.
6. **T29.M02/M03/M05/M07:** decisões sobre localização primária e eventuais diferenças materiais por consequência econômica, previdenciária e federativa não ratificadas.
7. **Diferenciação temporal:** Lei 15.371/2026 publicada com vigência futura deve constar como tal no sistema; EC 103/2019 e transições precisam de histórico próprio.
8. **Status de CI do último SHA, revisão jurídico-adversarial independente e integração na main ainda a verificar**. Nenhuma decisão C0/C1/M concluída.
9. **Constituição alternativa:** não cotejada integralmente nesta rodada; sempre consultar versão atual da CF independente antes de formular interface constitucional normativa.

## PRÓXIMO — uma atividade prioritária

**T29.M01/F1-B — Quatro testes de assimetria sistêmica:**
1. Ambiental: Lei 14.119 art. 23 × Lei 8.212 art. 12 §9º VIII × Lei 8.213 art. 11 §8, prática INSS e precedentes;
2. Idade: Leis 8.212 art. 14/8.213 art. 13 **14 anos** × Decreto 3.048 art. 11/INSS **16 anos**, fundamentos constitucionais;
3. Menor sob guarda: 1991, Lei 9.528/1997, ADIs 4878/5083 (STF 2021) e Lei 15.108/2025, com recorte de óbitos e provas;
4. Mandato eletivo: Resolução Senado 26/2005 × 8.212 art. 12 I h/j × 8.213 art. 11 I h/j, constitucionalidade e cronologia.

**Insumos:** textos originais, DOU, inteiro teor de decisões, normas administrativas; **entregável:** quatro dossiês curtos com cronologia e alternativas classificadas Q ou M-proposta, mapa de interfaces sem duplicação e teste adversarial. **Aceite:** cada afirmação com fonte e eficácia datadas, cláusulas de não regressão e parecer sobre se a diferença é legislativa, interpretativa ou apenas editorial.

**Fila:** F1-C transcrição literal certificada dos 198 registros, F2 modelo jurídico vigente e F3 pesquisa comparada; apenas então F4/F5.

## COORDENAÇÃO / CONTROLE

- **Proprietário:** T29.M01, com T29.M02 custeio, M03 aposentadorias, M04 incapacidade, M05 pensões, M06 rito, M07 RPPS, M08 complementar; T28 trabalho, T30 assistência, T12 contribuições, T13/T17/T32 pessoas/dependentes. Não editar outros módulos.
- **CF:** cenário A CF/1988 e EC103; cenário B anteprojeto distinto e condicional; DEC-016 sobre veículo legislativo de Código único pendente.
- **Não foi editada a `main`** nem alterada a issue/PR de T24.M01. A branch T29 contém apenas trabalho especializado, PR draft.
- **Controle estrutural executado:** 198 registros, 198 IDs únicos, 117/81 por lei; 78 relações; 0 campos divergentes de contagem. **Não equivale a qualidade jurídico-semântica, certeza de toda alteração, ou aprovação.**
- **CI:** consultar e reportar status real do último commit, sem presumir aprovação por ausência de checks.

- [x] Conferi `main`, PR #41 e PRs de outras frentes antes de escrever.
- [x] Conservei estados de fonte, jurisprudência, norma proposta e tempo distintos.
- [x] Registrei FEITO/PENDENTE/PRÓXIMO, risco de alteração e responsabilidades.
- [ ] F1 completa por subunidade e efeito.
- [ ] Revisão jurídica independente, controle CI e integração autorizada.
