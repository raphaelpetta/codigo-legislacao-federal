# T29.M01 — Pacote de continuidade da rodada 18 / F4-2 (14/10/2026)

**Dono:** T29.M01 (auditoria textual seletiva). **Issue:** [#40](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/40). **PR draft:** [#41](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/41). **Branch:** `modulo/T29-M01-segurados-dependentes-f0-f1-20261014`. Baseline main do início da frente: `16fba172c875c7a0de388288fe70005c944021d6`. **Lei vigente base:** CF/1988 + EC103. Nenhuma hipótese da Constituição alternativa usada como direito positivo.

## FEITO
- [F42_ESPELHO_LITERAL_SEIS_PARES_SHA256.csv](F42_ESPELHO_LITERAL_SEIS_PARES_SHA256.csv) — seis pares de transcrições **da Câmara, norma atualizada**, com texto reproduzido, hash SHA256 de **transcrição manual normalizada em Unicode NFC** e resultado: **5 coincidências**, **1 divergência (`do` na Câmara/8213 × `no` na Câmara/8212)**. Hashes **NÃO são checksums dos bytes das páginas oficiais**, nem certificação DOU.
- [F42_TRIANGULACAO_SINDICAL_06_FONTES.csv](F42_TRIANGULACAO_SINDICAL_06_FONTES.csv) — versões **Câmara/Planalto/Lei 9.528/1997**, duas leis, seis observações. **Três formulações** na cadeia do §4º da 8213: Câmara consolidada `do Regime`, Planalto `no Regime`, lei alteradora original disponível `no Regimento`. **Não foi provada eventual retificação/republicação em fac-símile DOU**, preservar Q.
- [RELATORIO_F42_6_PARES_PROVA_LITERAL_E_DIVERGENCIA_FONTE.md](RELATORIO_F42_6_PARES_PROVA_LITERAL_E_DIVERGENCIA_FONTE.md): procedimento de transcrição, fontes, limites de hash, efeitos A/B e bloqueios para fusão. README atualizado.
- Fontes oficiais consultadas: [Lei8213 Câmara atualizada](https://www2.camara.leg.br/legin/fed/lei/1991/lei-8213-24-julho-1991-363650-normaatualizada-pl.html), [Lei8212 Câmara atualizada](https://www2.camara.leg.br/legin/fed/lei/1991/lei-8212-24-julho-1991-363647-normaatualizada-pl.html), [ambas](https://www.planalto.gov.br/ccivil_03/leis/l8213compilado.htm) [compiladas no Planalto](https://www.planalto.gov.br/ccivil_03/leis/l8212compilado.htm), [publicação original Lei9528 Câmara](https://www2.camara.leg.br/legin/fed/lei/1997/lei-9528-10-dezembro-1997-349414-publicacaooriginal-1-pl.html), [Lei9528 Planalto](https://www.planalto.gov.br/ccivil_03/leis/l9528.htm); a economia familiar indica [Lei11718/2008](https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2008/lei/l11718.htm).
- **Nenhum caso dos 51 testes de F2-C duplicado:** estes seis são **pares de normas**, não seis novos cenários. Nenhum outro módulo alterado ou reforma ratificada.

## PENDENTE
1. **F4-2 é auditoria literal de transcrição**, não obtenção de snapshot/bytes do DOU. Não anunciar hash do HTML oficial ou identidade histórica integral das duas leis.
2. **Dirigente sindical:** `Regimento` da publicação original Lei9.528 versus Planalto compilado `Regime` e Câmara atualizada da Lei8213 `do`; exigido fac-símile DOU + eventual errata e cadeia da consolidação; não corrigir inadvertidamente ou equiparar somente por intenção aparente.
3. **Cinco trechos iguais na fonte Câmara:** ainda carecem de prova de efeitos, histórico temporal por ato e manifestação dos donos M02/M05/M06/T01. Identidade na compilação não equivale a C1 certificado, especialmente para categoria de empregado/segurado especial.
4. Decisões centrais pendentes: DEC-016 veículo legislativo, F2-D/F6, arquitetura A/B ainda hipóteses, incerteza sobre PSA, facultativo 14/16, STF Tema1271 guarda, carência materna e colisão art73-A pertencente a M05/T01/M06. Microdados SUIBE seguem 403, pedido LAI **não protocolado**.

## PRÓXIMO — F4-3 de proveniência e teste jurídico
- Priorizar busca oficial do **fac-símile DOU de 11/12/1997** (Lei9528) e eventual retificação da redação `Regimento`, sem presumir que houve errata.
- Conferir os cinco trechos coincidentes com respectivas versões originárias/alteradoras e verificar se eventuais variantes entre Planalto/Câmara não alteram conclusão.
- Submeter as seis origens aos módulos titulares e testar diferenciação custeio/prestação/prova. Somente então classificar C0/C1/M como **proposta não ratificada** e comparar alternativas A/B.
- **Sem aprovação F5, fusão, revogação, reforma M, CI confirmado, merge ou alteração de `main`**.

**Critério de continuidade:** uma nova rodada precisa avançar comprovadamente **proveniência textual/história ou efeitos**, não duplicar hashes de transcrições sem fonte independente.
