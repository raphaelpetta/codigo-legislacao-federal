# T29.M01 — F4-2: seis espelhos literais, hashes de transcrição e conflito do dirigente sindical

**Corte de consulta:** 14/10/2026. **Issue:** [#40](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/40) · **PR:** [#41, draft](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/41). **Objeto único:** selecionar seis pares da F4-1 e conferir seu texto na **compilação oficial da Câmara dos Deputados** das Leis 8.213 e 8.212, mais contraste com Planalto e lei alteradora para divergência. **Não é certificação de igualdade de efeitos, de texto do DOU ou de original HTML**, nem escolha entre A/B, elaboração F5, homologação C0/C1/M, fusão ou revogação.

## 1. Fontes e método reproduzível

- [Câmara: Lei 8.213/1991, norma atualizada](https://www2.camara.leg.br/legin/fed/lei/1991/lei-8213-24-julho-1991-363650-normaatualizada-pl.html), art. 11, incisos I, alíneas `a` e `b`, inciso II e §§ 1º, 2º, 4º.
- [Câmara: Lei 8.212/1991, norma atualizada](https://www2.camara.leg.br/legin/fed/lei/1991/lei-8212-24-julho-1991-363647-normaatualizada-pl.html), art. 12 nos mesmos incisos e alíneas e §§ 1º, 2º, 5º.
- [Planalto: Lei 8.213 compilada](https://www.planalto.gov.br/ccivil_03/leis/l8213compilado.htm) e [Lei 8.212 compilada](https://www.planalto.gov.br/ccivil_03/leis/l8212compilado.htm) como controle de segunda publicação — há variações de renderização/diacríticos e, no art. 11 §4º da 8213, uma palavra divergente.
- [Lei 9.528/1997, texto da publicação original no portal Câmara](https://www2.camara.leg.br/legin/fed/lei/1997/lei-9528-10-dezembro-1997-349414-publicacaooriginal-1-pl.html), art. 1º (8212 §5º) e art. 2º (8213 §4º); [Planalto Lei 9.528](https://www.planalto.gov.br/ccivil_03/leis/l9528.htm). [Lei 11.718/2008 (Planalto)](https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2008/lei/l11718.htm), art. 1º, para a redação da economia familiar.

**Método:** transcrição manual supervisionada dos trechos principais tal como visualizados em **Câmara/norma atualizada**, retirando somente o rótulo (`a)`, `§ 1º` etc.), notas de alteração e espaços editoriais externos; conversão Unicode **NFC** e substituição de sequências de espaços por espaço único; **preservação** de pontuação, preposições, acentos e maiúsculas/minúsculas. Hash **SHA-256 calculado sobre o texto transcrito e normalizado**, não sobre arquivo obtido por download, página HTML inteira ou DOU. O algoritmo SHA-256 usado foi testado contra o vetor `abc`, mas **a transcrição não é extração independente de bytes de fontes originais**. Não usar hash igual como prova de identidade textual em todos os suportes ou ao longo do tempo.

**Artefato de seis pares com textos completos e hashes:** [F42_ESPELHO_LITERAL_SEIS_PARES_SHA256.csv](F42_ESPELHO_LITERAL_SEIS_PARES_SHA256.csv).

## 2. Resultado: cinco coincidências na versão da Câmara e uma divergência

| Par | 8213 → 8212 | Resultado da transcrição normalizada Câmara | Histórico aparente |
|---|---|---|---|
| L01 Empregado subordinado | art. 11, I, a → art. 12, I, a | **Coincide**, hash idêntico | Sem alteração do próprio trecho indicada nas compilações consultadas |
| L02 Trabalho temporário | art. 11, I, b → art. 12, I, b | **Coincide**, hash idêntico | Mesmo limite de consulta |
| L03 Empregado doméstico | art. 11, II → art. 12, II | **Coincide**, hash idêntico | Mesmo limite de consulta; legislação trabalhista posterior não cotejada exaustivamente |
| L04 Economia familiar | art. 11 §1º → art. 12 §1º | **Coincide**, hash idêntico | Ambos assinalados com redação da **Lei 11.718/2008** |
| L05 Atividades simultâneas | art. 11 §2º → art. 12 §2º | **Coincide**, hash idêntico | Sem alteração do trecho indicada nas compilações consultadas |
| L06 Dirigente sindical | art. 11 §4º → art. 12 §5º | **Diverge na Câmara**: `do` × `no`; hashes diferentes | Ambos vinculados à **Lei 9.528/1997**; outros suportes discordam quanto à transcrição |

**Importante:** igualdade de texto em norma compilada é **indício forte apenas do enunciado normativo selecionado**, não da identidade de valor normativo completa. A incidência de dever contributivo, registro, contribuição, carência e prestações pode estar determinada **em outros artigos**, preservados pelos módulos titulares. A LC 95, art. 13, §2º, III ([texto compilado](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp95compilado.htm)) exige valor normativo idêntico para fusões editoriais; nenhuma das cinco coincidências foi marcada como **C1 aprovado**.

## 3. Achado de proveniência: dirigente sindical apresenta três variantes

[F42_TRIANGULACAO_SINDICAL_06_FONTES.csv](F42_TRIANGULACAO_SINDICAL_06_FONTES.csv) registra **seis observações**: duas leis × (compilação Câmara, compilação Planalto, Lei 9.528/1997 na publicação original disponível).

**Lei 8.213 art. 11 §4º:**
- Câmara, norma atualizada: frase com **`do Regime Geral`**;
- Planalto, Lei 8.213 compilada: **`no Regime Geral`**;
- Lei 9.528/1997, transcrição da publicação original disponível na Câmara e no Planalto: **`no Regimento Geral`**, em que `Regimento` parece erro textual, mas **não há prova neste recorte de uma retificação oficial publicada no DOU**.

**Lei 8.212 art. 12 §5º:**
- Câmara e Planalto: **`no Regime Geral`** (formatação do hífen/espaços pode variar);
- Lei 9.528/1997, redação da 8212: **`no Regime Geral`**.

**Consequência:** não declarar **identidade literal geral** do par, nem corrigir `Regimento` na fonte histórica sem anotar a origem e eventual cadeia formal de retificação; no máximo reconhecer a clara aproximação funcional na manutenção de enquadramento. A F4-2 descobriu uma **divergência de representação de texto oficial**, distinta da pergunta de identidade material. **Q_FONTE_LITERAL** permanece até confronto do fac-símile da publicação original no DOU, eventual errata/republicação e histórico das consolidações. Se houver erro da fonte histórica, deve ser tratado nos níveis C0 e proveniência antes de C1.

## 4. Consequências para a escolha arquitetural A/B

**Opção A — núcleo comum com exceções:** os cinco trechos coincidentes podem ser **candidatos melhores à definição nuclear** depois de validação jurídica, mas não autorizam transportar a M01 a responsabilidade contributiva definida em M02 ou pressupor uniformidade prestacional. O dirigente sindical deve ficar como **Q de proveniência** até esclarecimento, sem escolha de palavra por preferência editorial.

**Opção B — blocos coordenados:** manter as duas referências internas durante a reconstrução evita decidir prematuramente qual texto deve prevalecer, mas aumenta a necessidade de mecanismo de concordância estável e aviso quando os suportes divergem.

**Estratégia incremental candidata, NÃO decisão:** preservar blocos B como quadro de migração conservadora; após provar identidade **literal, temporal e material**, promover ao núcleo A somente as unidades sem efeitos diferentes. Cada mudança é submetida a M02/M05/M06 e DEC-016, sem presunção de concordância por silêncio.

## 5. Status por garantia e verificação residual

| Origem F2-C | Perigo na fusão apesar de semelhança | Controle futuro |
|---|---|---|
| G01/G06 empregado e temporário | Custeio atribuído ao empregador/tomador e normas de prova, sem identidade de função | M02 e M06 |
| G01/G06 doméstico | Incidências de LC 150/2015 e histórico de categoria | M02, M06, T01 |
| G05 economia familiar | Titularidade e prova individual de trabalho especial | M02 e M06 |
| G03/G06 concomitância | Cada atividade obrigatória versus contagem temporal por competência | M02, M07 |
| G01/G20 dirigente sindical | Variante do/no/Regimento e transição 1997 | M02 e T01 |

**Validação que falta:** extração article-local dos **bytes fonte ou HTML** com registro de URL, snapshot e hash de origem; histórico de cada dispositivo em atos originais e DOU; verificação das consequências jurídicas por módulo e aplicação aos **51 cenários** já inventariados, sem contar estas seis linhas como casos adicionais. A publicação da Câmara serve de fonte secundária oficial recomposta e é controlada pelo Planalto; **não substitui o exame crítico da norma alteradora para divergência**.

## 6. FEITO/PENDENTE/PRÓXIMO

**FEITO:** seis textos transcritos em paralelo, comparação normalizada NFC e hashes de transcrição, **cinco coincidências**, uma discordância Câmara; triangulação do último em seis fontes e Lei 9.528 original; status qualificado, sem fusão ou aprovação.

**PENDENTE:** confronto DOU fac-símile e eventual retificação para dirigente sindical; extração independente automatizada e hashes do HTML original; auditoria jurídico-material do valor normativo por titular M02/M05/M06/T01 e demais fontes; F1 global e F2-D/F6 ainda parciais; DEC-016 aberto; dados SUIBE permanecem sem XLSX (HTTP 403), minuta LAI não enviada.

**PRÓXIMO — F4-3:** resolver proveniência do §4º sindical por fac-símile DOU/republicação e confirmação das cinco coincidências em originais datados; gerar matriz **C0 editorial / C1 potencial / M / Q** apenas como **proposta sujeita a decisão** para pares selecionados, com mapa de efeitos e concordância intermodular. Não iniciar F5 de Código até que A/B, os módulos titulares e a governança central definam o que fazer. **PR #41 draft; main e outros módulos não alterados.**
