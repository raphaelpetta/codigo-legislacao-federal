# T29.M01 — Nota de conciliação dos dois conjuntos F2-C

**Data de corte:** 14/10/2026. **PR:** [#41](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/41), draft. **Natureza:** coordenação e reconciliação de documentação concorrente; NÃO é terceira versão substantiva de modelo, nem aprovação C0/C1/M. Todos os arquivos originais são preservados até revisão jurídica. Não alterar outras frentes nem a `main`.

## 1. Duplicação detectada no mesmo módulo e branch

Dois conjuntos F2-C foram entregues no **mesmo PR #41 e branch**, abordando a mesma etapa, com organização diferente:

| Conjunto | Produtos | Significado |
|---|---|---|
| **A — modelo funcional** | [15 entidades](F2C_ESQUEMA_CONCEITUAL_15_ENTIDADES.csv), [56 correspondências](F2C_CONCORDANCIA_FUNCIONAL_56_REGRAS.csv), [47 casos](F2C_AUDITORIA_NAO_REGRESSAO_47_CASOS.csv), [relatório](RELATORIO_F2C_MODELO_UNIFICADO_CONCORDANCIA_E_TESTES.md), [pacote rodada 10](PACOTE_CONTINUIDADE_RODADA_10.md) | Mapeia **cada uma das 33 regras F2-A + 23 transições F2-B** para conceitos e entidades. 40 casos com controle conceitual condicionado e **7 Q**. |
| **B — ampliação normativa e intertemporal** | [19 entidades](F2C_MODELO_ENTIDADES_E_VINCULOS.csv), [34 grupos de fonte/conceito/destino](F2C_CONCORDANCIA_ORIGEM_CONCEITO_DESTINO.csv), [20 garantias](F2C_INVARIANTES_DE_NAO_REGRESSAO.csv), [47 casos](F2C_REGRESSAO_47_CENARIOS.csv), [4 casos novos](F2C_TESTES_ADICIONAIS_COLISAO_2026.csv), [relatório](RELATORIO_F2C_ARQUITETURA_CONCORDANCIA_E_CHOQUE_ART73A.md) | Compara **grupos legislativos**, não as 56 regras 1:1. Adiciona fonte versionada, situação contributiva, direitos adquiridos e **colisão art73-A entre duas leis de 2026**. 35 casos com ressalvas condicionais e **12 Q**. |

**Não comparar os totais 56 e 34 como se um deles estivesse incorreto:** o primeiro é contagem por **regra/transição funcional**; o segundo é por **grupo de correspondência normativa**. **Não somar 15+19 entidades**: ambos são decomposições alternativas do mesmo universo. **Não escolher uma versão como texto canônico por ordem de commit.**

## 2. Ponte de entidades, sem fusão automática

| Entidade da versão A | Correspondência preliminar na versão B | Questão |
|---|---|---|
| E01 Pessoa, E02 Regime, E03 Atividade | P01 Pessoa, P02 Regime, P03 Atividade | Sem divergência estrutural relevante localizada |
| E04 Vínculo + E05 Filiação | P04 Vínculo + P05 Categoria por intervalo | **A separa FILIAÇÃO como entidade; B a representa como atributo/resultado do vínculo e sua categoria.** Escolha requer teste de temporalidade e de inscrição facultativa |
| E06 Cadastro, E07 Período de qualidade | P07 Cadastro, P06 Qualidade por intervalo | Conceitos análogos com campos e temporalidade diferentes |
| E08 Evento modificador | P03/P06/P14 (atividade, qualidade, evento) | B distribui fatos de mudança por domínio; A tem evento de modificação próprio |
| E09 Responsabilidade contributiva, E10 Histórico | P09 Obrigação de recolher, P08 Histórico contributivo | Sem absorver os deveres de custeio em M01 |
| E11 Evento protegido, E12 Relação de dependência | P14 Evento, P11 Relação + P12 Classe/equiparação | B separa as classes e equiparações de relações |
| E13 Prova, E14 Direito prestacional | P13 Prova, P15 Pretensão + P19 Exceção/direito adquirido | B distingue direito adquirido de prestação e procedimento |
| E15 Versão de fonte | P17 Fonte/versão + P18 Regra jurídica aplicada | B distingue ato/versionamento de interpretação material |
| Sem equivalente isolado em A | P10 Grupo de economia familiar + P16 Procedimento/decisão | Podem ser subdomínios ou entidades próprias; não forçar nova norma apenas por escolher banco de dados |

**Porta de qualidade para F2-D:** documentar a razão de manter FILIAÇÃO, EVENTO MODIFICADOR e DIREITO ADQUIRIDO como entidade própria ou atributo do vínculo/resultado, sempre sem perda dos efeitos do direito positivo. Nenhum dos esquemas é implantação de software nem dispositivo legislativo.

## 3. Divergência nos resultados dos 47 testes

Ambos recuperaram os **mesmos 47 IDs anteriores**, mas suas regras de rotulagem **não são idênticas**:

- Conjunto A: **7 casos** com `PENDENTE_POR_Q`.
- Conjunto B: **12 casos** com `PRESERVADO_COM_QUESTAO_JURIDICA`.
- **5 casos** são Q em ambos: `F2A-T02`, `F2A-T10`, `F2A-T15`, `F2A-T16` e `P18`.
- **9 casos** receberam rótulos diferentes: `F2A-T03`, `F2A-T11`, `F2A-T14`, `P04`, `P05`, `P15`, `P17`, `P24`, `P26`. **Não assumir que rótulo conservador de B com Q signifique que o próprio caso é juridicamente indecidível**; por exemplo, ter uma questão de idade abstrata na categoria facultativo não impede resolver caso de pessoa maior de 16 com requisitos cumpridos. Inversamente, A sinalizou Q específicas (P15 remuneração inferior ao mínimo; P26 termo preciso da qualidade) omitidas como Q por B.
- **Critério conservador de controle antes da conciliação:** manter **14 casos em revisão** (união dos 7 e 12 conjuntos), **33 condicionais**; isso é **sinalizador interno de revisão**, não resultado final dos testes, nem 14 negativas ou violações jurídicas demonstradas.

**Próxima revisão caso a caso:** definir Q por fato específico, não pelo tema amplo da categoria; graduar `CONCLUSAO_NORMATIVA`, `PROVA_FALTANTE`, `JURISPRUDENCIA_PENDENTE` e `DESTINO_MODULAR`; rejeitar tanto falsa segurança quanto marcação excessiva de dúvida.

## 4. Lacuna substantiva que exige inclusão no controle comum

**Leis 15.371 e 15.415 de 2026:** os dois diplomas **inseriram art. 73-A** na Lei 8.213 com objetos diferentes, mas vigência desencontrada:
- [Lei15.371, de 31/03/2026, arts.8 e 14](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/lei/l15371.htm), DOU **01/04/2026**: novo art73-A de **salário-paternidade**, com eficácia prevista **01/01/2027**.
- [Lei15.415, de 25/05/2026, arts.1 e 2](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/lei/l15415.htm), DOU **26/05/2026**: novo art73-A de **salário-maternidade**, **já vigente** desde publicação (prazo de concessão de 30 dias, eventual concessão provisória, garantias de análise e irrepetibilidade salvo má-fé).

A colisão é **documental/estrutural comprovada**; não concluir efeito revogatório automático após 01/01/2027. A versão A referia genericamente a lei futura do salário-paternidade, mas **não incorporava expressamente o conflito de numeração**. B abriu **G19/G20** e quatro testes específicos, que devem ser considerados **aditivo necessário a ambos**, sem alterar unilateralmente M05/M06/T28 ou a CF.

## 5. Regras temporárias de coordenação

1. **Preservar as duas versões integralmente**; nenhuma exclusão ou renomeação até conciliação por titular designado.
2. O [pacote da rodada 10](PACOTE_CONTINUIDADE_RODADA_10.md) é o pacote do conjunto A; **esta nota** serve de adendo para o conjunto B, sem suplantar A nem criar dois pacotes com o mesmo nome.
3. No PR, qualquer referência a "F2-C concluída" significa **modelo preliminar duplo sujeito à revisão**, não concordância homologada.
4. **Responsabilidade sobre o T29.M01 deve ficar centralizada numa conversa/frente** durante F2-D; trabalho paralelo só com repartição explícita por arquivo/questão. Não abrir outra F2-C concorrente.
5. F2-D deverá reconciliar os **9 casos com status divergentes**, a ponte E/P e a colidência do art73-A. Pesquisa **F3-A comparada poderá ocorrer de modo independente**, mas a F4/F5 normativa não deve depender de concordância ainda divergente.
6. **Reserva de competência:** M01 sujeitos/qualidade/dependentes; M02 custeio; M03–M05 prestações; M06 procedimento; destino exato de maternidade/paternidade e solução legislativa do art73-A exigem coordenação central. Nenhuma C0/C1/M ratificada.

## FEITO / PENDENTE / PRÓXIMO

**FEITO:** dois esquemas F2-C localizados, 47 IDs idênticos, diferença de 9 classificações e de cardinalidade explicada, colisão de art73-A incorporada às garantias de versão B. **PENDENTE:** adotar arquitetura única, revisar os 9 casos, verificar efeitos legais de janeiro/2027 e titularidade formal, revisar fontes e CI. **PRÓXIMO:** F2-D conciliatória focal, sem novas matrizes duplicadas, antes de qualquer unificação C0/C1/M.
