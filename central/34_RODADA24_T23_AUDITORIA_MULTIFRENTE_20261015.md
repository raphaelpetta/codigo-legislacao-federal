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
