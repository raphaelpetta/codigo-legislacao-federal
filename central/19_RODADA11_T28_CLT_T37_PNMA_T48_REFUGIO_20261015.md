# Central CLF — Rodada 11: núcleo laboral T28, definições ambientais T37 e rito de refúgio T48

**Corte:** 15/10/2026 (Brasil, -03). **Entrega:** [PR #56 draft](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/56), derivado do HEAD do PR #55 (draft), cadeia de trabalho `#49 → #53 → #54 → #55 → #56`; `main` preservada. [Central de comando #48](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/48).

## FEITO — expansão real de cobertura documental

### T28.M01 — primeiro recorte textual laboral

- [CLT (anexo do Decreto-Lei 5.452/1943), arts. 1º–3º: **3 artigos e 7 unidades Q**](../produto/vistas/T28_CLT_ART1_3_PREVIA_Q.md), [espelho 7 origens/7 destinos](../modulos/T28/M01_ESPELHO_CLT_ART1_3_7_Q.csv), [manifesto de origem imutável](../produto/fontes/T28_M01_CLT_7_R11_v1.json) e fonte institucional [Câmara, CLT atualizada](https://www2.camara.leg.br/legin/fed/declei/1940-1949/decreto-lei-5452-1-maio-1943-415500-normaatualizada-pe.html), cotejo [Planalto](https://www.planalto.gov.br/ccivil_03/decreto-lei/del5452.htm); Git blob fonte `6439a139cacdd3c7fca3202963c8cfcc2dcf188c`.
- **Precisão de objeto:** artigos da CLT são diferentes dos artigos 1º–3º do Decreto-Lei 5.452/1943 que **aprova** a CLT. O art. 2º §§2º e 3º integra a reforma da Lei 13.467/2017; comprovar a vigência na cronologia de 2017 antes de C0-T definitivo. Empresa, grupo econômico, dependência, não eventualidade e salário requerem gates próprios.
- **PEC 221/2019 escala 6×1:** [Senado 14/10/2026, aprovação **em dois turnos**](https://www12.senado.leg.br/institucional/presidencia/destaque-noticia/sob-a-presidencia-de-davi-alcolumbre-senado-aprova-a-pec-do-fim-da-escala-6x1); [Rádio Senado](https://www12.senado.leg.br/radio/1/noticia/2026/10/14/senado-aprova-pec-que-acaba-com-escala-6x1-texto-segue-para-promulgacao); [Câmara 15/10/2026](https://www.camara.leg.br/noticias/1311348-hugo-motta-comemora-aprovacao-do-fim-da-escala-6x1-no-senado). Fontes oficiais indicam **encaminhamento à promulgação** e não documentam promulgação/publicação final até o corte. **Não importar 42/40 horas ou duas folgas como norma vigente**. O [PL 1.838/2026](https://www.camara.leg.br/proposicoesWeb/fichadetramitacao?idProposicao=2616127) também continua sendo projeto no recorte verificado, não lei integrada à CLT.

### T37.M01 — conceitos e objetivos da Política Nacional do Meio Ambiente

- [Lei 6.938/1981, arts. 3º–4º, **2 artigos / 19 posições Q**](../produto/vistas/T37_PNMA_ART3_4_PREVIA_Q.md) com [fonte↔destino 19×19](../modulos/T37/M01_ESPELHO_PNMA_ART3_4_19_Q.csv), [manifesto](../produto/fontes/T37_M01_6938_19_R11_v1.json), fonte [Câmara atualizada](https://www2.camara.leg.br/legin/fed/lei/1980-1987/lei-6938-31-agosto-1981-366135-normaatualizada-pl.html) e controle Planalto; Git blob `e452c4aee3166b74853a6f5870295e9a7478d9d5`.
- Art. 3º III: **cinco alíneas a–e** subordinadas à definição de poluição, e não cinco tipos sancionadores independentes. Art. 3º IV: poluidor direto ou indireto, sujeito a prova e nexo no plano de responsabilidade; art. 3º V: redação de Lei 7.804/1989 para recursos ambientais. Art. 4º objetivos: compatibilização de desenvolvimento, padrões, pesquisa, recuperação, reparação e contribuição de usuários, preservando as competências constitucionais de União, estados, DF e municípios e LC 140/2011.
- T37 passa a **4 artigos / 32 unidades Q** junto com arts. 1º–2º e o inciso XI incluído pela Lei 15.512/2026 (vigente 23/09/2026). DOU original e alteradoras por fac-símile pendentes.

### T48.M03 — acesso, instrução e proteção procedimental

- [Lei 9.474/1997, arts. 17–21, **5 artigos / 8 unidades Q**](../produto/vistas/T48_REFUGIO_ART17_21_PREVIA_Q.md); [espelho 8×8](../modulos/T48/M03_ESPELHO_REFUGIO_ART17_21_8_Q.csv) e [manifesto](../produto/fontes/T48_M03_9474_8_R11_v1.json); fonte original [Câmara](https://www2.camara.leg.br/legin/fed/lei/1997/lei-9474-22-julho-1997-365390-publicacaooriginal-1-pl.html) e cotejo Planalto; Git blob `cafa2f66c34566adab89ef20ef380c96c0f47d0f`.
- **Preservado:** art.17 manifestação da vontade de solicitar refúgio; art.18 declarações e comunicação à ACNUR (parágrafo único); art.19 intérprete quando necessário, família e elementos de prova; art.20 **sigilo** dos registros; art.21 **protocolo de estada até decisão final**, acesso a documento de trabalho e registro de filhos menores de 14 anos.
- **Descontinuidade deliberada:** T48 alcança **15 artigos / 29 posições Q**, mas **arts. 11–16 NÃO foram incorporados** e **arts. 22–49 permanecem fora da vista**. Não afirmar processo completo ou automatizar decisões, devolução/exclusão; Lei 13.445/2017, Convenção 1951/Protocolo 1967, CONARE e normas de proteção de dados requerem exame específico.

## FEITO — produto único, fonte e verificabilidade

- [Índice de Livros](../produto/fontes/indice_livros.json) e [Código de Trabalho](../produto/CODIGO_DE_TRABALHO.md) atualizados **sem copiar novamente o texto-fonte em outro arquivo autoritativo**; [painel de 48 títulos](PAINEL_GERADO.csv), [quadro](QUADRO_PRODUTO.csv), [fila](FILA_TRABALHO.csv) e [guia](../produto/00_LEIA_O_CODIGO.md) harmonizados.
- **Corte R11: 160 artigos de origem / 532 unidades documentais positivas textuais + 1 registro histórico T07; 11 componentes / 7 títulos** (T05, T07, T24, T25, T28, T37, T48). T05 art.15 refere vigência histórica da lei original 1998 e já está dentre as 532 unidades documentais, não é comando de vigência futuro.
- [Verificador R11 de SHAs, cardinalidades e estados Q](../scripts/validar_r11_t28_t37_t48.py) integrado ao [roteiro de validação offline](../scripts/validar_operacao_local.sh). Inspeção GitHub da compilação confirma 160 cabeçalhos e montagem de 11 vistas; **isso não prova execução de Python/Actions nem equivalência jurídica**.
- Reserva concorrente T13 intocada; todos os originais textuais novos são **Q**, sem C0-J. Nenhuma hipótese de reforma constitucional CF foi importada como direito vigente.

## PENDENTE

1. DOU autenticado e retificações: CLT/Decreto-Lei 1943, Lei 13.467/2017, PNMA 1981, Lei 7.804/1989, refúgio 1997 e Lei 15.512/2026. O cotejo Câmara/Planalto não substitui fac-símile e versão oficial de cada evento normativo.
2. T28: acompanhar promulgação/publicação final, e efeitos temporais constitucionais da PEC 221/2019 **antes** de atualizar qualquer norma de jornada; CLT relação de emprego versus legislação especial, grupo econômico e jurisprudência.
3. T37: art. 6º SISNAMA após Lei 15.190/2025, competência LC140/2011, Lei 15.512/2026 ECA/PNMC, responsabilidade civil/administrativa/penal. T48: arts. 11–16, 22–32, proteção contra devolução, processo sigiloso, práticas normativas CONARE, protocolos.
4. Controle de CI GitHub Actions, efetiva execução Python e cadeia de PRs; nenhum merge automático.

## PRÓXIMO

1. Reconciliar recepção/vigência em T28 à medida que surja promulgação oficial, distinguindo PEC aprovada de emenda vigente e vacatio de efeitos.
2. Priorizar T48 proteção de refúgio em arts. 22–32 e interface Lei 13.445, sem assumir completude antes de cobrir arts. 11–16.
3. Avançar T37 art. 6º e mapa de competências sem confundir lei ordinária, LC 140/2011 e leis de entes subnacionais; abrir novo título horizontal T03 ou T02 quando houver fonte verificada e capacidade.
4. T24 CPC85 documentos DOU, precedentes e especialidade; T05 texto autêntico DOU.

**Estado formal:** C0-J=0; M aprovadas=0; DEC-016 pendente; revogações=0; merges=0. **FEITO:** 3 novos recortes literais Q e corpus ampliado. **PENDENTE:** autenticidade e equivalência jurídica. **PRÓXIMO:** vigência, procedimento e competência sem falsas homologações.
