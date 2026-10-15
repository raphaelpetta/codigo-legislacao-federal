# Protocolo de triagem de leis, alterações e destinos na CLF

**ID:** CLF-GOV-021 · **Data:** 15/10/2026 · **Estado:** PROPOSTA DE MÉTODO (não decisão de mérito) · **Vinculação:** DEC-001/003/005/007/010/012/014/016; T01.M04 e T07.M03.

## 1. Três perguntas separadas

1. **Norma de origem:** que texto estava/está vigente, em que versões e momentos, para quem e sob qual competência?
2. **Destino editorial:** em que parte/título/módulo, texto histórico, acervo externo ou transição a norma estará localizada?
3. **Decisão legislativa futura:** se e como poderá ser revogada, substituída, transformada ou modernizada, com espécie, iniciativa e quórum juridicamente próprios?

Não se conclui (3) só porque (2) foi resolvida. Localização editorial não confere validade legislativa ao CLF.

## 2. Níveis de análise obrigatórios

- **Diploma**, com ementa, data, espécie, autor, origem, atualização e revogações.
- **Dispositivo**, com artigo/parágrafo/inciso, texto original, texto vigente em data de corte, alteração introduzida, revogação e remissões.
- **Evento de mudança**, com lei alteradora, objeto-alvo, diffs, vetos, vigência, data de efeitos e transições.
- **Regime jurídico**, potencialmente distribuído entre diplomas, com conflitos, especialidades, remissões, decisões judiciais e interfaces constitucionais.

Um diploma de alteração pode conter simultaneamente dispositivos que alteram outra lei, criam regras autônomas, dispõem sobre vigência e disciplinam transições. Nunca etiquetar o diploma inteiro como 'mera alteração' sem conferir artigos próprios.

## 3. Classificação de atos (descritiva, multi-rótulo)

- `ALTERADORA_PURa` — só modifica/revoga dispositivos anteriores, ressalvadas fórmulas estritamente instrumentais; classificar com auditoria dos artigos.
- `ALTERADORA_MISTA` — altera diplomas e institui ao menos uma regra autônoma relevante.
- `REGIME_NOVO` — institui ou substitui regime substancial, podendo revogar lei anterior.
- `REGIME_AUTONOMO_ESPECIFICO` — lei nova de alcance setorial particular, ainda candidata ao Código.
- `TEMPORARIA_ORCAMENTARIA_INDIVIDUAL` — efeitos pontuais, localizados, anuais ou exauridos; manter em acervo rastreável.
- `SEM_CLASSIFICACAO` — levantamento inconcluso.

Rótulos `ALTERA`, `REVOGA`, `INSTITUI`, `REGULAMENTA`, `TRANSITORIA`, `ORCAMENTARIA`, `DENOMINA` e `ESTRUTURA` podem coexistir; a ementa orienta triagem, mas não decide categoria.

## 4. Destino proposto dos dispositivos (sem declarar revogação)

| ID | Destino | Critério preliminar |
|---|---|---|
| NUCLEO | Texto do CLF proposto | Regra geral/permanente, com competência e espécie identificadas. |
| ALVO_ALTERADO | Incorporado ao texto-alvo no inventário vigente | Artigo alterador que passa a integrar outro diploma; conservar evento e efeitos remanescentes. |
| RESIDUAL | Disposição própria da lei alteradora | Regras autônomas, transições, exceções, cláusulas de efeitos, revogações históricas. |
| EXTERNO_COMPETENTE | Catálogo vinculado, fora do corpo legislativo federal | CF/EC, direito estadual ou municipal, tratados (com atos próprios), atos privativos e infralegais. |
| EXTERNO_TEMPORAL | Arquivo histórico / anexo de transições | LOA, leis de crédito, atos de efeito consumado, medidas individuais e normas sem aplicação prospectiva; preservar possíveis efeitos residuais. |
| PENDENTE_Q | Não classificado | Vigência, interpretação, controle constitucional, espécie, iniciativa ou alcance controvertido. |

**'Excluído do núcleo' não significa 'revogado', 'irrelevante' ou 'inexistente'.** Nada é suprimido silenciosamente. É possível fazer consulta unificada do Código e de acervos, preservada diferenciação formal.

## 5. Testes jurídicos antes de incorporar

- CF/1988 vigente, recepção, espécie LC/LO e quórum, reserva de iniciativa, competência federativa; em documento separado, cenário condicional do anteprojeto constitucional.
- Alterações sucessivas, datas de vigência e de produção de efeitos, regime intertemporal, direito adquirido, coisa julgada, ato jurídico perfeito.
- Normas gerais nacionais versus normas administrativas da União; alcance de 'Esta Lei', subsidiariedade e especialidade.
- Perda de proteção por fatiamento de estatutos multissetoriais; impactos penais, processuais, sancionadores, fiscais e orçamentários.
- Exame de vetos, não recepção, decisões de controle abstrato e efeitos vinculantes, sem inferir revogação ou invalidação apenas de jurisprudência não pertinente.
- Migração rastreável C0-T ≠ C0-J; classificar C0/C1/M/Q e testar recontextualização antes de declarar equivalência.

## 6. Como medir 'a maioria das leis é alteradora ou nova?' 

**Situação em 15/10/2026:** a CLF ainda não mediu essa proporção com critérios próprios; dados totais de 'normas' não respondem à pergunta. **Evidência acadêmica recuperada:** Silva (USP, 2023), examinando 6.870 leis ordinárias federais de 1988–2022, identificou 1.929 que alteraram, revogaram ou repristinaram legislação anterior (**28,1%** do conjunto). A autora também menciona **42,39%** de leis alteradoras e informa que mais de 2.500 das 6.870 leis versavam sobre matéria orçamentária: esses números e os respectivos denominadores **não se conciliam diretamente** (1.929 dividido por [6.870 menos mais de 2.500] seria superior a 44%, não 42,39%). Registrar a divergência como questão metodológica a esclarecer, sem transformar os 42,39% em percentual certificado para o universo filtrado. A contagem de 1.929 inclui alterações, revogações e repristinações, **não somente alterações puras**; exclui, conforme nota da autora, algumas mudanças indiretas sem nova redação textual. A cobertura termina em 2022 e não representa automaticamente a CLF permanente. **Fonte:** https://www.teses.usp.br/teses/disponiveis/2/2134/tde-19102023-140622/publico/11737037MIO.pdf (pp. 69–70).

**Universo principal:** leis ordinárias e complementares federais sancionadas/promulgadas em anos completos, por exemplo 2015–2025, conforme classificação consistente; tabular em separado MPs convertidas, decretos-leis históricos, leis delegadas e orçamento. Reexecutar após identificar todas as fontes e lacunas. Preferir censo a amostra; se amostra, sortear estratos por ano, espécie e assunto, com erro amostral.

**Métricas separadas (denominadores explícitos):**
1. Número e percentual de diplomas exclusivamente alteradores, exclusivamente instituintes, mistos e especiais/individuais/temporários.
2. Percentual de dispositivos operativos que modificam legislação anterior versus dispositivos autônomos.
3. Quantidade de eventos de alteração por lei-alvo, efeitos temporais e remissões, produzindo distribuição de concentração por leis receptoras.
4. Cobertura de leis históricas e atualmente vigentes, diferentes coortes, textos dispositivos e regimes de competência.
5. Leis revogadas, disposições de efeitos exauridos e eventos de revogação com preservação documental.

**Fonte de dados:** portal Normas (https://normas.leg.br/busca), com histórico de versões e relações, e planilhas/listagens oficiais da legislação da Presidência e da Câmara, materiais de Dados Abertos da Câmara e Senado, com checagem de texto integral oficial, retificações e datas. A ementa não basta para separar lei alteradora mista de pura. Registrar script ou procedimento, versão da base, data da extração, casos indeterminados e critérios de exclusão. A legislação estadual/municipal e atos infralegais **não** compõem o denominador das leis federais.

## 7. Exemplos de teste inicial

- Lei 14.905/2024 modifica o Código Civil quanto a juros/correção: não tratá-la como novo livro de obrigações; verificar dispositivos instrumentais e efeitos próprios.
- Lei 15.040/2024 institui regime especial de contrato de seguro e revoga parcelas do CC e do DL 73/1966: 'nova' e 'revogadora' coexistem.
- LC 227/2026 cria instituições/processos relativos a IBS e altera múltiplas leis: 'instituinte + alteradora mista' e reserva legislativa complexa; transições da reforma tributária exigem tratamento próprio.
- Lei 9.784/1999 já tem espelho de 215 unidades no T07.M03, todas ainda Q quanto à equivalência jurídica e sem aprovação de revogação.

## 8. Impactos operacionais, sem prejudicar equilíbrio horizontal/vertical

- **Trilha horizontal permanente:** por parte, matriz de leis-âncora, lacunas, leis com múltiplos destinos, impacto em CF e remissões entre títulos.
- **Trilha vertical permanente:** cada rodada de módulo deve entregar inventário de dispositivos + destinação + minuta viva no seu recorte, com controle C0/C1/M/Q.
- **Critério de avanço:** cobertura catalogada e taxa de verificação jurídica separadas de número de linhas de minuta. Não medir maturidade apenas por páginas ou artigos.
- **Gatilhos de integração:** nova lei multitemática, mudança de competência/reserva, supressão de regra protetiva, colisão entre módulos, alteração de fonte nova, transição sistêmica ou decisão constitucional.
- **Duas centrais, decisões independentes:** mensagens CF→CLF e CLF→CF registram pedido, versões e impacto; jamais importar hipóteses materiais automaticamente.
- **Arquivo central recomendado:** tabela futura `catalogo/22_INVENTARIO_DE_DIPLOMAS.csv` alimentada gradualmente por fontes verificadas, com relacionamento `lei_origem → evento_alterador → artigo_alvo → destino_proposto`. Não criar linhas falsas.

## 9. Conformidade de governança

A apresentação das categorias e das fontes-âncora neste documento é **proposta de triagem**, não alteração automática do índice, nem do quadro de decisões. Integrar por PR e homologação da central; preservar `DEC-016` e as garantias de T01.M04 e T07.M03. A LC 95/1998 arts. 13–14 e o Decreto 12.002/2024 arts. 62–64 estabelecem o enquadramento de consolidação a direito constante; reformas materiais 'M' demandam procedimento legislativo próprio e justificativa.

Fontes: 
- https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp95compilado.htm
- https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2024/decreto/d12002.htm
- https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2024/lei/l14905.htm
- https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2024/lei/l15040.htm
- https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp227.htm

## 10. Controle de séries numéricas históricas e completude documental (pesquisa complementar, 15/10/2026)

**Regra:** número máximo publicado **não é contagem exata** de leis e não serve de denominador estatístico. A série federal atual inicia na **Lei 1, de 4/10/1946**, e a LC 95/1998, art. 2º, § 2º, II, continua a série para leis ordinárias, complementares e delegadas. Antes de 1946 ocorreram séries distintas, inclusive 1891–1930, 1934 e 1935–1937, com intercalação de leis, decretos legislativos e resoluções; há também legislação imperial. Há números históricos acrescidos de sufixos (p.ex., Lei 30-A/1947, 369-A/1948). Catalogar decretos-leis, atos institucionais, atos complementares, medidas provisórias e demais fontes por **espécie, época e série**.

**Fontes oficiais:** Lei 1/1946 e coleção histórica da Câmara (https://www2.camara.leg.br/legin/fed/lei/1940-1949/lei-1-4-outubro-1946-364689-publicacaooriginal-1-pl.html); LC 95/1998 (https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp95.htm); coleções históricas da Câmara (https://bd.camara.leg.br); atos institucionais (https://www4.planalto.gov.br/legislacao/legislacao-historica/atos-institucionais); estudo histórico de numeração do Senado (https://www2.senado.leg.br/bdsf/bitstream/handle/id/496763/RIL030.pdf?isAllowed=y&sequence=1); plataforma Normas (https://normas.leg.br/busca).

**Auditoria prospectiva:** criar tabela `SERIE + ESPECIE + ANO + NUMERO + SUFIXO + ATO/EDIÇÃO + PUBLICACAO_DOU + FONTE_PRIMARIA + STATUS_DOCUMENTAL + STATUS_JURIDICO + JUSTIFICATIVA_DA_LACUNA`. Marcar `LACUNA_DOCUMENTAL` apenas depois de pesquisar publicações originais e índices históricos, distinguindo número legitimamente não utilizado, ato não numerado, ato anterior a 1946, lacuna de digitalização e ocorrência efetiva sem texto recuperado. Nenhuma ausência de registro prova inexistência de lei; nenhuma rubrica 'não consta revogação expressa' prova vigência plena.

**Métrica material distinta da alteração textual:** classificação de dispositivo em `REGRA_GERAL_NOVA`, `INOVACAO_NO_REGIME_EXISTENTE`, `ALTERACAO_SEM_NOVACAO_MATERIAL`, `INDIVIDUAL_ORCAMENTARIA_HONORIFICA_TEMPORARIA`, `INDETERMINADA`, admitindo múltiplos rótulos com primária auditável. A pesquisa de Silva (USP, 2023, pp. 69–70) mostra que alteração textual pode criar **direitos ou tipos jurídicos novos**, e que leis sem alteração textual frequentemente são orçamentárias ou simbólicas; portanto **não deduzir 'maioria de regimes jurídicos novos'** da proporção de 1.929/6.870 leis com alterações/revogações/repristinações. O percentual de 42,39% mencionado na p. 70 demanda reconciliação metodológica com a base reportada na p. 69.
