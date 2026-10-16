# T25.M01 — auditoria R3 de integração documental da Parte Geral do CP, arts. 1º–12

**Corte:** 16/10/2026. **Objeto:** apenas 12 artigos/39 unidades positivas documentadas, sem promulgação e sem efeitos normativos. **Fonte setorial fixa:** PR #32, commit `3f0b56273caebfdbaba87ec4e87988da9f12c6c9`, Git blob do espelho `40b5c03d72f975aad1339c605399f7f66ec056d0`. **Fonte oficial de confronto** [Decreto-Lei 2.848/1940 compilado no Planalto](https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848compilado.htm), com atualização central da Parte Geral pela [Lei 7.209/1984](https://www.planalto.gov.br/ccivil_03/leis/1980-1988/l7209.htm). Não há autenticação integral dos DOU/retificações e toda a cadeia penal neste lote.

## Escolha marginal em comparação com T24
**T25 preferido** para lote de integração pela unidade setorial única de 39 textos fixados por hash, concordância 39×39 e gerador `--check` utilizável sobre checkout SHA fixado. **T24 CPC70–102** oferece 33 artigos e 181 unidades, mas é composto (106 PR #38 e 75 transcrições editoriais). A segunda conferência independente de 75, lei alteradora e jurisdição real sobre gratuidade/custas/honorários demanda R3 mais complexo. **T24 continua a frente vertical prioritária**, não recusada ou apagada.

## A — identidade e temporalidade
- CP Decreto-Lei nº 2.848, de 07/12/1940, arts. 1º–12, texto compilado da Câmara/Planalto e **Lei 7.209/1984**: providenciar cadeia histórica original DOU e futuras normas alteradoras antes de concluir vigência e efeitos de fato concreto. A data do fato e a lei mais favorável exigem reconstrução própria.
- **Não confundir CP com Código Penal Militar, legislação extravagante, tratados, competência STJ ou Lei 13.445/2017**, nem usar direito constitucional hipotético em lugar da CF vigente.

## B — proveniência, origem e destino
- Espelho setorial PR #32 permanece externo, commit e blob imutáveis; 39 origens únicas; [matriz produto](../../produto/concordancia/T25_CP_ART1_12_39.csv) 39 origens × 39 destinos simbólicos; [manifesto](../../produto/fontes/T25_CP1_12_v1.json) e [gerador](../../scripts/gerar_previa_t25.py) verificam vista byte por byte. [Dez gates setoriais](../../central/08_T25_DEZ_GATES_ESPECIALIDADE_PENAL_20261015.csv) e [verificador ativo](../../scripts/validar_t25_gates_r3.py) tornam falha a mudança não declarada de texto, fonte, classe Q ou referente de CP12.
- O texto **`deste Código` no art. 12 refere-se ao Código Penal de origem** e sua subsidiariedade perante leis penais especiais. Não é o Código da Legislação Federal; reescrevê-lo para o CLF seria C1/M potencial e depende de decisão expressa. Numeração CP 1–12 não é numeração final do CLF.

## C — riscos adversariais R3 que permanecem Q
| Núcleo | Risco e garantia |
|---|---|
| CP arts. 1º–3º | Legalidade/anterioridade e proibição de lei penal mais grave retroativa; retroatividade benéfica, lei temporária ou excepcional e intertemporalidade |
| CP art. 7º §§ 2º–3º | Extraterritorialidade condicionada, dupla incriminação, extradição, consentimento e competência; não generalizar automaticamente a qualquer regime federal |
| CP arts. 8º–9º | Pena já cumprida no exterior e sentença estrangeira; competência e tratado aplicável, distinção entre homologação e transferência de execução |
| CP art. 11 | Frações de dia e antiga denominação monetária: efeito atual depende da disciplina da multa e sucessão monetária |
| **CP art. 12** | Lei especial prevalece quando disponha diferentemente; vedado transformar o futuro CLF inteiro em Código Penal |
| Direito especial | CP/CPM e legislação extravagante permanecem fora deste recorte; art. 13 e subsequentes não foram transpostos |

**Melhor objeção:** justapor o CP ao CLF geral pode sugerir que todas as regras gerais do CP irradiam para livros não penais, alterar responsabilidade sancionadora ou aplicar efeitos intertemporais errados. **Saída R0:** preservar referente textual ao Código Penal, com origem e escopo explicitados e normas especiais intactas. **R1/M:** reestruturação penal legislativa exige matriz de efeitos, competências, revisão independente e ratificação. **Resultado:** `INTEGRADO_EXPERIMENTAL_PARCIAL_Q` **somente documental**; zero C0-J, zero M aprovadas, nenhum artigo promulgado/revogado e DEC-016 pendente. Auditoria DOU/jurisprudência por instituto e revisão humana independente seguem pendentes.
