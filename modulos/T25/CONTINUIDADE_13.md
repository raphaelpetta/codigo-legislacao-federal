# T25.M03 — Continuidade 13: espécies, penas alternativas e execução inicial

**Corte:** 15/10/2026 (America/Sao_Paulo). **Frente:** T25.M03, interfaces T25.M01/M02, T26/T27, T01/T02/T45. **Issue [#31](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/31)**; **[PR #32, rascunho](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/32)**; branch `modulo/T25-parte-geral-f0-f1`. **Baseline CLF `main` no início e após os registros deste ciclo:** `16fba172c875c7a0de388288fe70005c944021d6`. **Projeto constitucional independente `main`** conferido quanto ao SHA `2a770a8136f8ca4877e865be3e3b7745a6d4b168`, não usado como fonte normativa vigente ou decisão importada. **HEAD anterior** do ciclo 12 `97a10e3c1d24089c9cd24282ea0258c81dace472`; verificar HEAD/CI novo após gravação.

## 1. FEITO — persistido na branch, NÃO integrado à main

| Entrega | Arquivo | Escopo/prova |
|---|---|---|
| Índice de **41 artigos** por numeração, sendo CP 32–58 (27) e CPM 55–68 (14), com **107 posições descritivas** de risco, incluindo veto/revogações | `INVENTARIO_ESPECIES_CP32_58_CPM55_68_CICLO13.csv` | texto consolidado consultado; índices únicos; **não** fonte literal C0-T nem exaustão de cada parágrafo |
| Concordância crítica de **25 confrontos** | `CONCORDANCIA_ESPECIES_SUBSTITUICOES_CICLO13.csv` | CP44 versus CPM59, penas e detração, sursis, sujeitos civil/militar, pena de morte/guerra, competência, histórico 2023, categorias Q/M não homologadas |
| Dois tipos penais previstos em lei e **oito variações hipotéticas**, em CSV regular de **14 colunas** | `CASOS_TIPOS_REAIS_SUBSTITUICOES_CICLO13.csv` | **CP163 dano simples** e **CPM187 deserção**; sem julgamento nem cálculo individual real |
| STF, STJ, STM: **três precedentes** com qualidade de fonte e limites declarados | `JURISPRUDENCIA_SUBSTITUICAO_PENAL_CICLO13.csv` | STF HC94083 (2010), STJ CC161898 (2019), STM Ap7000286 (julgada 2024, publicação na revista em 2026) |
| Investigação jurídica, nove problemas `PROB-T25-0044–0052` e interfaces normativas | `DOSSIE_13_ESPECIES_SUBSTITUICOES_E_EXECUCAO.md` | F1/F2/F3/F4 parciais; `C0-J` não demonstrado, `M` não aprovada |
| Índice e pacote de estado | `README.md` e `CONTINUIDADE_13.md` | governança FEITO/PENDENTE/PRÓXIMO |

**Fontes oficiais efetivamente consultadas e corte 15/10/2026:**
- CP, Câmara versão atualizada: https://www2.camara.leg.br/legin/fed/declei/1940-1949/decreto-lei-2848-7-dezembro-1940-412868-normaatualizada-pe.html — arts.32–58, art.163 caput (dano, detenção 1–6 meses OU multa), art.167 (ação privada no dano simples), art.77 III (sursis e substituição).
- CPM, Câmara versão atualizada: https://www2.camara.leg.br/legin/fed/declei/1960-1969/decreto-lei-1001-21-outubro-1969-376258-normaatualizada-pe.html — arts.55–68,84–88,187, Lei 14.688/2023 revogou alíneas f,g de CPM55, art.60,64,65 e alterou art.84 (novos prazos); CPM187 detenção 6 meses–2 anos por ausência superior a 8 dias, pena agravada se oficial; CPM88 II a exclui sursis para deserção; CPM59 pode converter pena curta **em prisão militar**, não em penas restritivas do CP44.
- STF HC94.083/DF, 2ª Turma, 09/02/2010, Informativo 574: https://stf.jus.br/arquivo/informativo/documento/informativo574.htm (identificado por resumo institucional; URL tem indisponibilidade episódica de navegação). O art.44 CP não se estende automaticamente ao crime militar.
- STJ CC161.898/MG, 3ª Seção, 13/02/2019, ementa oficial https://scon.stj.jus.br/SCON/jurisprudencia/toc.jsp?livre=%28CC+INPATH%28CLAS%29+AND+161898+INPATH%28NUM%29%29 — deslocamento de competência pode atingir benefício penal material; proteger lei do fato se mais benéfica.
- STM Ap7000286-26.2024.7.00.0000, julgada em 24/10/2024 e publicada em revista institucional 29/01/2026 https://revista.stm.jus.br/index.php/periodicos/article/view/jurisprudencia-09-v34-n1-2024 — ementa/resumo consultados, **não inteiro teor** da apelação.
- CF/1988 no Planalto, art.5º XLVI–XLIX: https://www4.planalto.gov.br/legislacao/legis-federal/constituicao . Proposta constitucional alternativa é independente.

**Controle adicional:** três CSVs principais validados quanto a uniformidade de colunas e IDs únicos: inventário **107×13**, concordância **25×15**, casos **8×14**. Um erro de CSV com tabelas misturadas foi corrigido imediatamente em commit posterior, antes do encerramento. Teste estrutural CI do último SHA ainda a acompanhar.

## 2. Conclusões e distinções que DEVEM sobreviver

**CP44 ≠ CPM59:** CP44 permite trocar privativa por pena **não privativa** sob condições; CPM59 converte pena até dois anos **em pena de prisão** no sistema militar quando não cabe sursis. **Substituição é palavra compartilhada mas não um efeito jurídico comum.** Estender CP44 ao penal militar constitui hipótese de reforma material M. Especialidade confirmada em STF HC94083, STJ CC161898 e STM apelação de 2024 (não obrigatoriamente vinculantes em toda hipótese).

**CPM84 + 88 II a + 59:** pena de deserção curta não assegura sursis; CPM88 II a expressamente o veda. Se aplicada pena de reclusão/detenção até dois anos a militar e o sursis for incabível, CPM59 disciplina conversão em prisão militar; requisitos/sujeito e status temporal precisam ser conferidos. **Não concluir** que todos os réus militares receberão pena privativa efetiva independentemente de tipo, prova ou outros direitos.

**CP163 × CPM187:** o dano comum simples (objeto privado, sem violência/qualificadora) traz multa **cominada alternativamente**, antes de qualquer instituto de substituição; eventual detenção só poderá ter art44 examinado após requisitos. CPM187 exige sujeito militar e ausência sem licença superior a oito dias, com faixa própria e restrição expressa de sursis. **Não tratar os crimes como semelhantes em lesividade**, servem apenas para tornar visíveis caminhos de espécies de penas.

**Revogações 2023:** CPM55 f/g, arts.60,64,65 não podem ser reintroduzidos como vigentes. CPM63 impedimento permanece. CPM56–57 pena de morte e execução excepcional de guerra: verificar CF5 XLVII a, devido processo, direito humanitário e eventual relação com tratados. Nada disso implica autorização em paz ou conclusão global de constitucionalidade.

**CP44 × CP54:** a permanência de expressão restritiva do art54 do CP de 1984 (inferior a um ano/culposos) ao lado do art44 ampliado em 1998 exige tratamento de lex posterior e harmonização; não declarar revogação expressa sem prova, nem suprimir limiar moderno. **Q**.

**CPM62, civil condenado pela Justiça Militar:** regime de cumprimento civil e benefícios comuns não resolvem automaticamente incidência da substituição de pena do CP44 no título condenatório. Exige confronto jurisprudencial/temporal e T26/T27.

## 3. PENDENTE / NÃO VERIFICADO

1. **Prova histórica** dos textos originais e retificações CP 1984/1998, CPM 1969/1978/2023, preservando datas do fato e lei benigna. DOU 13/07/1984 p.10217 localizado em outros ciclos mas ainda não visualmente autenticado.
2. **Sursis e execução** completos: CP77–82, CPM84–88, LEP, CPPM, detração e progressão, inclusive benefícios e restrições a tipos específicos. O recorte 55–68 é insuficiente isoladamente.
3. **Substituição CP44 aplicabilidade em civil condenado militarmente** (CPM62) e mudança de qualidade do militar antes/até julgamento; precedentes adicionais com fatos controlados.
4. **Penas acessórias e efeitos militares pós-2023**, para não revitalizar artigos revogados, e integração com sistema de T45 (estatuto e disciplina).
5. **A3/B3 e escolha M**: A2/B2 do ciclo11 não foram alteradas nesta rodada; adicionar regime de penas alternativas e distinção de art59 CPM exige decisão material, concordância e avaliação constitucional. Opções A2-D1/B2-DP/B2-DM para erro CPM35 seguem Q.
6. **Constitucionalidade de pena de morte** em guerra e regra CPM57 PU, deveres de humanidade, garantia jurisdicional, controle de tratados; não aprovar automaticamente.
7. **Ritos e reparação civil:** ação penal privada no CP163/167 e defesas do CPM187 conectam T26/T16, não norma única de direito penal material.
8. **CI do último commit** ainda a confirmar; aprovação de validador estrutural não significa equivalência jurídica ou compatibilidade constitucional.

## 4. PRÓXIMO — T25.M03/T27

**Ciclo14 recomendado:** elaborar fluxograma normativo de etapas de decisão `tipo → espécie → pena-base → agravantes/atenuantes → minorantes/majorantes → pena final → substituição → sursis → lugar de execução → benefícios` para dois fatos CP163 e CPM187, sob versões 2022/2026 e CP77–82 versus CPM84–88 e LEP. Fichas de Q/M de cada porta com fonte e consequência de alteração. Conferir jurisprudência posterior à Lei14.688 e normas processuais para particulares.

**Porta de aceite:** pelo menos 12 interfaces de decisão com mesmo fato, 8 cenários sob caminhos condicionais, sem inventar sentença; provas de cada exclusão do benefício; riscos de transição penal; recomendar texto C0/C1/M só se avaliação jurídica demonstrar efeitos, sem homologar `DEC-016` e sem merge.

**Interdependências:** T01 (veículo/DEC-016/vigência), T02 (direitos), T16 (efeitos civis), T25.M01/M02/M03, T26 (competência/ação/prova), T27 (execução), T45 (administração militar), T23/T47/T48 (tratados).

- [x] Repositório, branch e PR conferidos; `main` inalterada.
- [x] 41 artigos, 107 unidades, 25 relações, dois tipos e oito variações.
- [x] Precedentes STF/STJ/STM com níveis de acesso declarados.
- [x] FEITO/PENDENTE/PRÓXIMO registrado em branch.
- [ ] CI do SHA final e comentário na PR.

**Regra de continuidade:** `governanca/18_PROTOCOLO_CONTINUIDADE_POR_RODADA.md`.
