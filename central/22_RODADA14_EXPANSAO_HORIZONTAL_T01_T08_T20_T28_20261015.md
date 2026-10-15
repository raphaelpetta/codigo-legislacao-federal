# CLF — Rodada 14: três novos títulos e auditoria transversal de 48 títulos

**Corte:** 15/10/2026. **Entrega no GitHub:** [PR #59 draft](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/59), encadeado sobre o [PR #58](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/58), sem tocar na main. **Central permanente [#48](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/48)**. Alteração deliberada da priorização após crítica ao foco reiterado em T48/T03/T37: abertura horizontal três títulos novos, extensão limitada T28 e reconciliação da auditoria.

## FEITO — nova cobertura horizontal em 3 títulos até então sem texto no Código

### T01.M01 — LINDB, Decreto-Lei 4.657/1942 arts. 2º–5º

- [Vista documental Q](../produto/vistas/T01_LINDB_ART2_5_PREVIA_Q.md), [espelho 7×7](../modulos/T01/M01_ESPELHO_LINDB_ART2_5_7_Q.csv), [manifesto SHA](../produto/fontes/T01_M01_LINDB_7_R14_v1.json), **4 artigos/7 unidades positivas**. Git blob `be0414b5b5fad67e75ac9dafa8eda072c6ec59dc`. [Câmara atualizada](https://www2.camara.leg.br/legin/fed/declei/1940-1949/decreto-lei-4657-4-setembro-1942-414605-normaatualizada-pe.html) e [Planalto compilado](https://www.planalto.gov.br/ccivil_03/decreto-lei/del4657compilado.htm).
- **Efeitos sensíveis:** art. 2º distingue revogação expressa, incompatibilidade, regulação total, especialidade e não repristinação; art. 3º presunção de conhecimento, art. 4º integração por analogia, costumes e princípios, art. 5º aplicação por fins sociais e bem comum. Não autoriza reforma material ou revogação expressa/tácita do conjunto legislativo pela simples compilação do CLF.
- **Lacuna art. 1º intencional:** o § 2º está **revogado pela Lei 12.036/2009**, e o art. 1º demanda teste de vacatio, republicação e prazo de vigência. Seu conteúdo não foi integrado nem conta como texto positivo; DOU original 09/09/1942 e retificações 08/10/1942 e 17/06/1943 sem cotejo fac-símile. Interface temática T23 sem duplicação.

### T08.M01 — Lei 8.112/1990 arts. 1º–4º

- [Vista documental Q](../produto/vistas/T08_RJU_LEI8112_ART1_4_PREVIA_Q.md), [espelho 5×5](../modulos/T08/M01_ESPELHO_LEI8112_ART1_4_5_Q.csv), [manifesto SHA](../produto/fontes/T08_M01_8112_5_R14_v1.json); **4 artigos/5 unidades positivas**, Git blob `b3aad48b503c3017f42a0c462aaf3b32f6d54f55`; [Câmara atualizada](https://www2.camara.leg.br/legin/fed/lei/1990/lei-8112-11-dezembro-1990-322161-normaatualizada-pl.html) e [Planalto consolidado](https://planalto.gov.br/ccivil_03/leis/l8112cons.htm).
- **Escopo:** servidores públicos civis da União, autarquias e fundações federais, não todos os servidores estaduais/municipais. Definição de servidor, cargo e provimento, ressalvados CF art. 37 e concursos. Art. 4º proíbe serviço gratuito **salvo nos casos previstos em lei**; não transformar em vedação absoluta.
- **Gates:** DOU 12/12/1990, vetos/promulgação 1991, republicação 1998 e decisões constitucionais sobre RJU e diversidade de vínculos (ADI 2.135) sem assumir aplicação irrefletida a todo emprego público.

### T20.M01 — CDC, Lei 8.078/1990 arts. 1º–3º

- [Vista documental Q](../produto/vistas/T20_CDC_ART1_3_PREVIA_Q.md), [espelho 6×6](../modulos/T20/M01_ESPELHO_CDC_ART1_3_6_Q.csv), [manifesto SHA](../produto/fontes/T20_M01_CDC_6_R14_v1.json); **3 artigos/6 unidades positivas**, Git blob `fe31eb04f129673a432310285e3256a0248bc1e9`. [Câmara atualizada](https://www2.camara.leg.br/legin/fed/lei/1990/lei-8078-11-setembro-1990-365086-normaatualizada-pl.html) e [Planalto compilado](https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm).
- **Abrangência e especialidade:** consumidor pessoa física ou jurídica como destinatário final e coletividade equiparada; fornecedores públicos e privados, bens móveis/imóveis materiais/imateriais e serviços remunerados, incluindo operações financeiras, bancárias e securitárias. Excluídas as relações de caráter trabalhista do conceito do art. 3º § 2º; temas T16 e T21 ficam com remissão, sem reprodução da mesma origem em duplicidade.
- **Gates:** DOU suplemento 12/09/1990, vetos e retificação 2007; jurisprudência sobre destinatário final, vulnerabilidade e operações financeiras exige cotejo por hipótese, não interpretação C0-J já homologada.

## FEITO — vertical pequena e diferente do foco repetitivo: T28 CLT

- [CLT arts. 4º–6º, 3 artigos/14 unidades Q](../produto/vistas/T28_CLT_ART4_6_PREVIA_Q.md), [espelho 14×14](../modulos/T28/M01_ESPELHO_CLT_ART4_6_14_Q.csv), [manifesto SHA](../produto/fontes/T28_M01_CLT_14_R14_v1.json), blob `53060ec8de80bf0de9bbc8df9f438d4ad245e875`. Fonte [Câmara CLT atualizada](https://www2.camara.leg.br/legin/fed/declei/1940-1949/decreto-lei-5452-1-maio-1943-415500-normaatualizada-pe.html).
- Art. 4º conta tempo à disposição, § 1º trata especificamente de períodos por serviço militar ou acidente para indenização/estabilidade, § 2º tem **oito incisos subordinados e exemplificativos** sobre atividades pessoais, introduzidos pela Lei 13.467/2017. Art. 5º é igualdade salarial por sexo e **não substitui** CLT art. 461 e Lei 14.611/2023. Art. 6º equipara subordinação telemática e trabalho a distância quando configurado vínculo; não presume vínculo para todo serviço remoto (Lei 12.551/2011).
- **Total T28: 6 artigos/21 unidades positivas Q**, arts. 1º–6º contínuos. PEC de jornada/escala não foi incorporada sem promulgação comprovada.

## FEITO — revisão transversal do produto e da auditoria de 48 títulos

- [Índice de livros](../produto/fontes/indice_livros.json), [Código único de trabalho](../produto/CODIGO_DE_TRABALHO.md), [painel](PAINEL_GERADO.csv), [quadro](QUADRO_PRODUTO.csv), [fila](FILA_TRABALHO.csv) e [guia](../produto/00_LEIA_O_CODIGO.md) atualizados. **204 artigos/637 unidades textuais documentais positivas de origem, +1 histórico T07** = **638 registros do índice**, **20 componentes e 11 títulos**. **37 de 48 títulos permanecem sem vista integrada.**
- [Matriz de auditoria dos 48 títulos, agora reconciliada](01_MATRIZ_AUDITORIA_48_TITULOS_20261015.csv) com o índice: 204 artigos, 637 unidades positivas, 11 títulos representados e 37 sem texto, excluído do denominador positivo o único registro histórico do T07. Mantidos campos zero para C0-J, atualizados próximos recortes dos títulos com conteúdo e observações de caráter experimental.
- [Validador R14](../scripts/validar_r14_horizontal_matriz.py) inclui Git SHA, correspondências 1:1, cardinalidades das quatro fontes e confronto de todos os 48 registros de auditoria com índice; roteiro [validar_operacao_local.sh](../scripts/validar_operacao_local.sh) chama-o. **Os scripts foram criados, mas execução Python/Actions em CI ainda não está demonstrada.**
- Reserva T13 e demais títulos sem texto permanecem intocados; nenhum merge na main, nenhum C0-J aprovado e nenhuma materialidade M implantada.

## PENDENTE

1. **Autenticação:** DOU fac-símile das quatro fontes originais e alteradoras relevantes; LINDB art.1 §2 revogado e retificações; Lei8112 vetos 1990/1991; CDC vetos/retificação 2007; CLT Lei12.551/2011 e Lei13.467/2017; C0-J não certificado em qualquer frente.
2. **Revisão jurídico-normativa:** espécie e competência de LINDB/DEC-016, diversidade de vínculos dos servidores, finalismo e proteção do consumidor, teletrabalho/igualdade salarial. Preservar recepção constitucional, direitos fundamentais e a referência cruzada, sem atribuir competência federal omnímoda.
3. **CI e PRs:** executar os verificadores no checkout real, auditar integração e possíveis conflitos da cadeia draft PRs #49, #53, #54, #55, #56, #57, #58, #59 antes de qualquer proposta de merge. Nenhuma autorização de merge foi concedida.
4. **Escopo:** 37 títulos ainda vazios, sem métrica de cobertura percentual das normas federais como se 11 títulos representassem total da legislação.

## PRÓXIMO

- Alternar **dois ou três títulos ausentes** (p. ex. T09 contratações, T12 tributação, T43 educação, sujeitos à verificação oficial), com recortes textuais e vínculo fonte de origem verificável. Aprofundar algum título distinto das frentes das rodadas R12/R13; não voltar automaticamente T48 ou T03.
- DOU original/retificações e revisão cruzada de lacunas, integração entre versões e efeitos; validar de modo independente todos os scripts e a matriz.
- Manter os objetivos de esforço propostos (aproximadamente **50% expansão horizontal, 30% vertical e 20% QA**) como guia, não quotas automáticas; evitar rodadas sucessivas com mesmo par de títulos.

**Estado operacional:** FEITO 3 títulos novos reais, +14 artigos/+32 unidades, QA transversal; PENDENTE C0-J/DOU/CI e DEC-016; PRÓXIMO expansão diversa. **C0-J=0, M=0, DEC-016 pendente, revogação=0, merge=0.**
