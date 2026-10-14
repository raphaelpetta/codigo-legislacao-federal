# T29.M01 — Pacote de continuidade, rodada 10 (F2-C)

**Data/corte:** 14/10/2026. **Dono:** T29.M01. **Issue:** #40. **PR:** #41 (draft). **Branch:** modulo/T29-M01-segurados-dependentes-f0-f1-20261014. **Baseline main CLF na abertura:** 16fba172c875c7a0de388288fe70005c944021d6. **Parâmetro constitucional:** CF/1988 e EC 103/2019. Constituição alternativa em repositório próprio, não integrada nesta rodada.

## FEITO
- [Esquema F2-C de 15 entidades](F2C_ESQUEMA_CONCEITUAL_15_ENTIDADES.csv): pessoa, regime, atividade, vínculo, filiação, inscrição, qualidade por período, modificadores, contribuição, evento, dependência, prova, prestação e versão de fonte, com proprietário e temporalidade.
- [Concordância funcional de 56 entradas](F2C_CONCORDANCIA_FUNCIONAL_56_REGRAS.csv): 33 regras da F2-A e 23 transições F2-B. A correspondência é **conceitual e preliminar**, não equivalência C0/C1/M.
- [Reavaliação de 47 casos](F2C_AUDITORIA_NAO_REGRESSAO_47_CASOS.csv): 20 da F2-A e 27 da F2-B; 40 passam condicionalmente pelo esquema, 7 retêm questão jurídica aberta. Sem presunção de deferimento real.
- [Relatório F2-C](RELATORIO_F2C_MODELO_UNIFICADO_CONCORDANCIA_E_TESTES.md) com dez invariantes, fronteiras e a estrutura editorial candidata.

**Validação realmente realizada**: 15 entidades, 56 origens de regras/transições, 47 testes; IDs não duplicados, nenhum campo faltante ou referência quebrada; as 15 entidades aparecem na concordância. Os números são controles de integridade, não certificação jurídica.

**Revisão de fontes oficiais**: Lei 8.213/1991, Lei 8.212/1991, Decreto 3.048/1999, STJ Tema 1.360, Tema 21/Súmula 416 e STF ADIs 2.110/2.111; ficha STF Tema 1.271 consultada sem tese final de mérito. Lei 15.108/2025, STJ Tema 732 e MP 1.523/1996 recuperados dos trabalhos anteriores sem nova leitura integral nesta rodada.

## PENDENTE
- F1 por todo dispositivo do módulo segue parcial: índices de 198 unidades não são transcrições jurídicas certificadas.
- A interpretação da idade do facultativo (14 na lei/16 no decreto) continua Q.
- PSA: assimetria Lei 8.212 art. 12 §9 VIII e Lei 8.213 art. 11 §8; efeitos prestacionais e IN RFB 2.110 em 2026 continuam Q.
- Menor sob guarda após EC 103 art. 23 §6: STF Tema 1.271 sem mérito final localizado no corte; manter dependência e direitos temporalmente qualificados.
- Remuneração inferior ao mínimo, carência após nova filiação e efeitos das ADIs 2.110/2.111 exigem interface M02/M05.
- Prova de desemprego: STJ Tema 1.360 não aceita ausência isolada de anotações CNIS/CTPS; outros meios idôneos devem ser aceitos.
- Titularidade de contribuições, benefícios, registro e RPPS pertence respectivamente a M02, M03–M05, M06 e M07: **não alterados**.
- Sem revisão jurídica independente, concordância F6 de artigos, validação CI aprovada, decisão C0/C1/M, merge ou atualização da main. DEC-016 continua pendente.

## PRÓXIMO
**F3-A — estudo comparado crítico.** Comparar modelos de filiação obrigatória/facultativa, proteção durante períodos sem contribuição, cadastro e prova, dependência e repartição de competência entre órgão de custeio e de benefícios. Incluir riscos de transplante para o RGPS, federalismo e CF/1988. Entregar estudo com fontes verificadas e consequências para pelo menos duas opções estruturais, preservando os 47 casos de não regressão.

**Critério de aceite para F4**: pesquisa crítica concluída, alternativas expressas, Q preservadas, concordância original/destino com os módulos donos e decisão central sobre eventuais alterações materiais. Esta frente permanece **PR draft**; a unificação conceitual não significa legislação aprovada.
