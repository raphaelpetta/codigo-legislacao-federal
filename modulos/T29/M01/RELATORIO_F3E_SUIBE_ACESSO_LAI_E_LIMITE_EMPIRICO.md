# T29.M01 — F3-E: acessibilidade dos microdados SUIBE, protocolo LAI e porta metodológica de F4

**Data/corte:** 14/10/2026. **Responsabilidade:** T29.M01 exclusivamente. **Issue [#40](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/40)**; **PR [#41](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/41) draft**. **Nenhum C0/C1/M, F4/F5 aprovado ou texto de lei produzido.** Outros módulos T29.M02/M05/M06 e T01 são interfaces sem edição.

## 1. Resultado da rodada: a fonte existe, os bytes não foram obtidos

A [base oficial INSS “Benefícios Indeferidos” (PDA 2023–2027)](https://dadosabertos.inss.gov.br/dataset/beneficios-indeferidos-plano-de-dados-abertos-jun-2023-a-jun-2025) anuncia competências, espécies, motivos de indeferimento, filiação, UF e DER. A [ficha do XLSX de agosto/2026](https://dadosabertos.inss.gov.br/dataset/beneficios-indeferidos-plano-de-dados-abertos-jun-2023-a-jun-2025/resource/673c05c7-93a1-4d6c-9cdd-1d9208a4df20) indica publicação em **22/09/2026**; o catálogo declara **“No License Provided”**, a ser esclarecido antes de redistribuir dados.

**Tentativas concretas realizadas em 14/10:** download do XLSX de julho e agosto pelos links oficiais para S3: **HTTP 403 Forbidden**; consulta das ações CKAN `package_show` e `resource_show` por ferramenta de web: **não acessíveis nessa ferramenta**; tentativa HTTPS do ambiente executável: **falha DNS de resolução do domínio**. Mudança do idioma/rota do catálogo preserva os metadados, não fornece os bytes dos XLSX. **Não houve processamento de nenhuma linha de benefício.** Não é correto afirmar que o INSS não disponha dos dados ou que os links estejam falhando para todos os usuários; relata-se apenas o resultado das tentativas documentadas. Nenhuma versão íntegra alternativa foi verificada.

[Registro de 10 verificações e limites](F3E_LOG_ACESSO_SUIBE_LAI_TCU_10_VERIFICACOES.csv). Fontes e estados sem porcentagens inventadas.

## 2. Consulta formal pronta, NÃO protocolada

O [INSS indica o Fala.BR como canal único para acesso à informação](https://www.gov.br/inss/pt-br/acesso-a-informacao/sic-servico-de-informacao-ao-cidadao/como-utilizar). A [minuta de pedido LAI para os XLSX e dicionário](F3E_MINUTA_PEDIDO_LAI_SUIBE_NAO_PROTOCOLADO.md) identifica recurso e UUID, erros HTTP, solicita:
- link restaurado ou cópia de **julho/agosto de 2026**, na forma de registros já existentes;
- documentação de layout, dicionário e versão de **código de motivo**, espécie e filiação;
- unidade de observação, duplicidades, data de extração, universo RGPS/BPC/BLE e critérios de revisão;
- se restrição de acesso houver, sua fundamentação e disponibilização da parte não protegida ou agregação já existente.

**O pedido NÃO foi enviado; não há protocolo nem prazo concreto em curso.** A [LAI prevê resposta ordinária em até 20 dias e prorrogação justificada por até dez](https://www.gov.br/inss/pt-br/acesso-a-informacao/sic-servico-de-informacao-ao-cidadao/como-utilizar), a contar da efetiva apresentação. O texto foi redigido para pedir dados existentes, evitando transformar a LAI em obrigação de criação de análise nova. A requisição de microdados deve respeitar proteção de dados pessoais.

## 3. Protocolo analítico condicionado à fonte

O [protocolo F3-E de tabulação](F3E_PROTOCOLO_TABULACAO_SUIBE_E_CRITERIOS_QUALIDADE.md) estabelece portas:
- G0: obter arquivo oficialmente e documentar URL, SHA-256, bytes, versão/licença;
- G1–G2: conferir colunas **reais** e unidade observacional/versão de códigos, não presumir o que anuncia o catálogo;
- G3–G4: testar nulos, duplicação, datas, espécies e separar **RGPS, assistência/BPC, acidentários e BLE**;
- G5: calcular frequência somente com **denominador de mesmo universo, espécie, filiação e competência**, distinguindo registro, requerimento e pessoa;
- G6: classificar motivo do despacho como **declaração administrativa**, não prova de indeferimento ilícito; isso exige auditoria jurídica de fatos/provas e norma aplicável;
- G7: série histórica apenas com mudança do dicionário considerada, análise causal somente com desenho robusto.

A F3-E **não aplicou** o protocolo a planilha alguma porque não obteve bytes. O resultado principal é um método auditável que poderá ser executado quando houver dados, sem anunciar resultados inexistentes.

## 4. TCU: situação de cumprimento permanece em seu último nível individualizado comprovado

Nesta rodada não se localizou, nas pesquisas direcionadas, ato oficial posterior que **reclassificasse individualmente** as oito determinações em cumprimento do [Acórdão 985/2026](https://btcu.apps.tcu.gov.br/api/obterDocumentoPdf/80248239), relacionadas ao Acórdão 634/2025. Assim, **mantém-se a última classificação específica encontrada**: **três CUMPRIDAS** (9.2.2, 9.2.6 e 9.2.10) e **oito EM CUMPRIMENTO** (9.2.1, 9.2.3, 9.2.4, 9.2.5, 9.2.7, 9.2.8, 9.2.9 e 9.2.11) **na deliberação de maio/2026**. **Isso não é certificação de que permaneciam oito pendentes em outubro**: a classificação não foi atualizada por prova conclusiva posterior encontrada. [Matriz F3-D por item](F3D_MONITORAMENTO_TCU_985_2026_11_ITENS.csv).

O [Acórdão 2.207/2026](https://pesquisa.apps.tcu.gov.br/doc/acordao-completo/2207/2026/Plen%C3%A1rio) confirmou alto risco no sistema previdenciário, mas não permite inferir estado específico de cada ordem TCU 2.002/2024, 2.591/2024 ou 1.498/2026. **Prazo decorrido não prova cumprimento nem descumprimento.**

## 5. Implicações ao CLF: preservar a fronteira normativa e processual

A experiência das F3-A/B/C/D/E **documenta problemas reais de cadastro e de instrução**, mas não comprova a eficácia causal de uma arquitetura legislativa. O material empírico oficial disponível indica a importância de:
- filiação do segurado obrigatório derivada da atividade e prova, **não dependente de perfeição do CNIS** (titular M01);
- retificação do histórico cadastral e possibilidade de contraditar falhas, com comunicação e prova (titular M06);
- revisão de enquadramento contributivo sem dispensar norma de custeio específica (titular M02);
- preservação do direito prestacional e do melhor benefício, sem condições implícitas de carência inconstitucional ou discriminação de dependentes (titular M05);
- versões de normas, emendas, jurisprudência e efeitos futuros, incluindo colisão de numeração art.73-A de Leis 15.415/2026 e 15.371/2026 (interface T01/M05/M06).

A opção **A** (núcleo comum de sujeitos/qualidade e módulos especializados) e **B** (regimes separados com coordenação) continuam alternativas não ratificadas; **C** (fusão integral) conserva risco alto de alteração material indireta. A base de dados **não resolve** qual é superior em custo, litigiosidade ou justiça distributiva. Para qualquer recomendação de reforma, preservar os **51 casos F2-C**, as Q facultativo 14/16, PSA, guarda pós EC103/Tema1271 e o estudo de competência/espécie DEC016.

## 6. Estado e portas de continuidade

**FEITO:** recuperação dos metadados e erro verificável dos downloads; verificação pública da política de LAI do INSS; minuta pronta mas não enviada; protocolo técnico de análise; registro de fontes e não fontes; comparação com monitoramento TCU anterior sem atualização fictícia.

**PENDENTE:** XLSX de julho/agosto não acessados, dicionário oficial não obtido, nenhuma taxa de motivo ou erro calculada, estados específicos dos comandos TCU não atualizados por ato posterior, acertos CNIS e coortes DER sem números; revisão por donos M02/M05/M06/T01 não realizada e F2-D separada.

**PRÓXIMO:** (i) **requerimento LAI, somente por ação autorizada e registrada**, ou URL oficial acessível; (ii) tabulação sob critérios G0–G7 após obtenção de dados; (iii) ensaio de duas arquiteturas A/B com confronto material da concordância e avaliação das Q. **Sem novos downloads repetidos se a rota e o erro não mudarem**; o valor de uma nova rodada é cumprir condição de acesso ou passar à F4-0 (quadro de alternativas condicionado, sem escolher reforma), não repetir F3-E.

**Governança:** PR #41 draft; nenhum merge, nenhuma reforma M/C0/C1 aprovada, nenhum arquivo de outros módulos alterado.
