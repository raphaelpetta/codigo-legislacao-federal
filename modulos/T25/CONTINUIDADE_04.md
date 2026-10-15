# T25.M01 — Pacote de continuidade 04 (histórico 1984 e dez leis especiais)

**Data e recorte:** 14/10/2026; CP arts.1º–12 e interações amostrais com regras especiais. **Proprietário funcional:** T25.M01. **Issue:** [#31](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/31) · **PR:** [#32 — rascunho](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/32) · **branch:** `modulo/T25-parte-geral-f0-f1`.

**Versões observadas:** `main` do CLF na abertura desta rodada e na checagem antes do pacote = `1974be250848d94eabe1f0000bf424e459fdb8cb`. Diferença desde a rodada 03: commit em T07.M03, governança/status e validador estrutural, sem alteração de arquivos T25 (comparação baseada em `9c84d9c…1974be2`). A PR permanece sobre branch anterior e deve ser atualizada/comparada antes de integração. **`main` do projeto constitucional (referência de coordenação, NÃO incorporada):** `e648bd71227f407f2b46207e9c8d546a255254d2` em 14/10/2026; conteúdo constitucional novo não foi examinado.

## 1. FEITO — arquivos realmente gravados na branch, fora da main

| Entrega | Arquivo | Natureza e limite |
|---|---|---|
| Prova amostral de especialidade de **dez leis** e seus artigos certos | `MATRIZ_ESPECIALIDADE_ART12_CICLO04.csv` | 10 casos de exceção, confirmação e complemento; **não** inventário total |
| Auditoria da reforma da Parte Geral **12 artigos** e **4 dispositivos externos** da Lei 7.209/1984 | `AUDITORIA_HISTORICA_ART1_12_CICLO04.csv` | 16 posições, sem conferir fac-símile DOU; três anomalias de digitalização de texto histórico |
| Análise sistemática, 4 novos problemas `Q`, 15 testes | `DOSSIE_04_ESPECIALIDADE_HISTORIA_1984.md` | hip. PROB-T25-0013–0016; efeitos materiais ainda não homologados |
| Registro de links, responsáveis e escopo no índice | `README.md` | continuação do pacote de ciclos 01–03; nenhuma nova norma aprovada |

**Fontes institucionais verificadas com recorte exato:**
1. [Câmara — publicação original digitalizada da Lei 7.209/1984](https://www2.camara.leg.br/legin/fed/lei/1980-1987/lei-7209-11-julho-1984-356852-publicacaooriginal-1-pl.html), CP arts.1º–12 inseridos pelo art.1º e Lei 7.209 arts.2º–5º; 
2. [Senado — mesma Lei 7.209, texto do Sigen](https://legis.senado.leg.br/norma/549085/publicacao/15715239); [ficha da publicação DOU, Seção 1, 13/07/1984 p.10217](https://legis.senado.leg.br/norma/549085). **Nenhuma cópia fac-similar autêntica foi efetivamente lida**;
3. [Câmara — CP atualizado](https://www2.camara.leg.br/legin/fed/declei/1940-1949/decreto-lei-2848-7-dezembro-1940-412868-normaatualizada-pe.html), arts.1º–12 como controle da redação atual;
4. [Câmara — LEP 7.210/1984 art.204](https://www2.camara.leg.br/legin/fed/lei/1980-1987/lei-7210-11-julho-1984-356938-publicacaooriginal-1-pl.html), vigência conjunta;
5. **Dez leis especiais**: DL 3.688/1941 arts.1º–4º; Lei 9.455/1997 art.2º; CTB Lei 9.503/1997 art.291; ECA Lei 8.069/1990 arts.225–227; Lei 11.343/2006 arts.45–46 e 48; Lei 9.605/1998 arts.2º–3º e 21–24; Lei 13.260/2016 arts.2º §2º, 5º e 10; Lei 7.716/1989 arts.16,18,20-C,20-D; Lei 12.850/2013 arts.1º–2º; Lei 8.072/1990 arts.1º–2º. URLs oficiais individuais e níveis de prova constam do CSV. Atenção especial a alterações de 2025–2026.

**Descobertas centrais:**
- Duas fontes públicas de transcrição de 1984 apresentam possíveis erros correlatos `embora, decorrido`, `praticado a crime` e `aplicam especial se` (CP arts.3º/4º/12). **Sem confronto com DOU verdadeiro, a causa não está identificada**; não tratar como erro comprovadamente original ou como emenda legislativa.
- Lei 7.209/1984 art.2º tinha efeitos em **leis especiais externas ao CP**, e seus arts.3º–5º contêm instrumentos e vacatio; a migração da Parte Geral exige histórico separado.
- Regra comum + exceção específica exige testar **cada efeito jurídico**. No CLF unificado, "deste Código" do CP art.12 muda potencialmente de referente — `Q` de alta prioridade. Não existe prova de C0-J, nem disposição material `M` ratificada.

## 2. PENDENTE / NÃO VERIFICADO

- Obter e conferir fac-símile da Lei 7.209 no DOU 13/07/1984 p.10217 e páginas seguintes, incluindo sequência íntegra; registrar versões, grafia e justificativa para discrepâncias. O período nominal de seis meses após publicação e eventual transição histórica exigem cálculo jurídico de datas e conferência da LEP art.204.
- Separar leis especiais com derrogações comprovadas (LCP e tortura) de regimes aditivos ou processuais; não inferir hierarquia/constitucionalidade de texto só por aparecer em compilação. Identificar jurisprudência e data efetiva de todas alterações de 2026.
- Levantar outras leis: Estatuto do Desarmamento, lei penal militar, eleitoral, crimes financeiros/tributários, crimes cibernéticos, tratados e competências internacionais; sample de dez **não** é inventário exaustivo.
- Examinar, por jurisprudência qualificada, os efeitos da responsabilidade penal da pessoa jurídica ambiental, delitos preparatórios, regime de contravenção no exterior e alcance de normas de trânsito/ECA. Positivação de direitos e restrições permanecem decisões abertas.
- **Categoria:** a atual transcrição C0-T do **texto compilado** (ciclo 03) mantém-se **sem prova de equivalência jurídica C0-J**; mudanças editoriais `C1`, mudanças materiais `M` e qualquer supressão/revogação não foram aprovadas.
- **Fronteira constitucional:** CF/1988 vigente, legislação infraconstitucional; Constituição em elaboração é cenário condicional independente; necessidade de revisão de direitos/proporcionalidade/reserva legal quando avançar.
- **CI e integridade:** após gravar último arquivo, verificar último SHA em GitHub Actions; êxito estrutural não certifica vigência, interpretação, compatibilidade constitucional ou revogação.

## 3. PRÓXIMO PASSO EXECUTÁVEL

**Prioridade:** T25.M01 / [issue #31](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/31): obter a publicação **autêntica** de 1984, reconstruir linha temporal de 12 artigos e disposições transversais 1984–2026 com auditoria de erros; abrir submatriz de leis especiais **com efeito específico no CP arts.1º–12** (não misturar todas as leis penais especiais com derrogações gerais).

**Critério de aceitação:** por unidade, proveniência do texto e datas, qual tratamento necessário em norma comum ou exceção, evidência de vigência/alteração ou marca `A_VERIFICAR`, prova de alcance intertemporal; separar transcrição de redação jurídica transformadora. Preparar nota de integração para T01/T02/T26/T27/T37/T47/T48 e CF conforme pertinente, sem fazer alterações concorrentes.

**Fila:** T25.M02 art.13–31 e responsabilidade pessoa jurídica; T25.M03 sanções, medidas de segurança e jurisdição; comparação crítica de alternativas para art.12 antes de eventual minuta.

## 4. CONTROLE

**Cruzamentos:** T01 (regras gerais/eficácia/revogação), T02 (direitos fundamentais), T23/T47/T48 (tratados e jurisdição), T25.M02/M03/M04–M07, T26 (processo), T27 (execução), T32 (criança/adolescente), T37 (ambiente), T41 (trânsito).

**Ratificação material nesta rodada:** nenhuma. **Integração `main`:** nenhuma. **Revogação e mecanismos legislativos `DEC-016`:** nenhuma decisão/alteração. **CI:** consultar execução do commit final e registrar na PR; não inferir.

- [x] Consultada a versão da `main` e PR antes de escrever.
- [x] Dez diplomas rastreados por artigos e interfaces, cobertura explicitamente limitada.
- [x] Registradas anomalias históricas sem presumir texto oficial errado.
- [x] FEITO/PENDENTE/PRÓXIMO e próxima tarefa reproduzível no GitHub.
- [ ] CI estrutural do commit final e comparação de última hora com a `main`.

**Protocolo:** `governanca/18_PROTOCOLO_CONTINUIDADE_POR_RODADA.md`.
