# T07.M03 — Processo administrativo geral

**Estado:** PILOTO EXPERIMENTAL F0/F1/F2 parcial. **Não** é parte codificada aprovada do CLF, lei em vigor ou homologação de C0 jurídico. **Fonte de referência:** [Lei 9.784/1999 atualizada](https://www2.camara.leg.br/legin/fed/lei/1999/lei-9784-29-janeiro-1999-322239-normaatualizada-pl.html).

## Ciclo 13 — unidade de prova arts. 1º e 2º

- [`PILOTO_13_ARTIGOS_1_2_LEI9784.md`](PILOTO_13_ARTIGOS_1_2_LEI9784.md): protótipo textual completo dos dois artigos, incluindo **6 unidades** de âmbito/definições e **15 unidades** de princípios/critérios, alternativas de contextualização e hipóteses de revogação **bloqueadas**.
- [`CONCORDANCIA_INTEGRAL_ART1_ART2_13.csv`](CONCORDANCIA_INTEGRAL_ART1_ART2_13.csv): **21** transcrições com espelho literal e destino provisório, todas com `equivalencia_juridica=Q` e `status_destino=NAO_PROMULGADO`.
- [`MAPA_DEPENDENCIAS_SISTEMICAS_13.csv`](MAPA_DEPENDENCIAS_SISTEMICAS_13.csv): **16** dependências sistemáticas/jurisprudenciais, notadamente arts. 3º–70, 49-A–49-G, 69/69-A e Súmula 633 do STJ.
- [`TESTES_VETO_CONTEXTO_TRANSICAO_13.csv`](TESTES_VETO_CONTEXTO_TRANSICAO_13.csv): **30** cenários adversariais sobre veto por unidades, direitos, competência, subsidiariedade, retroatividade e revogação parcial.

**Invariantes:**
1. Igualdade de texto `C0-T` não implica equivalência normativa `C0-J`.
2. Nenhum dispositivo da Lei 9.784/1999 está revogado por esse teste.
3. “Esta Lei” não se converte automaticamente em “este Código”; mudança de referente é problema de alcance jurídico.
4. Não revogar apenas os arts. 1º e 2º enquanto restante da lei continuar a depender dos seus conceitos/âmbito e sem transição juridicamente válida.
5. A unidade de codificação definitiva depende do mecanismo geral `DEC-016` e da interface constitucional `CF-IC-001`.

**Próxima prova:** inventariar e versionar artigos 3º–70 (inclusive artigos intercalares e vetados), mapear os regimes especiais e redigir minuta contextual completa sujeita a direitos, jurisprudência e duplo procedimento de aprovação, distinguindo C0/C1 de inovação material M.

## Ciclo 14 — inventário integral no nível de artigo (13/10/2026)

- [`DOSSIE_14_INVENTARIO_INTEGRAL_E_ARQUITETURA.md`](DOSSIE_14_INVENTARIO_INTEGRAL_E_ARQUITETURA.md): cotejo da arquitetura inteira da Lei 9.784/1999, com 19 grupos funcionais incluindo o capítulo XI-A, alterações, vetos, jurisprudência, antinomias potenciais e plano de codificação.
- [`INVENTARIO_ARTIGOS_INTEGRAL_14.csv`](INVENTARIO_ARTIGOS_INTEGRAL_14.csv): **80 posições de artigo**, das quais **79 com algum conteúdo positivo** e **49-C integralmente vetado**; vetos parciais em 49-A, 49-G e 69-A. **Não** é inventário exaustivo de parágrafos e incisos.
- [`HISTORICO_ALTERACOES_VETOS_14.csv`](HISTORICO_ALTERACOES_VETOS_14.csv): **16 registros** de publicação, retificação, acréscimos legislativos e vetos; distinguir a vigência própria de 2006, 2009 e 2021.
- [`MATRIZ_REMISSOES_INTERDEPENDENCIAS_14.csv`](MATRIZ_REMISSOES_INTERDEPENDENCIAS_14.csv): **50 vínculos importantes**, entre remissões literais, efeitos sistemáticos e Súmula 633/STJ; amostra crítica, **não** universo final de remissões.

**Limite:** F1 completo apenas em nível de posição de artigo; 21 unidades textuais originais dos arts. 1º/2º já cotejadas no ciclo 13, mas transcrição completa dos arts. 3º–70 e subunidades, equivalência jurídica C0-J e instrumento de promulgação permanecem **abertos**. `DEC-001` continua finalidade; `DEC-016` pendente.

## Ciclo 15 — texto integral dos arts. 3º a 17

- [`CONCORDANCIA_LITERAL_ART3_17_15.csv`](CONCORDANCIA_LITERAL_ART3_17_15.csv): **40 unidades textuais** (caputs, incisos e parágrafos), em **15 artigos**, espelhadas literalmente com classificação `C0-T` e equivalência `Q`, sem eficácia.
- [`DOSSIE_15_COTEJO_ART3_17.md`](DOSSIE_15_COTEJO_ART3_17.md): exame da preservação dos direitos do administrado, representação facultativa por advogado e STF SV5, requisitos de pedido, legitimidade, delegação e suas três hipóteses de indelegabilidade.
- **Acumulado textual:** 21 unidades arts. 1º–2º + 40 unidades arts. 3º–17 = **61 unidades** em **17 artigos** transcritas experimentalmente; o inventário por artigo da lei toda contém 80 posições.
- **Limite:** não confundir 61 unidades com percentual de cobertura total, pois faltam levantar todos os parágrafos/incisos dos arts. 18–70. `C0-J` não foi confirmado, nem se aprovou cláusula revogatória.

## Ciclo 16 — impedimento, suspeição, forma e comunicação (14/10/2026)

- [`PILOTO_16_ARTIGOS_18_28.md`](PILOTO_16_ARTIGOS_18_28.md): **33 unidades literais** dos **11 arts. 18º–28**, com texto integral, riscos de veto, prazos e referência cruzada ao art. 41 e ao art. 49-D.
- [`CONCORDANCIA_LITERAL_ART18_28_16.csv`](CONCORDANCIA_LITERAL_ART18_28_16.csv): destino experimental 1:1, sem promulgação, `C0-T` e `Q` jurídico.
- [`TESTES_ADVERSARIAIS_ART18_28_16.csv`](TESTES_ADVERSARIAIS_ART18_28_16.csv): **30 cenários** de impedimento, suspeição, forma, intimação, saneamento, prazo, veto e direitos.
- [`MAPA_DEPENDENCIAS_ART18_28_16.csv`](MAPA_DEPENDENCIAS_ART18_28_16.csv): **20 ligações críticas**, entre elas art.26→art.41, art.26→49-D, art.26→59, art.23→66, STJ MS 7.181 e informativo de 2024.
- **Acumulado:** arts. 1º–28 completamente espelhados no nível de suas unidades **(21+40+33 = 94 unidades)**, sem equivalência jurídica C0-J validada. As **80 posições** do inventário integral da lei seguem cobrindo apenas o nível de artigo para os arts. 29–70.
- **Aviso:** a fonte da Lei 9.784/1999 não foi revogada e o espelho não substitui sua redação autêntica.

## Ciclo 17 — Instrução administrativa: arts. 29–47 (14/10/2026)

- [`PILOTO_17_INSTRUCAO_ART29_47.md`](PILOTO_17_INSTRUCAO_ART29_47.md): texto experimental **integral** do Capítulo X (19 artigos, **28 unidades**), com análise de direito probatório, participação pública, pareceres, cautelares e sigilo.
- [`CONCORDANCIA_LITERAL_ART29_47_17.csv`](CONCORDANCIA_LITERAL_ART29_47_17.csv): 28 espelhos literais `C0-T`, todos **Q** quanto à equivalência e **não promulgados**.
- [`TESTES_ADVERSARIAIS_INSTRUCAO_17.csv`](TESTES_ADVERSARIAIS_INSTRUCAO_17.csv): **36 hipóteses** sobre veto, contraditório, consulta, provas, parecer vinculante e não vinculante, cautelares.
- [`DEPENDENCIAS_INSTRUCAO_17.csv`](DEPENDENCIAS_INSTRUCAO_17.csv): **34 relações críticas**, inclusive art.26/41, art.36/37, art.38/50, art.42/49 e STJ REsp 1.747.877/GO.
- **Acumulado textual experimental:** arts. 1º–47 = **122 unidades (21+40+33+28)**, todas em `Q` jurídico; os arts. 48–70 e intercalares continuam apenas inventariados em nível de artigo, aguardando espelho e cotejo de subunidades.

Nenhum espelho modifica a legislação vigente, tampouco representa decisão sobre espécie do Código `DEC-016`.

## Ciclo 18 — Dever de decidir, decisão coordenada e motivação (14/10/2026)

- [`PILOTO_18_DECISAO_COORDENADA_MOTIVACAO.md`](PILOTO_18_DECISAO_COORDENADA_MOTIVACAO.md): espelho e análise dos arts. 48–50 com as intercalares 49-A–49-G, preservando o veto integral de 49-C.
- [`CONCORDANCIA_LITERAL_ART48_50_CICLO18.csv`](CONCORDANCIA_LITERAL_ART48_50_CICLO18.csv): **40 unidades positivas** distribuídas por nove posições de artigo, correspondência textual C0-T e equivalência jurídica `Q`, sem promulgação.
- [`REGISTRO_VETOS_LEI14210_CICLO18.csv`](REGISTRO_VETOS_LEI14210_CICLO18.csv): **seis unidades históricas vetadas**, nenhuma convertida em texto positivo.
- [`TESTES_ADVERSARIAIS_DECISAO_18.csv`](TESTES_ADVERSARIAIS_DECISAO_18.csv): **36 testes** de dever decisório, veto, exceções, motivação e responsabilidades.
- [`DEPENDENCIAS_DECISAO_18.csv`](DEPENDENCIAS_DECISAO_18.csv): **30 vínculos**, incluindo art. 49-A com competências originárias, arts. 49-B/49-D e Súmula 674/STJ.
- **Acumulado experimental:** **162 unidades textuais** espelhadas (21+40+33+28+40); equivalência jurídica e mecanismo de Código uno (`DEC-016`) ainda pendentes.

Esses arquivos **não promulgam novas normas**, nem revogam a Lei 9.784/1999. Próxima etapa: arts. 51–70, 64-A/64-B e 69-A, seguida de auditoria jurídica integral.

## Ciclo 19 — Conclusão do espelho dos arts. 51–70 (14/10/2026)

- [`PILOTO_19_RECURSOS_REVISAO_VIGENCIA.md`](PILOTO_19_RECURSOS_REVISAO_VIGENCIA.md): espelho textual integral dos arts. 51–70, **incluindo 64-A, 64-B e 69-A**, e pesquisa crítica sobre extinção, autotutela, decadência, recurso, revisão, prazos, prioridade e subsidiariedade.
- [`CONCORDANCIA_LITERAL_ART51_70_CICLO19.csv`](CONCORDANCIA_LITERAL_ART51_70_CICLO19.csv): **53 unidades** distribuídas por **23 posições**, inclusive **art. 70 como texto histórico**, todas `Q` quanto à equivalência jurídica e **não promulgadas**.
- [`VETOS_HISTORICOS_ART69A_CICLO19.csv`](VETOS_HISTORICOS_ART69A_CICLO19.csv): **três vetos** do art. 69-A (inciso III, §§ 3º–4º), sem incorporação como normas vigentes.
- [`TESTES_ADVERSARIAIS_ART51_70_CICLO19.csv`](TESTES_ADVERSARIAIS_ART51_70_CICLO19.csv): **44 testes** de interrupção de garantias, direitos, veto, decadência e temporalidade.
- [`DEPENDENCIAS_ART51_70_CICLO19.csv`](DEPENDENCIAS_ART51_70_CICLO19.csv): **37 nexos**, incluindo art. 54/Súmula 633 STJ, art. 64/65 e art. 69/procedimentos especiais.
- **Acumulado histórico do piloto:** **215 unidades textuais** (21 + 40 + 33 + 28 + 40 + 53) em **79 posições com algum texto positivo** da Lei 9.784; a posição 49-C foi integralmente vetada. Não confundir cobertura textual com equivalência jurídica demonstrada.

**Gates ainda abertos:** revisão histórica/DOU dos textos, auditoria de todo sistema e remissões, relação com leis especiais, C0-J, transição, iniciativa/quórum e `DEC-016` sobre promulgação de Código juridicamente uno. Nenhuma lei foi revogada ou aprovada.

## Ciclo 20 — Primeira auditoria jurídico-semântica transversal (14/10/2026)

- [`DOSSIE_20_AUDITORIA_SEMANTICA_INICIAL.md`](DOSSIE_20_AUDITORIA_SEMANTICA_INICIAL.md): revisão crítica dos referentes da lei, regras gerais e especiais, jurisprudência, LINDB e Lei 14.129; critérios de passagem C0-T/C0-J/C1/M/Q.
- [`MATRIZ_TRIAGEM_215_UNIDADES_CICLO20.csv`](MATRIZ_TRIAGEM_215_UNIDADES_CICLO20.csv): **215 unidades** de todos os espelhos anteriores, com textos ligados aos CSVs originais, análise de risco **automática**, destinação funcional num **único Livro**, todas **Q** juridicamente.
- [`CONTRAPROVAS_SEMANTICAS_CICLO20.csv`](CONTRAPROVAS_SEMANTICAS_CICLO20.csv): **32 hipóteses** de mudanças indevidas, lacunas ou reformas que exigem justificativa e decisão própria.
- [`MATRIZ_INTERFACES_EXTERIORES_CICLO20.csv`](MATRIZ_INTERFACES_EXTERIORES_CICLO20.csv): **15 interfaces externas**, incluindo LINDB, governo digital, LGPD, LAI, especialidade, decadência e jurisprudência.
- [`ARQUITETURA_E_MINUTA_DEMONSTRATIVA_CICLO20.md`](ARQUITETURA_E_MINUTA_DEMONSTRATIVA_CICLO20.md): **14 cláusulas experimentais**, com seis títulos dentro de **um Livro do Processo Administrativo Federal**, regras gerais uma vez e complementos específicos sem supressão de direitos.

**Alcance:** QA verifica se as 215 linhas de triagem coincidem com seus seis CSVs originais, mas **não** valida os textos contra todo o DOU nem certifica equivalência C0-J. Não há artigos homologados, lei promulgada ou revogação. `DEC-001` objetivo de Código uno; `DEC-016` instrumento promulgatório pendente. **Próximo ciclo:** auditoria aprofundada por blocos com direito externo e efeitos temporais.

## Ciclo 21 — âmbito federal, subsidiariedade e comunicações digitais (14/10/2026)
- [Dossiê 21](DOSSIE_21_AMBITO_INTIMACAO_DIGITAL.md): revisão de Lei 9.784 arts. 1–3/69 e 22–28/41 em confronto com Lei 14.129/2021 arts. 2, 7–9 e 42–43, LINDB 20–30 e CPC art. 15; duas alternativas arquitetônicas Q (R1/R2).
- [Matriz de 18 cenários](MATRIZ_AUDITORIA_BLOCOS_CICLO21.csv): riscos verificáveis de ampliação do âmbito, falsa equiparação de emissão/recebimento à ciência, perda de opt-in/opt-out e de garantias de intimação, todas classificadas Q.
- [Pacote de continuidade 21](CONTINUIDADE_21.md) com FEITO/PENDENTE/PRÓXIMO.
**Limite:** não houve certificação C0-J das 215 unidades, nem aprovação de redação final, promulgação ou revogação. Próximo: casos jurisprudenciais reais de intimação digital e concordância funcional das subunidades prioritárias.

## Ciclo 22 — precedentes sobre ciência administrativa (14/10/2026)
- [Parecer jurisprudencial 22](PARECER_22_JURISPRUDENCIA_CIENCIA_DIGITAL.md) e [matriz de quatro casos](JURISPRUDENCIA_CICLO22_04_CASOS.csv): STJ MS 24.567/DF (inteiro teor, cadastro e peticionamento SEI), MS 27.227/DF (notícia oficial, edital indevido), AREsp 3.090.241 (conclusão probatória TRF3 sobre fax/e-mail não revista pelo STJ por Súmula 7) e TRF3 AC 5015411-30.2019.4.03.6105 (controle de intimação pessoal e temporalidade).
- [Pacote de continuidade 22](CONTINUIDADE_22.md) — FEITO/PENDENTE/PRÓXIMO e limites.
**Estado:** quatro casos qualitativos, sem generalização de tese vinculante nem certificação das 215 unidades C0-J. Próximo: cotejo das unidades 26–28/41 da Lei 9.784 e Lei 14.129 arts. 42–43 com atos reais e regimes especiais.

## Ciclo 23 — concordância funcional de intimações (14/10/2026)
- [Dossiê 23](DOSSIE_23_CONCORDANCIA_FUNCIONAL_INTIMACOES.md): vinculadas **16 unidades** da Lei 9.784 (IDs AUD20-080 a 094 e 114) e **11 interfaces** da Lei 14.129 (2 III, 42, 43) a casos concretos, com ratio e limites separados.
- [Matriz de 27 vínculos funcionais](MATRIZ_CICLO23_INTIMACAO_UNIDADES_E_PRECEDENTES.csv) e [Continuidade 23](CONTINUIDADE_23.md).
- Corrigido o AREsp 3.090.241/SP: **Segunda Turma**, sessão de 19–25/02/2026, publicação 02/03/2026; **REsp não conhecido sob Súmula 7**. Não é jurisprudência de validade universal de e-mail.
**Limite:** ligações funcionais, não transposição literal ou equivalência C0-J; toda a matriz das 215 unidades segue Q. Próximo: casos institucionais de SEI/domicílio digital por ente, temporalidade, opt-in/opt-out, termo inicial do prazo e regime especial.

## Ciclo 24 — três regimes de intimação eletrônica (14/10/2026)
- [Dossiê 24](DOSSIE_24_TRES_REGIMES_CIENCIA_E_PRAZOS.md): (i) processo eletrônico geral Lei 9.784/Decreto 8.539; (ii) DTE fiscal federal Decreto 70.235 art. 23; (iii) Meu INSS, Portaria DIRBEN 993/2022 alterada em 2025, Lei 14.129 e TCU Acórdão 2.002/2024, item 9.1.1.
- [Matriz de 23 normas e controles](MATRIZ_CICLO24_TRES_REGIMES_INTIMACAO.csv) e [12 testes adversariais](CONTRAPROVAS_CICLO24_TRES_REGIMES.csv), **tudo Q jurídico**, sem transposição C0-J das 215 unidades.
- [Pacote de continuidade 24](CONTINUIDADE_24.md): sem prova de cumprimento da determinação TCU em 2026; distinguir prazo de ciência fiscal de prazo de defesa, protocolo de intimação e norma infralegal de lei.
**Próximo:** monitorar cumprimento da determinação do TCU, aferir legalidade e evidência do art. 20 I da Portaria 993 e o regime especial fiscal, antes de qualquer regra geral integrada.
