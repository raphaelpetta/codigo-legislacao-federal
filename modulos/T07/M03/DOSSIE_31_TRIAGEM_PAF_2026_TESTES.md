# T07.M03 — Ciclo 31: política de triagem intertemporal do PAF, com limites de ciência
**Corte:** 14/10/2026 · **PR #39 (draft)** · nenhuma norma do CLF promulgada, nem C0-J/C1/M aprovada. A triagem é um **artefato de testes**, não mecanismo para emitir intimação, fixar vencimentos ou calcular preclusão em processos reais.

## Base oficial e distinções
A [Receita Federal, orientação sobre prazo de recurso voluntário, atualizada em 18/03/2026](https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/julgamento-administrativo/prazo-do-recurso-voluntario) registra: 20 dias úteis para recurso voluntário ao CARF (Decreto70.235/1972, art.33), prazo específico de **30 dias corridos** no contencioso de pequeno valor com recurso à DRJ-R (Portaria MF 20/2023, art.50), contagem geral em dias corridos salvo disposição em contrário (art.5º), e a salvaguarda transitória do [Ato Declaratório Interpretativo RFB 2/2026](https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/julgamento-administrativo/prazo-do-recurso-voluntario): até a intimação em 31/03/2026, quando prazo alterado pela LC227, prevalece o **prazo que vencer por último** entre 20 úteis e 30 corridos, conforme o caso.

A [Receita — perguntas e respostas sobre prazos LC 227/2026](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/piloto-da-reforma-tributaria/perguntas-e-respostas-prazos-processuais-v2-final.pdf/view) distingue intimações pré-vigência da LC227 em **14/01/2026**, suspensão de prazos **entre 14 e 20/01/2026** (naquele janeiro inicial) e a contagem retomada **21/01/2026**. Em outras ocasiões vigentes o art.5º-A suspende 20/12–20/01. O PAF continua exigindo art.23 para **marco de ciência**, art.5º/5º-A para contagem/suspensão e arts.15/33 para **duração**.

O contrato T07/T43 aprovado? **Não**. Lei14.129 art.43 II exige prova de emissão e recebimento das ferramentas no seu âmbito, **não uma data universal de ciência legal**; Decreto70.235 art.23 é especial. O TCU Acórdão2.002/2024 não resolve em tese a validade de portaria previdenciária ou todos os atos administrativos do INSS.

## Implementação de porta automatizada
[Matriz com 15 hipóteses e fontes](MATRIZ_CICLO31_REGRAS_TEMPORAIS_PAF_2026.csv) e [script com classificação determinística](../../../scripts/validar_paf_2026_t07.py) executado pelo [workflow próprio](../../../.github/workflows/validar-paf-2026-t07.yml). O teste passou no PR, contemplando cinco barreiras adicionais e mantendo todos os registros **Q**. A função responde **qual regime precisa ser pesquisado**, não o dia em que uma defesa vence.

**Categorias explícitas:** (i) ciência não certificada quando o cenário não traz comprovante de recebimento; (ii) PAF anterior a 14/01/2026 com disciplina temporal transitória a verificar; (iii) 14/01–31/03/2026 com maior vencimento entre 20 úteis/30 corridos nos casos contemplados; (iv) após 31/03/2026 prazo de 20 úteis para CARF/impugnação conforme artigos legais, ressalvadas hipóteses especiais; (v) pequeno valor 30 corridos; (vi) Lei9.784 geral e INSS PAT fora da calculadora fiscal.

**Limites técnicos relevantes:** a entrada fictícia `comprovacao_recebimento=SIM` é somente um predicado ilustrativo e **não certifica** ciência jurídica, nem prova evento de entrega nos termos exatos de cada sistema. A classificação do período de transição não resolve o cálculo real do máximo de dois vencimentos. O validador **não conhece feriados, suspensão local, dias de expediente, indisponibilidade, termo de ciência especial, datas de publicação/registro nem natureza do recurso de cada processo**. Não calcular ou publicar data real a partir dos exemplos.

## Contraprovas de regressão
- **C31-03 vs. C31-04:** ciência informada em 31/03/2026 x 01/04/2026 → regime transitório x novo prazo do recurso ao CARF.
- **C31-02/C31-12:** ciência informada em 14/01 ou 20/01/2026 → transição e suspensão de 14 a 20/01; 21/01 é retomada de contagem conforme interpretação RFB.
- **C31-06:** pequeno valor DRJ-R mantém 30 dias corridos, e não aplica o CARF genérico.
- **C31-07:** emissão sem comprovante de recebimento → não certificar ciência; eventual ficção especial só com pressupostos e prova exigíveis, não inferida.
- **C31-10/C31-11:** SEI geral e MeuINSS **não** admitem prazo fiscal de 20 úteis importado por conveniência.
- **C31-13:** prazo para pagamento de exigência deve confrontar art.10 V e transição, não automatizar sem identificar o ato.

## FEITO / PENDENTE / PRÓXIMO
**FEITO:** 15 hipóteses, cinco barreiras de especialidade, script/CI reprodutíveis, fontes federais oficiais, todos os resultados Q. **PENDENTE:** norma de ciência do art.23 aplicada a logs documentados, dados reais de processo fiscal/previdenciário, calendário/feriados/expediente e acesso ao ato interpretativo integral, atualização da cadeia de LC227, governança com T12 e T43, DEC-016. **PRÓXIMO:** casos com atos reais de ciência e impugnação, comparação de data de ciência/contagem/prazo e redação X6 que ressalve intertemporalidade; sem fazer cálculo de vencimento automático até validação jurídica e calendário oficial.
