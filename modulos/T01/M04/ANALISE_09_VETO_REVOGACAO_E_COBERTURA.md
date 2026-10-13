# T01.M04 — Ciclo 09: veto parcial, dependência substituição–revogação e cobertura incompleta do Código único

**ID:** CLF-T01-M04-VETO09 · **Corte:** 13/10/2026 · **Status:** PESQUISA / TESTE ADVERSARIAL, **NÃO** decisão constitucional, normativa ou jurisprudência vinculante.  
**CLF main-base:** `74aa56d2942d1499044fbf5256909692be904ece`. **CF main-base:** `e2a94d0df28a629bb1f19052e54e330adc65c93d`.  
**Dependências:** `SIMULACAO_08_PROCESSO_COMPLETO_CP_CE.md`, `ESBOCOS_CONSTITUCIONAIS_07_CP_CE.md`, CLF `DEC-001` confirmado e `DEC-016` pendente; CF `CF-IC-001`, M00.02, M03.01, M14.  
**Dados:** `MATRIZ_VETO_DEPENDENCIAS_09.csv`; **esboços não aprovados** em `HIPOTESES_NORMATIVAS_09_V1_V2.md`.

## 1. Pergunta

Como evitar que **veto a norma substitutiva**, **veto a cláusula de revogação**, **veto a ambas** ou **iniciativa reservada não exercida** causem, na codificação, lacunas normativas, duplicidade ou falsa substituição de leis originais? A saída precisa decorrer **do texto que passou por processo legislativo competente**, não de indicação de um editor, comissão técnica ou programa informático.

Separar quatro planos:
- **legalmente possível hoje**, para um projeto de lei sob a CF/1988;
- **novo texto constitucional CP/P3**, ainda sem definição do instrumento de promulgação jurídico-formal uno;
- **novo texto constitucional CE/P4**, com espécie Código hipotética, mas ritos incompletos;
- **plano técnico de publicação** (matriz de dependências, histórico e controle de divergências) que não substitui a lei.

## 2. Estado jurídico brasileiro conferido

**CF/1988, art. 66, §§ 1º–7º:** veto presidencial, prazo, motivos, unidades do veto parcial (**artigo, parágrafo, inciso, alínea integrais**), apreciação e eventual derrubada congressual, promulgação do texto resultante. **Não há, no art. 66 vigente, autorização genérica para “veto a conjunto substantivo” criado unilateralmente pelo Executivo após a votação.** Art. 65 preserva revisão bicameral; art. 69 contém quórum de lei complementar quando reservado; arts. 61, 96 e outras normas tratam de iniciativa. Texto vigente: https://www2.camara.leg.br/legin/fed/consti/1988/constituicao-1988-5-outubro-1988-322142-normaatualizada-pl.html .

**LC 95/1998, art. 13, §1º, e arts. 9º e 14:** consolidação com revogação formal, **sem modificação de alcance nem interrupção da força normativa**; cláusulas revogatórias devem identificar objeto; mera reclassificação editorial não revoga. Fonte atualizada da Câmara: https://www2.camara.leg.br/legin/fed/leicom/1998/leicomplementar-95-26-fevereiro-1998-363948-normaatualizada-pl.html .

**Não presumir um efeito automático da veto sobre outras disposições não vetadas.** A Constituição vigente define processo de veto e promulgação; a **interpretação de cláusulas de eficácia condicionada**, a possibilidade de elaboração previamente aprovada e os seus limites constitucionais demandam estudo da redação exata e de precedentes. Não atribuir ao Executivo poder de declarar por conta própria uma “revogação condicional” não votada pelas Casas.

## 3. Exemplo legislativo real, sem confundir correlação e causalidade

### LC 236/2026 / Mensagem 743/2026 / VET 48/2026

A Lei Complementar 236, de **4/9/2026**, alterou o CTN e recebeu veto parcial comunicado pela Mensagem 743/2026. O acompanhamento oficial do **Congresso Nacional**, com consulta no corte de **13/10/2026**, registra o **VET 48/2026 como “Em tramitação — Sobrestando pauta”**, a partir de **08/10/2026**, e identifica **14 dispositivos vetados ainda não apreciados**.

Entre os itens estão:
- `48.26.006` — **§1º proposto do art. 174 do CTN**, no texto do PLP;
- `48.26.007` — **§2º proposto do art. 174**;
- `48.26.008` — **§4º proposto do art. 174**;
- `48.26.014` — **caput do art. 2º do PLP**, que dizia **“Revoga-se o § 2º do art. 44 da Lei nº 9.430/1996”**; essa *cláusula de revogação foi vetada*.

Portanto, **o texto vetado não se tornou lei só porque o projeto foi votado**, e **o ato revogatório vetado não pode ser anotado como revogação legislativa eficaz** sem acompanhar a subsequente deliberação e eventuais efeitos. A cláusula e os parágrafos vetados **não são comprovadamente uma única unidade de interdependência jurídica**. Este é um exemplo real da coexistência de vetos a normas substantivas e à revogação, **não prova factual da lacuna normativa hipotética abaixo**.

**Fontes oficiais verificadas:**
- Congresso, estado item a item, data e tramitação: https://www.congressonacional.leg.br/pt_BR/materias/vetos/-/veto/detalhe/18651 .
- Senado, Mensagem 743/2026: https://legis.senado.gov.br/norma/43759571 .
- Câmara, LC 236/2026, cadastro e veto: https://www2.camara.leg.br/legin/fed/leicom/2026/leicomplementar-236-4-setembro-2026-799905-norma-pl.html ; https://www2.camara.leg.br/legin/fed/leicom/2026/leicomplementar-236-4-setembro-2026-799905-veto-181229-pl.html .

**Limite temporal:** a situação `não apreciado` é a fotografia do portal na data do corte, **não** promessa de que persistirá. Qualquer inclusão de norma no CLF deve revisar eventos subsequentes de derrubada/manutenção de veto e data de promulgação.

## 4. Caso abstrato controlado: substituto S e revogação R

**Lei antiga A:** contém regra geral válida, com possíveis efeitos residuais.  
**Dispositivo novo S:** reproduz ou modifica regra A, conforme classificação `C0/C1/M/Q`; só terá eficácia se corretamente aprovado, promulgado e no seu termo de vigência.  
**Dispositivo R:** revoga expressamente regra A, quando juridicamente eficaz.  
**Condição de substituição:** `R` **só deve produzir efeitos quando houver base legislativa válida e eficácia suficiente de `S`**, **se** tal condicionalidade tiver sido **expressamente prevista e aprovada pelo legislador** e for constitucionalmente admissível. A relação `depende-de` por si só é um metadado de teste, não lei.

### Quatro resultados quando o veto trata S e R separadamente

| S eficaz | R eficaz | Resultado sem cláusula de vinculação | Juízo de risco |
|---|---|---|---|
| Não | Não | Regra A permanece, S não substitui | Baixo quanto a lacuna, controlar efeitos reais |
| Sim | Não | S e A coexistem formalmente; compatibilidade, especialidade e revogação tácita **a analisar**, não declarar automaticamente duplicação inválida | Médio/alto |
| Não | Sim | A revogada e S ausente: **lacuna ou ruptura potencial** (dependendo de outras fontes aplicáveis) | Crítico |
| Sim | Sim | Substituição possível **se** coerência, competência, efeitos intertemporais e vigor forem comprovados | Moderado, requer auditoria |

**Importante:** `vetado` nem sempre equivale a `ineficaz para sempre`: um veto pode ser derrubado; dispositivos não vetados podem ter vigência futura ou condicionada; o direito entre promulgação e deliberação de veto deve ser modelado por **datas** e atos efetivos. A matriz distingue vetado/apreciação/eficácia, em vez de uma variável booleana definitiva.

## 5. V1 — Veto por unidades constitucionais, com dependência *pré-legislada* (hipótese preferencial de teste)

**Objetivo:** manter unidades de veto equivalentes às do art. 66, §2º, e reduzir o risco de R eficaz com S ausente. A redação do projeto, **antes das votações**, vincularia cada revogação formal a um substituto identificado, mediante condição de eficácia que também leve em conta data e compatibilidade jurídica.

**Mecanismo hipotético:**
1. `S` e `R` são artigos/unidades explicitamente identificados no projeto; o legislador **aprova expressamente** o nexo e sua condição de vigência/eficácia.
2. Se `S` for vetado, a disposição `R` **não produzirá efeito antes da condição aprovada** (desde que a condição como redigida sobreviva ao veto e seja juridicamente eficaz).
3. Se `R` for vetado, `S` exige reexame de coexistência de regimes; a mera promulgação de S não apaga A sem fundamento legislativo próprio ou incompatibilidade juridicamente apreciada.
4. Se veto for derrubado, atualizar o cálculo **pela data de promulgação e de vigência efetiva da parcela antes vetada**; não presumir efeitos retroativos.
5. Se o texto condicional ou sua base normativa forem vetados, **o mecanismo também poderá falhar**; não há garantia absoluta de blindagem contra lacuna.
6. No caso de iniciativa privativa não apresentada, **não existe S aprovado nem R eficaz**: fonte original continua na legislação externa ao Código, com referência e cobertura incompleta expressas.

**Ponto adversarial central:** a cláusula de dependência não pode funcionar como **delegação implícita ao Presidente, editor ou tribunal** para escolher depois da votação quais revogações terão eficácia. O gatilho tem de ser **objetivo, público e votado previamente**; o controle de existência de eficácia deve poder ser impugnado judicialmente.

**Questão de vigência sob a CF atual:** mecanismo de vigência condicionada pode ser investigado na técnica legislativa ordinária, mas **não declarar definitivamente sua constitucionalidade** em qualquer modalidade sem pesquisa jurisprudencial específica e texto concreto. A opção V1 **não soluciona**, por si, a unidade formal CP/CE.

## 6. V2 — Veto por componente normativo indivisível, constitucionalmente definido (hipótese rival)

**Objetivo:** evitar que a escolha do veto sobre um só artigo esvazie a substituição sem afetar a revogação correlata. Sob a **Constituição alternativa**, o órgão competente poderia vetar/aprovar **uma unidade integral de codificação** previamente certificada e votada, contendo S, R e normas transitórias interdependentes.

**Requisitos mínimos de validade futura:**
- A unidade é **definida previamente pelo Legislativo**, com fundamento público de indivisibilidade funcional; **não** é agrupada unilateralmente pela autoridade vetante.
- O tamanho é restrito à **menor unidade de dependência necessária**; nunca um título inteiro apenas por conveniência política.
- O veto incide **antes da promulgação** da unidade, e o Parlamento pode apreciar/derrubar veto segundo procedimento constitucional próprio; **não** autoriza cancelamento pós-promulgação.
- Preservar quórum material e iniciativa própria de cada cláusula; uma unidade não pode ocultar norma materialmente complementar ou salário de iniciativa reservada.
- Garantir devido controle jurisdicional e direito de impugnação sobre classificação da unidade; proibir "contrabando normativo".
- Definir se veto a uma unidade bloqueia publicação de outras unidades independentes, como tratar o texto positivo uno incompleto e quem reordena capítulos sem inovar.

**Objeção central:** poder de veto mais amplo pode gerar **veto estratégico**, inclusive sobre direitos/deliberações que o Executivo não deseja mas não poderia eliminar mediante as unidades atuais. A suposta indivisibilidade pode induzir concentração de agenda e controle excessivo da legislação.

**Limite sob a CF/1988:** **não** há autorização no art. 66 para um veto por "componente material" definido somente por um regulamento ou lei comum que exceda as unidades constitucionais. V2 exige escolha constitucional independente e detalhamento consistente com desenho de governo e Parlamento ainda não decidido.

## 7. Direito comparado — lição sobre cancelamento pós-promulgação

**Estados Unidos, `Clinton v. City of New York`, 524 U.S. 417 (25/06/1998):** a Suprema Corte considerou incompatível com o procedimento constitucional de *presentment* o `Line Item Veto Act` que permitia ao presidente **cancelar partes de leis já promulgadas**. A ratio específica é relevante para impedir que o projeto CLF crie suposto veto **depois** da entrada em vigor por decisão executiva/editorial. **Não** se infere que todo veto parcial brasileiro seja inválido: CF/1988 permite veto parcial por unidades enumeradas. Fonte judicial `United States Reports`: https://www.govinfo.gov/app/details/USREPORTS-524/USREPORTS-524-417 .

**Nova Zelândia, `Legislation Act 2019`, versão 17/03/2026:** ss. 30–38 distinguem alteração/revogação e efeitos sobre relações antigas; ss. 59–62 disciplinam `revision Acts` e sua equivalência; ss. 78–91 separam fonte oficial e operações editoriais. **Lição de transição/publicidade**, não transposição de poderes de veto neozelandeses. Fonte: https://www.legislation.govt.nz/act/public/2019/58/en/2026-03-17/ .

## 8. Ausência de iniciativa reservada — problema independente do veto

**Caso J:** Lei 11.416/2006, arts. 11–13. Sob CF vigente, **reforma material** em matéria efetivamente sujeita ao art. 96, II, b, exige titular competente. A reedição literal via consolidação proposta por parlamentar permanece `Q` (issue #14), não se presume constitucional ou inconstitucional a partir de analogia.

Simular três saídas no Código formal positivo **hipotético**:
- **J1 — titular apresenta proposta:** componente pode seguir rito apropriado, sujeita à votação e ao veto conforme Constituição aplicável.
- **J2 — titular não apresenta proposta:** **lei original continua em vigor**; registrar remissão externa e cobertura parcial. O Código pode ser positivo naquilo que foi validamente aprovado, mas a pretensão de **substituição universal plena** não está alcançada.
- **J3 — legislador tenta incorporar sem titular:** para reforma material reservada, **bloquear**; não rebatizar M como C0. Para C0 estritamente fiel com revogação/reedição, exigir parecer específico, ou procedimento especial da **Constituição futura**, sem supor anuência informal capaz de curar iniciativa viciada.

**Consequência para DEC-001:** o Código **pode nascer unitário como diploma** e ainda **não cobrir toda legislação**. Essas são dimensões diferentes; a métrica de cobertura precisa demonstrar quais fontes antigas permanecem fora do Código e por quê. Não fingir completude por meio de links.

## 9. Matriz de julgamento comparado

| Critério | V1 | V2 |
|---|---|---|
| Necessidade de alterar a regra constitucional de veto vigente | **Não necessariamente** quanto às unidades de veto; cláusulas condicionais concretas requerem análise | **Sim**, se a unidade exceder as previstas no art. 66, §2º |
| Controle da continuidade normativa | Forte em tese se a condição pré-votada sobreviver | Forte em tese se a indivisibilidade for legítima |
| Risco de veto estratégico | Menor por conservar unidades atuais | **Maior**, pela possibilidade de veto a blocos amplos |
| Poder de órgão editor | Nenhum, se desenhado corretamente | Nenhum, se desenhado corretamente |
| Solução para titular de iniciativa não participante | **Não resolve**; remissão externa | **Não resolve**; remissão externa |
| Proteção contra lacuna por veto de S | Condição textual expressa, se eficaz e sobreviver | Veto atinge conjuntamente S/R, desde que unidade constitucional legítima |
| Risco de efeitos não pretendidos | Cláusula de dependência ambígua; coexistência S/A | Unidade mal delimitada; captura e veto excessivo |
| Complexidade institucional | Relativamente menor | Maior e dependente de desenho constitucional novo |

**Conclusão técnica provisória:** **V1 é a hipótese de trabalho preferível**, principalmente por menor alteração do poder de veto, rastreabilidade e possibilidade de preparar o texto legislativo antes de sua deliberação. **Não é decisão constitucional ratificada.** V2 permanece comparação adversarial; pode funcionar em contextos onde uma unidade indivisível bem definida seja justificável, mas não deve ser a solução-padrão. A escolha depende de simulação parlamentar, direitos, bicameralismo e texto constitucional final.

## 10. Próximas portas de qualidade

1. **Versão de redação rival** `HIPOTESES_NORMATIVAS_09_V1_V2.md` — ainda não aprovada, incluir solução constitucional para veto e revogação condicionada sem transferência ao editor.
2. **Teste com histórico real de veto 48/2026:** cruzar itens 006–008 e 014 à situação congressual **por data**; o veto à revogação específica é fato, **não demonstra por si** dependência causal com os itens 006–008.
3. **Teste de cobertura incompleta:** regras de iniciativa ausente, texto remanescente, versões, direitos em curso e perda de possível unidade universal.
4. **Devolução CF M03.01/M00.02/M14** com demanda para definir legitimamente o veto no sistema de governo futuro, ainda sem regime escolhido, e o efeito sobre o Código positivo uno.
5. **DEC-016 continua pendente** até resolução da espécie jurídica do Código, promulgação, sanção/veto, divergências legislativas e emenda posterior.

**Nada aqui promulga dispositivo nem certifica vigência.** A matriz de simulações mantém identidade do ato fonte e exige confirmação de cada evento de veto em fonte oficial atual.
