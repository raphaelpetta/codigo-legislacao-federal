# CLF — Rodada 20: acesso à informação, inovação, segurança pública e instrumentos consumeristas

**Corte:** 15/10/2026. **PR [#67 draft](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/67)**, empilhado sobre o [#64 draft](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/64), sem merge. [Central permanente #48](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/48). **Todos os textos são Q, experimentais e não homologados.**

## FEITO — três novos títulos de áreas distintas

**T10 — Transparência e integridade administrativa.** [LAI arts. 1º–3º](../produto/vistas/T10_LAI_ART1_3_PREVIA_Q.md), [espelho](../modulos/T10/M01_ESPELHO_LAI_ART1_3_12_Q.csv), [manifesto](../produto/fontes/T10_M01_LAI_12_R20_v1.json): **3 artigos/12 unidades Q**, blob `cba21fca81f3b8e72d19e9ee973c53cf4271445f`. Fonte [Câmara LAI atualizada](https://www2.camara.leg.br/legin/fed/lei/2011/lei-12527-18-novembro-2011-611802-normaatualizada-pl.html) e Planalto. Incidência federal/estadual/distrital/municipal, órgãos dos Poderes/MP e entidades controladas, transparência de recursos públicos recebidos por entidades privadas sem fins lucrativos e publicidade regra/sigilo exceção. Não generalizar esse comando como liberação de dados pessoais protegidos por LGPD T43 ou restrições específicas.

**T35 — Ciência, pesquisa e inovação.** [Lei 10.973/2004, art. 1º](../produto/vistas/T35_INOVACAO_LEI10973_ART1_PREVIA_Q.md), [espelho](../modulos/T35/M01_ESPELHO_INOVACAO_ART1_16_Q.csv), [manifesto](../produto/fontes/T35_M01_INOV_16_R20_v1.json): **1 artigo/16 unidades Q**, SHA `9930e68f301a245fcc33b57895ec56622bbb6da5`. Fonte [Câmara atualizada](https://www2.camara.leg.br/legin/fed/lei/2004/lei-10973-2-dezembro-2004-534975-normaatualizada-pl.html). Caput alterado e parágrafo único com **14 incisos acrescidos pela Lei 13.243/2016**. A redação de 2016 não deve ser confundida com 2004; **art. 2º definições não incluído**, nem poderes automáticos para contratar ou conceder benefícios. DOU e retificação 2005 pendentes.

**T45 — Segurança pública e inteligência.** [Lei 13.675/2018, Susp arts. 1º–3º](../produto/vistas/T45_SUSP_ART1_3_PREVIA_Q.md), [espelho](../modulos/T45/M01_ESPELHO_SUSP_ART1_3_3_Q.csv), [manifesto](../produto/fontes/T45_M01_SUSP_3_R20_v1.json): **3 artigos/3 unidades Q**, SHA `fc806c7adb9aa48c9bab770fd827c1c5d25d9910`. Fonte [Câmara SUSP atualizada](https://www2.camara.leg.br/legin/fed/lei/2018/lei-13675-11-junho-2018-786843-normaatualizada-pl.html). Integração sistêmica entre União/estados/DF/municípios e respectiva competência para políticas, **sem criar competência policial por compilação**. Princípios de direitos fundamentais e limitação do uso da força do art. 4º, inclusive alteração de 2023, ficam como gate fora do recorte.

## FEITO — expansão vertical alternada

**T20 — CDC art. 5º**, [vista](../produto/vistas/T20_CDC_ART5_PREVIA_Q.md), [espelho 8×8](../modulos/T20/M01_ESPELHO_CDC_ART5_8_Q.csv) e [manifesto](../produto/fontes/T20_M01_CDC_8_R20_v1.json): **1 artigo/8 unidades Q**, blob `a28bd24a188d2ac92473ad8c18e25bb6e17032cf`. Fonte [Câmara CDC atualizada](https://www2.camara.leg.br/legin/fed/lei/1990/lei-8078-11-setembro-1990-365086-normaatualizada-pl.html). Sete instrumentos da política, incisos VI/VII da Lei 14.181/2021. **§§ 1º e 2º vetados, não contados como positivos**. Total T20 **arts. 1º–5º, 5 artigos/29 unidades Q**.

## FEITO — consolidação transversal

- [Código único Q](../produto/CODIGO_DE_TRABALHO.md), [índice](../produto/fontes/indice_livros.json), [matriz dos 48 títulos](01_MATRIZ_AUDITORIA_48_TITULOS_20261015.csv), [painel](PAINEL_GERADO.csv), [quadro](QUADRO_PRODUTO.csv), [guia](../produto/00_LEIA_O_CODIGO.md) e [fila de 61 tarefas](FILA_TRABALHO.csv) atualizados: **266 artigos de origem/895 unidades textuais positivas +1 histórico T07 =896 registros documentais**, **44 componentes em 29 de 48 títulos**, **19 títulos ainda sem texto**.
- **+8 artigos, +39 unidades positivas, +3 títulos novos**. Arquivos Q não produzem ratificação jurídica, revogação ou nova espécie normativa.
- Adicionado [verificador R20](../scripts/validar_r20_horizontal.py) e [workflow de diagnóstico de runner](../.github/workflows/clf-r20-diagnostico-runner.yml), distinguindo job mínimo `runner-smoke` sem checkout do job `corpus-r20` que roda Python sobre a branch. O objetivo é isolar falha de infraestrutura e falha de script, **não declarar aprovação antes do GitHub informar conclusões**.

### Resultado efetivamente consultado do diagnóstico R20

No PR #67, [workflow `CLF R20 - Diagnostico do runner e QA`, run **38799728643**](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38799728643), os dois jobs foram concluídos com **`failure`**:

- `runner-smoke` (job **116645313161**): **failure**, sem checkout e sem execução de verificador do corpus;
- `corpus-r20` (job **116645312795**): **failure**, configurado para checkout e validação documental.

Para ambos, `fetch_workflow_job_steps` retornou **lista vazia** e a solicitação de logs retornou **404 BlobNotFound**. A falha do job que nem realiza checkout mostra que os scripts documentais novos **não explicam, sozinhos, todas as falhas de CI**, mas **não identifica causa** (runner, política de Actions, restrição da instalação, configurações e outros mecanismos permanecem hipóteses a apurar). Assim, o CI R20 permanece **REPROVADO/P0 BLOQUEANTE**, sem atestado de execução positiva de Python, e o projeto não está pronto para merge.

**QA documental remoto distinto do CI:** leitura via conector GitHub confirmou as **44 vistas alinhadas ao Código**, 266 cabeçalhos, 4 SHA/manifestos novos, 48 linhas da matriz/29 preenchidas, 266 artigos e 895 positivas, 61 tarefas com IDs únicos e T13 preservado. Esses controles não substituem cotejo DOU nem a execução de CI.

## PENDENTE — bloqueio de CI P0 e efeito jurídico

Os três workflows legados estrutura/T07/T24 e o R19 autossuficiente tiveram conclusão `failure` no PR #64; [relatório anterior](27_RODADA19_BENS_CPP_CTB_CDC_CI_20261015.md). O conector devolveu **404 BlobNotFound** ao solicitar logs de jobs, o que impediu atribuição causal. O workflow R20 com dois jobs foi criado para produzir evidência adicional, sem presumir a causa. Tarefas P0 `CLF-TRANSVERSAL-006`, `007` e `008` permanecem abertas; **não mesclar PRs com CI reprovação**.

DOU original/alteradoras, correção de retificações e vetos, competência, relações entre LAI e LGPD, Lei 13.243/2016 e inovação, Susp e art. 144 CF, superendividamento e requisitos especiais continuam pendentes. **C0-J=0, M aprovada=0, DEC-016 pendente; revogação, renumeração definitiva e merge=0.** A reserva T13 não foi alterada.

## PRÓXIMO

1. Verificar separadamente conclusões dos jobs `runner-smoke` e `corpus-r20`, registrar diagnósticos e corrigir somente causa demonstrada. Caso logs sigam inacessíveis, declarar limitação e manter gate.
2. Abrir títulos restantes por áreas diferentes, equilibrando horizontal, vertical e autenticidade, sem confundir contagem de títulos com fração do direito brasileiro coberta.
3. Programar cotejo de fontes DOU e efeitos temporais, e só então submeter equivalências C0-J para deliberação jurídica expressa.

**Estado final R20: entrega real em PR draft, QA documental sob verificação, CI P0 bloqueante, nenhuma homologação.**
