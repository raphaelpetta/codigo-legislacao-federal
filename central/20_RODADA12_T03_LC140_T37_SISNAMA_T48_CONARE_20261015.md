# CLF — Rodada 12: LC 140 (T03), SISNAMA (T37) e CONARE (T48)

**Corte:** 15/10/2026. **PR de execução:** [#57 draft](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/57), base PR #56 draft, integra a cadeia dependente **#49 → #53 → #54 → #55 → #56 → #57**; `main` preservada, sem merge ou alteração normativa promulgada. [Central permanente #48](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/48).

## FEITO — três recortes textuais com portas jurídicas autônomas

### T03.M01 — LC 140/2011 arts. 1º–3º: primeiro título federativo integrado

- [Espelho 10×10](../modulos/T03/M01_ESPELHO_LC140_ART1_3_10_Q.csv) → [prévia 3 artigos](../produto/vistas/T03_LC140_ART1_3_PREVIA_Q.md), [manifesto versionado](../produto/fontes/T03_M01_LC140_10_R12_v1.json), blob fonte `e334a875316cac76355793859c281933b96c3131`. Fonte [Câmara, publicação original](https://www2.camara.leg.br/legin/fed/leicom/2011/leicomplementar-140-8-dezembro-2011-611919-publicacaooriginal-134506-pl.html), [Senado: norma e DOU](https://legis.senado.leg.br/norma/572895).
- **Direito federativo:** LC 140 é **lei complementar** para a cooperação CF art. 23, e não lei ordinária; consolidá-la no mesmo arquivo de leitura não altera espécie, veículo, iniciativa, quórum ou revogação. A **atuação supletiva** (art. 2º II) substitui o titular nas hipóteses da LC; a **subsidiária** (III) auxilia quando solicitada. A confusão entre ambas alteraria competências e risco jurídico-federativo.
- [Retificação legislativa Câmara de 12/12/2011](https://www2.camara.leg.br/legin/fed/leicom/2011/leicomplementar-140-8-dezembro-2011-611919-retificacao-134533-pl.html) corrige nome de signatário na publicação original, sem demonstrar alteração dos arts. 1º–3º. **O original e a retificação não foram cotejados em fac-símile DOU**; equivalência jurídica continua Q, e [ADI 4.757](https://www2.camara.leg.br/legin/fed/leicom/2011/leicomplementar-140-8-dezembro-2011-611919-norma-pl.html) exige análise do âmbito constitucional.

### T37.M01 — PNMA arts. 5º–6º, redação de SISNAMA atualizada

- [Espelho 9×9](../modulos/T37/M01_ESPELHO_PNMA_ART5_6_9_Q.csv) → [prévia 2 artigos](../produto/vistas/T37_PNMA_ART5_6_PREVIA_Q.md), [manifesto SHA](../produto/fontes/T37_M01_6938_9_R12_v1.json), blob `e38a08c629bc2e3e46392cb530e93a63aac12470`, [Câmara versão atualizada](https://www2.camara.leg.br/legin/fed/lei/1980-1987/lei-6938-31-agosto-1981-366135-normaatualizada-pl.html).
- **Art. 6º inciso I:** versão atual contém redação alterada pela [Lei 15.190/2025, art. 63](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15190.htm), publicada em 08/08/2025 (com retificação no mesmo dia); fonte Câmara informa vigência após **180 dias**. Em 15/10/2026, a redação alterada já estava aplicável. Não reintroduzir versão de 1981.
- **Arranjo federativo:** SISNAMA inclui Conselho de Governo, CONAMA, órgão central, IBAMA/ICMBio e órgãos seccionais estaduais/locais municipais, com competências próprias. Texto histórico de referência ministerial não pode ser alterado editorialmente sem prova de sucessão; interface T03.M01 LC 140 e CF 23/24/225 fica por remissão, não por fusão de espécies.
- **T37 agora:** seis artigos / quarenta e uma unidades documentais Q. O inciso XI do art. 2º acrescido pela Lei 15.512/2026 permanece integrado na parte anterior.

### T48.M03 — CONARE arts. 11º–16º

- [Espelho 23×23](../modulos/T48/M03_ESPELHO_REFUGIO_ART11_16_23_Q.csv) → [prévia 6 artigos](../produto/vistas/T48_REFUGIO_ART11_16_PREVIA_Q.md), [manifesto SHA](../produto/fontes/T48_M03_9474_23_R12_v1.json), blob `8478bfb09467641e2a8355a7677491d86677acb0`; [Câmara original de 1997](https://www2.camara.leg.br/legin/fed/lei/1997/lei-9474-22-julho-1997-365390-publicacaooriginal-1-pl.html) e Planalto.
- CONARE: órgão colegiado e competências de reconhecimento/cessação/perda **em primeira instância**; regimento, composição, participação de representante de organização não governamental; **ACNUR voz, sem voto**; deliberação com quatro membros votantes, maioria simples e voto de desempate pelo presidente.
- O texto de 1997 usa nomes ministeriais que podem ter sido alterados por reestruturações administrativas; reproduzir literalmente em Q não certifica a composição **operativa em 2026**. Garantias de recurso ao Ministro da Justiça (arts. 29–31) e não devolução de art. 32 exigem expansão posterior e cotejo com Lei 13.445/2017 e tratados.
- **Resultado:** T48 Lei 9.474 agora **artigos 1º–21 em sequência contínua**, 21 artigos e 52 unidades Q (antes 15 artigos e 29 unidades com lacuna 11–16). A partir do art. 22 segue fora do corpus.

## FEITO — compilação e controles integrados

- [Código único Q](../produto/CODIGO_DE_TRABALHO.md), [índice](../produto/fontes/indice_livros.json), [painel](PAINEL_GERADO.csv), [quadro de 48 títulos](QUADRO_PRODUTO.csv), [fila](FILA_TRABALHO.csv) e [guia de leitura](../produto/00_LEIA_O_CODIGO.md) reconciliados no PR #57. [Validador incremental R12](../scripts/validar_r12_t03_t37_t48.py) foi inserido no roteiro de validação local.
- **171 artigos originais; 574 unidades documentais textuais +1 registro histórico T07; 14 componentes, oito títulos:** T03 3/10, T05 15/30, T07 78/214 +1 histórico, T24 33/181, T25 12/39, T28 3/7, T37 6/41, T48 21/52. O art. 15 da Lei 9.709 é registro textual de efeito temporal histórico de 1998, mas está dentre as 574 unidades, não constitui vigência futura do CLF.
- Verificação documental por leitura GitHub: manifestos SHAs, cardinalidade 10/9/23, correspondências, 171 cabeçalhos e montagem a partir do índice; **não se afirma execução local efetiva dos scripts Python, nem CI GitHub Actions bem-sucedida**. Reservas T13 preservadas.

## PENDENTE — autenticidade, competência e eficácia

1. **DOU em imagem e retificações oficiais:** LC 140/2011 publicação 09/12/2011 p.1, retificação 12/12/2011 p.2; PNMA 1981, alteradoras 1989/1990/2013/2025/2026 e refúgio 1997. Identificar toda supressão/alteração por espécie, órgão competente e vigência temporal. A fonte HTML institucional não certifica o texto promulgado por si.
2. **C0-J zero** em todo o Código: aprovar equivalência jurídico-normativa exigiria cotejo de remissões, sujeitos, competência, vetos e direito intertemporal por unidade e revisão humana, jamais somente similaridade textual ou hash.
3. **T03:** LC 140 arts. 4º–17 e ADI 4.757; cooperação ambiental e articulação com PNMA e lei de licenciamento, sem usurpar normas estaduais/municipais; espécie LC não homogeneizável sem DEC-016.
4. **T37:** organização do órgão central SISNAMA e competências efetivas pós-2025, controle de constitucionalidade/licenciamento e efeitos transitórios; texto conservador da lei original versus redação compilada.
5. **T48:** composição real CONARE em 2026, atos de funcionamento, direitos de defesa, recursos, proteção enquanto pendente, sigilo e tutela contra devolução (arts. 22–49).
6. **T28:** promulgação/publicação e transição constitucional da PEC 221/2019 sobre escala 6×1 permanecem não comprovadas no corte; nada no texto da CLT foi modificado nesta rodada.
7. Runner Actions, execução Python, compatibilidade PRs #46/#49/#53–#57 ainda aguardam avaliação; sem merge.

## PRÓXIMO

- T48.M03: arts. 22–32 com decisão, motivação, recurso e não devolução; hipótese especial de art. 3º III/IV sem habilitar retorno ao risco automaticamente.
- T03/T37: cotejo DOU PNMA e LC 140, ADI 4.757, art. 4º e LC 140 completa por blocos jurídicos, regramentos de licenciamento e CF 23/24/225.
- T28 PEC 221/2019: verificar documento de promulgação **antes** de mudar redações prospectivas, com transição da jornada por data; T24 CPC85 e T05 CE/DOU prosseguem em revisões autônomas.
- Alternância horizontal em T02/T43 após consolidação dos gates, sem sobreposição da reserva T13.

**Estado operacional:** FEITO +42 unidades documentais e 11 artigos, novo título T03, lacuna 11–16 T48 preenchida; PENDENTE DOU/competência; PRÓXIMO continuidade e revisão. **DEC-016 pendente, C0-J=0, M aprovada=0, revogações/merges=0.**
