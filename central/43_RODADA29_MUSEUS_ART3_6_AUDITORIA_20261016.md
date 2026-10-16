# CLF R29 — 16/10/2026: Museu arts3–6, veto e QA vivo

**Base:** PR #78 draft, HEAD `50050494b57ef3f7da34832bdfbe012c05309060`. Nada em main ou C0-J homologada.

## FEITO
- T34 Lei11.904/2009 arts3º–6º, **4 artigos/11 positivas Q** com [vista](../produto/vistas/T34_MUSEUS_LEI11904_ART3_6_PREVIA_Q.md), [espelho](../modulos/T34/M01_ESPELHO_MUSEUS_LEI11904_ART3_6_11_Q.csv), [manifesto SHA](../produto/fontes/T34_M01_MUSEUS_11_R29_v1.json). T34 agora total 6 artigos/21 positivas.
- **Veto §3 art5** na [Câmara](https://www2.camara.leg.br/legin/fed/lei/2009/lei-11904-14-janeiro-2009-585365-normaatualizada-pl.html) conservado em nota e metadados, **não** entre unidades positivas, sem restaurar texto vetado ou contar como histórico T07.
- Gates de impacto [11 registros](42_R29_AUDITORIA_MUSEUS_VETO_E_TRANSICOES_20261016.csv): declaração de interesse público não desapropriação/tombamento; fomento não é despesa autorizada automaticamente; exclusão legal das bibliotecas, arquivos e coleções visitáveis; PNC 2010–2024 expirado sem revogar Museu; PL5894/2025 ainda proposição; Estatuto Cidade XXI eficaz em abril/2026 e XXII–XXIII/lei mobilidade com vigência diferida após 1 ano do DOU de 14/06/2026.
- **QA de cabeçalhos:** a primeira nota do veto usava marcador `**Art.` igual a cabeçalho positivo, gerando contagem falsa. Corrigida para `**Marcador vetado ...**` antes de integração. Novos validadores `scripts/validar_museus_ativos.py` e gates R29 no `validar_gates_ativos.py`; roteiro substitui o teste de snapshot R28 (T34 2/10) por verificador válido após T34 6/21.
- **Produto:** 59 componentes Q em 40/48 títulos, **305 artigos/1043 unidades positivas +1 histórica T07 (1044 registros)**; +4 artigos/+11 unidades, 0 títulos, oito títulos vazios, T13 reservado. Código, índice, painel/matriz 48, guia/quadro e fila **81 tarefas únicas**.

## PENDENTE
- DOU 2009, mensagem de veto, atos de interesse público, requisitos de fomento e jurisprudência com competências; jurisprudência e eficácia PNC/mobilidade. HTML Câmara/Planalto não significa cotejo fac-símile.
- CI [#66](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/66) continua pré-steps com smoke sem checkout falhando e anotações não acessíveis. **Nenhuma execução Python/CI verde comprovada**; QA documental remoto não resolve diagnóstico de runner.
- **C0-J=0, M=0, DEC-016 PENDENTE**, nenhuma revogação, renumeração definitiva, positivação ou merge.

**Próximo:** recuperar anotações causais GitHub autenticado, execução de QA nos checkouts, auditoria DOU e dos efeitos prioritários antes de novo avanço horizontal ou vertical.

## QA remoto pós-abertura do PR #79 — evidência real

- Base R28: Git tree com **444 entradas**, R29: **450 entradas** (ambas `truncated=false`). **58/58 vistas e manifestos anteriores preservados com Git blob SHA idêntico**; a nova vista e manifesto T34 encontrados no HEAD. Nenhuma substituição de componente anterior.
- T34 novo: fonte CSV de 11 unidades, SHA `cff3c898e56d7db1daacbd6ba959043a72437fdb` conferido com manifesto; 4 cabeçalhos `**Art.` e integração integral no `CODIGO_DE_TRABALHO.md`. O primeiro cabeçalho editorial da nota de veto foi corrigido para **Marcador vetado** antes da composição — o §3º do art5 não virou quinto artigo nem unidade positiva. **Corpus: 59 componentes/40 títulos, 305 artigos/1043 positivas +1 histórico T07 =1044 registros**.
- **Matriz e painel 48/48**: leitura independente de cada linha confirmou quantidade de componentes, artigos, unidades (descontando histórico T07 no campo positivo da matriz) e C0-J=0. **Fila 81/81 IDs distintos; matriz R29 11/11 IDs**; T13 intacto. Roteiro local atualizado para validador T34 ativo em lugar do snapshot R28 com T34 fixo 2/10.
- **CI em commit de abertura `bc9d79e6650876fdceaa5b38b509ebdcf35e31df`**: cinco runs `completed/failure`, entre eles [diagnóstico 38854429921](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38854429921). `runner-smoke` **sem checkout**, job `116822606498`, e `corpus-r20` **com checkout**, job `116822606887`, falharam com **zero steps**. Seis check-runs exibem `annotations_count=2`, mas a API de leitura das mensagens não é autorizada ao conector. Não foi possível demonstrar a causa da falha nem executar Python em CI.
- **Limites:** hashes e controles por árvore comprovam consistência documental, **não** cotejo de fac-símile DOU ou validação de mérito jurídico C0-J. Validador Python R29 foi incluído, não executado de forma comprovada nesta rodada.
