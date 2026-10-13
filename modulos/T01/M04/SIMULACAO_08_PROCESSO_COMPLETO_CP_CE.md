# T01.M04 — Simulação integral do processo de promulgação: CP versus CE

**ID:** CLF-T01-M04-SIM08 · **Data de corte:** 13/10/2026 · **Estado:** SIMULAÇÃO INSTITUCIONAL HIPOTÉTICA, não projeto de lei, não parecer conclusivo.  
**Baseline do CLF:** `3a5a4977b51b4666d16ab453769ed98cb0442982`; **baseline da Constituição alternativa:** `4c728c0bc5ef1d5c9fb6b4d76a20286f759704fb`.  
**Decisões:** objetivo `DEC-001` de Código único preservado; veículo `DEC-016` **PENDENTE**; propostas CP/P3 e CE/P4 **NÃO RATIFICADAS**.  
**Dados de teste:** `MATRIZ_ETAPAS_CP_CE_08.csv` (estados por caso/etapa) e `FALHAS_E_DECISOES_CP_CE_08.csv` (ramos adversariais). **Nenhum artigo desses diplomas foi realmente incorporado a um Código novo.**

## 1. Estado de direito comprovado e correção metodológica do piloto

**Três componentes atuais selecionados, em vez de tratar norma histórica revogada como vigente:**

| Componente | Dispositivo fonte em 13/10/2026 | Regime que importa | Destino de teste |
|---|---|---|---|
| **T — reservado** | CTN, art. 174, Lei 5.172/1966, com alterações da **LC 236/2026** | Regra de prescrição tributária geral **materialmente complementar**, CF art. 146, III, b; STF SV 8 | `CLF-T12-M01-TESTE-T` |
| **O — ordinário** | Lei **9.784/1999, art. 2º**, princípios e critérios de processos administrativos federais | Lei formal ordinária, sem reserva específica de LC para esse dispositivo demonstrada; observância dos direitos fundamentais constitucionais | `CLF-T07-M03-TESTE-O` |
| **J — iniciativa judicial** | Lei **11.416/2006, arts. 11–13** sobre remuneração de servidores do Judiciário da União | Lei ordinária; alterações materiais abrangidas pela iniciativa dos tribunais conforme art. 96, II, b, da CF. **Nem todo enunciado da lei exige a mesma conclusão sem análise.** | `CLF-T-SETOR-JUD-TESTE-J` (título/módulo definitivo a definir) |

**Fonte histórica auxiliar H (NÃO é componente positivo vigente):** antiga LC 70/1991, art. 6º, II, e Lei 9.430/1996, art. 56, STF Tema 71 e SV 62: ensina que matéria ordinária em LC formal não fica artificialmente reservada. A simulação de atualidade **usa a Lei 9.784/1999 no componente O**; não transporta antiga isenção da COFINS como direito atual.

**Alerta de controle de versão obrigatoriamente aplicado:** a LC 236/2026 alterou a disciplina do CTN, mas o projeto teve **veto parcial documentado na Mensagem presidencial 743/2026**, com veto a fragmentos propostos para **§1º e §2º e §4º do art. 174**, conforme cadastro legislativo oficial. **Texto vetado não se torna lei porque constava do projeto.** Assim, o `T` positivo deve derivar do texto **efetivamente promulgado**, com confronto da redação compilada e da situação de vetos até o corte — jamais de cópia integral do projeto e suas alíneas vetadas. O teste simula veto **futuro**, independentemente daquele veto real.

Fontes oficiais:
- CF/1988 arts. 47, 59, 61, 65–66, 69, 96, 146: https://www2.camara.leg.br/legin/fed/consti/1988/constituicao-1988-5-outubro-1988-322142-normaatualizada-pl.html ;
- CTN atualizado: https://www2.camara.leg.br/legin/fed/lei/1960-1969/lei-5172-25-outubro-1966-358971-normaatualizada-pl.html ;
- LC 236/2026 e veto oficial: https://www2.camara.leg.br/legin/fed/leicom/2026/leicomplementar-236-4-setembro-2026-799905-norma-pl.html e https://www2.camara.leg.br/legin/fed/leicom/2026/leicomplementar-236-4-setembro-2026-799905-veto-181229-pl.html ;
- Lei 9.784/1999 atualizada: https://www2.camara.leg.br/legin/fed/lei/1999/lei-9784-29-janeiro-1999-322239-normaatualizada-pl.html ;
- Lei 11.416/2006 atualizada: https://www2.camara.leg.br/legin/fed/lei/2006/lei-11416-15-dezembro-2006-548306-normaatualizada-pl.html ;
- STF art. 66, que reproduz julgados sobre veto e iniciativa: https://portal.stf.jus.br/constituicao-supremo/artigo.asp?abrirArtigo=66&abrirBase=CF .

**Controle de interpretação:** `O` deriva de lei ordinária, mas eventual mudança não pode suprimir garantias constitucionais de contraditório, motivação, devido processo, etc. `J` é regime institucional com iniciativa do titular constitucionalmente competente, e a dúvida sobre transposição `C0` por parlamentar permanece registrada na issue CLF #14.

## 2. Premissas da simulação, não direito brasileiro vigente

Simulamos uma **Constituição alternativa ainda NÃO adotada** em que:
- **CP/P3**: um procedimento coordenado tenta produzir ato jurídico formalmente único, mantendo espécies legislativas já existentes. Como não há regra constitucional completa sobre o **estatuto jurídico do ato final**, tratá-lo como `BLOQUEADO_ATO_FINAL` até norma constituinte suficiente; não confundir aprovações setoriais com promulgação una.
- **CE/P4**: a Constituição hipotética cria expressamente `Código da Legislação Federal` como corpo normativo positivo uno, mas **sem** converter toda norma em matéria de reserva reforçada; cada classe conserva iniciativa, quórum, proteção e controle por conteúdo. Isto é solução **condicional**: ainda requer disciplinar sanção/veto, emenda bicameral, texto final e alteração futura.

**Nenhum voto, data de deliberação, sanção ou veto abaixo ocorreu na realidade.** "Aprovado" nas planilhas refere-se exclusivamente a **resultado pressuposto de cenário simulado**. O sistema não deve apresentar `simulacao_aprovada` como norma promulgada.

## 3. Linha de produção comum e estados verificáveis

| Fase | Ato simulado | Controle jurídico | Saída permitida |
|---|---|---|---|
| S00 | Inventário e redação de dispositivo fonte e versão | Fonte vigente, vetos, datas, efeitos, remissões | `FONTE_AUDITADA` ou `BLOQUEADO_FONTE` |
| S01 | Classificação da regra: T/O/J | Competência, reserva **material**, iniciativa, procedimento, direito intertemporal | `CLASSIFICADO` ou `PENDENTE` |
| S02 | Início formal do projeto componente | Autor competente; para J, proposta pelo tribunal titular quando houver reforma material | `INICIADO_VALIDAMENTE` ou `SEM_INICIATIVA` |
| S03 | Primeira Casa vota cada componente | Maioria material adequada; publicidade; não mascarar `M` de `C0` | `APROVADO_1` ou `REPROVADO` |
| S04 | Casa revisora examina | Se modificar, reapreciação pela iniciadora, CF vigente art. 65; regime da nova CF a definir | `APROVADO_2` ou `DEVOLVIDO` |
| S05 | Comissão técnica reconcilia números e referências | Nenhuma inovação material sem retorno ao autor/quórum apropriados | `TEXTO_COERENTE` ou `RETORNO_DE_MERITO` |
| S06 | Voto final de integração | Não substituir votos exigidos da etapa S03/S04; tema de competências conjuntas | `INTEGRAÇÃO_VOTADA`, **não** promulgação |
| S07 | Sanção/veto/promulgação | **Hipótese essencial ausente** em CP e **incompleta** em CE: unidade de veto e responsabilidade do promulgador | `BLOQUEADO_ATO_FINAL` ou `APTO_CONDICIONAL` |
| S08 | Publicação do **texto promulgado** | Registrar versão autoritativa, número, atos originais e dispositivos de destino | `POSITIVADO` apenas se houver autorização constitucional e atos reais |
| S09 | Revogação formal e transição | Não revogar lei antiga sem substituto eficaz; ressalvas de relações e efeitos residuais | `SUBSTITUICAO_CONTROLADA` |
| S10 | Primeira lei alteradora do Código | Regime conforme conteúdo: T/LC; O/ordinário; J/iniciativa judicial para mérito reservado | `ALTERADO_VALIDAMENTE` se satisfeitas condições |
| S11 | Revisão e controle | Divergência publicada, controle jurisdicional, correção/errata, manutenção de versões | `TRILHA_AUDITAVEL` |

**Regra de bloqueio:** nenhuma fase S08–S10 será qualificada como conclusão jurídica real sem **aprovação efetiva**, conforme a Constituição realmente aplicável. Em CP, a ausência de desenho de S07 bloqueia conceitualmente a promessa de ato único; em CE, S07 ainda necessita de regras constitucionais próprias.

## 4. Caso T (CTN art. 174) — ciclo de lei reservada

**Iniciativa:** para transposição `C0` o tratamento depende de prova de equivalência/controle institucional; reformas `M` precisam respeitar CF art. 146, III, b, e demais competências. **Trâmite simulado:** componente identificado `T`; maioria constitucional exigida para LC na aprovação; reconhecimento da aprovação pela revisora; conciliação sem alterar causa interruptiva ou prazo.

**Veto de teste:** o Executivo veta um **parágrafo completo** de disposição do componente T (hipótese), observando a regra de unidade do art. 66, §2º, vigente na CF/1988 — ou disciplina nova especificada pelo constituinte. O componente veto pode ser crucial para integridade da cláusula de revogação de artigos anteriores. Se retirado fragmento do texto do novo Código, a hipótese **não permite revogar automaticamente** o art. 174 original sem norma positiva substitutiva coerente.

**Primeira alteração posterior:** norma nova quer adicionar/retirar hipótese de interrupção. Isso é `M`, sujeito a exigência constitucional de instrumento/quórum materialmente complementar — mesmo que o corpo do Código seja de espécie CE. A publicação digital não faz a mudança.

## 5. Caso O (Lei 9.784/1999 art. 2º) — disciplina legal ordinária e direitos

**Iniciativa:** exercício do regime geral onde não incida reserva especial por conteúdo. Para transposição `C0`, rastrear princípios, critérios do parágrafo único e efeitos jurisprudenciais. Não suprimir termos como `segurança jurídica`, `contraditório` ou garantias de direitos sob pretexto de fusão.

**Trâmite:** aprovação por maioria exigida para lei ordinária na Constituição vigente, e por equivalente funcional na nova Constituição. Se uma matéria materialmente ordinária for promulgada dentro de Código CE, a **primeira alteração posterior** deve poder usar procedimento ordinário (com iniciativa compatível), sem exigir quórum de LC por causa do ato global original. **Fonte histórica separada:** STF SV 62 sobre LC 70 demonstra problema de classificação, mas não informa a reserva específica da Lei 9.784.

**Veto de teste:** veto hipotético a todo inciso do parágrafo único, não a frase isolada; a remoção pode afetar deveres de motivação/proteção de administrados. Submeter a teste de direitos, remissões e coerência antes de liberar revogação correspondente.

## 6. Caso J (Lei 11.416/2006 arts. 11–13) — iniciativa privativa

**Hipótese favorável J1:** titular judicial competente inicia validamente a proposição de reforma material do seu âmbito; Parlamento aprova com rito, limita emendas de matéria reservada e concilia sem modificar benefícios. CE **poderia** transformar esse componente em parte do corpo uno, se procedimento constitucional futuro disciplinar expressamente apropriação, promulgação e emendas.

**Hipótese adversarial J2:** tribunal não inicia o componente; Parlamento quer promover reedição formal integral por projeto comum. Sob CF/1988, **não se presume que a LC 95/1998 art. 14 §2º supere reserva de iniciativa** quando há revogação/reedição. Na Constituição nova é possível **estudar** rito de certificação de neutralidade com participação do titular, mas não há fórmula aprovada. **Resultado correto:** componente J não ingressa; Lei 11.416 permanece vigente em sua esfera. Qualquer texto único que sugira substituição global seria incorreto.

**Veto de teste:** se o Executivo veta por completo dispositivo integrante de J aprovado pelo titular, o constituinte precisará fixar se há veto presidencial (em uma república parlamentar sua estrutura muda) e como impedir que veto parcial deixe em vigor somente metade do regime remuneratório. Esta regra **não é dedutível automaticamente** do art. 66 atual.

**Primeira alteração posterior:** projeto de aumento remuneratório no campo reservado requer iniciativa judicial; aprovação do Código por rito integrado não confere a parlamentares iniciativa material plena para modificar remuneração futuramente.

## 7. Veto, aprovação final e o perigo de "contrabando" do processo

### Direito vigente (referencial de controle, não regra projetada)

- **CF art. 65:** se Casa revisora emendar, o projeto retorna à Casa iniciadora; não presumir autonomia da comissão técnica para mudar conteúdo.
- **Art. 66, §§1º–2º:** o Presidente pode vetar total ou parcialmente por inconstitucionalidade ou interesse público, no prazo constitucional, e o veto parcial só abrange texto integral de **artigo, parágrafo, inciso ou alínea**; não é permitido vetar palavra ou termo isolado.
- **Art. 66, §4º:** apreciação do veto pelo Congresso em sessão conjunta; rejeição por maioria absoluta das duas Casas (artigo com redação atual EC 76/2013). Veto mantido = não promulga trecho vetado.
- **STF ADI 2.867:** sanção não convalida usurpação de iniciativa; **ADPF 714/715/716:** não se permite novo veto, por arrependimento, após sanção parcial.

### Questões que o novo texto constitucional PRECISA responder

1. **Unidade jurídica do veto** em texto de milhares de disposições: artigo/parágrafo/inciso/alínea ou `componente normativo indivisível` quando direitos/competências dependem entre si? A categoria "componente" tem de ser **delimitada antes da votação**, para não criar veto ilimitado.
2. Se veto a artigo de incorporação deixa **cláusula de revogação anterior** aparentemente intacta, quem identifica relação de dependência e como evita lacuna? **Preferência de teste:** promulgação/revogação **condicionadas em pares individualizados**, com aprovação parlamentar expressa prévia — **não** correção discricionária pelo editor.
3. Pode Presidente de um sistema constitucional alternativo **vetar política pública** em iniciativa reservada a Judiciário? Há tensão entre autonomia institucional e separação dos Poderes, resolvida na nova Constituição, não pelo CLF.
4. **Votação de integração:** é nova votação de mérito de todos os componentes ou ato de certificação? Se for nova votação majoritária ordinária que substitui quorum reservado, **FALHA**; se for só certificação editorial, é preciso explicar por que cria novo ato jurídico unitário.
5. **Veto antes/depois de integração:** texto sancionado após veto ainda corresponde ao texto votado sob quórum apropriado e aprovado pelas duas Casas? Se não, exigir reexame, não publicar remendo automático.
6. **Rejeição de veto:** regime atual art. 66, §4º; Constituição futura pode mudar, mas deve fornecer solução precisa e não ignorar dissenso.
7. **Não submissão de J:** se um titular reservou a iniciativa e não envia componente, Código **pode existir formalmente para conteúdo promulgado**, mas **não substitui toda a legislação federal permanente**. Registrar cobertura incompleta, solução provisória de remissão e suas consequências.

## 8. Dois mecanismos experimentais de veto para comparação futura — H, nenhum aprovado

**V1 — Veto atual com cláusula expressa de dependência legislativa:** preservar unidades de art. 66, §2º, e exigir que cada artigo revogador identifique dependência de dispositivo substitutivo; voto legislativo prévio determina consequência quando um trecho for vetado. **Problema:** uma regra automática de não revogação condicional pode depender de promulgação integral do bloco e do texto votado; estudar juridicidade e republicação.

**V2 — Veto por unidade substantiva certificada:** a nova Constituição permitiria vetar um **componente indivisível previamente delimitado** com direito de manifestação e revisão parlamentar, desde que unidade não sirva para ampliar poder de veto ou impedir emendas. **Problema:** Executivo poderia vetar capítulos amplos; revisão/limitação rigorosa necessária.

**Resultado:** V1 preserva familiaridade institucional; V2 exige reforma constitucional mais explícita. **Nenhuma escolha está ratificada.**

## 9. Teste do ato final: onde CP e CE falham ou sobrevivem

**CP, como redigido atualmente:** S00–S06 podem produzir propostas legitimamente aprovadas por matéria. Na **S07 falta norma que diga qual é o ato final, seu regime de sanção/promulgação e seu estatuto formal de emendas**. Assim, **CP NÃO PASSA** no teste de unidade jurídico-formal — *na versão atual*, sem significar impossibilidade eterna. A integração editoral é possível, a promulgação jurídica unificada **não está demonstrada**.

**CE, como redigido atualmente:** uma categoria constitucional positiva dá nome e autoridade ao ato em tese. Entretanto, **S07 e S09 ainda dependem** de regras sobre veto, direitos, revogação recíproca, promulgação parcial e tratamento de J2. Assim, **CE PASSA apenas condicionalmente na definição de unidade formal, mas NÃO PASSA ainda como procedimento completo**. O déficit é normativo real e impede recomendação de texto definitivo.

**P2, como controle:** promulgar instrumentos competentes separadamente permite implementar legislação real em partes, mas mantém múltiplos diplomas de origem, e portanto **não substitui** a exigência U4/U5 do usuário.

## 10. Trabalho posterior exigido antes de escolher CE ou CP

**A — Redigir aditivo constitucional apenas experimental** para CP e CE que resolva (i) ato final; (ii) espécie e quórum de alteração; (iii) titular do veto; (iv) unidade do veto e revogação dependente; (v) bicameralismo; (vi) iniciativa reservada quando não há proposta; (vii) juízo sobre validade de mera C0; (viii) competência de controle.

**B — Submeter ao módulo CF-M03.01** os dois modelos mais completos e perguntar como se adaptam a eventual parlamentarismo e a diferentes arranjos de Câmara alta ainda não decididos.

**C — Elaborar amostra artigo-a-artigo de fonte→destino com versão e veto**, sobretudo CTN art. 174 após LC 236/2026, e não presumir que um inventário inicial seja prontidão jurídica para codificar.

**D — Construir teste independente de direitos e controle de alterações editoriais**, usando Lei 9.784 art. 2º e eventuais transições do CTN. Mandar achados a T07.M03, T12.M01 e módulo judicial aplicável.

**E — Manter `DEC-016` PENDENTE e quaisquer minutas constitucionais sob H/Q**, até deliberação expressa. O projeto poderá seguir com inventários e redação de corpus único sem depender do êxito imediato da opção formal.

**Síntese:** nenhum dos modelos CP/CE está pronto para ser promulgado. O que se obteve é uma **prova de onde o processo teria de adquirir validade**, separando realidade normativa, hipótese constitucional, simulação legislativa e texto positivo.
