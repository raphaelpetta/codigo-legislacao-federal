# Anexo 03 — Sistema normativo federal integrado CF–CLF–CRF: referências, atualizações e custódia

**Data:** 15/10/2026 · **Estado:** PROPOSTA DE ARQUITETURA, `M/Q`, **sem ratificação material** · **Destino:** T01.M04/M05/M06, T07, T43 e interface constitucional condicionada · **Central:** issue #48 · **PR draft:** #51.

## 0. Natureza, nomenclatura e decisão pendente

Três **camadas de consulta e organização**, não três degraus universais de hierarquia nem três espécies jurídico-formais:
1. **CF — Constituição Federal**: texto constitucional e emendas, com normas de superioridade constitucional;
2. **CLF — Código da Legislação Federal**: corpus único geral/permanente em desenvolvimento, **DEC-016 ainda pendente** quanto à positivação formal e às diferentes reservas/competências;
3. **CRF — Código de Regulamentação Federal** (nome proposto pelo usuário; equivale à denominação provisória `CFR-BR` do Anexo 02): repositório oficialmente instituído de atos normativos infralegais federais de efeito geral, organizado por matéria e autoridade, sem fusão das competências.

**Atenção:** não presumir que toda norma do CRF tenha fundamento exclusivo num único artigo do CLF: alguns atos têm fundamento constitucional direto ou em atos próprios, e a lei não esgota o suporte de validade. Tratados, atos de outros Poderes, normas anuais/temporárias, legislação federada e textos históricos permanecem sob sistemas de referência próprios. As fontes que ainda não foram absorvidas no CLF não podem desaparecer do suporte normativo do CRF.

**Objetivo jurídico:** legislar sobre a existência, integridade e manutenção dos sistemas, sem transferir para órgão catalogador a competência de criar, modificar ou revogar normas. Os campos e procedimentos abaixo são hipóteses de modernização `M`, com dúvidas `Q` de reserva de iniciativa, arquitetura e eficácia jurídica do texto consolidado.

## 1. Direito brasileiro existente e comparação

- **CF/1988 art. 59, parágrafo único:** lei complementar disciplina elaboração, redação, alteração e consolidação das leis; **art. 60 §3º:** promulgação de EC pelas Mesas da Câmara e Senado; **arts. 61 §1º e 84 IV/VI:** reservas de iniciativa e poder regulamentar/organizatório. Não criar uma nova espécie normativa só com nomenclatura.
- **LC 95/1998 art. 12:** alteração legislativa por texto integral, revogação ou substituição/acréscimo no texto vigente; **arts. 13–14:** consolidação das leis já prevista. Não presumir que LC 95 autorize unidade formal universal de CLF ou outorgue poder normativo à equipe de edição.
- **Decreto 12.002/2024, arts. 8, 65–71:** alteração/revogação de atos da mesma espécie e consolidação periódica, com publicação autêntica/compilação. Já existe técnica setorial, mas não corpus federal global de todos os órgãos, e o próprio decreto tem campo de aplicação delimitado (art. 2º).
- **44 U.S.C. §§ 1506, 1510:** Congresso norte-americano disciplina estrutura de publicação e codificação do *Code of Federal Regulations*, mantendo autoridades emissoras; 44 USC §1510(c) trata da republicação anual e versões eletrônicas por data; §1510(e) dá status de prova prima facie ao CFR codificado e complementos do Federal Register. **Federal Register** publica atos; **CFR** condensa; **eCFR** é versão editorial eletrônica, não edição legal oficial. Regras dos EUA não se importam automaticamente.
- **Office of Federal Register, Document Drafting Handbook**: regras de *amendatory instructions* exigem designar unidades concretas do CFR a modificar, inserir, revogar, renumerar; cada alteração é promovida por autoridade competente por instrumento publicado, não por editor substantivo.
- **STF Tema 917 (ARE 878.911)**: despesa não vicia por si só iniciativa de lei; o vício emerge se houver disciplina de estrutura/atribuições de órgãos ou de regime jurídico de servidores em matérias reservadas. A aplicação a eventual órgão federal central requer parecer próprio; não tomar precedente municipal como autorização geral.

Fontes primárias:
- https://www4.planalto.gov.br/legislacao/portal-legis/legislacao-1/constituicao
- https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp95compilado.htm
- https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2024/decreto/d12002.htm
- https://uscode.house.gov/view.xhtml?edition=prelim&f=treesort&fq=&hl=false&num=0&req=%28title%3A44+section%3A1510%29
- https://www.govinfo.gov/help/cfr
- https://www.archives.gov/federal-register/write/ddh
- https://portal.stf.jus.br/jurisprudenciaRepercussao/verAndamentoProcesso.asp?classeProcesso=ARE&incidente=4744414&numeroProcesso=878911

## 2. Sistema de referências: o que disciplinar em lei, em regulamentos e na tecnologia

### 2.1. Quatro identificadores coexistentes

1. **Citação canônica humana:** CF art. n, §/inciso; CLF livro/título/art. n; CRF título/parte/seção ou artigo n; ato-fonte tradicional por espécie, número, data e unidade. A numeração do CLF segue DEC-016 (nada aprovado); nomenclatura CRF é futura.
2. **Identificador digital persistente** por unidade/dispositivo sem depender de mudança de nome ou renumeração de capítulos. Ex.: `urn:br:clf:t07:livro-pa:art-XYZ` / `urn:br:crf:t07:orgao-abc:parte-123:sec-XYZ` são **exemplos fictícios**, não URNs oficiais nem normas atuais.
3. **Identificador de versão / temporalidade:** estado válido e efeitos `na data D`, `conforme ato modificador P`, com eventos individualizados e cadeia de assinaturas/proveniência. Identidade da unidade ≠ conteúdo vigente em cada data.
4. **Citação da fonte promulgadora autêntica:** EC ou lei com número/data/DOU; decreto/portaria/resolução com espécie, emissor, número, data e DOU. A compilação não suprime o ato fonte.

**Regra:** toda referência automática deve preservar fonte original, qualificação `VIGENTE_CONFIRMADO` ou `Q`, e versões, sem converter uma remissão interpretativa em ato válido.

### 2.2. Relações explícitas entre normas (muitos-para-muitos)

- `fundamento_de_validade` (CF, competências legais);
- `regulamenta` (CRF → CLF/lei ainda fora do CLF ou CF, nos limites verificados);
- `altera`, `acrescenta`, `revoga`, `substitui`, `consolida`;
- `remete_a` e `complementa`, distinguindo relação literal de anotação editorial;
- `excecao_a`, `aplicacao_subsidiaria`, `condiciona`, `transicao`;
- `suspensao_ou_invalidez_verificada` com decisão, efeito temporal e competência, não como supressão editorial.

**Exemplo ilustrativo (não são referências reais):** CF art. 37 → CLF/T07/Livro PA/dispositivo X → CRF/T07/órgão Y/dispositivo Z; a versão de Z mantém referência à Portaria original e à publicação no DOU. O vínculo depende da regra concreta: não presumir que todos os regulamentos descendam de um único artigo.

### 2.3. Reserva jurídica por instrumento

| Questão | Lei/CLF, conforme veículo constitucional | Autoridade executiva/órgão competente | Execução técnica |
|---|---|---|---|
| Dever legal de registro/consolidação e seus limites | Sim, sujeito a iniciativa competente | Observa e detalha dentro da competência | Implementa |
| Formato de citação oficial, citações históricas e referências cruzadas mínimas | Núcleo de garantias em lei | Padrão de redação e formato conforme competências | URNs, APIs, persistência e alias |
| Força probatória do compilado, divergência e proteção da confiança | Lei após estudo específico | Cumpre e corrige | Publica erratas rastreáveis |
| Alteração material de lei do CLF | Legislativo no rito da espécie/competência | Não | Apenas aplica alteração promulgada |
| Alteração material de ato do CRF | Não cabe ao legislador reescrever unilateralmente regulamentos, embora lei superior possa alterar seu fundamento e conteúdo permitido | Titular do poder regulamentar, por ato válido/publicado | Consolida sem mudar mérito |
| Estrutura de equipe e gestão interna da administração | Sujeita a iniciativa/competência reservadas | Organiza órgãos existentes e execução, conforme lei | Profissionais e serviços |

Não se deve exigir constitucionalizar **cada detalhe**; a Constituição asseguraria hierarquia, competência e segurança jurídica, enquanto a base legislativa garante sistema/rotina e regulamentos disciplinam procedimentos.

## 3. Como se alteraria o CLF x o CRF

### CLF — alteração legislativa

Projeto/ato competente → aprovação na forma exigida (LO/LC etc.) → sanção/veto/promulgação conforme caso → publicação → altera, acrescenta, revoga ou cria bloco do **CLF** → serviço técnico regenera redação corrente, índice e histórico. **O texto consolidado é resultado**, não substitui lei autenticamente aprovada. `DEC-016` ainda impede presumir alteração legislativa de um diploma único universal já válido.

### CRF — duas variantes jurídicas para atos regulamentares

**R1 — corpus oficial documental (viável preparatoriamente):** cada órgão edita ato próprio válido (decreto/portaria/resolução, observada sua espécie e competência), indicando **expressamente** qual ato e qual dispositivo altera ou revoga. Publicado na forma adequada, sua versão atualizada é **incorporada pelo CRF** segundo a chave tema+emissor+ato+dispositivo. O editor não pode emitir comando que não esteja no ato original. A fórmula “fica alterado artigo X do CRF” **não substitui** a identificação da fonte material normativa, enquanto o CRF permanecer apenas editorial.

**R2 — codificação regulamentar positiva por órgão, mais ambiciosa:** a autoridade competente edita e autentica uma **parte/regulamento consolidado próprio** identificado por seção do CRF, com atos sucessivos que modificam formalmente suas seções. Continua necessário ato material emitido pelo órgão (com DOU, competência, vigência, revisão e transição). O CRF continua conjunto de atos de **múltiplos emissores**, sem nova autoridade central com poder regulamentar universal. Esta opção requer estudo de efeito jurídico, forma de publicação e migração de espécies.

**Casos especiais:** decreto presidencial pode revogar/alterar decretos de sua competência mas uma portaria de ministro não revoga decreto; agência independente não tem competência genérica para alterar ato de outra; ato especial pode ter ligação com mais de uma lei; alteração do CLF impõe **revisão de compatibilidade** de normas inferiores, mas não implica revogação automática universal por um editor, devendo identificar inaplicabilidade, incompatibilidade, revogação ou necessidade de ato competente e seus efeitos.

**Separar:** `DATA_PUBLICACAO`, `INICIO_VIGENCIA`, `INICIO_EFEITOS`, `FIM_EFEITOS`, `DATA_COMPILACAO`, `DATA_ULTIMA_CONFERENCIA`. Não ocultar `Q`.

## 4. Estruturas profissionais de custódia e auditoria

**Princípio:** tecnologia automatiza execução; a responsabilidade documental e jurídica continua **humana, especializada e institucionalmente atribuída**. Uma estrutura profissional permanente é recomendável; **órgão novo é hipótese, não pressuposto**.

| Função | Localização funcional possível | Competência restrita |
|---|---|---|
| Custódia constitucional | Estruturas legislativas e de publicação constitucional existentes | Texto autêntico, ECs, versões e remissões sem interpretação substantiva imposta por editor. |
| Serviço técnico de codificação legislativa | Apoio técnico do Congresso e serviços competentes, com coordenação interinstitucional | Inventário, concordância, numeração, rastreio de leis e propostas; sem legislar. |
| Serviço de registro/codificação regulamentar | Arranjo executivo existente ou institucionalidade criada por veículo e iniciativa competentes | Disponibilizar atos de diversos emissores, versionar e estruturar publicação, sem modificar mérito. |
| Pontos focais de autenticidade | Cada ministério, agência e órgão emissor | Validar atos, alterações, efeitos, vacatio, revogações e remissões que lhes competirem. |
| Auditoria, arquivos, dados e acessibilidade | Equipes mistas vinculadas aos serviços acima | Certificação de origem, qualidade, correções, linguística jurídica, UX, APIs, segurança, acessibilidade. |

Perfis mínimos: especialistas jurídicos de diferentes ramos, técnica legislativa/regulatória, arquivistas, bibliotecários/documentalistas, engenheiros de dados e software, cientistas da informação, comunicação clara, acessibilidade, controle de qualidade e segurança da informação.

**Governança:** conselho **consultivo** federado entre Legislativo, órgãos administrativos, agências, órgãos de publicação e arquivo; não atribuir competência para revogar ato alheio. Separação de funções (*quatro olhos*): curadoria documental ≠ decisão material; registrar quem propôs, aprovou, publicou e auditou cada mudança; historização e correção pública. Criar cargos/agência específica somente após comprovar necessidade, custos e competência/iniciativa, não por inércia institucional.

## 5. Sequência de implementação proporcional

**Fase 0 — piloto interno CLF/CRF:** modelar dados, URNs e regras de concordância em T07 (processo administrativo) e em outra área com alto volume infralegal, com fontes oficiais, efeitos, autoridades e datas. Não atribuir força legal ao protótipo.

**Fase 1 — lei-base, após auditoria formal:** instituir dever de registro, referência, atualização, transparência, competências, critério de divergência do texto integrado e histórico, sem criar órgão forçosamente nem invadir autonomia administrativa.

**Fase 2 — execução administrativa e migração de atos atuais:** priorizar efeitos gerais externos e atos de maior relevância, publicações autenticadas, relações com leis, criação de API e controle temporal; metas de cobertura verificáveis, não metas de revogação quantitativa.

**Fase 3 — codificação regulamentar positiva por emissor, caso desejada:** gradual, com cada autoridade adotando atos consolidados próprios, instruções padronizadas de atualização e compatibilidade jurídica. Evaluar se a codificação editorial R1 já satisfaz a finalidade sem custos extras.

**Fase 4 — aprofundamento constitucional apenas condicional:** se o projeto CF optar por viabilizar CLF como espécie/unidade formal sui generis ou alterar organização de competências/iniciativas, remeter à interface constitucional; não assumir necessidade de emenda constitucional para o corpus CRF documental.

## 6. Minuta de garantias de sistema (M/Q — não numerada no CLF)

**Cláusula proposta 1 — Referências oficiais.** A identificação normativa conterá espécie, autoridade emissora quando cabível, data e unidade normativa, acompanhada, nos sistemas oficiais, de identificador persistente e registro verificável de suas alterações e períodos de vigência e produção de efeitos.

**Cláusula proposta 2 — Rastreabilidade e integração.** Os sistemas oficiais de legislação e regulamentação manterão vínculos verificáveis entre norma superior e atos de execução, sem prejuízo das referências às fontes originais, aos atos ainda não codificados e às competências normativas próprias.

**Cláusula proposta 3 — Alterações.** As alterações da legislação e da regulamentação deverão identificar as disposições afetadas, com destino sistemático e regras de transição, nos termos e limites da espécie e competência exigidas para a edição do ato.

**Cláusula proposta 4 — Compilação oficial.** Os responsáveis pelos repositórios produzirão versões temporalmente identificadas e preservadas, com acesso público gratuito, ressalvadas hipóteses legais de restrição, além de mecanismos de correção, auditoria e restauração. A compilação não modificará por si só o alcance normativo da fonte autêntica.

**Cláusula proposta 5 — Custódia qualificada.** A execução do sistema contará com responsabilidade institucional definida, procedimentos documentados de controle jurídico e técnico, especialistas em documentação normativa e infraestrutura segura, observadas as competências de organização administrativa e iniciativa legislativa constitucionalmente reservadas.

**Não fixado:** texto final, numeração de artigos, nomenclatura oficial CRF, natureza jurídica de cada edição, força probatória, órgão custodiante, calendário, custo, alteração do produto constitucional e veículo legislativo. Exigem pesquisas e decisões específicas. Nenhuma norma existente foi alterada.

## 7. Testes adversariais e interfaces

1. CF é alterada por EC e compilada; o editor jamais promulga emenda ou altera norma constitucional.
2. CLF atualiza norma de competência e CRF aponta regulamento potencialmente incompatível: `Q` e revisão por autoridade própria, jamais revogação silenciosa.
3. Agência altera sua resolução: original autêntico é registrado; CRF incorpora versão; outro órgão não edita seu conteúdo.
4. Norma disciplinar e lei penal remissiva: não criar tipo penal por interpretação editorial; preservar legalidade.
5. Decisão judicial invalida dispositivo regulamentar com efeitos temporais: registro completo do processo, da autoridade e extensão do julgado.
6. Erro de compilação e confiança legítima: corrigir publicamente e examinar proteção jurídica sem converter editor em legislador/regulador.
7. Lei anual/orçamentária ou regulamento excepcional: acervo temporal com vínculos e rastreio, sem supressão.
8. Mudança de nomes/competências de órgãos: identificador persiste, histórico se mantém, novas atribuições só por atos válidos.

**Handoff para Central CLF #48:** registrar alternativa de integração CF–CLF–CRF, diferenciação R1/R2, regras de referência, papéis profissionais e teste prático. **Handoff para CF #103:** apenas matriz de impacto constitucional, sem pedir constitucionalização de minúcias nem importar decisões.
