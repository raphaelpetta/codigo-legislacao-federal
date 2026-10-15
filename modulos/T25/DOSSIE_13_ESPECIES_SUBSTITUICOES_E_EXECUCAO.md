# T25.M03 — Dossiê 13: espécies penais, substituições e execução inicial

**Data de corte:** 15/10/2026, Brasília. **Issue [#31](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/31)**; **PR [#32](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/32)**, `draft`; branch `modulo/T25-parte-geral-f0-f1`. **Módulo principal:** T25.M03; interfaces T25.M01/M02, T26 (ação penal/competência), T27 (execução) e T01/T02/T45. **Fases:** F1 (inventário), F2 (concordância funcional), F3 (precedentes delimitados), F4 (testes jurídicos com tipos concretos). **NENHUM** texto normativo aprovado, nenhum C0-J ou M ratificado, sem merge à `main`.

## 1. Base documental e abrangência comprovada

- [Câmara — Código Penal comum compilado DL 2.848/1940](https://www2.camara.leg.br/legin/fed/declei/1940-1949/decreto-lei-2848-7-dezembro-1940-412868-normaatualizada-pe.html), **arts.32–58**, consultados em 15/10/2026, incluindo CP 163 (dano simples), 167 (ação penal) e 77 (sursis) como interfaces de teste.
- [Câmara — Código Penal Militar compilado DL 1.001/1969](https://www2.camara.leg.br/legin/fed/declei/1960-1969/decreto-lei-1001-21-outubro-1969-376258-normaatualizada-pe.html), **arts.55–68**, com interfaces **84–88 (sursis)** e **187 (deserção)**. Lei 14.688/2023 (DOU 21/09/2023, vigor 60 dias após publicação) **revogou** CPM 55 alíneas f/g, art.60, 64 e 65, e alterou hipóteses de sursis em art.84. A reconstrução da forma impressa de 1969 e de eventuais retificações de 2023 **não** foi feita nesta rodada.
- [CF/1988, art.5º XLVI–XLIX](https://www4.planalto.gov.br/legislacao/legis-federal/constituicao), individualização, integridade do preso e vedação de morte **ressalvada guerra declarada**. A proposta independente de nova CF não é direito vigente nem foi importada.

[Inventário `INVENTARIO_ESPECIES_CP32_58_CPM55_68_CICLO13.csv`](INVENTARIO_ESPECIES_CP32_58_CPM55_68_CICLO13.csv): **41 artigos por numeração**, sendo CP32–58 = **27** e CPM55–68 = **14**, divididos em **107 posições descritivas** com identificadores não repetidos; marca posições revogadas/vetadas. **Limite:** as subunidades foram selecionadas por risco, o `resumo_funcional` de cada posição caput não reproduz literalmente a norma. Não se alega cobertura textual exaustiva por inciso nem concordância C0-T/C0-J. A inclusão histórica de um número revogado **não ressuscita** sua força jurídica.

[Concordância funcional `CONCORDANCIA_ESPECIES_SUBSTITUICOES_CICLO13.csv`](CONCORDANCIA_ESPECIES_SUBSTITUICOES_CICLO13.csv): **25 pares/temas** classificados Q, com indicação de diferença e risco material. Não são 25 revogações nem 25 dispositivos equivalentes.

## 2. Diferença estrutural fundamental: duas operações chamadas 'substituição'

| Tema | CP comum | CPM | Efeito de codificação |
|---|---|---|---|
| Espécies de pena | CP32: privativa de liberdade; restritiva de direitos; multa | CPM55: morte, reclusão, detenção, **prisão**, **impedimento**; alíneas f/g revogadas em 2023 | Uma tabela de nomes única pode omitir ou criar penas |
| Pena alternativa ao cárcere | CP43–48 e **CP44**: prestação pecuniária, de serviços, interdição, limitações e condições de substituição | Art.59 CPM: **conversão de reclusão/detenção em pena de prisão**, que **continua privativa de liberdade** | **Não** mapear CP44 para CPM59 como mesmo benefício |
| Limites e requisitos | CP44 I: pena aplicada até **4 anos** em crime sem violência ou grave ameaça, ou qualquer quantum de culpa, mais incisos II–III e §§ | CPM59: pena de reclusão/detenção até **2 anos**, aplicada **a militar**, **quando não cabível o sursis**, com recinto militar ou estabelecimento penal militar | M se ampliar art44 ao militar; também não trocar praça por civil inadvertidamente |
| Cumprimento por sujeito | CP33 regimes fechado/semiaberto/aberto e regras CP34–40 | CPM59 separa oficial e praça; CPM61 pena superior a dois anos de militar; **CPM62 civil condenado pela Justiça Militar** cumpre em estabelecimento civil e sujeita-se ao regime comum com benefícios | Distinguir **espécie/fase de condenação** de **regime de cumprimento** e beneficiário |
| Suspensão condicional da execução | CP77, em regra pena até 2 anos com condições, subsidiária à substituição do art44 (CP77 III) | CPM84 alterado em 2023: prazos distintos para reclusão e detenção; CPM88 exclui classes de crimes, inclusive **deserção** | Só olhar duração da pena induz falsa concessão de sursis |
| Sancionamento em tempo de guerra | CF impede pena de morte, **salvo guerra declarada**; CP comum não a comina | CPM55 a,56–57 disciplinam morte; 57 PU prevê imediatidade excepcional em operação de guerra | Exigir controle constitucional/direitos humanitários, não usar em tempo de paz |

**Precedentes que confirmam a diferença de efeito:**
1. [STF, HC 94.083/DF, Segunda Turma, 09/02/2010, Informativo 574](https://stf.jus.br/arquivo/informativo/documento/informativo574.htm): a substituição por restritivas de direitos do **CP art.44** não se aplica simplesmente a crimes militares, diante de regime próprio do CPM art.59.
2. [STJ, CC 161.898/MG, Terceira Seção, 13/02/2019](https://scon.stj.jus.br/SCON/jurisprudencia/toc.jsp?livre=%28CC+INPATH%28CLAS%29+AND+161898+INPATH%28NUM%29%29): a ampliação da competência militar pela Lei 13.491/2017 pode produzir efeitos materiais desfavoráveis; **inaplicabilidade da substituição CP44** figura entre os exemplos. Aplicação imediata da regra de competência exige proteção da norma penal material mais benéfica ao tempo do fato; **não** chancelou livre combinação de segmentos de leis.
3. [STM, Apelação 7000286-26.2024.7.00.0000, julgamento 24/10/2024, publicada em revista 29/01/2026](https://revista.stm.jus.br/index.php/periodicos/article/view/jurisprudencia-09-v34-n1-2024): em caso de estelionato militar (CPM251), deu provimento ao recurso do MPM contra a substituição pelo art.44 do CP. Fonte **resumo/ementa institucional**, não leitura completa de todos os votos desta apelação.

[`JURISPRUDENCIA_SUBSTITUICAO_PENAL_CICLO13.csv`](JURISPRUDENCIA_SUBSTITUICAO_PENAL_CICLO13.csv) preserva processo/data/alcance/nível de exame; três decisões **não** bastam para afirmar solução vinculante irrestrita para todos os crimes e todas as pessoas, particularmente diante de CPM62 e da competência.

## 3. Diferenças jurídicas adicionais

### 3.1. Direitos na execução, saúde e detração

CP37–40 fazem referência expressa à mulher presa, direitos e integridade, trabalho remunerado com previdência e legislação penitenciária. CPM61–62 tratam estabelecimento e benefícios comuns para certos condenados; CPM66–68 doença mental, detração e transferência. O **direito fundamental de integridade do preso (CF5 XLIX) não cessa em prisão militar**, ainda que normas infraconstitucionais descrevam estabelecimentos diferentemente. Não transformar silêncio setorial em exclusão de direitos. **T27 deve conduzir** harmonização penitenciária e normas de saúde.

### 3.2. Penas e dispositivos revogados em 2023

Lei 14.688/2023 revogou alíneas **f/g do CPM55** e **CPM60,64,65**. Penas de suspensão do exercício do posto/graduação/cargo/função e de reforma deixaram de ser cominadas por esses artigos. No entanto, **CPM63 impedimento** e **CPM59 pena de prisão** continuam na compilação. Conservar posição histórica é útil para concordância e intertemporalidade; **não a incorporar como vigente**. A reforma de 2023 pode exigir conferir outras penas acessórias ainda previstas no CPM e efeitos funcionais em T45.

### 3.3. Aparente descompasso CP44 × CP54

O [CP art.54](https://www2.camara.leg.br/legin/fed/declei/1940-1949/decreto-lei-2848-7-dezembro-1940-412868-normaatualizada-pe.html) mantém a expressão de substituição para penas privativas **inferiores a um ano** ou crimes culposos, ligada ao desenho de 1984; o **art.44 atualizado em 1998** prevê possibilidade de substituição até **quatro anos** em determinadas condições. Essa coexistência demanda análise de **regra geral/especial, lex posterior e técnica legislativa**. É impróprio simplesmente codificar a limitação menor de CP54 como prevalente e eliminar ganhos do art.44; igualmente não afirmar revogação expressa de CP54 sem prova. **Q: demanda saneamento textual intertemporal e concordância de efeitos.**

### 3.4. Morte, guerra e garantias constitucionais

**CPM55–57** trazem pena de morte e execução em contextos próprios; a **CF5 XLVII a** só admite sua exceção em **guerra declarada** segundo CF84 XIX. A cláusula especial **CPM57 parágrafo único** permite execução imediata em zona de operações quando interesse de ordem/disciplina o exigir. **Essa regra exige auditoria constitucional, devido processo, tratados e direito humanitário de alto risco**; não declarar recepção/validade global, revogação automática nem estendê-la a tempos de paz. Mudar/suprimir qualquer hipótese é ato de conteúdo material, não edição C1.

### 3.5. Civil perante Justiça Militar

**CPM62** confere ao civil condenado pela Justiça Militar cumprimento em estabelecimento civil e regime conforme a legislação penal comum, com seus benefícios e concessões. Isso **não resolve automaticamente a incidência do art.44 CP na sentença penal militar**, pois há diferença entre benefício de execução e **substituição da espécie da pena no título condenatório**. A prática depende do tipo penal militar, status do agente, competência e marcos temporais. O teste de deserção abaixo **exige militar**; não extrapolar CPM187 para civil.

## 4. Dois tipos penais concretos e oito testes — sem sentenças fabricadas

A matriz [`CASOS_TIPOS_REAIS_SUBSTITUICOES_CICLO13.csv`](CASOS_TIPOS_REAIS_SUBSTITUICOES_CICLO13.csv) mantém **um cabeçalho CSV uniforme** e oito cenários funcionais (quatro ligados a cada tipo), com pressupostos explícitos e períodos hipotéticos 2022/2026. Os fatos não correspondem a processos reais.

| Aspecto | CP art.163 caput — dano simples | CPM art.187 — deserção |
|---|---|---|
| Sujeito e fato básico | Destruir, inutilizar ou deteriorar coisa alheia; exemplo: objeto privado sem qualificadora, sem violência | Militar sem licença ausenta-se da unidade/lugar designado **por mais de oito dias**; exemplo usa praça ativa |
| Pena abstrata conferida | **Detenção 1 a 6 meses OU multa** | **Detenção 6 meses a 2 anos; agravamento se oficial** |
| Natureza/execução | Multa **originária** como alternativa do tipo; se determinada pena privativa, examinar CP44 com seus requisitos | Pena privativa; **CPM88 II a** exclui sursis na deserção; **CPM59** disciplina conversão em prisão militar de pena até 2 anos quando o sursis não é cabível |
| Perspectiva temporal | Fato de **15/10/2026**, controlar CP163, 44 e 167; variação de 2022 pede cotejo da versão do fato | Fato de **15/10/2026**, após reforma de 2023; variante de 2022 exige versão anterior de CPM84 e controle das regras materiais |
| Processual/civil | **CP167**: dano simples é em regra ação penal privada; reparar objeto pode repercutir em civil e em institutos penais diversos | Tipicidade própria exige status militar e ausência objetiva superior a oito dias, além de culpabilidade, procedimento militar, eventual exclusão de ilicitude |
| Consequência de unificação | Atenção ao direito à multa originária e, se pena detentiva, alternativas do art44 | Aplicar CP44 diretamente mudaria potencialmente **prisão por pena não privativa**, material **M** |

**Exemplo de dosimetria sem fingir sentença:** se hipoteticamente a pena final de **deserção** for **um ano de detenção**, para praça **ainda militar** e sem causa que modifique situação, o **CPM88 II a impede sursis** e o CPM59 indica a **conversão em pena de prisão militar**, não prestação comunitária. Para dano simples, a pena abstrata oferece **multa originária**, distinta de converter uma hipotética detenção de quatro meses em restritiva; essa última depende de CP44 I–III, antecedentes, reincidência e suficiência, logo **não se afirma concessão automática**.

**Variações programadas:** 2022 versus 2026 (temporais), dano com multa originária, detenção de 4 meses sob condições favoráveis, subsidiariedade do sursis, deserção com um ano hipotético, porta de dois anos/agravamento, tentativa impossível de civil figurar como autor de deserção sem qualidade militar. A fonte não autoriza criar pena superior a dois anos a partir do caput CPM187 para praça sem causa específica; **toda condição de agravamento requer regra de tipo e prova**.

## 5. Novas fichas de risco e arquitetura A2/B2

- **PROB-T25-0044:** nomenclatura `substituição` abrange conversões com efeitos opostos (CP44 direitos versus CPM59 prisão); risco de ampliar encarceramento ou conceder benefício inexistente. M se alterado.
- **PROB-T25-0045:** CP32 vs CPM55 e penas especiais, incluindo pena de morte exclusivamente no espaço constitucional de guerra declarada; vigência e categoria jurídica.
- **PROB-T25-0046:** CP44/54 aparente tensão interna por versões de 1984/1998; preservar resultado de norma posterior até estudo definitivo; não declarar revogação não documentada.
- **PROB-T25-0047:** CPM55 f/g e arts.60,64,65 revogados em 2023, e mudanças do CPM84; necessidade de auditoria histórica e não reintrodução.
- **PROB-T25-0048:** civil condenado pela Justiça Militar (CPM62) versus militar condenado com reclusão/detenção (CPM59,61); regime de execução não equivale automaticamente a substituição judicial na sentença.
- **PROB-T25-0049:** CPM88 veda sursis em deserção apesar da pena curta; a classificação de benefício não se pode deduzir da duração isoladamente.
- **PROB-T25-0050:** crimes militarizados por Lei 13.491/2017, CP44, retroatividade benigna e competência, segundo STJ CC161898; não fabricar uma `lex tertia`.
- **PROB-T25-0051:** transferência, saúde, detração, trabalho e direitos na execução exigem interface T27 e CF5 XLIX.
- **PROB-T25-0052:** imediatidade da execução de morte em operações de guerra no CPM57 PU: constitucionalidade e direito humanitário ainda Q de altíssima sensibilidade.

**Consequências para os textos A2/B2:** A2 como núcleo geral **precisaria de exceção expressa ou decisão M** para CP44 versus CPM59/88; B2 como subparte militar conserva separação de estrutura, mas não pode descuidar de direitos da pessoa presa, do CPM62, nem da legalidade das penas revogadas. A escolha de arquitetura **continua Q**.

## 6. Protocolo de aceitação e continuidade

**FEITO:** **41 artigos** identificados, **107 posições descritivas** não repetidas, **25 confrontos Q**, **2 tipos reais e 8 cenários**, **3 referências judiciais** com grau de fonte e limites. Tudo apenas em branch; não há reforma `M` aprovada nem `C0-J`.

**PENDENTE:** histórico autenticado CPM 1969/1978/2023, CP 1984/1998, redação e alcance de CP54, profundidade jurisprudencial de CPM62 (civil), lei de execução/CPPM, penas acessórias, medidas de segurança, inimputabilidade, pena de morte em guerra e normas internacionais. Ausência de diagnóstico empírico sobre benefícios. Não extrapolar precedentes a toda criminalidade castrense. NENHUMA minuta de lei promulgável pronta.

**PRÓXIMO (Ciclo14):** testar integração penal material e executória por **matriz das portas de escolha** `espécie → pena-base → causas → pena final → substituição → sursis → estabelecimento → execução` para CP163 e CPM187, com jurisprudência e critérios temporais. Abrir análise de **CPM art.84–88, CP art.77–82 e LEP** em articulação T27, antes de decidir se o núcleo compartilhado A2 poderá incorporar regime alternativo militar (M) ou se B2 o manterá expressamente (Q). Efectuar prova C0-J frase por frase apenas quando íntegra de regras e efeitos estiver disponível.

**Governança:** `governanca/18_PROTOCOLO_CONTINUIDADE_POR_RODADA.md`; CF em elaboração é independente e **não** é a Constituição vigente.
