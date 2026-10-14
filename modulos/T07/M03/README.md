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
