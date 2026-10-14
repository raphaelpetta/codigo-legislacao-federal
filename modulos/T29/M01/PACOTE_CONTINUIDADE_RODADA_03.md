# T29.M01 — Continuidade da rodada 03 (F1-B aprofundada)

**Corte:** 14/10/2026 · **Proprietário exclusivo:** T29.M01 — Segurados e dependentes RGPS · **Issue:** [#40](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/40) · **PR:** [#41 draft](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/41).  
**CLF `main` verificada na abertura:** `16fba172c875c7a0de388288fe70005c944021d6`. **Branch:** `modulo/T29-M01-segurados-dependentes-f0-f1-20261014`.  
**Outro dono:** T24.M01 pertence ao PR #38 (outra frente); nenhum arquivo do T24 foi alterado. **CF/1988 com EC 103** constitui direito constitucional vigente, enquanto anteprojeto da CF é separado, não incorporado. SHA da CF independente foi registrado na rodada precedente (`2a770a8136f8ca4877e865be3e3b7745a6d4b168`), **não revalidado nesta rodada**.

## FEITO

| Entrega | Evidência na branch/PR | Alcance jurídico e controle |
|---|---|---|
| Auditoria F1-B focal de **quatro conflitos jurídicos** com fundamento legislativo e judicial | [RELATORIO_F1B_QUATRO_CONFLITOS_E_TEMA_1271.md](RELATORIO_F1B_QUATRO_CONFLITOS_E_TEMA_1271.md) | Distingue normas e precedentes sem aprovar C0/C1/M |
| Cronologia de **19 eventos de legislação, decisão e administração**, divididos em 3 ambientais, 5 idade, 6 guarda e 5 mandato | [F1B_MATRIZ_QUATRO_DIVERGENCIAS.csv](F1B_MATRIZ_QUATRO_DIVERGENCIAS.csv) | Proveniência, data, status, limites, módulo e incertezas explícitas |
| README coordenado com F1-A | [README.md](README.md) | Integração documental interna, não main |
| **Achado novo: STF Tema 1271, RE 1.442.021**, discute especificamente EC 103/2019 art.23 §6º e menor sob guarda | [ficha de andamento oficial do STF](https://portal.stf.jus.br/jurisprudenciaRepercussao/verAndamentoProcesso.asp?classeProcesso=RE&incidente=6661561&numeroProcesso=1442021&numeroTema=1271) | Último andamento relevante visível **16/04/2026**, conclusos ao relator após manifestação da PGR; **mérito não identificado como julgado** no corte; não confundir com ADIs 2021 |
| Assimetria em PSA legalmente comprovada e quadro de 14/16 anos, h/j | [Lei 14.119 art.23](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14119.htm), [8.212 compilada](https://www.planalto.gov.br/ccivil_03/leis/l8212compilado.htm), [8.213 compilada](https://www.planalto.gov.br/ccivil_03/leis/l8213cons.htm), [Decreto 3048](https://www.planalto.gov.br/ccivil_03/decreto/d3048compilado.htm), [Res.Sen 26/2005](https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2005/congresso/ressf26-05.htm) | **Texto positivo/estado formal** distinto de consequência prestacional Q |

**Fontes consultadas efetivamente:** leis compiladas 8.212/8.213 (art.12 §9 VIII e art.11 §8; arts.14/13; arts.12/11 I h/j; art.16 §2º), Lei 14.119/2021 arts.17/23, Lei 15.108/2025 arts.1º/2º, EC 103/2019 art.23 §§4º/6º/7º, ADIs 4878/5083 (ementa/notícia STF), ficha de RG Tema 1271 (movimentos), STF RE 351717 (notícia institucional), Senado Res26/2005 arts.1–2, Decreto 3048 art.11 e art.18 §2, orientação INSS 18/08/2026 sobre facultativo, CF/1988 art.7 XXXIII/EC20/1998. **Decisões judiciais completas, DOU e histórico de medidas provisórias NÃO foram todos auditados.**

## PENDENTE / NÃO VERIFICADO

1. **Tema 1271/STF:** revalidar o mérito antes de produzir qualquer norma CLF; não antecipar decisão de constitucionalidade EC103 §6. Analisar os votos/dispositivos integrais de ADIs 4878/5083, se houve modulação e efeitos em óbitos anteriores; interface T29.M05.
2. **PSA:** buscar julgados e orientação INSS aplicando os arts.12 §9 VIII e art.11 §8; consequência real sobre benefício e custeio e tributação separadas; interface T29.M02/T12/T38.
3. **Facultativo 14/16:** confirmar se há tese judicial controladora específica para adolescente sem trabalho, distinguir aprendiz/atividade ilícita e filiação voluntária. Hierarquia e intertemporalidade da EC20 são Q, não assumir que o decreto atualizou o texto legal.
4. **Mandato eletivo h/j:** conferir completo RE351717 e eventuais efeitos subjetivos sobre o art.11 I h da 8.213; conferir lei 10.887/2004 e contribuições por competência.
5. **198 unidades da F1-A:** permanecem **inventário funcional descritivo** com alguns subgrupos editoriais, **não banco literal certificado de todas unidades positivas da legislação**. Preenchimento original/atual, DOU, veto/retificação/MP e concordância C0-J exigem rodada própria.
6. **Projeto constitucional alternativo:** ainda não cotejado dispositivo por dispositivo nesta frente. Nenhuma escolha M ratificada, nenhuma lei CLF aprovada, revogada ou mesclada à `main`.
7. **CI e revisão adversarial:** consultar estado no último SHA do PR; ausência de verificações não equivale à aprovação.

## PRÓXIMO — atividade prioritária única

**T29.M01 / F1-C:** análise jurídico-temporal das quatro divergências: obter decisões judiciais integrais ou, quando não disponíveis, dispositivo oficial dos **STF ADIs 4878/5083, Tema 1271, RE351717**; jurisprudência sobre facultativo 14–16; atos DOU de 1997, 2004, 2021, 2025; consulta a precedentes administrativos sobre PSA. Criar matriz de **casos e tempo do fato gerador**, com posição fundamentada (`DIREITO_VIGENTE`, `Q` ou `HIPOTESE_M`) e interfaces M02/M05, distinguindo proposta de reforma.

**Critério de aceite:** alegações determinantes provadas por fontes oficiais datadas; decisões de RG com mérito pendente expressamente Q; origem/destino sem omissão; nenhuma fusão automática ou transposição C1/C0 jurídica sem equivalência demonstrada.

**Fila:** F1 texto literal e histórico por subunidade priorizada, F2 modelo completo, F3 comparação internacional e F4 alternativas; só depois F5.

## COORDENAÇÃO / CONTROLE

**Interfaces:** T29.M02 custeio, T29.M03 aposentadoria, M05 pensão, M06 administrativo, M07 regimes próprios, T12 tributação, T28 trabalho, T32 proteção de menores, T38 meio ambiente. Cada um recebe referência, **não alteração unilateral**. DEC-016 sobre veículo de promulgação do Código permanece pendente.

**Teste estrutural a conferir após último commit:** matriz tem 19 registros sem duplicação de chave (questão+data+fonte), quatro eixos com 3/5/6/5 eventos; não comprova estado do processo judicial posterior à data consultada nem equivalência jurídica. Sem texto CLF C0/C1/M.

- [x] Verifiquei `main` e PRs concorrentes no início.
- [x] Separei fonte legal, constitucional, judicial, regulamento e orientação administrativa.
- [x] Registrei quatro Q, FEITO/PENDENTE/PRÓXIMO e proveniência.
- [ ] Certifiquei efeitos jurídico-temporais de todas as fontes no acórdão integral.
- [ ] Validei CI no HEAD final, obtive aprovação ou fiz merge.
