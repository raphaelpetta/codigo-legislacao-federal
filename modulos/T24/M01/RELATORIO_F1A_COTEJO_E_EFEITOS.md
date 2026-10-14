# T24.M01 — F1-A: relatório de cotejo e matriz de efeitos jurídicos

**Rodada:** 02 · **Data de corte:** 14/10/2026 · **Escopo:** arts. 1º–20 (20 artigos) e 42–69 (28 artigos) do CPC.  
**Produto:** triagem dispositivo a dispositivo com duas matrizes ([48 artigos](F1A_MATRIZ_48_ARTIGOS.csv) + [98 unidades subordinadas](F1A_SUBUNIDADES_01-20_42-69.csv)); leitura direta dos textos oficiais original e atualizado. **Não constitui inventário exaustivo da cadeia histórica nem concordância textual para efeito de C0.**  
**Baseline:** CLF `main` `16fba172c875c7a0de388288fe70005c944021d6`. Branch exclusiva T24.M01. Não altera a arquitetura central.

## 1. Fontes cotejadas e método

- **Publicação original da Lei 13.105/2015**, Câmara dos Deputados (texto da lei publicado em 17/03/2015), arts. 1º–20 e 42–69, inclusive incisos e parágrafos: https://www2.camara.leg.br/legin/fed/lei/2015/lei-13105-16-marco-2015-780273-publicacaooriginal-146341-pl.html
- **Texto atualizado da Lei 13.105/2015**, Câmara dos Deputados, mesmos recortes, consultado em 14/10/2026: https://www2.camara.leg.br/legin/fed/lei/2015/lei-13105-16-marco-2015-780273-normaatualizada-pl.html
- **Planalto**, CPC compilado, conferência cruzada seletiva: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105compilada.htm
- **Leis alteradoras**: Lei 13.256/2016 (art. 12), https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2016/lei/l13256.htm ; Lei 13.894/2019 (art. 53), https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2019/lei/l13894.htm ; Lei 14.879/2024 (art. 63), https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2024/lei/l14879.htm
- **STF:** notícia institucional de decisão conjunta das ADIs 5.492 e 5.737 (04/05/2023), https://portal.stf.jus.br/noticias/verNoticiaDetalhe.asp?idConteudo=506742&ori=1 ; páginas de andamento ADIs 6.792 e 7.055 (julgamento de 22/05/2024), https://portal.stf.jus.br/processos/listarProcessos.asp?classe=ADI&numeroProcesso=6792 e https://portal.stf.jus.br/processos/listarProcessos.asp?classe=ADI&numeroProcesso=7055
- **STJ:** CC 206.933/SP, Segunda Seção, Rel. Nancy Andrighi, julgado em 06/02/2025, DJEN 13/02/2025; resumo em Informativo 842: https://processo.stj.jus.br/jurisprudencia/externo/informativo/?acao=pesquisarumaedicao&from=feed&livre=0842.cod.

**Método:** leitura comparada manual artigo a artigo no HTML de dois estados editoriais (original/compilado). Os registros de subunidades distinguem as quatro alterações textuais expressas localizadas; as demais foram registradas como **sem alteração sinalizada nesta triagem**, não como equivalência semanticamente certificada, e não houve extração automática/normalização criptográfica de textos. As matrizes mapeiam função, **não cópia literal do dispositivo**.

## 2. Resultado quantitativo documental

| Medida | Total | Limite |
|---|---:|---|
| Artigos de escopo verificados em publicações original e atualizada | **48** | Aferição documental, não interpretação exaustiva |
| Arts. 1º–20 | 20 | Outros dispositivos de tutelas especiais não incluídos |
| Arts. 42–69 | 28 | Arts. 21–41 serão objeto da interface T23 |
| Subunidades discriminadas (parágrafos, incisos e alíneas selecionados) | **98** | Caputs comuns estão nas 48 linhas-base; não há transcrição integral literal |
| Artigos com modificação textual explícita localizada | **3**: 12, 53 e 63 | Quatro mudanças individuais, conforme abaixo |
| Interpretações constitucionais selecionadas | 3 pontos: art. 46 §5º; art. 52 parágrafo único; art. 53 | Não são alterações na redação do Código |
| Minutas CLF ou revogações geradas | 0 | Nenhuma deliberação substantiva |

**Advertência:** a ausência de indicação de alteração nos demais artigos não prova ausência de ato modificativo não sinalizado na versão consolidada; a conferência da cadeia histórica das leis alteradoras e de decisões de controle concentrado é uma porta independente.

## 3. Alterações textuais com cadeia verificável

### (A) Art. 12, caput — Lei 13.256/2016

- **Promulgação original 2015:** ordem cronológica expressa como dever estrito dos juízes e tribunais.
- **Edição modificada antes da eficácia do CPC:** art. 2º da Lei 13.256/2016 introduziu o atendimento **preferencial** à ordem de conclusão; a lei modificadora dispôs expressamente, art. 4º, que entraria em vigor junto com o CPC.
- **Classificação:** **modificação legislativa expressa antes da vigência da lei-base**, e não sucessão de dois regimes processuais aplicáveis.
- **Destinação preliminar:** T24.M02 (gestão do fluxo/atos), com remissão a T24.M01/T06. Cuidado para não reproduzir o comando original mais rígido como vigente.

### (B) Art. 53, I, d — Lei 13.894/2019

- **Original 2015:** não havia alínea d no inciso I.
- **Em 2019:** incluída competência do foro do domicílio da vítima de violência doméstica e familiar, nos termos da Lei 11.340/2006.
- **Regime especial sistêmico:** a mesma lei também alterou a Lei Maria da Penha, o CPC art. 698 (intervenção do MP) e o art. 1.048 (prioridade processual). Não desmembrar a proteção territorial de suas outras garantias no inventário futuro.
- **Destinação preliminar:** T24.M01, interfaces T17, T32 e T24.M06; efeitos protetivos precisam de teste para não sofrer regressão em eventual formulação geral.

### (C) Art. 63, §1º e §5º — Lei 14.879/2024

- **Original 2015, §1º:** forma escrita e referência a determinado negócio jurídico.
- **Redação vigente, §1º:** requisitos anteriores acrescidos da pertinência entre foro, domicílio/residência de uma das partes ou local da obrigação, preservada eleição mais favorável ao consumidor.
- **§5º novo:** demanda em juízo aleatório qualificada como prática abusiva que autoriza declinação de ofício.
- **Art. 2º da lei alteradora:** eficácia a partir da publicação, no **DOU de 05/06/2024**, embora a lei tenha sido datada de 04/06/2024.
- **STJ, CC 206.933/SP:** aplica-se o novo regime às demandas ajuizadas **após 04/06/2024** e afasta-se sua aplicação às anteriores. A fórmula do STJ coincide operacionalmente com a publicação em 05/06/2024; é necessário reproduzir o marco literal dos acórdãos e o marco documental do DOU **sem dizer equivocadamente que a publicação ocorreu em 04/06**. Não atribuir efeito retroativo à regra nova.
- **Súmula 33/STJ:** permanece relevante fora das hipóteses legais específicas e para ações anteriores, conforme a tese da Segunda Seção; registrar **superação parcial, não revogação geral**.
- **Destinação preliminar:** T24.M01, interface T20 (consumidor), T01 (intertemporalidade), T23 (foro internacional sob CPC art. 25).

## 4. Três interpretações constitucionais que mudam a aplicação sem mudar palavras

### 4.1 Art. 46, §5º — competência na execução fiscal

STF, **ADIs 5.492/5.737**: interpretação conforme para restringir competência territorial em demandas de execução fiscal envolvendo entes subnacionais, considerada a abrangência territorial do ente competente e a localização do fato gerador. A notícia institucional de 04/05/2023 relata a maioria, mas **não foi conferido o dispositivo integral do acórdão** nem eventual modulação.

**Auditoria:** texto do CPC pode ser comparado e até parecer inalterado, mas **um possível C0 sem ressalva de interpretação conforme falsearia o alcance vigente**. Guardar o vínculo STF e o regime especial T12/T24.M05.

### 4.2 Art. 52, parágrafo único — demandas contra Estados/DF

STF, **ADIs 5.492/5.737**: interpretação conforme restringe a opção pelo domicílio do autor aos limites territoriais do ente estadual/distrital demandado, conforme notícia institucional. **Não equiparar indiscriminadamente a posição processual dos Estados/DF à da União no art. 51**.

**Auditoria:** constitucionalidade federativa e autonomia territorial (T03/T06), com ressalva da necessidade de verificar o inteiro teor e exceções.

### 4.3 Art. 53 — assédio judicial contra imprensa

STF, **ADIs 6.792/7.055**, julgamento de 22/05/2024: havendo demandas sobre os mesmos fatos distribuídas em comarcas diversas com intuito notório de prejudicar defesa de jornalistas ou órgãos de imprensa, interpretação conforme exige reunião no foro do domicílio do réu. Não confundir proteção **específica contra assédio judicial à liberdade de expressão** com derrogação universal de todo foro à escolha do autor.

**Auditoria:** art. 53 e remissões T02/T24.M01; integrar art. 55 (conexão), art. 59 (prevenção), art. 69 (cooperação) e garantias de expressão da CF. A interpretação judicial não equivale a supressão da competência protetiva do art. 53, I, d. Examinar razões e limites no inteiro teor.

## 5. Modelo funcional e interfaces — primeira proposta não ratificada

| Recorte CPC | Destinação preliminar | Por quê |
|---|---|---|
| Arts. 1º–11 | T24.M01, com referências a T01/T06/T24.M04/M07 | Estrutura das garantias comuns de todos os sujeitos |
| Art. 12 | T24.M02 | Ordem e gerenciamento de julgamentos |
| Arts. 13–15 | T23 (13), T01 (14–15), interface com T24 | Normas de aplicação no espaço e no tempo, e subsidiariedade |
| Arts. 16–20 | T24.M01 | Jurisdição, legitimidade e ações declarativas |
| Arts. 21–41 (fora da F1-A) | T23 com interface T24.M01/T06 | Limites de jurisdição nacional e cooperação internacional |
| Arts. 42–66 | T24.M01 (remissões por regime especial) | Competência e conflitos |
| Arts. 67–69 | T24.M01, com interfaces T24.M02/M03/M05/T19 | Cooperação nacional e atos concertados |

**Dúvida sistêmica relevante:** a estrutura do CLF prevê um único local primário para cada disposição; portanto a colocação de **art. 13 em T23 e arts. 14–15 em T01** é proposta de trabalho, não determinação automática. O T01 pode preferir ter regras gerais de aplicação em T01, com regime internacional em T23; decidir após leitura cruzada do T01.M01/M04 e inventário do T23. Não duplicar artigos.

## 6. Questões classificadas Q — revisão adversarial

**Q-1.** Relação dos arts. 43 e 63 no tempo: competência fixada na distribuição, modificação por foro e ação em ajuizamento anterior. Evitar aplicação retroativa da §5º de 2024.

**Q-2.** Art. 53 e assédio judicial: comandos protetivos para vítima, consumidor, idoso e titular de liberdade de expressão podem conflitar em situações específicas; verificar critérios de solução sem simplesmente abolir especialidades.

**Q-3.** Cooperação judicial (arts. 67–69): atos concertados não autorizam deslocamento arbitrário de competência, supressão de contraditório ou redução de direitos de sujeitos vulneráveis.

**Q-4.** Normas art. 14–15: transposição ao T01 pode alterar interação com processos eleitoral, trabalhista e administrativo se remissões/subsidiariedade forem esquecidas.

**Q-5.** Natureza do CPC como lei ordinária federal de alcance nacional e competências de organização judiciária: CNJ e regimentos não se tornam lei ordinária por transposição.

**Q-6.** Controle de compatibilidade constitucional: não substituir notícia institucional do STF por dispositivo do acórdão nem confundir interpretação conforme com declaração de nulidade textual.

## 7. O que já está testado e o que ainda não

- **Testado nesta rodada:** existência e leitura documental dos 48 artigos, discriminação das 98 subunidades especialmente relevantes, localização das quatro alterações em três artigos e rastreio inicial de cinco pontos de jurisprudência (incluindo STJ art. 63).
- **Não testado:** equivalência jurídico-material, normalização literal automatizada, inventário integral da cadeia modificativa no DOU, inteiro teor de todos os acórdãos, jurisprudência posterior a esses julgados, testes intertemporais extensivos, classificação de todos os subdispositivos como C0, comparação constitucional vigente/anteprojeto atual.
- **Consequência:** **F1-A documental avançada; F1 do módulo completo ainda NÃO concluída.** Nenhuma redação legislativa aprovada.

## 8. Próxima investigação executável

**F1-B:** detalhar art. 21–41 (interface internacional T23) e arts. 70–138 (sujeitos e intervenções), começando pelos 70–81 e 98–102. Na interface T24.M01, realizar antes revisão adversarial focal dos cinco pontos de interpretação judicial indicados, lendo o inteiro teor dos julgados relevantes e checando espécies e temporalidade. Entrega: tabela de fonte/origem/destino por subdispositivo, mudanças posteriores e solicitação de decisão de arquitetura para T01/T23/T24.M02.
