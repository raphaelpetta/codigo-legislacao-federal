# CLF — entrada do corpus integrado experimental (Q)

**Corte documental:** 16/10/2026 · **NÃO É LEGISLAÇÃO VIGENTE NEM RATIFICADA**. A `main` integra experimentalmente somente [T05.M06 — Lei 9.709/1998 arts. 1º–2º](vistas/T05_DEMOCRACIA_DIRETA_LEI9709_ART1_2_PREVIA.md): **2 artigos, 7 unidades documentais**, com [espelho editorial](../modulos/T05/M06_ESPELHO_LEI9709_ART1_2_7_Q.csv), [manifesto de proveniência](fontes/T05_M06_9709_7_v1.json) e [auditoria R3](../modulos/T05/M06_PORTAS_ABC_PRIMEIRA_INTEGRACAO_20261016.md).

[Ler o Código de Trabalho experimental](CODIGO_DE_TRABALHO.md), produzido **somente** a partir de [indice_livros.json](fontes/indice_livros.json). A transcrição Q dos arts. 1º–2º não representa T05 completo: os arts. 3º–15, seis módulos do título e as outras espécies legislativas estão fora. **T07 (78 artigos), T24 (33) e T25 (12) seguem exclusivamente em PRs experimentais**, não foram descartados nem reconhecidos como consolidados na `main`.

**Regeneração, sem editar derivados:** `python3 scripts/gerar_previa_t05.py --write && python3 scripts/gerar_codigo_integrado.py --write`. Verificar: `python3 scripts/gerar_previa_t05.py --check && python3 scripts/gerar_codigo_integrado.py --check && python3 scripts/preflight_consolidacao.py --root .`. `--check` não altera arquivos. CI automatiza essas portas.

**Natureza jurídica:** todas as sete posições são Q, candidatas a correspondência C0-T local, **não C0-J**, nem M aprovada. Art. 1º *«desta Lei»* permanece referente à Lei 9.709/1998; nunca ao CLF inteiro. Sem revogação, efeitos eleitorais novos, promulgação ou decisão DEC-016. A CF vigente (arts. 14, 18, 49 e 61) orienta revisão futura. A fonte eletrônica TSE/Planalto **não substitui o DOU autêntico de 19/11/1998**.
