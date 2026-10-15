# T25.M02 — Dossiê 09: excesso, elementares hierárquicas e a primeira comparação de minutas

**Consulta:** 14/10/2026. **Issue #31 · PR [#32](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/32) em rascunho.** **Baseline:** `main` `16fba172c875c7a0de388288fe70005c944021d6`. **Fases:** F1 CP/CPM setor selecionado (texto consolidado), F2 e F3 precedentes com voto integral publicado, F4 alternativas e **F5-EXP experimental**, não F5 redação ratificada. **Decisões C0-J/C1/M:** nenhuma.

## 1. CPM 46 e 47: efeitos que um redator não pode omitir

**Fontes oficiais:** [CPM consolidado em publicação Câmara](https://www2.camara.leg.br/legin/fed/declei/1960-1969/decreto-lei-1001-21-outubro-1969-376258-normaatualizada-pe.html), [versão Planalto](https://www.planalto.gov.br/ccivil_03/decreto-lei/del1001compilado.htm), [Lei 14.688/2023](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14688.htm). Conferido em 14/10/2026 o núcleo textual vigente dos arts.45–47; notas históricas *não* substituem o cotejo autêntico do DOU de 1969/2023.

- **CPM art.46:** permite que o juízo atenue pena mesmo se o excesso tenha sido doloso e punível. **Não é exclusão automática de crime e não contém quantum explícito**. Comparar com CPM art.45 PU (excesso escusável não punível), CPM art.73 (atenuantes com limites) e CPM art.76 (majorantes/minorantes especiais que podem ultrapassar limites cominados) antes de redigir consequência. CP art.23 PU pune excesso doloso/culposo; CP art.66 prevê atenuação genérica em circunstâncias relevantes, mas isto **não equivale textualmente** a conferir a mesma causa específica do CPM46.
- **CPM art.47, caput/I:** a qualidade de superior ou inferior hierárquico deixa de ser elemento constitutivo do crime se o agente a desconhecia. O dispositivo interage com os **tipos especiais hierárquicos**, com CPM art.24 (conceito de superior) e com CP art.20 (erro sobre elemento), porém **não** é só regra de erro com igual resultado em toda hipótese.
- **CPM art.47, II:** qualidade de superior/inferior, oficial de dia/serviço/quarto, sentinela/vigia/plantão também deixa de ser elemento constitutivo quando ação praticada em repulsa a agressão; não confundir retirada de **elementar hierárquica** com licença geral para qualquer agressão ou absolvição plena de outros delitos. O inciso foi atualizado na nomenclatura pela **Lei 14.688/2023**. Sua relação com legítima defesa CPM42 II/44, excesso CPM45/46 e tipos militares precisa ser testada.
- **Forma:** quatro unidades registradas em [`INVENTARIO_CPM_ART46_47_CICLO09.csv`](INVENTARIO_CPM_ART46_47_CICLO09.csv). Só o art.47 incisos I–II tiveram anotação de 2023; não atribuir mudança de art.46 sem fonte.

**Novo problema PROB-T25-0033:** distinguir exclusão de elementar hierárquica da própria exclusão da ilicitude. **PROB-T25-0034:** classificar natureza e quantum da atenuação de excesso doloso CPM46 sem copiar automaticamente art.66 do CP ou art.73 CPM.

## 2. Avanço probatório substancial: acórdão completo STM Ap 7000232-60.2024.7.00.0000

Foi localizado e aberto **PDF integral do volume da Revista de Doutrina e Jurisprudência do STM**, contendo páginas impressas **351–397** do julgamento em https://dspace.stm.jus.br/bitstream/handle/123456789/198251/REVISTA_34_n1___040725_PDFA.pdf?isAllowed=y&sequence=1 .

**Natureza da fonte:** reprodução institucional na revista de acórdão/relatório/voto relator/declarações de voto; exame efetivo do **texto disponibilizado** por páginas **351–397**, com **inspeção visual das páginas 352, 380 e 396**, e leitura do texto sobre os votos divergentes nas pp.381–397. Isso melhora a prova do ciclo 08, em que se dispunha apenas da ementa; não equivale a acesso ao processo eletrônico e todos os documentos das instâncias.

### 2.1. Dispositivo e posições reais do Pleno (julgado 25–28/11/2024; publicado na Revista 29/01/2026)

1. **Maioria, relator Min. Cláudio Portugal de Viveiros:** reformou a absolvição de primeiro grau em caso de porte de cannabis no quartel, considerando insuficiente a autorização médico-sanitária civil para a atividade no ambiente militar, **mas reconheceu aplicação do CPM art.35** para reduzir a pena. Fixou 1 ano base; agravante de 1/5 por estar de serviço (1 ano, 2 meses, 12 dias); aplicou redutor de 1/3 do CPM35 **na terceira etapa** para **9 meses e 18 dias de detenção**, sursis de dois anos e regime aberto se executada. Fonte: PDF pp.379–381 e ata pp.352–353.
2. **Dissenso absolutório Min. José Barroso Filho**, acompanhado, segundo ata publicada, por José Coêlho Ferreira e Maria Elizabeth Guimarães Teixeira Rocha: negaria provimento ao recurso ministerial, mantendo absolvição com fundamento no **art.439, b, do CPPM**, em razão das particularidades da autorização sanitária/receita, discussão do elemento subjetivo e limites da tipicidade. O voto não é adesão à solução da maioria baseada em redução de pena. Fonte: pp.381–396.
3. **Divergência de dosimetria Min. Carlos Augusto Amaral Oliveira:** concordou com condenação e mitigação do CPM35, **mas** considerou art.35 uma *atenuante própria* limitada pelo **CPM art.73**, não causa especial apta a reduzir abaixo do mínimo cominado. Fixaria **um ano de reclusão**. Invocou o STF **Tema 158** sobre atenuante genérica. Fonte pp.396–397 e ata pp.352–353.

**Controle de generalização:** STF [Tema 158, RE 597.270, rel. Cezar Peluso](https://portal.stf.jus.br/jurisprudenciaRepercussao/verAndamentoProcesso.asp?classeProcesso=RE&incidente=2663001&numeroProcesso=597270&numeroTema=158): a tese **diz respeito a atenuantes genéricas**, que não permitem pena aquém do mínimo. **NÃO decide automaticamente se a norma específica do CPM35 é atenuante genérica/própria ou causa especial de diminuição**: essa é justamente a divergência observada no STM. A revisão de codificação deve definir efeitos e resolver insegurança de categoria, se esse for o objetivo de reforma material.

**Tensão de expressão da ementa:** a fórmula da ementa sobre `erro de direito inescusável` convive com reconhecimento do benefício do art.35 pelo voto majoritário. A leitura do voto revela que o relator identificou dúvida concreta sobre crença subjetiva do acusado na validade de sua documentação e sustentou ser mais adequado reconhecer mitigação. Não apagar a contradição por resumo artificial: **Q de motivação/coerência probatória**, avaliação de eventual recurso e fundamentação jurídica ainda pendente.

**Fonte de prova controlada:** [`JULGADO_STM_ART35_E_TEMA158_CICLO09.csv`](JULGADO_STM_ART35_E_TEMA158_CICLO09.csv) distingue três posições do mesmo processo e o Tema 158, com páginas, grau de exame e efeito.

**Novo problema PROB-T25-0035:** dever de classificar inequivocamente mitigação do erro de proibição (atenuante genérica x causa especial) e estabelecer se/como opera abaixo do mínimo; repercute CP21, CPM35, CPM73/76, STF Tema158 e individualização da pena. **Não decidir apenas citando o Tema 158.**

## 3. Duas minutas com redação concreta — ambas não aprovadas

[`MINUTAS_EXPERIMENTAIS_AB_CULPABILIDADE_CICLO09.md`](MINUTAS_EXPERIMENTAIS_AB_CULPABILIDADE_CICLO09.md) contém dois textos estruturados com artigos de teste:

- **Minuta A (P-A1–P-A9):** núcleo comum de culpabilidade, erro, ordens, necessidade e excesso, com remissões militares precisas. **Introduz mudanças M** ao estender isenção por erro inevitável a militar, flexibilizar coação moral em dever militar, reformular justificação/exculpação, restringir exceção de comando violento do CPM42 PU e generalizar mitigação do excesso doloso. **Contraargumentos materialmente relevantes:** deveres militares especiais, risco de ampliar defesas a condutas graves, previsibilidade legislativa, descompasso de dosimetria, crimes de guerra e tratados.
- **Minuta B (P-B1–P-B9):** núcleo constitucional curto e subparte militar autônoma com pressupostos similares aos atuais CPM35–47 e regra de hierarquia. **Não é C0-J ou C1**: a forma abreviada deixa pendentes detalhes e remissões. Preservar literalmente os dispositivos e suas exceções dependeria de concordância completa, inclusive requisito `se escusáveis`, dever militar, CPM39/40/42PU, CPM45PU/46 e hipóteses do CPM47.
- **Ambas:** `P-A`/`P-B` são placeholders sem numeração legislativa; não há texto de revogação, efeito temporal, implementação, processamento ou tramitação aprovado.

[`CONCORDANCIA_PROPOSTAS_AB_CICLO09.csv`](CONCORDANCIA_PROPOSTAS_AB_CICLO09.csv) documenta **16 relações** CP/CPM × A/B com efeito possível, categoria experimental, risco e prova faltante. `categoria=Q` por não haver equivalência jurídica demonstrada e por se tratar de propostas sob teste; `categoria_a=M` identifica efeitos que seriam reforma na Minuta A, **não aprovação**.

## 4. Testes adversariais decisivos para A × B (F4)

| Caso controlado | A | B | Questão que decide |
|---|---|---|---|
| Erro inevitável de agente militar sobre ilicitude | isenção quando inevitável (**M** vs CPM35) | mitigação escusável sujeita à regra especial; garantia constitucional por resolver | prova da possibilidade real de consciência e disciplina |
| Agente militar ameaçado por violência moral grave para violar dever | inexigibilidade concreta em hipótese extrema (**M**) | CPM40 preservado, analisar CPM39 | limites de sacrifício e dever funcional |
| Ordens criminosas dadas por superior | responde quem agir com consciência e culpabilidade | CPM38 §2 explicitamente preservado | evitar imunidade e responsabilidade objetiva |
| Defesa com excesso por surpresa escusável | mecanismo geral com requisitos definidos (**M**) | instituto militar CPM45 PU | prova real de surpresa e vedação de pretextos para agressão |
| Excesso doloso punível | redução facultativa potencialmente geral (**M**) | regra militar CPM46 | naturezas de redutor, pisos e individualização |
| Crime militar depende da qualidade de superior desconhecida do autor | erro geral sobre elemento + ressalva | CPM47 I mantido | equivalência sobre elementares e crimes próprios |
| Repulsa de agressão contra sentinela por pessoa que conhece qualidade militar | aplicar defesa e regra especial a formular (**M**) | CPM47 II preservado | eliminação de elementar não é causa de licitude total |
| Comandante emprega força violenta contra subordinado em crise grave | somente sob proporcionalidade e direitos (M) | mantém instituto CPM42 PU em Q constitucional | limites absolutos e impossibilidade de tortura |
| CPM35 aplicado com pena base mínima | A deveria criar dispositivo de dosimetria claro | B deve resolver ambiguidade art35/73/76 | maioria e divergência STM, STF Tema158 |
| Mesmo evento antes/depois da lei modernizadora | regras constitucionais de lex mitior | idem | efeitos benignos retroativos, vedação a retroatividade gravosa |

## 5. Regras de integridade e continuidade

**Nenhuma escolha ratificada:** A e B são meramente demonstrativas e não passaram F6 concordância jurídica, F7 testes contra casos reais completos, F8 revisão adversarial ampla nem F9 integração. **A entrada de alterações M é consciente e sinalizada**, sem equipará-las a correção editorial. Discussão de jurisdição, tratados e hierarquia depende de outros módulos; dispositivos do CP e CPM continuam vigentes conforme fontes oficiais consultadas.

**FEITO:** 4 unidades CPM46–47; acesso a acórdão reproduzido integral STM 7000232 com votos e páginas; Tema158 verificado; nove dispositivos demonstrativos em cada alternativa e concordância em 16 relações; novas Q 0033–0035.

**PENDENTE:** retroatividade e prazo de adaptação; história 1969/2023 original DOU; validade constitucional específica da coação CPM40 e comando CPM42 PU; jurisprudência abrangente de erro e excesso; efeito da norma de qualidade do art47 em **crimes militares específicos**; efeito preciso do CP66 e CPM73/76; texto integral de demais excludentes e dosimetria para comparação exaustiva.

**PRÓXIMO:** corrigir propostas A/B com revisão por artigo de tipo militar hierárquico, conduzir testes de 10 fatos sob cada texto e direito vigente, indicar minutas de transição **apenas se o usuário deliberar sobre arquitetura**, ou manter Q e aprofundar penal M03 sem depender da seleção A/B.

**Coordenação:** T01 (regras de remissão e DEC-016), T02 (garantias), T16 (efeitos civis), T25.M02/M03/M06, T26/27 (processo e execução), T45 (disciplina/comando), T23/T47 (tratados).
