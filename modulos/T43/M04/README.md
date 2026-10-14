# T43.M04 — Governo Digital
**Fase:** F0 e F1 seletivo em andamento; não incorporado à `main`; issue [#42](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/42). O módulo é **autônomo** em relação ao T07.M03, e sua abertura não aprova automaticamente a arquitetura R2.

- [F0/F1: dossiê de âmbito, direito vigente e limites](DOSSIE_01_F0_F1_GOVERNO_DIGITAL.md)
- [F1: inventário prioritário de 76 unidades estruturais, com fonte e estado Q](INVENTARIO_F1_PRIORITARIO.csv)
- [Pacote de continuidade](CONTINUIDADE_01.md)

**Fonte:** [Lei 14.129/2021 atualizada, Câmara](https://www2.camara.leg.br/legin/fed/lei/2021/lei-14129-29-marco-2021-791203-normaatualizada-pl.html), arts. 1–9 e 42–43. Outros artigos **não** foram auditados nesta rodada. A transposição literal e jurídica permanece Q; dois incisos foram vetados. A interface com [T07.M03 PR #39](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/39) será verificada sem confundir emissão/recebimento de comunicação com o momento de ciência processual.

**Próximo:** cotejo histórico dos arts. 2/42/43, normas de dados e assinaturas, aplicação federativa do art.2º, e concordância com T07/T01/DEC-016.

## F1-A/B — 16 unidades literalmente cotejadas na Câmara (14/10/2026)
- [Transcrição focal art. 2º/42/43 — 16 unidades](F1A_ESPELHO_LITERAL_02_42_43.csv), [relatório de âmbito/remissões](RELATORIO_F1A_AMBITO_DOMICILIO_PROVAS.md). Cobertura estrutural F1 do piloto: 76 unidades (inclui 2 vetos); **60 ainda sem transcrição**.
- [Verificador de fonte externa](../../../scripts/validar_t43_f1a_16.py), [CI #38554726682 aprovado](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38554726682), [JSON com hash e 16 resultados](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38554726682/artifacts/11888466504): zero ausências na fonte consolidada Câmara. [Dossiê da validação](RELATORIO_F1B_VALIDACAO_EXTERNA_16.md) e [Continuidade 02](CONTINUIDADE_02.md).
**Limite:** verificação textual na página completa não resolve DOU/cadeia histórica/efeitos de “esta Lei” ou o alcance por ente; toda C0-J Q. Integração com T07 PR39 e DEC-016 ainda condicionada.

## F1-C/D — 76 unidades extraídas e interface bilateral (14/10/2026)
- [Espelho por artigo de 76 unidades da Lei 14.129](RELATORIO_F1C_ESPELHO_76_LEI14129.md), com [script reexecutável](../../../scripts/extrair_t43_76.py) e [CI #38555902096 aprovado](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38555902096): **74 dispositivos de conteúdo normativo e dois vetos; 16 espelhos manuais cotejados, 0 divergências**, [CSV+JSON com hash da fonte](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38555902096/artifacts/11889257820); [continuidade 03](CONTINUIDADE_03.md).
- [Resposta técnica à conciliação de 26 campos de T07](PARECER_F1D_INTERFACE_BILATERAL_T07.md): quatorze funções com suporte normativo mas formato técnico proposto, oito especificações novas M potencial, quatro efeitos jurídicos reservados ao processo/lei especial. Contrato R2 **não aprovado**.
**Próximo:** edição 2021 original/DOU, revisar 60 novas extrações, inventariar arts.10–41/44–57, integrar LGPD e leis de assinaturas e completar decisão T01 DEC-016.
