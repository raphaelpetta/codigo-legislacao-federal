# CLF — fotografia de integração e decisões pendentes

**Corte:** 14/10/2026. **Estado:** pesquisa e coordenação, não reforma jurídica aprovada. **Base main CLF:** 16fba172c875c7a0de388288fe70005c944021d6. **Base CF consultada:** 2a770a8136f8ca4877e865be3e3b7745a6d4b168. **Não substitui** os READMEs/handoffs das frentes: conferir novo HEAD antes do merge.

## 1. Onde realmente estamos

O projeto tem 8 partes, 48 títulos, 273 módulos candidatos e 34 interfaces preliminares com a revisão constitucional. São catálogos de planejamento, não inventários jurídicos exaustivos. DEC-001 estabelece **um único Código federal integrado** como objetivo. DEC-016 (veículo de promulgação, reservas de espécie/iniciativa, veto, transição) segue PENDENTE. Não há Livro normativo juridicamente homologado.

| Frente / dono | PR / issue | Entrega verificável recente | Pendência principal |
| --- | --- | --- | --- |
| T07.M03 — processo administrativo | #39 / #35 e #26 | 215 unidades da Lei 9.784 em espelho dos ciclos 13–19, protótipo de 14 cláusulas e pesquisa posterior até ciclo 37 (editais e intimação) | C0-J, direito externo, provas sobre ciência, transição e DEC-016 |
| T43.M04 — governo digital | #43 / #42 | 259 unidades estruturais da Lei 14.129 e 14 destinos de leis modificadas estudados | Não duplicar arts. 51–54 nem igualar envio eletrônico a ciência; DOU/competências |
| T24.M01 — processo civil | #38 / #37 | CPC art. 85 com 36 unidades, 19 ocorrências de remissão e 45 pares de destino | C0-J, remissões implícitas, custas/garantias e histórico |
| T25 — Parte Geral penal | #32 / #31 | 10 ciclos; comparação CP×CPM e minutas A/B de culpabilidade | Diferenças materiais, penas e retroatividade; nenhuma alternativa ratificada |
| T29.M01 — segurados/dependentes RGPS | #41 / #40 | 18 rodadas, F4-2: seis pares 8.213×8.212, cinco coincidências na Câmara e uma divergência do dirigente sindical | DOU, efeitos distintos custeio/benefícios, interface M02/M05 e F2-D |

**T01.M04:** pesquisa sobre consolidação, veto, iniciativas reservadas, anexos e modelos P0–P5 já existe na main. A alternativa preparatória P2 permite escrever um corpus temático **sem resolver** a unidade formal DEC-001; P3/P4 seguem hipóteses constitucionais. Nenhum desses modelos foi homologado.

## 2. Regras de exclusividade entre frentes

1. **T07 é dono do efeito jurídico da intimação administrativa geral; T43 é dono da infraestrutura e dos direitos de governo digital.** Meio eletrônico, acesso, entrega, ciência e contagem de prazo não se confundem. Ver arts. 22–28/41 Lei 9.784 e aplicação específica da Lei 14.129 e regimes especiais.
2. **T07 conserva especialidade e subsidiariedade** (Lei 9.784 art. 69); T12 responde por contencioso fiscal, T10 pelo sancionador especial e T29 pelos procedimentos previdenciários. Não presumir incidência da regra geral em lugar de rito específico.
3. **T43 deve rastrear artigos alteradores nos respectivos diplomas de destino**, especialmente as mudanças posteriores da Lei 14.534/2023, e não replicá-los como regras autônomas em dois títulos.
4. **T24 não deve converter o CPC em processo administrativo universal.** Sua aplicação supletiva/subsidiária possui pressupostos próprios; preservar competências, prazos, custas e direitos.
5. **T25 não pode unificar penal comum e militar por renumeração**, quando erro, coação, tentativa, justificação ou pena tenham consequências distintas. Isso é M e exige decisão explícita.
6. **T29 não deve fundir as Leis 8.212 e 8.213 só por coincidência textual**. Filiação, custeio, qualidade, benefício e dependência mantêm funções distintas. A duplicação F2-C já foi provisoriamente reconciliada: P19 como modelo de referência, E15 como controle; 47 casos comuns e quatro adicionais, não terceira série cumulativa. Questões jurídicas permanecem abertas. Conflito de art. 73-A (vigências 2026/2027) demanda estudo titular, não retificação editorial.

## 3. Portas de qualidade

- **C0-T**: textos correspondem no recorte documentado; não comprova versão histórica ou efeitos jurídicos.
- **C0-J**: exige prova por unidade de destinatários, âmbito, direito material, competências, exceções, direitos e deveres, remissões, prazos, vigência, especialidade, veto, transição e instrumento válido.
- **C1/M**: ajustes com ou sem alteração material devem ser classificados, fundamentados e aprovados, sem inseri-los implicitamente numa consolidação.
- **Q**: todas as dúvidas sem prova jurídica suficiente permanecem expressas; sucesso de script/CI valida somente o aspecto testado.
- **Merge de pesquisa**: permitido só após auditoria técnica do HEAD, ausência de colisão/duplicidade, preservação de fontes e pacote FEITO/PENDENTE/PRÓXIMO. Não equivale à aprovação de dispositivos, revogação ou DEC-016.

## 4. Caminho para o primeiro núcleo normativo

Escolha operacional de trabalho: **T07.M03**, primeiro núcleo do futuro Livro do Processo Administrativo Federal, começando pelos 21 registros dos arts. 1º–2º e pelo art. 69 como controle de especialidade. Os 215 registros já existentes são universo mínimo de regressão antes de qualquer revogação integral; os 14 artigos do ciclo 20 são demonstrações **insuficientes** como substituto legislativo.

A [proposta de texto e gates](03_PILOTO_T07_PRIMEIRO_NUCLEO_20261014.md) constitui exercício F5 **não homologado**. A frente T07, com T43 e T01, precisa testar a troca contextual 'esta Lei' → 'este Livro' e se isso preserva alcance administrativo federal, outros Poderes em função administrativa, rol aberto de direitos, leis especiais, competência e direito digital; os módulos externos continuam titulares de suas matérias.

**Decisões não tomadas:** veículo DEC-016; numeração definitiva; reforma material de garantias; obrigação universal de processo digital; conteúdo revogatório; homologação C0-J de qualquer unidade.

**Próximo passo executável:** T07.M03/issue #35 preparar a ficha 21+1 com destino, fundamentos e dez cenários adversariais de âmbito/especialidade; rever com T43/T01 e registrar resultados Q antes de submeter artigos à decisão central.
