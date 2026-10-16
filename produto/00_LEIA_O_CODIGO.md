# Código da Legislação Federal — vista experimental não ratificada

**Corte de integração na main: 16/10/2026.** [Código de Trabalho gerado](CODIGO_DE_TRABALHO.md) do [índice versionado](fontes/indice_livros.json), sem edição paralela. **Não é texto legislativo vigente, não há C0-J homologada, M aprovada, revogação, promulgação ou decisão DEC-016.**

- **T05.M06 — Lei 9.709/1998 arts. 1º–2º:** 2 artigos e 7 registros positivos Q; [vista](vistas/T05_DEMOCRACIA_DIRETA_LEI9709_ART1_2_PREVIA.md), [manifesto](fontes/T05_M06_9709_7_v1.json), remissão «desta Lei» permanece referida ao diploma de origem.
- **T07.M03 — Lei 9.784/1999:** 78 artigos de ensaio, 214 positivos Q e 1 histórico, [vista](vistas/T07_PROCESSO_ADMINISTRATIVO_PREVIA.md), [11 C1 potenciais](../central/03_T07_GATE_C1_11_EFEITOS_20261015.csv), [auditoria R3](../modulos/T07/M03_PORTAS_ABC_C1_20261016.md), sem homologação.
- **T25.M01 — Código Penal, arts. 1º–12:** 12 artigos, 39 unidades Q, [vista](vistas/T25_PENAL_PARTE_GERAL_CP1_12_PREVIA.md), [manifesto e origem SHA PR32](fontes/T25_CP1_12_v1.json), [dez gates adversariais](../central/08_T25_DEZ_GATES_ESPECIALIDADE_PENAL_20261015.csv), [auditoria R3](../modulos/T25/M01_PORTAS_ABC_CPLITERAL_20261016.md). A locução **«deste Código» no CP art. 12 significa Código Penal**, não CLF.

**Total deste checkout:** **3 Livros, 92 artigos experimentais, 260 unidades positivas Q + 1 registro histórico T07 = 261 registros**. T24 CPC70–102 e 57 componentes restantes do PR #80 ainda não integrados, não revogados nem abandonados. Não afirmar completude da legislação federal.

A validação automatizada exige `python3 scripts/gerar_previa_t05.py --check`, `python3 scripts/gerar_produto_experimental.py --setorial-root t07 --check`, `python3 scripts/gerar_previa_t25.py --setorial-root t25 --check`, `python3 scripts/validar_t25_gates_r3.py --setorial-root t25`, `python3 scripts/gerar_codigo_integrado.py --check` e `python3 scripts/preflight_consolidacao.py --root .`; `t07` e `t25` são checkouts dos SHAs setoriais respectivos. CI verde prova somente integridade documental.
