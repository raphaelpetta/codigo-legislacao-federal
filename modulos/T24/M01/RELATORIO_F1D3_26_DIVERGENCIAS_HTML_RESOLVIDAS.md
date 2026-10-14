# T24.M01 — F1-D3: encerramento das 26 falsas divergências HTML dos arts. 82–97 do CPC
**Data de corte:** 14/10/2026. **PR:** [#38 draft](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/38), main-base 16fba172c875c7a0de388288fe70005c944021d6.

## A. Resultado da segunda validação automática
O [extrator versionado](../../../scripts/extrair_f1d_t24.py), acionado por [workflow GitHub](../../../.github/workflows/extrair-cpc-f1d.yml), comparou por unidade os textos dos CPC arts.82–97 na [publicação 2015 da Câmara](https://www2.camara.leg.br/legin/fed/lei/2015/lei-13105-16-marco-2015-780273-publicacaooriginal-146341-pl.html) e na [compilação Câmara em 2026](https://www2.camara.leg.br/legin/fed/lei/2015/lei-13105-16-marco-2015-780273-normaatualizada-pl.html).

A execução [#38530844010](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38530844010) terminou **aprovada**, com [artefato JSON/CSV e hashes](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38530844010/artifacts/11877627151), e demonstrou:
- **45 pares** reconhecidos diretamente pelo extrator primário como iguais.
- **26 pares** antes apontados como divergentes por interrupção de marcadores HTML internos na edição compilada, agora identificados como **falsos positivos**: a redação original integral constava **no mesmo artigo** da fonte HTML compilada, como sequência contínua após normalização de espaços.
- **4 acréscimos efetivos** pós-publicação original, a saber art. 82 §3º ([Lei 15.109/2025](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15109.htm)) e art. 85 §§6º-A, 8º-A, 20 ([Lei 14.365/2022](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2022/lei/l14365.htm)).
- **Zero divergências não explicadas pelo teste entre 2015 e a compilação selecionada** para as outras 71 unidades.

**Nova salvaguarda posterior ao resultado inicial:** o script passa a exigir **ocorrência única** do texto original **dentro do próprio artigo**, registrando o número de ocorrências; a evidência dessa versão precisa ser lida no novo job de CI após o commit. Os 71 textos reproduzidos e conferidos podem ser usados como **candidatos a concordância documental técnica**, ainda não C0-J e sem declaração de equivalência legal de CLF. Os quatro acréscimos requerem confirmação independente do texto consolidado/lei alteradora/DOU.

## B. Limites da prova e espécies de equivalência
**O que foi comprovado:** localização do texto integral dos 71 dispositivos não acrescentados no mesmo artigo de duas versões publicadas pela Câmara, com identificação técnica de falso positivo da estratégia primária de corte de parágrafos e controle de hashes das fontes.

**O que NÃO foi comprovado:** que a redação nunca sofreu alteração e reconstituição entre 2015 e 2026, que uma retificação do DOU inexista, que o conteúdo normativo isolado preserve o mesmo significado se transferido para outro Código, que a lei especial ou atos de competência sejam absorvíveis, ou que já haja cláusula válida de revogação. As fontes são duas **fotografias** oficiais, não prova exaustiva da cadeia histórica. A captura secundária por elementos HTML `p` identificou estruturas diferentes nas duas páginas (130 versus 4.501 blocos), e **não foi capaz de verificar os 16 caputs em ambas**; seu diagnóstico permanece registrado para melhoria, sem ser artificialmente computado como sucesso. A prova dos 26 ocorreu por **confronto do texto integral do mesmo artigo**, não pelo método secundário de `p`.

## C. Consequências jurídicas prioritárias
**CPC art. 82 §3º:** dispensa do adiantamento de custas pelo advogado em cobrança/execução/cumprimento de honorários, com transferência final ao réu/executado se der causa. Distinguir competência processual federal de taxa judiciária estadual, acesso à justiça e incidência temporal. A lei entrou em vigor com publicação 14/03/2025; efeitos em casos em curso exigem pesquisa.

**CPC art. 85 §§6º-A, 8º-A e 20:** textos incorporados em 2022 que interagem com [Tema repetitivo 1076/STJ](https://processo.stj.jus.br/repetitivos/temas_repetitivos/pesquisa.jsp?cod_tema_final=1076&cod_tema_inicial=1076&novaConsulta=true&tipo_pesquisa=T), regime de honorários por escalões da Fazenda Pública, equidade excepcional e controvérsia constitucional no [Tema 1255/STF](https://portal.stf.jus.br/jurisprudenciaRepercussao/tema.asp?num=1255). Conferir efeito de vetos, intertemporalidade, EAOAB e repercussão geral antes de classificar identidade jurídico-material.

**CPC arts. 91 e 95 e arts. 98–102 (F1-C):** adiantamento de perícias por MP/Fazenda/Defensoria, custeio orçamentário de perícia de beneficiários JG, suspensão de exigibilidade da sucumbência e proteção recursal de preparo. Não converter custeio específico em obrigação genérica de depósito prévio. Interfaciar T24.M03/M04, T06, T32 e legislação estadual de custas.

## D. FEITO / PENDENTE / PRÓXIMO
**FEITO:** resolução probatória dos 26 falsos positivos HTML, 71 candidatos técnicos localizados na fonte consolidada e 4 acréscimos assinalados, com evidência por URL/artigo, hashes e CI; não alterar antiga matriz histórica nem apagar alerta.
**PENDENTE:** aceitação da revisão com ocorrência única no SHA mais recente; auditoria DOU/alteradores/retificações dos quatro acréscimos; cadeia legislativa; jurisprudência pertinente por dispositivo e competência; distinção C0-T documental de C0-J material; estratégia `DEC-016`.
**PRÓXIMO:** avançar para concordância jurídico-material Q/C0-J restrita por bloco, começando art. 82 §3º e art. 95/91, e testes de integração com gratuidade; manter as 75 unidades como espelho técnico pesquisado. Não converter automaticamente em norma nova sem aprovação.
