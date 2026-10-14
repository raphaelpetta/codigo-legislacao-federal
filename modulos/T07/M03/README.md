# T07.M03 — Processo administrativo geral

**Estado:** PILOTO EXPERIMENTAL F0/F1/F2 parcial. **Não** é parte codificada aprovada do CLF, lei em vigor ou homologação de C0 jurídico. **Fonte de referência:** [Lei 9.784/1999 atualizada](https://www2.camara.leg.br/legin/fed/lei/1999/lei-9784-29-janeiro-1999-322239-normaatualizada-pl.html).

## Ciclo 13 — unidade de prova arts. 1º e 2º

- [`PILOTO_13_ARTIGOS_1_2_LEI9784.md`](PILOTO_13_ARTIGOS_1_2_LEI9784.md): protótipo textual completo dos dois artigos, incluindo **6 unidades** de âmbito/definições e **15 unidades** de princípios/critérios, alternativas de contextualização e hipóteses de revogação **bloqueadas**.
- [`CONCORDANCIA_INTEGRAL_ART1_ART2_13.csv`](CONCORDANCIA_INTEGRAL_ART1_ART2_13.csv): **21** transcrições com espelho literal e destino provisório, todas com `equivalencia_juridica=Q` e `status_destino=NAO_PROMULGADO`.
- [`MAPA_DEPENDENCIAS_SISTEMICAS_13.csv`](MAPA_DEPENDENCIAS_SISTEMICAS_13.csv): **16** dependências sistemáticas/jurisprudenciais, notadamente arts. 3º–70, 49-A–49-G, 69/69-A e Súmula 633 do STJ.
- [`TESTES_VETO_CONTEXTO_TRANSICAO_13.csv`](TESTES_VETO_CONTEXTO_TRANSICAO_13.csv): **30** cenários adversariais sobre veto por unidades, direitos, competência, subsidiariedade, retroatividade e revogação parcial.

**Invariantes:**
1. Igualdade de texto `C0-T` não implica equivalência normativa `C0-J`.
2. Nenhum dispositivo da Lei 9.784/1999 está revogado por esse teste.
3. “Esta Lei” não se converte automaticamente em “este Código”; mudança de referente é problema de alcance jurídico.
4. Não revogar apenas os arts. 1º e 2º enquanto restante da lei continuar a depender dos seus conceitos/âmbito e sem transição juridicamente válida.
5. A unidade de codificação definitiva depende do mecanismo geral `DEC-016` e da interface constitucional `CF-IC-001`.

**Próxima prova:** inventariar e versionar artigos 3º–70 (inclusive artigos intercalares e vetados), mapear os regimes especiais e redigir minuta contextual completa sujeita a direitos, jurisprudência e duplo procedimento de aprovação, distinguindo C0/C1 de inovação material M.
