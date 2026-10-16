# T24.M01 — Continuidade da rodada F1-D2 (14/10/2026)
**Branch T24.M01 — PR #38 (draft)**. Baseline main `16fba172c875c7a0de388288fe70005c944021d6`.
## FEITO
Extração reproduzível por artigo de 75 unidades dos CPC arts.82–97 em duas edições oficiais Câmara, script `scripts/extrair_f1d_t24.py`, workflow `.github/workflows/extrair-cpc-f1d.yml`. [Job GitHub Actions #38526972117 aprovado](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38526972117) e [evidência JSON/CSV com hashes](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38526972117/artifacts/11875918126). 45 pares iguais no extrator; 4 acréscimos pós-2015 (82 §3º; 85 §§6º-A,8º-A,20); 26 divergências **de extração OU edição**, não alterações legislativas demonstradas. [Relatório de limites](RELATORIO_F1D2_EXTRACAO_AUTOMATICA_75.md).
## PENDENTE
Conferência dos 26 pares por DOM e DOU; cotejo leis 14.365/2022 e 15.109/2025, jurisprudência Tema 1076/STJ e Tema1255/STF, texto válido dos honorários e despesas de perícia/benefício JG; separação de taxa judiciária estadual e norma federal, DEC016 e C0-J. Aprovado teste estrutural não significa equivalência jurídica. Checar checks no HEAD final após nova alteração.
## PRÓXIMO
F1-D3: verificar 26 divergências uma a uma com fonte e log; focar arts.82,85,91,95 e eventual impacto art.98/99; emitir parecer de equivalência jurídica C0-J restrito apenas se todos os critérios por unidade estiverem satisfatoriamente demonstrados. Nenhuma alteração normativa/merge.
## COORDENAÇÃO
T24.M01, T24.M02/M03/M04, T01 DEC016, T06, T32 e interfaces de processo/gratuidade. CF vigente/CF futura não confundir.
