# CLF — plano de integração de governança, corpus e frentes
**Corte:** 15/10/2026. Protocolo operacional em PR, sem aprovação legislativa. [Central #48](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/48).

## Fontes de autoridade e reconciliação
- **#46:** método amplo (F0–F7, progresso por camadas, proteção de efeitos C0-T/C0-J/C1/M/Q, DEC-016 e decisões). **#49:** executor da central, fila, compilador, índice de Livros e visualizações experimentais. Ambos são draft; conciliá-los antes de merge, sem substituir silenciosamente decisões e instruções prévias.
- **#45:** fonte setorial T07 (SHA registrado em produto/fontes/T07_M03_v4.json). A vista na central #49 só é válida para aquela versão e deve ser regenerável e comparada com a origem.
- **#38:** fonte setorial do recorte T24 CPC 70–81/98–102 (SHA no manifesto T24_M01_106_v1.json). O Código inclui uma prévia PARCIAL, jamais representa transposição integral do CPC.
- **#50:** levantamento de fontes-âncora dos 48 títulos (candidaturas não equivalem a levantamento exaustivo ou texto normativo integrado).
- **#47 e #43:** interface T07–T43 e pesquisas de governo digital. Exigem coordenação com CF M07, sem importar hipóteses constitucionais como vigente.
- **#51:** frente T01.M06 relativa a regulamentação infralegal; manter como pesquisa setorial, sem transformar atos infralegais em texto de lei por mera compilação.

## Portas de integração materialmente distintas
1. Pesquisa e hipótese mantidas em PR, com fonte/data, correspondência e riscos.
2. **Integração experimental** após revisão aplicável: índice de Livros e vista são atualizados com estado Q/H, nunca como direito vigente ou C0-J certificado. São permitidos Livros parciais com lacunas explícitas.
3. **Ratificação material e promulgação** são atos independentes, que não decorrem do merge. DEC-016 continua pendente.

## Grafo de dependência para o corpus
```text
PR #45 T07 (origem SHA) ──> manifesto T07 ──> prévia T07 ──┐
                                                        ├──> indice_livros.json ──> CODIGO_DE_TRABALHO.md
PR #38 T24 (origem SHA) ──> manifesto T24 ──> prévia T24 ──┘
PR #46 governança ── revisão cruzada com #49
PR #50 fontes-âncora ── inventário temático (fora do texto até transposição controlada)
```

**Gates técnicos:** conferir blob Git e commit da fonte; conferir concordância origem–destino, estado jurídico Q, unidades e texto; regenerar vista e Código; atualizar painel; executar validadores de fato. O CI de Actions falhou antes das etapas em execuções verificadas — não declarar aprovação técnica inexistente.

## Regras para retomada e próximas entregas
- A fila `central/FILA_TRABALHO.csv` distingue PRONTA, EM_REVISAO e outras etapas. PR #49 já inclui T24 e T13 em diferentes graus de cobertura. Não repetir a redação setorial, nem promover T13 a Livro sem texto e concordância suficientes.
- A integração de T24 no Código é **somente do recorte parcial explicitamente identificado**: 17 artigos, 106 subunidades Q; não equivale a aprovação, nem a CPC completo.
- O próximo Livro novo deve ser escolhido por universo e pesquisa efetiva (T25/T29/T43/T05 ou outro título atrasado), mantendo o conjunto de 48 títulos em vista, e não necessariamente voltando a T07.
- Depois de cada merge de fonte, conferir se `origem_commit` do manifesto ainda corresponde à versão pretendida. Atualizar o snapshot apenas se a mudança for deliberada e reproduzível.

## Critério de conclusão desta conciliação
Um protocolo executivo vigente por projeto, sem duplicação de autoridade. O PR #46 pode incorporar regras gerais revisadas; #49 concentra executor e produto. Qualquer mudança de roteiro material é variante/proposta, nunca decisão D ou M automática.
