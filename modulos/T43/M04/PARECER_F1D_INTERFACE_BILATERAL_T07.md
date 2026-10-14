# T43.M04 — F1-D: resposta técnica à reconciliação T07.M03 dos 26 campos
**Corte:** 14/10/2026. **T43 PR #43 ↔ T07 PR #39**, ambos abertos em rascunho. O [contrato técnico inicial T07 ciclo28](https://github.com/raphaelpetta/codigo-legislacao-federal/blob/pesquisa/t07-m03-ciclo21-ambito-intimacao-digital-20261014/modulos/T07/M03/CONTRATO_CICLO28_T07_T43.md) recebeu [matriz do ciclo29 com 26 classificações jurídicas](https://github.com/raphaelpetta/codigo-legislacao-federal/blob/pesquisa/t07-m03-ciclo21-ambito-intimacao-digital-20261014/modulos/T07/M03/MATRIZ_CICLO29_BILATERAL_T07_T43_26.csv). Este texto **documenta o exame do módulo técnico**, não formaliza aprovação intermodular, nem muda as condições legais das intimações.

## Base T43 verificada
[Lei 14.129/2021 consolidada Câmara](https://www2.camara.leg.br/legin/fed/lei/2021/lei-14129-29-marco-2021-791203-normaatualizada-pl.html), F1-C de T43 [76 unidades extraídas](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38555902096/artifacts/11889257820), das quais 74 normativas e dois vetos; F1-A validou 16 textos manualmente (arts.2,42,43). A integridade do dado depende de sigilo, segurança, armazenamento arquivístico e LGPD.

## Resposta de T43
**Apoio normativo claro mas não esquema obrigatório exato:** art.43 I meios de provar autoria; II meios de provar emissão e recebimento mesmo sem leitura; IV auditabilidade; V conservação dos dados de envio e recebimento por pelo menos cinco anos. Art.42 caput e §2º opção e saída quando aplicável, art.2 III e §2º condiciona adoção subnacional. Art.8º caput recepção de **ato do interessado** pelo sistema, distinto de recebimento de **intimação pelo cidadão**.

**Oito campos com potencial inovação material:** IDs de evento/processo, hash, timestamps segregados, logs da consulta, identidade do consultante e indisponibilidade. Ainda que úteis, sua imposição por lei requer análise de custo, privacidade, segurança, competência e impacto, em vez de equipará-los automaticamente a termos explícitos da Lei 14.129.

**Quatro campos de efeito jurídico que T43 NÃO deve determinar autonomamente:** `data_ciencia_juridica`, `base_legal_ciencia`, `marco_inicial_prazo`, `prazo_tipo`. Podem constar do sistema somente mediante decisão conforme lei procedimental e regras especiais; T43 pode armazenar o resultado com fundamento, **não fabricar o fundamento a partir do timestamp de envio**.

**Quatorze funções apoiadas no direito existente:** suas traduções em **campos de banco de dados** continuam propostas de engenharia; não são obrigações de schema textualmente promulgadas. São classificadas como origem positiva / operacionalização condicionada e aguardam detalhamento governamental competente.

## Testes de recusa a equivalências indevidas
(1) Timestamp de envio não é ciência; (2) entrega não gera prazo igual em todos os regimes; (3) falta de leitura não descaracteriza por si ferramenta do art.43 II; (4) protocolo de petição do art.8 não é recibo de intimação; (5) art.2 III impede extensão a Estado não aderente; (6) sem consentimento quando requerido não se presume adesão; (7) prazo de retenção mínima de cinco anos trata dos **dados de envio e recebimento** das ferramentas abrangidas, não de toda documentação do processo por cinco anos; (8) gestão de dados deve preservar direito de acesso e sigilo sob LAI/LGPD.

## FEITO / PENDENTE / PRÓXIMO
**FEITO:** resposta técnica documentada à matriz T07 de 26 campos com classificação 14/8/4, apoiada em F1-C verificável de 76 unidades; estados Q. **PENDENTE:** atos de implementação, parecer de espécie/iniciativa DEC-016, citação do histórico DOU, normas LGPD/assinaturas, análise em casos reais e decisão formal R1/R2. **PRÓXIMO:** conferir o caso DTE/SEI/Meu INSS com eventos datados para validar se a interface R2 conserva direitos e prazos; redline de cláusulas X2/X6 e eventual decisão conjunta T01/T07/T43.
