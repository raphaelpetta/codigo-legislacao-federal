# T43.M04 — F1-C: espelho reproduzível das 76 unidades (Lei 14.129/2021)
**Corte:** 14/10/2026 · issue [#42](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/42) · PR [#43](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/43) draft. Este relatório registra um **resultado documental**: não houve aprovação C0-J, C1, M, R2 ou revisão de todo o diploma.

## FEITO — ampliação efetiva do cotejo
- `scripts/extrair_t43_76.py` + `.github/workflows/extrair-t43-76.yml`: **extração artigo-local** do conteúdo HTML da [Lei 14.129/2021 atualizada na Câmara](https://www2.camara.leg.br/legin/fed/lei/2021/lei-14129-29-marco-2021-791203-normaatualizada-pl.html), gerando texto individualizado de todos os IDs do inventário prioritário.
- [Execução CI #38555902096](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38555902096), job `extrair_76` **aprovado**; [artefato ZIP com CSV e JSON, hash SHA-256 da fonte e data/hora de obtenção](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38555902096/artifacts/11889257820).
- **76/76** unidades extraídas dos arts. 1º–9º e 42–43, com **74 unidades de texto normativo e duas marcadas VETADO** (art. 4º I e art. 7º §1º V). **16/16** unidades previamente transcritas manualmente nos arts. 2º, 42 e 43 coincidiram com o novo parser. **60 unidades adicionais** passaram a ter espelho *extraído* no artefato; **não** foram objeto de cotejo manual individual de um segundo leitor.
- O script e a configuração do job são versionados na branch: o artefato pode ser produzido novamente. A disponibilização no GitHub Actions pode ter prazo de retenção, mas o método de geração permanece.

## Problemas jurídicos detectados pela extração sistemática
**Art. 3º (26 diretrizes):** o tratamento digital deve preservar inclusão presencial, acessibilidade, atendimento a pessoas de baixa renda/áreas isoladas, linguagem clara, presunção de boa-fé, interoperabilidade, proteção de dados, e a vedação de exigências duplicadas. A redação não pode ser convertida em um catálogo de serviços *exclusivamente* digitais. Os incisos IX e XXIII remetem expressamente à LGPD, ao CTN, à LC 105 e ao sigilo aplicável.

**Art. 4º (definições + veto):** a transposição não poderá criar definição substantiva onde houve veto, nem trocar `esta Lei` por referência a todo o futuro CLF (ampliando alcance). O parágrafo único importa conceitos da LGPD; deve continuar norma de interface.

**Arts. 5º–6º:** execução de processos eletrônicos não elimina exceções de escolha do usuário, inviabilidade, indisponibilidade ou risco relevante à celeridade; meios em papel podem ser utilizados nessas situações com digitalização posterior. A escolha do canal no art. 6º é **distinta** da opção pelas comunicações do art.42; não fundir os dois regimes.

**Art. 7º e incisos §1º:** níveis de risco e remissões **a sete posições I–VII, com a quinta vetada**. Não substituir em todo o Estado uma lista de assinaturas por obrigação de certificado ICP-Brasil em todos os atos, nem criar comando vetado. Há relação com a Lei 14.063/2020 e outras seis normas referidas no texto.

**Arts. 8º–9º:** o protocolo é ato praticado pelo interessado, reconhecido no recebimento pelo sistema; regra de 23h59 do último dia e horários em **Brasília**, com exceções legais e regulamentação de falhas. **Recibo de protocolo não é recibo de intimação** e nem prova de ciência de uma decisão administrativa já proferida.

**Arts. 42–43:** ferramentas para o regime de opção de comunicações eletrônicas dentro dos entes/usuários do art. 2º; autenticação, **emissão e recebimento mesmo sem leitura**, auditabilidade, cinco anos de guarda mínima dos dados de envio/recebimento e uso do meio eletrônico quando lei especial só mencione pessoal/postal, sem alterar automaticamente os critérios legais de ciência e prazo do procedimento. Estado/município só no alcance e momento dos atos próprios de adoção.

## Qualidade e limites
O parser reconstrói texto a partir de linhas do HTML; foi confrontado automaticamente com os 16 registros manuscritos, não validado contra fotografia do DOU nem todos os elementos DOM por auditor humano. Isso é uma **porta textual provisória**, não um texto pronto para promulgação. Os 76 IDs não abrangem arts. 10–41, 44–57, disposições alteradoras de outras leis ou todos os atos infralegais; o instituto de Governo Digital requer integração LGPD/LAI/Lei 14.063 e legislação setorial. A cláusula de validade de um único Código sob `DEC-016` segue aberta.

## PENDENTE / PRÓXIMO
**PENDENTE:** comparação 2021 original x atualizada 2026, cadeia DOU/retificações, revisão humana das 60 unidades novas, inventário do restante da lei, atos de adoção subnacionais, LGPD/LAI e classificação remissão `esta Lei`. **PRÓXIMO:** testar a interface de 26 campos da PR #39 contra os dispositivos agora individualizados, classificando cada campo como exigência legal já existente, detalhe operacional proposto, ou determinação de efeito jurídico por T07/lei especial, sem ratificar arquitetura R2.
