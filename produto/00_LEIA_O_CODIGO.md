# Código da Legislação Federal — corpus experimental na main (não ratificado)

**Corte 16/10/2026.** [Código de Trabalho único](CODIGO_DE_TRABALHO.md) gerado do [índice versionado](fontes/indice_livros.json). Documento de pesquisa, **não legislação vigente, não proposta aprovada, sem C0-J nem M homologadas e com DEC-016 pendente**. Compilação só das unidades integradas na main, não do direito federal inteiro.

**T05.M06 — participação popular:** [Lei 9.709/1998 arts. 1º–2º, 2 artigos/7 unidades Q](vistas/T05_DEMOCRACIA_DIRETA_LEI9709_ART1_2_PREVIA.md), [fonte e espelho](../modulos/T05/M06_ESPELHO_LEI9709_ART1_2_7_Q.csv), [manifesto](fontes/T05_M06_9709_7_v1.json). A remissão «desta Lei» não se estende ao CLF. Arts. 3º–15 e outros módulos T05 não incluídos.

**T07.M03 — processo administrativo federal:** [Lei 9.784/1999, ensaio arts. 1º–69-A, 78 artigos/214 unidades positivas Q e art. 70 histórico = 215 registros](vistas/T07_PROCESSO_ADMINISTRATIVO_PREVIA.md), PR setorial #45 no SHA `2a4d1eefa864f44435aec70ed0cc55a96b718b64`; [manifesto com hashes de fonte e concordância](fontes/T07_M03_v4.json), [matriz das onze C1 potenciais](../central/03_T07_GATE_C1_11_EFEITOS_20261015.csv), [doze casos adversariais](../central/06_T07_DOZE_CASOS_ADVERSARIAIS_REMISSOES_E_ESPECIALIDADE.csv) e [auditoria A/B/C R3](../modulos/T07/M03_PORTAS_ABC_C1_20261016.md). Das 214 positivas, 203 C0-T locais sem delta textual e **11 C1 potenciais Q** (5 críticos, 3 altos, 3 tipográficos). A troca «desta Lei» → «deste Livro» é **hipótese editorial explicitamente NÃO homologada**, e não altera o direito vigente. Art. 70 permanece histórico, sem reeditar vigência de 1999.

**Total na main: 80 artigos experimentais, 221 unidades positivas Q e uma histórica = 222 registros.** T24, T25 e outros componentes experimentais permanecem exclusivamente nas demais branches e não foram revogados/descontinuados.

Validação sem alteração dos derivados (requer `setorial/` checkout SHA exato #45):

```bash
python3 scripts/gerar_previa_t05.py --check
python3 scripts/gerar_produto_experimental.py --setorial-root setorial --check
python3 scripts/validar_t07_gates_c1.py --setorial-root setorial
python3 scripts/gerar_codigo_integrado.py --check
python3 scripts/preflight_consolidacao.py --root .
```

Geradores têm `--write` apenas para vistas e Código derivados; editar manualmente fontes e respectivas vistas sem regeneração viola a proveniência. Mesmo CI verde não comprova DOU, vigência, equivalência C0-J, reestruturação legal ou decisão DEC-016.
