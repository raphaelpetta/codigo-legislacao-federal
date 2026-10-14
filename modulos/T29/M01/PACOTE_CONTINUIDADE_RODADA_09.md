# T29.M01 — Pacote de continuidade da rodada 09: F2-B (14/10/2026)

**Proprietário funcional:** T29.M01 — Segurados e dependentes RGPS · **Issue:** [#40](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/40) · **PR:** [#41 draft](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/41) · **branch:** `modulo/T29-M01-segurados-dependentes-f0-f1-20261014`.  
**Base `main` CLF no início:** `16fba172c875c7a0de388288fe70005c944021d6`; conferir SHA atual antes de mesclar. **CF/1988 com EC103/2019:** direito vigente; projeto constitucional independente não auditado nesta rodada. **Outros donos:** T24.M01/PR38 e T29.M02/M03/M04/M05/M06/M07, com interfaces, nenhum arquivo de outro módulo modificado. **DEC016:** veículo de promulgação do CLF único ainda pendente.

## FEITO

| Produto | Evidência | Natureza e verificação |
|---|---|---|
| **23 transições condicionais** de filiação obrigatória e facultativa, atividade simultânea, período de graça, termo de perda, nova filiação, carência, qualidade no óbito e dependência | [F2B_TRANSICOES_23_ESTADOS.csv](F2B_TRANSICOES_23_ESTADOS.csv) | 23 IDs exclusivos, 10 campos completos; **estados analíticos**, não norma CLF |
| **27 testes hipotéticos respondidos** sobre as transições, inclusive seis regras não testadas na F2-A | [F2B_TESTES_TEMPORAIS_27.csv](F2B_TESTES_TEMPORAIS_27.csv) | 27 IDs únicos, 8 campos, sem referência inválida; 23/23 transições exercitadas, 27 IDs de F2-A citados, seis omissões anteriores corrigidas |
| Reconstrução temporal e contrastes entre contribuição, filiação, qualidade, carência e benefício | [RELATORIO_F2B_DINAMICA_TEMPORAL_E_NAO_REGRESSAO.md](RELATORIO_F2B_DINAMICA_TEMPORAL_E_NAO_REGRESSAO.md) | Fundamentação jurídica, estado Q identificado e fluxo decisório não automatizado |
| README atualizado com estado da etapa e roteiro F2-C | [README.md](README.md) | Continuidade sem retrabalho da cadeia das MPs |

**Fontes oficiais consultadas em 14/10/2026:**
- [Lei8.213/1991 compilada, arts. 11, 15, 16, 24–27-A e 102](https://www.planalto.gov.br/ccivil_03/leis/l8213compilado.htm), distinção entre filiação, graça, nova filiação/carência, direito adquirido e pensão após perda da qualidade.
- [Decreto3.048/1999 compilado, arts. 11, 13, 14, 19-E, 20 e 27-A](https://www.planalto.gov.br/ccivil_03/decreto/d3048compilado.htm), prazos/termo/inscrição/competências.
- [STJ Tema1360, REsps 2.169.736/RJ e 2.188.714/MT, banco de precedentes qualificados](https://processo.stj.jus.br/repetitivos/temas_repetitivos/pesquisa.jsp?cod_tema_final=1360&cod_tema_inicial=1360&novaConsulta=true&tipo_pesquisa=T): julgamento **11/03/2026**, publicação **19/03/2026**, trânsito **21/05/2026**; [acórdão integral REsp2.169.736](https://processo.stj.jus.br/processo/julgamento/eletronico/documento/?documento_sequencial=364154764&documento_tipo=integra&publicacao_data=20260319&registro_numero=202403443449). Prova de desemprego por meios idôneos; CTPS/CNIS isolados insuficientes. A notícia institucional de julho não é a data da decisão.
- [STJ Súmula416](https://scon.stj.jus.br/SCON/sumstj/toc.jsp?sumula=416.num.), [STJ Informativo525 sobre recolhimento post mortem de CI](https://scon.stj.jus.br/jurisprudencia/externo/informativo/?acao=pesquisarumaedicao&from=feed&livre=0525.cod.), [AgRg AREsp636.048/PR](https://scon.stj.jus.br/SCON/GetInteiroTeorDoAcordao?dt_publicacao=26%2F05%2F2015&num_registro=201403121321).
- [STF ADIs2110/2111, decisão 21/03/2024](https://portal.stf.jus.br/processos/detalhe.asp?incidente=1795149): inconstitucionalidade da carência do salário-maternidade do art25 III, cujo reflexo no art27-A precisa ser preservado, sem apagar a filiação.
- STF Tema1271/EC103§6 e STJ Tema732 relativos à guarda: remissões aos relatórios F1-C/F1-E; **não afirmar nova leitura ou novo julgamento nesta rodada**.

**Questões novas não omitidas:**
1. **CI responsável por recolher x empregado com empregador inadimplente:** filiação pelo exercício não tem efeito uniforme sobre possibilidade de recolhimento **post mortem** para obter pensão; STJ restringe regularização após morte no caso do CI responsável pelo pagamento.
2. **Art27-A x ADIs2110/2111:** a redação legal menciona ainda salário-maternidade e metade da carência; **não restaurar exigência declarada inconstitucional** por via de codificação/editoria.
3. **Tema1360 transitado:** ampliar meios de prova de desemprego sem aceitar apenas silêncio do CNIS/CTPS, na via administrativa e judicial.
4. **Período de graça não é um relógio único:** incisos do art15, mais de 120 contribuições, desemprego provado e termo do §4; nenhum cálculo de data por aproximação.
5. **Perda de qualidade não apaga direito adquirido:** art102 e Súmula416 exigem examinar requisitos completos de aposentadoria em vida.

## PENDENTE / NÃO VERIFICADO

- **F2 continua parcial:** estrutura de dados (pessoa/vínculo/dependência) e concordância da duplicação Leis8.212/8.213 não aprovadas; o modelo de 23 estados não demonstra exaustividade RGPS.
- **Aplicação temporal do art27-A após ADIs2110/2111**, especialmente salário-maternidade, deve ser trabalhada com M05; texto oficial legal ainda contém menção a carência, sem transposição automática.
- **Contribuinte individual pós-morte:** analisar em M02 quem era realmente obrigado ao recolhimento (retenção por tomador, responsabilidade própria) antes de estender precedentes; condições da pensão em M05.
- **STF Tema1271 (guarda)** e efeitos pós EC103 art23§6: verificar eventual julgamento antes de proposta; **não decretar solução** a partir de STJ Tema732 ou Lei15108/2025.
- **Segurado facultativo 14/16, PSA e IN RFB2110 versão 2026, remuneração abaixo do mínimo**: Q específicos, sem alteração em M02 ou norma regulamentar incorporada ao Código.
- **Datas concretas de perda da qualidade** dependem de calendário de vencimento/competência para cada categoria; não foram inventadas nem se pretende cálculo administrativo universal.
- **F1 de todo o T29.M01 ainda incompleta**; 198 índices antigos são classificações funcionais, não prova de equivalência jurídico-literal. F3–F9 e CF futura pendentes.
- **CI do último SHA e revisão jurídico-material independente** pendentes até confirmação. PR **draft**, nenhuma norma C0/C1/M promulgada, DEC016 em aberto.

## PRÓXIMO — F2-C

**T29.M01/F2-C: modelo de dados e concordância jurídica do universo subjetivo**, separar `pessoa ↔ vínculos ↔ regime ↔ qualidade ↔ contribuição/custeio ↔ fatos geradores ↔ dependentes`, com **proprietário por regra** (M01 define filiação/qualidade/classe; M02 paga/contribui; M05 decide prestação por morte; M06 instrui requerimento). Criar matriz **origem → conceito → exceção → destino**; testar novamente **47 casos F2-A/F2-B**, identificando requisitos que precisam de remissão e os que exigiriam alteração material M, sem produzir minuta antes de ratificação.

**Critério de aceite:** sem unificação fictícia de alíneas/parágrafos, sem exigência clandestina de carência materna, sem restrição indevida de guarda ou prova de desemprego, sem retroatividade de contribuições post mortem por CI, sem introduzir regras de regime futuro como vigentes. Só passar a F3/F4 após consolidação F2-C.

## VERIFICAÇÕES
- [x] PR41 e main consultadas na abertura.
- [x] Fontes legais e jurisprudenciais consultadas, com registro de datas e níveis distintos.
- [x] Matriz transições **23** e testes **27**: integridade de campos, IDs e referências verificada após revisão; todos 6 IDs ainda não cobertos em F2-A foram exercitados.
- [x] Arquivo intermediário de 26 testes substituído sem preservar cópias redundantes.
- [ ] CI do último HEAD, revisão central e eventual integração dependem de confirmação/autorização.
