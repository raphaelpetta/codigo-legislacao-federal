# T07.M03 — Ciclo 33: estudo de caso CARF 1301-008.239, DTE, ciência, prazo e regime temporal
**Data de corte 14/10/2026**. PR #39 draft. Caso real extraído da [base indexada de acórdãos do CARF, processo 13896.720305/2014-50](https://acordaos.economia.gov.br/solr/acordaos2_shard12_replica_n68/browse?debugQuery=true&fq=ano_publicacao_s%3A%222026%22&fq=ano_sessao_s%3A%222026%22&fq=camara_s%3A%22Terceira+C%C3%A2mara%22&fq=decisao_txt%3A%22da%22&fq=decisao_txt%3A%22membros%22&fq=decisao_txt%3A%22votos%22&fq=nome_relator_s%3A%22EDUARDO+MONTEIRO+CARDOSO%22&fq=secao_s%3A%22Primeira+Se%C3%A7%C3%A3o+de+Julgamento%22&q=), decisão nº **1301-008.239**, Primeira Turma Ordinária da Terceira Câmara/Primeira Seção, relator Eduardo Monteiro Cardoso, sessão **20/05/2026**, publicação **18/06/2026**. **Este caso não é julgamento judicial, tese repetitiva nem certificação de C0-J.**

## Cadeia documental — datas que o CARF efetivamente registrou
A [matriz de seis eventos](MATRIZ_CICLO33_CARF_1301_008239_EVENTOS.csv) reproduz somente o que consta do texto indexado:
- **12/02/2015:** Termo de Ciência por Abertura de Mensagem/Comunicado no DTE, fl. 279 do processo administrativo, relativo ao despacho decisório. O colegiado considerou ser o ato de ciência do art. 23 §2º III Decreto 70.235.
- **16/03/2015:** data final do prazo de 30 dias indicada no acórdão para a manifestação de inconformidade segundo o regime então aplicável. **Não** é data calculada por esta pesquisa ou código.
- **22/04/2015:** manifestação de inconformidade protocolada, considerada intempestiva.
- **20/05/2026 e 18/06/2026:** julgamento e publicação do acórdão 1301-008.239, que conheceu do recurso apenas no ponto da tempestividade e negou-lhe provimento.
- **Abertura de anexos/arquivos:** o extrato pesquisado não informa uma data precisa e o CARF a considerou juridicamente secundária em relação ao termo de abertura da mensagem. Campo `NAO_INFORMADA`, não inventado.

O [CARF Acórdão 3401-005.286, sessão 28/08/2018](https://carf.fazenda.gov.br/sincon/public/pages/ConsultarJurisprudencia/listaJurisprudencia.jsf?idAcordao=7440885) foi expressamente utilizado como precedente: abertura da **mensagem** é distinta de abertura de **arquivo**; a prova de entrega ou a consulta anterior ao decurso de quinze dias dependem dos registros correspondentes e da lei tributária aplicável.

## Ponto jurídico decisivo para T07/T43
**T43** armazena/prova os eventos `ENTREGA`, `CONSULTA_DA_MENSAGEM` e `ABERTURA_DE_ARQUIVO` se previstos e comprovados. **T07/lei especial** define qual deles é ciência jurídica e o termo inicial. O CARF neste caso validou consulta à mensagem em **12/02/2015**, não data da mera abertura de PDF nem o dia do julgamento de 2026. Um **envio sem prova** não pode ser tratado automaticamente como ciência, ressalvada ficção especial efetivamente comprovada.

**Intertemporalidade:** Lei Complementar 227/2026 e ADI RFB 2/2026 alteraram contagens/prazos do PAF em 2026. O precedente de **maio de 2026** examinou **evento administrativo de 2015**, de modo que não é exemplo de aplicação de prazo de 20 dias úteis instituído em 2026. Não atualizar retroativamente o vencimento de 16/03/2015 como se fosse cálculo novo.

## O que ainda não temos
Não foi extraída a íntegra dos autos administrativos (termologia original do SEI/e-CAC, hashes dos recibos, atos históricos completos, calendário de expediente), nem verificamos todas as condições de validade de uma comunicação **qualquer**; o acórdão fornece uma cadeia de fatos reconhecidos para **este caso**. Sua orientação administrativa não autoriza generalizar prazo de 30 dias a todos os procedimentos pós-2026 nem a Meu INSS e processo administrativo geral. **Todos os 6 eventos seguem Q**.

## FEITO / PENDENTE / PRÓXIMO
**FEITO:** primeiro caso fiscal da frente com *datas de ciência, vencimento e protocolo explicitamente documentadas*, além de metadados do julgamento e lacuna de abertura de anexo; teste de especialidade para X2/X6. **PENDENTE:** consulta à íntegra do processo administrativo e recibos, calendário histórico, vigência de cada alteração, rastreio jurisprudencial de casos discordantes, coordenação T12 fiscal e T43 ferramentas; `DEC-016`. **PRÓXIMO:** elaborar redline X2/X6 com triagem de eventos do CARF/SEI/INSS, mas **não** automatizar ciência ou vencimento individual sem fonte e lei válida. 
