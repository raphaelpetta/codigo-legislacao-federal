# Auditoria forense de proveniência — 60 componentes experimentais do PR #80

**Corte:** 16/10/2026. **Base da main:** `c79084f0be3bb4926de14a4bba53447924d57f3b`. **Fotografia PR #80 verificada para a rotina:** `d1d733561944d67d3d3ffa13c32763784d5cdb6c`. O número do PR é referência à **origem documental experimental**, não aprovação jurídica nem incorporação automática dos componentes.

## Problema demonstrado e método da auditoria

A integração T05.M06 arts. 3º–15 (PR #88) detectou que um manifesto afirmava proveniência no commit `1302768...`, mas **o caminho do arquivo não existia naquele commit**; seu blob foi confirmado no HEAD `37bab...` do PR #80, e o manifesto integrado na `main` foi corrigido para a fotografia reproduzível. Esse caso demonstra por que verificar apenas o hash dos arquivos **atuais** não valida a reivindicação de que eles já estavam em um **commit histórico**.

O auditor `scripts/auditar_proveniencia_pr80.py` percorre os **60 componentes** do índice PR #80 e, por cada manifesto, verifica: (a) ID/vista/Q e contagem; (b) hash Git atual da origem local, ou natureza da fonte externa/composta; (c) objeto commit realmente acessível e existência do **caminho nesse exato commit**; (d) identidade byte a byte entre blob do commit declarado e blob atual; (e) hashes dos componentes de fontes compostas. Cada Livro recebe uma classificação específica e caminho/commit para intervenção posterior.

**Categorias:** `ANCORA_COM_BLOB_IDENTICO` (foto histórica comprovada neste checkout), `ANCORA_ANTERIOR_AO_ARQUIVO` (caminho faltante), `ANCORA_COM_BLOB_DIFERENTE` (commit tem versão anterior), `COMMIT_HISTORICO_NAO_VERIFICAVEL`, `SEM_ANCORA_HISTORICA_DECLARADA`, `FONTE_SETORIAL_EXTERNA`, `COMPOSTO_MULTIPLAS_FONTES_PENDENTE` e `SEM_ESPELHO_LOCAL_COM_HASH`.

**Distinção essencial:** o validador **falha** por inconsistência de integridade da foto PR80 (fonte atual ausente quando deveria estar presente, SHA atual falso, C0-J/M/DEC-016 indevidos, vista/contagem incorreta, composto com blob local adulterado), mas **não mascara nem promove** uma âncora histórica inválida: ela aparece como **PENDÊNCIA** no relatório, não é tratada como C0-J. A CI verde certifica somente que a análise de pendências **foi executada**, não que todos os históricos são autênticos.

## Reproduzir / artefato de análise

```bash
git clone --filter=blob:none https://github.com/raphaelpetta/codigo-legislacao-federal.git
cd codigo-legislacao-federal
git fetch origin d1d733561944d67d3d3ffa13c32763784d5cdb6c
git worktree add experimental d1d733561944d67d3d3ffa13c32763784d5cdb6c
python3 -m unittest discover -s tests -p 'test_auditar_proveniencia_pr80.py' -v
python3 scripts/auditar_proveniencia_pr80.py --experimental-root experimental --report relatorios/pr80_proveniencia_60.json
```

O workflow `auditoria-proveniencia-pr80.yml` usa checkout Git com histórico completo e publica `clf-pr80-proveniencia-60-q` como artefato contendo **todos os 60 resultados individuais**; logs identificam pendências nominais. Ele mantém o PR #80 como draft e não corrige seus manifestos em lote. Ao alterar a fotografia do PR #80, **atualizar o SHA pinado e reexecutar** em novo PR independente, sem seguir `HEAD` móvel silenciosamente.

## Portas A/B/C ainda abertas

1. **Fonte autêntica (A):** nem SHA Git nem duas apresentações HTML conferem, por si, autenticidade do DOU, retificações ou vigência na data relevante. Os 75 textos editoriais CPC82–97 de T24 continuam sem segunda transcrição independente.
2. **Referente e efeitos (B):** um arquivo com hash igual em dois commits pode conter lei revogada, referência deslocada, recorte incompleto ou risco C1, como T07. Auditoria documental não avalia equivalência material.
3. **Aprovação legítima (C):** C0-J exige revisão jurídica independente; M e DEC-016 dependem de decisão humana expressa. Nenhum aumento de cobertura na `main` é criado por esta rotina.

**Estado:** `Q_SEM_C0_J`, C0-J=0, M=0, DEC-016 pendente, nenhuma revogação. A ordem de saneamento será definida pelos erros de ancoragem e ganho marginal jurídico efetivamente encontrados no relatório.
