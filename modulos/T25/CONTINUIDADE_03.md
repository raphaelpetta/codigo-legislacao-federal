# T25.M01 — Continuidade do ciclo 03: CP arts. 1º–12

**Data e corte:** 14/10/2026 (fuso America/Sao_Paulo). **Escopo:** texto literal em fonte legislativa compilada, sucessão temporal, territorialidade, sentenças estrangeiras e subsidiariedade. **Gestão:** [Issue #31](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/31); [PR #32 — rascunho](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/32); branch `modulo/T25-parte-geral-f0-f1`.

**SHAs:** `main` do CLF verificada no início e imediatamente antes deste arquivo = `9c84d9cc7e0c729b36b6fba2b81a59adec70f5e5`; branch anterior aos novos arquivos (HEAD ciclo 02) = `9576461886f73648131b3ba220d7bdbe06ba34b2`. Após gravações, verificar HEAD e CI. **Anteprojeto constitucional:** não relido neste ciclo, usar CF/1988 para legislação vigente; nenhuma escolha constitucional nova importada.

## 1. FEITO — na branch, NÃO na main

| Entrega verificada | Arquivo | Natureza/limite |
|---|---|---|
| Espelho de 39 unidades textuais dos 12 artigos | `CONCORDANCIA_LITERAL_ART1_12_CICLO03.csv` | fonte compilada Câmara, C0-T no aspecto textual, equivalência jurídica `Q`, destinos de teste, sem promulgação |
| Auditoria seletiva das garantias, conflitos e jurisprudência | `DOSSIE_03_ART1_12_TEXTO_TEMPORAL_E_ESPECIALIDADE.md` | F2/F3 parciais, sem proposta M ratificada |
| Novo achado de integração | CP art.9º × Lei 13.445/2017 arts. 100–105 × STJ AgRg HDE 13.803-EX | a Lei de Migração acrescentou hipóteses de transferência de execução de pena; a jurisprudência de 2026 delimita o objeto da homologação de absolvição estrangeira; **requer T23/T26/T27/T48** |
| Três famílias jurisprudenciais delimitadas | STF Súmulas 611/711 e STJ Súmula 501/Tema 191 | apenas os contextos consultados, sem generalização automática |
| Índice T25 e estado documentados | `README.md` e este pacote | continuidade e rastreabilidade |

**Fontes efetivamente consultadas (14/10/2026):**
1. Câmara CP atualizado arts. 1º–12: https://www2.camara.leg.br/legin/fed/declei/1940-1949/decreto-lei-2848-7-dezembro-1940-412868-normaatualizada-pe.html — **texto atual compilado** e notas de 1984.
2. Planalto CP compilado arts. 1º–12: https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848compilado.htm — controle editorial, sem histórico integral.
3. Câmara Lei 7.209/1984 publicação original digitalizada, arts.1º–12: https://www2.camara.leg.br/legin/fed/lei/1980-1987/lei-7209-11-julho-1984-356852-publicacaooriginal-1-pl.html — erros aparentes de conversão/formatação não validados como texto autêntico.
4. STF Súmula 611 https://portal.stf.jus.br/jurisprudencia/sumariosumulas.asp?base=30&sumula=2560 , inclusive exemplo HC 106.454; STF Súmula 711 https://portal.stf.jus.br/jurisprudencia/sumariosumulas.asp?base=30&sumula=2551 .
5. STJ Súmula 501 e Tema Repetitivo 191: https://processo.stj.jus.br/repetitivos/temas_repetitivos/pesquisa.jsp?cod_tema_final=191&cod_tema_inicial=191&novaConsulta=true&tipo_pesquisa=T ; REsp 1.117.068/PR.
6. Lei 13.445/2017 arts. 100–105, Planalto https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2017/lei/l13445.htm ; STJ Informativo 898, 25/08/2026 (AgRg na HDE 13.803-EX julgado em 19/08/2026): https://scon.stj.jus.br/jurisprudencia/externo/informativo/?acao=pesquisarumaedicao&livre=%270898%27.cod.

## 2. PENDENTE / NÃO VERIFICADO

- **Texto autêntico e histórico:** cotejar o DOU de 1984 e eventuais retificações com a Câmara e Planalto; há aparentes erros de formatação na versão digitalizada da lei original; verificar integralidade em subunidades e vigência contextual.
- **Jurisprudência:** leitura dos votos/acórdãos e dissensos (STF Súmulas 611/711, STJ Tema 191, AgRg HDE 13.803), delimitação precisa de ratio e alcance; ainda não há revisão exaustiva.
- **Sistemática:** tratados, extradição, transferências de execução e de pessoa condenada, coisa julgada, competência e efeitos de sentenças estrangeiras dependem de inventário conjunto T23/T26/T27/T48.
- **Especialidade:** não levantadas exaustivamente as derrogações das regras gerais do CP por 6–10 leis penais especiais para prova do art.12.
- **Reforma:** mérito da ultratividade, remissões, moeda e territorialidade permanece `Q`; sem `C0-J`, `C1` ou `M` aprovada; sem revogação/veto/transição projetados.
- **Verificações:** CI deve rodar no commit final. Validação estrutural NÃO atesta equivalência semântica ou constitucionalidade.

## 3. PRÓXIMO PASSO EXECUTÁVEL

**T25.M01 / issue #31:** cotejar o espelho literal das 39 subunidades com **publicação autêntica do DOU** de 1984 e versões subsequentes, documentar diferenças genuínas versus erros de digitalização; criar amostra explicitamente delimitada de **6–10 leis penais especiais**, com exceções aos arts.1º–12, especialmente art.12; incluir Lei 13.445/2017 e tratados em matriz de dependências T23/T26/T27/T48.

**Entregável e aceite:** concordância `origem × versão temporal × destino × efeito` para o recorte; 6–10 leis com indicação de artigo preciso, sem exceção presumida; ao menos 3 casos judiciais efetivamente confrontados; hipóteses de reforma C1/M expostas como alternativas, sem ratificação automática.

**Fila:** Parte Geral T25.M02 (arts. 13–31) — texto autêntico, jurisprudência e revisão adversarial; T25.M03 — penas/consequências; coordenação com decisão DEC-016 quanto ao veículo do Código.

## 4. COORDENAÇÃO

**Regimes afetados:** T01.M01/M04; T02; T23; T25.M02/M03 e leis especiais; T26/T27; T47/T48. **CF/1988:** legalidade (art.5º XXXIX), retroatividade benigna (XL), competência e STJ homologação (art.105 I i), e garantias penais pertinentes; reforma constitucional separada como hipótese. **Estado da decisão:** nenhuma nova aprovação material do usuário. **CI:** pendente de conferir após este commit. **`main`:** sem alterações adicionais observadas até a gravação.

- [x] Versão `main` e PR conferidos.
- [x] Fonte textual compilada vinculada a 39 IDs, com limites, sem declaração C0-J.
- [x] Fichas `Q` e remissões transversais, sem alteração silenciosa de outros módulos.
- [x] Resultado/pendências/próximo trabalho gravados na mesma branch.
- [ ] Conferir CI estrutural e SHA final após a gravação.

**Protocolo:** `governanca/18_PROTOCOLO_CONTINUIDADE_POR_RODADA.md`.
