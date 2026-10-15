# T25 — Dossiê 10: casos e dosimetria

Corte: 14/10/2026. Esta rodada compara dez casos entre direito vigente e minutas A/B. Categoria Q: nenhuma decisão legislativa aprovada.

## Fontes

- [CPM consolidado](https://www2.camara.leg.br/legin/fed/declei/1960-1969/decreto-lei-1001-21-outubro-1969-376258-normaatualizada-pe.html), arts. 35, 73, 76 e 77.
- [CP consolidado](https://www2.camara.leg.br/legin/fed/declei/1940-1949/decreto-lei-2848-7-dezembro-1940-412868-normaatualizada-pe.html), arts. 20–25 e 65–68.
- [STF Tema 158](https://portal.stf.jus.br/jurisprudenciaRepercussao/tema.asp?num=158).
- [STJ Informativo 823](https://processo.stj.jus.br/jurisprudencia/externo/informativo/?acao=pesquisarumaedicao&aplicacao=informativo.ea&l=10&livre=%270823%27.cod.&refinar=S.DISP.).

## Achado central

O CPM art. 77, parágrafo único, introduzido em 2023, impede pena aquém do mínimo fora das causas de diminuição; o art. 73 disciplina atenuação genérica e o art. 76 disciplina minorantes especiais. O regime CPM art. 35 precisa ser classificado antes de definir os efeitos da pena. O Tema 158 é específico às atenuantes genéricas e não resolve, sozinho, a natureza do art. 35.

A Minuta A tornou obrigatória a redução de erro evitável (P-A3), enquanto CP art. 21 atual diz que a pena poderá ser diminuída. Esta é mudança material M, não uma mera correção editorial. A Minuta B (P-B2) permanece sem regra de cálculo suficiente.

## Entrega

Dez casos no arquivo `CASOS_COMPARADOS_VIGENTE_A_B_CICLO10.csv` e doze problemas no `AUDITORIA_SEMANTICA_MINUTAS_AB_CICLO10.csv`. A resposta judicial nos casos hipotéticos não foi presumida. Permanecem pendentes as versões 2023 e a classificação dos institutos.

## Os dez casos e seus resultados condicionados

| Caso | Direito vigente | Minuta A | Minuta B |
|---|---|---|---|
| P10-01 — erro inevitável de militar, fora do dever militar | CPM 35 permite mitigar/substituir, sem isenção literal geral | PA3 isenta quando inevitável (**M**) | PB2 mitiga, ressalvada questão constitucional **Q** |
| P10-02 — erro evitável de civil | CP 21: redução é **facultativa** | PA3: redução **obrigatória (M inadvertida)** | sem alteração explícita ao CP |
| P10-03 — erro inevitável em crime contra dever militar | CPM 35 exclui benefício específico; exculpação constitucional exige exame | PA3 isenta (**M**) | PB2 mantém exceção, com ressalva genérica constitucional |
| P10-04 — parâmetros STM 7000232 | maioria aplicou CPM 35 abaixo do mínimo; voto divergiu da dosimetria | PA3 não disciplina a categoria do CPM 35; quantum **indeterminado** | PB2 §2 remete para regra inexistente; quantum **indeterminado** |
| P10-05 — ordem criminosa sabida pelo subordinado | CPM 38 §2: subordinado também responde | PA4 §1 conserva imputação pessoal | PB4 a preserva sob regra militar |
| P10-06 — ameaça moral grave para abandonar posto | CPM 40 restringe via de coação, mas CPM 39 pode operar conforme prova | PA4/PA5 permitem exame amplo de inexigibilidade | PB5 conserva CPM 40, ressalvando CPM 39 |
| P10-07 — sacrifício patrimonial superior para salvar desconhecido | CPM 39 protege próprio ou pessoa de vínculo estreito; CPM 43 exige mal causado inferior | PA5 amplia beneficiário, podendo exculpar sem justificar (**M**) | PB6 mantém categorias e restrições |
| P10-08 — excesso por surpresa escusável em defesa | CPM 45 PU não pune quando cumpridos requisitos | PA7 §1 expande mecanismo de escusabilidade ao regime comum (**M**) | PB8 mantém especialidade militar |
| P10-09 — excesso doloso punível menos censurável | CPM 46 admite atenuação | PA7 §2 amplia instituto sem fixar fração ou piso (**M e lacuna**) | PB8 conserva hipótese, mas faltam critérios completos |
| P10-10 — repulsa a agressão por superior conhecido | CPM 47 II retira elementar hierárquica em condições expressas; avaliar demais crimes | PA9 promete regra militar **não escrita** | PB9 transcreve o efeito em síntese ainda não homologada |

Os nove fatos inventados são **testes adversariais**, não julgamentos reais. P10-04 é referência ao julgado existente, não reconstituição de uma sentença contrafactual sob projeto de lei.

## Dosimetria: controle específico CPM 35, 73, 76 e 77

**CPM art. 73:** atenuação sem fração indicada, entre **um quinto e um terço**, observados os limites da pena cominada. **Art. 76:** causas especiais de redução podem operar além dos limites. **Art. 77 caput/PU:** na sequência de fases da pena, apenas as causas de aumento e diminuição permitem ultrapassar limites cominados; esse texto resulta da Lei 14.688/2023. Assim, definir se art. 35 opera como atenuante ou minorante é condição para o cálculo.

O [STM Ap 7000232-60.2024.7.00.0000](https://revista.stm.jus.br/index.php/periodicos/article/download/jurisprudencia-05-v34-n1-2024/88/238), examinado na rodada anterior, registrou maioria de **9 meses e 18 dias de detenção** e divergência de dosimetria por **um ano de reclusão**. Não se deve apresentar as duas espécies de penas como equivalentes. O [STF Tema 158](https://portal.stf.jus.br/jurisprudenciaRepercussao/tema.asp?num=158) e a manutenção da [Súmula 231 pelo STJ em 2024](https://processo.stj.jus.br/jurisprudencia/externo/informativo/?acao=pesquisarumaedicao&aplicacao=informativo.ea&l=10&livre=%270823%27.cod.&refinar=S.DISP.) dizem respeito às atenuantes genéricas; **não solucionam automaticamente a classificação do CPM 35**.

**Contraprova puramente aritmética:** partindo hipoteticamente de 3 anos de pena mínima, uma minorante especial legalmente prevista de 1/3 poderia chegar a 2 anos. Já a simples atenuante genérica de 1/3 na segunda fase não permite redução abaixo de 3 anos. Isto não é cálculo de pena de nenhum processo.

## Auditoria interna e estado da decisão

A [auditoria de 12 problemas](AUDITORIA_SEMANTICA_MINUTAS_AB_CICLO10.csv) identifica, entre outros: PA3 alterando `poderá` para `reduzirá`; PB2 omitindo critério de piso; PA7 §2 sem fração de redução; PA9 sem regra real sobre a elementar CPM 47; PA5/PA6 ampliando inexigibilidade e misturando elementos justificantes; PB5/PB6 sem delimitar integralmente efeitos do CPM 39 e 40; além de ausência de transição material para lei nova.

**FEITO:** dez testes completos em planilha de dados, verificações do CP e do CPM e sua redação de 2023, foco de precedentes STF/STJ/STM, doze problemas com ressalvas. **PENDENTE:** minutas corrigidas e votadas, prova histórica original, inteiros teores adicionais, penal militar especial e coordenação com T16/T26/T27/T45. **PRÓXIMO:** A2/B2 com escolhas materiais rastreadas e teste de concordância contra os mesmos dez casos, ou abertura controlada de T25.M03 para sistema completo das penas.

**Categoria de saída:** estudo F4 e F5 experimental `Q`; **nenhum C0-J, C1 ou M aprovado**.
