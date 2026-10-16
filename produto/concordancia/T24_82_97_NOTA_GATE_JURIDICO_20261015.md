# T24 — Gate jurídico do CPC arts. 82–97: 75 posições e 36 do art. 85

**Rodada 03 · 15/10/2026 · Q jurídico / não homologado.** Fonte setorial [PR #38](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/38), commit `3fdbfa10b8d288b1cef56c78b47cf3cb1eb28745`, `modulos/T24/M01/F1D_INVENTARIO_ART82_97_SUBUNIDADES.csv` (Git blob `4928ddd37b1d9c2dfcf8273092f699e97367ebbc`). [Matriz de 75 destinos sem texto transcrito](T24_82_97_GATE_75_SEM_TEXTO.csv). **75 subunidades localizadas não equivalem a 75 textos integrados ou C0-J.**

## Gate por artigo e fonte
| CPC | Unidades | Porta jurídica necessária |
|---|---:|---|
| 82 | 4 | §3º acrescido pela Lei 15.109/2025, dispensa específica de antecipação de custas em cobrança de honorários: não transformar em isenção geral; preservar causalidade |
| 83–84 | 7 | Caução de quem reside fora do Brasil, dispensas por tratado, execução, reconvenção; despesas abrangentes |
| **85** | **36** | Crédito do advogado, faixas progressivas para Fazenda Pública, majoração recursal, §8º excepcional, §§6º-A/8º-A/20 de 2022, dez remissões do §20; impedir resumo materialmente regressivo |
| 86–90 | 12 | Sucumbência, litisconsórcio, jurisdição voluntária, desistência, transação e reconhecimento |
| 91–94 | 6 | Custeio institucional e orçamentário de perícias, nova ação após extinção, adiamento injustificado, custas de assistente |
| 95 | 8 | Adiantamento e rateio de perícia, remissão CPC 465 §4º, JG CPC 98 §§2º–3º, recursos da Defensoria |
| 96–97 | 2 | Destinação de multas, fundos estaduais/federais e competência financeira |

A fonte textual é o [CPC atualizado pela Câmara](https://www2.camara.leg.br/legin/fed/lei/2015/lei-13105-16-marco-2015-780273-normaatualizada-pl.html). A pesquisa setorial do PR #38 já produziu relatório e artefatos técnicos do espelho **integral do art. 85 (36 posições)**, mas a central ainda não possui neste commit a versão textual reutilizável das 75 unidades, com fonte/hashes próprios. **Não transferir trechos da minuta P1–P7 do PR #38 como se fossem C0-J:** há mudanças potenciais de sujeito obrigado, custo orçamentário, remissões e regimes excepcionais.

## Julgados imprescindíveis, por efeito

- [Tema 1.076/STJ](https://processo.stj.jus.br/repetitivos/temas_repetitivos/pesquisa.jsp?cod_tema_final=1076&cod_tema_inicial=1076&novaConsulta=true&tipo_pesquisa=T): equidade não substitui percentuais legais porque a base seja elevada; §§2º–3º prevalecem fora das exceções legais.
- [Tema 1.313/STJ](https://processo.stj.jus.br/repetitivos/temas_repetitivos/pesquisa.jsp?cod_tema_final=1313&cod_tema_inicial=1313&novaConsulta=true&tipo_pesquisa=T): demandas de prestação de saúde contra Poder Público são arbitradas por equidade **sem aplicar o art.85 §8º-A**; não universalizar tabela OAB.
- [Tema 1.190/STJ](https://processo.stj.jus.br/repetitivos/temas_repetitivos/pesquisa.jsp?cod_tema_final=1190&cod_tema_inicial=1190&novaConsulta=true&tipo_pesquisa=T): cumprimento não impugnado contra Fazenda, mesmo RPV, sem honorários sucumbenciais; **modulação para cumprimentos iniciados após publicação do acórdão**.
- [Tema 1.255/STF](https://portal.stf.jus.br/jurisprudenciaRepercussao/tema.asp?num=1255): repercussão geral reconhecida sobre equidade em bases elevadas; **mérito não certificado como julgado nesta rodada**.

Estas leituras são gates de jurisprudência, não supressões automáticas do CPC ou declarações sobre invalidade de dispositivos. Efeitos temporais, distinções de casos e competência de tribunais exigem parecer adicional antes de C0-J ou C1.

## Próxima transformação em texto normativo experimental

1. Extrair/cotejar **75 transcrições literais** contra Câmara, DOU, cadeia original e alteradoras, preservando §§6º-A/8º-A/20 do art.85 (2022) e §3º do art.82 (2025).
2. Gerar fonte de 75 IDs e texto derivado, com rastreabilidade SHA; conciliar com a vista T24 atual de **106 unidades** para meta condicional de **181 unidades / 33 artigos** neste recorte ampliado.
3. Conferir remissões expressas art.85/95/98/465/77, competência e orçamento por unidade; classificar C0-T e C0-J independentemente, sem presunção de efeito por igualdade de palavras.
4. Manter **DEC-001** como objetivo e **DEC-016** pendente; nenhuma M aprovada, nenhuma revogação e nenhum conflito resolvido por simples concatenação.

**FEITO:** inventário dos 75 destinos e riscos, 36 art.85 identificados, jurisprudência e transições explicitadas. **PENDENTE:** texto integral de 75 unidades na central, DOU histórico, QA em CI e equivalência jurídica. **PRÓXIMO:** 36 art.85 + 4 art.82 + 8 art.95 como subfaixa de 48 unidades de alto impacto, seguida das 27 restantes.
