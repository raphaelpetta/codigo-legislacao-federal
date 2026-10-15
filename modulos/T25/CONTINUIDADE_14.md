# Continuidade T25.M03 — ciclo 14

**Corte:** 15/10/2026. **Issue #31; [PR #32 (draft)](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/32)**, branch `modulo/T25-parte-geral-f0-f1`. **Baseline main CLF:** `16fba172c875c7a0de388288fe70005c944021d6`. **Main do projeto constitucional (apenas controle, não direito vigente):** `2a770a8136f8ca4877e865be3e3b7745a6d4b168`. SHA ciclo13: `03c1fd11aaa69a55b11a9185fa12b03759bc3503`. Validar HEAD deste ciclo após gravação.

## FEITO, apenas em branch

| Arquivo | Entrega | Limite |
|---|---|---|
| `INVENTARIO_SURSIS_CP_CPM_LEP_CICLO14.csv` | 20 artigos: CP77–82 (6); CPM84–88 (5); LEP2 e 156–163 (9); **61 unidades descritivas** | Texto consolidado sem C0-J nem cotejo histórico integral |
| `MATRIZ_PORTAS_SURSIS_EXECUCAO_CICLO14.csv` | 30 relações de pena, substituição, sursis, revogação, execução, competência, ANPP/processo e temporalidade | Status Q; eventuais reformas M não ratificadas |
| `CASOS_PORTAS_EXECUCAO_CICLO14.csv` | 12 cenários didáticos com CP163/CPM187, 2022/2026, custódia ordinária e suspensão | Nenhuma sentença real ou concessão automática |
| `JURISPRUDENCIA_E_ANPP_SURSIS_CICLO14.csv` | 6 referências STM, STF e STJ, inclusive ANPP 2024/2025 e PSV149 2026 | Distinguir decisão, notícia, ata e proposta |
| `DOSSIE_14_SURSIS_PROCESSO_EXECUCAO.md` | Análise, fluxograma, problemas PROB-T25-0053–0062 | Pesquisa F1–F4, não minuta ratificada |
| `README.md` e este documento | Governança e índice | Sem integração à main |

**Fontes lidas 15/10/2026:** [CP atualizado](https://www2.camara.leg.br/legin/fed/declei/1940-1949/decreto-lei-2848-7-dezembro-1940-412868-normaatualizada-pe.html), [CPM atualizado](https://www2.camara.leg.br/legin/fed/declei/1960-1969/decreto-lei-1001-21-outubro-1969-376258-normaatualizada-pe.html), [LEP atualizada](https://www2.camara.leg.br/legin/fed/lei/1980-1987/lei-7210-11-julho-1984-356938-normaatualizada-pl.html). Ver dossiê e matriz judicial para precedentes e seus limites.

## ACHADOS PRESERVÁVEIS

1. **Sursis da pena CP77/CPM84, suspensão do processo Lei9099 art89 e ANPP CPP28-A são institutos distintos.** STJ 2024 aplica art90-A para impedir suspensão de processo no militar; STF 2024 e STJ 2025 admitem possibilidade de ANPP militar sob requisitos. **PSV149:** consulta pública STF em 27/08/2026, não súmula aprovada (andamento posterior não aferido).
2. **CPM84** diferencia prova reclusão **3–5** e detenção **2–4** anos; §2 desde 2023 admite pena até 4 anos e prova 4–6 para >70 anos ou saúde, **sem afastar CPM88**. CP77 não diferencia reclusão/detenção no prazo ordinário 2–4.
3. **CPM88 II a** exclui sursis de deserção CPM187. Se militar com pena privativa até dois anos e sursis incabível, CPM59 trata conversão em **prisão militar**, não substituição CP44 por restritiva. Evitar prometer ANPP para deserção sem teste específico.
4. **CPM86 §1** autoriza revogação FACULTATIVA em punição disciplinar militar grave desde 2023; o gatilho não equivale ao CP81. CPM86 III foi revogado em 2023 e não pode ressurgir.
5. **LEP2 parágrafo único:** a lei incide sobre condenados pela Justiça Militar quando recolhidos em estabelecimento sujeito à jurisdição ordinária. A LEP não se aplica automaticamente a qualquer estabelecimento militar, sem prejuízo de direitos constitucionais. Rito LEP156–163 não substitui automaticamente CPPM.
6. **Artigos de regulação de condições, prazo inicial e execução** têm efeitos materiais/temporais que precisam matriz de competências T26/T27 antes da codificação.

## PENDENTE / NÃO VERIFICADO

- C0-J da área ausente e C0-T não realizado para esses artigos; textos originais e retificações 1984/2023 não inspecionados em arquivo DOU. DEC-016 e arquitetura A2/B2 não ratificadas.
- CPPM, execução e fiscalização de sursis militar, jurisdição em cumprimento em estabelecimento civil/militar, audiência e termo inicial; distinção entre material, processual e execução.
- Estudo constitucional específico da vedação de sursis CPM88, condições de revogação, contraditório e decisões judiciais detalhadas.
- Estado posterior da consulta PSV149 sem verificação de aprovação; não afirmar súmula vigente.
- CI estrutural do SHA final a conferir e comentar PR #32.
- Sem merge, revogação, escolha de M ou importação de Constituição projetada.

## PRÓXIMO — ciclo 15

**T25.M03/T27/T26:** mapear CPPM e LEP para um fluxo controlado da sentença até a extinção: **condições → autoridade de execução → estabelecimento → audiência/termo inicial → fiscalização → revogação/prorrogação → extinção**, distinguindo militar e civil condenado pela Justiça Militar. Testar transferência para estabelecimento ordinário, sursis já concedido, medida disciplinar grave, benefícios no tempo (2022/2026) e o que decorre expressamente da LEP2 parágrafo único. Criar matriz com fonte, data e categoria Q/M para cada porta; sem simular automaticamente jurisprudência.

**Interfaces:** T01/T02/T16, T25.M02/M03, T26/T27, T45, T23/T47. **Protocolo:** `governanca/18_PROTOCOLO_CONTINUIDADE_POR_RODADA.md`.
