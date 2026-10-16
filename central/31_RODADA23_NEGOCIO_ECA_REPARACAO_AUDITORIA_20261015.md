# CLF R23 — negócios jurídicos, proteção integral e responsabilidade civil (15/10/2026)

**Origem:** PR #69 draft, HEAD `1ea77e5b3a1fcd3d73f31ea00b6b67bb3ddf249a`. Branch R23 derivada sem tocar main. O corpus é texto **experimental Q**, não legislação promulgada, C0-J ou reforma material.

## FEITO — novas frentes e conexão de efeitos

- **T15 — CC arts. 104–107 — negócio jurídico**: [vista](../produto/vistas/T15_CC_NEGOCIO_ART104_107_PREVIA_Q.md) e [manifesto](../produto/fontes/T15_M01_CCNJ_7_R23_v1.json); 4 artigos/7 unidades textuais Q. Requisitos de validade e forma; art104 III não afasta forma especial art108; DOU e C0-J pendentes
- **T32 — ECA arts. 1º–3º — proteção integral**: [vista](../produto/vistas/T32_ECA_ART1_3_PREVIA_Q.md) e [manifesto](../produto/fontes/T32_M01_ECA_5_R23_v1.json); 3 artigos/5 unidades textuais Q. ECA art2 PU 18–21 apenas casos expressos; art3 PU Lei13257/2016; art4 atualizado 2026 fora da vista
- **T16 — CC arts. 927–930 — reparação**: [vista](../produto/vistas/T16_CC_REPARACAO_ART927_930_PREVIA_Q.md) e [manifesto](../produto/fontes/T16_M01_CCRESP_7_R23_v1.json); 4 artigos/7 unidades textuais Q. Art188 excludente não elimina art929 reparação; art927 PU responsabilidade objetiva e art930 regresso

- **T06: [parecer sobre ADI 1.127](../modulos/T06/M05_NOTA_ADI1127_EFEITOS_R23_20261015.md)** com leitura do resultado final STF: a palavra “qualquer” no art. 1º, I é inconstitucional; impugnação relativa à expressão “juizados especiais” prejudicada por superveniência; art. 2º, §3º julgado improcedente. Separados texto editorial histórico e alcance jurídico atual. Nenhum texto normativo foi materialmente emendado.
- **Corpus e controles:** 54 componentes Q, 36/48 títulos com texto, 292 artigos de origem / 979 positivas +1 histórico T07 (980 registros); **incremento +11 artigos/+19 unidades/+2 títulos**, 12 vazios. Código integrado, índice, painel, quadro, matriz, guia, fila **72 tarefas únicas** e validador R23 adicionados. T13 reservado intacto.
- **QA por fonte:** o validador `scripts/validar_r23_corpus_auditoria.py` está no roteiro local; compara hashes Git, IDs, texto espelho/destino, vista/código, painel/matriz/fila e estados Q. O arquivo criado **não comprova sua execução**.

## PENDENTE — portas independentes

- A fonte Câmara HTML atualizada (ECA e CC), Planalto e resultado final STF **não equivalem** ao cotejo DOU em fac-símile. CC 2002, ECA 1990 e alteradoras, efeitos retroativos/intertemporais e acórdãos integrais não foram todos inspecionados.
- CI GitHub Actions **P0 ainda bloqueante** conforme [issue #66](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/66). Verificação no run `38818620819` apontou `runner-smoke` e `corpus-r20` ambos com `failure` e 0 steps; a causa exata não pode ser inferida. Corrigir apenas após mensagem/anotação oficial.
- **Nenhuma C0-J, M, DEC-016, revogação, renumeração definitiva ou merge.** Não converter 36 títulos textuais em denominador de cobertura jurídica total.

## PRÓXIMO

Priorizar diagnóstico do bloqueio CI e auditoria DOU/constitucional por risco; avançar títulos remanescentes e verticalidade apenas se superar em ganho marginal a consolidação do já construído. Evitar mera soma de títulos e atualizações redundantes.
