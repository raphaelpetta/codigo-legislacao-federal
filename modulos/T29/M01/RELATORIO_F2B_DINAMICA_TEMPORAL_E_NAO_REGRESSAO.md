# T29.M01 — F2-B: dinâmica temporal da filiação, manutenção, perda, recuperação e dependência

**Corte:** 14/10/2026 · **Escopo:** reconstrução jurídico-sistêmica do regime geral de segurados e dependentes · **Issue** [#40](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/40) · **PR draft** [#41](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/41).  
**Base inicial CLF main:** `16fba172c875c7a0de388288fe70005c944021d6`. **Proprietário funcional único:** T29.M01; T29.M02, M03, M04, M05, M06 e M07 permanecem módulos de interface, sem alteração. T24.M01 reservado à outra frente, PR38. CF/1988 com EC103/2019 é direito vigente, não o projeto de CF alternativa.

## 1. Resposta sistemática: não existe um único booleano “segurado”

A tutela previdenciária exige **cinco eixos independentes, mas relacionados**:

1. **Filiação**: o vínculo nasce do exercício efetivo de atividade obrigatória ou, para facultativos válidos, da inscrição e primeiro recolhimento; a identificação administrativa não define sozinha o vínculo obrigatório.
2. **Qualidade no instante do evento**: manutenção pela atividade, pela prestação protegida, por um dos períodos de graça ou sua perda após termo legal preciso; a categoria altera o prazo.
3. **Histórico contributivo e carência**: período contributivo acumulado não some da história apenas porque cessou a qualidade, mas sua utilização para prestações específicas exige normas próprias, algumas afetadas por controle de constitucionalidade. Remeter a M02/M03/M04/M05.
4. **Direito já formado**: aposentadoria cujos requisitos se completaram em vida resiste à perda posterior de qualidade (Lei8.213 art102§1), e pensão pode decorrer da exceção do §2, conforme **Súmula416/STJ**.
5. **Dependência no fato gerador**: classe, prova, presunção e norma/precedente aplicável à data de morte devem ser qualificados separadamente do momento em que se requer ou cadastra a prestação. Guardas posteriores à EC103 têm a Q constitucional do STF Tema1271.

**Consequência:** um conceito único futuro poderá definir `segurado` como papel jurídico geral, mas não deve produzir uma consequência uniforme de todo silêncio contributivo, inscrição, carência e dependência. **Uma pessoa pode ter mais de um vínculo simultâneo**, proteção durante prazo de graça sem pagar e direito já adquirido após perda da qualidade.

**Instrumentos verificáveis desta rodada:** [F2B_TRANSICOES_23_ESTADOS.csv](F2B_TRANSICOES_23_ESTADOS.csv) descreve **23 transições condicionais**, e [F2B_TESTES_TEMPORAIS_26.csv](F2B_TESTES_TEMPORAIS_26.csv) descreve **26 casos hipotéticos respondidos**, vinculados às regras anteriores F2-A e à nova matriz. Não são decisões judiciais ou cálculo automatizado do INSS.

## 2. Modelo de estados e fluxos (sem simplificação indevida)

```text
INÍCIO
├─ atividade remunerada obrigatória provada ───────────────> FILIAÇÃO OBRIGATÓRIA
│     ├─ atividades concomitantes ────────────────────────> vínculos múltiplos,
│     │                                                       não tempo duplicado
│     ├─ empresa não recolhe ─────────────────────────────> pendência M02;
│     │                                                       vínculo não desaparece
│     └─ atividade cessa ─────────────────────────────────> QUALIDADE EM GRAÇA
│            ├─ art.15 II: 12 meses
│            ├─ art.15 §1: até 24 meses (>120 recolhimentos sem perda)
│            ├─ art.15 §2: +12 meses (desemprego involuntário provado)
│            └─ art.15 §4: termo exato conforme vencimento de contribuição
├─ opção facultativa válida + inscrição + 1º pagamento ─────> FILIAÇÃO FACULTATIVA
│     ├─ interrompe contribuições ────────────────────────> GRAÇA 6 MESES
│     └─ filiação aos 15 anos ────────────────────────────> Q: Lei 14 / Decreto 16
├─ benefício protegido em curso ───────────────────────────> QUALIDADE MANTIDA
│     └─ auxílio-acidente apenas ─────────────────────────> exceção ao art.15 I
└─ depois do termo legal art.15§4 ─────────────────────────> QUALIDADE PERDIDA
       ├─ reingressa RGPS por atividade/ato válido ───────> NOVA FILIAÇÃO
       │     └─ carência de certas prestações ────────────> art.27-A com
       │                                                     controle das ADIs
       ├─ já completara aposentadoria ────────────────────> DIREITO ADQUIRIDO
       │     └─ morre ────────────────────────────────────> ressalva art.102§2
       └─ morre sem qualidade/aposentadoria aperfeiçoada ─> regra negativa,
                                                             ressalvas e prova
EM CADA ÓBITO: classe de dependente, união estável, deficiência, guarda,
            data, normas transitórias, eventual Q STF Tema1271.
```

O fluxograma identifica perguntas e condicionantes; **não constitui algoritmo suficiente para decidir benefício individual**.

## 3. Núcleo temporal de manutenção e perda da qualidade

O [art.15 da Lei8.213](https://www.planalto.gov.br/ccivil_03/leis/l8213compilado.htm) diferencia manutenção sem limite enquanto recebe benefício protegido (exceto auxílio-acidente), cessação de contribuição/atividade, segregação compulsória, detenção/reclusão, serviço militar e facultativo. Somente a **hipótese do inciso II** comporta as prorrogações específicas dos §§1 e 2 na leitura legal ordinária. **Mais de 120 contribuições**, sem interrupção que causasse perda, permite §1; **desemprego involuntário comprovado** acrescenta 12 meses (também ao prazo do §1). A contagem ordinária poderá chegar a **12/24/36 meses**, não é 36 para todos.

**Critério probatório agora qualificado:** [STJ Tema1.360](https://processo.stj.jus.br/repetitivos/temas_repetitivos/pesquisa.jsp?cod_tema_final=1360&cod_tema_inicial=1360&novaConsulta=true&tipo_pesquisa=T), REsps **2.169.736/RJ e 2.188.714/MT**, julgamento **11/03/2026**, acórdãos publicados **19/03/2026**, **trânsito 21/05/2026**. A notícia de **16/07/2026** é notícia tardia, **não a data do julgamento**. A tese permite **outros meios idôneos**, em âmbito administrativo/judicial, para demonstrar desemprego involuntário, mas mera ausência de anotações CTPS/CNIS **não basta isoladamente**. [Acórdão completo do REsp2.169.736/RJ](https://processo.stj.jus.br/processo/julgamento/eletronico/documento/?documento_sequencial=364154764&documento_tipo=integra&publicacao_data=20260319&registro_numero=202403443449), [Informativo881/STJ](https://scon.stj.jus.br/jurisprudencia/externo/informativo/?acao=pesquisarumaedicao&from=feed&livre=0881.cod.).

**Termo final — trava obrigatória:** o art.15 **§4º** e [Decreto3.048 art.14](https://www.planalto.gov.br/ccivil_03/decreto/d3048compilado.htm) vinculam a perda da qualidade ao **dia posterior ao vencimento da contribuição do contribuinte individual relativa ao mês imediatamente posterior** ao término do período de graça. Portanto, o código não deve usar apenas “12 meses desde o último trabalho”, e nossos testes **não calculam dia exato sem competência, categoria e calendário aplicável**. Há outras condições regulamentares (Decreto art13 §§7–8, art19-E) quanto a valores inferiores ao mínimo, que exigem interface M02 e caso concreto.

## 4. Recuperação do vínculo não significa recuperação automática de toda carência

**Lei8.213 art27-A**, redação Lei13.846/2019, exige nova filiação e determinada fração de contribuições para que se aproveitem anteriores à perda em **benefícios selecionados**. A versão consolidada do dispositivo **ainda menciona salário-maternidade** e remete ao art25 III. Todavia, o [STF nas ADIs 2.110 e 2.111, julgamento de 21/03/2024](https://portal.stf.jus.br/processos/detalhe.asp?incidente=1795149), declarou inconstitucional a exigência de carência do art25 III para salário-maternidade. **Não se pode reintroduzir pela via do art27-A metade de uma carência afastada constitucionalmente**, ao menos sem fundamento autônomo que suporte a exigência. O tema tem interface com M05; o escopo M01 se limita à **filiação real, sua nova aquisição e prova**. A questão de adaptação formal do art27-A à decisão constitucional deve ficar em Q de concordância e não em simples C1 editorial.

**Separação obrigatória:**
- **nova filiação/qualidade**: condição subjetiva material;
- **contribuições existentes**: histórico contributivo não apagado;
- **carência**: requisito de determinado benefício, quando válido;
- **alegada fraude**: causa específica, dependente de demonstração, não presumível por um único recolhimento.

**Teste adversarial:** uma segurada recém-filiada não pode ser tratada como sem qualidade só porque não completou prazo de carência que o STF declarou inconstitucional; também não se deve dispensar prova efetiva de filiação e requisitos de fato gerador.

## 5. Segurado obrigatório versus recolhimento pós-morte: risco encontrado

A tese geral de filiação obrigatória automática é **insuficiente** quando aplicada indiscriminadamente à elegibilidade à pensão de **contribuinte individual responsável pelo próprio recolhimento**. [STJ, Informativo 525, REsp1.346.852/PR, julgamento 21/05/2013](https://scon.stj.jus.br/jurisprudencia/externo/informativo/?acao=pesquisarumaedicao&from=feed&livre=0525.cod.) e [AgRg no AREsp636.048/PR, DJe26/05/2015](https://scon.stj.jus.br/SCON/GetInteiroTeorDoAcordao?dt_publicacao=26%2F05%2F2015&num_registro=201403121321) afirmam que **dependentes não podem recolher após o óbito as contribuições devidas pelo próprio CI para constituir qualidade de segurado e, com isso, a pensão**.

**Não igualar esse caso** ao empregado cujo empregador era responsável pela arrecadação, e **não presumir a mesma conclusão para todas as atividades classificadas CI** após regras de retenção da Lei10.666/2003: quem era legalmente responsável pelo recolhimento no período concreto é pergunta jurídica determinante para M02. STJ não disse que inscrição de empregado após morte sempre se confunde com vedação CI, nem que prova de vínculo de trabalho de empregado sem contribuição patronal produz negativa automática. Em M01, distinguir vínculo material, condição de pagamento para prestações, ônus e prova; M05 decide pensão, M02 contribuições.

**Teste P19 x P20:** CI autônomo sem pagamento próprio anterior ao óbito → restrição STJ ao recolhimento post mortem; empregado formal ou de fato com empregador inadimplente → filiação pela atividade, contribuições devidas pelo empregador e prova do vínculo, com efeitos previdenciários a apurar.

## 6. Direito após perda: exceções de natureza diferente

[Lei8.213 art102 §§1–2](https://www.planalto.gov.br/ccivil_03/leis/l8213compilado.htm) e [STJ Súmula416](https://scon.stj.jus.br/SCON/sumstj/toc.jsp?sumula=416.num.) estabelecem que:
- o preenchimento integral dos requisitos de aposentadoria, segundo a lei da época, **preserva o direito adquirido mesmo com perda posterior de qualidade**;
- na morte após perda de qualidade, **a pensão pode ser devida**, caso o instituidor já reunisse os requisitos para aposentadoria em vida, além das condições próprias da pensão e da dependência.

A exceção não equivale a “toda pessoa que teve mais contribuições pode receber pensão”: exige comprovação integral dos requisitos da aposentadoria ao tempo em que se aperfeiçoaram, sujeita à lei correspondente. Pensão e aposentadoria permanecem em M05/M03, com remissão de M01.

## 7. Estados simultâneos, atividade especial e dependentes

**Vínculos simultâneos:** empregado de dois estabelecimentos pode ter dois vínculos RGPS num mesmo mês; servidor efetivo RPPS que exerce outra atividade RGPS pode ter posições próprias simultâneas. Não se contam meses duplicados para tempo de aposentadoria nem se presume dupla cobertura prestacional proporcional sem regras específicas. A personalidade previdenciária não é unidade de histórico sem origem; o futuro modelo deve identificar `vínculo + categoria + intervalo + responsável pelo recolhimento`.

**Mudança do segurado especial:** a atividade rural/familiar e suas exceções (§§8–12 do art11) são relevantes para caracterizar ou descaracterizar **aquela categoria**. Um ingresso em outra atividade obrigatória não significa automaticamente perda de **toda** proteção do RGPS; ao mesmo tempo, a condição de especial não se transfere para todo novo emprego. PSA e cooperativas requerem exceções e vetos de 2024 (Q com interface M02).

**Dependência:** a data do óbito fixa pergunta sobre lei aplicável e qualidade; prova administrativa posterior pode comprovar fato anterior. A existência de companheiro classe I exclui mãe classe II conforme art16 §1, se efetivamente comprovada a qualidade do primeiro. Menor sob guarda e óbito 2018 é controlado também pelo **STJ Tema732** e pelas ADIs; óbito 2023 demanda exame do **art23§6 EC103, STF Tema1271**. Não adotar exigências de 2025 para negar automaticamente direitos anteriores, nem afirmar resultado de mérito do Tema1271 sem verificação.

## 8. Testes executados, novas salvaguardas e cobertura F2-A

[F2B_TESTES_TEMPORAIS_26.csv](F2B_TESTES_TEMPORAIS_26.csv) responde **26 situações hipotéticas** (concomitância, filiação facultativa, 120/121 contribuições, prova, benefício, remuneração abaixo do mínimo, perda/retorno, maternidade, empregado/CI após óbito, dependência, segurado especial). **Não substituem decisões individualizadas**; certas linhas permanecem Q deliberadamente.

**Cobertura complementar intencional dos seis IDs da F2-A que não haviam sido exercitados:**
- `F2A-R01`: posição geral de beneficiários (P01);
- `F2A-R04`: duas atividades RGPS concomitantes (P02);
- `F2A-R09`: RPPS versus filiação facultativa (P04);
- `F2A-R10`: trabalho voluntário sem remuneração (P05);
- `F2A-R14`: inscrição de segurado especial (P06);
- `F2A-R21`: conservação de direitos durante o período de graça (P16, nota: a aplicação do requisito de carência foi destacada; testar especificamente direito durante a graça também em revisão F2-C se necessário).

Esses seis pontos tinham sido omitidos dos **20 casos anteriores**, e a presente rodada os alcança com hipóteses específicas. **Isso não significa exaustão jurídica de todas as 33 regras ou de todas as exceções.**

**Arquitetura preparatória (sem aprovação):** um modelo de `pessoa/vínculo/atividade/categoria/intervalo/qualidade/causa de perda ou manutenção` acoplado a um `dependente/classe/vínculo familiar/prova/óbito`, com campos independentes de `histórico contributivo, carência, requisitos de benefício`, mantidos em M02/M03/M05. Tal modelo de dados não decide política pública nem promulga o CLF.

## 9. FEITO/PENDENTE/PRÓXIMO

**FEITO:** modelo de **23 transições condicionais** e **26 testes analisados**; acrescida jurisprudência STJ do recolhimento post mortem, verificado **Tema1360 com acórdão, julgamento em março e trânsito em maio de 2026**, corrigindo notícia de julho antes usada como principal fonte; identificada inconsistência do art27-A após ADIs2110/2111, proteção ao direito adquirido e necessidade de qualificação das fontes contributivas.

**PENDENTE:** confirmação artigo-local de todas as versões históricas de períodos de graça, pagamento extemporâneo e novas filiações; definição de aplicação prática da carência no art27-A pós ADIs; Tema1271 STF sobre guarda/EC103; PSA e IN RFB2110/2026; captação completa dos fatos de segurado especial, contagem de competências e critérios de prova; compatibilidade do modelo com CF alternativa; revisão jurídico-adversarial independente, verificação CI no HEAD e governança de integração.

**PRÓXIMO — F2-C:** modelo único de **pessoas, vínculos, históricos e dependentes** com fronteiras formais entre F2 material e M02/M05; construir matriz de concordância `regra origens → conceito → exceção → titular`; executar contraprovas de **carência após perda**, filiação facultativa de 14/16, reconciliação da condição de segurado especial e dependência em óbitos múltiplos. **Antes de proposta C1/M**, consultar governança DEC016, texto CF alternativa atual e testar não regressão dos 46 cenários acumulados F2-A/F2-B. **F3 comparado e F4 alternativas somente depois da F2.**

**Critério:** nenhuma simplificação que transforme inscrição em filiação obrigatória, contribuição em carência universal, perda de qualidade em caducidade absoluta, a data da Lei15108 em origem exclusiva de proteção ao menor sob guarda, ou a prova de desemprego em registro administrativo exclusivo.

**Nenhum texto C0/C1/M, revogação ou fusão legal foi criado. PR draft e main não alterada.**
