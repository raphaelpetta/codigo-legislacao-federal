# T01.M04 — Caso-teste formal FJ-002: LC 70/1991, Lei 9.430/1996 e SV 62

**ID:** CLF-T01-M04-CASE001 · **Data:** 13/10/2026  
**Status:** análise histórica/jurisprudencial focal, não minuta nem solução integral de espécies.  
**Matriz de origem:** `MATRIZ_ESPECIES_INICIATIVAS_FORMAL_v1.csv`, FJ-002.  
**Relevância:** demonstrar por **caso efetivamente julgado** por que a **forma de lei complementar** não pode ser confundida com **reserva material de lei complementar** no projeto CLF.

## 1. Cadeia legal conferida

- **LC 70, de 30/12/1991, art. 6º, II (texto original):** previa isenção da COFINS para sociedades civis a que se referia o DL 2.397/1987. Fonte original da Câmara: https://www2.camara.leg.br/legin/fed/leicom/1991/leicomplementar-70-30-dezembro-1991-354945-publicacaooriginal-1-pl.html .
- **Lei ordinária 9.430, de 27/12/1996, art. 56 (texto original):** impôs às sociedades civis de prestação de serviços profissionais de profissão regulamentada o dever de contribuir, com referência às normas da LC 70/1991; o parágrafo único indicou o marco temporal de receitas a partir de abril de 1997. Fonte original da Câmara: https://www2.camara.leg.br/legin/fed/lei/1996/lei-9430-27-dezembro-1996-367738-publicacaooriginal-1-pl.html .
- **STF, RE 377.457, Tema 71, j. 17/09/2008, e SV 62 (enunciado publicado em 09/01/2025):** o STF julgou legítima a revogação da isenção anterior pela lei ordinária, pois os dispositivos em questão da LC 70/1991 eram **materialmente ordinários**. Fonte oficial STF: https://portal.stf.jus.br/jurisprudencia/sumariosumulas.asp?base=26&sumula=9347 .
- **Verificação temporal adicional:** o cadastro legislativo oficial da LC 70/1991 assinala revogações parciais posteriores, inclusive pela **LC 214/2025**. Esta ficha ilustra uma **cadeia histórica e tese de espécie normativa**, não afirma que as isenções e obrigações de 1991/1996 estejam inalteradas ou constituam texto atual em 2026. Fonte cadastro: https://www2.camara.leg.br/legin/fed/leicom/1991/leicomplementar-70-30-dezembro-1991-354945-norma-pl.html . A cadeia completa de vigência e produção de efeitos deve ser completada no módulo tributário.

## 2. Simulação hipotética na arquitetura única CLF

**Origem histórica A:** `LC70/1991:art6:II@1991` (regime de isenção, histórico).  
**Origem posterior B:** `LO9430/1996:art56@1996` (regime que tornou a isenção anterior inoperante para aquela hipótese segundo STF).  
**Tese vinculante:** `STF-SV62@2025-01-09`.

**Registro proposto — somente de metadados de teste:**
- `fonte_formal_inicial = LC`;
- `reserva_material_decidida_pelo_STF = NAO no recorte`;
- `instrumento_modificador_reconhecido = LO`;
- `referencia_temporal_historica = SIM`;
- `versao_do_direito_atual = A_AUDITAR`;
- `destino_CLF = NAO_DEFINIDO` (o regime não pertence ao núcleo de técnica legislativa do T01.M04);
- `modulo_destino_sugerido = tributario setorial`, a validar contra o catálogo;
- `inclusao_desses_enunciados_como_direito_vigente = PROIBIDA sem auditoria temporal`.

## 3. Teste adversarial

Se o CLF fosse promulgado como **uma LC formal** contendo esse tipo de matéria materialmente ordinária, e posteriormente surgisse **uma lei ordinária** alterando somente aquele conteúdo, a experiência brasileira demonstra que **não se pode presumir exigência de LC exclusivamente por causa do rótulo da lei original**.

**Atenção:** isto é inferência a partir de caso específico. Não demonstramos ainda a validade de uma **LC única de centenas de matérias**, sua recepção de diversas iniciativas reservadas, a relação entre cada disposição e normas especiais ou qual o procedimento real de edição e atualização de tal Código.

### Implicação de desenho

Todo dispositivo, quando futuramente incluído no CLF, precisará ser acompanhado de informação sobre sua **espécie formal de origem** e sua **reserva constitucional material** (ou `A_VERIFICAR`). Essas duas etiquetas não equivalem a conteúdo promulgado por si próprias e não substituem interpretação jurisdicional competente.

**Conclusão do caso:** o obstáculo `LO x LC` é **mais sutil do que uma impossibilidade absoluta**, mas continua inviável inferir unidade jurídico-formal global do Código sem enfrentar iniciativa, matéria, procedimentos de outros Poderes e distribuição territorial de competências.
