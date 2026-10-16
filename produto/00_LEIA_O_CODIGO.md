# Código da Legislação Federal — Código de Trabalho experimental Q

**Corte 16/10/2026.** [Vista unificada gerada](CODIGO_DE_TRABALHO.md) a partir do [índice versionado](fontes/indice_livros.json). **Não é legislação promulgada, C0-J homologada, norma revogada, reforma aprovada ou resolução da DEC-016.**

- **T05.M06 — Lei 9.709/1998 arts. 1º–2º:** [vista Q](vistas/T05_DEMOCRACIA_DIRETA_LEI9709_ART1_2_PREVIA.md), 2 artigos, 7 registros.
- **T07.M03 — Lei 9.784/1999:** [vista Q](vistas/T07_PROCESSO_ADMINISTRATIVO_PREVIA.md), 78 artigos, 214 positivos + 1 histórico; [onze C1 ainda abertos](../central/03_T07_GATE_C1_11_EFEITOS_20261015.csv).
- **T24.M01 — CPC arts. 70–102:** [vista contínua Q](vistas/T24_CPC_70_102_PREVIA_CONTINUA_Q.md), 33 artigos, **181 unidades positivas Q**: **106 setoriais PR38 e 75 editoriais ainda sem segunda revisão independente**; [manifesto de duas proveniências](fontes/T24_CPC_70_102_181_v1.json), [auditoria R3](../modulos/T24/M01_PORTAS_ABC_CPC70_102_20261016.md). Manter referente original **CPC** em «deste Código», art. 465 § 4º e outras remissões; arts. 1º–69 e 103 em diante fora do recorte.
- **T25.M01 — Código Penal arts. 1º–12:** [vista Q](vistas/T25_PENAL_PARTE_GERAL_CP1_12_PREVIA.md), 12 artigos e 39 registros; «deste Código» no art. 12 se refere apenas ao CP.

**Total na `main`: 4 Livros experimentais, 125 artigos, 441 unidades positivas Q e um comando histórico T07 não transposto = 442 registros documentais.** Todos os demais livros da ponta PR #80 permanecem não integrados; não há inferência de revogação por omissão.

**Regeração sem edição manual:** `python3 scripts/gerar_previa_t24.py --setorial-root setorial --check`, `python3 scripts/gerar_t24_cpc_181.py --check`, `python3 scripts/validar_t24_gates_r3.py --setorial-root setorial`, `python3 scripts/gerar_codigo_integrado.py --check`, `python3 scripts/preflight_consolidacao.py --root .`. O `setorial` é checkout SHA `3fdbfa10b8d288b1cef56c78b47cf3cb1eb28745`; CI verifica também os Livros anteriores. **Verde técnico não é C0-J.**
