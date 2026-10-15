# Pacote de continuidade — integração central CLF (14/10/2026)

**Responsável:** integração central / revisão metodológica. **Branch:** integracao/diagnostico-central-piloto-t07-20261014. **Base main CLF consultada:** 16fba172c875c7a0de388288fe70005c944021d6. **CF main consultada:** 2a770a8136f8ca4877e865be3e3b7745a6d4b168. **Situação jurídica:** pesquisa e minuta experimental Q, nenhum dispositivo homologado, nenhuma lei revogada. O PR de integração deve permanecer draft até análise. A decisão DEC-016 permanece PENDENTE.

## FEITO

1. Fotografia de cinco PRs substantivos abertos e de suas entregas mais recentes, com rastreio de dono, issue, riscos e dependências em [02_FOTOGRAFIA_CENTRAL_20261014.md](02_FOTOGRAFIA_CENTRAL_20261014.md). Não sumariza as branches como incorporadas à main.
2. Escolha **operacional, não material**, do piloto T07 como próximo núcleo de redação. Cotejadas na documentação da main as 21 unidades dos arts. 1º–2º da Lei 9.784, art. 69 e o protótipo incompleto de 14 cláusulas.
3. Elaborada [minuta conservadora F5-Q](03_PILOTO_T07_PRIMEIRO_NUCLEO_20261014.md), contendo três artigos experimentais de âmbito/princípios/especialidade, correspondência por grupos com 22 origens e doze cenários adversariais propostos.
4. Preservadas as responsabilidades de T07, T43, T24, T25, T29 e T01. Nenhum arquivo setorial dos PRs #32/#38/#39/#41/#43 foi modificado.
5. Fontes consultadas efetivamente: READMEs/handoffs e artefatos de GitHub CLF da main e branches acima; Lei 9.784 em texto já transcrito e citado no repositório; quadro de coordenação CF. **Não houve nova auditoria independente de DOU/fac-símile ou validação de mérito jurídico no presente ciclo.**

## PENDENTE / NÃO VERIFICADO

- Conferir CI, diffs e conflitos dos PRs setoriais no HEAD de eventual merge (não realizado nesta rodada).
- Demonstrar C0-J do primeiro núcleo; a alteração 'desta Lei'→'deste Livro' depende de domínio jurídico e cobertura real, não apenas substituição de caracteres.
- Auditar direito externo (Lei 14.129, LAI, LGPD, LINDB, ritos especiais e CPC art. 15) e os demais 193 registros da Lei 9.784 além dos 22 selecionados, antes de substituir a lei inteira.
- Obter pareceres funcionais T07/T43/T01 e, em seu tempo, decisões expressas do projeto sobre DEC-016, eventual C1/M e instrumento transitório/revogatório.
- Não homogeneizar F2-C/P19 e E15 de T29 nem corregir art. 73-A por opinião editorial. Não integrar a minuta penal A/B nem redigir processo digital universal.
- Reconferir estado exato dos PRs e a main na próxima rodada; esta é fotografia datada.

## PRÓXIMO — um trabalho com aceite verificável

**Responsável:** T07.M03, issue #35, com T43.M04 e T01.M04 como revisores. **Tarefa:** formar a concordância 22/22 em tabela unitária (origem, texto oficial, destino proposto, diferença, âmbito, exceções, vigência, classe C0-T/C0-J/C1/M/Q, prova e revisão), sem recopiá-la como 22 normas aprovadas; aplicar de fato os doze testes apresentados no documento 03, com casos concretos onde exigidos. **Aceite:** nenhum ID órfão, fontes oficiais conferidas, efeitos preservados ou divergências explicitadas, Q sem decisão mantidas, pareceres bilaterais recebidos e gate DEC-016 registrado.

**Segunda tarefa em fila:** após isso, completar o capítulo de direitos, deveres e competência da Lei 9.784 para que a unidade desenvolvida não seja um extrato enganoso de Livro integrado.

## Controle e interfaces

O teste desta rodada é **revisão documental manual**, não execução de suíte de regressão jurídica. A CI eventual do PR verifica integridade estrutural, não autenticidade nem legalidade material. Constituição vigente = parâmetro jurídico A; modernização constitucional = hipótese B separada. O objetivo de um Código único é DEC-001; DEC-016, escolhas de implementação e aprovações C0-J/C1/M seguem abertas.


## ADENDO — rodada 02, 14/10/2026 (mesmo PR #45)

### FEITO
- `05_CONCORDANCIA_T07_22_UNIDADES_20261014.csv`: **22/22** origens com textos e destinos individuais. 15 sem delta local, três mudanças de referente em art. 1º, três ajustes de pontuação nas definições e uma mudança de posição/referente do art. 69. **Nenhuma com C0-J homologado.**
- `06_TESTES_ADVERSARIAIS_EXECUTADOS_T07_12.csv`: **12 hipóteses examinadas documentalmente** e classificadas, das quais 4 passam apenas no recorte (incluindo uma ressalva), 2 condicionais e 6 bloqueadas por regras ausentes do fragmento. Ver `07_RELATORIO_T07_AUDITORIA_22_E_12_TESTES.md` para limites e fontes.
- `08_CONCORDANCIA_T07_SEGUNDO_NUCLEO_16_UNIDADES.csv` e `09_T07_DIREITOS_INTERESSADOS_COMPETENCIA_F5Q.md`: **16 unidades de artigos 3º, 4º, 9º e 11** em quatro artigos experimentais, a partir das 40 unidades existentes na main para arts.3º–17. Nenhuma reforma material ratificada.
- `scripts/validar_integracao_t07_nucleo.py` e workflow de CI específico criados; controle estrutural de ids, origens, destinos, comparações e ausência de homologação. **Consultar execução HEAD da CI antes de afirmar aprovação.**
- Fontes oficiais reconsultadas nesta rodada: Lei 9.784 edição atualizada e publicação original Câmara, Lei 14.129 atualizada Câmara, Súmula 633/STJ e SV 5/STF. A validação automatizada lê o espelho arquivado do GitHub; **não** valida hash de bytes DOU, nem equivalência C0-J.

### PENDENTE
- Reconstruir juridicamente **24/40** unidades remanescentes dos arts.3º–17 e 193 registros fora das 22 unidades do primeiro núcleo, sem tratar os universos como aditivos independentes: os 24 já estão contidos no universo de 193.
- A transposição de 'esta/desta Lei' para 'este/deste Livro' permanece Q; sem Livro integral e direito externo não há prova de mesmo alcance.
- T07 titular e T43/T01 precisam rever processo eletrônico, opção, ciência, prazo, leis especiais e DEC-016. A ausência de advogado em PAD segundo SV5 não extingue direito de assistência, lei especial ou devido processo. A Súmula 633 não torna o CLF nacionalmente cogente.
- Confirmar CI no HEAD. Nenhuma revogação, aprovação jurídica C0-J, C1, M ou fusão/merge de módulos.

### PRÓXIMO
**T07.M03/issue #35:** completar e auditar **os 24 dispositivos restantes dos arts. 3º–17** (5–8, 10, 12–17) com os mesmos campos de concordância, seguidos de testes de devido processo, delegação/avocação e meios de manifestação. Aceite: 40/40 com destino e prova textual, relatório de direitos/competências e bloqueios reais; nenhuma norma original perdida e parecer T43/T01 das interfaces condicionantes. Depois iniciar os blocos de ciência/instrução/recurso e 215/215 sob revisão material antes de qualquer revogação.


## ADENDO — rodada 03, fechamento textual dos arts. 3º–17 (14/10/2026)

### FEITO — arquivo e prova efetivamente produzidos

1. **`10_T07_COMPLEMENTO_24_UNIDADES_F5Q.csv`**: 24 posições de arts. 5–8, 10 e 12–17, ausentes na rodada anterior, com origem, texto, destino, risco, testes e rótulo Q.
2. **`11_T07_CONCORDANCIA_UNIFICADA_40_UNIDADES_F5Q.csv`**: união sem duplicação das 16 posições anteriores + 24 novas; **40/40** posições documentais da Lei 9.784 arts. 3º–17, texto idêntico ao espelho de origem armazenado na main; não certifica histórico integral nem C0-J.
3. **`12_T07_LIVRO_SEQUENCIAL_ARTS1_17_69_F5Q.md`**: **18 artigos experimentais em sequência** com **62 unidades de origem** (21 arts. 1º–2º, 40 arts. 3º–17, 1 art. 69), sem afirmação de revogação. Soluciona editorialmente a antiga numeração salteada no ensaio dos arts. 3º, 4º, 9º e 11; mantém rastreio pelo ID.
4. **`13_TESTES_T07_REQUERIMENTOS_CAPACIDADE_COMPETENCIA.csv`**: 16 cenários jurídicos hipotéticos com confronto textual realizado: **10 passagens no recorte, 4 passagens com ressalva e 2 condicionais**. Não são 16 julgamentos reais nem equivalência certificada.
5. **`14_RELATORIO_T07_CRITICO_REQUERIMENTO_CAPACIDADE_COMPETENCIA.md`**: relatório crítico, cotejo da Lei 9.784, Lei 14.129 (arts. 5º–10), Lei 14.063, Lei 13.146 e matéria orgânica. Registra a diferença de competência entre delegação e avocação, e a ocorrência de 'unidade fundacional competente' **em duas transcrições oficiais da Câmara** (original e atualizada). Não revisado fac-símile DOU.
6. **Validador ampliado** `scripts/validar_integracao_t07_nucleo.py` e workflow que acompanha `integracao/**` passaram a exigir 40/40, 62 unidades dentro de 18 artigos, fontes textuais e 16 testes. Conferir CI no HEAD mais recente; resultados de SHAs anteriores não substituem a CI atual.

**Fontes oficiais efetivamente abertas na rodada:** textos atualizado/original da Lei 9.784 na Câmara; Lei 14.129 atualizada; Lei 14.063 atualizada; Lei 13.146/2015 (edição da Câmara) quanto à capacidade civil da pessoa com deficiência. Não foi feita análise de autos individuais ou jurisprudência aprofundada sobre cada instituição, nem cotejo de DOU em imagem.

### PENDENTE / NÃO VERIFICADO

- **Gate jurídico C0-J segue ABERTO** para as 62 unidades. A alteração de referente 'desta Lei'→'deste Livro' exige contexto do Livro completo, condição jurídica de promulgação e sucessão válida; DEC-016 não foi decidida.
- A matriz **40/40 é cobertura apenas dos arts. 3º–17**; os 215 registros textuais do estudo T07 total continuam a ser universo de controle, não aprovados. Ainda faltam todas as disciplinas não abrangidas por arts. 1º–17/69.
- Capacidade administrativa versus civil e atos de criança/adolescente e pessoa com deficiência dependem de regimes especiais (T13/T32). Requerimentos digitais exigem parecer T43. Nenhum modelo novo de assinatura eletrônica, avocação ou delegação foi escolhido.
- Art. 16 'unidade fundacional': original e atualização Câmara coincidem, mas o fac-símile DOU e repercussões jurídicas não foram certificados. Não corrigir editorialmente sem prova.
- Nenhum dispositivo material homologado, nenhuma lei revogada, nenhum PR setorial fundido à main ou mudança na CF proposta nesta rodada.

### PRÓXIMO — tarefa prioritária e critério de conclusão

**Módulo dono:** T07.M03 (issue #35; PR próprio #39), com T43.M04, T01.M04 e T24 conforme as interfaces.

**Atividade única:** auditar e preparar o **bloco de arts. 18–28 da Lei 9.784**, em especial impedimentos/suspeição, forma dos atos, horário/prazos e intimações. Exigir concordância por unidade com fonte atual e versões históricas, casos/precedentes concretos onde pertinentes, meios digitais (Lei 14.129 arts. 6–10/42–43 e Lei 14.063), prova de recebimento/ciência, causas de nulidade e preservação da defesa.

**Aceite verificável:** 100% das unidades dos arts. 18–28 com destino e diferença classificada C0/C1/M/Q, testes de conflitos físico/digital, reserva de competência/forma, direito a vista e contraditório e pacote de continuidade. Q não deve ser convertido em aprovação em caso de falta de prova. **Após esse bloco:** prosseguir com instrução, decisão, recurso e prazos para que o Livro se torne integral, ao invés de repetir textos parciais.

**Coordenação CF–CLF:** a CF/1988 é norma vigente; qualquer versão constitucional futura é cenário independente, DEC-016 não deve ser resolvida por inferência.


## ADENDO — rodada 04, 15/10/2026: impedimentos, suspeição e intimações (arts. 18–28)

### FEITO
- **`15_T07_CONCORDANCIA_ART18_28_33_UNIDADES.csv`**: 33 posições dos arts. 18–28 (4+2+1+1+5+2+2+1+12+2+1), da matriz de 215 unidades da main, com origens, destinos, literalidade, alertas, situações, classificações Q e interfaces; 11 artigos adicionais.
- **`16_T07_LIVRO_SEQUENCIAL_ARTS1_28_69_F5Q_V2.md`**: reordenação **experimental** do recorte completo em 29 artigos `LPA-SEQ2`, reunindo 95 unidades originárias (21 dos arts.1–2 + 40 arts.3–17 + 33 arts.18–28 + art.69). O antigo art. `LPA-SEQ-018` (origem art.69) passa na proposta v2 para `LPA-SEQ2-029`, sem modificação legal ou aprovação de numeração. **120/215 origens seguem fora desta minuta.**
- **`17_T07_TESTES_INTIMACAO_IMPARCIALIDADE_20.csv`**: vinte cenários **hipotéticos e documentais** de imparcialidade, nulidade/sanação, prazos e intimação digital. Doze trechos preservados no recorte, três interfaces condicionais, três lacunas de direito externo, um condicionamento fático e um jurisprudencial. Não são 20 casos administrativos reais.
- **`18_T07_PARECER_CRITICO_IMPARCIALIDADE_INTIMACAO.md`**: análise jurídica de Lei9.784 arts.18–28, 41, 66 e de Lei14.129 arts.42–43, com **três precedentes contextualizados do STJ** (MS7.181/DF, MS21.312/DF e RMS42.193/ES), fontes oficiais e limites de generalização. A jurisprudência mostra tanto a relevância de enfrentar a arguição quanto o exame probatório de suspeição e a consequência de intimação com prazo reduzido em um caso concreto.
- **Validador `scripts/validar_integracao_t07_nucleo.py` ampliado** para exigir 33 posições, 29 artigos, 95 origens, 20 cenários e fonte/destino vinculados. A CI deve ser consultada **no HEAD desta rodada** antes de afirmar sucesso.
- **Fontes efetivamente conferidas:** texto atualizado Câmara da Lei9.784; texto do Planalto da Lei14.129; pesquisas institucionais STJ e informativo 88. **Não** foi obtido fac-símile DOU, conjunto completo de AR/certidões individuais, nem dados empíricos novos.

### PENDENTE / NÃO VERIFICADO
- **C0-J e DEC-016** seguem Q. Cobertura de 95/215 é **somente textual/local**, sem direitos e efeitos completos do Livro e sem regime promulgatório aprovado; nenhum dispositivo de Lei9.784 revogado.
- A relação entre recebimento eletrônico (Lei14.129 art43 II), escolha/desistência do usuário (art42), possibilidade de meio eletrônico mesmo sob lei especial pessoal/postal (art43 III), ciência jurídica e termo inicial do prazo depende de rito/destinatário/prova. **Não** fixar equivalência universal entre `enviado`, `recebido`, `lido`, `ciência válida`.
- Não equiparar art23 (atos em dias úteis) à contagem geral em dias úteis: Lei9.784 art66 §2 prevê contagem contínua. Art26 §2: 3 dias úteis para **comparecimento**, não toda notificação.
- Decisões STJ sobre nulidade e comparecimento são factuais; não inferir nulidade automática do edital Ibama do PR39 nem sanação generalizada.
- Ausentes revisão titular T07/PR39, T43/PR43, T01/DEC016, inventário jurídico dos procedimentos especiais, 120 unidades adicionais, fonte histórica DOU e gate normativo.

### PRÓXIMO (prioridade única e aceite)
**T07.M03/issue #35, com T43.M04 e T01.M04:** auditar dois percursos de comunicação administrativa com prova temporal e causal: **(1)** ato regido por Lei9.784 + Lei14.129, opção/saída eletrônica/recebimento/ciência/defesa; **(2)** processo sancionador especial com destinatário desconhecido ou tentativa postal frustrada (Ibama PR39, quando houver autos), decisão sobre edital e direito de defesa. Para cada percurso, registrar regime, período, competência, fonte da comunicação, prova de entrega, prazo, participação, resultado normativo e `Q`. **Aceite:** duas cronologias com documentos primários ou lacunas expressas e confronto com três julgados. Não concluir nulidade se não houver prova de AR/certidões/caso individual.

**Fila:** redigir arts.29–47 (instrução, prova, participação e acesso) com concordância das próximas posições; transpor todas 215 origens antes de cogitar revogação da Lei9.784 e homologação de um Livro.
