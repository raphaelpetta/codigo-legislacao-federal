# T07.M03 — Ciclo 20: primeira auditoria transversal de equivalência normativa (C0-J)

**ID:** CLF-T07-M03-DOS20 · **Corte:** 14/10/2026 · **Status:** F1/F2 AUDITORIA PRELIMINAR, **sem certificação geral C0-J**, sem lei promulgada ou revogada e sem deliberação de reforma material.  
**Base GitHub:** [CLF PR #34](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/34), com 215 unidades textuais espelhadas dos ciclos 13–19.  
**Fontes primárias:** [Lei 9.784/1999 — Câmara](https://www2.camara.leg.br/legin/fed/lei/1999/lei-9784-29-janeiro-1999-322239-normaatualizada-pl.html), [LC 95/1998](https://www2.camara.leg.br/legin/fed/leicom/1998/leicomplementar-95-26-fevereiro-1998-363948-normaatualizada-pl.html), [LINDB, Lei 13.655/2018](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13655.htm), [Lei do Governo Digital 14.129/2021](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14129.htm).

## 1. Objetivo da rodada e resultado

A fase de cópia literal terminou; **não há razão para seguir acrescentando planilhas de simples transcrição**. O próximo problema é verificar se as normas produzem o mesmo direito **depois** de agrupadas num Livro integrado, e não só se seus caracteres coincidem. A transposição demanda testar **alcance pessoal e federativo, competência, garantias, prazos, exceções, vigência, remissões, especialidade e legislação superveniente**.

Entregues nesta rodada:

1. `MATRIZ_TRIAGEM_215_UNIDADES_CICLO20.csv`: **215 linhas**, uma por unidade positiva espelhada, com texto de origem, identificador estável, destino **em títulos de um único Livro**, sinais de risco e fila de prioridade. **Todas ainda `Q` e `NAO_AUDITADA_JURIDICAMENTE`**. A triagem é automática: prioridade e tags não equivalem a análise jurídica conclusiva.
2. `CONTRAPROVAS_SEMANTICAS_CICLO20.csv`: **32 situações jurídicas criticamente analisadas** para demonstrar que certas transformações não são neutras, ou dependem de prova/decisão material. Esses juízos se referem **às transformações hipotéticas** (p.ex., trocar `desta Lei` por `deste Código`), não às 215 unidades individualmente homologadas.
3. `MATRIZ_INTERFACES_EXTERIORES_CICLO20.csv`: **15 interfaces** com legislação não contida na Lei 9.784 e jurisprudência, que precisam ser verificadas antes de tratar seu Livro como sistema completo.
4. `ARQUITETURA_E_MINUTA_DEMONSTRATIVA_CICLO20.md`: **primeira arquitetura provisória de seis títulos dentro de um Livro único**, com **14 cláusulas experimentais de integração**. É amostra de técnica jurídica, não substituto condensado da Lei 9.784 nem minuta aprovada.

### Distinção entre quatro fases de trabalho

| Rótulo | Prova exigida | Situação agora |
|---|---|---|
| **C0-T** | Origem e espelho textualmente iguais | **215 transcrições** com verificação automática de igualdade entre campos; comparação universal autônoma com DOU ainda pendente |
| **C0-J** | Preservação demonstrada de alcance, destinatários, competências, direitos, efeitos temporais, exceções e direito externo aplicável, **dado um instrumento legislativo válido** | **Nenhuma das 215 aprovada ainda** |
| **C1** | Ajuste editorial com prova documentada de que conteúdo e efeitos permanecem | Hipóteses em estudo, sem aprovação |
| **M** | Alteração material expressa, justificada por pesquisa, com quórum/iniciativa apropriados | Hipóteses registradas; nenhuma aprovada |
| **Q** | Dúvida, falta de prova, bloqueio de requisitos | Situação de toda a transposição jurídica nesta rodada |

**Importante:** a categoria `C0-J` não depende apenas de equivalência semântica abstrata: a força normativa, a entrada em vigor, o ato promulgatório e a sucessão válida de leis também importam. Nenhum teste informático constitui promulgação.

## 2. Primeiros resultados adversariais de fundo

### A. O universo da lei não pode virar o universo do Código

O art. 1º da Lei 9.784 define **processo administrativo federal** e sua aplicação a outros Poderes da União **em função administrativa**. O art. 69 aplica essa própria lei **subsidiariamente** aos processos especiais. Se o futuro CLF de 48 títulos substituir `desta Lei` por `deste Código`, uma regra originalmente restrita passará, em tese, a remeter a **todo** o Código — grave mudança de alcance. **Conclusão condicional verificável:** a substituição mecânica **NÃO** é neutra. É necessária a delimitação de um **Livro do Processo Administrativo Federal**, e comprovação de que todas as remissões correlatas foram ajustadas sem perder a especialidade.

O [REsp 1.046.376/DF/STJ](https://scon.stj.jus.br/SCON/GetInteiroTeorDoAcordao?dt_publicacao=16%2F08%2F2021&num_registro=202001449632), julgado como repetitivo segundo precedente citado no acórdão oficial de 2021, é fonte para examinar primazia do regime especial e subsidiariedade do art. 69. **Conferir o inteiro teor do precedente original antes de extrair qualquer formulação maior**. A [Súmula 633/STJ](https://processo.stj.jus.br/jurisprudencia/externo/informativo/?livre=%40CNOT%3D017068) restringe aplicação subsidiária a estados e municípios à ausência de lei local e específica.

### B. Regras gerais não anulam exceções especiais

Alguns pares evidenciam por que `repetição de palavras` não é `repetição de direito`:

- **Art. 2º X x art. 38 § 2º:** o direito geral de prova **não substitui** as causas e fundamentação específicas da recusa de prova.
- **Art. 26 x art. 41:** intimação geral e comunicação de prova/diligência com **antecedência de três dias úteis** são normas relacionadas, mas não idênticas.
- **Art. 31 § 2º x art. 9º:** participar de consulta dá direito a resposta fundamentada, **não automaticamente** a qualidade de interessado do processo.
- **Art. 42 §§1º/2º:** a lei atribui consequências opostas ao atraso de parecer obrigatório **vinculante** (não prosseguir) e **não vinculante** (prosseguir admissível).
- **Art. 49-A §6º:** decisão coordenada exclui licitação, processo sancionador e autoridades de Poderes distintos; resumo em regra geral de coordenação não pode eliminá-los.
- **Art. 64 parágrafo único x art. 65 parágrafo único:** recurso pode admitir agravamento com **prévia ciência e alegações**; revisão sancionatória **proíbe** o agravamento.
- **Art. 66 §2º:** prazos em dias são contados **continuamente**; adotar dias úteis em geral seria **reforma material**, não reindexação.

Desses resultados não decorre a proibição de reformar a lei: decorre que a reforma precisa ser **identificada, fundamentada e aprovada**, em vez de escondida numa consolidação.

### C. A Lei 9.784 convive com outros diplomas necessários

**LINDB**: os arts. 20–30 acrescidos pela Lei 13.655/2018 regulam consequências, revisão de atos, transição de novas interpretações, compromissos, motivação e segurança jurídica na aplicação do direito público. O art. 50 da Lei 9.784 **não esgota** essa matéria. O [Decreto 9.830/2019](https://www2.camara.leg.br/legin/fed/decret/2019/decreto-9830-10-junho-2019-788287-publicacaooriginal-158117-pe.html) regulamenta essas disposições em nível próprio; não incorporar um decreto ao Livro como lei sem examinar competência e hierarquia. O enquadramento final dessas normas na arquitetura do Código ainda é **Q**.

**Lei 14.129/2021 (Governo Digital)**: disciplina trâmite eletrônico, regras de exceção ao meio digital e comunicação/intimação por domicílio eletrônico, notadamente arts. 5º–6º e 42–43. Copiar isoladamente a Lei 9.784, arts. 22 e 26, sem isso seria um retrato **incompleto do direito vigente**, ainda que fiel ao texto de 1999. A exata incidência da Lei 14.129 para cada ente e Poder necessita verificação por dispositivo e por data. **Não** afirmar derrogação automática de toda formalidade anterior.

**Outras interfaces:** LGPD e LAI na vista dos autos e proteção dos dados; simplificação de formalidades e assinaturas eletrônicas; prescrição punitiva federal da Lei 9.873/1999 versus decadência da anulação de atos favoráveis do art. 54; ritos de licitação e sanção da Lei 14.133/2021; direitos dos usuários de serviços públicos da Lei 13.460/2017; jurisprudência sobre normas especiais e federalismo. **Nenhuma dessas leis foi automaticamente incluída ou revogada neste ciclo.**

### D. A vigência antiga não pode ser transplantada

O art. 70 da Lei 9.784 é o controle negativo por excelência: `Esta Lei entra em vigor na data de sua publicação` referia-se à **publicação do ato de 1999**. Mesmo transcrito com perfeita identidade, não define a vigência do CLF. Exigir **novo dispositivo autêntico de entrada em vigor** e preservar o registro histórico, em vez de fazer a frase voltar a produzir efeitos como se fosse de novo promulgada. Também não reviver o **art. 49-C vetado** ou outras subunidades vetadas.

## 3. Técnica de integração — regra geral única, exceção mantida

O documento de arquitetura oferece **14 artigos de demonstração**, agrupados num **único Livro**, testando a unidade estrutural:

- **Âmbito e subsidiariedade**: art. 1º e art. 69 aproximados, mas com âmbito do Livro, não do Código inteiro.
- **Competência**: irrenunciabilidade geral + capítulos contendo inelegibilidades delegatórias, publicidade e avocação.
- **Intimação**: regra geral do art. 26 uma vez, **requisito especial do art. 41** na instrução de prova/diligência.
- **Instrução**: direitos gerais e regras específicas de ônus, busca de documentos e recusa motivada de prova.
- **Pareceres**: norma sobre prazo geral e **divisão nítida** entre vinculante e não vinculante.
- **Decisão coordenada**: competência de cada órgão, exclusões e **lacuna de convocação** do art. 49-C vetado reconhecidas.
- **Recurso e revisão sancionatória**: institutos separados, sem importar restrição de um para outro.
- **Prazos**: regra geral contínua; prazos especiais claramente vinculados à própria hipótese.
- **Transição e revogação**: o novo Livro só alcançaria status positivo mediante o **ato constitucionalmente competente**, com proteção de processos pendentes e efeitos do direito antigo.

**Limite da amostra:** esses 14 artigos contêm **sínteses e redações parciais** e **NÃO SUBSTITUEM** as 215 unidades da Lei 9.784. Uma versão integral precisará transpor cada garantia, exceção, prazo e requisito ainda omitido, demonstrando concordância jurídica 1:1 ou justificação de alteração M. **Não há minuta pronta para aprovação legislativa.**

## 4. Portas de qualidade para a próxima fase

| Controle | Critério de passagem | Estado |
|---|---|---|
| Q20.1 — proveniência | 215 textos conferidos contra DOU, retificações, versões de 2006/2009/2021 e veto, não só CSV espelhado | **ABERTO** |
| Q20.2 — relações normativas | Remissões e dependências literais e implícitas **exauridas** no Livro; regras especiais identificadas | **ABERTO** |
| Q20.3 — direito externo | Cada interface com LINDB, Lei14.129, LAI, LGPD, leis especiais e súmulas avaliada por dispositivo, âmbito e data | **ABERTO** |
| Q20.4 — contraprovas | Cada uma das **32** transformações testadas e cada desvio considerado em minuta | **CASOS PRODUZIDOS**, decisões não homologadas |
| Q20.5 — redação legal única | Todos os efeitos da Lei 9.784 e do regime selecionado preservados ou marcados M; nenhum resumo perde direito | **PROTÓTIPO DE ARQUITETURA, INCOMPLETO** |
| Q20.6 — veículo | CF iniciativa, quórum, veto, fonte autêntica, transição e revogação compatíveis | **DEC-016 PENDENTE** |
| Q20.7 — governança | Decisões aprovadas registradas separadamente das hipóteses e sincronizadas com CF-IC-001 | **NENHUMA MINUTA APROVADA** |

## 5. Feito, pendente, próximo

**FEITO:** primeira triagem sistemática de **215 unidades**, **32 contraprovas semânticas**, **15 interfaces de legislação/jurisprudência** e **arquitetura experimental de um Livro com 14 artigos de demonstração**, preservando `Q` e nenhum efeito normativo.

**PENDENTE:** conferir todas as fontes históricas e vigências, expandir universo ao direito externo aplicável, provar conservação ou registrar reforma em cada unidade, redigir o Livro integral, testar efeitos e resolver o instrumento constitucional `DEC-016`. **`DEC-001` é finalidade confirmada; não substituir Código uno por coleção de diplomas ou planilhas.**

**PRÓXIMO:** escolher um primeiro bloco para auditoria aprofundada de verdade (sugeridos **arts. 1º–3º + art. 69 + LINDB** e **arts. 22–28/41 + Lei 14.129**), com correspondência texto a texto, contexto e efeito, começando a emitir pareceres **C0-J condicionais apenas onde os critérios forem satisfeitos**. Não transformar a triagem automática em aprovação global.
