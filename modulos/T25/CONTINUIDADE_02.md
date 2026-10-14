# T25 — pacote de continuidade do ciclo 02 (arts. 1º–31)

**Data da rodada e corte de fontes:** 14/10/2026. **Responsável funcional:** frente T25.M01–T25.M02. **Issue:** [#31](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/31) · **PR:** [#32 — rascunho](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/32) · **Branch:** `modulo/T25-parte-geral-f0-f1`.

**Versões conferidas:** CLF `main` na entrada = `e9f05f36f68d48db5b27dd0ea1ffab2e1626cc73`; `main` mudou durante a rodada para `9c84d9cc7e0c729b36b6fba2b81a59adec70f5e5`, conferida em 14/10/2026; comparação revelou **apenas arquivos T07.M03, governança/status e verificador estrutural**, sem arquivos T25 em comum. Branch T25 aberta a partir da versão inicial, sem *rebase* neste ciclo: comparar novamente antes de integrar. Constituição alternativa `main` consultada para rastrear versão = `50b498885e17fa1709e66b0861f40e5387b4f4b0`; **não examinada materialmente** nem houve decisão constitucional importada.

## 1. FEITO (na branch, não na main)

| Entrega | Referência | Categoria/limites |
|---|---|---|
| Indexação do CP, arts.1º–12, com 39 subunidades identificadas | `INVENTARIO_ART1_12_UNIDADES_02.csv` | Parafraseada por unidade; NÃO espelho C0-T ou equivalência C0-J |
| Indexação do CP, arts.13–31, com 48 subunidades identificadas | `INVENTARIO_ART13_31_UNIDADES_02.csv` | Idem; anotado art.25 PU/Lei 13.964/2019 |
| Conferência sintática/dados | 87 IDs únicos, artigos 1º–31 (31/31) sem lacunas de numeração | Não significa exaustividade material; subunidades identificadas na versão Câmara |
| Análise jurídica e comparada de dois módulos, jurisprudência selecionada, 7 fichas Q, 12 testes adversariais | `DOSSIE_02_ART1_31_DIAGNOSTICO_E_TESTES.md` | F2/F3 **parciais**, sem decisão de reforma M nem minuta |
| Atualização do índice modular com links e estado | `README.md` | Documento de gestão e pesquisa |

**Fonte principal efetivamente examinada:** texto da Câmara do DL 2.848/1940, arts.1º–31 e notas de alterações, em 14/10/2026: https://www2.camara.leg.br/legin/fed/declei/1940-1949/decreto-lei-2848-7-dezembro-1940-412868-normaatualizada-pe.html . **Original de reforma:** https://www2.camara.leg.br/legin/fed/lei/1980-1987/lei-7209-11-julho-1984-356852-publicacaooriginal-1-pl.html , examinado parcialmente.

**Jurisprudência realmente consultada:** STF Súmulas 611/711, STJ Súmulas 501/567; decisão da ADPF 779 (01/08/2023), além da fonte institucional correspondente. Limites: enunciados e dispositivo, não todos os votos e paradigmas. **Comparado:** StGB §§1–2, 8–9, 13 (tradução com última alteração até 07/11/2024) e CP Espanha arts.1–11 e 14 (texto consolidado informativo atualizado em 09/04/2026). **Não houve comprovação de consenso doutrinário ou dados empíricos.**

## 2. PENDENTE / NÃO VERIFICADO

- Cotejo textual *literal*, histórico original completo de cada dispositivo, efeitos intertemporais de cada alteração, ressalvas de promulgação/vetos, leis especiais e tratados relevantes. A cobertura é de **índice descritivo**, não equivalência `C0-J`.
- Qualificação e eventual necessidade de reforma material em extraterritorialidade, lei temporária, imputação objetiva, culpa/dolo eventual, art.25 PU, preparação e imputabilidade; todas Q.
- Examinar limites do enunciado STJ 501, impactos da ADPF 779, competência do juízo da execução, imposição e reconhecimento de penas estrangeiras, e art. 11 (referência histórica a cruzeiro).
- Completar doutrina e julgados centrais por assunto (STF/STJ; contraditórios), evidência empírica, direito comparado com Portugal/França/América Latina e análise de execução; sem parecer de constitucionalidade abrangente.
- **Veto/revogação:** não há cláusula proposta. **Aplicação temporal:** normas de 1984/2019 e situações anteriores devem ser auditadas antes de qualquer substituição jurídica.
- **Interface CF:** observar CF/1988, principalmente art.5, art.22 e art.228. Nenhuma proposta de reforma constitucional foi avaliada por esta branch.
- **CI no HEAD do último commit:** verificar ao encerrar; teste estrutural não valida mérito jurídico. **Conflito potencial:** novo commit `main` alterou o verificador; PR precisa rodar com versão corrente antes de integração.

## 3. PRÓXIMO PASSO EXECUTÁVEL

**Primeiro:** T25.M01 / issue #31: espelho **literal** de cada uma das 39 subunidades dos arts.1º–12, verificação temporal texto Câmara × redação de 1984 × eventuais mudanças, interpretação STF 611/711, STJ 501, e interações entre legalidade, lei temporária, prescrição e lei especial. **Entrega:** CSV de texto original íntegro, texto de origem com versão, evidência, ressalva, risco Q e destino candidato; dossiê F2 com ao menos três casos reais contextualizados. **Critério de aceitação:** toda unidade identificada com recorte literal e vigência rastreável (ou `A_VERIFICAR`), nenhum artigo sem destino, nenhuma equivalência jurídica presumida.

**Depois:** T25.M02 arts.13–31; decisões sobre quais institutos permanecem na Parte Geral e sobre a possibilidade de redação M, após relatório adversarial. Outros módulos não devem ser editados sem solicitação de integração.

## 4. COORDENAÇÃO

**Interdependências:** T01.M01/M02/M04; T02; T23/T47; T25.M03–M07; T26; T27; T32; T45. **C0:** nenhuma transposição literal concluída; **C1:** nenhuma equivalência; **M:** nenhuma alteração material adotada; **Q:** problemas PROB-T25-0006 a 0012 e anteriores 0001–0005 permanecem hipóteses. **Status CLF:** PR rascunho, `main` não contém entregas T25 nesta rodada.

- [x] Estado da `main` e PRs conferidos antes e durante.
- [x] 87 registros descritivos distintos conferidos; limites documentados.
- [x] Registro de fontes e de efeitos potenciais; sem falsa aprovação material.
- [x] Documentação FEITO/PENDENTE/PRÓXIMO gravada na mesma branch.
- [ ] CI estrutural do HEAD final e comparação da `main` imediatamente antes da integração.

**Regra:** `governanca/18_PROTOCOLO_CONTINUIDADE_POR_RODADA.md`.
