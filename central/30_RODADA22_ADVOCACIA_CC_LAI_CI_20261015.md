# CLF — R22: T06, T16, LAI e porta de auditoria (15/10/2026)

**Base:** PR #68 HEAD `c75a0ae31405c346bddf4ea5164019dd21f79453`. Trabalho documental Q em draft, não lei vigente, sem ratificação C0-J/M ou decisão DEC-016.

## FEITO — amplitude controlada

- **T06:** [vista](../produto/vistas/T06_ADVOCACIA_LEI8906_ART1_2_PREVIA_Q.md), [manifesto](../produto/fontes/T06_M05_OAB_11_R22_v1.json), 2 artigos/11 unidades positivas Q, Lei 8.906/1994 arts. 1º–2º. ADI 1.127: expressão qualquer art.1º,I não homologada; art2-A fora, DOU e Lei14365/2022 pendentes.
- **T16:** [vista](../produto/vistas/T16_CC_ATOS_ILICITOS_ART186_188_PREVIA_Q.md), [manifesto](../produto/fontes/T16_M01_CC_6_R22_v1.json), 3 artigos/6 unidades positivas Q, CC arts. 186–188. Ato ilícito e abuso, excludentes art188; arts929–930 e responsabilidade objetiva preservados; DOU pendente.
- **T10:** [vista](../produto/vistas/T10_LAI_ART5_6_PREVIA_Q.md), [manifesto](../produto/fontes/T10_M01_LAI_5_R22_v1.json), 2 artigos/5 unidades positivas Q, LAI arts. 5º–6º. Dever de acesso e gestão/proteção de informação; preservados sigilo e LGPD, DOU pendente.

**Corpus:** 51 componentes Q em 34 de 48 títulos, 281 artigos de origem, 960 unidades positivas e 1 histórico T07, incremento +7 artigos/+22 positivas/+2 títulos. Os 14 títulos restantes são lacunas explícitas, não equivalência quantitativa da legislação federal.

**QA:** três novos espelhos Git blob SHA e vistas vinculadas em manifestos; índice, Código, matriz, quadro, painel, guia, fila com 69 tarefas únicas e script `scripts/validar_r22_fonte_e_codigo.py` atualizados. O script valida identidade fonte-vista, SHA, artigos, IDs, Q, índice/matriz/painel/fila e reconstrução de Código. **Adicionar script não representa execução exitosa**.

## PENDENTE — bloqueios jurídicos e de CI

- P0 [incidente #66](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/66): `runner-smoke` sem checkout falhou tanto quanto jobs com checkout, com etapas vazias e logs indisponíveis/404. Evidência insuficiente para atribuir causa a Python, política de Actions, cobrança, runner ou permissão. Obter mensagem/anotações de check-run no GitHub e só corrigir causa demonstrada.
- Estatuto OAB art1 I — ADI1127 e extensão da reserva, CF133, DOU original e alteradoras; CC arts186-188 e reparação arts929/930, regimes objetivos, precedentes; LAI5/6, LGPD/sigilos/órgãos abrangidos e DOU2011. Texto HTML institucional não é cotejo fac-símile de DOU.
- Reservas de lei complementar, normas especiais, jurisprudência, origem e destino por efeito permanecem portas independentes. **C0-J=0; M=0; DEC-016 pendente; revogação, renumeração definitiva e merge=0. T13 intocado.**

## PRÓXIMO

Investigar bloqueio Actions com mensagem do run/check-run, auditar por efeito ADI1127/CC188/LAI6, e avançar horizontalmente apenas segundo ganho marginal verificável, sem presumir homologação por número de títulos.
