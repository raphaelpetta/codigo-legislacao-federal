# CLF — R24: auditoria jurídica por efeito e proveniência (15/10/2026)

**Método:** conferir número, ano, epígrafe, fonte textual, alteração, competência, vigência, alcance e distinção entre **Q, C0-T e C0-J**, amostragem dirigida por risco. Nenhum exame nesta nota homologa C0-J, promulga texto, promove revogação ou resolve DEC-016.

## 1. T23 — LINDB como regra de conexão

O recorte [T23 arts. 8º–9º](../produto/vistas/T23_LINDB_DIREITO_INTERNACIONAL_PRIVADO_ART8_9_PREVIA_Q.md) trata de lei aplicável a bens e obrigações. Há seis unidades, com fonte [Câmara atualizada](https://www2.camara.leg.br/legin/fed/declei/1940-1949/decreto-lei-4657-4-setembro-1942-414605-normaatualizada-pe.html) e [Planalto](https://www.planalto.gov.br/ccivil_03/decreto-lei/del4657compilado.htm). A grafia antiga '**moveis**' e '**constituida**' deve permanecer sinalizada, não normalizada silenciosamente. O caput do art. 9º diverge na acentuação ('**constituírem**' na Câmara atualizada; '**constituirem**' no Planalto). Texto experimental toma a Câmara como base, sem resolver o confronto por presunção editorial; DOU de 1942 e cadeia de alterações exigem cotejo. No art. 8º e art. 9º, normas especiais de direito internacional privado, tratados e regras processuais não são revogadas ou fundidas por inferência.

## 2. T06 — ADI 1.127: três conclusões distintas

O [STF](https://portal.stf.jus.br/peticaoInicial/verPeticaoInicial.asp?base=ADI&numProcesso=1127) declarou inconstitucional a expressão '**qualquer**' do art. 1º, I, da Lei 8.906/1994; julgou **prejudicada** a alegação relativa à expressão 'juizados especiais'; julgou **improcedente** a impugnação ao art. 2º, § 3º. São estados distintos. A vista Q mantém a origem editorial; não autoriza declarar o inciso integralmente invalidado, nem enquadrar todo o Estatuto como C0-J. Modificações de dispositivo vigente, efeitos de decisões posteriores e direitos de postulação direta devem ser examinados antes de formar texto limpo.

## 3. T29 — antídoto contra a lei falsa

Em R18, foi corrigida URL erroneamente atribuída à **Lei 15.108/2025** como se fosse a fonte da **Lei 8.213/1991**. Em R24, fonte primária e epígrafe foram novamente confrontadas com [Câmara atualizada](https://www2.camara.leg.br/legin/fed/lei/1991/lei-8213-24-julho-1991-363650-normaatualizada-pl.html) e [Planalto compilado](https://www.planalto.gov.br/ccivil_03/leis/l8213compilado.htm); a Lei 8.213 é a fonte correta, sem modificar SHA de texto já corrigido. O art. 1º expressa finalidades mais amplas, enquanto o art. 9º, §1º distingue a cobertura do RGPS e exclui o desemprego involuntário, sujeito a diploma específico. Permanecem as etapas de DOU e controle de eficácia.

## 4. T32 — alteração temporal não absorbida artificialmente

A [Lei 15.512, de 22/09/2026, art. 33](https://www2.camara.leg.br/legin/fed/lei/2026/lei-15512-22-setembro-2026-800007-publicacaooriginal-181452-pl.html) introduziu expressamente **natureza** na lista de direitos do art. 4º, caput, do ECA. A vista R23 cobre apenas os arts. 1º–3º; não deve afirmar que o art. 4º de 1990 permanece inalterado. Não equivale à incorporação automática no corpus: DOU, atualizações e efeitos pendentes.

## 5. T16 e T10 — efeito sistemático, não literal isolado

A exclusão de ilicitude do CC art. 188, II não exclui necessariamente o dever de indenizar inocente (art. 929); o art. 930 regula ação regressiva. O art. 927, parágrafo único, contém hipóteses de responsabilidade objetiva. A LAI art. 6º, III mantém proteção de informação sigilosa e pessoal: transparência não implica liberação indiscriminada de dados protegidos pela LGPD ou por sigilos legais.

## 6. CI P0 e DEC-016

No [run R23](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38835749406), o job `runner-smoke`, sem checkout, e o `corpus-r20`, com checkout, falham antes dos steps. A API de checks retornou 6 checks failure, 2 anotações cada, mas o conector disponível não autorizou ler o conteúdo. **Não estabelecer causalidade técnica nem CI verde**. O veículo normativo DEC-016 (espécies, iniciativa, transições e vetos) segue pendente de deliberação. [Matriz de 12 controles](32_R24_AUDITORIA_EFEITO_PROVENIENCIA_MULTIFRENTE.csv).

**FEITO:** 12 decisões de classificação documental, 6 unidades T23, sem alteração das partes juridicamente não homologadas. **PENDENTE:** DOU, decisões judiciais integrais em casos selecionados, runner/annotations e DEC-016. **PRÓXIMO:** priorizar resolução do gate CI, auditoria R3 em T07/T24/T25 e consolidação da pilha de drafts por dependência antes de ampliar títulos mecanicamente.
