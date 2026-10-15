# T25.M03 — Dossiê 12: aplicação e cálculo da pena no CP e no CPM

**Sessão e corte:** 14/10/2026 (America/Sao_Paulo). **Issue [#31](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/31)**, **PR [#32 — draft](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/32)**, branch `modulo/T25-parte-geral-f0-f1`. **Main CLF à abertura:** `16fba172c875c7a0de388288fe70005c944021d6`. **F0:** foco T25.M03, subtema aplicação e dosimetria de penas. **F1:** 19 artigos (CP 59–68, CPM 69–77), 86 posições descritivas. **F2:** 22 relações avaliadas. **F3:** 5 referências STF/STJ/STM com limites. **F4:** 10 simulações aritméticas condicionadas. **Não há C0-J, C1 ou M aprovados, minuta final ou revogação.**

## 1. Fontes, datas e limites

- [Câmara, CP atualizado DL 2.848/1940 arts.59–68](https://www2.camara.leg.br/legin/fed/declei/1940-1949/decreto-lei-2848-7-dezembro-1940-412868-normaatualizada-pe.html). **Alterações recentes relevantes:** [Lei 15.159/2025](https://www2.camara.leg.br/legin/fed/declei/1940-1949/decreto-lei-2848-7-dezembro-1940-412868-normaatualizada-pe.html) incluiu **art.61 II m** (instituição de ensino); [Lei 15.160/2025](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15160.htm) mudou **art.65 I** (exclui atenuante etária no caso legal de violência sexual contra a mulher). Verificar as datas de incidência em fatos concretos.
- [Câmara, CPM atualizado DL 1.001/1969 arts.69–77](https://www2.camara.leg.br/legin/fed/declei/1960-1969/decreto-lei-1001-21-outubro-1969-376258-normaatualizada-pe.html); [Lei 14.688/2023](https://www2.camara.leg.br/legin/fed/lei/2023/lei-14688-20-setembro-2023-794728-normaatualizada-pl.html) alterou **CPM art.70 II h** e **art.77 caput/PU**. A Câmara registra DOU em 21/09/2023 e vacatio de 60 dias; falta cotejo de eventuais retificações e de conflitos intertemporais por cada subunidade.
- Registros analíticos: [`INVENTARIO_DOSIMETRIA_CP59_68_CPM69_77_CICLO12.csv`](INVENTARIO_DOSIMETRIA_CP59_68_CPM69_77_CICLO12.csv), **45 subunidades CP + 41 CPM = 86 IDs**, com descrições; [`CONCORDANCIA_CRITICA_DOSIMETRIA_CICLO12.csv`](CONCORDANCIA_CRITICA_DOSIMETRIA_CICLO12.csv), 22 relações `Q`. Não são 86 transcrições literais nem demonstração de cobertura histórica integral. Não usar `C0-T` da pesquisa dos CP arts.1–12 como prova de C0-J desta faixa.

## 2. Achados materiais que impedem fusão editorial automática

### 2.1. Pena-base CP59 × CPM69

O CP59 considera expressamente **culpabilidade, antecedentes, conduta social, personalidade, motivos, circunstâncias, consequências e comportamento da vítima** e confere ao juiz decisões sobre **espécies de pena, quantum, regime inicial e substituição**. O CPM69 menciona gravidade, personalidade, **intensidade do dolo/grau de culpa, extensão do dano ou perigo, meios, execução, tempo/lugar, antecedentes e atitude de insensibilidade, indiferença ou arrependimento**; §1 escolhe pena alternativa cominada e §2 fixa limites salvo art76.

**Consequência:** supressão/adição de um vetor judicial altera justificação do quantum e eventual vedação de bis in idem; CP60 tem multa e substituição específicas **sem equivalente nesta faixa do CPM**, mas isso NÃO prova que todo o CPM não disponha de sanções/multas. Deve ser investigado juntamente com CPM arts.55–65, 58, 63, regras de penas e execução.

### 2.2. Agravantes e reincidência

- **CP61 II m (2025):** agravamento por fato em dependência de instituição de ensino, sem paralelo literal em CPM70; **introduzir no militar** não seria edição sem efeito (**M**).
- **CP61 II f × CPM70:** proteção doméstica/violência contra mulher no CP, especificidade funcional militar CPM70 II c,l,m,n,o e parágrafo único; não substituir os róis cegamente.
- **CP61 II h × CPM70 II h:** redações **diferentes**, porque CPM70 II h explicita pessoa com deficiência (2023), CP61 II h inclui categorias próprias. Não inventar reciprocidade automática de proteção.
- **CP63–64 × CPM71:** a reincidência depende de condenação definitiva anterior, mas **CP64 I menciona período de prova de sursis/livramento** no prazo depurador; CPM71 §1 não o enuncia. **CP64 II afasta crimes militares próprios e políticos**, enquanto CPM71 §2 menciona especificamente **crimes anistiados**. Unificar poderia alterar a própria existência da agravante, com efeito gravoso ou benigno conforme datas e natureza do delito.
- **CP62 agravantes de concurso de agentes:** sem cláusula idêntica nos **arts.69–77 CPM**; examinar regras de concurso militar em outros dispositivos (p.ex. CPM53) antes de alegar lacuna sistêmica.

### 2.3. Atenuantes e temporalidade

**CP65 I — Lei 15.160/2025:** a atenuante etária possui exceção específica para violência sexual contra mulher. **CPM72 I** não reproduz essa exceção; não considerar a mesma idade e a mesma categoria de crime automaticamente equivalentes.

**CP65 II — desconhecimento da lei; III c — coação resistível/ordem; III d — confissão:** o **CPM72 II** privilegia comportamento anterior meritório; **CPM72 III d** exige confissão de autoria antes desconhecida ou imputada a outrem; **CPM72 III e** considera rigor ilegal sofrido. Diferenças textuais relevantes; CP66 aceita atenuante judicial inominada. Não é válida a conclusão de que inexistem outras formas de mitigação militar: CPM41 e CPM35 são interfaces anteriores.

**CPM72 parágrafo único:** facultatividade especial em crimes com pena máxima abstrata de morte. Tal regra exige exame da excepcionalidade constitucional de pena de morte em guerra declarada e do próprio tratamento do processo; não suprimir sem estudo nem pressupor plena aplicação em qualquer tempo.

### 2.4. Três fases, quantum e limites

- **CP67 × CPM75:** ambos atribuem peso às circunstâncias preponderantes, mas CPM75 contém cláusula expressa de neutralização quando há equivalência.
- **CP68 caput × CPM77 caput (redação 2023):** três etapas similares: pena-base, atenuantes/agravantes, causas de aumento/diminuição. O **CPM77 parágrafo único (2023)** explicita que apenas causas especiais permitem ir além dos limites abstratos.
- **CPM73:** na ausência de fração especial legal, regra de **1/5 a 1/3** para agravantes e atenuantes, **com respeito aos limites cominados**. O CP não estabelece fração legal geral numérica nos arts.65–68; não importa automaticamente 1/5–1/3.
- **CP68 PU × CPM76 PU:** CP permite considerar apenas o fator mais intenso em concurso de causas previstas **na Parte Especial**; CPM76 PU tem enunciado mais amplo de causas especiais. Escopo de restrição e cumulação podem mudar.
- **CPM76:** causas especiais escapam aos limites quantitativos do tipo, **mas preservam os limites da espécie de pena**, cuja reconstrução depende também do CPM58.

## 3. STF, STJ e STM — por que a categoria da circunstância importa

Arquivo [`JURISPRUDENCIA_DOSIMETRIA_CICLO12.csv`](JURISPRUDENCIA_DOSIMETRIA_CICLO12.csv), 5 fontes individualizadas.

1. **STF Tema158 / RE 597.270:** vedação de ultrapassar mínimo apenas em **atenuantes genéricas**; não afirma que toda norma penal especial sobre mitigação seja uma atenuante. [Registro](https://portal.stf.jus.br/jurisprudenciaRepercussao/verAndamentoProcesso.asp?classeProcesso=RE&incidente=2663001&numeroProcesso=597270&numeroTema=158).
2. **STJ, REsp 1.869.764/MS, Terceira Seção, 14/08/2024:** manutenção da Súmula231 diante do Tema158, quanto à atenuante genérica no CP. [Registro oficial](https://scon.stj.jus.br/SCON/jurisprudencia/toc.jsp?livre=%28RESP+INPATH%28CLAS%29+AND+1869764+INPATH%28NUM%29%29+OR+%28NEAR%28%28RESP%2C1869764%29%2C0%2CTRUE%29+INPATH%28SUCE%29%29).
3. **STJ Tema1194, REsp 2.001.973/RS, 10/09/2025**, [ficha de precedente qualificado](https://processo.stj.jus.br/repetitivos/temas_repetitivos/pesquisa.jsp?cod_tema_final=1194&cod_tema_inicial=1194&novaConsulta=true&tipo_pesquisa=T): a confissão **não precisa servir ao convencimento para atenuar CP65 III d**, mas retratação, confissão parcial/qualificada e a preponderância da circunstância admitem limites; **efeitos prejudiciais modulados** para fatos após publicação do acórdão. [Súmula545 revisada](https://processo.stj.jus.br/SCON/sumstj/toc.jsp?sumula=545.num.). Tema diretamente sobre CP, **não resolve sozinho CPM72 III d**.
4. **STM Ap 7000232-60.2024.7.00.0000**, publicado no acervo da revista do tribunal e já examinado no ciclo09: maioria tratou mitigação por CPM35 como redutor na etapa que permite pena abaixo do mínimo (9 meses e 18 dias de detenção), enquanto voto divergente a classificou como atenuante sujeita a piso (um ano de reclusão); **espécies penais distintas, não converter apenas cifras**. [Acórdão publicado](https://revista.stm.jus.br/index.php/periodicos/article/download/jurisprudencia-05-v34-n1-2024/88/238).

**Controvérsia aberta, não solução jurídica aprovada:** saber se CPM35 é atenuante (fase II, piso) ou causa especial (fase III, abaixo do piso), inclusive como opera substituição de pena, e qual parte do quadro jurisprudencial se aplica ao conjunto de fatos.

## 4. Dez simulações controladas e matematicamente validadas

[`SIMULACOES_FASES_DOSIMETRIA_CICLO12.csv`](SIMULACOES_FASES_DOSIMETRIA_CICLO12.csv) contém **10 cenários aritméticos**, com campos `antes_piso`, `apos_piso`, `final`, tipo de fase, fração e categoria. **Sem lei incriminadora específica:** pena abstrata de **reclusão de 5 a 10 anos, hipótese fictícia**, pena-base inicial de 5 anos (=60 meses) na maioria dos casos; em dois casos base de 6 anos (72 meses). Não representam pena real de CPM35, erro de direito, CPM46 ou tipos concretos. Frações das minutas A2/B2 são **propostas M**, não direito automaticamente vigente.

| Simulação | Segunda fase | Terceira fase | Pena final em meses |
|---|---|---|---|
| S12-01 base no mínimo | nenhuma | nenhuma | **60** |
| S12-02 atenuante hipotética 1/5 | cai a 48 aritmeticamente, piso mantém 60 | nenhuma | **60** |
| S12-03 atenuante hipotética 1/3 | cai a 40 aritmeticamente, piso mantém 60 | nenhuma | **60** |
| S12-04 B2-DM minorante especial 1/5 | nenhuma | 60 × 4/5 | **48** |
| S12-05 B2-DM minorante especial 1/3 | nenhuma | 60 × 2/3 | **40** |
| S12-06 A2-D1 minorante especial 1/6 | nenhuma | 60 × 5/6 | **50** |
| S12-07 A2-D1 minorante especial 1/3 | nenhuma | 60 × 2/3 | **40** |
| S12-08 excesso doloso como atenuante 1/5 | piso mantém 60 | nenhuma | **60** |
| S12-09 base 72, atenuante 1/5 e minorante 1/3 | 72 × 4/5 = 57,6, piso mantém 60 | 60 × 2/3 | **40** |
| S12-10 base 72, só minorante 1/3 | nenhuma | 72 × 2/3 | **48** |

**Prova material:** com pena-base no piso, atenuante pode ser reconhecida **sem impacto numérico**; causa especial legalmente prevista pode reduzir a pena **abaixo**. Não afirmar que uma norma de conduta autoriza a causa especial até que sua categoria seja demonstrada ou legislativamente criada. A comparação sobre redução por erro evitável também depende da **facultatividade** de CP21, preservada na minuta A2.

**Risco do exemplo:** os limites de 5–10 anos são fictícios e só permitem contraste controlado das fases; regimes executórios, substituições, sursis, espécie da pena e efeitos civis **não foram calculados**. Não usar para aconselhamento em caso judicial concreto.

## 5. Escolhas materiais e riscos para o CLF

**PROB-T25-0036 — Vetores de pena-base:** unificar CP59 e CPM69 sem ocultar distinções relevantes e risco de dupla valoração.  
**PROB-T25-0037 — Reincidência:** CP64 × CPM71 têm exclusões e formas de contagem diferentes; há potencial aumento de pena involuntário.  
**PROB-T25-0038 — Agravantes e atenuantes recentes:** leis 14.688/2023, 15.159/2025, 15.160/2025 impõem controle temporal e de especialidade; uma regra comum pode estender agravante ou perder atenuante.  
**PROB-T25-0039 — Confissão:** Tema1194/STJ e CPM72 III d devem ser comparados sem tratar súmula do CP como revogação do texto militar.  
**PROB-T25-0040 — Categoria do CPM35:** escolher entre B2-DP (atenuante sob piso), B2-DM (minorante) e A2-D1 (minorante para núcleo comum) é **M**, não ajuste de técnica.  
**PROB-T25-0041 — CPM46:** fixar 1/5–1/3 para excesso doloso em A2-D2/B2-DEx é proposta **M**; a lei militar atual não fixa no art46 tal fração e o sistema de pena precisa ser analisado em conjunto.  
**PROB-T25-0042 — Concorrência de causas:** CP68 PU limita-se à Parte Especial e CPM76 PU é mais amplo; risco de alterar a pena pela técnica de reunião.  
**PROB-T25-0043 — Penas e direitos em guerra:** CPM72 PU (pena abstrata de morte) exige exame crítico à luz da CF/1988 e dos efeitos em guerra declarada; código novo não cria permissões constitucionais.

## 6. Feito, pendente e próximo

**FEITO:** dois intervalos integrais de numeração (19 artigos), **86 posições indexadas**, **22 relações de especialidade**, cinco fontes jurisprudenciais e dez simulações verificadas numericamente, com ressalvas sobre direito vigente e propostas M.

**PENDENTE:** original e cadeia temporal 1940/1969/1984/2023/2025 por subunidade; estudo integral das espécies de pena, multas e substituições, CPM53,58 e CP44; dosimetria em múltiplas causas com tipos reais; jurisprudência específica do STM em reincidência/confissão; direitos constitucionais e competência, efeitos sobre T26/T27, opção A2/B2 e DEC-016.

**PRÓXIMO (T25.M03 ciclo13):** abrir o subbloco de **espécies, substituições e execução inicial** (CP32–58 e CPM55–68 em recorte por consequência) e anexar teste com **dois tipos legais concretos e seus marcos temporais**, mantendo separação da escolha política por B2-DP/B2-DM/A2-D1. Em paralelo, produzir nota intertemporal CP64/65 e CPM71/72 e verificar jurisprudência militar específica antes de formular artigos gerais consolidados.

**Categorias:** `Q` para comparação; proposta `M` identificada, **não aprovada**; `C0-T` não produzido para este inventário descritivo; `C0-J` não demonstrado. [Protocolo de continuidade](../../governanca/18_PROTOCOLO_CONTINUIDADE_POR_RODADA.md).
