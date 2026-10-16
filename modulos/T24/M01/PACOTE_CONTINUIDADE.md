# T24.M01 — Pacote de continuidade da rodada 01

**Data/corte:** 14/10/2026 · **Responsável funcional:** frente especializada T24.M01 · **Issue:** [#37](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/37)  
**PR:** [#38 — rascunho](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/38) · **Branch:** `modulo/T24-M01-jurisdicao-sujeitos-f0-f1-20261014`  
**CLF main de entrada, conferida:** `16fba172c875c7a0de388288fe70005c944021d6`  
**CF main identificada:** `f6b95d977bfe293fd393972d499ca5d1965a1bcd` (o texto completo do anteprojeto não foi examinado neste trabalho; apenas as interfaces históricas constantes do CLF).  
**SHAs dos commits de conteúdo:** README `519ae9874cb55cfd5b2de06dba99f9adfaf86594`, inventário `c3d086d0fa6592847368323c77d02257726a418e`, nota `e71a3aa7917a308d1968afc9dcc42ed1048babb0`. O SHA deste pacote é o commit que o incorpora e poderá ser conferido no PR; não presumir hash futuro neste texto.

## 1. FEITO

| Entrega real | Onde | Estado | Categoria jurídica |
|---|---|---|---|
| Conferência da arquitetura e de PRs concorrentes; nenhuma frente T24 identificada | docs/governanca consultados; issue #37 | Pesquisa concluída | Gestão de projeto, não C0/C1/M |
| F0: delimitação dos sujeitos, jurisdição, competência e interfaces com T24.M02–M07/T01/T06/T23 | [README](README.md) | Branch, aguardando revisão | Escopo, não C0/C1/M |
| F1 inicial: **27 registros por faixa/fonte**, grau de leitura e pendências | [INVENTARIO_F1_SELETIVO.csv](INVENTARIO_F1_SELETIVO.csv) | Branch, parcial | Triagem, não transposição literal |
| Diagnóstico: oito problemas e alternativas **não aprovadas**, jurisprudência focal e estatísticas oficiais | [NOTA_01_DIAGNOSTICO_E_OPCOES.md](NOTA_01_DIAGNOSTICO_E_OPCOES.md) | Branch, revisão pendente | `Q` de pesquisa; não constitui decisão normativa |
| PR #38 **draft** para tramitação e revisão central | GitHub | Aberto, **não integrado à main** | F9 documental preliminar |

**Fontes oficiais de fato consultadas em 14/10/2026:** Lei 13.105/2015 atualizada (Câmara/Planalto; blocos e dispositivos parciais), Lei 14.879/2024 (art. 1º), Lei 9.099/1995 (1º–3º, 9º, parcialmente), Lei 12.153/2009 (1º–2º e 5º, parcialmente), Lei 8.906/1994 (arts. iniciais e trechos), LC 80/1994 (início), Lei 8.625/1993 (início), Lei 9.307/1996 (dispositivos selecionados), Lei 13.140/2015 (seleção), CNJ Res. 345/2020 (texto/alterações iniciais), STJ Temas 1.178 e 1.198 (ficha/tese), STF ADI 5.941 (notícia institucional), CNJ Justiça em Números 2026 (notícia e endereço do relatório), leis 15.479/2026 e 15.484/2026 (objeto/referência em fontes oficiais). O texto da Lei 10.259/2001 e todos os pormenores da CF/1988 **não foram conferidos artigo por artigo**.

## 2. PENDENTE / NÃO VERIFICADO

| Lacuna / Q / dependência | Teste necessário | Bloqueia |
|---|---|---|
| Inventário ainda é por **faixas**, não por artigo/parágrafo/inciso | F1-A CPC 1º–20 e 42–69; F1-B restante | Sim — status INVENTARIADO |
| Alterações legislativas históricas e impacto intertemporal | Cotejar versões oficiais e atos modificadores, inclusive Lei 14.879/2024 | Sim — C0/C1 e revogação |
| CF/1988, iniciativas reservadas e anteprojeto futuro | Ler texto constitucional vigente e quadro atual CF; validar interfaces antigas 002/003/013/014/023/027/028 | Sim — reforma institucional |
| Abrangência dos juizados especiais, MP/DP e exceções | Conferir leis orgânicas, leis especiais, tratados e normas estaduais apenas como camadas | Sim — harmonização |
| Ementas/teses e notícias não substituem inteiro teor ou pesquisa jurisprudencial | Ler acórdãos e eventuais mudanças/limitações de STJ/STF | Sim — tese jurídica completa |
| Dados CNJ apenas descritivos | Análise metodológica, séries, grupos e desenho causal para opções materiais | Sim — atribuição de efeitos |
| Decisões normativas | Escolhas do usuário e revisão central | Sim — M aprovada |
| PR/CI | Verificar checks do último SHA e revisão independente | Sim — conclusão estrutural |

**Status jurídico:** C0, C1 e M = nenhum texto classificável criado; Q = hipóteses explicitamente não resolvidas. Nenhuma disposição tem destino codificado aprovado ou comando revogatório.

## 3. PRÓXIMO

**Prioridade única:** T24.M01, F1-A — inventariar individualmente os **arts. 1º–20 e 42–69 da Lei 13.105/2015**, confrontando texto original, redação atual, leis alteradoras e recortes temporais.

**Quem:** frente T24.M01, sob coordenação central CLF.  
**Insumos:** publicação original do CPC, atualizações legislativas oficiais, art. 63 (Lei 14.879/2024), Constituição vigente, quadro atual da CF-projeto, inventário seletivo desta branch.  
**Entregável:** tabela granular por artigo e subdivisão, com proveniência e status de verificação; tabela de titularidade de localização primária T24.M01/T01/T23/T24.M02 e riscos de efeito jurídico.  
**Aceite:** não chamar transposição de C0 sem cotejo literal, não aceitar como exaustivo sem cadeia de alterações, classificar lacunas `A_VERIFICAR`, assinalar exigência de iniciativas/espécies.

**Fila posterior:** ampliar F1 para CPC 70–187; instruir microssistemas dos juizados; aprofundar precedentes 1.178/1.198/ADI 5.941; F2 completo; estudo comparado orientado a problemas.

## 4. COORDENAÇÃO E CONTROLES

- **Central CLF:** não foram editados os arquivos de índice, matriz, protocolo, decisões ou status central.
- **Interfaces normativas:** T01, T06, T07, T13, T17, T20, T23, T24.M02–M07, T29, T32, T43.
- **CF/1988 versus projeto CF:** parâmetros e versões **separados**; matriz histórica de interfaces não é versão do texto constitucional atual.
- **PR/CI:** #38 criado como **draft**; testes de CI do SHA final **não confirmados neste pacote**; nenhuma aprovação ou merge.
- **Governança:** conformidade procedimental pretendida com `governanca/18_PROTOCOLO_CONTINUIDADE_POR_RODADA.md`; o caráter parcial dos registros impede dizer módulo auditado.

- [x] Consultei main e PRs concorrentes ao abrir.
- [x] Separei fontes primárias, anotações editoriais e hipóteses.
- [x] Mantive C0/C1/M sem aprovação e registrei Q.
- [x] Guardei pacote e PR na branch própria.
- [ ] F1 granular e concordância por artigo concluídos.
- [ ] CI verificada no último SHA e revisão independente concluída.
- [ ] Decisões materiais aprovadas/integração efetuada.
