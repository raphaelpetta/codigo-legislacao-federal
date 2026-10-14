# T29.M01 — Segurados e dependentes do RGPS

**Título:** T29 — Previdência social e proteção contributiva  
**Regime jurídico:** Segurados e dependentes · **Dossiê:** v0.1 / F0 e F1 seletiva  
**Data de corte:** **14/10/2026** · **Status:** PLANEJADO, inventário seletivo incompleto, sem dispositivos CLF aprovados  
**Baseline:** CLF `main` `16fba172c875c7a0de388288fe70005c944021d6`; Constituição alternativa `main` `2a770a8136f8ca4877e865be3e3b7745a6d4b168` (fotografia, nenhuma norma importada).  
**Issue:** [#40](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/40) · **PR:** abrir na presente branch · **Proprietário funcional exclusivo:** esta frente T29.M01.  
**Não sobreposição:** T24.M01 está reservado ao PR #38/issue #37 em outra frente; **não tocar seus documentos**.

## 1. F0 — escopo jurídico positivo

**Pergunta central:** quem está coberto por filiação ao RGPS, a partir de quando, por quanto tempo e em quais condições um terceiro ostenta a qualidade de dependente?

Inclui, provisoriamente:
1. categorias de **segurados obrigatórios** (empregado, doméstico, avulso, contribuinte individual, especial) e **facultativos**, exceções e ocupações atípicas;
2. **filiação e inscrição**, nascimento, manutenção, perda e recuperação da qualidade de segurado, período de graça e vínculos entre RGPS e regimes próprios;
3. **segurado especial**, economia familiar, grupo familiar, dimensão da exploração, renda acessória, perda e prova da atividade; regra de enquadramento, sem criar aqui as aposentadorias rurais;
4. classes, **dependência econômica**, prova, equiparações (enteado, tutelado, menor sob guarda), proteção da criança/pessoa com deficiência e perda da qualidade de dependente;
5. cronologia de mudanças do universo subjetivo (EC 103/2019, Lei 11.718/2008, Lei 13.846/2019, Lei 15.072/2024, Lei 15.108/2025, e atos subsequentes identificados).

**Exclusões operacionais para impedir duas frentes de escreverem o mesmo regime:**

| Objeto reservado a outro módulo | Dono e remissão para M01 |
|---|---|
| Bases de cálculo, recolhimento, alíquotas e responsabilidade tributária | **T29.M02** / T12 (regras tributárias); T29.M01 usa somente qualificações necessárias ao enquadramento |
| Requisitos, renda, DIB, cálculo e reajuste de aposentadorias | **T29.M03** |
| Incapacidade, carências de benefícios e perícia | **T29.M04**; M01 fornece filiação e qualidade |
| Direito à pensão por morte/auxílio-reclusão, DIB, duração e rateio | **T29.M05**; M01 define dependência subjetiva, M05 regra prestacional |
| Procedimento de requerimento, prova administrativa, recurso/INSS/CRPS | **T29.M06** e T07, T24 para judicialização; regras materiais de prova de dependência ficam em M01 com interface M06 |
| RPPS e previdência complementar | **T29.M07** e **T29.M08**; M01 limita-se a conflitos de filiação |
| BPC/LOAS e proteção assistencial não contributiva | **T30**; não confundir assistência social com RGPS |
| Direito material do trabalho e proteção da criança/família | **T28**, T13, T17 e T32 em remissão, não reprodução |

## 2. Constitucionalidade e espécies de fonte

**CF/1988 vigente, cenário A:** arts. 7º (garantias laborais), 22, 24 e 149 (competência), 194–195 (seguridade/custeio) e 201 (RGPS). A EC 103/2019 contém **regras próprias de transição que não se esgotam no art. 201**. A Constituição proposta possui repositório separado; consultar versão antes de construir eventual cenário B, sem antecipar reformas.

**Camadas jurídicas:** (1) CF/1988 e ECs — parâmetro superior, externas ao CLF; (2) Leis 8.213/1991 e 8.212/1991 — legislação positiva, parcialmente coincidente quanto a segurados; (3) leis especiais/alteradoras e decisões do STF/STJ — efeitos normativos e hermenêuticos distintos; (4) Decreto 3.048/1999 e IN INSS 128/2022 — **regulamentos externos**, não artigos de lei passíveis de transposição automática; (5) políticas assistenciais, RPPS estaduais/municipais e acordos internacionais — interfaces próprias.

**C0/C1/M/Q:** **nenhuma norma CLF redigida ou homologada nesta rodada**; inventário descritivo não demonstra equivalência jurídica. Normas alteradas/vetadas/sem vigência exigem marca temporal específica. **DEC-016** sobre veículo legislativo único ainda PENDENTE.

## 3. F1 seletiva — evidências, não exaustividade

| Fonte oficial e unidade consultada | Função observada | Nota crítica | Estado |
|---|---|---|---|
| [Lei 8.213/1991, arts. 9º–17 (Câmara atualizada)](https://www2.camara.leg.br/legin/fed/lei/1991/lei-8213-24-julho-1991-363650-normaatualizada-pl.html) | Definição de beneficiários, segurados, qualidade, dependência, inscrição | Art. 11 é multiestratificado, não uma definição simples; art. 16 e 17 dependem de alterações posteriores | Lido por artigo/trechos, **não por todas as subdivisões** |
| [Lei 8.212/1991, arts. 12–15 (Planalto compilada)](https://www.planalto.gov.br/ccivil_03/leis/l8212compilado.htm) | Segurados para custeio, segurado especial/facultativo, empresa | Convergir conceito sem fundir base tributária e qualificação de beneficiário | Leitura seletiva |
| [Decreto 3.048/1999, arts. 9–17 (Planalto)](https://www.planalto.gov.br/ccivil_03/decreto/d3048compilado.htm) | Regulamentação operacional de filiação, inscrição e dependência | Necessária comparação de conformidade hierárquica, **não norma legislativa do Código** | Busca focal |
| [Lei 15.108/2025 (Planalto)](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15108.htm) | Art. 16 §2º: reinclui expressamente **menor sob guarda judicial** entre os equiparados a filho | Comparar STF ADIs 4878/5083 (2021), lei de 2025, efeitos intertemporais e ECA | Texto do dispositivo lido |
| [Lei 15.072/2024, alterações art. 11 (Câmara compilada)](https://www2.camara.leg.br/legin/fed/lei/1991/lei-8213-24-julho-1991-363650-normaatualizada-pl.html) | Novas subhipóteses de exercício de atividade político/cooperativa pelo segurado especial | Conferir vetos, incidência temporal e paralelo da Lei 8.212 | Trechos e anotações lidos |
| [Lei 13.846/2019, art. 16 §§5º–7º (Câmara compilada)](https://www2.camara.leg.br/legin/fed/lei/1991/lei-8213-24-julho-1991-363650-normaatualizada-pl.html) | Início de prova material, casos de união estável, exclusão por homicídio doloso | Direito à prova e presunções: confrontar critérios de proteção, limites e jurisprudência | Trechos lidos |
| [Lei 15.371/2026 (Planalto), art. 14](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/lei/l15371.htm) | Licença e salário-paternidade; muda as Leis 8.212 e 8.213 | **Publicada em 01/04/2026, VIGÊNCIA FUTURA 01/01/2027**; interface com T29.M02/M05 e T28; não usar como vigente em outubro de 2026 | Art. 1º, 7º, 8º e 14 lidos |
| [STF ADIs 4878/5083 — notícia institucional 2021](https://portal.stf.jus.br/noticias/verNoticiaDetalhe.asp?idConteudo=467309&ori=1) | Interpretação conforme do art. 16 §2º em favor do menor sob guarda com dependência econômica | Confirmar dispositivo de acórdão, modulação e relação com Lei 15.108/2025 | Notícias, **não inteiro teor** |
| [STJ Tema 1115 (Informativo 758)](https://processo.stj.jus.br/jurisprudencia/externo/informativo/?livre=%40CNOT%3D019565) | Área rural acima de quatro módulos não descaracteriza por si só economia familiar se outros requisitos presentes | Conflito aparente com limite legal; não abolir requisito só com ementa | Tese institucional, **não acórdão integral** |
| [IN PRES/INSS 128/2022 — portal com alterações até 2026](https://www.gov.br/inss/pt-br/centrais-de-conteudo/legislacao/instrucao-normativa/2022) | Procedimentos e interpretações operacionais | Regulamento administrativo mutável; última atualização registrada em agosto de 2026 no portal | Índice de versões, não íntegra |

**Inventário estruturado:** [INVENTARIO_F1_SELETIVO.csv](INVENTARIO_F1_SELETIVO.csv). **Diagnóstico crítico:** [NOTA_01_DIAGNOSTICO_FRONTEIRAS_E_OPCOES.md](NOTA_01_DIAGNOSTICO_FRONTEIRAS_E_OPCOES.md).

## 4. Modelo preliminar do direito vigente (F2 ainda não concluída)

`atividade enquadrada → filiação obrigatória` ou `opção de filiação facultativa + ato constitutivo` → `qualidade de segurado` (inclusive manutenção legal sem contribuição) → `cobertura eventual no evento, segundo legislação da prestação`; em paralelo, `relação familiar/dependência + prova + classe` → `qualidade de dependente`.

Cada seta exige regras de início/fim, competência temporal, exceções e prova; não é fórmula decisória. **Pagamento e filiação não são sinônimos**. A condição de segurado especial possui regras próprias e a dependência pode existir sem inscrição prévia, conforme dispositivo aplicável.

## 5. Problemas e decisões em aberto

`Q29-01` conflito ou redundância entre art. 11 da Lei 8.213 e art. 12 da Lei 8.212, com riscos de reescrever dever contributivo em benefício e vice-versa.  
`Q29-02` leis materialmente constitucionais/transitórias EC 103/2019 e hipóteses estaduais/RPPS.  
`Q29-03` proteção de menor sob guarda, tutela, deficiência e união estável (STF 2021 versus lei 2025, grau de prova e efeitos pretéritos).  
`Q29-04` segurado especial e trabalho híbrido rural/cooperativo (Lei 15.072/2024, STJ Tema 1115, vetos e regulamentação).  
`Q29-05` período de graça, manutenção e perda da qualidade (art. 15), prova do desemprego e hipótese de múltiplas filiações.  
`Q29-06` faculdade de filiação: idade indicada na literalidade da Lei 8.212 art. 14 versus regulamento/INSS que referem 16 anos e CF art. 7º XXXIII; verificar cadeia e hierarquia antes de classificar idade mínima.  
`Q29-07` Lei 15.371/2026 publicada em vacatio até janeiro de 2027 — **não incorporar como positiva vigente em outubro de 2026**; avaliar relação com M02/M05/T28.  
`Q29-08` textos de lei, jurisprudência vinculante e atos administrativos podem diferir: preservar fonte, hierarquia e efeito, sem escolher resultado editorialmente.

**Sem propostas M aprovadas.** Alternativas de simplificação só serão redigidas após inventário/cadeia históricos e testes de não regressão.

## 6. Próximo passo (tarefa única)

**F1-A detalhada do T29.M01:** auditar **Lei 8.213/1991, arts. 10–17**, subunidade por subunidade (incluindo art. 11 completo), com cotejo Lei 8.212/1991, arts. 12–14, em matriz de origem, redação atual, leis alteradoras, vigência, veto, elemento de prova e módulo primário. Priorizar art. 16 §2º (Lei 15.108), art. 11 §9º V (Lei 15.072) e art. 15. Complementar fontes oficiais da cadeia e decisões judiciais **por inteiro teor**. Aceite: inventário identificado por unidade e classificação Q quando não comprovado.

**Fila:** definir identidade de segurado especial em legislação 1991/2008/2024; mapear jurisprudência especial; análise crítica comparativa e alternativas de reforma só após F1 sólido.

## 8. Rodada 02 — F1-A granular (14/10/2026)

A frente passou do inventário **seletivo inicial (36 registros de fontes/grupos)** para uma triagem por subunidade de **198 registros**: **117** da Lei 8.213/1991, arts. 10–17, e **81** da Lei 8.212/1991, arts. 12–14. Foram mapeadas **78 relações funcionais** entre as duas leis, sem afirmar redação idêntica ou equivalência jurídico-material.

- [Matriz F1-A — 198 subunidades](F1A_MATRIZ_GRANULAR_8213_8212.csv).
- [Paralelos art. 11 (benefícios) × art. 12 (custeio) — 78 relações](F1A_PARALELOS_8213_ART11_8212_ART12.csv).
- [Relatório jurídico sobre assimetrias, alterações e testes](RELATORIO_F1A_AUDITORIA_GRANULAR_E_ASSIMETRIAS.md).
- [Pacote de continuidade da rodada 02](PACOTE_CONTINUIDADE_RODADA_02.md).

**Achado novo prioritário:** Lei 14.119/2021, art. 23, acrescentou o art. 12, §9º, VIII, à Lei 8.212 (participação em programas de pagamento por serviços ambientais sem descaracterizar segurado especial), mas **não** criou inciso simétrico no art. 11, §8º, da Lei 8.213. Essa assimetria é textual/documental; **a consequência jurídica ainda é Q**.

Pontos cuja cadeia precisa ser mantida: alínea h suspensa da Lei 8.212/1991 art. 12 I (Resolução Senado 26/2005) e alínea j distinta; hipóteses e vetos da Lei 15.072/2024; menor sob guarda 1991→1997→STF 2021→Lei 15.108/2025; segurado facultativo 14 anos nas leis versus 16 no decreto/INSS; Lei 15.371/2026 com vigência só em **01/01/2027**.

**F1 ainda parcial**: os 198 registros são classificações funcionais **não transcrições literais certificadas**. Nenhum C0/C1/M ou revogação foi proposto. **Próxima tarefa:** F1-B focada nas quatro divergências com maior risco de alteração de direitos, antes de eventual F2/F5.

## 9. Rodada 03 — F1-B focada: quatro assimetrias críticas (14/10/2026)

Complemento **não duplicativo** da matriz F1-A: [F1B_MATRIZ_QUATRO_DIVERGENCIAS.csv](F1B_MATRIZ_QUATRO_DIVERGENCIAS.csv) contém **19 eventos datados**, com proveniência, status de vigência/decisão e interfaces, e [RELATORIO_F1B_QUATRO_CONFLITOS_E_TEMA_1271.md](RELATORIO_F1B_QUATRO_CONFLITOS_E_TEMA_1271.md) contém análise adversarial dos quatro Q:

- `Q29-ENV`: Lei 14.119/2021 art.23 acrescentou art.12 §9º VIII (8.212) **sem espelho literal** na 8.213 art.11 §8º; repercussão prestacional depende de pesquisa, não permite negar segurado só pelo silêncio.
- `Q29-IDADE`: Lei 8.212 art.14 e Lei 8.213 art.13 dizem **14 anos**, Decreto 3.048 art.11 e INSS 2026 adotam **16**; tese sobre facultativo sem trabalho aos 15 anos continua Q, não corrigir como simples C1.
- `Q29-GUARDA`: STF ADIs 4.878/5.083 (2021) e Lei 15.108/2025 protegem guarda judicial, mas **EC 103/2019 art.23 §6º** suscita a questão autônoma do **Tema 1271/STF (RE 1.442.021)**, **sem julgamento de mérito localizado** na pesquisa de 14/10/2026. Deixar explícito o período do óbito e a hierarquia constitucional.
- `Q29-MANDATO`: Resolução Senado 26/2005 suspendeu estritamente **Lei 8.212 art.12 I h**, não a alínea j de 2004 nem, pelo seu dispositivo, o art.11 I h de Lei 8.213; preservar períodos pré e pós EC20/1998.

**Critério:** nenhuma conclusão autoriza transposição C0-J, fusão C1 ou reforma M aprovada. Fontes oficiais e testes contrafactuais no relatório. O **pacote de continuidade da rodada 03** registra FEITO/PENDENTE/PRÓXIMO.

**Próximo:** F1-C, revisão judicial/temporal de 4 cadeias (Tema 1271, ADIs 4878/5083, facultativo 14/16 e h/j); pedir nota de custeio ao T29.M02 sem editar seus arquivos.

## 10. Rodada 04 — F1-C: precedentes e efeitos temporais (14/10/2026)

**Nova evidência que altera os riscos e fecha parcialmente Q:**

- [Matriz F1-C de 18 casos e períodos](F1C_CASOS_TEMPORAIS_18.csv) — 5 mandato, 4 idade facultativa, 5 guarda e 4 serviços ambientais, todos com origem, período e ressalva.
- [Relatório F1-C jurisprudência e efeitos temporais](RELATORIO_F1C_JURISPRUDENCIA_E_EFEITOS_TEMPORAIS.md) — confronto STF Tema 691, RE 351717, ADIs 2110/2111 e 4878/5083, STF Tema1271, TRF3 decisão de 15 anos e Receita Federal IN2110.
- [Continuidade rodada 04](PACOTE_CONTINUIDADE_RODADA_04.md).

**Mandato:** STF Tema **691** (RE626837, mérito 25/05/2017; trânsito 21/02/2018) encerra a Q geral da constitucionalidade **da contribuição sobre agente político não vinculado a RPPS após Lei10887/2004**, sem revalidar a norma de 1997, nem ampliar automaticamente Resolução Senado26/2005 (8.212 h) à h da 8.213.

**Facultativo 14–16:** o acórdão [TRF3, 11ª Turma Recursal de SP, processo 5002988-56.2025.4.03.6322](https://web.trf3.jus.br/acordaos/Acordao/BuscarDocumentoPje/395087868), admite em tese filiação facultativa aos **15 anos** (contra sentença que aplicara decreto), mas mantém improcedência de salário-maternidade por reputar instrumental **contribuição única em gravidez**. O requisito de carência do salário-maternidade foi invalidado nas **ADIs 2110/2111**, exigindo teste para impedir carência/tempo mínimo disfarçado sob presunção não demonstrada de fraude. **Decisão TRF3 é caso concreto e não vincula nacionalmente.**

**Guarda:** Tema **1271** STF (RE1442021), sobre **EC103/2019 art23 §6**, permanecia sem julgamento de mérito identificado na ficha oficial consultada, com última movimentação 16/04/2026. ADIs4878/5083 e Lei15108/2025 não eliminam dever de estudar §§4/6/7 e cronologia dos óbitos.

**PSA:** IN RFB **2.110/2022 art9 §5 IX** recebeu expressamente exceção de **Lei8212 art12 §9 VIII** para PSA. A prova fiscal administrativa é adicional à assimetria legislativa com Lei8213 art11 §8, mas não demonstra efeito automático em todos os benefícios. Verificar alterações da IN em 2024/2025/2026 antes de usar redação vigente.

**Status:** pesquisa F1-C executada, mas inventário jurídico/literal integral ainda Q; nenhuma redação CLF C0/C1/M, nenhuma intervenção em T24, T29.M02 ou `main`. **Próxima:** F1-D — cotejo literal e histórico concentrado dos nove dispositivos críticos, com DOU e separação de legislação, decisão e regulação.

## 11. Rodada 05 — F1-D, cotejo histórico focal (14/10/2026)

- [F1D_ESPELHO_NUCLEOS_19.csv](F1D_ESPELHO_NUCLEOS_19.csv): **19 posições** por fonte/versão em quatro eixos; há **uma ausência de inciso** registrada como ausência estrutural, e **uma transcrição de IN RFB 2110/2022 da edição original sem certificação da versão de 2026**. As demais redações são cotejo **manual** entre publicação original de 1991, leis modificadoras e versões oficiais compiladas. Não equivalem a 19 normas novas nem a C0.
- [RELATORIO_F1D_COTEJO_LITERAL_HISTORICO.md](RELATORIO_F1D_COTEJO_LITERAL_HISTORICO.md): cronologia e 9 testes adversariais de eventual transposição.
- [PACOTE_CONTINUIDADE_RODADA_05.md](PACOTE_CONTINUIDADE_RODADA_05.md): FEITO / PENDENTE / PRÓXIMO, limites e coordenação.

**Resultados:** 14 anos nos arts.13 Lei8.213 e 14 Lei8.212 desde 1991, contra 16 no Decreto3048 art.11/18 §2; guarda protegida literalmente em 1991, excluída do art16 §2 em 1997 e reinserida pela Lei15108/2025, com EC103 art23 §§4/6/7 e Tema1271 pendente; mandato h incluída em ambas leis em 1997, j em 2004, ResSen26/2005 suspendeu **apenas** h da 8.212 art12 I; exceção de PSA consta da 8.212 art12 §9 VIII, sem inciso VIII na 8.213 art11 §8. **Regime de custeio, benefício e interpretação constitucional não podem ser fundidos como mera operação editorial.**

**Pendente:** fac-símiles DOU e comparação textual independente, versão oficial atualizada da IN RFB2110 (a consulta não retornou conteúdo autenticável), inteiro teor de decisões e conclusão do Tema1271, inventário literal global. Nenhum C0/C1/M nem revogação aprovado. **Próximo F1-E:** fechar fontes e testar equivalência material dos quatro conflitos antes de F2.

## 12. Rodada 06 — F1-E: MP1523/1996, STJ Tema732 e autenticação de fontes

**Errata histórica obrigatória:** a retirada do menor sob guarda da **letra do art.16 §2 Lei8213** ocorreu **já na MP1.523 de 11/10/1996, DOU 14/10/1996, art.2º**, vigente na publicação pelo art.5º. **A Lei9.528/1997 é o marco de conversão posterior, não a primeira redação excludente.** As reedições e eventuais efeitos de perdas/renovações de eficácia de 1996–1997 ainda devem ser auditadas individualmente.

**Precedente qualificado acrescido:** [STJ Tema732 — REsp 1.411.258/RS](https://processo.stj.jus.br/repetitivos/temas_repetitivos/pesquisa.jsp?cod_tema_final=732&cod_tema_inicial=732&novaConsulta=true&tipo_pesquisa=T), julgado **11/10/2017**, publicado **21/02/2018**, trânsito **09/03/2023**: menor sob guarda economicamente dependente pode obter pensão mesmo após MP1523/1996. A tese não resolveu expressamente **EC103/2019 art23 §6º**, sujeito ao STF Tema1271.

**Dados e resultados desta rodada:**
- [F1E_CADEIAS_FONTE_19_EVENTOS.csv](F1E_CADEIAS_FONTE_19_EVENTOS.csv): **19 eventos com fontes e datas**, sem classe de equivalência C0/C1/M.
- [RELATORIO_F1E_RETIFICACAO_MP1996_TEMA732_E_FONTES.md](RELATORIO_F1E_RETIFICACAO_MP1996_TEMA732_E_FONTES.md): fontes primárias e quatro questões F1.
- [F1C_CASOS_TEMPORAIS_18.csv](F1C_CASOS_TEMPORAIS_18.csv) corrigido, IDs **C10/C11** atualizados para marco **14/10/1996** e Tema732, mantendo 18 casos.
- [PACOTE_CONTINUIDADE_RODADA_06.md](PACOTE_CONTINUIDADE_RODADA_06.md): FEITO/PENDENTE/PRÓXIMO.

**Outros avanços:** Senado confirmou DOU31/10/1997 da Lei9506; LexML confirmou DOU21/06/2004 da Lei10887; [RFB oficial](https://normas.receita.fazenda.gov.br/sijut2consulta/consulta/link.action?idAto=126687&visao=original) disponibiliza texto original de IN2110 art9§5 IX (PSA) e histórico de alterações **2024/2025/2026**, mas não foi certificada por dispositivo sua redação final de outubro/2026. **Próximo F1-F:** reconstrução literal da cadeia de reedições da MP1523/1996–1997, inclusive datas/efeitos.

Nenhuma regra CLF foi redigida, nenhuma reforma M foi ratificada, nenhum outro módulo alterado e PR continua draft; F1 parcial e F2 ainda pendente.

## 13. Rodada 07 — F1-F: fechamento documental da cadeia MP1523/1996 a Lei9528/1997

**Cotejo efetivamente executado:** [F1F_CADEIA_COMPLETA_MP1523_1996_1997.csv](F1F_CADEIA_COMPLETA_MP1523_1996_1997.csv) registra **15 MPs** (MP 1.523 inicial, reedições -1 a -13 e MP 1.596-14) **mais a Lei 9.528/1997**. Confronto manual do **art.16 §2 da Lei8.213** por ato e disposições de **convalidação na MP sucessora/lei final**: nas 15 MPs o rol permanece sem menor sob guarda, e Lei9528 **art.2º** o mantém; **art.13** convalida expressamente atos praticados com base nas 15 MPs. Convalidação de atos e texto não significam certificação automática de todos os efeitos individuais ou regularidade constitucional de cada período.

- [Relatório jurídico com fontes individuais, 16 atos, datas e testes temporais](RELATORIO_F1F_CADEIA_MP1523_E_CONVALIDACAO.md).
- [Pacote de continuidade da rodada 07](PACOTE_CONTINUIDADE_RODADA_07.md).

**Duas reservas documentais:** (1) [MP1523-11](https://www.planalto.gov.br/ccivil_03/mpv/1996-2000/1523-11.htm) traz "forma estabelecido", ao contrário de [MP1523-12](https://www.planalto.gov.br/ccivil_03/mpv/1996-2000/1523-12.htm) e das outras versões ("estabelecida"); não é alteração material do rol. (2) [Senado registra DOU 24/10/1997](https://legis.senado.leg.br/norma/555128) para MP1523-13, enquanto rodapé Planalto registra 26/10; conservamos data do Senado e **Q de fonte** até cotejo do DOU fac-símile.

**Marco da proteção judicial:** Tema732/STJ protege menor sob guarda economicamente dependente apesar da exclusão textual de MP1996/lei1997; STF ADIs4878/5083 e questão posterior EC103 art23§6 do STF Tema1271 exigem análise de período e hierarquia. **Próximo: F2-A**, reconstrução do modelo vigente de filiação e dependência, com `Q` preservadas; avançar no mérito do CLF sem repetir transcrições já documentadas.

**Estado:** pesquisa documental por núcleo F1-F concluída em escopo; **F1 do T29 ainda não integral**, C0/C1/M não aprovados, PR draft sem merge.

## 14. Rodada 08 — F2-A: modelo funcional do direito vigente (14/10/2026)

A pesquisa deixou de acumular novos índices históricos para construir **modelo jurídico do RGPS em 33 regras funcionais** — filiação obrigatória/facultativa, qualidade, segurado especial, dependentes e interfaces — e **executar 20 testes analíticos**, com respostas condicionadas às fontes e Q explícitas.

- [F2A_MATRIZ_MODELO_VIGENTE.csv](F2A_MATRIZ_MODELO_VIGENTE.csv) — 33 regras com fundamento, pressuposto, consequência, módulo e grau de verificação;
- [F2A_TESTES_20_CASOS.csv](F2A_TESTES_20_CASOS.csv) — 20 testes realizados de casos hipotéticos de ingresso, qualidade, segurado especial, dependência e inscrição;
- [RELATORIO_F2A_MODELO_VIGENTE_E_20_TESTES.md](RELATORIO_F2A_MODELO_VIGENTE_E_20_TESTES.md) — fluxo decisório e crítica de não regressão;
- [PACOTE_CONTINUIDADE_RODADA_08.md](PACOTE_CONTINUIDADE_RODADA_08.md) — FEITO/PENDENTE/PRÓXIMO.

**Achados de F2:** (i) **filiação obrigatória** pelo exercício de atividade não equivale a inscrição ou pagamento feito pelo responsável; facultativo segue ato de vontade, inscrição e primeiro recolhimento; (ii) período de graça art15 inclui prorrogações e **STJ Tema1360/2026** permite prova idônea de desemprego diversa do registro no Ministério, mas falta isolada de CTPS/CNIS não basta; (iii) **Lei8213 art102 §§1/2 e STJ Súmula416** impedem regra absoluta de perda de pensão por morte quando todos requisitos de aposentadoria estavam preenchidos; (iv) dependentes e segurado especial têm exceções que a codificação não pode apagar.

**Q preservadas:** facultativo de 14–15 anos, assimetria PSA entre Leis8212/8213, STF Tema1271 guarda pós-EC103, limites probatórios/carência de salário-maternidade após ADIs2110/2111. **Nenhum C0/C1/M ou texto CLF aprovado.** **Próximo F2-B:** tempo, sucessão de vínculos, recuperação de qualidade e compatibilidade do conceito único com M02/M05, sem editar módulos vizinhos.

## 15. Rodada 09 — F2-B: dinâmica de vínculos, perda/recuperação e não regressão (14/10/2026)

A reconstrução funcional foi aprofundada com [F2B_TRANSICOES_23_ESTADOS.csv](F2B_TRANSICOES_23_ESTADOS.csv), **23 transições condicionais de estados**, [F2B_TESTES_TEMPORAIS_27.csv](F2B_TESTES_TEMPORAIS_27.csv), **27 testes respondidos** de ingresso, graça, prova, remuneração, retorno, pensão, dependência e mudanças de categoria, e [RELATORIO_F2B_DINAMICA_TEMPORAL_E_NAO_REGRESSAO.md](RELATORIO_F2B_DINAMICA_TEMPORAL_E_NAO_REGRESSAO.md), relatório jurídico detalhado.

**Achados qualificados:**
1. **STJ Tema1360** — julgamento **11/03/2026**, publicação **19/03/2026**, trânsito **21/05/2026**; a notícia de julho é posterior. Desemprego involuntário provado por meios idôneos (incluindo no processo administrativo), sem formalismo de registro estatal exclusivo; CTPS/CNIS isoladamente insuficientes.
2. **Art. 27-A da Lei8213** — nova filiação e aproveitamento de carência **não são idênticos** à retomada da qualidade; o texto ainda menciona salário-maternidade, cuja carência prevista no art25 III foi invalidada pelas **ADIs2110/2111/STF**. Não reconstituir exigência inconstitucional por interpretação do art27-A.
3. **STJ REsp1.346.852/PR e Informativo525** — impossibilidade de **recolhimento post mortem de CI responsável por suas próprias contribuições** para formar qualidade e pensão; não equiparar à omissão do empregador em recolher contribuição de empregado.
4. **Lei8213 art102 e STJ Súmula416** — direito adquirido à aposentadoria e exceção da pensão depois de perda de qualidade quando havia requisitos completos em vida; art15§4 exige termo exato de vencimento, sem datas presumidas.
5. **Teste específico do período de graça**: art15§3 mantém direitos no prazo; não converter lacuna de recolhimento corrente em negativa automática.

A validação estrutural dos CSVs confirmou **23 transições, 27 testes, IDs únicos, fontes/campos preenchidos e zero remissões a IDs inexistentes**. Os seis IDs funcionais da F2-A não exercitados na rodada anterior foram incluídos em testes desta rodada; **não significa cobertura de todas as exceções materiais do RGPS**.

[Continuidade da rodada 09](PACOTE_CONTINUIDADE_RODADA_09.md). **Próximo: F2-C**, estrutura unificada de pessoa/vínculo/dependência com separação de qualificação, custeio e prestações, e controle de não regressão dos **47 cenários** F2-A/F2-B. F1 ainda seletiva, F2 parcial; nenhuma C0/C1/M aprovada, PR draft, módulos vizinhos e `main` intocados.

## 16. Rodada 10 — F2-C (14/10/2026)

F2-C consolidada: [15 entidades jurídicas](F2C_ESQUEMA_CONCEITUAL_15_ENTIDADES.csv), [56 concordâncias funcionais](F2C_CONCORDANCIA_FUNCIONAL_56_REGRAS.csv) e [47 casos reavaliados](F2C_AUDITORIA_NAO_REGRESSAO_47_CASOS.csv), sendo 40 controles conceituais condicionais e 7 Q retidas. O [relatório jurídico](RELATORIO_F2C_MODELO_UNIFICADO_CONCORDANCIA_E_TESTES.md) distingue pessoa, vínculo, filiação, qualidade temporal, inscrição, contribuição, benefício e relação de dependência. O [pacote de continuidade](PACOTE_CONTINUIDADE_RODADA_10.md) encaminha F3-A comparada.

Nenhuma regra C0/C1/M foi proposta como aprovada. Permanecem Q facultativo 14/16, PSA, guarda pós EC 103/Tema 1.271 e interfaces contributivas. PR draft; main e outros módulos sem alterações.

### Adendo de coordenação — duas versões F2-C no mesmo PR

Durante a rodada foram identificados **dois conjuntos F2-C em paralelo na mesma branch**. O conjunto anterior mapeia [15 entidades](F2C_ESQUEMA_CONCEITUAL_15_ENTIDADES.csv), [56 regras/transições](F2C_CONCORDANCIA_FUNCIONAL_56_REGRAS.csv) e 47 testes (40 condicionais, 7 Q). O complemento adiciona [19 entidades refinadas](F2C_MODELO_ENTIDADES_E_VINCULOS.csv), [34 grupos de concordância por fonte](F2C_CONCORDANCIA_ORIGEM_CONCEITO_DESTINO.csv), [20 garantias](F2C_INVARIANTES_DE_NAO_REGRESSAO.csv), [47 regressões](F2C_REGRESSAO_47_CENARIOS.csv) e [4 testes novos](F2C_TESTES_ADICIONAIS_COLISAO_2026.csv).

**Não comparar 56 e 34 como contagens do mesmo objeto; não somar entidades nem escolher uma versão canônica sem revisão.** A auditoria cruzada encontrou **9 casos com marcação de Q divergente** entre as duas matrizes de 47 cenários. A [nota de conciliação](F2C_NOTA_DE_CONCILIACAO_E_CONTROLE_DE_DUPLICIDADE.md) documenta todos eles e estabelece **14 casos sob revisão conservadora** até decisão jurídica individual.

**Novo problema intermodular:** [Lei15.371/2026](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/lei/l15371.htm) inseriu **art.73-A de salário-paternidade**, vigência **01/01/2027**, enquanto [Lei15.415/2026](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/lei/l15415.htm), vigente desde **26/05/2026**, inseriu **outro art.73-A sobre salário-maternidade**. A colisão de número e vigência foi analisada no [relatório complementar](RELATORIO_F2C_ARQUITETURA_CONCORDANCIA_E_CHOQUE_ART73A.md); **não há solução de revogação, renumeração ou primazia aprovada**. Módulos de benefícios e governança deverão tratar a questão.

**Próximo controle antes de F4/F5:** conciliar modelos E/P e nove casos em F2-D, unificando a responsabilidade sobre o T29.M01 para impedir terceira rodada F2-C repetida; F3-A comparativa é trabalho distinto e pode prosseguir sem converter Q em norma.

### Retificação de coordenação da F2-C

Ao final da rodada surgiram duas séries F2-C no mesmo PR. A [nota de reconciliação](NOTA_F2C_RECONCILIACAO_DUAS_TRILHAS.md) fixa **provisoriamente P19 (19 entidades, 20 invariantes, 34 origens normativas)** como referência e **E15 (15 entidades, 56 regras/transições)** como controle cruzado, não duas frentes independentes. Os **47 casos são os mesmos**, com **quatro adicionais** na série P (51 hipóteses distintas). Status de dúvida não é equivalente entre séries. O relatório P identificou **dois dispositivos previstos como art. 73-A da Lei8.213**, um vigente de salário-maternidade desde 26/05/2026 (Lei15.415) e outro de salário-paternidade com vigência em 01/01/2027 (Lei15.371); efeitos futuros são Q e exigem interface M05/M06/T01. **Não usar este README para concluir renumeração, revogação ou C1.**

## 17. Rodada 11 — F3-A comparada (14/10/2026)

**Escopo independente da F2-D e sem minuta legal:** pesquisa comparada de **Alemanha, Espanha, Portugal e Uruguai**, mais OIT, em [17 mecanismos documentados](F3A_MATRIZ_COMPARADA_17_MECANISMOS.csv). O [relatório F3-A](RELATORIO_F3A_DIREITO_COMPARADO_E_OPCOES_PRELIMINARES.md) distingue organização legislativa, filiação, cadastro, responsabilidade contributiva, proteção em períodos sem contribuição e prova da atividade. **Não atribui causalidade nem transplanta requisitos estrangeiros para o RGPS**.

[Três alternativas qualitativas confrontadas com dez riscos (30 cruzamentos)](F3A_TESTE_TRES_ARQUITETURAS_30_RISCOS.csv): (A) núcleo comum e especialidades de M02/M03–M05/M06/M07; (B) regimes separados com coordenação; (C) unificação integral, de alto risco para direitos e custeio. São **candidatas a F4**, não decisão aprovada, C1 ou M.

[Agenda brasileira de dez indicadores](F3A_AGENDA_EVIDENCIA_BRASIL_10_INDICADORES.csv) identifica BEPS 2026, Transparência INSS, painéis RGPS e TCU/CNIS, **sem fingir coleta de números nem eficácia empírica comprovada**. [Continuidade rodada 11](PACOTE_CONTINUIDADE_RODADA_11.md). **Próximo F3-B:** levantar dados de implementação, cadastro, prova e litígio com denominadores e fontes auditáveis; a F2-D de conciliação anterior segue responsabilidade distinta. Nenhum arquivo de outros módulos ou `main` alterado; PR draft.

## 18. Histórico


- **14/10/2026, rodada 01:** abertura independente do T29.M01 após checar catálogo e ausência de frentes T29 abertas; F0 e F1 seletiva registrados em branch e PR próprio; nenhum arquivo `main` ou T24 modificado.
