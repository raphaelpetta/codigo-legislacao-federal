# T24.M01 — Pacote de continuidade da rodada 05 (F1-C2)

**Data/corte:** 14/10/2026 · **Frente:** T24.M01 · **Issue:** [#37](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/37) · **PR:** [#38 — draft](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/38).  
**CLF main observada na abertura:** `16fba172c875c7a0de388288fe70005c944021d6`; branch `modulo/T24-M01-jurisdicao-sujeitos-f0-f1-20261014`. **CF proposta:** não reconsultada; não importar hipóteses como CF/1988 vigente.  
**Objeto:** segunda etapa de F1-C, transcrição manual de pares originais/atuais para CPC arts. 70–81 e 98–102, cruzamento com a edição compilada do Planalto e atos modificadores.

## FEITO

| Entrega verificável | Arquivos e estado | Prova e significado |
|---|---|---|
| Espelho textual de **106 unidades em 17 artigos**, com 102 coincidentes na comparação manual, **1 alteração, 2 acréscimos** e **1 divergência editorial** | [F1C2_ESPELHO_UNIFICADO_106.csv](F1C2_ESPELHO_UNIFICADO_106.csv); 5 arquivos de origem parcial; branch do PR | Leitura direta das edições Câmara 2015/2026, com transcrição manual e controles de IDs; **não é transposição C0 certificada** |
| Cotejo intertemporal de CPC 75 III/§5º e 77 VII | [Relatório F1-C2](RELATORIO_F1C2_ESPELHO_106_E_DIVERGENCIA.md) | Leis 14.341/2022 e 14.195/2021, com textos, datas, reservas e efeitos a investigar |
| Divergência editorial **77 VI: ponto-final original/Planalto compilado versus ponto e vírgula Câmara atualizada** | Relatório e espelho da unidade | Lei 14.195/2021 acrescenta VII sem alterar expressamente VI. Classificação Q, **não** alteração legal comprovada |
| Teste programático de integridade realizado durante produção | Resultado no histórico da rodada; [verificador versionado](verificar_espelho_f1c2.py) | 106 IDs de origem únicos, nenhum ausente em relação à F1-C; distribuição 102/1/2/1. Teste apenas estrutural, não jurídico |
| Cruzamento prévio das 26 prioridades com 49 vinculações da matriz de 106 preservado | [Reconciliação](F1C_RECONCILIACAO_26_PARA_106.csv) | Sem destruição dos documentos concorrentes e sem decisões arquiteturais silenciosas |

**Fontes efetivamente examinadas em 14/10/2026:** publicação original e texto atualizado do CPC da Câmara, arts. 70–81/98–102; Planalto CPC compilado, especialmente 75/77; Planalto Lei 14.341/2022 arts. 12–15; Planalto Lei 14.195/2021 art. 44 e alterações correlatas em 246. URLs e limites da leitura estão no relatório.

## PENDENTE / NÃO VERIFICADO

1. **Certificação independente** dos pares textuais: não foi possível capturar HTML bruto e produzir diff entre arquivos originais, hashes de exemplares oficiais e cadeia histórica completa das leis; os 102 enunciados iguais são **comparação/transcrição manual**. Validar por segunda leitura/DOU antes de classificar C0/C1 ou afirmar cobertura jurídica completa.
2. Solucionar **Q da pontuação do CPC 77 VI** com publicação autêntica da lei-base e ato modificador, distinguindo alteração editorial de inovação.
3. Considerar jurisprudência e normas materiais externas, especialmente LBI arts. 84–85, STJ Tema 1178/Súmula 481 e precedentes sobre curadoria/saneamento, já registrados em relatórios anteriores; identidade textual não equivale à identidade da norma jurídica aplicada.
4. Definir localização primária de deveres, representação, sanções e gratuidade em T24.M01/T24.M02/T24.M04/T06/T13/T32. Não transpor/revogar.
5. Verificar CI e controles no último SHA do PR; nenhuma reforma ratificada, módulo global permanece `PLANEJADO` (F1 parcial), embora recorte documental F1-C2 tenha avançado.
6. Não foram examinados nesta rodada os arts. 82–97 ou 103–187, nem microssistemas processuais, legislação estadual de custas ou conteúdo atual da CF futura.

## PRÓXIMO — prioridade única

**T24.M01 / F1-D:** inventário normativo e auditoria inicial dos **CPC arts. 82–97 — custas, honorários advocatícios, sanções e perícias**, vinculando-os às regras de gratuidade e à disciplina geral da parte sucumbente.

**Critério de aceite:** todas as subunidades desses 16 artigos mapeadas com proveniência, cadeia de alterações, jurisprudência qualificada pertinente, questões Q e destino provisório; custos estaduais e atos infralegais somente como camadas externas. **Paralelamente no controle de qualidade**, revisão independente dos 106 pares F1-C2/DOU antes de qualquer C0, sem bloquear a pesquisa F1-D.

**Fila:** arts. 103–118 (advocacia, sucessão e litisconsórcio), 119–187 e microssistemas, F2 reconstrução completa e reforma fundamentada.

## COORDENAÇÃO / CONTROLES

- **Dono funcional:** T24.M01. Interfaces T01/DEC-016, T03/T06, T13/T14/T17/T32, T24.M02/M04/M05 e T43.
- **CF/1988** como direito positivo; anteprojeto constitucional como cenário condicional externo, não reconsultado.
- **C0/C1/M:** nenhuma categoria de redação CLF aprovada ou incorporada; apenas comparação de fontes do CPC vigente. **Q:** divergência documental do art. 77 VI e os efeitos jurídico-semânticos/intertemporais.
- **Main/PR:** alterações exclusivamente no PR #38 (draft), sem merge ou decisão de governança material.
- **CI:** conferir status no SHA final, não presumir sucesso pelo resultado de uma verificação JS local.

- [x] Conferida main e PRs na abertura.
- [x] Preservados arquivos concorrentes, sem duplicar destinos normativos.
- [x] Documentados fontes, resultados, ressalvas e FEITO/PENDENTE/PRÓXIMO.
- [x] Validação interna estrutural executada.
- [ ] Cotejo autêntico automatizado/segunda revisão independente.
- [ ] CI confirmada e decisões jurídicas de integração tomadas.
