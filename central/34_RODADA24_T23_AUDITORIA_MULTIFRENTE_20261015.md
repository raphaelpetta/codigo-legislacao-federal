# CLF R24 — LINDB T23 e auditoria de alto ganho marginal (15/10/2026)

**Base:** PR #70 draft, HEAD 5c96984dd0058e3d40bc743cd2dfd087fe13cee3. Main não alterada, sem homologação, DEC-016 pendente.

## FEITO

- **T23 novo:** [LINDB arts. 8º–9º](../produto/vistas/T23_LINDB_DIREITO_INTERNACIONAL_PRIVADO_ART8_9_PREVIA_Q.md), 2 artigos/6 unidades Q com [espelho](../modulos/T23/M01_ESPELHO_LINDB_ART8_9_6_Q.csv) e [manifesto SHA](../produto/fontes/T23_M01_LINDB_DIP_6_R24_v1.json), divergência de grafias Câmara/Planalto documentada e DOU ainda pendente.
- **Auditoria por efeito:** [12 controles](32_R24_AUDITORIA_EFEITO_PROVENIENCIA_MULTIFRENTE.csv) e [nota jurídica](33_R24_NOTA_CRITICA_LINDB_T29_T06_T16_ECA.md) sobre T06 STF ADI1127, T29 fonte correta e art9§1, T32 ECA art4 atualizado em 2026 fora do recorte, T16 CC188/927–930, T10 LAI6, T23 DIP, CI e DEC-016. Nenhum C0-J.
- **Código experimental único:** **55 componentes em 37 de 48 títulos, 294 artigos, 985 unidades positivas + 1 histórica T07 = 986 registros**; +2 artigos/+6 unidades/+1 título. Restam 11 títulos sem texto. Índice, Código, matriz e painel 48, quadro, guia e fila com 74 tarefas únicas recompostos. Reserva T13 intacta.
- **QA criado:** `scripts/validar_r24_t23_e_auditoria.py` no roteiro offline. Não declarar execução local/Actions sem logs e conclusão.

## PENDENTE

- CI P0 [#66](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/66): erro antes dos steps inclusive runner-smoke sem checkout, checks com anotações inacessíveis pela conexão. Não supor causa ou alterar workflows sem diagnóstico.
- DOU fac-símile, alterações, decisões integrais, especialidades e fase de fechamento da pilha de PRs. R3 T07/T24/T25 permanecem prioritárias.
- **C0-J=0, M=0, DEC-016 pendente, sem revogação, renumeração definitiva ou merge**.

**PRÓXIMO:** obter mensagem literal do runner, aprofundar auditoria R3 e fechar pilha draft por dependência, sem sacrificar qualidade por métrica de títulos.

## Verificações remotas após abertura do PR #71 (R24)

- **Reconstrução por releitura independente:** 55/55 vistas correspondem exatamente aos respectivos blocos do `produto/CODIGO_DE_TRABALHO.md` (última vista com normalização apenas de quebras de linha finais), com **294 cabeçalhos**. Índice: 55 componentes, 37 títulos, 294 artigos e 986 registros (985 positivos +1 histórico).
- **Quadros:** as **48 linhas da matriz** coincidem com artigos/unidades do índice, reservando T07 histórico fora dos positivos; C0-J=0 em todas as linhas. **Painel:** 48/48 linhas correspondem a componentes/artigos/registros de origem. **Fila:** 74 tarefas e 74 IDs únicos. Reserva T13 sem texto. Manifesto T23 confere exatamente com Git blob SHA `89bd2cd56d6d71ab8f533e247545d333cb01884b`; seis unidades Q e dois artigos.
- **CI no HEAD `9946760965835dbd76eca61716d396c348d3d5a7`:** cinco runs `completed/failure`: [estrutura 38837908553](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38837908553), [T07 38837908531](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38837908531), [R19 38837908487](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38837908487), [diagnóstico 38837908495](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38837908495) e [T24 38837908532](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38837908532). **Seis check-runs com `failure` e duas anotações cada**. No diagnóstico, `runner-smoke` **sem checkout** e `corpus-r20` **com checkout** concluíram failure/**zero steps**. Não se obteve a mensagem concreta das anotações; **causa indeterminada, CI ainda não aprovado**.
- QA por leitura GitHub **não equivale** à execução do verificador Python R24, a cotejo DOU, a validade jurídica C0-J ou aprovação normativa.

## Incidente estrutural de QA local — correção executiva R24

A leitura do roteiro `scripts/validar_operacao_local.sh` demonstrou **incompatibilidade entre snapshots**: ele executava no mesmo HEAD os verificadores antigos com asserts exatos para 48 (R21), 51 (R22) e 54 (R23) componentes, enquanto o índice R24 contém **55**. Assim, haveria reprovação lógica mesmo que o corpus estivesse consistente. Em R24, o despacho foi refeito: se o manifesto R24 está presente, executa verificações gerais, o **validador genérico do índice atual** `scripts/validar_corpus_ativo.py`, o verificador R24 e a reconstrução canônica. Os scripts históricos continuam preservados para execução nos checkouts de suas rodadas; não foram adulterados para aceitar automaticamente aumentos de corpus. As portas setoriais T07/T24/T25 permanecem exigidas no SHA de origem, e a ausência de checkouts retorna `PARCIAL`/exit 2, não falso CI verde.

O novo genérico avalia todas as **55** vistas/manifestos, hashes Git das fontes que estão presentes na branch e sinaliza separadamente fontes setoriais externas sem inventar acesso. **Não houve execução local Python comprovada** desta alteração nesta rodada; é uma correção lógica do roteiro, sujeita a confirmação executável quando os runners permitirem.
