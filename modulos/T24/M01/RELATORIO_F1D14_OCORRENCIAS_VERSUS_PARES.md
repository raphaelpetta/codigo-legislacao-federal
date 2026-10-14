# T24.M01 — F1-D14: ocorrências textuais ≠ pares de remissão do CPC art. 85
**Corte:** 14/10/2026; [PR #38](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/38) draft. **Esta etapa não homologa C0-J, não exaure todas as dependências e não atribui numeração legislativa ao CLF.**

## FEITO — inventário de citações efetivamente existentes
O [extrator `scripts/inventariar_f1d14_ocorrencias.py`](../../../scripts/inventariar_f1d14_ocorrencias.py) reutiliza o espelho oficial artigo-local do [CPC art.85](https://www2.camara.leg.br/legin/fed/lei/2015/lei-13105-16-marco-2015-780273-normaatualizada-pl.html), separa as **36 subunidades** e procura expressões literais como `§`, `§§`, `art.`, `incisos` e `caput`, removendo apenas o marcador inicial da própria subunidade para não contá-lo como autorreferência.

**Resultado comprovado:** [CI #38586997870 aprovada](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38586997870), [artefato CSV + JSON com offsets, contexto e hash de origem](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38586997870/artifacts/11906301984):
- **19 ocorrências lexicais**, não 19 destinos e não 19 regras jurídicas. Uma única expressão plural pode apontar a vários parágrafos.
- **45 pares de dependência** do grafo F1-D13 (35 anteriores + 10 contextuais), que não coincidem numericamente com as 19 expressões.
- **§11:** dois trechos distintos — `§§ 2º a 6º` e `§§ 2º e 3º`. A primeira ocorrência identifica cinco destinos; a segunda volta a citar dois deles para o controle dos limites. Remover a segunda por suposta redundância perderia informação sobre o teto.
- **§20:** uma expressão plural com **dez destinos individualizados**. A ocorrência lexical não deve ser substituída por uma única aresta ao `caput` ou por `aplica-se no que couber`.

## Distinguir três coisas diferentes
| Camada | Objeto | Unidade |
|---|---|---|
| Texto-fonte | Ocorrência escrita em uma subunidade | expressão com offset e contexto |
| Concordância interpretativa | Destino ou destinos jurídicos de uma expressão | pares origem→destino, com classificação literal/contextual |
| Texto do futuro CLF | Remissão após escolha de Livro/espécie/competência | **não existe numeração autorizada**; DEC-016 não resolvido |

**Risco controlado:** nos incisos I/II do §4º, a referência a cinco faixas é interpretada à luz do caput, que remete ao §3º. Esses dez pares **não são dez menções literais completas ao §3º**. O inventário lexical usa expressões regulares, portanto pode deixar de capturar referências sem o gatilho pesquisado (`deste artigo`, locuções anafóricas, regras gerais externas); **não se declara exaustividade**. Também não há cotejo humano independente de cada ocorrência.

## Próxima porta
**FEITO:** separação reexecutável de ocorrências de pares, detecção de duas expressões do §11 e da enumeração do §20, 36 fontes por unidade e execução aprovada. **PENDENTE:** auditoria independente de linguagem natural para `deste artigo`, `deste Código`, referência a sanções, situação jurídica de CPC art77 e normas conexas, cadeia DOU/Lei14.365/2022, STF Tema1255, decisão DEC-016 e C0-J. **PRÓXIMO:** construir concordância `ID_OCORRÊNCIA → ID_ORIGEM → ALVOS` sem perder repetição, testar cada ocorrência com o texto integral e só então propor substituição de remissões jurídicas.
