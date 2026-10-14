# T29.M01 / F3-E — protocolo de leitura e tabulação de indeferimentos SUIBE

**Data:** 14/10/2026 · **Estado:** metodologia preparada **sem acesso ao XLSX**, sem execução de contagens e sem equivalência presumida entre `motivo` e `erro jurídico`. Fontes: [catálogo SUIBE/INSS](https://dadosabertos.inss.gov.br/dataset/beneficios-indeferidos-plano-de-dados-abertos-jun-2023-a-jun-2025), [ficha agosto/2026](https://dadosabertos.inss.gov.br/dataset/beneficios-indeferidos-plano-de-dados-abertos-jun-2023-a-jun-2025/resource/673c05c7-93a1-4d6c-9cdd-1d9208a4df20), [BEPS agosto/2026](https://www.gov.br/previdencia/pt-br/assuntos/previdencia-social/Dados-estatisticos-previdencia-social-e-inss/boletins-da-previdencia-social/2026/beps082026_final.pdf).

## Portas sequenciais, sem pular etapas

**G0 — obtenção lícita e proveniência.** Somente recurso público oficial funcional ou documento encaminhado pelo órgão. Registrar URL de origem, nome do arquivo, bytes, SHA-256, competência declarada, data e hora da extração, versão da ficha CKAN, restrições de licença e erros de download. **403 não é zero registros**. Dados pessoais, se houver, permanecem fora do repositório GitHub; publicar somente agregados justificáveis.

**G1 — cabeçalho e esquema real.** Ler na própria planilha original as grafias e tipos dos campos; conferir se a planilha tem uma ou mais abas, linhas de metadados, células mescladas, nomes de códigos, valores em branco, datas Excel e linhas repetidas. O catálogo **só anuncia** as colunas competência indeferimento, espécie, motivo, forma de filiação, UF, data indeferimento, DER e outras. **Não assumir** que esses nomes correspondem literalmente ao cabeçalho da planilha.

**G2 — dicionário e unidade observacional.** Obter codificação de motivo e espécie e regras de múltiplos motivos. Não inferir que uma linha representa **requerimento único** ou **pessoa única** até a documentação confirmar. Registrar se `DER` significa data do requerimento do mesmo despacho e se competência representa data da negativa ou da extração.

**G3 — controle de integridade.** Contar linhas efetivamente válidas, vazios por coluna, duplicatas possíveis sem identificar terceiros, resultados de conversões de data e códigos desconhecidos. Fazer listagem anonimizada de categorias e frequência dos códigos **sem divulgar valores de identificação**; se faltar dicionário, usar códigos como brutos, sem criar classe jurídica especulativa.

**G4 — universo antes da taxa.** Separar RGPS, benefícios acidentários, BPC/assistenciais e legislação especial conforme espécie/dicionário; explicitamente marcar `NAO_CLASSIFICADO` quando impossível. **Não** dividir indeferimentos por concessões do mesmo mês para calcular taxa de coorte. Tentar reconciliar total mensal da mesma fonte e definição com BEPS, explicando diferença de corte/escopo/despacho/retificação.

**G5 — tabulações apenas com denominadores reconhecidos.** Para cada competência de despacho e espécie (e, quando possível, forma de filiação), somar **linhas válidas do universo**. Em seguida, agrupar por motivo, gerando `n_{m,e,f,t}` e, se motivos forem mutuamente exclusivos, `n_{m,e,f,t}/N_{e,f,t}`. Havendo múltiplos motivos por despacho, declarar frequências de **ocorrências** sem pretender que a soma de proporções seja 100%. Registrar critério de tratamento de motivos ausentes. Evitar células pequenas identificáveis e não publicar cruzamentos com datas individuais, CPF ou nascimento.

**G6 — confronto jurídico, posterior e separado.** `Motivo do indeferimento = classificação administrativa declarada`. `Indeferimento indevido = resultado de revisão/julgamento/auditoria sobre caso e norma aplicável`. Não são intercambiáveis. Para filiação, perguntar exercício/inscrição/tipo e data; para guarda, data do óbito e EC 103/Tema 1.271; para maternidade, STF ADIs 2.110/2.111; para desemprego STJ Tema 1.360. Se for preciso avaliar ilegalidade, planejar auditoria com universo, regra e provas, não inferir da planilha.

**G7 — versões e inferência.** Não homogeneizar códigos de motivos de 2024 com 2026 sem mapa de mudanças. Não atribuir à codificação CLF qualquer efeito causal sobre indeferimentos. Para avaliação de política, exigir coortes DER de pedidos protocolados e seus desfechos, temporalidade da decisão final e eventual tratamento de vieses por espécie, UF, categoria e canal.

## Estrutura mínima do produto agregado futuro (quando houver arquivo)

| campo | significado |
|---|---|
| `competencia_despacho` | mês de classificação conforme documentação, não DER |
| `especie_codigo_original` / `especie_interpretada` | código bruto e classificação auditável, com `INDETERMINADO` se necessário |
| `categoria_regime` | RGPS/acidentário/assistencial/legislação especial/indeterminado |
| `forma_filiacao_original` | valor bruto, sem converter automaticamente em filiação legal |
| `motivo_codigo_original` | código literal, não “fundamento juridicamente correto” |
| `motivo_rotulo_fonte` | descrição do dicionário oficial/versionado, se existir |
| `n_registros` | contagem de linhas de registro segundo unidade declarada |
| `denominador_interno` | número de registros válidos **mesmo universo/mês/espécie/filiação**, quando admissível |
| `percentual_interno` | somente se denominador materialmente comparável e motivo único, com fórmula publicada |
| `url_fonte`, `versao`, `sha256_arquivo`, `nota_qualidade` | proveniência e ressalvas |

## Testes de aceitação antes de publicar estatística

- Contagem total da base deve reconciliar linhas válidas, linhas descartadas e códigos ausentes; ninguém chama `missing` de indeferimento por falta de filiação.
- A soma dos grupos no mesmo recorte tem de igualar o total de registros **se cada registro tiver motivo único**; com múltiplos motivos, declarar o motivo dessa divergência.
- As espécies assistenciais **não** entram no denominador estrito do RGPS.
- Conferir amostras de transformações de datas/UF/filição sem exportar linhas individuais.
- Guardar dicionário, fórmula, chaves de filtro, data de extração e eventuais diferenças entre planilha SUIBE e BEPS.
- Se o dado permanecer inacessível, **nenhuma tabela de frequências é produzida**, e o status permanece `Q_EMPIRICA_SEM_DADOS`.

## Alternativas de acesso ao XLSX e contato

O [Portal INSS do conjunto SUIBE](https://dadosabertos.inss.gov.br/dataset/beneficios-indeferidos-plano-de-dados-abertos-jun-2023-a-jun-2025) e a ficha do recurso apresentam metadados, mas as URLs S3 publicadas para julho/agosto 2026 retornaram **403 Forbidden** na pesquisa; rota oficial de API CKAN não ficou acessível e a execução local não conseguiu resolver o host. Não há espelho licenciado e íntegro verificado. A [minuta de pedido LAI F3-E](F3E_MINUTA_PEDIDO_LAI_SUIBE_NAO_PROTOCOLADO.md) solicita **arquivo já existente, dicionário e documentação**, sem afirmar protocolo e sem requerer criação de relatório inédito. [O INSS usa Fala.BR para pedidos de informação](https://www.gov.br/inss/pt-br/acesso-a-informacao/sic-servico-de-informacao-ao-cidadao/como-utilizar).

**Não executado:** download de bytes XLSX, cálculo de frequências, tratamento de dados pessoais, solicitação LAI, contato com INSS, algoritmo automático de concessão ou reforma C0/C1/M.
