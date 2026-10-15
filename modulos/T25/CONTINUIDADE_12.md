# T25.M03 — Continuidade 12: dosimetria e confronto CP × CPM

**Data de corte e fuso:** 14/10/2026 (America/Sao_Paulo). **Frente responsável:** T25.M03, interfaces T25.M01/M02, T26/T27, T01 e T02. **Issue [#31](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/31)** · **[PR #32 (draft)](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/32)** · branch `modulo/T25-parte-geral-f0-f1`. **Baseline CLF `main`** no início/fim das pesquisas = `16fba172c875c7a0de388288fe70005c944021d6`. **CF alternativa `main` (apenas verificação de SHA, não incorporada ao direito)** = `2a770a8136f8ca4877e865be3e3b7745a6d4b168`. **HEAD ciclo11** `dccd5e868aa75e2c646f1784eca485989b536893`; confirmar HEAD/CI deste ciclo ao encerrar.

## FEITO — trabalhos realmente persistidos na branch, não na main

| Entrega | Arquivo | Natureza/status |
|---|---|---|
| 86 unidades descritivas de **19 artigos**, CP 59–68 (45) e CPM 69–77 (41) | `INVENTARIO_DOSIMETRIA_CP59_68_CPM69_77_CICLO12.csv` | F1 seletivo por subunidade; **não** espelho textual literal C0-T, nem auditoria histórica integral |
| 22 relações entre regras de base, agravantes, atenuantes, reincidência, confissão, fases e causas especiais | `CONCORDANCIA_CRITICA_DOSIMETRIA_CICLO12.csv` | F2 análise de riscos **Q**, não equivalência jurídica C0-J; nenhuma alteração M ratificada |
| 10 simulações com verificação aritmética programática | `SIMULACOES_FASES_DOSIMETRIA_CICLO12.csv` | pena hipotética de reclusão 5–10 anos; pena-base 60/72 meses, piso de 60 e frações 1/6, 1/5, 1/3; nenhuma pena individual ou tipo real calculado |
| Cinco fontes qualificadas de precedentes | `JURISPRUDENCIA_DOSIMETRIA_CICLO12.csv` | STF Tema158, STJ Súmula231/REsp1869764, Tema1194/REsp2001973, Súmula545 revista e STM7000232; âmbito e modulação distintos |
| Análise crítica, problemas PROB-T25-0036–0043, referências e agenda do próximo ciclo | `DOSSIE_12_PENAS_DOSIMETRIA_CP_CPM.md` | F2/F3/F4 documentais, **F5 não iniciado neste subbloco** |
| Índice cumulativo e este handoff | `README.md` e `CONTINUIDADE_12.md` | fonte de continuidade metodológica |

### Fontes primárias efetivamente consultadas

1. **CP 59–68 — Câmara atualizada**: https://www2.camara.leg.br/legin/fed/declei/1940-1949/decreto-lei-2848-7-dezembro-1940-412868-normaatualizada-pe.html . Lei **15.159/2025** introduziu art.61 II m (instituição de ensino); Lei **15.160/2025**, https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15160.htm, mudou art.65 I (idade e violência sexual contra mulher).
2. **CPM 69–77 — Câmara atualizada**: https://www2.camara.leg.br/legin/fed/declei/1960-1969/decreto-lei-1001-21-outubro-1969-376258-normaatualizada-pe.html ; **Lei 14.688/2023**: https://www2.camara.leg.br/legin/fed/lei/2023/lei-14688-20-setembro-2023-794728-normaatualizada-pl.html . Destaques: CPM70 II h atualizado, CPM77 caput alterado e PU introduzido.
3. **STF Tema158** https://portal.stf.jus.br/jurisprudenciaRepercussao/verAndamentoProcesso.asp?classeProcesso=RE&incidente=2663001&numeroProcesso=597270&numeroTema=158 .
4. **STJ REsp 1.869.764/MS**, 3ª Seção, 14/08/2024, Súmula231 e mínimo; fonte oficial https://scon.stj.jus.br/SCON/jurisprudencia/toc.jsp?livre=%28RESP+INPATH%28CLAS%29+AND+1869764+INPATH%28NUM%29%29+OR+%28NEAR%28%28RESP%2C1869764%29%2C0%2CTRUE%29+INPATH%28SUCE%29%29 .
5. **STJ Tema1194**, 3ª Seção, 10/09/2025, REsp2001973/RS, publicado 16/09/2025, trânsito 30/10/2025, **modulação de efeitos prejudiciais**; ficha oficial https://processo.stj.jus.br/repetitivos/temas_repetitivos/pesquisa.jsp?cod_tema_final=1194&cod_tema_inicial=1194&novaConsulta=true&tipo_pesquisa=T . **Súmula 545 revista** em 2025 https://processo.stj.jus.br/SCON/sumstj/toc.jsp?sumula=545.num. .
6. **STM Ap 7000232-60.2024.7.00.0000**, reproduzido em revista e **examinado com votos e páginas no ciclo09**, reutilizado no presente ciclo sem afirmar nova inspeção de fonte: https://revista.stm.jus.br/index.php/periodicos/article/download/jurisprudencia-05-v34-n1-2024/88/238 .

## PENDENTE / NÃO VERIFICADO

- **Diferenças legislativas materiais ainda em Q:** CP64 I/II × CPM71 §§1–2 (reincidência), CP65 I e CP61 II m pós-2025 × CPM72/70, CP65 III d × CPM72 III d e jurisprudência do STJ, CP66 × sanções militares, CP68 PU × CPM76 PU, pena-base CP59 × CPM69, circunstâncias em serviço e hierarquia. **Não presumir** que texto diferente seja necessariamente constitucionalmente inválido ou que mesma finalidade prove equivalência.
- **Originais/alteradores:** faltam tabelas de vigência por fatos de 1940/1969/1984/2023/2025 e conferência de DOU autenticado e retificações por subunidade; CPM70 II h e 77 em 2023, CP65 I e 61 II m em 2025 demandam controle antes/depois. DOU Lei7.209/1984 p.10217 ainda não foi visualmente conferido nas rodadas anteriores.
- **Natureza CPM35:** penal militar dispõe mitigar por erro escusável, mas a controvérsia atenuante vs minorante permanece, embora CPM73/76/77 definam efeitos distintos; STF Tema158 e STJ231 são sobre atenuantes genéricas, não encerram classificação de art35. Sem escolher **A2-D1**, **B2-DP** ou **B2-DM** (F5 experimental anterior).
- **CPM46:** atenuação por excesso doloso e classificação/fração ainda Q; as propostas de 1/5–1/3 em A2/B2 representam **M**, não declaração de percentual legal literal do CPM46.
- **Limites das simulações:** exemplos não correspondem a pena real, não incorporam multa, substituição, prisão provisória, espécies de pena, regime, concurso de crimes, sursis e execução. Não extrapolar para condenação concreta.
- **Jurisprudência:** Tema1194 STJ dirige-se CP65 III d e a modulação não pode ser esquecida; a aplicação a CPM72 III d depende de exame próprio. Julgados militares sobre reincidência e pena-base precisam investigação específica. Não afirmar consenso quando houver voto divergente.
- **Constituição e governança:** devido processo, individualização, igualdade, legalidade e direito de defesa devem informar F4/F5. CF/1988 vigente não se confunde com CF projetada em repositório independente. DEC-016 e veículo normativo sem decisão; nenhuma alteração/revogação ratificada e PR fora de main.
- **CI:** verificação de integridade do HEAD final pendente depois deste commit; CI não é prova de mérito jurídico.

## PRÓXIMO — execução reproduzível em T25.M03

**Ciclo13:** expandir para **espécies de pena, conversão, substituição e execução inicial**, começando com CP 32–58 × CPM 55–68 (subunidades e relações funcionais, sem presunção de equivalência). Buscar **dois tipos legais concretos** (um comum e um militar) com marco temporal para testar espécie/pena mínima, fase e conversão, sem criar condenação simulada determinística. Coordenar substituições/penas não privativas com T27 e alterações recentes.

**Critério de aceite:** matriz por dispositivo com fonte e data, confronto de regime, espécie, quantum, pena inicial, efeitos de substituição, possibilidade de sursis e tempo, mais testes adversariais e jurisprudência. Preservar classificação Q/M por consequência, sem supor que escolher B2-DP ou B2-DM se tornou possível por simulações abstratas.

**Dependências:** T01 (vigência/DEC-016), T02 (direitos), T16 (efeitos civis), T25.M01–M03, T26 (processo/competência/prova), T27 (execução), T45 (militar e hierarquia), T23/T47/T48 (tratados).

- [x] `main`, PR e branch consultadas antes/depois das alterações; nenhum merge realizado.
- [x] 86 subunidades indexadas com IDs únicos e mudança de 2023/2025 notada.
- [x] 22 relações Q e dez cálculos aritméticos verificados.
- [x] Cinco registros judiciais com limites, dados de fontes e temporalidade.
- [x] FEITO/PENDENTE/PRÓXIMO e interface com minutas A2/B2.
- [ ] Confirmar GitHub Actions após o commit final e comentar resultado na PR.

**Padrão:** `governanca/18_PROTOCOLO_CONTINUIDADE_POR_RODADA.md`.
