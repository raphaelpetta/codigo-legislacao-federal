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

## F1-E — cobertura completa por artigo 1–55 (14/10/2026)
- [Relatório e correção do limite da lei](RELATORIO_F1E_ARTIGOS_10_41_44_55.md), [inventário dos 44 artigos restantes](INVENTARIO_F1E_RESTANTE_ARTIGOS_10_41_44_55.csv), [extrator](../../../scripts/extrair_t43_resto_44.py) e [CI #38558404950 aprovada](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38558404950), com [CSV/JSON/hash do texto extraído](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38558404950/artifacts/11891385637).
- **A Lei14.129 termina no art.55**, não no art57, como constava incorretamente em relatórios iniciais agora retificados. 44 novos artigos por bloco: **38 materiais, 4 alteradores (51–54), 1 veto (46), 1 regra histórica de vigência (55)**; 11 artigos prioritários anteriores já subdivididos em 76 unidades, não somar duas vezes.
- [Continuidade 04](CONTINUIDADE_04.md). **Não** equivalência jurídico-material nem inventário fino completo dos arts.10–41/44–55. Próximo: controlar alterações efetivas nas quatro leis de destino, vacatio antiga, art.2 III e DEC016.

## F1-F — 183 subunidades e veto do art. 32 derrubado (14/10/2026)
- [Relatório F1-F](RELATORIO_F1F_183_SUBUNIDADES_VETOS_E_ART32.md), [extrator por subunidade dos 44 artigos restantes](../../../scripts/extrair_t43_restante_fino.py) e [workflow próprio](../../../.github/workflows/extrair-t43-fino.yml) [CI #38561552561 aprovado](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38561552561), [CSV/JSON/hash](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38561552561/artifacts/11893440118).
- **183 registros** novos + 76 prioritários = **259 unidades estruturais** da Lei14.129; seis vetos sem conteúdo somados, **art32 vigente após rejeição de veto (DOU11/06/2021)**. [Continuidade rodada05](CONTINUIDADE_05.md). Os arts51–54 são alteradores de outros diplomas, art55 vacatio histórica.
**Próximo:** conferir independentemente os textos extraídos, DOU original e efeitos das alterações; C0-J permanece Q e R2 não está aprovada.

## F1-G — nove posições históricas de veto da Lei 14.129 (14/10/2026)
- [Relatório de cotejo publicação original/compilada e vetos](RELATORIO_F1G_CADEIA_NOVE_VETOS.md) + [matriz com 9 decisões históricas](MATRIZ_F1G_NOVE_POSICOES_VETOS_2021.csv) + [script/verificador](../../../scripts/auditar_t43_vetos_2021.py), [CI #38566127903 aprovado](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38566127903), [artefato JSON/hashes](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38566127903/artifacts/11895825425).
- **Sete vetos mantidos** (seis marcadores no texto consolidado mais **art.32 parágrafo único suprimido**, embora apareça texto na publicação original); **dois rejeitados** (art.32 caput e **art.35**, restaurados DOU 11/06/2021). Art.35 contém **recurso em 10 dias desde ciência e prazo de 5 dias para autoridade superior**; art.37 Lei9.784 subsidiária e interface com T07 PR39.
- [Continuidade rodada06](CONTINUIDADE_06.md). Quadro histórico não adiciona art32 PU aos 259 registros textuais nem homologa C0-J; DOU, competências/DEC016 e revisão humana ainda pendentes.

## F1-H — cinco publicações oficiais na cadeia dos vetos (14/10/2026)
[Matriz de 5 eventos 30/03–11/06/2021](MATRIZ_F1H_CINCO_EVENTOS_DOU_2021.csv), [relatório sobre efeitos editoriais e jurídicos](RELATORIO_F1H_CRONOLOGIA_PUBLICACOES_2021.md), [teste de páginas oficiais com hashes](../../../scripts/auditar_t43_cronologia_2021.py) e [continuidade07](CONTINUIDADE_07.md). Republicação de **14/04** corrigiu art32 como VETADO; retificação de **27/04** corrigiu **razões do veto**; promulgação de **10/06**, publicada **11/06**, restabeleceu art32 caput e art35, **não art32 parágrafo único**. C0-J Q; DOU fac-símile e DEC016 pendentes.

## F1-I — proveniência dos arts. 51–54 e Lei 14.534/2023 (14/10/2026)
- [Matriz de 14 posições de destino](MATRIZ_F1I_14_DESTINOS_LEI14129_51_54.csv) e [relatório dos quatro diplomas alterados](RELATORIO_F1I_DESTINOS_LEIS_ALTERADAS.md): 5 posições com texto reescrito pela **Lei 14.534/2023** (Lei 7.116 art.3º g e §§1º–3º; Lei 13.460 art.10-A §1º), outras 9 com proveniência Lei14.129/2021 na compilação consultada. Incluem Lei12.527 art12 e Lei12.682 art3. Não recodificar redação 2021 como vigente quando sucedida por lei 2023.
- [Validador](../../../scripts/validar_t43_f1i_destinos.py), workflow `validar-t43-f1i.yml` e [continuidade 08](CONTINUIDADE_08.md). **C0-J Q**, intertemporalidade/DOU/DEC016 ainda não aprovados.

## F1-J — cinco textos históricos 2021–2023 e implementação do CPF (14/10/2026)
- [Cotejo literal cinco dispositivos Lei14.129→Lei14.534](F1J_COTEJO_LITERAL_5_POSICOES_2021_2023.csv), [parecer histórico e material](RELATORIO_F1J_COTEJO_5_POSICOES_2021_2023.md), [script com quatro fontes Câmara e SHA256](../../../scripts/auditar_t43_f1j_cinco.py) / [workflow](../../../.github/workflows/auditar-t43-f1j.yml), [continuidade09](CONTINUIDADE_09.md). A auditoria externa encontrou **cinco textos de 2021, cinco de 2023 e os cinco destinos atuais**, sem divergência de localização nas fontes.
- Lei7.116 art3 g/§§1–3 e Lei13.460 art10-A §1 sofreram reescrita, com diferenças materiais de identidade/CPF, dados biométricos e alcance do dever. Lei14.534 art9 fixou **12 meses para adequação dos sistemas** e **24 meses para interoperabilidade dos cadastros**; são prazos históricos, não nova vacatio CLF.
- Nove outras posições dos arts51–54 seguem a auditar; **não duplicar artigos alteradores**, C0-J Q, atos DOU/DEC016 pendentes.

## F1-K — nove destinos remanescentes de 2021 localizados na legislação atual (14/10/2026)
- [Nove dispositivos de destino em texto integral](F1K_NOVE_DESTINOS_LITERAL_2021_2026.csv) + [dossiê de proveniência 14 posições](RELATORIO_F1K_NOVE_DESTINOS_2021_2026.md), [comparador de cinco fontes oficiais](../../../scripts/auditar_t43_f1k_nove.py), [CI #38586703047 aprovado](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38586703047), [JSON/hashes](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38586703047/artifacts/11904884118) e [continuidade10](CONTINUIDADE_10.md).
- **9/9 redações de 2021** ainda localizadas na consolidação de 2026 (Lei7.116 art3 h; LAI12.527 art12 C/§§1–2; Lei12.682 art3 C; Lei13.460 art7 §6/10-A C/§§2–3) + **5 posições reescritas em 2023** (F1-J) = **14 posições rastreadas dos arts51–54 da Lei14.129**. C0-J Q; não recodificar alterações legislativas em duplicidade nem reabrir prazos históricos.
