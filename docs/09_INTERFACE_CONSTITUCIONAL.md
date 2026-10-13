# Interface entre o Código da Legislação Federal e o projeto constitucional

**ID:** CLF-INT-001 · **Versão:** 0.1 · **Data:** 13/10/2026  
**Estado:** PROTOCOLO METODOLÓGICO EM USO; decisões normativas e institucionais permanecem pendentes de aprovação

## 1. Finalidade e limites

Integrar metodologicamente dois projetos distintos: (i) o Código da Legislação Federal (CLF) e (ii) a modernização da Constituição brasileira. Preservam-se dois objetos, dois registros de decisões e duas linhas de versionamento. Não se fundem Constituição e legislação infraconstitucional, nem se presume que as propostas de um projeto estejam aprovadas no outro.

Esta interface permite:
- pesquisar e consolidar o direito federal **vigente** segundo a Constituição de 1988;
- identificar, separadamente, adaptações eventualmente necessárias **se** aprovado o anteprojeto constitucional;
- devolver ao projeto constitucional problemas revelados pelo inventário infraconstitucional;
- evitar decisões editoriais que modifiquem competências, direitos, espécies normativas ou situações jurídicas sem deliberação expressa.

**Não cria uma segunda versão completa do Código.** A regra é manter uma base de inventário e concordância única e acrescentar variantes normativas condicionais apenas onde a divergência entre cenários produzir consequências concretas.

## 2. Fontes e proveniência conferidas

**CLF:** repositório privado `raphaelpetta/codigo-legislacao-federal`, ramo `main`, documentação v0.1 de 13/10/2026, especialmente Carta de Arquitetura, Catálogo dos 48 Títulos e 273 módulos candidatos, Registro de Decisões, Protocolo de Trabalho e Status.

**Projeto constitucional:** duas fontes recuperadas da Biblioteca/Projeto do usuário em 13/10/2026:
1. `anteprojeto_constituicao_brasileira_versao_revisao_2026(1).pdf` — anteprojeto v0.1 de 13/10/2026; 13 títulos, 174 artigos permanentes, 18 artigos do ADCT; matriz editorial de 16 questões abertas.
2. `guia_geral_projeto_constitucional_2026(1).md` — guia-mestre de 13/10/2026, inclusive quadro D/P/H/A/V de status e ressalva de independência em relação ao projeto separado de “Brasil alternativo”.

Os nomes acima identificam fontes históricas de pesquisa, **não fontes oficiais do direito vigente**. O projeto constitucional passou a ter repositório próprio, em https://github.com/raphaelpetta/modernizacao-constitucional-brasileira, com implantação inicial incorporada no commit `fa35da0ec5bfec0ae33515c2a48f264c55d3308c` (13/10/2026). Os arquivos `referencias/guia_mestre_constitucional_v0.1.md` e `referencias/anteprojeto_constitucional_v0.1_texto.md` preservam, respectivamente, o guia histórico integral e a transcrição do anteprojeto antigo. O PDF original deverá continuar disponível para conferência de forma e paginação; a transcrição não é versão normativa aprovada. O conteúdo da Constituição futura deve ser referido por commit e IDs estáveis à medida que for elaborado, não por uma numeração histórica imutável.

Não importar premissas de outro projeto independente: MMP, 600 deputados, lista partidária fechada e fórmulas eleitorais específicas não são decisões deste anteprojeto. As hipóteses de parlamentarismo, Conselho da Federação e Tribunal Constitucional separado também permanecem abertas à auditoria. O texto redacional do anteprojeto não equivale a decisão aprovada pelo usuário.

## 3. Três camadas de referência

| Camada | Natureza | Uso permitido |
|---|---|---|
| **A — CF/1988 vigente** | Direito constitucional positivo, sujeito à conferência em fonte oficial e na data do módulo | Inventariar, interpretar e testar validade, competência e espécies normativas do direito hoje vigente |
| **B — Anteprojeto constitucional v0.1** | Hipóteses e diretrizes de Constituição futura, sem eficácia jurídica | Modelar consequências condicionais, detectar incompatibilidades e sugerir reformas; **nunca afirmar vigência** |
| **C — CLF v0.1** | Arquitetura de proposta codificadora, ainda sem textos legislativos integrados | Sistematizar a legislação e produzir propostas C0/C1/M/Q e concordâncias |

Um dispositivo CLF pode ter `texto_base_A` e `variante_condicional_B` vinculada à versão constitucional. A variante B não revoga nem substitui o texto base enquanto não aprovada pelas instâncias competentes do projeto e, em eventual processo político real, pelos órgãos constitucionais aplicáveis.

## 4. Status que não devem ser confundidos

**Constituição (guia-mestre):** `D` = diretriz escolhida; `P` = proposta preferida; `H` = hipótese de redação; `A` = questão aberta; `V` = verificação ainda necessária.

**Código (Carta de Arquitetura):** `C0` = transposição fiel; `C1` = reforma editorial a direito constante; `M` = reforma material; `Q` = questão controvertida.

**Interface:** `IDENTIFICADO` → `AUDITADO` → `PROPOSTO` → `APROVADO_POR_AMBOS` → `INTEGRADO`; `BLOQUEADO` quando houver divergência não resolvida. A matriz inicial registra impactos *identificados*, não auditorias ou aprovações.

Esses status pertencem a dimensões independentes. Uma opção constitucional `D` pode exigir proposta legislativa `M`, e uma `C0` sob CF/1988 pode precisar de adaptação em B. A classificação inicial de um agrupamento temático não substitui a classificação artigo a artigo.

## 5. Procedimento de mão dupla

1. **Ler versões fixadas** das duas fontes de governança e dos textos constitucionais A e B. Indicar versões e data de corte.
2. **Inventariar e reconstruir** o direito vigente conforme A, incluindo dispositivos, espécie normativa, competência e jurisprudência relevante.
3. **Examinar B apenas como cenário condicional:** usar artigos e ADCT propostos, status da respectiva escolha e efeitos potenciais.
4. **Classificar a interface:** (a) compatível sem mudanças; (b) ajuste terminológico; (c) reforma material condicional; (d) conflito de competência/espécie; (e) necessidade transitória; (f) lacuna constitucional a devolver.
5. **Registrar solicitação `IC-AAAA-NNN`** com fonte, motivação, dispositivos CLF e constitucionais, impactos, opções, status, testes e dependências.
6. **Revisão separada:** o chat responsável pelo CLF examina seus dispositivos; o responsável pela Constituição examina os constitucionais. Nenhum aprova escolhas pelo outro.
7. **Integração:** somente propostas aprovadas nos dois projetos alteram os textos de referência respectivos. Atualizar matriz, versão e remissões.
8. **Regressão:** após mudanças em competências, processo legislativo, direitos ou ADCT, reexecutar testes dos módulos atingidos.

O diálogo entre projetos pode ocorrer por notas exportadas ou PRs/commits quando houver repositório constitucional. Não existe sincronização automática entre chats, Biblioteca e GitHub.

## 6. Regras jurídicas não negociáveis na pesquisa

- A CF/1988 continua sendo parâmetro para a legislação brasileira real, inclusive espécie normativa, competências e recepção de normas.
- Uma lei ordinária não absorve automaticamente matérias constitucionalmente reservadas a espécies distintas. **Unidade editorial** não supre os instrumentos juridicamente necessários à positivação.
- O art. 174 do anteprojeto prevê publicação autêntica e lei sobre técnica normativa, **mas não aprova por si só** um Código único, nem define sua espécie ou seu procedimento. Trata-se de agenda de desenho legislativo.
- A recepção de legislação anterior é tratada como hipótese do art. T1 do ADCT proposto. Verificar incompatibilidades materiais, direitos, continuidade institucional e prazos, sem declarar revogações imaginárias.
- Distinguir incompatibilidade constitucional real, conflito possível, reforma politicamente desejável e mudança meramente editorial.
- Na divisão federativa, registrar para cada função: normatização, garantia do resultado, execução, financiamento e fiscalização. Não presumir que legislação editada pela União é necessariamente exclusiva do nível federal.

## 7. Interfaces prioritárias já identificadas no anteprojeto

1. **T01.M03/M04/M05:** arts. 64–66 e 174; T1 e T17 do ADCT. Técnica legislativa, consolidação, processo legislativo, publicação, recepção e legislação de implementação.
2. **T03 e títulos setoriais:** arts. 38–53, sobretudo 44–49; T10–T12 do ADCT. Autonomia local, competências, financiamento e transição.
3. **T04/T05/T11:** arts. 54–74; T3–T6 do ADCT. Eleições, bicameralismo, governo e orçamento, **sob hipóteses ainda abertas**.
4. **T06/T24/T26:** arts. 75–89; T7–T8. Possível reorganização das competências jurisdicionais e transição.
5. **T07–T12/T43:** arts. 90–116; T12. Administração, responsabilização, finanças, tributos, serviços e digitalização.
6. **T29–T35:** arts. 117–133; T13–T15. Saúde, previdência, assistência, educação e garantias financeiras.
7. **T02/T14/T25/T37/T39:** arts. 134–150; T16. Meio ambiente, territórios indígenas, quilombolas, consulta e pluralismo jurídico.
8. **T23/T45–T48:** arts. 151–168; T9. Defesa, polícias, emergência, tratados e relações internacionais.

O inventário inicial verificável dessas interfaces consta de `catalogo/10_MATRIZ_COMPATIBILIDADE_CONSTITUCIONAL.csv`. A tabela é um **mapa de triagem, não prova de cobertura exaustiva**.

## 8. Testes de estresse interprojetos

- Uma regra nacional de saúde impõe encargos aos estados; verificar autoridade normativa, financiamento, execução, tutela e responsabilidade segundo A e B.
- Lei geral do Código altera receitas estaduais; testar competência e participação do Conselho da Federação **somente no cenário B e se seu desenho for aprovado**.
- Processo penal em andamento muda de órgão constitucional competente; testar preservação de atos, foro, garantias e transição judicial.
- Município reorganizado mantém serviços essenciais e obrigações anteriores; testar sucessão e transição fiscal.
- Regime territorial indígena passa a domínio coletivo especial; conferir titularidade, direitos originários, proteção de terceiros, indenização e consultas.
- Novo Código elimina enunciado aparentemente repetitivo; testar se houve redução real de proteção ao comparar direitos, procedimentos e exceções.

## 9. Governança e próximas verificações

O protocolo metodológico foi incorporado ao CLF pelo PR #1; a aprovação desse procedimento não aprova opções materiais do anteprojeto constitucional. A aprovação do PR adotará a **ferramenta metodológica**, não as hipóteses constitucionais materiais. Não alterar automaticamente `04_REGISTRO_DE_DECISOES.md` nem classificações de módulos por causa desta proposta.

**Pendências:** (i) manter link e commit constitucional atualizados; (ii) atribuir IDs estáveis às novas propostas normativas; (iii) revisar as 16 questões abertas; (iv) auditar primeiro os arts. 64–66, 174 e ADCT T1/T17 com T01.M04; (v) validar matriz de impacto artigo a artigo conforme avanço dos módulos.
