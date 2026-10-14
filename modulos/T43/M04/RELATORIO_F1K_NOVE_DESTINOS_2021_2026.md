# T43.M04 — F1-K: completa a proveniência das nove posições remanescentes dos arts. 51–54
**Corte:** 14/10/2026; [PR #43](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/43) draft. O novo cotejo cruza **Lei 14.129/2021, redação introduzida**, com os **quatro diplomas de destino na versão Câmara consultada em 2026**. Não declara equivalência jurídica C0-J, nem dispensa cadeia DOU, competência e DEC-016.

## FEITO — nove dispositivos verificáveis
[Matriz de nove textos, riscos e fontes](F1K_NOVE_DESTINOS_LITERAL_2021_2026.csv), [extrator/comparador automático](../../../scripts/auditar_t43_f1k_nove.py) e [workflow `auditar-t43-f1k.yml`](../../../.github/workflows/auditar-t43-f1k.yml).
- **Lei 7.116/1983, art. 3º, alínea h:** número de inscrição no CPF como informação da Carteira de Identidade (1 registro). A alteração de 2023 sobre a alínea **g** e §§1º–3º foi confrontada separadamente na F1-J.
- **Lei 12.527/2011, art. 12 caput e §§1º–2º** (3 registros): gratuidade da busca/fornecimento de informação, ressarcimento apenas dos custos pertinentes à reprodução material e isenção para insuficiência econômica sob declaração conforme Lei 7.115/1983. Não confundir dever de transparência ativa com cobrança livre por pesquisa.
- **Lei 12.682/2012, art. 3º caput** (1 registro): digitalização deve assegurar integridade, autenticidade e, quando necessário, confidencialidade, com **assinatura eletrônica**. A alteração de 2021 substituiu a referência anterior a certificado ICP-Brasil obrigatório no caput; verificar demais normas aplicáveis a documentos públicos, inclusive parágrafos da mesma lei.
- **Lei 13.460/2017, art. 7º §6º, art. 10-A caput e §§2º–3º** (4 registros): Cartas e Base Nacional de Serviços Públicos, apresentação de documento com CPF para identificação, declaração de CPF acompanhada de documento de fé pública, e possibilidade de ato excepcional do ente federativo ou Poder. O art.10-A §1º, reescrito em 2023, está na F1-J e **não** foi somado aqui.

A [CI #38586703047](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38586703047) verificou **nove coincidências textuais de 2021 na respectiva norma alteradora e nove nas quatro fontes consolidadas atuais** — sem divergência; [artefato JSON com SHA-256 de cinco fontes e resultados individuais](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38586703047/artifacts/11904884118). São ocorrências da redação introduzida, não prova de todas as cláusulas que alteram os efeitos jurídicos.

## Resultado consolidado
Com a [F1-J dos cinco dispositivos reescritos pela Lei 14.534/2023](F1J_COTEJO_LITERAL_5_POSICOES_2021_2023.csv), estão documentalmente rastreadas as **14 posições** selecionadas de destinação dos **arts. 51–54 da Lei 14.129/2021**:
- **5 posições** com redação posterior de 2023 identificada e cotejada;
- **9 posições** com texto de 2021 ainda localizado nas compilações consultadas.

**Não inferir que os arts. 51–54 devem ser colocados de novo como texto autónomo do CLF.** A função de lei alteradora já se materializou nos diplomas de destino; copiar os dois conjuntos produz duplicação e pode apagar alterações posteriores. A Lei 14.534/2023 contém **prazos históricos de implementação** (12 e 24 meses no art.9º) que também não devem ser renovados silenciosamente.

## Gates jurídicos restantes
A coincidência literal entre duas páginas da Câmara **não garante equivalência C0-J** na futura localização legislativa. Faltam conferência DOU, revisão dos atos de adoção federativa e da hierarquia/competência, LAI/LGPD/assinaturas e direitos à informação, efeitos intertemporais e decisão estrutural DEC-016. **FEITO:** 14 destinos com cotejos, 5 fontes atuais reexecutáveis para nove posições. **PENDENTE:** auditoria completa da cadeia de cada destino e direitos em outros diplomas, avaliação de limites do futuro CLF. **PRÓXIMO:** redline jurídico 1:1 de direito vigente por lei destinatária, não por artigo meramente alterador, e revisão independente de todas as garantias.
