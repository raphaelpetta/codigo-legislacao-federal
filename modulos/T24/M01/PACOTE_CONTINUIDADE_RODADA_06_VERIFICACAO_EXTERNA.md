# T24.M01 — Continuidade complementar da rodada 06 (F1-C3)
**14/10/2026** · PR #38 draft · baseline `main` 16fba172c875c7a0de388288fe70005c944021d6. 
## FEITO
Validador independente `scripts/auditar_f1c_t24.py` + GitHub Actions; 106 pares de textos localizados externamente em Câmara original/atualizada, 0 falhas após correção. [Log de CI](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38520856833); [evidência JSON hashes](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38520856833/artifacts/11873583358). Encontrada discrepância pontuação art.77 VI: original Câmara e Planalto atual ponto-final, Câmara consolidada ponto e vírgula. Lei 14.195/2021 adiciona VII mas não reescreve explicitamente VI. Informação tratada como **Q editorial**, não reforma material; ver [relatório específico](RELATORIO_F1C3_VERIFICACAO_EXTERNA_106.md).
## PENDENTE
O teste só procura texto normalizado em cada página integral, não extrai estrutura de cada artigo; fonte DOU ainda não cotejada, Planalto comparado apenas em foco, efeitos intertemporais e C0-J pendentes. CI sempre reconfirmar no SHA final, sem merge, sem revogação.
## PRÓXIMO
Validar artigo-local 106 subunidades com publicação original, consolidada Câmara, Planalto e DOU para casos de divergência, registrar controle de duplicidade e análise jurídica do âmbito; em paralelo F1-D CPC arts.82–97 se dependências claras. Critério: discrepâncias tratadas com fundamento e vinculação exata a artigo/subunidade/ato e efeito temporal.
## COORDENAÇÃO
T24.M01, T01 DEC016, T06/T13/T32, T24.M02/M04, CF/1988 vigente e CF alternativa condicionada. Sem aprovação material.
