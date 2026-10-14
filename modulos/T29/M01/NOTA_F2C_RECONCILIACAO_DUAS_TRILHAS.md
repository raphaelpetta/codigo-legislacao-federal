# T29.M01 — Reconciliação das duas trilhas F2-C

**Corte:** 14/10/2026 · **Issue:** #40 · **PR:** #41 (draft). Esta nota é coordenação de pesquisa, **não decisão C0/C1/M**. Identificadas duas séries F2-C no mesmo PR. Não apagar arquivos sem revisão.

## Referência provisória e complemento

| Objeto | Referência principal provisória (trilha P) | Controle complementar (trilha E) |
|---|---|---|
| Entidades | [P01–P19, 19 conceitos](F2C_MODELO_ENTIDADES_E_VINCULOS.csv) | [E01–E15, 15 conceitos](F2C_ESQUEMA_CONCEITUAL_15_ENTIDADES.csv) |
| Origem e destino | [34 origens normativas](F2C_CONCORDANCIA_ORIGEM_CONCEITO_DESTINO.csv) | [56 regras/transições de F2-A e F2-B](F2C_CONCORDANCIA_FUNCIONAL_56_REGRAS.csv) |
| Não regressão | [20 invariantes G](F2C_INVARIANTES_DE_NAO_REGRESSAO.csv) | Dez invariantes narrativos no [relatório E](RELATORIO_F2C_MODELO_UNIFICADO_CONCORDANCIA_E_TESTES.md) |
| Casos anteriores | [47 IDs](F2C_REGRESSAO_47_CENARIOS.csv): 35 condicionais, 12 com questão jurídica | [Mesmos 47 IDs](F2C_AUDITORIA_NAO_REGRESSAO_47_CASOS.csv): 40 controles condicionais, 7 Q retidas |
| Testes novos | [4 testes N01–N04](F2C_TESTES_ADICIONAIS_COLISAO_2026.csv) | Não há repetição |
| Parecer | [Relatório P](RELATORIO_F2C_ARQUITETURA_CONCORDANCIA_E_CHOQUE_ART73A.md) | [Relatório E](RELATORIO_F2C_MODELO_UNIFICADO_CONCORDANCIA_E_TESTES.md) |

**Decisão metodológica provisória:** linha **P19** como referência de F2-C (maior separação de categoria temporal, grupo familiar, procedimento, versão de fonte e direito adquirido); linha E15 como **auditoria de cobertura**, não arquitetura concorrente a expandir. A [matriz de 15 correspondências E→P](F2C_RECONCILIACAO_15_PARA_19_ENTIDADES.csv) documenta convergências e desdobramentos. As 34 origens normativas e 56 regras funcionais são dimensões complementares, **não 90 dispositivos novos**. Os 47 testes são os mesmos, **não 94**; com N01–N04 há **51 cenários distintos**.

**Critério de prudência:** 12 casos classificados com questão jurídica na trilha P e 7 Q na trilha E refletem critérios de risco distintos. Não inferir que cinco dúvidas estejam resolvidas; prevalece reserva mais protetiva por caso, antes de futura redação C1/M.

## Achado obrigatório de integração: art. 73-A duplicado

- [Lei 15.415/2026](https://www2.camara.leg.br/legin/fed/lei/2026/lei-15415-25-maio-2026-799179-publicacaooriginal-179514-pl.html), publicada **26/05/2026**, criou **Lei 8.213 art. 73-A** com prazo de 30 dias para salário-maternidade pago diretamente pelo INSS e concessão provisória se ultrapassado o prazo. **Vigente desde a publicação**.
- [Lei 15.371/2026](https://www2.camara.leg.br/legin/fed/lei/2026/lei-15371-31-marco-2026-798908-publicacaooriginal-178711-pl.html), publicada **01/04/2026**, prevê **outro art. 73-A** de salário-paternidade, mas **vigência em 01/01/2027**.
- [Compilação oficial Câmara da Lei 8.213](https://www2.camara.leg.br/legin/fed/lei/1991/lei-8213-24-julho-1991-363650-normaatualizada-pl.html) exibe ambas referências.

**Colisão real de numeração; efeito jurídico futuro em Q.** Não há base para eliminar automaticamente o art. 73-A materno, renumerar o paterno por mera edição ou antecipar a vigência de 2027. Interessa primariamente a T29.M05 (benefícios), T29.M06 (processo) e T01 (técnica de vigência); T29.M01 apenas referencia condições de segurado e dependente. Saneamento normativo exige decisão de governança e espécie jurídica apropriada.

## Próximos passos e fronteiras

1. **F3-A comparada** com a arquitetura P19 como hipótese e E15 como teste cruzado.
2. Antes de F4/F5, revisar os 12 casos sinalizados na trilha P, conservar sete Q da E e comparar reservas por ID.
3. Submeter o choque do art. 73-A à coordenação dos módulos M05/M06/T01 sem editar os arquivos desses módulos.
4. Nenhum arquivo fora T29.M01 ou na `main` foi alterado; nenhum C0/C1/M, revogação, merge ou solução de jurisprudência aprovada. PR permanece **draft**.
