# T25 — pacote de continuidade do ciclo 01

**Data e corte normativo:** 14/10/2026. **Questão:** delimitar Parte Geral penal e mapear fontes, problemas e fronteiras, sem produzir lei nova. **Responsável funcional:** frente especializada T25.M01–M03; coordenação central preservada.

**Versões confirmadas:** CLF main SHA de entrada = `e9f05f36f68d48db5b27dd0ea1ffab2e1626cc73`; main ao checar depois da abertura do PR = `e9f05f36f68d48db5b27dd0ea1ffab2e1626cc73`; branch `modulo/T25-parte-geral-f0-f1`; [issue #31](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/31); [PR #32, rascunho](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/32). **CF proposta main SHA:** não consultado neste ciclo; nenhuma hipótese constitucional nova importada.

## 1. FEITO — entregas verificáveis

| Entrega | Arquivo/estado | Direito de origem, destino e categoria |
|---|---|---|
| Delimitação funcional F0 do T25.M01–03 | `README.md`, branch | Sem transposição normativa; apenas F0 |
| Dossiê crítico e histórico-comparado inicial; cinco hipóteses de problema, sem conclusão material | `DOSSIE_01_PARTE_GERAL_F0_F1.md`, branch | CF art.5 XXXVIII–XLVII, CP 1º–120 (índice por faixas), Lei 7.209/1984, LCP 1º–4, LEP 1º–2, Lei 12.850/2013 art.1, STJ Súmulas 231/545; Q preliminares |
| Inventário F1 **seletivo** de 15 registros de fontes/faixas (não 15 artigos comprovados) | `INVENTARIO_INICIAL_01.csv`, branch | Referências oficiais por faixa, atualizações do art.92 (Lei 15.487/2026) e art.103 (Lei 15.438/2026). `C0/C1/M` não realizados; Q aberto |
| Controle de versão e revisão | [Issue #31](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/31) / [PR #32](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/32) | Não incorporado à `main`; nenhum dispositivo revogado, promulgado ou juridicamente validado |

**Fontes oficiais consultadas (recortes efetivos):**
- https://www4.planalto.gov.br/legislacao/legis-federal/constituicao — amostra CF art.5.
- https://www2.camara.leg.br/legin/fed/declei/1940-1949/decreto-lei-2848-7-dezembro-1940-412868-normaatualizada-pe.html — estrutura da Parte Geral e dispositivos selecionados; não espelho.
- https://www2.camara.leg.br/legin/fed/lei/1980-1987/lei-7209-11-julho-1984-356852-publicacaooriginal-1-pl.html — Lei 7.209/1984, reforma e transição.
- https://www.planalto.gov.br/ccivil_03/decreto-lei/del3688.htm — LCP arts.1–4.
- https://planalto.gov.br/ccivil_03/leis/l7210compilado.htm — LEP arts.1–2.
- https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2013/lei/l12850.htm — lei de crime organizado art.1.
- https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/lei/l15487.htm — alteração do CP art.92 (art.6º da lei).
- https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/lei/l15438.htm — alteração do CP art.103 (art.2º da lei).
- https://processo.stj.jus.br/SCON/sumstj/toc.jsp?sumula=231.num. e https://processo.stj.jus.br/SCON/sumstj/toc.jsp?sumula=545.num. — enunciados, sem estudo de todas as decisões.
- Direito comparado: fontes oficiais Alemanha, Espanha, Portugal e França, listadas com links no dossiê; somente leitura estrutural e amostras de regras.

## 2. PENDENTE / NÃO VERIFICADO

| Ponto | O que falta | Bloqueia |
|---|---|---|
| Cobertura F1 não exaustiva | Espelho CP por artigo/subunidade, alterações, efeitos históricos, identificação de todas leis especiais e reservas de espécie | Aprovação de qualquer proposta C0/C1/M |
| Q: legalidade e densidade dos tipos | Casos-limite; distinguir simplificação de indeterminação | Reforma geral da parte especial |
| Q: omissão, imputação e culpabilidade | STF/STJ e doutrina divergente, alternativas precisas | Minuta T25.M02 |
| Q: individualização e critérios de pena | Auditar as Súmulas 231 e 545, art.59 e seguintes, jurisprudência e dados empíricos | Minuta T25.M03 |
| Q: fronteiras T26/T27 e leis especiais | Concordância e especialidade por dispositivo | Destino final das normas |
| Jurisprudência, história e pesquisa empírica | Não concluída; não classificar hipóteses como fato demonstrado | F3–F4 |
| Integração constitucional | CF/1988 como vigente; atual `main` da CF alternativa não consultada | Apenas decisões dependentes de futura CF |
| Revogação, veto, retroatividade e regras transitórias | Não existe proposta normativa nem equivalência jurídica; riscos ainda não foram testados | Positivação |
| CI/QA no commit final do PR | Conferir execução após esta gravação; testes automáticos não certificam validade jurídica | Integração do PR |

## 3. PRÓXIMO PASSO EXECUTÁVEL

**Tarefa prioritária:** T25.M01–M03 / [issue #31](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/31): inventariar a Parte Geral do CP (arts.1º–120) **por dispositivo e subunidade**, com texto oficial, estado de vigência, cadeia de alterações/ressalvas e risco constitucional. Priorizar arts. 1º–31 no primeiro subciclo verificável, e ampliar até 120 por recortes controlados.

**Insumos:** fonte Câmara atualizada; textos originais e leis modificadoras; CF/1988; precedentes efetivamente analisados; leis especiais identificadas nas dependências.

**Entregáveis:** CSV de inventário artigo-a-artigo com prova e pendência por unidade; dossiê F2 do recorte; diferenças de texto/tempo; nenhum C0-J automático.

**Critério de aceitação:** toda subunidade do recorte terá origem e redação oficial versionada, estado de verificação e risco contextual; discrepâncias não serão ocultadas.

**Fila:** doutrina e casos STF/STJ; Alemanha/Espanha/Portugal/França + América Latina por questão; evidência empírica sobre sanções; arquitetura Parte Geral e, só após F4, minuta classificada.

## 4. Coordenação, controle e proveniência

**Módulos:** T01.M01/M02/M04; T02; T25.M04–M07; T26; T27; e interfaces setoriais conforme incidência. **Constituição:** CF/1988 vigente, CF alternativa condicional; não transmitir como já aprovada. **Decisões materiais ratificadas:** nenhuma neste ciclo. **Estado do CLF:** documentação em PR de rascunho, não na `main`.

**CI:** a verificar no HEAD após a última gravação; nenhuma afirmação de validação automática ou jurídica. **Mudança da main durante a rodada:** nenhuma detectada na checagem anterior a este arquivo; comparar novamente ao integrar.

- [x] Baseline da `main` e PRs correlatos conferidos.
- [x] Fontes e limitações declaradas.
- [x] C0/C1/M/Q diferenciados; não houve norma codificada.
- [x] Pesquisa distinta de redação/aprovação/vigência.
- [x] FEITO / PENDENTE / PRÓXIMO neste pacote.

**Protocolo:** `governanca/18_PROTOCOLO_CONTINUIDADE_POR_RODADA.md`.
