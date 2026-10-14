# T29.M01 — Pacote de continuidade, rodada 01 (F0/F1 seletiva)

**Corte e execução:** 14/10/2026 · **Proprietário funcional:** T29.M01 · **Issue:** [#40](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/40).  
**CLF main na abertura:** `16fba172c875c7a0de388288fe70005c944021d6`; **branch:** `modulo/T29-M01-segurados-dependentes-f0-f1-20261014`.  
**CF alternativa main na abertura:** `2a770a8136f8ca4877e865be3e3b7745a6d4b168`; conteúdo de texto constitucional futuro não foi objeto de cotejo e nenhuma norma de B foi importada. **CF/1988 é o direito vigente A.**  
**Exclusividade:** T24.M01 permanece com o PR #38/issue #37, outra frente; nenhum arquivo T24 foi escrito nem lido para pesquisa substantiva desta rodada. **Nenhum PR concorrente T29.M01 localizado** entre PRs abertos/recentes nem issue ou dossiê existente na `main` na abertura.

## 1. FEITO

| Entrega | Arquivo e prova | Situação jurídica |
|---|---|---|
| F0 — fronteiras de RGPS: classes de segurado, filiação, qualidade, dependentes e inscrição; separação de custeio, benefícios e processo | [README.md](README.md) · commit `58014f81c50470c981a03ada0289542fbd002731` | Escopo editorial, **não lei** |
| F1 seletiva inicial: **36 registros** de fontes / grupos, com URLs, proveniência, data, vigência e dúvidas; 14 colunas de governança | [INVENTARIO_F1_SELETIVO.csv](INVENTARIO_F1_SELETIVO.csv) · atualização `a4527dcff33993f48d1bb31c22cf1a6674bf95c6` | Catalogação de entradas, **não inventário de todos os artigos** |
| Diagnóstico de oito problemas Q com evidências e cinco hipóteses arquiteturais; 12 testes adversariais *a realizar* | [NOTA_01_DIAGNOSTICO_FRONTEIRAS_E_OPCOES.md](NOTA_01_DIAGNOSTICO_FRONTEIRAS_E_OPCOES.md) · commit `ca3d6c17173afbd0c226b23e84153403dbb8ae26` | Nenhuma alternativa M ratificada |
| Verificação estrutural do CSV | Execução na rodada sobre conteúdo lido via GitHub: 36 linhas, 14 colunas, **0 IDs duplicados e 0 linhas com dimensão divergente** | Não comprova equivalência jurídica, vigência completa nem consistência de todas fontes externas |

**Fontes primárias realmente consultadas em 14/10/2026 (extensão):**
- Lei 8.213/1991 **arts. 9º–17** por Câmara atualizada e Planalto compilado, em faixas e trechos (11, 15, 16, 17 com atenção específica); Lei 8.212/1991 **arts. 12–15** no Planalto compilado;
- Lei 15.072/2024, **arts. 2º–4º** (mudanças bilaterais rural/cooperativas); Lei 15.108/2025, **arts. 1º–2º** (menor sob guarda); Lei 15.371/2026, **arts. 1º, 7º–8º, 14** (vigência **01/01/2027**); Resolução Senado 26/2005 (suspensão Lei 8.212 art. 12 I h);
- EC 103/2019 e CF/1988, parâmetro e transição — sem auditoria integral por artigo; Decreto 3.048/1999, **arts. 9–17 identificados**; IN 128/2022 — **índice oficial das alterações**, não íntegra;
- STF ADIs 4.878/5.083 — notícia institucional oficial do julgamento 2021; STJ Tema 1115 — tese e informativo oficial, não acórdão integral;
- Catálogo CLF T29.M01–M08, docs/governança `main`, quadro de coordenação CF, interface, SHAs.

URLs completas, dispositivo e profundidade de consulta estão no README, no CSV e na nota.

**Resultados factuais relevantes:**
- Art. 16 §2º da Lei 8.213 foi alterado pela Lei 15.108/2025 após interpretação conforme do STF em 2021 relativa a menor sob guarda.
- Lei 15.072/2024 alterou **ambas** as Leis 8.212 e 8.213 sobre segurado especial e cooperativismo, com vetos específicos; não transportar exceção apenas de um lado.
- Resolução Senado 26/2005 suspendeu **Lei 8.212 art. 12 I h**; eventual art. 12 I j possui história diversa; não fundir.
- A letra das Leis 8.213 art. 13 / 8.212 art. 14 indica idade **14**, mas orientação INSS atual cita **16** como mínimo de segurado facultativo: Q pendente.
- Lei 15.371/2026 publicada em 01/04/2026 entrará em vigor somente **01/01/2027**: não aplicar aos casos atuais de out/2026.

## 2. PENDENTE / NÃO VERIFICADO

| Lacuna | Prova faltante | Bloqueio |
|---|---|---|
| F1 seletiva não cobre todas subdivisões, alterações, vetos e textos originais de 8.213 arts. 9–17 ou 8.212 arts. 12–15 | Matriz integral de subunidades, publicação 1991 vs atual/alteradoras e datas de eficácia | F1 concluída e qualquer C0 |
| Direito de segurado facultativo entre 14–16; vínculo à CF, decreto, IN e jurisprudência | Cadeia legislativa/hierárquica e casos judiciais | Q29-02 |
| Interpretação de menor sob guarda e seus efeitos em óbitos anteriores a 2025 | Dispositivo integral ADIs 4878/5083 e legislação temporal | Q29-03 |
| Segurado especial, cooperativas e propriedade rural | Texto consolidado por subunidade, Lei 15.072 vetos e acórdão completo STJ Tema 1115 | Q29-04 |
| Regras de custeio e benefícios futuros | Titularidade definitiva M01/M02/M05, análises constitucionais/transitórias | Redação F5 |
| CF projeto e cláusulas de competência/seguridade | Comparar texto atual de `main` CF, não apenas SHA; solicitar interface se houver tensão comprovada | Cenário B futuro |
| Dados empíricos e pesquisa comparada | F3, metodologias, efeitos das mudanças | Reforma M |
| CI e integração | PR draft, checks último SHA, revisão central | Merge/integração |

**Não se presume** que fontes oficiais consultadas em 2026 sejam necessariamente completas para todos os efeitos temporais. Sem dispositivos promulgados pelo CLF, nenhum C0/C1/M recebeu aprovação. `PLANEJADO` permanece o status do módulo.

## 3. PRÓXIMO PASSO EXECUTÁVEL

**T29.M01 — F1-A granular:** inventariar **Lei 8.213/1991 arts. 10–17 e Lei 8.212/1991 arts. 12–14**.  
**Insumos:** publicações originais (DOU/Câmara), compiladas atuais (Câmara/Planalto) e leis alteradoras com páginas oficiais, STF ADIs 4.878/5.083, STJ Tema 1115, Res. 26/2005 e EC 103/2019.  
**Entregável:** tabela por dispositivo e subunidade identificável de texto original, texto atual, cadeia de mudanças/vigência, revogação/veto/suspensão, efeito material, destino primário T29.M01/T29.M02/T29.M05/T29.M07 e riscos protetivos.  
**Critério de aceite:** nenhum subdispositivo do recorte sem origem e status `VERIFICADO` ou `Q` com razão explícita; testes das cinco divergências normativas mais relevantes; concordância jurídico-material ainda pendente e sem C0 presumido.  
**Fila:** F2 modelo completo de filiação, tempo e dependência; estudo crítico F3 e propostas rivais F4, seguido de minuta F5 somente após decisões.

## 4. COORDENAÇÃO E CONTROLE

- **Dono:** T29.M01, e **exclusão operacional** T24.M01 (outra frente / PR #38).
- **Interfaces:** T29.M02 (contribuições), M03 (aposentadorias), M04 (incapacidade), M05 (pensões), M06 (processo), M07 (RPPS), M08 (complementar), T28 (trabalho), T30 (assistência), T12 (tributação), T13/T17/T32 (pessoas/família/vulnerabilidade), T07 e T24 (processos).
- **Competência/reserva:** CF 194–195/201, EC 103 e normas de financiamento de tipos diversos; DEC-016 sobre veículo formal de Código único pendente.
- **Fonte de verdade:** `main` CLF confirmada na abertura, nada foi alterado nela; a branch contém apenas nova documentação em `modulos/T29/M01/`.
- **Aprovação:** nenhuma reforma ratificada; alternativas são H/Q; eventual integração requer revisão da governança e decisão do usuário.
- **CI:** consultar status oficial após último commit e só declarar o que for retornado.

- [x] Conferi `main`, cadastro e PRs concorrentes.
- [x] Separei F0, F1 documental, hipóteses jurídicas e fonte vigente/futura.
- [x] Preservei limite M01/M02/M05/M06, sem duplicação T24.
- [x] Produzi pacote FEITO/PENDENTE/PRÓXIMO.
- [ ] F1 por subunidade, F2 e análise constitucional final.
- [ ] Revisão central e CI, integração autorizada.
