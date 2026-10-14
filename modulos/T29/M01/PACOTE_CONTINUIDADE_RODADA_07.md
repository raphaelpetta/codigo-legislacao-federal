# T29.M01 — Pacote de continuidade da rodada 07 / F1-F (14/10/2026)

**Dono:** T29.M01 (RGPS segurados e dependentes), **issue** [#40](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/40), **PR** [#41 (draft)](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/41).  
**Branch:** `modulo/T29-M01-segurados-dependentes-f0-f1-20261014`. **`main` do CLF observada na abertura:** `16fba172c875c7a0de388288fe70005c944021d6`. **CF/1988 vigente** (incluindo EC103/2019), anteprojeto CF em repositório independente não auditado nesta rodada.  
**Exclusividade:** T24.M01 pertence a PR38 e T29.M02/M05 a outras frentes; **não editar nem substituir trabalhos desses módulos**.

## FEITO

| Entrega | Arquivo/evidência | Alcance |
|---|---|---|
| Reconstrução da **cadeia de 15 MPs** (MP1523 e -1 a -13, depois MP1596-14) e **Lei9528/1997** | [F1F_CADEIA_COMPLETA_MP1523_1996_1997.csv](F1F_CADEIA_COMPLETA_MP1523_1996_1997.csv) | 16 atos/versionamentos, datas de assinatura e DOU reportado, fonte institucional individual, transcrição normalizada art16§2, convalidação e Q |
| Cotejo do rol de dependentes e convalidações | [RELATORIO_F1F_CADEIA_MP1523_E_CONVALIDACAO.md](RELATORIO_F1F_CADEIA_MP1523_E_CONVALIDACAO.md) | **Todas 15 MPs mantêm enteado/tutelado sem guarda**, Lei9528 art2 mantém, art13 convalida atos praticados sob todas nominalmente; **não prova de constitucionalidade ou validade material irrestrita** |
| Diferenças editoriais e cronologia de DOU documentadas | Relatório e matriz | MP1523-11 “na forma **estabelecido**” vs -12 “**estabelecida**”; MP1523-13: **Senado/DOU 24/10** versus rodapé Planalto **26/10/1997**, priorizar Senado, sem apagar Q |
| Relatório de 9 casos em datas limítrofes | Relatório F1-F | Exemplo: MP-8 publicada **30/05/1997**; MP-7 cobre óbito de 29/05; jurisprudência STJ Tema732 protege menor sob guarda com dependência econômica apesar da exclusão textual |
| README atualizado com histórico e próxima tarefa | [README.md](README.md) | Registra status F1 parcial e F2-A a começar |

**Fontes examinadas efetivamente em 14/10/2026:**
- [MP1.523/1996 — publicação original Câmara](https://www2.camara.leg.br/legin/fed/medpro/1996/medidaprovisoria-1523-11-outubro-1996-359451-publicacaooriginal-1-pe.html); [MP1.523-1 — publicação original Câmara](https://www2.camara.leg.br/legin/fed/medpro/1996/medidaprovisoria-1523-1-12-novembro-1996-359452-publicacaooriginal-1-pe.html);
- **MP1523-2 até -13** examinadas individualmente no [arquivo Planalto de MPs antigas](https://www.planalto.gov.br/ccivil_03/mpv/1996-2000/1523-2.htm) e versões por sufixo; [MP1596-14](https://www.planalto.gov.br/ccivil_03/mpv/antigas/1596-14.htm);
- [Lei9528/1997](https://www.planalto.gov.br/ccivil_03/leis/l9528.htm), **arts.2,13,14**; [Senado MP1523-13](https://legis.senado.leg.br/norma/555128), DOU24/10/1997; [Congresso MP1596-14](https://www.congressonacional.leg.br/materias/medidas-provisorias/-/mpv/14364) e documentos de conversão.
- Históricos judiciais já verificados no módulo: [STJ Tema732](https://processo.stj.jus.br/repetitivos/temas_repetitivos/pesquisa.jsp?cod_tema_final=732&cod_tema_inicial=732&novaConsulta=true&tipo_pesquisa=T), [STF ADIs 4878/5083](https://portal.stf.jus.br/jurisprudenciaRepercussao/verPronunciamento.asp?pronunciamento=10615600), e [STF Tema1271](https://portal.stf.jus.br/jurisprudenciaRepercussao/verAndamentoProcesso.asp?classeProcesso=RE&incidente=6661561&numeroProcesso=1442021&numeroTema=1271), julgamento específico EC103§6 **não identificado até consulta**.

**Natureza metodológica:** cotejo manual de transcrições oficiais do art16§2 e convalidações, sem cópias dos fascículos completos/fac-símile de cada DOU ou comparador criptográfico. As MPs perderam eficácia formal com reedição, mas houve **convalidação expressa de atos da anterior** e **convalidação cumulativa na Lei9528 art13**; esses comandos não afastam necessidade de interpretação de efeitos individuais nem de precedentes protetivos.

## PENDENTE / NÃO VERIFICADO

1. **Eficácia individual** de MPs anteriores à EC32/2001: a convalidação dos atos não prova necessariamente ausência de qualquer litígio, nem determina retroatividade de todos efeitos; particularidades do ato, data de óbito, ECA e STF/STJ exigem decisão apropriada.
2. **Fac-símile DOU de todas as 15 MPs** e a divergência **MP1523-13 24×26/10/1997**; a transcrição institucional do Planalto apresenta outras inconsistências de edição (MP1523-3 numera duas disposições como art7; -11 apresenta concordância “estabelecido”). Nenhuma norma com variante foi transposta ao CLF.
3. **STF Tema1271 sobre EC103 art23§6:** última consulta anterior mostrava mérito não julgado, revalidar quando houver ato; **não concluir** resultado a partir do STJ Tema732 ou STF ADIs 2021.
4. Conteúdo dos **demais artigos** das MPs não foi auditado; historicamente as reedições continham mudanças noutras áreas. O inventário de **198 unidades F1-A** segue **funcional**, sem auditoria literal exaustiva.
5. IN RFB2110 art9§5 IX (PSA) 2026 após três atos modificadores, facultativo 14/16 e maternidade, mandato h/j e efeitos de custeio, outras fontes do RGPS ainda Q em suas respectivas interfaces.
6. Conclusões normativas C0/C1/M e veículo legislativo DEC016 **não ratificados**. F2–F9 não concluídos e `main` intocada. Necessários controles e revisão central antes de qualquer integração.
7. **CI** no HEAD final deste PR: somente declarar status retornado pela consulta, ausência de checagens não significa aprovação.

## PRÓXIMO — mudar de tipo de pesquisa para avançar o projeto

**T29.M01 / F2-A — reconstrução do sistema vigente: filiação e dependência.** Não voltar a inventariar as mesmas MPs. Modelo de conceitos/regras por:
- ingresso no RGPS (obrigatório/facultativo; ato/fato de filiação; inscrição e prova);
- qualidade de segurado, prazo de manutenção/perda, desemprego e múltiplas filiações;
- enquadramento de segurado especial e renda permitida (Q PSA);
- classes de dependente, presunções, dependência econômica, tutela/guarda, deficiências, data do óbito;
- interfaces (T29.M02 — recolhimento; T29.M05 — benefícios por morte; T29.M06 — procedimento; T29.M07 — RPPS);
- regras transitórias e jurisprudência (Tema732, Tema1271, ADIs, idade14/16), cada bloco marcado `VERIFICADO` ou `Q`.

**Critério de aceite F2-A:** diagrama lógico textual ou quadro de decisões para casos reais de categoria/fato gerador, tabela origem→regra→destino, 12 testes adversariais executados com respostas normativamente fundamentadas, e proposta de estrutura conceitual sem alteração dos efeitos vigentes. Alternativas M somente na fase F4 e se usuário ratificar.

**Filas secundárias:** recuperar DOU autenticamente se surgir necessidade em F2, conferir RFB versão de 2026, jurisprudência STJ/STF 1271 e estudos comparados F3.

## CONTROLE

- [x] Verificação de `main`, PR41, dono do T29 e pacote 06 antes de escrever.
- [x] Confronto documento a documento de 15 MPs e lei final no art16§2/convalidação.
- [x] Registradas diferenças editoriais e Q temporais, sem presumir juridicamente solução não decidida.
- [x] Compatibilização dos dados com pesquisa STJ Tema732 e STF ADIs/Tema1271.
- [ ] Revisão independente do CSV e consulta de CI no último HEAD.
- [ ] Nenhuma aprovação C0/C1/M nem merge.
