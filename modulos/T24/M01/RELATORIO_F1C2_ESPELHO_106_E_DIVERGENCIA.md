# T24.M01 — Rodada 05 / F1-C2: espelho literal e auditoria das diferenças

**Corte:** 14/10/2026. **Issue:** #37. **PR:** #38 (draft). **Base CLF main:** `16fba172c875c7a0de388288fe70005c944021d6`.  
**Natureza:** pesquisa documental manual sobre direito positivo; **não é texto de reforma do CLF nem prova de equivalência jurídico-material**. CF/1988 é o parâmetro vigente, CF proposta é estudo externo condicional.

## 1. Fontes, método e nível de certeza

**Fontes primárias efetivamente examinadas em 14/10/2026:**

1. [Câmara — Lei 13.105/2015, publicação original](https://www2.camara.leg.br/legin/fed/lei/2015/lei-13105-16-marco-2015-780273-publicacaooriginal-146341-pl.html), arts. **70–81 e 98–102**.
2. [Câmara — Lei 13.105/2015, texto atualizado](https://www2.camara.leg.br/legin/fed/lei/2015/lei-13105-16-marco-2015-780273-normaatualizada-pl.html), mesmos artigos.
3. [Planalto — CPC compilado](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105compilada.htm), conferência cruzada focal, notadamente art. 75 e art. 77, VI–VII.
4. [Lei 14.341/2022](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2022/lei/l14341.htm), arts. 12–15: alterações do CPC art. 75 III e §5º e regime transitório.
5. [Lei 14.195/2021](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14195.htm), art. 44: inclusão do CPC 77 VII e alterações correlatas aos arts. 231, 238 e 246. **Importante:** a lei alteradora não modifica expressamente o art. 77 VI, embora a pontuação entre as edições da Câmara divirja.

**Método empregado:** comparação visual entre duas apresentações institucionais do CPC, transcrição manual da redação por **unidade funcional** para duas colunas (2015 / edição atual), cotejo com atos modificadores localizados, cruzamento por IDs da matriz F1-C e validação programática de integridade dos CSVs. **Não houve download confiável do HTML bruto nem diff automático entre exemplares oficiais, nem certificação independente de transcrição.** Os endereços e data de leitura documentam a proveniência, mas não são hashes dos arquivos oficiais.

## 2. Resultados documentais

| Recorte | Artigos | Unidades com par textual registrado |
|---|---:|---:|
| 70–76: capacidade e representação | 7 | 41 |
| 77: deveres e sanções | 1 | 16 |
| 78–81: ofensas, dano e má-fé | 4 | 16 |
| 98: âmbito da gratuidade | 1 | 18 |
| 99–102: pedido, impugnação e revisão | 4 | 15 |
| **Total** | **17** | **106** |

**Classificação do cotejo manual:**
- **102 unidades**: texto registrado coincidente entre a versão original da Câmara e sua consolidação, no nível documental visual examinado; **não** validadas por segunda transcrição independente.
- **1 unidade com alteração material expressa:** art. 75 III, representação municipal.
- **2 unidades acrescidas por lei:** art. 75 §5º (2022), art. 77 VII (2021).
- **1 divergência editorial Q:** art. 77 VI, pontuação final diferente entre as duas páginas da Câmara, mas **coincidente entre publicação original da Câmara e texto compilado do Planalto**.

**Conjunto de dados:**
- [F1C2_ESPELHO_UNIFICADO_106.csv](F1C2_ESPELHO_UNIFICADO_106.csv): 106 pares, rótulo de artigo/unidade, fonte, classificação, candidato a módulo e ressalva de certificação.
- Cinco espelhos parciais, mantidos para auditoria por blocos: `F1C2_ESPELHO_LITERAL_70_76.csv`, `_77.csv`, `_78_81.csv`, `_98.csv`, `_99_102.csv`.
- [verificar_espelho_f1c2.py](verificar_espelho_f1c2.py): validador de cardinalidade, duplicidade, artigos, estados e diferenças materiais/estruturais. **Não substitui conferência das fontes oficiais**.
- [F1C_RECONCILIACAO_26_PARA_106.csv](F1C_RECONCILIACAO_26_PARA_106.csv): vínculo anterior das 26 prioridades com 49 correspondências nos registros completos.

O confronto programático executado durante a rodada demonstrou **106 IDs únicos**, nenhuma unidade faltante ou duplicada em relação à matriz F1-C e distribuição 102/1/2/1. A versão do script foi adicionada para execução posterior pelo pipeline; **resultado de CI GitHub só pode ser declarado após sua efetiva consulta**.

## 3. Cadeias de alteração e fonte divergente

### 3.1 CPC 75, III — representação de municípios

A publicação original (2015) representava o Município pelo prefeito ou procurador. A **Lei 14.341/2022, art. 13**, passou a mencionar associação de representação municipal **quando expressamente autorizada**. A eficácia legislativa deu-se na publicação de **19/05/2022** (art. 15 da lei modificadora). É inovação material no **direito positivo**, não categoria M de reforma do CLF.

### 3.2 CPC 75, §5º — condição nova

Inserido pela mesma Lei 14.341/2022; exige **questão de interesse comum** e **autorização específica** do chefe do Executivo municipal, identificando direito ou obrigação objeto da medida judicial. **Não equiparar** associações privadas à Fazenda Pública: art. 12 da mesma lei preserva a separação de prerrogativas. O art. 14 concede dois anos de adaptação a entidades preexistentes: regra temporal, não comando permanente indistinto.

### 3.3 CPC 77, VII — dever cadastral acrescido em 2021

Lei 14.195/2021, art. 44, adicionou a obrigação de manter dados para comunicações judiciais e, na hipótese de remissão legal, tributárias. A **multa específica por ato atentatório do CPC art. 77, §2º**, não passou a mencionar o inciso VII: continuam expressos IV e VI. A mesma lei disciplinou consequências próprias de falta de confirmação de citação eletrônica no **art. 246, §1º-C**, cuja tipicidade e hipótese são distintas e devem ser auditadas em T24.M02.

### 3.4 CPC 77, VI — divergência entre consolidações, não reforma comprovada

- **Câmara, publicação de 2015:** encerra o inciso VI com ponto-final.
- **Câmara, texto atualizado consultado em 2026:** encerra o inciso VI com ponto e vírgula.
- **Planalto, compilação vigente:** encerra o VI com ponto-final, mesmo após inserir VII.
- **Lei 14.195/2021, art. 44:** reproduz expressamente o novo inciso VII, mas **não contém comando de nova redação do VI**.

**Conclusão Q:** não há prova de que o próprio legislador tenha modificado o inciso VI; a diferença é **editorial/documental** e deve ser conferida com o DOU/atos de consolidação antes de fixar versão canônica. O conteúdo substantivo da proibição permanece idêntico nas duas pontuações. Classificar a divergência como `C0` ou reforma material seria indevido.

## 4. Importância sistêmica para a codificação

1. **Capacidade (70–74)**: texto igual não prova ausência de influência da LBI (arts. 84–85), decisões sobre assistência/curatela e regras protetivas; interfaces T13/T17/T32.
2. **Representação e saneamento (75–76)**: a codificação não pode ampliar autorização associativa nem suprimir a oportunidade de saneamento de defeitos, inclusive na fase recursal; interfaces T03/T06/T24.M04.
3. **Sanções processuais (77–81)**: arts. 77 e 79–81 tipificam infrações e consequências diversas, com sujeitos, beneficiários e efeitos diferentes. Um tipo unificado exigiría **reforma M** motivada e teste de garantias.
4. **Gratuidade (98–102)**: preservar distinção entre insuficiência para pessoas naturais e jurídicas, presunção do art. 99 §3º, dever de motivar indeferimento, sucumbência/exigibilidade, requerimento em recurso e revisão; a leitura permanece integrada ao Tema 1.178/STJ e à Súmula 481, analisados em relatório anterior.
5. **Código único e reservas constitucionais**: localização primária em T24.M01 ou interfaces não resolve automaticamente competência/iniciativa, nem o dilema formal DEC-016 sobre promulgação.

## 5. Certificação: o que a entrega NÃO afirma

- **Não** foi feita auditoria exaustiva do histórico de *todos* os atos normativos que poderiam ter modificado/revogado dispositivos no período; compilação atual é indício, não cadeia completa.
- A transcrição é **manual**, com controle de IDs e diferenças entre transcrições, mas sem hash/autenticidade de exemplar bruto oficial nem segunda revisão independente.
- **102 textos coincidentes na pesquisa documental não equivalem a 102 classes C0 jurídicas**. Cada destino proposto exigirá teste de alcance semântico, incidência, precedentes e normas especiais.
- Nenhuma disposição foi transferida para redação final do CLF, revogada, categorizada como C1/M ou confirmada normativamente.
- CI do PR, conferência em DOU, controle material independente e compatibilidade com a Constituição futura permanecem portas separadas.

## 6. Próximo passo prioritário

**T24.M01 — F1-D: inventário articulado do CPC arts. 82–97 (despesas, honorários e perícia)**, porque esses dispositivos determinam o alcance econômico e operacional da gratuidade já pesquisada.

**Critério de conclusão:** identificar todas as alterações materiais e decisões judiciais relevantes (especialmente honorários de sucumbência e condenações), registrar subunidades e eventuais leis estaduais de custas como camada externa, além de localizar T24.M01/T24.M02/T24.M05/T06. Em **paralelo documental**, validar independentemente os 106 pares F1-C2 (DOU, hash ou segunda leitura) antes de qualquer etiqueta C0 ou integração material. Em seguida, arts. 103–118 (advocacia e litisconsórcio), 119–187 e microssistemas.
