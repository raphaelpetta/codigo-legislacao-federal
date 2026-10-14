# T07.M03 — Ciclo 28: contrato de interface X2/X6 entre processo administrativo e Governo Digital
**Data:** 14/10/2026. **PR #39 draft.** Documento de interface **proposto em T07** para possível revisão futura pelo módulo **T43.M04 (Governo Digital)**, que está **PLANEJADO e não inventariado no catálogo da main**; **não há diretório/branch T43 de implementação auditada** neste repositório no corte. Portanto, este contrato **não inaugura nem altera formalmente o T43**, não ratifica R2 e não autoriza norma CLF.

## 1. Separação de responsabilidades sem efeito material silencioso
**T07 — jurídico/procedimental, fonte de verdade de efeitos:** destinatário/representante, conteúdo obrigatório de intimação, canal legalmente admissível, garantias de defesa e ciência, subsidiariedade da Lei 9.784/1999, lei especial e prazo (termo de ciência, contagem, opções de comunicação, edital e saneamento). A determinação do dia da ciência legal **não deve ser calculada por padrão pela simples existência do log de recebimento**.

**T43.M04 — tecnologia e registros, apenas proposta de responsabilidade:** autoria/identidade técnica, entrega, recibos, integridade, retenção, auditabilidade, disponibilidade e protocolos. A [Lei 14.129/2021, arts. 42–43](https://www2.camara.leg.br/legin/fed/lei/2021/lei-14129-29-marco-2021-791203-normaatualizada-pl.html) prescreve, **no âmbito dos órgãos e usuários de seu art. 2º** e ferramentas do art.42, meios de comprovação de emissão e recebimento mesmo sem leitura, auditoria e conservação de dados de envio e recebimento por **ao menos cinco anos**. T43 não pode atribuir sozinho o efeito de ciência em processos fiscais, previdenciários ou sancionadores sem lei específica.

**Regra de integração:** a interface entrega **eventos técnicos e evidências**; T07 ou regime especial define **efeitos jurídicos**. O T43 pode expor um campo `data_ciencia_juridica` calculado ou registrado **somente com indicação verificável de lei, destinatário, procedimento, regra de contagem e autoridade competente**; fora disso, deve ser `SEM_DETERMINACAO_JURIDICA`, não data improvisada.

## 2. Especificação de 26 campos auditáveis
A [matriz de contrato](CONTRATO_CICLO28_T07_T43_CAMPOS.csv) distingue campos cuja finalidade decorre das normas atuais dos **campos técnicos novos propostos** (`id_comunicacao`, hash, campos de consulta, log de indisponibilidade, etc.), que não podem ser anunciados como imposições textuais existentes na Lei 14.129.

**Estados lógicos distintos, não presunções legais universais:**
- `EMITIDA`: órgão produziu e transmitiu ato com prova da emissão.
- `RECEBIDA`: registro idôneo de chegada técnica segundo o canal/regime.
- `CONSULTADA`: usuário/representante consultou, se existe registro e base legal.
- `CIENTE_JURIDICAMENTE`: satisfeitos os pressupostos da lei aplicável ao caso, inclusive ficções expressas, sem confundir com leitura de arquivo ou entrega interna.
- `PRAZO_INICIADO`: regra específica de contagem, natureza do prazo e eventual indisponibilidade/feriados verificados.
- `FALHA_REGISTRADA`: indisponibilidade técnica; não implica suspensão automática **sem previsão jurídica**.
- `PROTOCOLO_REGISTRADO`: ato entregue pelo interessado; não prova intimação anterior nem por si confere ciência.

**Não derivar automaticamente** transições `EMITIDA→RECEBIDA→CONSULTADA→CIENTE_JURIDICAMENTE→PRAZO_INICIADO`: há processos com ciência ficta sem consulta, recebimento técnico sem leitura, consulta anterior à ficção, prazo com início diferido ou outro canal. O encadeamento é um desenho de estados para auditoria, **não máquina de inferência legal automática**.

## 3. Chave de proveniência por regra e federatividade
**Lei 9.784/1999 arts. 26–28, 41, 69** — [Câmara](https://www2.camara.leg.br/legin/fed/lei/1999/lei-9784-29-janeiro-1999-322239-normaatualizada-pl.html): conteúdo, certeza da ciência, publicação residual, antecedentes de atos, subsidiariedade. **Lei 14.129/2021 arts. 2º, 42–43** — [Câmara](https://www2.camara.leg.br/legin/fed/lei/2021/lei-14129-29-marco-2021-791203-normaatualizada-pl.html): incidência a órgãos federais e demais entes que adotem comandos por atos normativos próprios; opção eletrônica e opt-out quando incidente; possibilidade de ferramenta digital mesmo onde lei especial mencione somente pessoal/postal (art.43 III); requisitos de prova de emissão e recebimento; cinco anos. **Decreto 70.235/1972 art.23 §2º III** — [Câmara](https://www2.camara.leg.br/legin/fed/decret/1970-1979/decreto-70235-6-marco-1972-418562-normaatualizada-pe.html): regimes legais especiais de entrega e consulta; não transportar quinze dias para outros processos.

## 4. Contraprovas de funcionamento sem presumir resultados
1. **Envio confirmado sem recibo:** `EMITIDA`; ainda não provar `RECEBIDA` com requisitos legais quando aplicáveis.
2. **Recibo sem consulta:** `RECEBIDA`; Lei 14.129 art.43 II não exige prova de leitura, mas ciência dependerá de outra norma.
3. **Consulta antes da ficção fiscal:** DTE registra `CONSULTADA`; norma especial pode antecipar `CIENTE_JURIDICAMENTE`.
4. **Ficção fiscal após 15 dias de entrega:** pode haver `CIENTE_JURIDICAMENTE` sem `CONSULTADA` na hipótese legal; não é prazo de defesa de quinze dias.
5. **PAT/Meu INSS, 5 dias desde emissão em portaria:** antes de fixar `CIENTE_JURIDICAMENTE`, controlar hierarquia da Portaria DIRBEN 993/2022 art.20 versus leis superiores, fato e prova; TCU Acórdão 2.002/2024 detectou necessidade de comprovante. Não afirmar nulidade geral.
6. **SEI com cadastro e petição:** STJ MS 24.567/DF validou em circunstâncias específicas; eventos devem conservar contexto, não criar presunção universal.
7. **Ente estadual sem adoção Lei 14.129:** art. 2º III impede atribuir automaticamente todos os requisitos a esse ente por apenas fazer parte do Brasil.
8. **Sistema indisponível no último dia:** guardar `FALHA_REGISTRADA`, avaliar Decreto 8.539 e lei aplicável; não prorrogar todos os prazos por configuração técnica.
9. **Consulta por representante sem poderes:** log não comprova ciência da pessoa juridicamente destinatária sem verificar representação.
10. **Canal facultativo encerrado:** efeitos para futuras comunicações dependem de registro do opt-out, sem invalidar retroativamente atos regulares.
11. **Mensagem enviada ao destinatário errado:** autenticação técnica do servidor não sana violação de destinatário.
12. **Regime especial só prevê forma postal:** art.43 III permite meio digital nos limites de art.42, **não** substitui todas as condições de ciência fixadas em lei especial.

## 5. R2 versus R1 — recomendação condicionada
**R2 (preferência de desenho, não decisão):** T43 mantém padrões técnicos digitalizados com referência a Lei 14.129 e LGPD, T07 retém normas de intimação e exceções, separados por contrato de interface. **Problemas:** T43.M04 ainda PLANEJADO, `DEC-016` (espécies/iniciativa/lei única) irresolvido, diferenças de ente e sistema, concentração indevida de obrigações tecnológicas em lei, risco de remissões entre Livros inviáveis.

**R1:** T07 contém tecnologia mínima junto às salvaguardas; útil se não existir Livro de Governo Digital integrado válido, mas menos modular e exige evitar duplicação do art.43 em instrumentos incompatíveis.

**Cláusula de arquitetura candidata, NÃO texto aprovado:** “A comprovação técnica da comunicação eletrônica observará os requisitos da legislação de Governo Digital aplicável ao órgão e ao usuário, preservadas as condições e os efeitos da intimação definidos nesta disciplina procedimental e nas leis especiais.” **Q:** pode ser C1 em parte, mas remissão entre espécies, extensão de destinatários ou imposição nova são M potencial.

## 6. Aceite e handoff ao T43
Para aceitar R2: (i) abrir F0/F1 efetivo T43.M04 no seu próprio ciclo, inventariar Lei 14.129 art.2/42/43 e LGPD, (ii) validar R2 como arquitetura pelos donos T07/T43/T01, (iii) mapear todos campos do contrato como **norma existente** vs **inovação material** e remissões precisas, (iv) confirmar DEC-016 e forma válida, (v) testar em autos/lógicas reais SEI, fiscal, INSS e no ente subnacional adotante/não adotante, (vi) adotar política LGPD de minimização, controles e guarda de dados, (vii) não misturar ferramenta digital com regra de ciência ficta. **Não existe aprovação nesta rodada.**

**FEITO:** contrato com 26 campos e 12 cenários concretos hipotéticos, proprietários e limites de lei atual versus propostas técnicas. **PENDENTE:** T43.M04 F0/F1, DEC-016, portaria do INSS e cumprimento TCU, aplicação a casos individuais, decisão R1/R2. **PRÓXIMO:** remeter contratualmente a futura frente T43.M04 (sem modificar módulo ausente), elaborar quadro de remissões e classificação C1/M por cláusula X2/X6, preservar aprovação do T07 PR39 como estudo Q.
