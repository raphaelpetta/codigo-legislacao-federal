# T25.M01–M02 — Pacote de continuidade do ciclo 06 (arquitetura penal A/B/C)

**Data:** 14/10/2026 (America/Sao_Paulo). **Escopo:** quadro comparado de 18 testes penais e proveniência documental 1984. **Proprietário funcional:** frente T25 com coordenação central. **Issue:** [#31](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/31). **PR:** [#32, rascunho](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/32). **Branch:** `modulo/T25-parte-geral-f0-f1`.

**Versões:** CLF `main` à entrada e na última conferência antes deste arquivo = `16fba172c875c7a0de388288fe70005c944021d6`; branch previamente registrada no ciclo 05 = `cac9cbbad45b48417422145bc2b73786a89c8729`; conferir HEAD e CI após esta gravação. A PR não está integrada à `main`. Projeto constitucional `main` verificado nesta rodada = `f6b95d977bfe293fd393972d499ca5d1965a1bcd` (mudou durante a rodada, **sem leitura material nem importação de propostas**). Usar CF/1988 como direito vigente.

## 1. FEITO — persistido SOMENTE na branch

| Entrega | Arquivo/fonte | Alcance real e classificação |
|---|---|---|
| 18 cenários adversariais mapeados aos modelos A/B/C, sendo 14 anteriores + 4 novos | `TESTE_COMPARATIVO_MODELOS_ABC_CICLO06.csv` | F4 exploratório, `Q`; não representa simulações judiciais reais nem validação normativa |
| Análise institucional, novos problemas PROB-T25-0017 a 0019, alternativas e melhor objeção | `DOSSIE_06_TESTE_ARQUITETURA_E_PROVENIENCIA.md` | comparação qualitativa; modelo C **hipótese condicionada**, não escolha ratificada |
| Contraste material CP art.14 PU × CPM art.30 PU: aplicação possível de pena do crime consumado à tentativa militar excepcionalmente grave | [CPM na Câmara](https://www2.camara.leg.br/legin/fed/declei/1960-1969/decreto-lei-1001-21-outubro-1969-376258-normaatualizada-pe.html), arts. 9–10 e 29–35; [CP comum na Câmara](https://www2.camara.leg.br/legin/fed/declei/1940-1949/decreto-lei-2848-7-dezembro-1940-412868-normaatualizada-pe.html), arts. 1–31 | diferença de efeitos materiais identificada; **não** testados STF/STJ/STM e constitucionalidade em profundidade |
| Fonte editorial histórica alternativa: Coleção de Leis do Brasil 1984 (Câmara/Departamento Imprensa Nacional, Parte 1, arquivo 13,15MB) | [Item do acervo digital](https://bd.camara.leg.br/bd/items/0cd48368-68f7-4cab-a101-891629ff0cbd); [PDF associado](https://bd.camara.leg.br/bd/bitstreams/e4497ab4-fafa-4d27-af34-11f8222627a9/download) | **PDF localizado mas inacessível para inspeção**, tal como o fac-símile do DOU 13/07/1984; não há autenticação das divergências |
| Registro do ciclo no índice T25 | `README.md` | apenas governança documental |

**Fontes e trechos efetivamente examinados:** Câmara CPM arts.1–35 (notas de alterações 2017/2023) e CP arts.1–31; Lei 7.209/1984 em duas versões informatizadas da Câmara, com diferenças aparentes em CP arts.3,4,12; biblioteca digital da Câmara (metadados da Coleção de Leis 1984); Senado (metadados do DOU 13/07/1984 p.10217); LCP 1–4 e Código Eleitoral art.287 selecionados do ciclo anterior. **Nenhum PDF histórico original foi lido nem imagem de página analisada.**

## 2. PENDENTE / NÃO VERIFICADO

- Ler por imagem o **DOU 13/07/1984, Seção 1, ed. 135, p.10217 e seguintes**, ou a **Coleção das Leis de 1984, vol.5, p.38**; comparar texto dos CP arts.3,4,12 e explicar causa das anomalias, sem presumir erro do original.
- Completar inventário por subunidade do CPM arts.1–40 com vigência e diferenças 2017/2023, e consulta jurisprudencial (STF/STJ/STM) de tentativa militar, extraterritorialidade, crimes militares por circunstâncias e medidas de segurança.
- Continuar casos com prova material: leis penais militares especiais, tratados, ECA/eleitoral, LCP, responsabilização penal ambiental pessoa jurídica, crime militar em guerra; hipóteses raras e complexas podem tornar A/B/C menos adequado do que presume a pesquisa.
- Arquitetura **A** (regimes paralelos), **B** (Parte Geral única), **C** (núcleo comum + subpartes especiais) — nenhuma ratificada. Avaliação preliminar de C no recorte não fundamenta supressão de qualquer regra militar, contravencional ou processual.
- Lei e espécie normativa adequada: DEC-016 não decidida; texto CLF final, concordância C0-J, testes intertemporais e de constitucionalidade não concluídos. Não declarar revogação ou vigência de anteprojeto.
- Interfaces CF/1988: legalidade e retroatividade (art.5 XXXIX,XL), competência legislativa (art.22 I), justiça militar (art.124 e limites relevantes); proposta de Constituição independente e não incorporada.
- CI estrutural no HEAD após este arquivo: pendente de confirmação; **QA de arquivos não é validação jurídica**.

## 3. PRÓXIMO PASSO EXECUTÁVEL

**Prioridade:** visualizar e conferir uma imagem da **publicação autenticamente impressa da Lei 7.209/1984**, usando DOU de 13/07/1984, p.10217+ ou Coleção Leis 1984 vol.5 p.38; registrar em matriz `texto_dou` / `texto_colecao` / `texto_html_historico` / `texto_atual`, página e localização de CP arts.3/4/12. **Critério de aceite:** evidência paginada legível, divergências reais e causas diferenciadas por nível de certeza; deixar `A_VERIFICAR` quando não houver prova. Não usar OCR sem validação visual.

**Fila:** inventário de CPM arts.1–40 por subunidade com temporalidade 2017/2023 e jurisprudência; executar testes C05-01 a C06-18 com ajustes de legalidade, retroatividade, competência, efeitos e remissões; só então apresentar alternativas de texto legislativo com C0/C1/M/Q por dispositivo.

## 4. COORDENAÇÃO, INTEGRAÇÃO E CONTROLE

**Módulos envolvidos:** T01 (vigência/forma); T02 (garantias); T05 (eleitoral); T23/T47/T48 (tratados); T25.M01/M02/M03/M06 (lei penal, tentativa, medidas, guerra); T26 (processo); T27 (execução); T32, T37, T45. Uma mudança na forma geral deve ser encaminhada por CR/IC conforme `governanca/05_PROTOCOLO_DE_TRABALHO.md`, não editando arquivos centrais unilateralmente. **Decisões confirmadas neste ciclo: nenhuma**; sem PR merge e sem `C0-J` comprovado. O espelho textual compilado do ciclo 03 (`C0-T`) **não é** prova da redação histórica DOU nem da equivalência de eventual Código Federal.

- [x] `main` do CLF, PR e `main` do projeto CF conferidas; nenhuma mudança de arquivos T25 na main.
- [x] Fontes específicas, 18 casos e incertezas identificadas.
- [x] Estudos e hipóteses separadas de direito vigente e de decisão normativa.
- [x] FEITO / PENDENTE / PRÓXIMO persistidos na branch.
- [ ] Verificar execução GitHub Actions após último SHA.

**Regra:** `governanca/18_PROTOCOLO_CONTINUIDADE_POR_RODADA.md`.
