# T24.M01 — F1-D7: concordância jurídico-material adversarial do art. 85 do CPC
**Data-corte:** 14/10/2026. **PR #38 draft.** **Não é homologação C0-J, não é edição definitiva do CLF e não altera a jurisprudência vigente.** Foram cotejadas as 36 unidades textuais já comprovadas no [espelho oficial gerado por CI](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38554226642/artifacts/11887718493) com precedentes qualificados e remissões internas/externas. Todos os **36 registros permanecem Q**.

## FEITO — matriz e grafo
- [Matriz por 36 unidades](MATRIZ_F1D7_36_HONORARIOS_JURISPRUDENCIA.csv): cada dispositivo tem função jurídica, invariantes, temas pertinentes e risco de perda por codificação. A ausência de tema repetitivo indicado **não** significa ausência de jurisprudência.
- [Grafo de 35 referências legais expressas](GRAFO_F1D7_REMISSOES_EXPRESSAS_ART85.csv): 34 vínculos internos ao art.85 e um externo (art.85 §12 → art.77), sem renumerar o destino no projeto. **Distinção:** o mapa funcional `MAPA_36_UNIDADES_ART85_REMISSOES_E_GATE.csv` admite associações conceituais; este novo grafo contém exclusivamente as remissões expressas que precisam ser reendereçadas.
- **Controle crítico §20:** §§2º, 3º, 4º, 5º, 6º, 6º-A, 8º, 8º-A, 9º e 10 (10 referências); §11: §§2º a 6º, com tetos §§2º e 3º; §12: §11 e art.77; §§3º–5º preservam a progressividade para Fazenda. [CPC atualizado, Câmara](https://www2.camara.leg.br/legin/fed/lei/2015/lei-13105-16-marco-2015-780273-normaatualizada-pl.html), art.85.

## Cinco precedentes que impedem um P7 simplificado
**1. STJ Tema 1.076 — base percentual e equidade.** [Ficha oficial](https://processo.stj.jus.br/repetitivos/temas_repetitivos/pesquisa.jsp?cod_tema_final=1076&cod_tema_inicial=1076&novaConsulta=true&tipo_pesquisa=T): nas causas de alto valor, aplica-se a regra percentual do art.85 §2º ou §3º; apreciação equitativa somente nas hipóteses legais de vantagem inestimável ou irrisória ou causa muito baixa. **Controle**: não permitir equidade fundada apenas em suposta exorbitância, sem precedentes constitucionais aplicáveis.

**2. STJ Tema 1.313 — demandas prestacionais de saúde contra Poder Público.** [Ficha oficial](https://processo.stj.jus.br/repetitivos/temas_repetitivos/pesquisa.jsp?cod_tema_final=1313&cod_tema_inicial=1313&novaConsulta=true&tipo_pesquisa=T) e [Informativo STJ 854](https://processo.stj.jus.br/jurisprudencia/externo/informativo/?acao=pesquisar&aplicacao=informativo&livre=%40CNOT%3D%27021597%27): obrigação de fazer/dar prestação de saúde contra o Poder Público atrai equidade do §8º, **sem o §8º-A**. **Controle**: não estender automaticamente a qualquer ação de saúde entre particulares, e não obrigar tabela OAB para esse recorte.

**3. STJ Tema 1.059 — honorários recursais.** [Ficha oficial](https://processo.stj.jus.br/repetitivos/temas_repetitivos/pesquisa.jsp?cod_tema_final=1059&cod_tema_inicial=1059&novaConsulta=true&tipo_pesquisa=T): a majoração do §11 pressupõe recurso **integralmente desprovido ou não conhecido**, excluído provimento total ou parcial ainda que apenas de consectários. **Controle**: o texto do §11 isolado, renumerado, não deve fazer perder os pressupostos judiciais concretos.

**4. STJ Tema 1.190 — cumprimento não impugnado contra Fazenda e RPV.** [Ficha oficial](https://processo.stj.jus.br/repetitivos/temas_repetitivos/pesquisa.jsp?cod_tema_final=1190&cod_tema_inicial=1190&novaConsulta=true&tipo_pesquisa=T), [Informativo STJ 818](https://processo.stj.jus.br/jurisprudencia/externo/informativo/?livre=%40CNOT%3D020809). Sem impugnação à pretensão executória, **não há honorários sucumbenciais adicionais em cumprimento contra Fazenda**, mesmo crédito por RPV. O precedente menciona **modulação e alteração de orientação**; a data/alcance precisos dessa modulação exigem conferência do inteiro teor antes de qualquer cláusula transitória. **Controle**: leitura apenas literal de `precatório` no §7º pode divergir da interpretação que abrange a RPV, e a referência ao §1º exige análise conjunta.

**5. STF Tema 1.255 — controle constitucional ainda aberto.** [Tema oficial](https://portal.stf.jus.br/jurisprudenciaRepercussao/tema.asp?num=1255): há repercussão geral reconhecida em 2023, **sem publicação de julgamento definitivo de mérito identificada na ficha consultada em 14/10/2026**. A controvérsia envolve honorários quando valores são exorbitantes e a Fazenda Pública segundo delimitações processuais a acompanhar. **Controle**: não atribuir tese de mérito ao STF nem antecipar modulação.

## Testes de não regressão normativa
| Teste | Direito vigente demonstrado | Simplificação rejeitada |
|---|---|---|
| Honorários de Fazenda acima de 200 SM | Faixas de §3º e aplicação progressiva §5º | Percentual único sobre condenação inteira |
| Equidade de causas de valor alto | Tema1076/STJ ressalvadas hipóteses legais | Equidade livre por “razoabilidade” abstrata |
| Prestação de saúde contra Poder Público | Tema1313/STJ: equidade, sem §8º-A | Piso automático de tabela OAB |
| Recurso provido parcialmente | Tema1059/STJ não admite majoração do §11 | Majoração em todo recurso julgado |
| Recurso integralmente improvido | Tema1059 permite observar §11 conforme pressupostos | Excluir honorários recursais indiscriminadamente |
| Cumprimento Fazenda não impugnado por RPV | Tema1190/STJ afasta sucumbenciais adicionais, com intertemporalidade a verificar | Exigir honorários automáticos só porque §7º fala em precatório |
| Honorários em causa própria | CPC §17 assegura verba | Suprimir proteção do advogado em causa própria |
| Omissão no título transitado | §18 permite ação autônoma | Exigir sempre embargos de declaração prévios no CLF |
| Arbitramento judicial | §20 remete exatamente a dez parágrafos | Substituir por `aplica-se no que couber` sem destinos |
| Advogado público | §19 observa leis específicas | Crédito idêntico e irrestrito em qualquer regime remuneratório |

## Os limites técnicos da matriz
A atribuição de temas a determinados incisos é **índice de relevância**, não decisão judicial individual de todos esses incisos. Um precedente repetitivo também pode ter alcance limitado por fatos e intertemporalidade; sua interpretação não é texto literal de lei. Os 33 dispositivos idênticos entre duas fotografias e três acréscimos de 2022 não provam que a remoção de um artigo para o CLF mantenha seu sentido. A transposição exige cadeia DOU, vigência, espécie e iniciativa (`DEC-016`), harmonização de causas especiais e preservação do §20 e do art.77.

## PENDENTE / PRÓXIMO
**PENDENTE:** precisão da modulação do Tema 1190; atualização STF 1255; jurisprudência de outros dispositivos, cadeia DOU e leis alteradoras, ligação do art.85 à sucumbência e JG dos arts. 82–102, remissões externas reais e competência. Nenhuma promoção C0-J. **PRÓXIMO:** incorporar testes estáticos de integridade do grafo e matriz, revisar especificamente modalidades de RPV/precatório, JG/garantias recursais e emitir quadro de equivalência por dispositivo com os 8 critérios jurídicos previamente estabelecidos, antes de levantar o bloqueio de P7.
