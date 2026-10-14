# T29.M01 — F2-A: modelo de direito vigente — filiação, qualidade de segurado e dependência

**Corte da pesquisa:** 14/10/2026 · **Dossiê:** F2-A (primeira reconstrução do regime; não conclusão do F2 integral).  
**Issue:** [#40](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/40) · **PR draft:** [#41](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/41) · **Baseline CLF `main`:** `16fba172c875c7a0de388288fe70005c944021d6`.  
**Fonte constitucional vigente:** CF/1988 com EC103/2019; projeto constitucional alternativo em repositório distinto **não transforma** hipóteses em direito positivo.  
**Titularidade:** T29.M01. Custeio T29.M02, prestações T29.M03/M04/M05, procedimento T29.M06 e RPPS T29.M07 são **interfaces, sem edição unilateral**. T24.M01 permanece com PR38.

## 1. Mudança metodológica: de histórico de artigos a funcionamento do sistema

Esta rodada não recopia as 15 MPs, o inventário F1-A de 198 registros ou os espelhos F1-D. **Reconstrói regras operativas e testa consequências.** Fontes jurídicas têm níveis distintos: lei; emenda constitucional; decreto regulamentar; tese repetitiva/controle concentrado; decisão não vinculante; proposta futura CLF. A matriz [F2A_MATRIZ_MODELO_VIGENTE.csv](F2A_MATRIZ_MODELO_VIGENTE.csv) contém **33 regras**, com pressuposto, efeito, fundamento, responsável e status de prova ou Q. A matriz [F2A_TESTES_20_CASOS.csv](F2A_TESTES_20_CASOS.csv) contém **20 casos hipotéticos avaliados** (não demandas reais ou julgamento judicial), com resposta motivada e incerteza.

**Regra de construção:** `fato remunerado qualificado → filiação obrigatória`; em alternativa `opção válida + inscrição + primeiro recolhimento → filiação facultativa`; em paralelo `relação familiar/jurídica + condição da classe + prova → dependência`. Uma vez existente o vínculo, examinar `atividade/benefício em curso → manutenção legal da qualidade → evento protegido e requisito da prestação`. A existência de carência, sua dispensa, valor do benefício ou recolhimento do tomador pertence a regras próprias, não a simples definição de segurado.

## 2. Diagrama decisório textual

```text
PESSOA FÍSICA E EVENTO / DATA DE REFERÊNCIA
|
+-- 1. EXERCE ATIVIDADE ENQUADRADA NO RGPS?
|   |
|   +-- SIM => FILIAÇÃO OBRIGATÓRIA pelo exercício (D.3048 art.20§1).
|   |          -> qual categoria da Lei8213 art11?
|   |          -> existe RPPS por outro vínculo? RGPS apenas para atividade simultânea.
|   |          -> inscrição e recolhimento não são automaticamente o fato constitutivo.
|   |          -> eventual inadimplemento do responsável: interface T29.M02.
|   |
|   +-- NÃO => AVALIAR FACULTATIVO
|              -> sem filiação obrigatória ou RPPS impeditivo;
|              -> inscrição + primeiro recolhimento; sem retroação comum.
|              -> 14 anos na lei / 16 anos no Decreto: Q, NÃO escolher por C1.
|
+-- 2. QUALIDADE DE SEGURADO NA DATA DO EVENTO?
|   |
|   +-- vinculado e em atividade / situação legal de benefício;
|   +-- OU dentro do período de graça do art.15:
|         inciso II 12 meses, §1 até 24 se mais de 120 contribuições;
|         §2 +12 para desemprego involuntário comprovado;
|         incisos III/IV/V/VI têm prazos próprios.
|         prazo exato da perda segue §4 e calendário legal de custeio.
|   |
|   +-- se já perdeu, avaliar direitos adquiridos à aposentadoria e
|       exceção de pensão art.102§2 / STJ Súmula416 (interface M03/M05).
|
+-- 3. DEPENDENTE?
|   |
|   +-- classe I: cônjuge, companheiro e filho segundo idade/deficiência;
|   |             equiparados do art.16§2 sob requisitos específicos.
|   +-- classe II: pais; classe III: irmão conforme art16 III.
|   +-- classe anterior exclui seguinte (§1);
|   +-- presunção econômica para inciso I (§4); prova para demais;
|   +-- prova de união estável/econômica conforme §§3,5,6;
|   +-- condenação definitiva por homicídio doloso/tentativa e ressalvas §7.
|
+-- 4. BENEFÍCIO SOLICITADO E DATA FATO GERADOR
    -> verificar tipo de prestação/carência/dispensa, Lei/EC no período,
       perda eventual, prova e efeitos; remissão M03/M04/M05/M06.
    -> caso de guarda após EC103: Q STF Tema1271; não negar só pelo §6
       isolado ou afirmar EC revogada pela Lei15108/2025.
```

**Diagrama de lógica, não algoritmo decisório suficiente para o deferimento de benefício.** Cada passo depende da vigência na data de evento, exceções, provas e jurisprudência; não há implementação de software que profira decisões individuais.

## 3. Reconstrução do ingresso: filiação, inscrição e contribuição são coisas distintas

**Obrigatório:** Lei8.213 art11/Lei8.212 art12 enumeram empregado, doméstico, avulso, contribuinte individual, especial e casos específicos; Decreto3.048 art20§1 afirma filiação automática pelo trabalho remunerado, observada exceção. Não confundir ausência de CNIS/cadastro, não recolhimento por empresa e não exercício de atividade: são problemas diferentes, com ônus e meios probatórios diferentes. A empresa desconta/arrecada contribuição de empregados e avulsos conforme Lei8.212 art30 I, mas seus deveres de custeio devem ser codificados em **M02**, não como cláusula de exclusão do empregado em M01.

**Facultativo:** Lei8.213 art13 e Lei8.212 art14 dizem **maior de 14 anos**, enquanto Decreto3.048 art11 e art18§2 mencionam 16. Decreto3.048 art11§3 e art20§1 regulam ato voluntário, inscrição e pagamento inicial, sem retroação ordinária, com ressalva de hipótese especial art28§3. **A divergência de idade permanece Q.** A decisão da 11ª Turma Recursal de SP no processo 5002988-56.2025.4.03.6322 admitiu em tese a pessoa de 15 anos, mas não é precedente nacional vinculante; crítica à recusa de salário-maternidade por única contribuição deve considerar **ADIs2110/2111/STF** sobre carência, distinta de prova efetiva de filiação/fraude.

**RPPS:** Lei8.212 art13/Lei8.213 art12 excluem do RGPS o vínculo já coberto por regime próprio, mas **§1 permite filiação obrigatória simultânea** por outra atividade abrangida pelo RGPS. Um cidadão pode ter diferentes atividades e posições jurídicas; tempo concomitante, contribuição e contagem recíproca não são automaticamente duplicados.

**Inscrição:** Lei8.213 art17 e Decreto3.048 art18 definem forma e responsável. Dependentemente da classe, a inscrição de dependente é promovida **quando requer benefício** (Lei8.213 art17§1). Lei8.213 art17§7 proíbe inscrição post mortem de contribuinte individual/facultativo; não se pode transportar a vedação sem exame para trabalhador empregado com trabalho efetivamente provado.

## 4. Manutenção da qualidade: matriz temporal e proteção probatória

| Estado / categoria | Disciplina recuperada do art.15 Lei8.213 | Advertência |
|---|---|---|
| Em gozo de benefício, salvo auxílio-acidente | inciso I: qualidade mantida sem limite por essa condição | auxílio-acidente foi excetuado pela Lei13.846/2019 |
| Cessou atividade ou contribuição (inciso II) | até 12 meses | aplicar regras especiais, data de cessação e §4 |
| Histórico superior a 120 contribuições mensais, sem perda | §1: até 24 meses | **mais de 120**, e não 120 exatas |
| Desemprego involuntário provado | §2: acrescenta 12 meses sobre II/§1, potencial até 36 | **STJ Tema1360 (2026)**: outros meios idôneos servem; ausência isolada de CTPS/CNIS não basta |
| Segregação / reclusão / serviço militar | incisos III, IV e V: 12/12/3 meses | fatos e termos iniciais específicos |
| Facultativo | inciso VI: 6 meses | não transferir a ampliação do inciso II automaticamente |
| Final do prazo | §4: perda no dia seguinte ao fim do prazo de recolhimento relativo ao mês subsequente | **não presumir dia exato sem calendário de custeio** |

**Fonte:** [Lei8.213 art15](https://www.planalto.gov.br/ccivil_03/leis/l8213cons.htm); [STJ Tema1360, julgamento publicado 16/07/2026](https://www.stj.jus.br/sites/portalp/Paginas/Comunicacao/Noticias/2026/16072026-Repetitivo-fixa-tese-sobre-prova-de-desemprego-para-extensao-do-periodo-de-graca-previdenciaria.aspx); [Decreto3048 art13](https://www2.camara.leg.br/legin/fed/decret/1999/decreto-3048-6-maio-1999-368532-normaatualizada-pe.html).

**Exceção de importância sistêmica:** Lei8.213 art102 §§1/2 e [STJ Súmula416](https://scon.stj.jus.br/SCON/sumstj/toc.jsp?sumula=416.num.) preservam aposentadoria já aperfeiçoada e podem permitir pensão por morte mesmo que a qualidade de segurado tenha sido perdida, quando todos requisitos de aposentadoria estavam cumpridos em vida. **Proibição de simplificação:** `perdeu qualidade → nenhum benefício aos dependentes` é falsa.

## 5. Segurado especial — pertencimento e exceções

**Lei8.213 art11 VII §§1,6–12 e Lei8.212 art12 VII e respectivos parágrafos** tratam trabalho em economia familiar, produtor/pescador, dimensões, mão de obra, atividade dos familiares, rendimentos e hipóteses que preservam ou extinguem enquadramento. Regras de 2024 (Lei15.072) sobre cooperativas incluem itens vetados: jamais reconstituí-los editorialmente. Tamanho de propriedade deve ser conjugado com economia familiar e alcance concreto de **STJ Tema1115**.

**PSA:** Lei14.119 art23 incluiu pagamento por serviços ambientais na exceção expressa de Lei8.212 art12§9 VIII, mas Lei8.213 art11§8 não tem inciso VIII igual. IN RFB2110/2022 art9§5 IX espelha em âmbito fiscal; edição anotada 2026 ainda não certificada de modo independente. **Não aplicar PSA como causa automática de desenquadramento**, nem tratá-lo como condição suficiente para criar segurado especial se ausente trabalho rural familiar. A interpretação prestacional pertence a Q e às interfaces M02/M03.

## 6. Dependência — regras materiais e a controvérsia constitucional

**Lei8.213 art16** fixa classes I (cônjuge/companheiro e filhos inclusive proteção por invalidez/deficiência), II (pais) e III (irmãos), com exclusão da classe posterior (§1), presunção econômica para inciso I e prova para demais (§4). **Enteado, tutela e guarda judicial (Lei15.108/2025)** estão no §2 e sujeitos a requisitos próprios; presumir ausência de toda prova econômica pela remissão à classe I é arriscado.

**União estável/prova:** §§3 e 5 exigem conformidade à união estável e início de prova material contemporânea, com ressalvas por força maior ou caso fortuito; §6 acrescenta prova temporal pertinente à regra específica de duração de pensão do art77 §2 V c — **não é duração universal para reconhecer união estável**. A exclusão por homicídio doloso ou tentativa do §7 exige condenação transitada em julgado, ressalvados absolutamente incapazes e inimputáveis.

**Guarda e tempo:** art16§2 original 1991 incluía guarda; **MP1523 publicada 14/10/1996** excluiu da letra, com 14 reedições até Lei9528/1997; **STJ Tema732 (2017)** reconheceu proteção a menor sob guarda economicamente dependente mesmo após a MP; STF ADIs4878/5083 (2021) interpretaram art16§2 em favor da guarda; **EC103 art23 §§4/6/7** impõe questão constitucional autônoma, objeto de **STF Tema1271** sem mérito localizado; **Lei15108/2025** reincorporou expressamente guarda. Não reconstruir “direito criado em 2025” nem negar automaticamente a guarda no período 1996–2025.

**Interfaces:** T29.M01 define classe/condição; T29.M05 trata fato gerador da pensão, duração, rateio e efeitos; T29.M06 organiza prova, instrução e recursos; T32 infância e tutela/guarda.

## 7. Resultado dos testes: 20 casos avaliados

A [matriz F2-A de testes](F2A_TESTES_20_CASOS.csv) responde **20 casos hipotéticos** com fundamento: **4 de ingresso, 5 de manutenção da qualidade, 2 de segurado especial, 7 de dependência e 2 de inscrição**. Casos de especial atenção:
- Trabalhadora com emprego efetivo e empregador inadimplente: **filiação pelo trabalho**, prova pendente; falta de recolhimento do responsável não é sinônimo de ausência de filiação.
- Facultativo de **15 anos**: **Q interpretativa**, não resposta automática por regulamento.
- Pessoa com **mais de 120 contribuições** e desemprego involuntário provado: **potencial 36 meses**, respeitado termo do §4 e prova no **Tema1360**; simples carteira vazia é insuficiente.
- Benefício **auxílio-acidente apenas**: não gera qualidade ilimitada pela hipótese do art15 I após Lei13846/2019.
- Pessoa sem qualidade na morte mas com requisitos de aposentadoria cumpridos: exceção **art102§2 e Súmula416**.
- Dependente com **deficiência grave** e mais de 21 anos: idade isolada não exclui enquadramento da lei.
- Guarda e óbito em **2018**: STJ Tema732 e ADIs protegem conforme prova; guarda em **2023/2025** exige análise EC103/Tema1271, sem presumir tese final.
- União estável com prova exclusivamente testemunhal ordinária, ausência de registro de dependentes e condenação penal sem trânsito: efeitos diferentes de regras diferentes.

**Validação dos testes:** são inferências condicionadas ao quadro normativo, não simulações automatizadas de concessão ou decisões de casos reais. Onde não há conclusão jurídica segura, a resposta está explicitamente `Q`.

## 8. Consequências para arquitetura futura do CLF — ainda hipóteses

**Conceitos que poderiam servir de eixo editorial**, condicionados a teste posterior de equivalência e promulgação formal adequada:
1. pessoas cobertas e regras gerais de filiação;
2. categorias de segurados obrigatórios, atividade simultânea e RPPS;
3. filiação facultativa e inscrição;
4. manutenção, perda e recuperação da qualidade;
5. segurado especial e hipóteses de conservação/descaracterização;
6. dependentes: classes, prova, equiparação, exclusões;
7. remissões aos regimes prestacionais e de custeio com preservação de transições.

**Não há minuta F5.** Nenhuma dessas rubricas altera direito, revoga lei ou foi aprovada como localização normativa definitiva. Um conceito único de segurado **não pode** eliminar as obrigações contributivas da Lei8.212; as salvaguardas de menores, deficiência, qualidade e dependência têm que permanecer expressas. Reservas legislativas, competência e natureza de Código único (**DEC-016**) ainda não resolvidas.

## 9. Riscos descobertos ao abandonar o simples inventário

1. **Novo precedente de 2026 não capturado na F1 histórica:** **STJ Tema1360** — não exigir exclusivamente registro estatal do desemprego involuntário; é insuficiente apenas falta de CTPS/CNIS, exigindo conjunto de prova.
2. **Regra que invalida simplificações absolutas:** **STJ Súmula416** — morte após perda de qualidade nem sempre afasta pensão; analisar aposentadoria adquirida em vida.
3. **Confusão entre inscrição, qualidade, carência e contribuição:** diferença entre empregado automaticamente filiado, facultativo volitivo, segurado especial e dependente; requer módulos distintos.
4. **Risco de redução de proteção de incapacidade/deficiência, guarda e maternidade:** não inferir requisitos que a lei ou o STF não impuseram.
5. **Tempo como chave do modelo:** um mesmo fato (guarda judicial, idade de filiação, mandato) pode produzir respostas diferentes conforme eventos de 1996, 2019, 2025 e decisões de interpretação; “compilado 2026” sozinho não representa direito histórico.

## 10. FEITO/PENDENTE/PRÓXIMO

**FEITO:** F2-A — **33 regras funcionais** referenciadas a artigos e precedentes, **20 testes respondidos**, reconstrução de ingresso, manutenção, segurado especial e dependentes, diferenciação de efeitos e Q, novos Tema1360 e Súmula416. **PENDENTE:** F2 integral e situações prestacionais específicas; individualizar regras especiais complementares (art. 38-A/38-B, Decreto3048, IN), conferir julgados em inteiro teor e acompanhar Tema1271; verificar IN RFB de 2026; **F1 literal ainda parcial**; normas futuras Lei15371 só entram em vigor em 01/01/2027; classificação C0/C1/M não aprovada, PR draft, `main` não alterada.

**PRÓXIMO — F2-B:** reconstruir a **dinâmica temporal da qualidade** com casos de manutenção/recuperação, sucessão de vínculos e dependência em datas de óbito, confrontando carência x filiação x decadência do direito ao benefício, sem produzir decisões de benefício pertencentes a M03/M04/M05. Avaliar sistematicamente a hipótese de **modelo único de qualificação subjetiva** e riscos de duplicação com Lei8212 em interface M02. Só após F2 e auditorias suficientes iniciar F3 comparativo e F4 opções de reforma.

**Controle:** fontes oficiais conferidas especificamente nos dispositivos citados; nenhuma norma CLF criada, nenhum efeito C0/C1/M aprovado, nenhuma alteração fora de T29.M01.
