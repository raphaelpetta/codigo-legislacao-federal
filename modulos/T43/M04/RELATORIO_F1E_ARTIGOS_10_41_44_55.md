# T43.M04 — F1-E: inventário completo por artigo da Lei 14.129/2021
**Data:** 14/10/2026. **PR #43 draft**; `main` continua no SHA `16fba172c875c7a0de388288fe70005c944021d6`. A auditoria F1-E é **por artigo** (cabeçalho/bloco de texto), não por todas as unidades legislativas finas, e não permite conclusão C0-J.

## 1. Correção de cobertura e prova reproduzível
**A Lei 14.129/2021 termina no art. 55**, conforme [edição atualizada da Câmara](https://www2.camara.leg.br/legin/fed/lei/2021/lei-14129-29-marco-2021-791203-normaatualizada-pl.html); o registro anterior “44–57” em materiais iniciais de T43 era **erro de escopo**, corrigido nesta fase. São **55 artigos principais**, mas **a lei possui mais de 55 subunidades** (incisos, parágrafos, alíneas e textos alteradores).

- O recorte F1-C prévio extraiu **76 subunidades estruturais dos arts.1º–9º e 42–43**: 74 de conteúdo e dois vetos, artefato [#38555902096](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38555902096/artifacts/11889257820). Desses 11 artigos prioritários, 16 unidades foram também cotejadas manualmente.
- A nova F1-E identificou os **44 artigos restantes (10–41 e 44–55)** em [inventário 44 caputs](INVENTARIO_F1E_RESTANTE_ARTIGOS_10_41_44_55.csv), com fonte, categoria e pendências.
- [Verificador externo específico](../../../scripts/extrair_t43_resto_44.py) + [workflow](../../../.github/workflows/extrair-t43-resto.yml) [**CI #38558404950 aprovado**](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38558404950). [Artefato JSON/CSV dos 44 artigos com hash SHA-256 da fonte](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38558404950/artifacts/11891385637). A rotina confirmou **55 cabeçalhos primários sem faltantes** e extraiu o conteúdo de cada bloco.
- Natureza dos 44 artigos restantes: **38 disposições materiais da própria Lei 14.129**, **1 artigo vetado** (art.46), **4 artigos alteradores de outras leis** (51–54) e **1 artigo de vacatio/entrada em vigor** (55).
- **Registros de veto:** art.4º I, art.7º §1º V, art.46 inteiro. Os primeiros dois já estavam no inventário F1-C, e o terceiro está no novo inventário, **não são comandos normativos vigentes**.

## 2. Achado metodológico: quatro normas alteradoras não podem ser consolidadas duas vezes
- **Art.51:** altera a Lei 7.116/1983 (documento de identificação);
- **Art.52:** altera a Lei 12.527/2011 (Lei de Acesso à Informação);
- **Art.53:** altera a Lei 12.682/2012 (digitalização);
- **Art.54:** altera a Lei 13.460/2017 (direitos do usuário de serviço público).
O conteúdo material alterado passa a integrar o diploma **de destino**, enquanto a regra histórica de modificação deve permanecer na trilha da proveniência, ressalvadas vigência, mudanças ou revogações posteriores e o veículo jurídico adequado. Copiar os artigos 51–54 como se fossem simultaneamente normas gerais autônomas de T43 **e** textos vigentes das leis modificadas geraria duplicação e remissões quebradas. Nada foi incorporado ou revogado pelo CLF.

## 3. Art.55: vigência escalonada e erro de universalização
O art.55 da Lei 14.129 prevê vacatio de **90 dias para União**, **120 dias para Estados/DF** e **180 dias para Municípios**, após sua publicação oficial. Isso deve ser interpretado juntamente com o art.2º, III e §2º: **a lei não dispensa o ato próprio de adoção pelos demais entes**. O termo inicial de vigência do diploma não equivale à adoção automática por qualquer município. A data de vigência histórica permanece registrada e pode não corresponder a efeitos atuais de leis alteradoras.
Um futuro livro CLF não deve copiar literalmente a antiga vacatio sem reclassificação como **norma histórica/exaurida ou disposição de transição distinta**, pois reiniciar por acidente prazos de 2021 em um novo diploma seria alteração material.

## 4. Prioridades de F2 por matéria
**Plataformas e interoperabilidade (arts.10–41):** controle de serviços digitais e arquitetura, compartilhamento de dados, privacidade e interoperabilidade, sigilo LGPD/LAI/CTN/LC105, direitos de correção e monitoramento de dados de referência (art.40), custeio de interoperabilidade (art.41).
**Inovação (44–45 e veto 46):** laboratórios e participação social, sem criar conteúdo para veto.
**Governança, risco e auditoria (47–49):** deveres organizacionais, fiscalização de serviços digitais e proteção de direitos fundamentais.
**Inclusão digital (50):** possibilidade de garantir acesso/conexão para universalização, sem substituir condicional “poderão” por obrigação orçamentária incondicional.
**Alteração legislativa (51–54):** cada texto terá proveniência 1:1 no diploma modificado e sua situação jurídica atual certificada antes da codificação.
**Vigência (55):** regra histórica e diferenças federativas, não norma técnica permanente a transpor ipsis litteris.

## 5. FEITO / PENDENTE / PRÓXIMO
**FEITO:** cobertura **do texto integral por ARTIGO de todos os 55 artigos principais**, com os 11 já recortados em subunidades finas e novos 44 por artigo (CI e hashes reproduzíveis); reconhecidos 3 dispositivos vetados (2 incisos/1 artigo), 4 artigos alteradores e uma regra de vigência. **PENDENTE:** subunidades individuais dos arts.10–41 e 44–55, cotejo histórico original/DOU e controle de alterações posteriores nos quatro diplomas modificados, revisão humana dos 44 blocos e 60 subunidades antes extraídas, integração LGPD/LAI, comparação federativa e DEC-016. **PRÓXIMO:** F1-F inventário de incisos/parágrafos por artigo restante, matriz de destino das leis alteradas, posição no Livro, exceções e interface jurídica com T07, mantendo Q jurídico.
