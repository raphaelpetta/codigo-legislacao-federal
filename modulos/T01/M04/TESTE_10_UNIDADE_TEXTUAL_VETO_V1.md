# T01.M04 — Ciclo 10: teste da unidade textual de veto na revogação condicionada (V1)

**ID:** CLF-T01-M04-UNIV10 · **Corte:** 13/10/2026 · **Estágio:** pesquisa adversarial F1/F3/F5, NÃO deliberação jurídica, constitucional nem texto promulgado.  
**Baseline CLF:** `1d4fbd2ea3ba792b8c7137e9bb26b68a04b721e8` · **Baseline CF:** `92a1af3d4ca6fd0560d1a576f48079500ca519c5`.  
**Interfaces:** `DEC-001` (Código integrado como finalidade), `DEC-016` (veículo jurídico PENDENTE), `CF-IC-001`, CLF issue #14 (iniciativa C0 reservada), M03.01 (veto), M14 (transição).  
**Artefatos:** `MINUTAS_EXPERIMENTAIS_10_UNIDADE_VETO.md`; `MATRIZ_UNIDADE_VETO_10.csv` com resultados de 32 hipóteses. Nada neste texto converte simulação em direito vigente.

## 1. Hipótese focal e resultado

**Pergunta:** vincular uma cláusula revogatória a uma condição de eficácia **no mesmo artigo, sem subdivisões vetáveis**, reduz o risco de veto à condição com preservação de revogação incondicional? E preserva a lei anterior quando o **dispositivo substitutivo S** é vetado, quando há derrubada de veto posterior, quando S é parcialmente promulgado ou quando S é inválido?

**Conclusão normativa provisória:**

- **Sim, no plano da divisibilidade textual do veto**: o art. 66, §2º, da CF/1988 só admite veto ao **texto integral de artigo, parágrafo, inciso ou alínea**. Se a única disposição `R+C` for um **artigo indiviso** (não houver parágrafo ou inciso contendo separadamente o comando e a condição), não se pode **vetar só palavras dentro desse artigo** para apagar a condição mantendo o comando. O Executivo poderia vetar **todo o artigo**; os demais dispositivos continuam sujeitos às unidades constitucionais.
- **Isso não garante equivalência de vigência, nem iniciativa ou quórum correto**. Se o substituto estiver noutro artigo, ele pode ser vetado. O risco relevante passa do `veto à condição` para `qualificação objetiva do gatilho, coesão do substituto, votação separada, temporalidade e revogação tácita`.
- A solução **não cria veto a bloco** e pode ser testada sem mudar as **unidades de veto** da CF/1988, **mas** a validade de cada cláusula concreta de eficácia e de seu objeto permanece sujeita a análise legislativa/judicial específica. Não declarar que o STF ratificou essa redação exata.
- **Preferência experimental:** artigo indiviso único `R+C`, fonte antiga precisamente identificada, condição pautada em **fatos jurídicos positivos públicos e objetivos**, nenhum poder discricionário do editor; ressalva explícita para efeitos residuais. A cláusula de `mera aplicabilidade` aberta está rejeitada como gatilho suficiente.

## 2. Direito positivo, art. 66 e técnica LC 95

**CF/1988, arts. 65–66:** a Casa revisora pode emendar projeto, exigindo retorno à iniciadora (art. 65, parágrafo único). A sanção/veto recai sobre projeto aprovado por ambas. O veto parcial abrange **artigo, parágrafo, inciso ou alínea inteiros**, art. 66, §2º; veto rejeitado pelo Congresso desencadeia procedimento de promulgação, §§4º–7º. A Constituição não determina que dependência semântica entre artigos os torne automaticamente uma única unidade de veto.

**LC 95/1998, arts. 8º–11:** a lei tem cláusula de vigência; cláusula revogatória **enumera expressamente** os atos/dispositivos; artigo é unidade básica; parágrafos exprimem complemento e exceções; precisão e remissões explícitas são obrigatórias. A LC 95 **não cria imunidade ao veto por agrupar o comando e a condição num artigo**, mas torna o projeto auditável. Art. 13, §1º, condiciona a consolidação a conteúdo e continuidade **sem mudança de alcance**.

**LINDB, arts. 1º, 2º §§1º–3º e 6º:** vigência, revogação expressa ou por incompatibilidade, convivência de disposições, **proibição geral de repristinação automática** e proteção do direito adquirido, ato jurídico perfeito e coisa julgada. Se uma norma foi **validamente revogada**, sua posterior perda de vigência **não** a restaura automaticamente. **Não confundir** `R nunca produziu efeitos porque a condição não ocorreu` com `R já produziu efeitos, depois perdeu a vigência`.

**Decreto 12.002/2024:** no Poder Executivo federal, disciplina publicação/retificação e distingue erro material de inovação; não amplia poderes de editor nem sobrepõe o processo constitucional do Legislativo. Sua aplicação ao CLF depende do tipo de ato.

Fontes oficiais:
- CF/1988 (Planalto): https://www4.planalto.gov.br/legislacao/legis-federal/constituicao
- LC 95 atualizada (Câmara): https://www2.camara.leg.br/legin/fed/leicom/1998/leicomplementar-95-26-fevereiro-1998-363948-normaatualizada-pl.html
- LINDB atualizada (Câmara): https://www2.camara.leg.br/legin/fed/declei/1940-1949/decreto-lei-4657-4-setembro-1942-414605-normaatualizada-pe.html
- Decreto 12.002/2024 (Câmara): https://www2.camara.leg.br/legin/fed/decret/2024/decreto-12002-22-abril-2024-795527-normaatualizada-pe.html

### Fato contemporâneo, e não prova da hipótese

O **VET 48/2026**, relativo à LC 236/2026, inclui veto ao dispositivo revogatório **art. 2º do PLP** (referente à Lei 9.430/1996, art. 44, §2º), além de vetos a trechos propostos ao CTN art. 174. O portal oficial registrava os itens **não apreciados** em 13/10/2026. **Não se demonstrou interdependência causal entre esses grupos do veto**: é dado empírico sobre a diversidade dos dispositivos vetáveis, **não** precedente de revogação condicionada. Fonte https://www.congressonacional.leg.br/pt_BR/materias/vetos/-/veto/detalhe/18651 .

## 3. Quatro minutas **concorrentes** (não promulgadas)

### M0 — Condição em parágrafo separado: controle negativo

> Art. R (SIMULAÇÃO). Fica revogado o art. A da Lei nº F, de ANO.  
> Parágrafo único. A revogação prevista no caput somente produz efeitos após a entrada em vigor do dispositivo substitutivo S da presente lei.

**Falha:** o parágrafo único é uma **unidade de veto autônoma** conforme art. 66, §2º. Se vetado, o caput permanece com comando revogatório sem a condição planejada. A redação falha o teste de veto isolado da condição.

### M1 — Condição integrada ao artigo indiviso: solução candidata

> Art. R (SIMULAÇÃO). Fica revogado o art. A da Lei nº F, de ANO, **a partir da data em que entrar em vigor o art. S desta lei**, se e na medida em que a revogação for aprovada e eficaz segundo o processo legislativo constitucionalmente competente.

**Benefício:** a condição e a declaração revogatória estão **na mesma unidade integral**. Um veto parcial que queira eliminar a condição deve vetar o próprio art. R inteiro; **não pode eliminar apenas a locução condicionante**.

**Limitações:**
1. O art. S pode ser vetado completamente e nunca promulgado; R tem condição ainda não satisfeita.
2. O art. S pode ser **parcialmente vetado** em subunidades e ainda `entrar em vigor` em parte; logo `vigor do artigo` pode não equivaler a `existência integral da solução substitutiva`. Necessária correspondência das unidades indispensáveis.
3. Veto derrubado depois poderá promulgar S em data posterior; não presumir retroatividade da revogação.
4. Um artigo S pode ser editado e entrar em vigor porém violar reserva material, iniciativa ou direitos; gatilho puramente formal `vigência` pode ativar revogação antes de julgamento judicial. Parecer e regime de efeitos devem enfrentar a hipótese.
5. Remissão ao `art. S desta lei` só funciona com identificador estável e numeração efetiva no projeto promulgado; não usar placeholders na lei final.
6. A oração `se e na medida em que` acima é didática, **NÃO** atende sozinha à precisão exigida pela LC 95: deve ser reformulada para identificar `S`, `A`, data e eventual enumeração de subunidades indispensáveis.
7. Se R é o último dispositivo de `lei de consolidação` e S assume novo texto dentro do CLF, exigir compatibilidade entre veículo jurídico e espécie material de ambos; não usar a condição para apagar reserva ou iniciativa.

### M2 — Artigo indiviso, cláusulas de revogação por unidade mínima: alternativa operacional

> Art. R1 (SIMULAÇÃO). Fica revogado o inciso [A] do art. [X] da Lei nº [F], de [ANO], **na data de início de vigência do inciso [S1] do art. [Y] deste Código**, desde que o texto integral do inciso [S1], aprovado pelas Casas, tenha sido promulgado.  
> Art. R2 (SIMULAÇÃO). Fica revogado o inciso [B] do art. [X] da Lei nº [F], de [ANO], **na data de início de vigência do inciso [S2] do art. [Y] deste Código**, desde que o texto integral do inciso [S2], aprovado pelas Casas, tenha sido promulgado.

**Benefício:** vínculo um-para-um e menor risco de que `S parcialmente vetado` satisfaça condição vaga; ambas as revogações são artigos inteiros autônomos. **Problemas:** 
- `promulgado` e `vigente` não são sinônimos; datas e efeitos precisam ser corretos;
- mesmo inciso promulgado pode ser declarado inconstitucional ou não alcançar todos os sujeitos cobertos por A;
- definir se cada unidade S1 corresponde exatamente a A requer **auditoria jurídico-semântica antes da votação**, não certificação pelo editor;
- se S1 estiver em `parte positiva` de ato formal distinto, referenciar instrumento correto;
- a redação final pode gerar uma multiplicidade de artigos revogatórios, comprometer legística de um único Código e conflitar com escolhas de remissão. **Não homologar** sem protótipo de concordância e revisão técnico-legislativa.

### M3 — Condição só em documentação digital: controle negativo

> No banco de dados, o editor registra `revogação_de_A_condicionada_a_vigência_de_S`, mas o artigo promulgado dispõe apenas: “Revoga-se A”.

**Falha:** metadado não integra lei promulgada. O condicionamento digital não tem força para contrariar uma revogação incondicional votada, sancionada/promulgada e eficaz.

## 4. Diferenciar veto da condição e veto do substituto

| Evento hipotético | M0 (parágrafo) | M1/M2 (mesmo artigo indiviso) |
|---|---|---|
| Executivo tenta vetar **apenas condição** | Possível vetar **parágrafo**: R pode subsistir incondicional | **Não é permitido vetar palavras** da condição dentro de artigo indiviso: só R integral |
| Executivo veta **R** integralmente | Lei A não sofre esta revogação expressa; coexistência e revogação tácita a examinar | Igual |
| Executivo veta **S** integralmente, R sancionado | R pode operar incondicionalmente se condição estiver em parágrafo vetado | R ainda depende do evento previsto no texto, **se a condição aprovada for juridicamente válida** |
| Executivo veta parte de **S** | Interpretação da condição depende da sua redação e da parte remanescente | **Risco residual**: S parcialmente em vigor pode ativar R apesar de solução incompleta |
| Congresso rejeita veto a S após entrada em vigor dos demais artigos | Condição separada pode ter sido vetada ou sobreviver; avaliar caso | R só passa a produzir efeito no marco objetivo descrito e juridicamente aplicável; **sem retroatividade presumida** |
| Lei posterior revoga R já eficaz | Não restaura automaticamente A | Idem; art. 2º, §3º, LINDB |
| Tribunal invalida S após R ter produzido efeito | Poderá exigir efeitos/modulação e analisar revogação, não simplesmente reativar A por edição | Igual; mera correspondência de texto não autoriza `repristinação editorial` |

## 5. Testes jurídicos que reprovam soluções aparentemente fáceis

**T-A — Misturar `S` e `R` no mesmo artigo.** Se a matéria de S exige quórum/ iniciativa especial e R afeta campo de outro titular, a fusão textual pode piorar a regularidade formal. Ainda que textual, `uma unidade de veto` **não é** automaticamente uma `única matéria constitucionalmente homogênea`. Solução candidata: S e R em artigos separados; **R com sua própria condição no artigo indiviso**, não S e R obrigatoriamente no mesmo dispositivo.

**T-B — Veto parcial de inciso/subunidade S.** Condição baseada em vigência de `art. S` pode ser insuficiente. Preferir testar remissão à **menor unidade positiva indispensável**, identificada por numeração e texto aprovado. Se houver vários incisos necessários, legislar condições cumulativas objetivas sem delegar juízo de equivalência ao editor.

**T-C — Derrubada posterior de veto.** Se S não foi promulgado no primeiro momento, R não pode valer retroativamente apenas porque o Congresso rejeitou o veto. Avaliar data da promulgação da parte do projeto, publicação e vacatio, com direitos e efeitos de A durante o intervalo.

**T-D — Revogação consumada e novo veto/lei.** LINDB art. 2º §3º rejeita repristinação tácita. Uma vez eficaz R, perda ulterior do vigor de S ou de R não significa que o editor possa ressuscitar A. Só lei/decisão constitucionalmente competente e seu regime próprio podem disciplinar consequências.

**T-E — Redação com cláusula de “equivalência certificada”.** O certificado técnico não pode funcionar como condição discricionária que outorga competência legal a um editor. O legislador deve definir fatos normativos objetivos no ato votado.

**T-F — Veto integral à revogação não implica veto a S.** É possível S promulgado e R vetado; pode haver coexistência ou conflito jurídico. Uma lei nova pode revogar tacitamente a anterior por incompatibilidade (LINDB art. 2º §1º), mas isso depende de interpretação jurídica; não tratar o índice como fonte de revogação automática.

**T-G — Titular de iniciativa reservada não participou.** Para reforma material reservada, a ausência de iniciativa bloqueia a incorporação; V1 não fornece iniciativa. A regra anterior permanece conforme direito vigente, com remissão e cobertura incompleta, sem unidade plena de abrangência.

**T-H — Veto por artigo inteiro pode inviabilizar a cláusula revogatória condicional.** Isso não é a mesma falha que produzir revogação incondicional: remove R em conjunto com sua condição, mas pode manter A e S simultaneamente. **V1 reduz risco de lacuna, não garante coerência completa após vetos.**

## 6. Evidência jurisprudencial e lacuna de pesquisa

Os fundamentos verificados para a afirmação limitada de **indivisibilidade textual** são constitucionais, **não** um precedente identificado que aprove expressamente a redação M1/M2. O levantamento focalizado **não identificou decisão do STF com a questão exatamente “veto à condição de revogação inserida no mesmo artigo que a revogação”**. Isso **não demonstra inexistência** de jurisprudência nem homologa legalidade material de condição complexa.

**Não utilizar** o precedente norte-americano `Clinton v. City of New York` para afirmar que a CF/1988 proíbe veto parcial: o caso impediu **cancelamento após promulgação** nos EUA, enquanto a CF/1988 permite veto parcial pré-promulgação nos limites do art. 66. Fonte comparada: https://www.govinfo.gov/app/details/USREPORTS-524/USREPORTS-524-417 .

## 7. Proposta de encaminhamento e decisão crítica

**Para T01.M04:** testar **M1 e M2**, com M0/M3 como controles negativos, mantendo `V1` como **hipótese preferencial sujeita a revisão**. Não migrar a minuta experimental 02 automaticamente. Abrir **ficha de dependência** para cada par S/R (`fonte A`, `destino S`, `texto C0/C1/M/Q`, `competência`, `iniciativa`, `quórum`, `redação e unidade de veto`, `vacatio`, `efeito`, `veto`, `derrubada`, `direitos residuais`, `revisão adversarial`).

**Para a Constituição nova:** indagar ao M03.01 se há razão para criar espécie **veto de bloco V2** quando V1 com artigo indiviso reduz parte substancial do risco. **Não** reduzir problema à técnica: Constituição CP ainda não criou ato final uno, e CE ainda exige rito de promulgação/alteração. Art. 66 vigente não soluciona sozinho `DEC-016`.

**Status final:** teste de estrutura parcialmente satisfatório para M1/M2; **sem aprovação de constitucionalidade ou promulgação**. `DEC-001` preservada como objetivo; `DEC-016` **PENDENTE**. A questão de iniciativa C0 e efeitos de invalidade/repristinação não se encerra.
