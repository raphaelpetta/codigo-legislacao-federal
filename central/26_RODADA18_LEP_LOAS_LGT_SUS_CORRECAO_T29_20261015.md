# CLF — Rodada 18: execução penal, assistência social, telecomunicações, SUS e correção de proveniência

**Corte 15/10/2026.** [PR #63 draft](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/63), base [PR #62 draft](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/62), **sem merge à main**. [Central #48](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/48).

## FEITO — três títulos novos, um recorte vertical e auditoria transversal

**T27 — Execução Penal.** [Vista arts. 1º–3º](../produto/vistas/T27_LEP_ART1_3_PREVIA_Q.md), [espelho 5×5](../modulos/T27/M01_ESPELHO_LEP_ART1_3_5_Q.csv), [manifesto SHA](../produto/fontes/T27_M01_LEP_5_R18_v1.json). **3 artigos/5 unidades Q**, SHA `4eec0c14bfd563fe1a280c395b7cf9932dbf954e`. Fonte [Câmara LEP atualizada](https://www2.camara.leg.br/legin/fed/lei/1980-1987/lei-7210-11-julho-1984-356938-normaatualizada-pl.html). Objetivo da execução, jurisdição, direitos do condenado e internado. Regra do art. 2º parágrafo único sobre preso provisório não elimina presunção de inocência nem transforma toda execução militar/eleitoral em execução ordinária; art. 9º-A identificação genética alterada em 2025 permanece fora.

**T30 — Assistência Social.** [Vista LOAS arts. 1º–2º](../produto/vistas/T30_LOAS_ART1_2_PREVIA_Q.md), [espelho 11×11](../modulos/T30/M01_ESPELHO_LOAS_ART1_2_11_Q.csv), [manifesto](../produto/fontes/T30_M01_LOAS_11_R18_v1.json). **2 artigos/11 unidades Q**, SHA `4642ff1e45006ed71565f46116bd2c6cac721c60`. Fonte [Câmara LOAS atualizada](https://www2.camara.leg.br/legin/fed/lei/1993/lei-8742-7-dezembro-1993-363163-normaatualizada-pl.html). Assistência **não contributiva**, em contraste ao RGPS T29. Art. 2º caput/I/II/III, alíneas I a–e e parágrafo único contidos; **incisos IV–V revogados pela Lei 12.435/2011 NÃO contados**. O art. 20, sobre requisitos do BPC e suas alterações de 2024–2025, permanece fora da vista; nenhuma concessão automática.

**T42 — Telecomunicações.** [Vista LGT arts. 1º–3º](../produto/vistas/T42_LGT_ART1_3_PREVIA_Q.md), [espelho 24×24](../modulos/T42/M01_ESPELHO_LGT_ART1_3_24_Q.csv), [manifesto](../produto/fontes/T42_M01_LGT_24_R18_v1.json). **3 artigos/24 unidades Q**, SHA `e28986b173017a20df9c3bf266eccacea28a46d0`. Fonte [Câmara LGT atualizada](https://www2.camara.leg.br/legin/fed/lei/1997/lei-9472-16-julho-1997-367735-normaatualizada-pl.html), Planalto. Art. 2º VII acrescido pela Lei 14.173/2021 e art. 3º parágrafo único pela Lei 13.673/2018. Direitos de acesso/qualidade/privacidade, proibição de suspensão em regime público nos limites legais; sigilo/defesa do consumidor/LGPD como interfaces, não autorização para tratamento irrestrito.

**T31 — Saúde/SUS, expansão pequena.** [Vista Lei 8.080/1990 arts. 4º–5º](../produto/vistas/T31_SUS_LEI8080_ART4_5_PREVIA_Q.md), [espelho 7×7](../modulos/T31/M01_ESPELHO_LEI8080_ART4_5_7_Q.csv), [manifesto](../produto/fontes/T31_M01_8080_7_R18_v1.json). **2 artigos/7 unidades Q**, SHA `4bc23e83d1479ec0c887d53a66558f2d80b1f10b`. Constituição do SUS como conjunto federativo de ações de saúde, participação da iniciativa privada **complementar** e três objetivos. **T31 alcança arts. 1º–5º, 5 artigos/13 unidades**. Art. 6º e efeitos da Lei 15.471/2026 permanecem fora para controle intertemporal.

### Correção transversal verificada: T29 Lei 8.213/1991

A origem primária da transcrição anterior apontava **incorretamente** ao texto da Lei 15.108/2025. A fonte correta é a [Câmara, Lei 8.213/1991 atualizada](https://www2.camara.leg.br/legin/fed/lei/1991/lei-8213-24-julho-1991-363650-normaatualizada-pl.html), cotejada ao Planalto. Corrigidos [CSV de T29](../modulos/T29/M01_ESPELHO_LEI8213_ART1_2_11_Q.csv), [manifesto](../produto/fontes/T29_M01_8213_11_R17_v1.json), [vista](../produto/vistas/T29_PREVIDENCIA_LEI8213_ART1_2_PREVIA_Q.md) e Código. **Blob anterior `600524864bc83a50f6c57f80b17bf9905eaf55f5`; corrigido `c2744c9ec1e4d47b8930dac464b00d0b262dbcf9`. Os onze textos, dois artigos e classificação Q não mudaram.** O novo manifesto contém registro auditável da correção e a referência anterior.

## FEITO — Código, matriz e controles

- [Código experimental](../produto/CODIGO_DE_TRABALHO.md) e [índice](../produto/fontes/indice_livros.json) atualizados: **247 artigos de origem, 819 unidades documentais textuais positivas +1 histórico T07 = 820 registros**, **36 componentes em 23 títulos**, 25 títulos ainda vazios.
- [Matriz dos 48 títulos](01_MATRIZ_AUDITORIA_48_TITULOS_20261015.csv), [painel](PAINEL_GERADO.csv), [quadro](QUADRO_PRODUTO.csv), [fila de 50 tarefas](FILA_TRABALHO.csv), [guia](../produto/00_LEIA_O_CODIGO.md) e [validador R18](../scripts/validar_r18_horizontal_e_proveniencia.py) integrados ao [roteiro local](../scripts/validar_operacao_local.sh). **+10 artigos, +47 unidades positivas, +3 títulos**, sem contagem adicional pela simples correção de URL.
- Controle de integridade documental por leitura GitHub distinto de execução local Python e distinto de cotejo em imagem do DOU. A reserva T13 permanece preservada.

## PENDENTE

1. Autenticação fac-símile DOU da LEP 1984, LOAS 1993/2011, LGT 1997/2018/2021, LOS 1990 e leis alteradoras. A fonte HTML oficial não prova sozinha toda a cronologia de eficácia. Em particular, Lei 15.295/2025 art. 9º-A LEP, normas do BPC art. 20 LOAS e Lei 15.471/2026 art. 6º LOS ficaram fora.
2. Revisão jurídico-material: lei complementar/competências, execução penal com direitos fundamentais, SUAS versus RGPS e BPC, direito à privacidade nos serviços de telecomunicações, SUS federativo e participação complementar de particulares.
3. Teste Python efetivamente executado, Actions CI, governança de PRs empilhados #49/#53–#63, validação jurídica C0-J por unidade e deliberação expressa DEC-016. **Sem merge, revogação ou renumeração.**
4. **25 títulos sem conteúdo**: a proporção de títulos preenchidos não é a proporção do volume de legislação federal consolidado.

## PRÓXIMO

- Expandir novos títulos sem reincidir nas mesmas áreas: escolher dois ou três dentre os ainda ausentes; alternar vertical limitado.
- Auditar DOU/vetos/efeitos, confrontar fontes e executar validadores com evidência reprodutível.
- Submeter equivalências jurídicas somente após avaliação competente e decisão expressa, preservando espécie normativa, competências e reserva T13.

**Estado:** C0-J=0, M=0, DEC-016 pendente, revogações/merges=0. PR #63 permanece draft.