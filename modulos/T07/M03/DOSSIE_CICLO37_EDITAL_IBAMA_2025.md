# T07.M03 — Ciclo 37: edital IBAMA de 28/03/2025, publicação ≠ ciência comprovada
**Corte:** 14/10/2026. **PR #39 draft.** Novo caso administrativo real pós-2019, inserido no **período P5** do [mapa de seis regimes de comunicação ambiental](MATRIZ_CICLO35_SEIS_PERIODOS_AMBIENTAL_2008_2026.csv). O caso não é acórdão do STJ, decisão administrativa definitiva ou prova automática de intimação válida.

## Documento oficial localizado
O índice do **Diário Oficial da União de 28/03/2025, Seção 3, p. 109**, contém o **Edital de Notificação nº 1/2025 – DIPRO**, processo editorial do IBAMA **02001.006658/2025-15**, emanado do Centro Nacional do Processo Sancionador Ambiental (Cenpsa). [Endereço de consulta ao documento no DOU](https://pesquisa.in.gov.br/imprensa/servlet/INPDFViewer?captchafield=firstAccess&data=28%2F03%2F2025&jornal=530&pagina=109), identificador eletrônico **05302025032800109**.

**Limite de prova:** a página foi identificada por **indexação do DOU**; a recuperação integral do fac-símile no navegador não foi concluída. Deve haver conferência da imagem/publicação e de eventuais retificações antes da homologação probatória. A identificação não equivale a acesso aos autos administrativos originais.

O edital informa aplicação do **art. 122 do Decreto 6.514/2008** e do **art. 80 da IN Ibama 19/2023**, declaração de que os interessados estão em local incerto ou não sabido **ou** de que tentativas de comunicação pessoal ou postal resultaram infrutíferas. Trata de **alegações finais**, eventual majoração/agravamento e **prazo declarado de dez dias da publicação**, sem que esta pesquisa calcule vencimento. Consta menção à conversão de multa, conforme os requisitos próprios.

## Três processos individualizados (sem dados pessoais)
A [matriz de nove fatos ou lacunas](MATRIZ_CICLO37_EDITAL_IBAMA_2025_PROCESSOS.csv) registra três processos que aparecem na publicação:
- **02047.102185/2017-31**, auto indicado **9172429/E**;
- **02013.000055/2022-10**, auto grafado na indexação em caracteres espaçados, exigindo confirmação do número diretamente na publicação;
- **02048.101638/2017-01**, auto indicado **9120812/E**.

Não foram reproduzidos nomes de autuados, CPFs ou CNPJs; os números processuais são suficientes para o controle documental.

## Distinção entre declaração oficial, fato material e validade
1. **Comprovado na fonte indexada:** a publicação do edital com data, base indicada, prazo declarado e identificação dos três processos; fonte original ainda precisa de cotejo do fac-símile.
2. **Apenas declarado pela própria autoridade emissora:** que os interessados se encontravam em lugar incerto ou que tentativas pessoal/postal haviam falhado. A expressão é **alternativa**, não se pode imputar a todos os três processos a mesma causa sem analisar cada auto/AR/certidão.
3. **Não comprovado nesta pesquisa:** datas e provas das tentativas anteriores, AR devolvido, diligências de endereço, consulta ou acesso ao processo eletrônico, apresentação de alegações finais, efetivo prejuízo, decisão administrativa e data juridicamente eficaz de ciência.
4. **Enquadramento temporal:** edital publicado em março de 2025 → período **P5** (art. 122, §§1º–2º, com remissão ao art. 96 §4º após alteração do Decreto 12.189/2024). Não transportar automaticamente a tolerância a edital prevista no antigo procedimento de 2008–2019 do **STJ Tema 1.329**. Verificar ainda as garantias de comunicação da [Instrução Normativa Ibama 19/2023](https://www.ibama.gov.br/component/legislacao/?legislacao=139335&view=legislacao) e Lei 9.784/1999 art. 26, sobretudo ciência e exigência de fundamento para publicação editalícia.

## Resultado para interface X2/X6
**T43/X2 (prova):** campos `tipo_evento`, `canal`, `publicacao_dou`, `id_edital`, `tentativa_postal`, `resultado_AR`, `endereco_consultado`, `acesso_eletronico` e `documento_certidao` só podem ser preenchidos com o que existe e sob proteção de dados; **um campo de prova ausente não pode receber timestamp fictício**.

**T07/X6 (efeito jurídico):** examinar redação aplicável, pressupostos da intimação editalícia, identidade/domicílio, ciência e eventuais prejuízos. Não permitir que `PUBLICADO_DOU=SIM` se converta por lógica de sistema em `CIENCIA_REGULAR=SIM` sem o pressuposto legal ou a prova concreta. De igual modo, falta de AR na pesquisa externa **não prova** que jamais houve tentativa válida — justifica diligência.

**FEITO:** primeiro edital real **pós-2024** vinculado a três processos individualizados, data e base normativa indicadas, nove eventos probatórios com qualidade/lacunas e [teste estrutural](../../../scripts/validar_t07_ciclo37_edital_2025.py). **PENDENTE:** fac-símile do DOU, autos administrativos e ARs/certidões, interpretação da IN vigente, contraditório individual e eventuais processos judiciais, coordenação T10/T43 e DEC-016. **PRÓXIMO:** obter pelo menos um dos autos administrativos com a cadeia documental que precede o edital e, se possível, manifestação/decisão posterior, para avaliar **regularidade e consequência**, não somente existência do aviso.
