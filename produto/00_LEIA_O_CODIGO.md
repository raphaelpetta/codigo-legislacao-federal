# Código da Legislação Federal — Código de Trabalho experimental Q

**Corte 16/10/2026.** [Vista unificada gerada](CODIGO_DE_TRABALHO.md) a partir do [índice versionado](fontes/indice_livros.json). **Não é legislação promulgada, C0-J homologada, norma revogada, reforma aprovada ou resolução da DEC-016.**

- **T05.M06 — Lei 9.709/1998 arts. 1º–2º:** [vista Q](vistas/T05_DEMOCRACIA_DIRETA_LEI9709_ART1_2_PREVIA.md), 2 artigos, 7 registros.
- **T07.M03 — Lei 9.784/1999:** [vista Q](vistas/T07_PROCESSO_ADMINISTRATIVO_PREVIA.md), 78 artigos, 214 positivos + 1 histórico; [onze C1 ainda abertos](../central/03_T07_GATE_C1_11_EFEITOS_20261015.csv).
- **T24.M01 — CPC arts. 70–102:** [vista contínua Q](vistas/T24_CPC_70_102_PREVIA_CONTINUA_Q.md), 33 artigos, **181 unidades positivas Q**: **106 setoriais PR38 e 75 editoriais ainda sem segunda revisão independente**; [manifesto de duas proveniências](fontes/T24_CPC_70_102_181_v1.json), [auditoria R3](../modulos/T24/M01_PORTAS_ABC_CPC70_102_20261016.md). Manter referente original **CPC** em «deste Código», art. 465 § 4º e outras remissões; arts. 1º–69 e 103 em diante fora do recorte.
- **T25.M01 — Código Penal arts. 1º–12:** [vista Q](vistas/T25_PENAL_PARTE_GERAL_CP1_12_PREVIA.md), 12 artigos e 39 registros; «deste Código» no art. 12 se refere apenas ao CP.

**Total na `main`: 4 Livros experimentais, 125 artigos, 441 unidades positivas Q e um comando histórico T07 não transposto = 442 registros documentais.** Todos os demais livros da ponta PR #80 permanecem não integrados; não há inferência de revogação por omissão.

**Regeração sem edição manual:** `python3 scripts/gerar_previa_t24.py --setorial-root setorial --check`, `python3 scripts/gerar_t24_cpc_181.py --check`, `python3 scripts/validar_t24_gates_r3.py --setorial-root setorial`, `python3 scripts/gerar_codigo_integrado.py --check`, `python3 scripts/preflight_consolidacao.py --root .`. O `setorial` é checkout SHA `3fdbfa10b8d288b1cef56c78b47cf3cb1eb28745`; CI verifica também os Livros anteriores. **Verde técnico não é C0-J.**


## Suplemento incremental T05.M06 — arts. 3º–15 (16/10/2026)

A **Lei 9.709/1998** está agora representada experimentalmente em **duas vistas e 15 artigos de origem**, 30 unidades documentais Q: [arts. 1º–2º](vistas/T05_DEMOCRACIA_DIRETA_LEI9709_ART1_2_PREVIA.md) (2/7) e [arts. 3º–15](vistas/T05_DEMOCRACIA_DIRETA_LEI9709_ART3_15_PREVIA_Q.md) (13/23). A origem reproduzível do suplemento é **PR #80 SHA `37babdb31da5b37b7c905ae51f3b7590b39e85f7`**, não o commit anterior `1302768` apontado pelo manifesto experimental original, que não contém os arquivos. [Manifesto corrigido](fontes/T05_M06_9709_23_v1.json), [gate R3](../modulos/T05/M06_PORTAS_ABC_SUPLEMENTO_ART3_15_20261016.md).

**Alertas abertos:** art. 3º (compõem/compõe), art. 8º IV (Câmara «a às» vs TSE «e às» e «nos meios» vs Planalto «nos meio») e art. 15 (cláusula de vigência de **1998**, jamais do CLF). Não aplicar automaticamente normas eleitorais ou mudanças territoriais a um Código não promulgado. DOU original 19/11/1998 p. 9 **não cotejado em fac-símile**; as grafias permanecem estritamente editoriais Q.

**Situação agregada:** **5 componentes, 4 títulos, 138 artigos e 465 registros documentais** (464 representados como positivos Q, 1 histórico T07). C0-J 0; M 0; DEC-016 pendente. Demais 55 componentes experimentais do PR80 permanecem fora da `main`.
