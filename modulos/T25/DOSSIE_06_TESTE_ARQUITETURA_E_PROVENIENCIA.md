# T25.M01–M02 — Ciclo 06: teste adversarial de arquitetura penal e prova documental da reforma de 1984

**Data de consulta:** 14/10/2026 (Brasília). **Issue:** [#31](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/31) · **PR:** [#32](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/32), rascunho; `main` na abertura `16fba172c875c7a0de388288fe70005c944021d6`. **Fases:** F1–F3 ampliadas por fonte setorial, **F4 teste controlado de alternativas**, **sem minuta de lei adotada, sem revogação, sem equivalência C0-J**.

## 1. Síntese analítica — o que mudou neste ciclo

O confronto revelou problema substantivo novo, além das 14 hipóteses do ciclo 05:

1. **CPM art.30, parágrafo único × CP art.14, parágrafo único:** a regra comum prevê a pena de tentativa reduzida de um a dois terços, ressalvadas disposições diversas; o CPM também admite a redução, **mas permite, no caso de excepcional gravidade, aplicação da pena do crime consumado**. Essa diferença muda a amplitude judicial da pena e **não pode desaparecer como mera edição C0/C1**. Questionar a conveniência dessa exceção é **reforma M**, cuja necessidade de controle constitucional/proporcionalidade deve ser pesquisada.
2. **CPM art.9º, especialmente inciso II com redação da Lei 13.491/2017:** a qualificação como crime militar pode alcançar crime previsto na **legislação penal**, em condições de sujeito, função e local. Não basta separar tipos militares versus comuns pela lei onde se encontram. Uma alteração de regra de incidência pode produzir efeitos **sobre competência jurisdicional e garantias processuais**, exigindo T26, Justiça Militar e CF/1988.
3. **CPM arts.10 e 15:** crimes em **tempo de guerra** e conceito temporal/setorial não se reduzem à Parte Geral civil, mesmo quando tipo penal comum integra o regime militar por condição de guerra.
4. **CPM art.3º:** medidas de segurança seguem referência própria de lei vigente à sentença/execução; não se pode dar a regra como constitucionalmente livre de problema nem transplantá-la sem reconstruir CF art.5º XL, jurisprudência e natureza das consequências.
5. **CPM art.2º §§1º–2º, com Lei 14.688/2023:** retroatividade benigna é garantia compartilhada, mas a forma legal de comparar leis **por conjunto de normas aplicáveis ao fato** necessita preservação e teste contextual. A identidade de finalidade constitucional não prova identidade literal ou intertemporal de todas as normas.

**Fonte primária examinada:** [Câmara — Código Penal Militar atualizado, DL 1.001/1969, arts. 1º–35 e notas de 2017/2023](https://www2.camara.leg.br/legin/fed/declei/1960-1969/decreto-lei-1001-21-outubro-1969-376258-normaatualizada-pe.html), consulta de 14/10/2026; [CP comum atualizado](https://www2.camara.leg.br/legin/fed/declei/1940-1949/decreto-lei-2848-7-dezembro-1940-412868-normaatualizada-pe.html), arts. 1º–31; [Lei das Contravenções Penais](https://www.planalto.gov.br/ccivil_03/decreto-lei/del3688.htm), arts. 1º–4º; [Código Eleitoral do TSE](https://www.tse.jus.br/legislacao/codigo-eleitoral/codigo-eleitoral-1/codigo-eleitoral-lei-nb0-4.737-de-15-de-julho-de-1965), art.287; e demais fontes indicadas na matriz do ciclo 05. **Amostras**, não inventário normativo militar completo.

## 2. Segundo caminho encontrado para o texto histórico de 1984

Além da edição do DOU identificada no ciclo 05, há [Coleção das Leis da República Federativa do Brasil de 1984, Câmara dos Deputados, publicada pelo Departamento de Imprensa Nacional](https://bd.camara.leg.br/bd/items/0cd48368-68f7-4cab-a101-891629ff0cbd), em **dois arquivos digitalizados**. A **Parte 1 – Atos do Poder Legislativo** tem [PDF `colecao_leis_1984_parte1.pdf` (~13,15 MB)](https://bd.camara.leg.br/bd/bitstreams/e4497ab4-fafa-4d27-af34-11f8222627a9/download) e indicação de que a Lei 7.209/1984 figura na **Coleção de Leis de 1984, vol.5, p.38**, segundo [Câmara — dados da Lei 7.209](https://www2.camara.leg.br/legin/fed/lei/1980-1987/lei-7209-11-julho-1984-356852-norma-pl.html).

**Situação probatória:** a coleção é fonte institucional histórica adicional e foi **localizada**, mas o PDF de 13,15 MB não pôde ser inspecionado visualmente nesta sessão. O fac-símile DOU `DO_1_19840713_135.PDF` também permaneceu inacessível ao leitor de PDF neste ciclo. **Não afirmar** autenticidade/solução dos três pontos de divergência (arts. 3º, 4º, 12). A versão denominada "Publicação Original" da Câmara em HTML, inclusive seu segundo endereço histórico `...publicacaooriginal-148882-pl.html`, reproduz divergências sintáticas; **duas páginas não equivalem a dois originais independentes**. A redação atualizada do CP na Câmara constitui espelho textual contemporâneo separado.

**Fonte de controle:** [Câmara — Lei 7.209/1984, primeira representação textual](https://www2.camara.leg.br/legin/fed/lei/1980-1987/lei-7209-11-julho-1984-356852-publicacaooriginal-1-pl.html), arts.3º, 4º e 12 introduzidos no CP. Questões abertas do inventário anterior: `embora, decorrido`, `praticado a crime`, `aplicam especial se`. A prova documental exige *página e imagem*, idealmente DOU original e volume da Coleção de Leis, antes de reparar o histórico por inferência. O erro de transcrição é hipótese forte, **não fato histórico demonstrado**.

## 3. Método de confronto A/B/C: critérios e 18 cenários

[Matriz `TESTE_COMPARATIVO_MODELOS_ABC_CICLO06.csv`](TESTE_COMPARATIVO_MODELOS_ABC_CICLO06.csv) traz **18 cenários hipotéticos** (14 recuperados do ciclo 05 + quatro casos adicionais) e, para cada um, o efeito a preservar, a resposta estrutural em A/B/C, a possível falha de codificação e o grau de risco **qualitativo e não empírico**. Nenhum cenário representa processo judicial julgado.

### Modelos definidos para comparação

- **A — Partes gerais paralelas:** CP/CPM continuam com regras completas e outras leis remetem ao corpus correspondente. Preserva a topologia conhecida, mas há duplicação e divergência acumulada.
- **B — Parte Geral única com exceções setoriais:** regra penal geral codificada uma vez; toda diferença precisa ser restabelecida em remissões ou parágrafos especiais. A economia normativa só é real se a matriz provar preservação de efeitos para **todos os subsistemas**.
- **C — núcleo geral e subpartes especializadas:** garantias e institutos de efeitos compartilhados ficam em núcleo expressamente delimitado; os regimes militar, contravencional, eleitoral e outras especialidades recebem regras gerais próprias **naquilo que diferirem** (incluindo definições, sujeitos, competência e consequências). Parte material de crimes especiais permanece nos respectivos títulos.

### Resultados por classe de dificuldade

| Questão | Modelo A | Modelo B | Modelo C | Conclusão do teste |
|---|---|---|---|---|
| Legalidade e retroatividade (CP 1º–2º / CPM 1º–2º) | mantém redundância | pode unificar após auditoria | pode unificar no núcleo | convergência potencial, mas cada efeito de 2023 a conservar |
| Extraterritorialidade militar (CPM 7º) | preserva regime próprio | exceção extensa e complexa | subparte militar com norma própria | diferenças são **materiais**, não economia editorial |
| Tentativa militar excepcional (CPM 30 PU × CP 14 PU) | conserva duas soluções | deve criar ressalva ou alterar a pena (M) | reserva regra militar expressa | hipótese com maior poder discriminante entre B/C |
| Contravenções (LCP 1º, 2º e 4º) | mantém lei de contravenções | requer duas ressalvas exatas | subparte contravencional | B e C não podem punir tentativa nem criar extraterritorialidade |
| Crime militar de tipo previsto na legislação penal comum (CPM 9 II) | mantém incidência legal própria | risco de confundir locus de tipo e natureza militar | mantém critério em subparte militar | taxonomia de tipos **não** substitui regra de competência |
| Tempo de guerra (CPM 10 e 15) | mantém | exige exceção extensa | subparte militar própria | importante para garantias, tratados e transição |
| Eleitoral (CE 287) e trânsito (CTB 291) | remissões setoriais | possível economia de remissões | núcleo + remissões só necessárias | redundância não é derrogação substantiva |
| Medida de segurança (CPM 3º) | pode manter regra problemática | reescrever exige justificativa | colocar regra em Q sujeito a auditoria | **todos** os modelos dependem de teste constitucional |
| Responsabilidade penal pessoa jurídica (Lei 9.605 art.3º) | preserva | precisa prever sujeitos especiais | subparte especial ou regras PJ | há adição material além de exceção a pessoa natural |

### Avaliação qualitativa das alternativas — sem pseudoquantificação

**A (conservação paralela)** satisfaz melhor o controle imediato de continuidade textual, **desde que** a execução de cada referência e as atualizações sejam reconciliadas; porém contraria parcialmente o objetivo de simplificação sistemática e preserva divergências normativas a investigar.

**B (núcleo totalmente unificado)** tem máximo potencial de concentração editorial, **mas neste momento exige maior prova de equivalência jurídica**. Em especial, CPM art.30 PU, art.7º, art.9º e art.10 não devem desaparecer ao substituir o CPM inteiro por institutos comuns. Uma fusão por cópia em B **seria materialmente transformadora, portanto M, não C1**.

**C (núcleo geral + subsistemas)** é **hipótese de arquitetura que melhor equilibra unidade formal e diferenças materiais, no recorte limitado**, porque permite reutilizar garantias (legalidade e retroatividade) sem omitir regras penais militares, contravencionais ou eleitorais. Isso **não significa escolha ratificada** ou prova de que C manterá todos os efeitos: falta inventário completo e haverá remissões e redundâncias residuais. Não impor desde já que toda regra especial seja subparte; avaliar ergonomia e distribuição de temas.

**Contraprova da hipótese C:** se a matriz completa demonstrar que exceções são raras, curtas e não interdependentes, B pode ser estruturalmente superior. Se verificar que o CPM forma regime integralmente autônomo com forte interação entre tipos e consequências, A pode ser mais seguro na transição. Essas são condições de revisão, não previsão de resultados.

## 4. Arquitetura funcional candidata, **NÃO texto normativo**

Caso o debate avance na hipótese C, testar as seguintes **unidades funcionais** (sem numeração de artigos ou reserva de conteúdo):
1. Disposições penais gerais: legalidade; lei no tempo e no espaço; imputação, culpabilidade e consequências comuns; condições de incidência expressamente penais.
2. Regras gerais do regime **contravencional**: classificação e consequências especiais; territorialidade; tentativa não punível; remissões delimitadas.
3. Regras gerais do regime **penal militar**: aplicação, sujeitos, tempo de guerra, crime militar por circunstância, extraterritorialidade e tentativa militar especial; remissões precisas e garantias comuns.
4. Regimes penais **eleitoral e setoriais**: só manter disposições gerais autônomas quando demonstração de necessidade; remissões processuais separadas em T26, execução em T27.
5. Cláusulas de interface: o núcleo de aplicação deve referir **"disposições gerais de direito penal [unidade exata]"**, nunca o CLF inteiro por `deste Código` sem restrição de escopo; nova redação exige avaliação C1/M conforme efeitos.

**Cuidado de espécie legislativa:** as regras jurídicas superiores de legalidade, competência constitucional, justiça militar e direitos não são modificadas por redistribuir textos no CLF; decisões de reforma substancial precisam processo legislativo adequado, inclusive DEC-016 ainda pendente.

## 5. Decisões, revisão adversarial e portas de qualidade

- **Classificação:** fontes textuais CP/CPM/LCP analisadas (com lacunas de histórico e atualização) = F1/F2 seletivo; 18 cenários = **F4 exploratório, `Q`**; não há transposição ou emenda de conteúdo na proposta CLF. `C0-T` do CP compilado arts.1º–12 continua válido somente como registro de fonte do ciclo 03; **`C0-J` não foi demonstrado**.
- **Problema novo PROB-T25-0017:** preservar a **exceção militar na punibilidade da tentativa** (CPM art.30 PU), avaliando legalidade/individualização e comparação com CP art.14 PU. A simples substituição pelo CP comum **é alteração M**.
- **Problema novo PROB-T25-0018:** critério de crime militar definido por **circunstâncias** e legislação penal comum (CPM art.9 II), interfaciando T26 e CF/1988. Sem regra de qualificação, a codificação pode alterar competência e defesa.
- **Problema novo PROB-T25-0019:** técnica de redução normativa pode **ocultar excepcões necessárias** ou reabrir disparidades não justificadas; decidir por prova de efeitos, não por quantidade de dispositivos.
- **Melhores objeções ao modelo C:** risco de burocracia de remissões e ambiguidade do que é geral/especial; possibilidade de conservadorismo excessivo ao preservar exceções problemáticas; aplicação judicial de subpartes sem determinação clara do subsistema aplicável. Testar com casos de concorrência de leis penais, mil/eletoral, crimes permanentes e ações omissivas.

### Próximo ciclo prioritário

**Tarefa executável:** obter uma imagem verificável do DOU de 13/07/1984 (ou, subsidiariamente, da **Coleção das Leis de 1984, vol. 5, p.38**) e cotejar CP arts.3º,4º,12 com transcrições oficiais digitalizadas, registrando evidência por página/coluna. **Porta de aceite:** identificar por imagem texto original e texto publicado na coleção, marcar origem de cada divergência ou `A_VERIFICAR`; **não usar OCR sem conferência visual**.

**Em segundo lugar:** inventariar CPM arts. 1º–40 por subunidades, incluindo remissões, datas de alteração 2017/2023, natureza do delito militar e efeitos da tentativa; depois rodar casos acima com hipóteses concretas das exceções antes de elaborar minuta penal. **Não mexer na `main` do CLF ou no projeto de Constituição por esta branch.**
