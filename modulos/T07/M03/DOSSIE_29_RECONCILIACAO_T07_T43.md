# T07.M03 — Ciclo 29: reconciliação bilateral dos 26 campos com T43.M04
**Corte:** 14/10/2026 · PR #39 (T07, draft) ↔ [PR #43 (T43.M04, draft)](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/43). A interface é **proposta**, não contrato implementado, espécie legislativa válida ou decisão R2. Todos os campos permanecem Q e requerem decisão T01/`DEC-016`.

## Fatos novos da outra frente
T43.M04 concluiu F1-C experimental: [CI #38555902096](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38555902096) e [artefato CSV+JSON com hash](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38555902096/artifacts/11889257820). Foram extraídas **76 unidades** dos arts. 1º–9º e 42–43 da Lei 14.129/2021 (74 existentes e dois dispositivos vetados), com cotejo automático bem-sucedido de 16 unidades com transcrições manuais; isso **não abrange toda a lei**, não atesta DOU e não constitui C0-J.

## FEITO — reconciliação nominal 26/26
A [matriz bilateral do ciclo 29](MATRIZ_CICLO29_BILATERAL_T07_T43_26.csv) mantém os **mesmos 26 identificadores** do [contrato preliminar do ciclo 28](CONTRATO_CICLO28_T07_T43_CAMPOS.csv), mas distingue **três naturezas jurídicas**:

| Natureza | Quantidade | Significado |
|---|---:|---|
| **EXIGENCIA_EXISTENTE_OPERACIONALIZADA** | 14 | A função encontra suporte na lei positiva (Lei 14.129, Lei 9.784 e legislação de dados); **o formato de campo proposto não é automaticamente obrigação legal já existente** |
| **TECNICA_NOVA_M_POTENCIAL** | 8 | Campo que pode melhorar prova/sistema (ID de evento, hash, timestamps segregados, consulta, indisponibilidade etc.), mas cuja exigência uniforme demandaria avaliação de custo/competência/inovação |
| **EFEITO_JURIDICO_T07_OU_ESPECIAL** | 4 | Ciência jurídica, base da ciência, termo inicial e tipo de prazo **devem ser definidos pelo procedimento**, não inferidos de mero log digital |

**Âncora normativa T43 por ID:** os 26 campos foram analisados à luz do inventário da PR #43, com referências expressas para art. 2º III/§2º, art. 3º XVII, art. 8º caput/§2º, art. 42 caput/§2º e art. 43 I–V. Campos sem fundamento literal direto estão assinalados como `SEM_REFERENCIA_LITERAL_T43`, sem criar citações fictícias.

## Ponto jurídico decisivo: quatro campos não podem virar fórmulas automáticas
**C28-16 — data_ciencia_juridica** depende da Lei 9.784/1999, art. 26 e normas especiais; **C28-17 — base_legal_ciencia** precisa registrar norma e pressupostos, mas não é metadado legal textual imposto pela Lei 14.129; **C28-18 — marco_inicial_prazo** depende da espécie de prazo e da lei correspondente; **C28-19 — prazo_tipo** deve separar comparecimento, instrução, defesa e recurso. A Lei 14.129 art. 43 II exige capacidade de comprovar emissão e recebimento mesmo sem leitura; **não** define ciência ficta universal.

**Exemplo fiscal:** Decreto 70.235/1972, art. 23, §2º III, distingue entrega documentada e consulta antecipada; um evento “RECEBIDA” não equivale sempre à “CIENTE_JURIDICAMENTE”. **Exemplo previdenciário:** Portaria DIRBEN 993/2022 art.20 contém presunção setorial a testar frente à Lei 14.129 e à determinação do TCU 2.002/2024; não presumir legalidade nem invalidade em abstrato. **Exemplo do protocolo:** Lei 14.129 art.8º cuida de ato praticado pelo usuário, cuja recepção pelo sistema não prova a intimação do órgão.

## Onde pode existir reforma material M
Os oito campos novos dependem de decisão se devem figurar na lei, em regulamento técnico ou apenas no esquema tecnológico. Tornar obrigatórios para todos os órgãos um `id_comunicacao`, hash da íntegra, controle de usuário consultante ou campos de timestamp separados **não é cópia literal** dos arts. 42–43. Podem ser boas propostas, mas exigem destinatário, sigilo, LGPD, custos, segurança e coerência federativa, especialmente art. 2º III e §2º. Não confundir `possibilidade de auditoria` com `divulgação pública irrestrita`.

## Critério de aceitação de R2
Antes de escolher definitivamente a repartição T43 (instrumentos/prova) / T07 (efeitos/prazos), exigir: (1) identificação da competência constitucional e da espécie legislativa sob DEC-016; (2) preservação de opt-in/out nos casos legalmente abrangidos; (3) reserva da lei especial para formação da ciência; (4) tratamento da LGPD/LAI; (5) regra de transição, implementação e custeio; (6) testes com dados reais e validação por revisor jurídico. R1 continua opção se a articulação normativa de R2 gerar remissões inviáveis.

## PENDENTE / PRÓXIMO
**FEITO:** 26/26 campos reconciliados, 14 com função jurídica já regulada (sem adotar formato do campo como texto legal), oito especificações técnicas novas e quatro efeitos jurídicos reservados a T07/lei especial. **PENDENTE:** cotejo histórico/DOU, legislação especial e atos federativos, TCU/INSS, confirmação do registro dos eventos reais e decisão DEC-016/R2. **PRÓXIMO:** redline de X2/X6 com esses três tipos, convertendo qualquer dever técnico novo em hipótese M explícita, sem “equivalência” silenciosa; caso real em DTE/Meu INSS com registros de entrega/consulta/prazo.
