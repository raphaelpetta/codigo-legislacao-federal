# T29.M01 — F1-B: auditoria adversarial de quatro divergências normativas

**Corte da pesquisa:** 14/10/2026. **Tarefa:** aprofundar apenas Q29-ENV (serviços ambientais), Q29-IDADE (segurado facultativo), Q29-GUARDA (menor sob guarda), Q29-MANDATO (mandatos eletivos). **Issue #40; PR #41 draft**. **Base CLF main verificada:** `16fba172c875c7a0de388288fe70005c944021d6`. **Estado jurídico:** direito positivo brasileiro (CF/1988 e emendas) distinto de hipóteses CLF/CF futura; nenhum C0/C1/M aprovado.

**Artefato companheiro:** [F1B_MATRIZ_QUATRO_DIVERGENCIAS.csv](F1B_MATRIZ_QUATRO_DIVERGENCIAS.csv) — **19 eventos/fonte**, com data, diploma, dispositivo, conclusão factual, efeito/ressalva temporal e URL. Não substitui o inventário descritivo [F1-A de 198 registros](F1A_MATRIZ_GRANULAR_8213_8212.csv) nem cria duplicação normativa.

## 1. Q29-ENV — Pagamentos por serviços ambientais e segurado especial

**Texto localizado:** a [Lei 14.119/2021, art. 23](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14119.htm) acrescentou **VIII ao §9º do art. 12 da Lei 8.212/1991**, alcançando participação em programas e ações de pagamento por serviços ambientais (PSA) entre as situações que **não descaracterizam** a condição de segurado especial. A [compilação 8.212](https://www.planalto.gov.br/ccivil_03/leis/l8212compilado.htm) confirma esse inciso. A [Lei 8.213, art. 11, §8º](https://www.planalto.gov.br/ccivil_03/leis/l8213cons.htm), tem lista correspondente que termina no inciso **VII**; **não contém inciso VIII sobre PSA**. A Lei 14.119/2021 não alterou expressamente o art. 11 da 8.213 no art. 23.

**Classificação:** divergência **legislativa textual comprovada**, não simples problema de numeração. **Não está comprovada** exclusão de segurado ou perda de benefício em razão exclusiva de PSA. Não inferir, de um silêncio num rol, que a norma concessiva do diploma paralelo seja juridicamente inaplicável; também não presumir equivalência sem exame da remissão de âmbito, do art. 11 §§9º–10 e art. 12 §§10–11.

**Hipóteses de leitura:**
- **A (integração sistemática):** efeitos da previsão expressa no custeio se refletem no enquadramento subjetivo RGPS, pois os arts. 11/12 descrevem as mesmas pessoas, com diferenças jurídicas. Exige demonstração normativa/jurisprudencial, não automação.
- **B (assimetria material):** uma categoria permanece protegida formalmente no custeio, mas há possível risco de indeferimento prestacional, lacuna a ser suprida em reforma **M**, se constatado.
- **C (regime distinto):** certos rendimentos/atividades PSA podem acarretar enquadramentos distintos conforme operação, contratação, caráter familiar e fatos, exigindo tipos próprios.

**Ressalva:** o **art. 17 da Lei 14.119**, com trechos vetados posteriormente promulgados, trata de tributos próprios e seus requisitos; não é sinônimo de isenção universal de contribuições previdenciárias. A participação em programas de PSA também **não dispensa automaticamente** prova de economia familiar, atividade rural principal ou demais requisitos do art. 11.

**Teste jurídico:**
1. Agricultor familiar em atividade tradicional passa a receber PSA pela manutenção de vegetação nativa, sem empregados permanentes: verificar se recebe remuneração por serviços enquadrada na exceção do art.12 §9 VIII; garantir que uma redação CLF não o exclua somente por PSA.
2. Prestador empresarial de consultoria ambiental remunerada, sem atividade rural em economia familiar: a exceção PSA **não cria segurado especial automaticamente**.
3. Produto remunerado de PSA com distintos contratos/tributações: examinar art. 17, dependências T29.M02/T12 e legislação ambiental, sem inventar isenção previdenciária.

**Decisão reservada:** manter `Q29-ENV` quanto à consequência jurídica e, antes de criar definição única, consultar precedentes administrativos/judiciais e os instrumentos de PSA; se comprovada divergência real, levar proposta M fundamentada à frente central.

## 2. Q29-IDADE — Facultativo 14 anos (lei) versus 16 anos (decreto e INSS)

**Direito textual:** [Lei 8.212/1991, art. 14](https://www.planalto.gov.br/ccivil_03/leis/l8212compilado.htm), e [Lei 8.213/1991, art. 13](https://www.planalto.gov.br/ccivil_03/leis/l8213cons.htm) referem-se ao **maior de 14 anos**. [Decreto 3.048/1999, art. 11 caput e art. 18 §2º](https://www.planalto.gov.br/ccivil_03/decreto/d3048compilado.htm) emprega **maior de 16** e idade mínima de inscrição; o [INSS, orientação de 18/08/2026](https://www.gov.br/inss/pt-br/assuntos/noticias/dia-do-estagiario-contribuir-para-o-inss-desde-cedo-pode-fazer-diferenca-no-seu-futuro), reproduz 16 anos como requisito administrativo para o estudante facultativo.

**Origem provável da interpretação:** a **EC 20/1998** elevou para 16 a idade geral mínima de trabalho, salvo aprendizagem a partir de 14, em CF art. 7º, XXXIII. Há tratamento doutrinário e jurisprudência de tribunais federais que aplicam esse marco à filiação facultativa. **Mas a norma constitucional regula diretamente trabalho, não inscrição voluntária sem trabalho**; derivação de idade mínima contributiva é uma conclusão jurídica **interpretativa**, não substituição expressa da redação ordinária. **Não afirmar revogação textual tácita das leis ou invalidade definitiva do decreto** sem verificação jurisdicional conclusiva. Material de doutrina da 4ª Região (revista de 2005 depositada em BDJur/STJ) defende 16 com base na EC20; trata-se de doutrina, **não precedente vinculante**.

**Distinguir três hipóteses:** (a) trabalho lícito aos 14–15 anos como aprendiz, **filiação obrigatória**, não facultativa; (b) trabalho efetivo **ilícito pela idade**, cujo reconhecimento previdenciário é tema protetivo de fatos consumados e não deve ser impedido mecanicamente; (c) adolescente de 15 anos **sem trabalho** deseja apenas contribuição voluntária: é o verdadeiro caso-testemunha da divergência lei/regulamento.

**Teste jurídico:** formular competência de filiação com nascimento aos 15 anos e primeiro recolhimento depois de 1998; confrontar CF, lei, decreto, jurisprudência do TRF, segurança jurídica e natureza contributiva voluntária. Marcar `Q29-IDADE` e vedar transposição "maior de 16" como C1/editorial sem fundamentação material. **Alternativa M futura:** harmonizar idade legal/regulamentar com garantia expressa da proteção de aprendiz e de trabalho infantil de fato.

**Limite:** não foi localizado repetitivo STJ ou tese STF diretamente sobre *facultativo sem atividade remunerada de 14–15 anos* com solução geral nesta rodada. A prática administrativa é concreta, mas sua fundamentação exata e validade judicial permanecem controvertidas.

## 3. Q29-GUARDA — Proteção do menor sob guarda e questão constitucional pendente

**Linha temporal em quatro regimes normativos:**
1. **1991**: redação original da [Lei 8.213 art. 16 §2º](https://www.planalto.gov.br/ccivil_03/leis/l8213cons.htm) incluía guarda judicial entre as equiparações a filho.
2. **1997**: [Lei 9.528/1997](https://www.planalto.gov.br/ccivil_03/leis/l9528.htm) excluiu a guarda da letra do dispositivo, mantendo enteado e tutelado.
3. **2019**: **EC 103/2019, art. 23 §6º**, em regime próprio de pensão, equiparou a filhos **exclusivamente enteado e menor tutelado**, sujeitos à prova de dependência econômica. Art. 23 §4º remete o rol e a qualificação à Lei 8.213, e §7º admite alterações legais da disciplina da pensão. **O contraste entre esses três parágrafos é material; não apagar §6º ao citar §4º/§7º**.
4. **2021**: [STF ADIs 4878 e 5083](https://portal.stf.jus.br/jurisprudenciaRepercussao/verPronunciamento.asp?pronunciamento=10615600), julgadas conjuntamente em junho de 2021, conferiram **interpretação conforme ao art. 16 §2º** para abranger guarda com **dependência econômica comprovada**. Esse julgamento não é, sem novo exame, decisão de mérito sobre constitucionalidade específica da **EC 103 art.23 §6º**.
5. **2025**: [Lei 15.108/2025, art. 1º](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15108.htm), publicada e vigente em **14/03/2025**, passou a incluir expressamente menor sob guarda judicial no art.16 §2º, mediante declaração do segurado e insuficiência de condições de sustento e educação.

**Achado novo da rodada:** [STF Tema 1271 — RE 1.442.021](https://portal.stf.jus.br/jurisprudenciaRepercussao/verAndamentoProcesso.asp?classeProcesso=RE&incidente=6661561&numeroProcesso=1442021&numeroTema=1271) tem objeto **precisamente a exclusão produzida pelo art.23 §6º da EC 103/2019**. Na última movimentação de mérito processual disponibilizada na consulta em 14/10/2026, constava **concluso ao relator em 16/04/2026 após parecer da PGR**; **não identificada tese de mérito final**. A ficha mostra a existência da repercussão geral, que **não equivale ao resultado do mérito**. Não declarar a questão encerrada com ADIs 2021 ou Lei 2025.

**Quadro de períodos de óbito a testar (NÃO decisões jurídicas definitivas):**

| Data do óbito | Camadas prioritárias | Resultado nesta pesquisa |
|---|---|---|
| Antes de 2019 | Lei 8.213 na data, Lei 9.528 e ADIs 2021; considerar situação jurídica consolidada e entendimento constitucional | Proteção reconhecida pelo STF no âmbito das ADIs; efeitos intertemporais concretos dependem da ratio e da prova |
| 13/11/2019–13/03/2025 | **EC 103 art.23 §6º** + ADIs de 2021 sobre art.16 | **Controvérsia constitucional específica Tema 1271**, evitar certeza absoluta |
| A partir de 14/03/2025 | Lei 15.108 (novo art.16 §2º) + EC 103 art.23 §§4º/6º/7º | Proteção legal expressa, mas efeitos constitucionais sistêmicos não se resolvem só pela redação ordinária |

**Teste de regressão:** uma minuta que copie o §6º da EC 103 isoladamente **apagaria a proteção legal vigente**; outra que copie só a Lei 15.108 e omita a EC 103/Tema 1271 **apagaria a controvérsia constitucional**. O CLF deve registrar **Q constitucional e situação por data de fato gerador**, com remissões à CF vigente e a T29.M05, T32/T17.

**Decisão reservada:** impedir C0-J de formulação "rol único definitivo" até enfrentar Tema 1271 e Lei 15.108; questões de comprovação, modulação e antecipação de efeitos sob julgamento devem permanecer Q.

## 4. Q29-MANDATO — Alíneas h/j e suspensão de execução

**Histórico:**
- **Lei 9.506/1997, art.13 §1º:** acrescentou **h** a **Lei 8.212 art. 12 I**, incluindo exercente de mandato sem RPPS como segurado/contribuinte no RGPS; compilação da **Lei 8.213 art.11 I** também exibe alínea h de 1997.
- **STF RE 351.717/PR (08/10/2003):** declarou inconstitucional a disciplina de 1997 por razão constitucional de custeio **na ordem anterior à EC 20/1998**. [Notícia institucional STF](https://noticias.stf.jus.br/postsnoticias/stf-declara-inconstitucional-dispositivo-de-lei-sobre-cobranca-previdenciaria-para-detentores-de-mandato/) e [fundamentação em pronunciamento posterior STF](https://portal.stf.jus.br/jurisprudenciaRepercussao/verPronunciamento.asp?pronunciamento=4595227).
- **Lei 10.887/2004:** acrescentou **j** aos mesmos dispositivos: nova positivação após alteração constitucional de custeio. **Não significa convalidação retroativa da lei de 1997**.
- **Resolução do Senado 26/2005, publicada em 22/06/2005:** [art.1º](https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2005/congresso/ressf26-05.htm) **suspendeu especificamente a execução do art. 12 I h da Lei 8.212**. **Não menciona** alínea **j**, **nem nomeia o art.11 I h da Lei 8.213**; a razão constitucional da decisão pode influenciar outros dispositivos, mas isso exige exame jurídico específico, não ampliá-la editorialmente como se houvesse suspensão formal universal.

**Ponto que exige correção futura no inventário:** o art. 11 I **h** da Lei 8.213 ainda aparece com texto na [compilação Planalto](https://www.planalto.gov.br/ccivil_03/leis/l8213cons.htm), ao lado da alínea **j**; é inadequado atribuir-lhe, sem outro ato, o mesmo status formal de suspensão que está **expressamente previsto** para Lei 8.212 art.12 I h. O corpo do CLF não deve reproduzir ambos os enunciados como normas cumulativas indistintas; tampouco revogar silenciosamente h de Lei 8.213 com fundamento exclusivo em resolução dirigida a outra lei.

**Teste temporal:** competência contributiva de 2001, após EC20 mas antes de j/2004, não pode ser tratada por aplicação retroativa de j; competência de 2005/2006 requer distinguir nova lei e suspensão da anterior. Regime de benefício e carência também não pode presumir recolhimento válido de tributo materialmente declarado inconstitucional em certo período sem análise própria. Interfaces **T29.M02** e **T12** são obrigatórias.

**Decisão reservada:** posição h de 8.212 = `EXECUCAO_SUSPENSA`; j = `POSITIVA_POSTERIOR`; h de 8.213 = `TEXTO_COMPILADO_COM_CONTROLE_CONSTITUCIONAL_A_APURAR`, não equiparação automática. Modernizar como conceito único só após revisão de alcance subjetivo, período e espécies.

## 5. Resultado integrado e decisão sobre a próxima pesquisa

| Problema | Há diferença comprovada? | Está resolvido materialmente? | Possível avanço CLF sem alterar direito |
|---|---|---|---|
| PSA | **Sim, lei expressa só no custeio** | **Não:** alcance na cobertura e implementação Q | preservar exceção textual e remissão para avaliação em M01/M02 |
| Facultativo 14/16 | **Sim, lei versus decreto** | **Não definitivamente para voluntário de 15 anos sem trabalho** | manter duas versões como fontes com estado de divergência, sem C1 fictício |
| Menor sob guarda | **Sim, EC 103 e Lei 2025; ADIs 2021** | **Tema 1271 ainda pendente na fonte consultada** | registrar cenário por fato gerador e constitucionalidade Q, não criar rol único absoluto |
| Mandato h/j | **Sim, atos e períodos diferentes** | **Formalidade de suspensão h em 8.212 verificada; extensão a 8.213 Q** | preservar histórico h/j e bloquear consolidação neutra sem concordância temporal |

**Arquitetura preliminar recomendada, não aprovada:** T29.M01 conservar regras de definição da qualidade e dependência e referências à T29.M02 para consequências contributivas; M05 recebe elegibilidade e impactos na pensão; reserva de lei/competência e constitucionalidade são avaliadas pela governança central. A divergência documental **não basta** para classificar automaticamente reforma como C1; eventual harmonização substantiva será M e exigirá decisão do usuário.

## 6. FEITO, limites e próxima porta

**FEITO:** quatro conflitos separados e reconstruídos por 19 eventos em matriz datada, com fontes institucionais; identificado **Tema 1271** e explícita limitação das ADIs; distinguida alínea h de 8.212 versus h de 8.213 e j; levantada assimetria PSA e a diferença fonte formal/decreto sobre 14/16.

**PENDENTE:** inteiro teor e eventual modulação das ADIs, tese final Tema 1271 (consultar nova movimentação antes de redigir), segunda fonte judiciária sobre filiação facultativa 14–15, decisões administrativas sobre PSA, DOU de toda cadeia 1997/2004/2021 e repercussões por competências tributárias, cotejo CF proposta por dispositivo. A matriz F1-A de **198 registros permanece descritiva**, com subdivisões indicativas, não afirma que todas as linhas equivalem a subunidades positivas separadas; F1 literal/cadeia global não concluída. **Nenhuma redação CLF, decisão M, revogação nem integração**.

**PRÓXIMO — T29.M01/F1-C seletivo:** verificação de **quatro cadeias com fontes primárias integrais**: STF Tema 1271 (processo e eventual acórdão), ADIs 4878/5083 dispositivo/modulação, Decreto 3.048 e precedentes de facultativo 14–16, Res.26/2005 versus 8.213 h e 8.212 j; requisitar do T29.M02 uma nota específica sobre PSA e base contributiva, **sem duplicar o módulo de custeio**. Entregável: parecer por evento e teste temporal, antes de qualquer escolha C1/M.
