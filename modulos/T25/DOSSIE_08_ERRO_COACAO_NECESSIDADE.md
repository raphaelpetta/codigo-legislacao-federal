# T25 — Dossiê 08 | Imputação e exclusão de responsabilidade: CPM 35–45 × CP 20–25

**Corte:** 14/10/2026. **Módulos:** T25.M02, interfaces M01/M03 e T26/T27/T45. **Issue:** [#31](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/31); **PR rascunho:** [#32](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/32). **Baseline `main` de abertura:** `16fba172c875c7a0de388288fe70005c944021d6`. **F1:** texto consolidado e 11 subunidades CPM 41–45 indexadas; **F2:** comparação de consequências por 20 cenários; **F3:** jurisprudência seletiva com limitações de acesso; **F4:** alternativas `Q` não decididas. Nenhum texto do CLF aprovado e nenhuma validação `C0-J` ou mudança material `M` ratificada.

## 1. Fontes efetivamente examinadas e controles de proveniência

- [Senado — DL 1.001/1969, CPM, texto consolidado](https://legis.senado.leg.br/norma/524625/publicacao/34620431), arts. **35–46**, e [Câmara — CPM atualizada](https://www2.camara.leg.br/legin/fed/declei/1960-1969/decreto-lei-1001-21-outubro-1969-376258-normaatualizada-pe.html), arts. 35–47. O **art.46** aparece apenas como interface necessária para análise completa do excesso; não incluído no inventário principal desta rodada.
- [Planalto — DL 2.848/1940, CP compilado](https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848compilado.htm), arts. **20–25**; comparação seletiva com [Câmara — CP atualizado](https://www2.camara.leg.br/legin/fed/declei/1940-1949/decreto-lei-2848-7-dezembro-1940-412868-normaatualizada-pe.html).
- [Lei 14.688/2023, Planalto](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14688.htm): alterou expressamente **CPM art.38 §2º**, preservando crítica à ordem manifestamente criminosa. A lei registra veto de um **parágrafo proposto para o art.42**, mas a compilação vigente ainda contém o **parágrafo único preexistente do art.42** sobre comando em perigo/calamidade. **Não afirmar sua revogação pelo veto**, nem presumir constitucionalidade automática da regra que permaneceu.
- Jurisprudência: [STM, Apelação 7000232-60.2024.7.00.0000 publicada na Revista do STM em 29/01/2026](https://revista.stm.jus.br/index.php/periodicos/article/view/jurisprudencia-05-v34-n1-2024); [STM, Apelação 7000206-62.2024.7.00.0000, j. 14/11/2024, ementa na base do STM](https://jurisprudencia.stm.jus.br/consulta.php?fq_assunto_pesquisa__2=SUSPENS%C3%83O+CONDICIONAL+DA+PENA&fq_assunto_pesquisa__3=DIREITO+PENAL+MILITAR&fq_assunto_pesquisa__4=SUSPENS%C3%83O&fq_data_autuacao=d%282024%2F04%29&q=%2A&q_or=&rows=25&search_fil=&search_filter_option=jurisprudencia&start=0); [Súmula STM 3, página institucional](https://www.stm.jus.br/1-instancia/4-cjm-mg/212-stm/cat7-servicos/stm-servicos-judiciais); [STF, ADPF 779 (ementa/dispositivo)](https://portal.stf.jus.br/constituicao-supremo/artigo.asp?abrirArtigo=226&abrirBase=CF).
- **Status probatório:** não foi lida a íntegra de todos os acórdãos, nem produzida amostra representativa das decisões. Fontes jornalísticas, indexadas ou ementas não se substituem pelo voto. **Não** foram localizados e examinados precedentes vinculantes específicos que solucionem de modo geral a constitucionalidade do CPM 35/40/42PU/45PU.

## 2. Inventário do subciclo

[`INVENTARIO_CPM_ART41_45_CICLO08.csv`](INVENTARIO_CPM_ART41_45_CICLO08.csv) contém **11 posições**: art.41 caput (1), art.42 caput + quatro incisos + parágrafo único (6), arts.43 e 44 caput (2), art.45 caput e parágrafo único (2). Unidade de auditoria **descritiva**, não espelho literal nem declaração de exaustividade histórica. O CPM 35–40 foi indexado no ciclo 07 e é confrontado nesta rodada, sem duplicar inventário.

[`MATRIZ_COMPARATIVA_ERRO_COACAO_NECESSIDADE_CICLO08.csv`](MATRIZ_COMPARATIVA_ERRO_COACAO_NECESSIDADE_CICLO08.csv): **20 casos hipotéticos**, com condições, efeitos prováveis sob a literalidade das leis, risco de integração, fontes, perguntas de defesa e limites de prova. Essas descrições **não representam julgamentos reais** nem estabelecem resultados inevitáveis em cada processo.

## 3. Comparação por consequência jurídica (F2)

| Instituto | Regime CP (1984 e alterações) | Regime CPM (1969, com 2023 parcial) | Risco de equivalência |
|---|---|---|---|
| Erro sobre ilicitude | CP 21: inevitável isenta de pena; evitável admite redução 1/6–1/3 | CPM 35: erro de direito **escusável**, fora de crime contra dever militar, pode atenuar/substituir pena, sem isenção geral expressa nesse artigo | **Muito alto:** núcleo do princípio da culpabilidade; migração automática altera consequência e requisito |
| Erro de elemento do tipo e descriminante fática | CP 20 caput: exclui dolo; culpa se prevista; §1º: erro plenamente justificado de descriminante; §2º terceiro | CPM 36: exige erro plenamente escusável para isenção; §1º responsabiliza culpa se erro culposo e tipo admite; §2º terceiro | **Muito alto:** estrutura e causalidade da exclusão do dolo/pena não são redacionalmente iguais |
| Erro sobre vítima/bem | CP 20 §3º e regras de concurso posteriores | CPM 37 e §§1º–2º, com remissão ao art.79 | **Alto:** há efeitos sobre elementares, culpa e concurso que exigem recorte de norma correlata |
| Coação e ordem | CP 22: só punível autor da coação/ordem se irresistível ou estrita obediência a ordem não manifestamente ilegal | CPM 38 a,b, §§1º–2º: ordem **direta em matéria de serviço**; superior responde; **ordem manifestamente criminosa** ou excesso também torna inferior punível (2023) | **Crítico:** não igualar `manifestamente ilegal` e `manifestamente criminosa` sem reconstruir prova e dolo |
| Coação contra dever militar | CP 22 não traz ressalva militar geral | CPM 40: em crime de violação de dever militar, coação irresistível invocável apenas se física ou material | **Crítico:** ameaça moral séria pode ter resultado jurídico diferente; confrontar CPM 39 e limites constitucionais |
| Necessidade exculpante | CP 24 é enunciado de estado de necessidade; inexigibilidade tem construção dogmática própria | CPM 39 explicita **ausência de culpabilidade** sob perigo certo e atual, inescapável, para direito próprio ou pessoa ligada, mesmo com direito sacrificado superior | **Crítico:** causa de inculpabilidade ≠ exclusão de ilicitude; terceiros, responsabilidade civil e concurso podem diferir |
| Necessidade justificante | CP 23 I e 24 exigem perigo atual, inevitabilidade, sacrifício inexigível e ausência de dever legal de enfrentar | CPM 42 I e 43 exigem, entre outros, mal causado **consideravelmente inferior** ao mal evitado e ausência de dever legal de arrostar perigo | **Crítico:** não colocar CP 24 e CPM 43 como correspondência C0-J |
| Coação violenta em emergência militar | Sem enunciado específico equivalente nos CP 20–25 | CPM 42 PU: excludente especial de comandante, meios violentos em grave perigo/calamidade para manobras urgentes | **Crítico:** alcance, proporcionalidade, ordem legítima e direitos humanos; veto de 2023 não extinguiu a regra já existente |
| Legítima defesa | CP 23 II e 25; art.25 PU inclui hipótese com refém, sujeita ao caput | CPM 42 II e 44, com requisitos de agressão injusta atual/iminente e meios moderados | **Potencial núcleo comum**, preservados sujeitos, contexto e limites constitucionais; ADPF 779 afasta tese de honra na interpretação do CP |
| Excesso | CP 23 PU: excessos doloso e culposo puníveis | CPM 45: excesso culposo se modalidade prevista; PU: excesso escusável por surpresa/perturbação não punível; CPM 46 pode atenuar excesso doloso | **Crítico:** subunidades adicionais afetam pena ou punibilidade; não apagar art.45 PU/46 ao reunir art.23 |

### 3.1. Erro escusável não equivale a dolo provado

O **CPM art.35**, ao permitir apenas mitigação/substituição de pena em erro escusável e excluir dessa via crimes contra dever militar, levanta dúvida difícil à luz do princípio de culpabilidade: é lícito punir o agente sem possibilidade de consciência da ilicitude? A questão não se resolve simplesmente pela palavra `escusável`. Há dois níveis: (i) a **literalidade do art.35**, contrastante com CP art.21; (ii) eventual **interpretação sistemática e constitucional** que possa produzir resultado diverso daquele sugerido por sua redação. Não declarar sem acórdãos completos que a jurisprudência já reconheceu ou negou hipótese supralegal geral.

**Caso concreto de tensão jurisprudencial:** a ficha da [Apelação STM 7000232-60.2024.7.00.0000](https://revista.stm.jus.br/index.php/periodicos/article/view/jurisprudencia-05-v34-n1-2024) tem título sobre `erro de direito inescusável` e, na exposição do desfecho, indica cabimento de **aplicação do art.35 para adequar a pena**. **Aparente tensão entre rótulo da ementa e conclusão**, que exige inteiro teor e exame dos votos, **não** deve ser simplificada como absolvição por erro inevitável, tampouco se deve ignorar o cabimento de mitigação descrito na fonte.

### 3.2. Obediência militar não pode legitimar ordem manifestamente criminosa

O CPM art.38 §2º na redação da **Lei 14.688/2023** determina que a ordem de ato manifestamente criminoso ou o excesso tornam **também punível o subordinado**. A redação geral CP art.22 usa formulação da ordem **não manifestamente ilegal**, diferença que requer comparação de hipóteses. O CPM art.41 prevê **atenuação** em condições expressas que envolvem coação, ordens e sacrifício do direito ameaçado. A redação de sua referência à **ordem não manifestamente ilegal** é interpretativamente sensível: não inferir dela, isoladamente, que ordem manifestamente criminosa autoriza exculpação; tampouco fingir que o art.41 não existe.

**Limite constitucional necessário à futura redação:** nem disciplina ou hierarquia são salvo-conduto para tortura, violência intencional proibida, execução extrajudicial e ordens manifestamente criminosas. **A regra da culpabilidade individual** não deve ser confundida com imunidade de comando nem com responsabilidade objetiva do subordinado.

### 3.3. Art.40 e art.39 têm de ser analisados juntos

A tese de que o CPM art.40, nos crimes contra dever militar, impede a invocação de coação **moral**, não autoriza o salto de afirmar que qualquer ameaça moral torna condenação obrigatória. O art.39 tem cláusula própria de **estado de necessidade exculpante** baseada em inexigibilidade, que pode precisar exame autônomo segundo os fatos e sua relação com o dever, sem decidir aqui sua compatibilidade ou abrangência em todo crime militar. **É igualmente incorreto** presumir que todo problema familiar ou financeiro satisfaz automaticamente o perigo certo e atual.

A jurisprudência selecionada fornece cenário prático: [STM Súmula 3](https://www.stm.jus.br/1-instancia/4-cjm-mg/212-stm/cat7-servicos/stm-servicos-judiciais) rejeita alegações pessoais/familiares **desacompanhadas de prova** em deserção e insubmissão; [Apelação 7000206-62.2024.7.00.0000](https://jurisprudencia.stm.jus.br/consulta.php?fq_assunto_pesquisa__2=SUSPENS%C3%83O+CONDICIONAL+DA+PENA&fq_assunto_pesquisa__3=DIREITO+PENAL+MILITAR&fq_assunto_pesquisa__4=SUSPENS%C3%83O&fq_data_autuacao=d%282024%2F04%29&q=%2A&q_or=&rows=25&search_fil=&search_filter_option=jurisprudencia&start=0) analisa dificuldades financeiras/pessoais sem perigo extraordinário comprovado. **Não transformar a súmula em vedação absoluta de defesa, inversão automática do ônus final da acusação, ou precedente vinculante do STF.**

### 3.4. Justificante, exculpante e reflexos para terceiros

O **CPM art.39** expressamente exclui a **culpabilidade**, enquanto os arts.42–43 disciplinam causas justificantes. A diferenciação é material: nem todo fato de agente não culpável é lícito perante terceiros. A reunião em dispositivo genérico `estado de necessidade` sem distinguir consequências **pode afetar responsabilidade civil, participação, legítima defesa de terceiro e limites de risco permitido**. Não concluir cada efeito sem conferir legislação civil/processual e hipóteses concretas.

O **CPM art.43** é mais explícito na desigualdade entre males (consideravelmente inferior) que a fórmula CP art.24. A alternativa de unificar exige declarar se o legislador quer manter, ampliar ou restringir justificações. Esses efeitos não podem ficar subentendidos.

### 3.5. Art.42 PU e art.45 PU: especiais pouco visíveis

- **Art.42 PU:** autoriza exclusão de crime em condições excepcionais ligadas a comando e iminência de perigo/calamidade, envolvendo compelir subordinados **por meios violentos**. A redação exige exame frontal: necessidade real, urgência, adequação, intensidade da força, vedação de tortura e maus-tratos e salvaguardas humanitárias. A alternativa moderna mais restritiva seria **M**, não `correção de estilo`. A proposta de parágrafo vetada em 2023 é distinta da manutenção do parágrafo original.
- **Art.45 PU:** registra excesso **escusável** por surpresa ou perturbação de ânimo que afasta punição. Não existe equivalência literal no CP art.23 PU. Uma nova Parte Geral não deve suprimir silenciosamente defesa aplicável, mas também não deve converter `perturbação de ânimo` em justificação geral para agressões desproporcionais. [STF ADPF 779, 2023](https://portal.stf.jus.br/constituicao-supremo/artigo.asp?abrirArtigo=226&abrirBase=CF) fornece limite constitucional da tese da honra na interpretação dos dispositivos do CP; **não é acórdão que julgou especificamente o CPM art.45 PU**.
- **Art.46** (fora da faixa de inventário): atenuação possível de pena por excesso doloso; precisa aparecer na comparação final. Este item impede declarar fechamento de todo o regime do excesso apenas pelos arts.41–45.

## 4. Decisões alternativas: quadro para eventual proposta, sem ratificação

| Família | Texto/efeitos atuais | Hipótese de preservação | Hipótese de reforma **M** a testar |
|---|---|---|---|
| Erro de proibição | CP21 × CPM35 (consequências diferentes) | manter exceção militar com fundamentação constitucional verificável | unificar **isenção por erro inevitável** sob reserva de deveres especiais de diligência na avaliação da evitabilidade, não como presunção irreversível de culpabilidade |
| Erro de tipo/fato | CP20 × CPM36 | manter formulações por subsistema | unificar exclusão de dolo com responsabilidade culposa só quando prevista, revendo erro descriminante |
| Ordem e coação | CP22 × CPM38–41 | conservar diferença dentro do módulo militar, sob controle | proteger expressamente recusabilidade de ordens criminosas e construir critério de inexigibilidade excepcional em coação moral |
| Necessidade | CP24 × CPM39/43 | manter justificante/exculpante separados | construir núcleo geral de justificação/exculpação com diferenciação de efeitos e parâmetros militares restritos |
| Excesso | CP23 PU × CPM45 PU/46 | manter benefícios militares específicos | reexaminar excesso escusável para aplicação geral, ou justificar delimitação e definir rigoroso padrão de escusabilidade |
| Comando em emergência | CPM42 PU | conservar como exceção especial auditada | limitar força e especificar atos vedados e controle de necessidade; **sem introduzir punição retroativa** |

**Nota:** esta tabela faz recomendações de **agenda**, não sugere que as reformas M já foram escolhidas. Qualquer reforma exigirá versões completas, debate adversarial, estudos empíricos, proteção constitucional e decisão formal.

## 5. Problemas adicionais e fronteira documental

- **PROB-T25-0027:** regime do erro sobre elementos e descriminantes CP20 × CPM36–37; risco de tipicidade dolosa a partir de mera culpa no erro.
- **PROB-T25-0028:** CPM42 PU e violência de comandante em emergência; proporcionalidade, controles, direitos fundamentais e tratados.
- **PROB-T25-0029:** legítima defesa CPM44/CP25, excesso escusável CPM45 PU e extensão CPM46.
- **PROB-T25-0030:** atenuação CPM41, sua redação e relação com requisitos de erro de proibição, ordens e causas de exculpação.
- **PROB-T25-0031:** distinção de justificantes e exculpantes em regime codificado único: impactos civis/processuais e direito de defesa de terceiros.
- **PROB-T25-0032:** efeito da Súmula STM3 e dos julgados sobre **prova de exculpação**, sem comprometer presunção de inocência, contraditório ou devido processo.

**FEITO:** fonte consolidada CPM 35–46 e CP20–25 confrontada; **11** subunidades de CPM41–45 identificadas, **20** testes adversariais, **6** referências judiciais e seis problemas novos Q (0027–0032). **PENDENTE:** acórdãos completos, histórico autêntico de 1969/2023, jurisdição constitucional específica, CPM46–47 e relações materiais T16/T26/T27/T45, pesquisas de resultados empíricos e propostas de texto. **PRÓXIMO:** aprofundar CPM45–47 + erros e coação com ênfase em julgamento STM 7000232 e controle constitucional da exigibilidade nos arts.35/40/42; depois simular redações concorrentes do núcleo e subparte militar, todas expressamente como `M proposta` se efeitos forem diferentes.
