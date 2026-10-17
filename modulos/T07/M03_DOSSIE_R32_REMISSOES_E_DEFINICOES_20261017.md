# T07.M03 — R32: contraprovas dos dez C1 remanescentes e três remissões críticas

**Corte documental:** 17/10/2026. **Base de origem:** `main` `4cb7eb139ece2380b785eaedc94b9572506cb7e1`. **Seleção H/V/I/D/F:** V+I (auditar dependências que podem contaminar três direitos, reduzir dívida de integração); H preterida nesta rodada por risco de ampliar fontes ainda não autenticadas. **Natureza:** auditoria documental cruzada com máquina; **NÃO** parecer jurídico independente, C0-J, M, FC3 ou reforma aprovada.

## 1. O problema é o destinatário normativo, não apenas o número

A [Lei 9.784/1999, redação institucional atualizada da Câmara](https://www2.camara.leg.br/legin/fed/lei/1999/lei-9784-29-janeiro-1999-322239-normaatualizada-pl.html) usa três remissões cujo referente é **a própria Lei 9.784**. A [prévia do T07](../../produto/vistas/T07_PROCESSO_ADMINISTRATIVO_PREVIA.md) substitui **“desta Lei”** por **“deste Livro”**. No estado documental atual, os destinos simbólicos **existem e o conteúdo-chave coincide**, mas isto pode deixar de ser verdade após reorganização, renumeração, integração com outros regimes ou promulgação. A operação deve continuar `C1_POTENCIAL_Q`, não `C0-J`.

A [matriz de riscos C1](../../central/03_T07_GATE_C1_11_EFEITOS_20261015.csv), a [triagem de 215 unidades](M03/MATRIZ_TRIAGEM_215_UNIDADES_CICLO20.csv), os [12 cenários adversariais](../../central/06_T07_DOZE_CASOS_ADVERSARIAIS_REMISSOES_E_ESPECIALIDADE.csv) e a [prévia gerada](../../produto/vistas/T07_PROCESSO_ADMINISTRATIVO_PREVIA.md) são **evidências diferentes**. A automação cruza as quatro sem fingir que qualquer uma delas autentica a cadeia original do DOU ou o conteúdo jurídico da futura norma.

## 2. Três vínculos conferidos documentalmente

| Origem vigente (Lei 9.784) | Destino jurídico vigente | Destinos atuais no ensaio T07 | Direito/limite que deve continuar protegido |
|---|---|---|---|
| Art. **36** → art. **37** | Art. 37: dever de o órgão instrutor buscar, de ofício, documentos já existentes na Administração | `LPA-SEQ4-036` → `LPA-SEQ4-037` (fonte `EXP17-37-C`) | Ônus do interessado não absorve dever de obter documentos que estão no poder público |
| Art. **49-B** → art. **9º** | Art. 9º: legitimados a atuar como interessados, inclusive titulares de interesses difusos/coletivos | `LPA-SEQ4-051` → `LPA-SEQ4-009` (fonte `EXP15-9-C`) | Participar como ouvinte não altera automaticamente direito de voz ou regras de habilitação |
| Art. **49-D** → art. **26** | Art. 26: intimação, requisitos, ciência, antecedência e consequências de inobservância | `LPA-SEQ4-052` → `LPA-SEQ4-026` (fonte `EXP16-26-C`) | Não equiparar mero envio eletrônico a ciência quando a lei exigir prova do recebimento ou meio apto |

**Constatação importante:** os artigos experimentais **49-B/49-D foram reposicionados** como `LPA-SEQ4-051/052`, mas os números 9, 26 e 37 dos alvos permanecem coincidentes nesta versão. Essa coincidência **não constitui garantia de correspondência** após qualquer outra reordenação. O vínculo jurídico exige identificador original → destino *validado*, com conteúdo, destinatário e temporalidade; número textual solto é insuficiente.

Na [matriz de 215 unidades](M03/MATRIZ_TRIAGEM_215_UNIDADES_CICLO20.csv), os três alvos e as respectivas origens permanecem `NAO_AUDITADA_JURIDICAMENTE / Q`. Logo, a confirmação é apenas de **existência e concordância documental no corte atual**, não da equivalência substantiva. A lei atual da Câmara confirma as obrigações dos arts. 9º, 26 e 37; permanece necessária verificação de textos fac-similares DOU, contexto da vigência e especialidades. [Lei 14.210/2021](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14210.htm) instituiu a decisão coordenada, mantendo exclusões em art. 49-A, §6º; a [Lei 14.129/2021](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14129.htm) requer cautela adicional no tratamento das comunicações eletrônicas, sem revogar implicitamente as garantias de intimação.

## 3. Todos os dez pontos C1 restantes — distribuição da dívida

| ID | Risco | Contraprova / próximo requisito |
|---|---|---|
| `P13-01-C` — art. 1º caput | CRÍTICO | Limitar ao processo administrativo **federal**, sem estender a entes subnacionais por causa do Código único |
| `P13-01-P1` — art. 1º §1º | CRÍTICO | Não ampliar de função **administrativa** de Legislativo/Judiciário da União para funções típicas destes Poderes |
| `P13-01-P2` — art. 1º §2º | ALTO | Definições de órgão/entidade/autoridade limitadas à Lei de Processo Administrativo, não vocabulário universal |
| `P13-01-P2-I` | BAIXO | “órgão -” → “órgão:” é diferença tipográfica, mas seu escopo segue preso ao §2º; conferir fonte |
| `P13-01-P2-II` | BAIXO | “entidade -” → “entidade:” nas mesmas condições e sem proclamar C0-J |
| `P13-01-P2-III` | BAIXO | “autoridade -” → “autoridade:” não muda autoridade decisória; verificar tipografia e contexto |
| `EXP17-36-C` — art. 36 | CRÍTICO | Vínculo com art. 37 e dever de obtenção oficiosa dos documentos públicos, testado documentalmente |
| `C18-49-A-P1` — art. 49-A §1º | ALTO | Decisão coordenada restrita ao procedimento competente e exclusões do §6º |
| `C18-49-B-C` — art. 49-B | ALTO | Vínculo com art. 9º, legitimados, qualidade de ouvinte e voz |
| `C18-49-D-C` — art. 49-D | CRÍTICO | Vínculo com art. 26, ciência/defesa e canal de intimação |

**Art. 69:** `P19-69-C` é o **11º** caso, já objeto da decisão preparatória **DEC-020/FC2**, mas continua `Q_SEM_C0_J`, ainda sem validação de transposição normativa. A DEC-020 não fecha as dez divergências, nem a questão-mãe `QD-2026-003`.

**Atenção às gerações de espelho:** o arquivo de concordância literal anterior do art. 1º conserva “Esta Lei”, enquanto a prévia posterior apresenta “Este Livro”. São duas fotografias editoriais; o analista deve fixar a versão e o SHA, não escolher arbitrariamente um espelho para afirmar identidade com a futura lei. Em nenhum dos casos, igualdade literal comprova por si equivalência constitucional.

## 4. Gate criado e limites expressos

O [mapa R32](M03_MAPA_TRIPLA_REMISSAO_R32.json), o [verificador](../../scripts/auditar_remissoes_t07_r32.py) e as [contraprovas](../../tests/test_auditar_remissoes_t07_r32.py) impõem:
1. **3 vínculos reais** conferidos em fonte C1, triagem de 215 unidades, cenários E04/E12/E08/E09 e prévia Q, com alvo textual correto;
2. **11 C1 integralmente preservados** (`3 + 7 + 1`), sem promover nenhum a C0-J, M, FC3 ou veículo;
3. inexistência de homologação material oculta, origem setorial fixa, DEC-001/019/020 salvaguardadas e **DEC-016 PENDENTE**;
4. rejeição de troca de alvo, desaparecimento de artigo, troca de norma, omissão de contraprova e alteração do status Q.

**O que o gate NÃO faz:** não consulta a versão oficial ao executar CI, não garante autenticidade DOU, interpretação jurisprudencial, validade constitucional de futura espécie, correção da edição original ou invariância semântica para sempre. Testa somente os **quatro arquivos versionados** e a fila de decisões.

## 5. H/V/I/D/F — fecho real desta rodada

**FEITO:** prova documental de existência/identidade dos três alvos na prévia, contagem fechada do universo `3+7+1`, contraprovas automatizadas, delimitação dos direitos e atualização da fila de pesquisa T07. **Não houve nova decisão normativa**: nenhuma pergunta está artificialmente marcada como aprovada.

**PENDENTE:** cotejo DOU e retificação de 1999, datas/alterações posteriores por unidade, análise de processos especiais e intimação digital, parecer independente, integração final dos IDs N:N, texto redacional jurídico homologável, QD-2026-003 e DEC-016. O art. 69 permanece em decisão preparatória FC2.

**PRÓXIMO:** avaliar se o tratamento de remissões por **IDs estáveis com correspondência de direitos** é delimitável como nova subquestão para deliberação; antes disso, aprofundar a interseção das três remissões com exclusões do art. 49-A e regras especiais. Continuar H/V/I sem quotas, conforme ganho marginal global.
