# T29.M01 — Pacote de continuidade da rodada 04 (F1-C jurisprudência e efeitos temporais)

**Data e corte:** 14/10/2026; pesquisa jurídica do RGPS (segurados/dependentes). **Responsável funcional:** T29.M01 exclusivo.  
**Repositório CLF:** `raphaelpetta/codigo-legislacao-federal`, branch `modulo/T29-M01-segurados-dependentes-f0-f1-20261014`; **`main` na abertura:** `16fba172c875c7a0de388288fe70005c944021d6`. **Issue:** [#40](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/40). **PR:** [#41 — draft](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/41).  
**CF/1988 vigente:** aplicação da EC103 e direitos previdenciários; **CF futura:** projeto distinto, não consultado por dispositivo nesta rodada; nenhuma hipótese constitucional incorporada. **Não sobreposição:** T24.M01 pertence a outra frente/PR #38; T29.M02 custeio e M05 benefícios têm apenas interfaces, sem arquivos desses módulos alterados.

## FEITO — entregas demonstráveis

| Entrega | Arquivo na branch | Grau de prova/resultado |
|---|---|---|
| Análise histórico-jurídica de quatro Q com novas evidências | [RELATORIO_F1C_JURISPRUDENCIA_E_EFEITOS_TEMPORAIS.md](RELATORIO_F1C_JURISPRUDENCIA_E_EFEITOS_TEMPORAIS.md) | Distingue tese STF vinculante, controle concentrado, tema pendente, decisão recursal específica, lei e regulação |
| Matriz de **18 cenários de incidência por período**, com risco e interfaces | [F1C_CASOS_TEMPORAIS_18.csv](F1C_CASOS_TEMPORAIS_18.csv) | Cinco cenários de mandato, quatro de idade, cinco de guarda e quatro PSA; são **casos analíticos**, não decisões empíricas |
| README consolidado sem duplicar registros F1-A/F1-B | [README.md](README.md) | Referências à F1-C; 198 registros anteriores continuam classificações funcionais, **não C0** |

**Fonte e achados, 14/10/2026:**
1. **Mandato — STF Tema 691/RE626837:** decisão de mérito de 25/05/2017, acórdão publicado 01/02/2018, trânsito **21/02/2018**: constitucional a contribuição depois da Lei10887/2004 para mandatários sem RPPS; [ficha STF](https://portal.stf.jus.br/jurisprudenciaRepercussao/verAndamentoProcesso.asp?classeProcesso=RE&incidente=3916429&numeroProcesso=626837&numeroTema=691), [STF Informativo330 sobre RE351717/PR](https://stf.jus.br/arquivo/informativo/documento/informativo330.htm); [Resolução Senado26/2005](https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2005/congresso/ressf26-05.htm) suspendeu apenas Lei8212 art12 I h e não j.
2. **Facultativo adolescente — TRF3/SP 11ª Turma Recursal:** [acórdão RecInoCiv 5002988-56.2025.4.03.6322](https://web.trf3.jus.br/acordaos/Acordao/BuscarDocumentoPje/395087868), admite em tese **15 anos não impedem filiação** pelo art13 Lei8213, mas rejeita salário-maternidade por pagamento isolado e suposta filiação instrumental. **STF ADIs2110/2111** declararam inconstitucional carência de salário-maternidade: [decisão oficial](https://portal.stf.jus.br/processos/detalhe.asp?incidente=1795149). Não confundir falta de carência com falta de filiação; nem presumir fraude de contribuição única sem apuração. Acórdão TRF3 é **não vinculante nacional**, sem data de julgamento/documento completa confirmada na fonte.
3. **Menor sob guarda — ADIs4878/5083** (STF ementa DJe06/08/2021) protegem menor sob guarda com dependência comprovada no âmbito Lei8213 art16 §2; **EC103 art23 §6** restringe equiparação, mas §§4 e 7 têm remissões próprias; Lei15108/2025 inclui guarda expressamente desde **14/03/2025**; **Tema1271/RE1442021** discute constitucionalidade do §6, com **última movimentação registrada 16/04/2026 e sem mérito localizado**: [ficha STF](https://portal.stf.jus.br/jurisprudenciaRepercussao/verAndamentoProcesso.asp?classeProcesso=RE&incidente=6661561&numeroProcesso=1442021&numeroTema=1271).
4. **PSA — Lei14119/2021 art23, Lei8212 art12 §9 VIII, IN RFB2110/2022 art9 §5 IX:** a Receita Federal reconheceu expressamente a exceção para classificar segurado especial; [norma e histórico em portal oficial RFB](https://normas.receita.fazenda.gov.br/sijut2consulta/consulta/link.action?idAto=126687&visao=original). Art11 §8 Lei8213 não possui paralelo literal. **Q apenas quanto ao alcance prestacional e à versão administrativa 2026**, pois IN 2110 sofreu alterações em 2024/2025/2026; regras fiscais do art17 Lei14119 não são exoneração previdenciária universal.

Fontes e limites discriminados no relatório F1-C. **Classificação jurídica:** `DIREITO_VIGENTE` para textos de lei, `TESE_VINCULANTE` somente Tema691 e decisões de controle com seus respectivos objetos, `Q` para Tema1271 e extensões não julgadas, `HIPOTESE_CRITICA` para teste da carência disfarçada. Nenhum `C0/C1/M` foi promovido.

**Controle estrutural realizado na geração:** 18 IDs distintos, 5/4/5/4 por eixo, fontes por linha e status explícito, sem prometer ensaios judiciais. Conferência de leitura integral do CSV e checks do último SHA deve seguir ao término.

## PENDENTE / NÃO VERIFICADO

- Não localizado julgamento de mérito Tema1271 até a consulta — **reconsultar** a ficha atual em cada rodada; não afirmar suspensão nacional sem ato próprio.
- Modulação/inteiro teor integral das ADIs 4878/5083, embargos e eventuais efeitos de decisões após 2021; caso TRF3 necessitaria leitura de voto vencido, acórdãos posteriores e cronologia oficial de publicação.
- A validade e o alcance de "filiação instrumental" como fundamento contra uma contribuição para salário-maternidade é **problema crítico de não regressão** diante das ADIs 2110/2111; não converter questionamento técnico em decisão de nulidade judicial.
- Exame de jurisprudência específica e orientação INSS de PSA; verificar texto atualizado IN RFB2110 após alterações em **06/04/2026**, e diferenças entre enquadramento, prestação e base tributável.
- Histórico de alíneas h/j e Lei10887/2004 (MP, DOU, anterioridade e temporalidade da cobrança) e correspondência ao art11 Lei8213 ainda incompletos. **Tema691 resolve constitucionalidade geral pós2004, não todos os efeitos individuais.**
- **198 unidades F1-A** são inventário funcional, não equivalência literal ou cadeia completa autenticada. F2–F9 e comparação constitucional futura não realizadas.
- Revisão adversarial independente, CI do último SHA, classificação C0/C1/M, governança central e merge continuam em aberto. PR continua **draft**.
- Nenhum outro módulo nem `main` foi escrito; não duplicar trabalho de T29.M02/M05.

## PRÓXIMO PASSO — prioridade única

**T29.M01 / F1-D — cotejo literal e histórico oficial de 9 núcleos críticos:** Lei8213 arts.13, 16 §2, 11 I h/j e §8; Lei8212 arts.14, 12 I h/j e §9 VIII; EC103 art23 §§4/6/7; Decreto3048 art11 e IN RFB2110 art9 §5 IX.  
**Insumos:** edições oficiais originais e atuais, leis alteradoras no DOU, decisões STF RE351717, Tema691, ADIs4878/5083, ADIs2110/2111 e Tema1271, decisão TRF3 5002988-56.2025.4.03.6322.  
**Entregável:** matriz de redações/versões e relação origem→destino, marcos de vigência e proteção de direitos, mantendo Q onde necessário; revisão da distinção entre requisito de filiação e carência.  
**Critério de aceite:** cotejo verificável da literalidade por ato/versão, ausência de modificação implícita do direito, pertinência de jurisprudência com ratio e classe de autoridade, sem C0-J automático.

**Fila:** F1 literal restante dos arts10–17/12–14, F2 modelo vigente completo e F3 pesquisa comparada, T29.M02/M05 em interfaces especializadas.

## COORDENAÇÃO

**Proprietário:** T29.M01; **interfaces:** T29.M02, M03, M05, M06, M07, T12, T28, T32, T38. **Espécie/reserva:** CF/1988, EC103 e LC/LO setoriais, DEC-016 sobre veículo da codificação continua PENDENTE. O código único não existe como lei aprovada; documentos são pesquisa em PR.

- [x] `main`, PR #41, PRs concorrentes e pacote 03 rechecados na abertura.
- [x] Jurisprudência STF e TRF3 diferenciadas por autoridade e ratio.
- [x] Fontes, períodos, FEITO/PENDENTE/PRÓXIMO registrados.
- [ ] Revisão independente da matriz e auditoria do DOU integral.
- [ ] CI no último SHA e integração aprovada.
