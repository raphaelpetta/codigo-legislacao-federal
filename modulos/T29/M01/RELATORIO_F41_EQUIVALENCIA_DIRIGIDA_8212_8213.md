# T29.M01 — F4-1: auditoria dirigida de equivalência das Leis 8.212 e 8.213

**Corte:** 14/10/2026. **Natureza:** análise jurídica de correspondência **preliminar**, sem prova de identidade literal integral ou efeitos iguais por todo o período histórico. [Issue #40](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/40) · [PR #41 draft](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/41) · branch `modulo/T29-M01-segurados-dependentes-f0-f1-20261014`. **Dono do recorte:** T29.M01. **Módulos externos M02/M03/M05/M06/M07/T01 NÃO editados**. Não houve aprovação C0/C1/M, texto de artigo CLF, fusão, renumeração legislativa nem alteração na `main`.

## 1. Problema e base de legalidade

O art. 13, §§1º–2º, III, da [LC 95/1998 compilada](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp95compilado.htm) exige preservação de conteúdo e alcance na consolidação e permite **fusão de disposições repetitivas ou de valor normativo idêntico**. **Texto semelhante não basta**, porque normas têm destinatários, consequências e vigências distintos. Além disso, um Código único é objetivo de governança (DEC-001), mas seu **veículo/especie legislativa DEC-016** ainda não foi decidido.

Foram comparados **32 pares/interações de unidades** com o texto compilado oficial da [Lei 8.213/1991](https://www.planalto.gov.br/ccivil_03/leis/l8213compilado.htm) e da [Lei 8.212/1991](https://www.planalto.gov.br/ccivil_03/leis/l8212compilado.htm), em consulta dirigida de artigos, incisos, parágrafos, fontes de alteração pontuais e efeitos. **Não houve transcrição integral e automatizada dos 32 pares, nem confronto com todas as edições do DOU e precedentes por inciso.** A matriz registra **o que foi observado**, ressalva interpretativa, invariantes e módulo titular; a auditoria literal C0 completa será etapa posterior.

**Artefato principal:** [F41_COTEJO_32_UNIDADES_8213_8212.csv](F41_COTEJO_32_UNIDADES_8213_8212.csv), com fontes oficiais por entrada e categorias explicativas. **Candidato C1 não é C1 aprovado**. O repositório conserva [F4-0 com alternativas A/B](RELATORIO_F40_OPCOES_A_B_NAO_REGRESSAO_E_DECISAO_PENDENTE.md) e as [51 hipóteses de não regressão](F2C_REGRESSAO_47_CENARIOS.csv), acrescidas das [4 de 2026](F2C_TESTES_ADICIONAIS_COLISAO_2026.csv), **não reexecutadas como testes de texto que ainda não existe**.

## 2. Resultados por recorte legal

### A. Correspondências de enquadramento — promissoras, condicionadas

O **art. 11, I, a/b, e II da Lei 8.213** acompanha os correspondentes **art. 12, I, a/b, e II da Lei 8.212** quanto a trabalho subordinado, trabalho temporário e doméstico. Também são muito próximos os dispositivos de contribuinte individual eventual/por conta própria (V, g/h), definição de economia familiar (§1º), múltiplas atividades remuneradas (§2º), dirigente sindical (§4º da 8213/§5º da 8212), ministros/secretários sem vínculo efetivo (§5º/§6º) e participação rural ativa dos familiares (§6º/§7º).

**Resultado:** para essas entradas, a F4-1 permite hipótese **`C1_POTENCIAL_SEM_CERTIFICACAO`**, nunca identidade jurídico-tributária declarada. Mesmo quando a classificação de segurado obrigatório coincide, a Lei 8.212 define **deveres de recolhimento** em seu [art. 30](https://www.planalto.gov.br/ccivil_03/leis/l8212compilado.htm), com titulares distintos, enquanto a Lei 8.213 descreve benefícios e qualidade. Um conceito nuclear de M01 não pode transferir responsabilidade contributiva nem apagar requisitos prestacionais.

### B. Segurado especial — assimetria, remissões e risco material

- **Lei 8.213 art. 11, VII caput x Lei 8.212 art. 12, VII caput:** a redação de custeio usa a qualificação de auxílio eventual **a título de mútua colaboração**; a do plano de benefícios, no trecho examinado, limita-se a auxílio eventual de terceiros. Isso demonstra **diferença literal**, mas **não é prova suficiente** de que os tribunais lhes atribuam alcances materiais diferentes. Q até análise jurisprudencial e de redações originárias.
- **Art. 11, V, a da 8213 x art. 12, V, a da 8212:** suporte fático próximo para contribuinte individual rural, mas a referência à perda de condição especial aponta, respectivamente, para **§§9º–10 x §§10–11**. Copiar a numeração de um diploma para o outro quebra remissões e pode alterar efeitos.
- **Art. 11, §§7º–10 x art. 12, §§8º–11:** estrutura paralela de contratação eventual, não descaracterização, outras rendas e perda de qualidade especial; contudo, **não foi verificada identidade de todos os incisos**. A [Lei 15.072/2024](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2024/lei/l15072.htm) atualizou em paralelo as cooperativas e deixou vetos específicos; esse histórico precisa de confronto subunidade por subunidade.
- **PSA — assimetria textual comprovada:** o [art. 23 da Lei 14.119/2021](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14119.htm) acrescentou **inciso VIII ao §9º do art. 12 da Lei 8.212**, preservando o enquadramento especial por participação em pagamento por serviços ambientais. Não se localizou espelho literal correspondente no §8º do art. 11 da Lei 8.213. **Não concluir** que a proteção material seja negada na lei de benefícios — o sistema jurídico pode ter efeitos cruzados; esta questão é **Q de interpretação e competência**. Suprimir o inciso VIII do custeio ou inseri-lo automaticamente como norma prestacional seria potencialmente mudança material, não ajuste C1.
- **Participação em microempresa rural:** art. 11, §12 da 8213 x art. 12, §14 da 8212 têm conteúdo semelhante, com parágrafos distintos, limites societários e territoriais a preservar.

**Resultado:** **B (blocos coordenados)** conserva maior margem de segurança documental provisória nesses pontos; **A (núcleo comum)** só pode acolher parte expressamente demonstrada como equivalente, deixando diferenças em módulos de efeitos especializados e Q. Isso **não escolhe a arquitetura B**.

### C. RPPS, segurado facultativo e aposentado ativo

- **8213 art. 12 caput e §§1º–2º x 8212 art. 13 caput e §§1º–2º:** as exclusões do RGPS para servidor efetivo/militar com RPPS e possibilidade de atividade simultânea abrangida pelo RGPS são próximas, com pequenas variações na redação de requisição. Não usar termo “excluído” como proibição geral de qualquer segunda filiação.
- **8213 art. 13 x 8212 art. 14:** ambas usam o corte de **maior de 14 anos**, mas a Lei 8.212 remete expressamente ao art. 21 para contribuição. O [Decreto 3.048/1999, art. 11](https://www.planalto.gov.br/ccivil_03/decreto/d3048compilado.htm) emprega **maior de dezesseis**. A F4-1 documenta a discrepância legal/regulamentar **sem resolver sua validade em todos os casos**, que requer exame constitucional, temporal e jurisprudencial.
- **8213 art. 11 §3º x 8212 art. 12 §4º:** o aposentado que exerce nova atividade é segurado obrigatório em ambas, mas as remissões a contribuições não são literalmente iguais. Não inferir extensão de direitos a novas prestações só porque existe novo dever de contribuição.

### D. Mandatário eletivo — proibição de consolidação ahistórica

A **alínea h de 1997** do art. 12, I, da Lei 8.212 teve sua execução **suspensa pela [Resolução do Senado nº 26/2005](https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2005/congresso/ressf26-05.htm)** em razão do RE 351.717/PR. A **Lei 10.887/2004** incluiu a **alínea j** de ambas as leis; a [tese do STF no Tema 691, RE 626.837](https://portal.stf.jus.br/jurisprudenciaRepercussao/verAndamentoProcesso.asp?classeProcesso=RE&incidente=3916429&numeroProcesso=626837&numeroTema=691) delimita a incidência da contribuição sobre agentes políticos não vinculados a RPPS **após essa lei**. Não apagar a versão histórica h, não fundir h/j como uma única regra de vigência desde 1997 e não convalidar exações anteriores por nova redação editorial.

### E. Qualidade, inscrição, dependência e custeio não são pares equivalentes

- **8213 art. 15 §§1º–4º** mantém qualidade sem contribuição atual, com períodos e termo de perda vinculados aos prazos de recolhimento; **8212 art. 30** regula dever, responsável e vencimento das contribuições. Relação **funcional e temporal**, não duplicação normativa. A prova do desemprego deve conservar [STJ Tema 1.360](https://processo.stj.jus.br/repetitivos/temas_repetitivos/pesquisa.jsp?cod_tema_final=1360&cod_tema_inicial=1360&novaConsulta=true&tipo_pesquisa=T).
- **8213 art. 17** trata da inscrição e documentação; não é espelho do art. 30 da 8212. O cadastro não cria necessariamente a filiação obrigatória pelo trabalho nem substitui a distinção de devedor empregado/empresa/CI.
- **8213 art. 16** descreve dependentes; **8212 art. 12** classifica segurados para custeio. Não há identidade de categoria jurídico-familiar com contribuinte.

## 3. Painel de estados do recorte dirigido

| Categoria documental | Número aproximado de entradas | O que significa |
|---|---:|---|
| `C1_POTENCIAL_SEM_CERTIFICACAO` | **12** | Correspondência segmental indicada, faltando prova de identidade literal, valor normativo e efeitos |
| `SEM_EQUIVALENCIA` / `INTERFACE_NAO_C1` | **4** | Não há duplicação da mesma regra: papéis, dependência, prazo, cadastro e custeio diferentes |
| Demais **Q sobre redação, remissões, vigência e efeitos** | **16** | Casos que exigem confronto específico e manifestação de titulares |
| **Total do recorte** | **32** | **32 unidades/pares selecionados**; não é inventário integral dos artigos nem 32 identidades normativas |

**Não basta ser candidato para ser C1.** Nenhuma das 12 correspondências foi submetida a cotejo literal artigo-local com hashes, histórico completo ou prova externa independente, e **nenhuma está aprovada para fusão**. O número de Q é de **registros de comparação**, não quantidade final de problemas constitucionais ou de leis conflitantes.

## 4. Encaminhamento intermodular (sem decisão unilateral)

[F41_PEDIDOS_VALIDACAO_INTERMODULAR_10.csv](F41_PEDIDOS_VALIDACAO_INTERMODULAR_10.csv) lista **dez questões concretas**, com responsáveis propostos, fontes e prova que falta. Prioridade elevada: PSA e exceções rural/cooperativa (**M02**), carência e direitos dos dependentes (**M05/M06**), posição do facultativo 14/16 (**M01/M02/T01**), suspensão h/mandato j (**T01/M02**), prazo de graça e vencimentos (**M02/M06**) e relação definição-empresa (**M02**). Nenhuma mudança em arquivo externo foi executada.

**Recomendação de método para F4-2:** escolher um conjunto mínimo de **seis candidatos textualmente promissores** (empregado art.11 I a/b, doméstico II, economia familiar §1, concomitante §2, dirigente sindical §4) e verificar **texto literal dos dois diplomas por unidade em versões vigentes/históricas**, com diferenças caractere a caractere, fontes originárias/alteradoras e efeitos. Resolver primeiro pelo inventário C0 antes de sugerir C1. Em paralelo, requerer análise dos dez pontos de Q por módulo, sem assumir consentimento do titular.

## 5. FEITO / PENDENTE / PRÓXIMO

**FEITO:** consulta ao texto oficial compilado de 8212 e 8213, Decreto3048, LC95, leis alteradoras 14.119/2021 e 15.072/2024, ResSen26/2005 e Tema691; **32 comparações dirigidas**, classificadas com 20 invariantes já definidas na F2-C e separação de responsabilidade; **10 questões para validação especializada**. Texto jurídico documentado na branch.

**PENDENTE:** cotejo literal exaustivo e DOU/versões por subunidade; validação de efeitos das 12 candidatas; jurisprudência para as diferenças possíveis do segurado especial; M02/M05/M06/T01 não se manifestaram; avaliação temporal da guarda/STF Tema1271 e conflito art73-A pertencem a interfaces, não foram resolvidos; F1 geral ainda parcial, F2-D adversarial e F6 não concluídas; SUIBE sem bytes XLSX e minuta LAI **não protocolada**, não há prova de economia causal.

**PRÓXIMO — F4-2 dirigida:** transcrição e comparação **caractere a caractere** de seis correspondências promissoras, com mapa de exceções e das datas de texto, destinando cada caso a `IDENTIDADE_COMPROVADA_NO_TEXTO`, `SEMELHANCA_NAO_IDENTICA` ou `Q`; confirmação de identidade **material** exige ainda efeito e titularidade, não apenas igualdade de texto. Só depois decidir opção A/B ou propor versões F5, com DEC-016 e governança central.

**Status:** F4-1 recorte dirigido documentado, **nenhuma C0/C1/M ratificada**, sem fusão ou redação de Código. PR draft e `main` intocada.
