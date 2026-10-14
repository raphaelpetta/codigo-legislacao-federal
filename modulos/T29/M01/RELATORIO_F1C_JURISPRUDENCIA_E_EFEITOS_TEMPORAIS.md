# T29.M01 — F1-C: jurisprudência, situações por período e testes de não regressão

**Data de corte:** 14/10/2026 · **Issue:** [#40](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/40) · **PR:** [#41 — draft](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/41). **Base `main` CLF:** `16fba172c875c7a0de388288fe70005c944021d6`. **Responsável exclusivo:** T29.M01.  
**Objeto:** testar, e não reinventariar, quatro Q identificadas em F1-B. O [arquivo de 18 casos temporais](F1C_CASOS_TEMPORAIS_18.csv) é instrumento analítico, **não decisões jurisdicionais novas, parecer vinculante nem simulação empírica**. Cada registro separa fato hipotético, data, fonte, posição justificável e Q.

## 1. Fontes oficiais e padrão de prova

**Decisões constitucionais / interpretação:**
1. [STF Tema 691 — RE 626.837/GO, registro e tese](https://portal.stf.jus.br/jurisprudenciaRepercussao/verAndamentoProcesso.asp?classeProcesso=RE&incidente=3916429&numeroProcesso=626837&numeroTema=691): mérito 25/05/2017, acórdão DJE 01/02/2018, trânsito 21/02/2018, **tese fixada e situação confirmadas na ficha**. Matéria específica: contribuição sobre remuneração de agentes políticos após Lei 10.887/2004 sem RPPS.
2. [STF RE 351.717/PR — Informativo 330](https://stf.jus.br/arquivo/informativo/documento/informativo330.htm) (2003) e [manifestação oficial no Tema 691](https://portal.stf.jus.br/jurisprudenciaRepercussao/verPronunciamento.asp?pronunciamento=4623556): inconstitucionalidade da norma que instituiu contribuição pela Lei 9.506/1997 sob CF art.195 na redação anterior à EC20; EC20 **não convalida** lei anterior inconstitucional.
3. [STF ADIs 4.878 e 5.083 — ementa e resultado reproduzidos na ficha STF](https://portal.stf.jus.br/jurisprudenciaRepercussao/verPronunciamento.asp?pronunciamento=10615600), DJe 06/08/2021, e [Informativo 1.020/STF](https://stf.jus.br/arquivo/informativo/documento/informativo1020.htm): interpretação conforme do art.16 §2º da Lei 8.213 para menor sob guarda com **dependência econômica comprovada**. Não atesta decisão sobre a validade da EC103 art.23 §6º.
4. [STF Tema 1.271 — RE 1.442.021, ficha e movimentos](https://portal.stf.jus.br/jurisprudenciaRepercussao/verAndamentoProcesso.asp?classeProcesso=RE&incidente=6661561&numeroProcesso=1442021&numeroTema=1271): repercussão geral reconhecida; a movimentação mais recente do processo disponibilizada **16/04/2026** indica autos conclusos ao relator com parecer PGR; **tese final de mérito não localizada** em 14/10/2026.
5. [STF ADIs 2.110/2.111, dispositivo e decisão de 21/03/2024](https://portal.stf.jus.br/processos/detalhe.asp?incidente=1795149) e [CF art.201, página STF com excerto da ementa](https://portal.stf.jus.br/constituicao-supremo/artigo.asp?abrirArtigo=201&abrirBase=CF): declarada inconstitucional a carência de salário-maternidade de classes específicas (Lei 8.213 art.25 III), por tratamento desigual de seguradas. **Qualidade de segurada** é requisito distinto de **carência**; essa distinção não autoriza criar sem prova uma carência disfarçada.

**Decisão específica nova, não vinculante nacional:**
6. [TRF3, 11ª Turma Recursal/SP, processo 5002988-56.2025.4.03.6322, documento integral no portal do tribunal](https://web.trf3.jus.br/acordaos/Acordao/BuscarDocumentoPje/395087868): caso de adolescente nascida em 28/03/2010, contribuição facultativa em 06/2025 paga em 02/07/2025, parto em 05/08/2025. **Sentença negou em razão de idade 15**; o **voto condutor do acórdão afirmou expressamente que 15 anos, por si só, não é impedimento legal à filiação**, mas manteve improcedência pelo entendimento de que o único recolhimento realizado durante gravidez constituiu vinculação instrumental sem filiação efetiva. Acórdão **por maioria**, com voto vencido não acessado no documento. **A data específica de julgamento/publicação não foi verificada**, não inventar. A conclusão tem alcance de caso, não enunciado nacional nem repetitivo.
7. [INSS Portaria DIRBEN/INSS 991/2022, art.424-A inserido por Portaria 1.132/2023](https://portalin.inss.gov.br/portaria991): proteção por salário-maternidade ao titular menor de 16 em certas hipóteses com trabalho precoce, fundada em ACP. **Não confundir proteção de segurado obrigatório que trabalhou irregularmente com filiação exclusivamente voluntária sem trabalho.** Versão consolidada atual do portal deve ser revalidada ao usar a regra.

**Legislação e interpretação administrativa:**
8. [CF/1988 e EC 103/2019, art.23 §§4º, 6º e 7º](https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc103.htm): §4º remete rol à Lei 8.213; §6º diz "exclusivamente enteado e menor tutelado"; §7º admite alterações legais para regimes especificados. A coexistência desses dispositivos é razão jurídica de Q29-GUARDA.
9. [Lei 15.108/2025](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15108.htm), vigente desde publicação no DOU 14/03/2025: acrescentou expressamente menor sob guarda judicial ao art.16 §2º, mediante declaração do segurado e insuficiência de meios para próprio sustento e educação.
10. [Resolução Senado 26/2005](https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2005/congresso/ressf26-05.htm), publicada DOU 22/06/2005: suspendeu **expressamente e apenas** Lei 8.212 art.12 I h, não a posterior alínea j ou, pelo seu dispositivo, o art.11 I h da Lei 8.213.
11. [Lei 14.119/2021, art.23](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14119.htm): incluiu PSA no §9º VIII do art.12 Lei 8.212, sem inseri-lo no §8 do art.11 Lei 8.213. O art.17 da Lei 14.119 regula tributos determinados, com texto posteriormente promulgado após veto; **não equivale a exoneração de toda contribuição**.
12. [IN RFB 2.110/2022 — portal institucional, versão original e histórico de alterações](https://normas.receita.fazenda.gov.br/sijut2consulta/consulta/link.action?idAto=126687&visao=original): art.9 §5º IX identifica PSA como hipótese que não descaracteriza segurado especial para classificação contributiva, com remissão à Lei 8.212 art.12 §9 VIII. **Há alterações posteriores 2024, 2025 e 2026**; consulta à versão original demonstra recepção administrativa fiscal, não certifica cada palavra do regulamento vigente após a alteração de 06/04/2026. [Cópia em PDF identificada como IN RFB 2110/2022, edição 23/02/2024, em diário municipal](https://diariooficial.prefeitura.sp.gov.br/md_epubli_visualizar.php?Vzp-k1rWH0K9VTSZLBt8hmNCVG8naCwsm6yoV-AlgB6g74JB5Ji7jdTYEQLu7_Mxzz1PzfVqxS86zQC5v58lwKa_GbTZEIIs7tYGk_CbCOFZRJTGyE2yQ8bfCdQq8aT-=) confirma que a regra aparecia em uma versão publicada anteriormente, **sem substituir a fonte federal oficial**.

**Estado do material:** leis/artigos, ementas, dispositivo do RE Tema691, informativos e portal de acórdão TRF3 foram consultados; **nem todos os inteiros teores do STF, votos vencidos, versões históricas do DOU e atos regulamentares pós-2024 foram lidos**. Isso delimita as afirmações.

## 2. Resultado por controvérsia

### 2.1 Mandato: a validade da contribuição posterior a 2004 deixou de ser Q

Antes da EC20, a Lei 9.506/1997 havia criado base contributiva para detentor de mandato eletivo, declarada inconstitucional pelo RE351717. A alteração constitucional de 1998 não convalidou essa lei. A **Lei 10.887/2004**, com nova alínea **j** em Lei 8.212 art.12 I, passou a fornecer fundamento próprio; em 2017 a tese do **Tema 691**, transitada em 2018, validou a contribuição após a lei para agente sem regime próprio.

**Correção necessária à F1-B:** não classificar `Q29-MANDATO` como "validade das contribuições pós-2004 ainda indeterminada". Há **tese vinculante**, com ressalvas sobre anterioridade, competências limítrofes e pessoa vinculada a RPPS. A Resolução Senado26/2005 permanece limitada à **alínea h da Lei 8.212**, e o destino documental do homônimo h na Lei 8.213 depende de exame jurídico próprio; não remover textualidade silenciosamente. O **CF art.40 §13** (redação EC103) trata de ocupação temporária/mandato e é parâmetro adicional, com exceções federativas a examinar.

**Teste:** cobrança patronal referente a competência de 2001 não se torna legítima por citar EC20 e lei de 2004; cobrança de 2006 a agente sem RPPS deve ser avaliada pela nova previsão, Tema691 e fatos e recolhimentos, sem invocar a suspensão de h contra j.

### 2.2 Idade 14/16: primeira decisão diretamente sobre contribuinte de 15 anos

Lei 8.213 art.13 e Lei 8.212 art.14 mantêm "maior de 14 anos". Decreto3048 art.11 e prática INSS adotam maior de 16. A CF art.7 XXXIII proíbe trabalho precoce (com ressalva do aprendiz), **não enuncia literalmente idade mínima da filiação voluntária de quem não trabalha**.

No processo **5002988-56.2025.4.03.6322**, a **11ª Turma Recursal de SP** afastou o fundamento etário de improcedência da sentença: *a idade de 15, isoladamente, não obsta filiação facultativa*. Contudo, pela maioria, o acórdão negou a prestação por interpretação de filiação "instrumental" do único pagamento próximo do parto. Trata-se de **posição judicial não uniforme automaticamente aplicável em todo o país**; não há neste conjunto repetitivo ou tese STF sobre o específico caso de 15 anos sem atividade.

**Crítica jurídica estruturada:** ADIs 2110/2111 afastaram a carência do salário-maternidade. O direito à proteção à maternidade não permite, sem prova específica, presumir fraude apenas porque houve contribuição única e gravidez anterior. Cabe verificar se a ideia de "filiação efetiva" acrescenta requisito sem previsão legal, tornando a inexistência de carência uma ficção. Não se declara que o acórdão TRF3 seja definitivamente inválido: o registro contém apenas o voto vencedor e não documenta eventuais provas de fraude ou a via recursal ulterior; **questão adversarial aberta**. Uma minuta CLF deve diferenciar expressamente **a) data e ato de filiação; b) recolhimento tempestivo; c) requisito de carência, quando permitido; d) fraude concreta e seu ônus de prova**.

**Teste:** adolescente de 15 anos sem trabalho com contribuições regulares x adolescente 15 anos que recolhe uma vez antes de parto; idade legal é a mesma, e a diferença na aplicação não pode ser automaticamente explicada por carência inconstitucional. Proteção ao aprendiz/ao adolescente que efetivamente trabalhou (Portaria991 art424-A) constitui classe distinta.

### 2.3 Guarda: proteção legal positiva + Q constitucional de abrangência

As ADIs 4878/5083 resolvem a interpretação do **art.16 §2 da Lei 8.213 sob CF art.227** para proteção de menor sob guarda com prova de dependência. EC103 art.23 §6º contém **equiparação exclusivamente a enteado/tutelado** para pensão, mas §§4 e 7 estabelecem remissão ao rol legal e possibilidade de alteração legislativa. A Lei 15.108/2025 protege expressamente a guarda.

No **Tema1271/STF** a constitucionalidade da exclusão pela EC103 §6º é objeto exato de repercussão geral. A última movimentação encontrada na ficha oficial foi 16/04/2026 (autos conclusos; PGR pelo não provimento), **sem tese de mérito publicada até o corte da consulta**. **Não confundir parecer da PGR com julgamento nem a ementa das ADIs sobre lei com decisão específica sobre a emenda.** O §7º da EC também exige análise antes de atribuir à Lei 2025 conflito automático absoluto com §6º.

**Três recortes:** óbito anterior a 13/11/2019 (lei e interpretação conforme); óbito de 13/11/2019 a 13/03/2025 (EC103 §6 com regime legal então existente); óbito desde 14/03/2025 (Lei15108 e EC). Em cada faixa importa a data do evento, tipo de dependência, guarda formal, declaração, prova econômica, direito adquirido e efeitos dos julgados; a classificação como Q **não autoriza negativa automática**.

### 2.4 PSA: divergência textual, mas já há aplicação administrativa fiscal

A Lei8212 art.12 §9 VIII expressamente protege participação em programa de pagamento por serviços ambientais como fato isolado não descaracterizador de segurado especial. O art.11 §8 da Lei8213 não ganhou inciso idêntico. Agora consta evidência adicional de aplicação: **IN RFB2110/2022 art.9 §5 IX** adotou essa exceção no enquadramento de segurado especial. Isso reduz a hipótese de a lei de custeio ser "letra morta", mas **não certifica uniformidade administrativa do INSS em concessão de aposentadorias, nem elimina diferenças sobre rendimento e tributos**.

**Três testes:** agricultor familiar que recebe PSA por conservação ambiental sem abandonar atividade rural → não perder condição automaticamente; empresa de consultoria vendendo serviços ambientais sem trabalho em economia familiar → não ganhar segurado especial automaticamente; beneficiário recebendo PSA com atividade remunerada paralela → verificar exceções do §9/§10 de ambas leis, art.17 Lei14119 e natureza do contrato.

**Próxima interface:** solicitar a T29.M02/T12 cruzamento de renda PSA, incidência contributiva e aplicação IN RFB **na versão atualizada de 2026**; esta frente não redigirá regras tributárias novas.

## 3. Concordância jurídica — aceites parciais e reservas

| Questão | F1-C demonstrou | O que segue Q | Proteção de codificação |
|---|---|---|---|
| Mandato | Tema691/STF, mérito e trânsito: validade contributiva **pós-Lei10887** sem RPPS; Res26 atinge h do art.12/8.212 | Competências fronteiriças, alcance à h da 8.213 e atos pretéritos | Enquadramento temporal e base sem retroatividade |
| Idade | Existe decisão TRF3/SP diretamente favorável a **15 anos como idade admissível em tese** | Eficácia nacional, caso de uma contribuição e exigência implícita de filiação efetiva | Evitar restrição por decreto ou carência disfarçada sem avaliação |
| Guarda | ADIs 2021 sobre 8.213 e lei expressa 2025; §6 EC103 é alvo do Tema1271 | Mérito do Tema1271, efeitos e interpretação dos §§4/6/7 | Preservar criança/dependência e não ocultar Q constitucional |
| PSA | Lei positiva e recepção na IN RFB 2110 art9 §5 IX | Benefícios INSS, natureza do pagamento/tributação, versões 2026 | Unificar só após provar que direitos/prestações não recuam |

Nenhuma linha acima autoriza `C0-J` ou `C1`; `M` não foi redigido nem ratificado. **Decisão temática futura pode ser: manter remissões separadas (controle), unificar com garantias demonstradas, ou propor reforma material explícita**, mas escolher agora apagaria informações necessárias.

## 4. Problemas adicionais identificados em revisão adversarial

- **Desvio de carência por interpretação de oportunismo:** exigir histórico contributivo após STF eliminar a carência exige fundamento autônomo para fraude ou invalidade de filiação, sob pena de produzir requisito temporal disfarçado. A hipótese de **uma contribuição após início de gestação** não é por si critério legal expresso de exclusão do benefício.
- **Administração não é lei:** a Receita dispõe sobre custeio e o INSS sobre reconhecimento prestacional; nenhum ato isolado supera a lei, e ambos são sujeitos a edição posterior. A IN RFB 2110 tem alterações em **2024, 2025 e 2026** segundo metadados oficiais; não transportar versão anterior como vigente sem nova verificação.
- **CF futura separada:** falta revisão específica das garantias previdenciárias no último texto da CF-projeto; a pesquisa jurídica descreveu a CF/1988 vigente e EC103, sem criar norma constitucional por inferência.
- **Portabilidade de precedentes:** STF Tema691 é qualificado e vinculante no recorte contributivo; TRF3 é decisão de caso concreto; Tema1271 repercussão geral ainda sem mérito; ADIs4878/5083 dizem respeito à lei ordinária. Usar a mesma categoria de "jurisprudência" para todos produziria falso equivalente.
- **Origens F1-A:** os 198 registros anteriores são localizações funcionais, não lista certificada de 198 dispositivos positivos; não contá-los como todos C0 nem repetir sua transcrição.

## 5. Estado e critério da próxima rodada

**FEITO:** 18 testes/posições datadas e precedentes/atos primários; a tese **Tema691** reduziu a Q29-MANDATO, **TRF3 caso 15 anos** reorientou a análise da filiação facultativa, **IN RFB2110** reforçou PSA, e Tema1271 foi revalidado como pendente na última fonte consultada.

**PENDENTE:** íntegra dos acórdãos STF/ADI e eventual modulação, histórico de MP/DOU das alíneas 1997/2004, resultado superveniente do Tema1271, jurisprudência sobre ato único de filiação e proteção à maternidade, atualização da IN RFB2110 em 2026 e aplicação INSS sobre PSA, efeitos temporais individualizados, auditoria literal dos 198 registros e legislação previdenciária restante.

**PRÓXIMO — F1-D:** seleção e auditoria literal/histórica de **dispositivos críticos**, sem reconstruir toda a matriz: Lei8213 art.13 e art.16 §2; Lei8212 art.14, art.12 I h/j e §9 VIII; EC103 art.23 §§4/6/7; Decreto3048 art.11 e IN RFB2110 art.9 §5 IX. **Aceite:** par de textos em versões autenticadas, histórico DOU e decisões por efeito, sem declarar homologação CLF; manter a pesquisa de benefícios (T29.M05) e tributação (T29.M02) nas respectivas frentes.

**Controles:** F1 ainda parcial, nenhuma redação CLF nem revogação aprovada, PR permanece draft; a `main` não foi alterada.
