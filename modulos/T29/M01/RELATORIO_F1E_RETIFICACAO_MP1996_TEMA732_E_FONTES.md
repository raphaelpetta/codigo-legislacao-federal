# T29.M01 — F1-E: validação histórica, precedentes qualificados e correção de datas

**Corte:** 14/10/2026. **Escopo:** auditoria corretiva das quatro divergências F1-B/C/D, com ênfase em fonte originária e vigência. **Issue:** [#40](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/40); **PR:** [#41 draft](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/41); **base `main` CLF:** `16fba172c875c7a0de388288fe70005c944021d6`. **T29.M01** é proprietário, T24.M01 pertence a outro PR. **Sem texto C0/C1/M aprovado nem reforma constitucional antecipada.**

## 1. Retificação obrigatória — guarda judicial foi retirada da letra da lei em 1996, NÃO inicialmente em 1997

A [MP nº 1.523, de **11 de outubro de 1996**, publicação original no DOU de **14/10/1996**, p. 20.692](https://www2.camara.leg.br/legin/fed/medpro/1996/medidaprovisoria-1523-11-outubro-1996-359451-publicacaooriginal-1-pe.html) dispõe, em seu **art. 2º**, que o art. 16 §2º da Lei 8.213 passa a equiparar a filho apenas **enteado e menor tutelado**, condicionado à declaração do segurado e comprovação de dependência econômica. **O menor sob guarda não aparece.** Seu **art. 5º** estabelece entrada em vigor na data da publicação. **Fonte original identificada e efetivamente lida**, não mera informação histórica em notícia. A [ficha oficial da MP](https://www2.camara.leg.br/legin/fed/medpro/1996/medidaprovisoria-1523-11-outubro-1996-359451-norma-pe.html) registra reedição com alteração, indicação de perda de eficácia e conversão da cadeia na **Lei 9.528, de 10/12/1997**. **Não se demonstrou** a ausência de qualquer hiato jurídico nas reedições: essa cronologia de continuidade será examinada antes de classificar efeitos individuais por competência/óbito.

**Correção implementada nos dados F1-C:** em [F1C_CASOS_TEMPORAIS_18.csv](F1C_CASOS_TEMPORAIS_18.csv), **C10** passa a cobrir óbitos até **13/10/1996**, e **C11** começa **14/10/1996**; o fundamento menciona **MP 1523/1996, STJ Tema 732 e STF ADIs 4878/5083**. O arquivo histórico F1-B/F1-D descreve corretamente a **lei de conversão em 1997**, mas não deve mais ser interpretado como sendo 1997 a primeira data de exclusão literal.

**Relevância sistêmica:** uma consolidação que use somente a Lei 9.528/1997 como marco inicial pode conduzir a respostas falsas para óbitos entre outubro/1996 e dezembro/1997. A legislação aplicável ao óbito e a interpretação judicial devem ser reconstruídas com as reedições e decisões, não por simples data de conversão.

## 2. Precedente qualificado que faltava — STJ Tema 732

O [STJ Tema Repetitivo **732**, REsp 1.411.258/RS](https://processo.stj.jus.br/repetitivos/temas_repetitivos/pesquisa.jsp?cod_tema_final=732&cod_tema_inicial=732&novaConsulta=true&tipo_pesquisa=T) registra:
- **Primeira Seção**, julgamento de **11/10/2017**;
- publicação de acórdão em **21/02/2018**;
- trânsito em julgado em **09/03/2023**;
- **tese:** menor sob guarda economicamente dependente tem direito à pensão por morte de seu mantenedor **mesmo se o óbito se deu depois da vigência da MP 1.523/1996**, em razão da proteção especial do **ECA art.33 §3º**.

O [Informativo 619/STJ](https://processo.stj.jus.br/jurisprudencia/externo/informativo/?acao=pesquisar&aplicacao=informativo&livre=%40CNOT%3D%27016558%27) contextualiza o caráter protetivo da interpretação. A tese é **precedente repetitivo**, não opinião doutrinária, e deve figurar como **reconstrução do direito vigente aplicado ao período da MP e da Lei 9.528**. A tese **não decidiu expressamente** a validade da EC 103/2019 art. 23 §6º posteriormente editada: para eventos abrangidos pela EC103 essa reserva constitucional continua relevante.

Assim, são **quatro** camadas indispensáveis no histórico de guarda, não duas: (i) letra original 1991, (ii) exclusão textual em **MP1996/Lei1997** com proteção pelo STJ Tema732, (iii) EC103/2019 e posterior interpretação conforme ao art.16§2 em **STF ADIs4878/5083 (2021)**, (iv) **Lei15.108/2025** reinclui guarda e **STF Tema1271** aprecia especificamente EC103§6.

## 3. Efeito da correção no quadro intertemporal e no desenho do T29

| Fato gerador (óbito) | Fonte textual histórica relevante | Precedentes e situação jurídica que não podem ser apagados | Status de síntese |
|---|---|---|---|
| 1991 até **13/10/1996** | Lei8.213 art16§2 original incluía guarda | dependência/declaração e requisitos da época | DIREITO_LEGAL_HISTORICO — prova concreta |
| **14/10/1996 até 12/11/2019** | MP1523/1996 e reedições → Lei9528/1997 excluíram guarda da literalidade | **Tema732/STJ** e, posteriormente, **ADIs4878/5083/STF**, resguardam proteção sob dependência econômica | DIREITO_INTERPRETADO; verificar reedições e efeitos particulares |
| **13/11/2019 até 13/03/2025** | EC103 art23 §§4/6/7, Lei8213 §2 na redação então vigente | Tema732/ADIs sobre lei; **Tema1271** pendente sobre exclusão constitucional EC103§6 | Q_CONSTITUCIONAL_ESPECIFICA |
| **desde 14/03/2025** | Lei15108/2025 reintroduz guarda sob condições, coexistindo com EC103 | proteção expressa; alcance da EC103 e tema1271 a examinar | LEI_VIGENTE + Q_CONSTITUCIONAL_ESPECIFICA |

Este quadro não é parecer para deferir/indeferir caso real; não presume resultado do Tema1271 ou efeitos retroativos universais. Pela ficha do [Tema1271, RE1442021](https://portal.stf.jus.br/jurisprudenciaRepercussao/verAndamentoProcesso.asp?classeProcesso=RE&incidente=6661561&numeroProcesso=1442021&numeroTema=1271), na pesquisa de **14/10/2026**, a última movimentação apresentada era **16/04/2026**, conclusos ao relator após parecer PGR; repercussão geral reconhecida **não equivale a tese de mérito**.

## 4. Validação adicional de fonte — RFB 2110/2022 (PSA)

O [sistema oficial de normas da Receita, IN RFB 2.110/2022](https://normas.receita.fazenda.gov.br/sijut2consulta/consulta/link.action?idAto=126687&visao=original) passou a ser recuperável em **índice pesquisável e resultados textuais oficiais**, que registram no **art. 9º §5º IX** a participação em programas e ações de pagamento por serviços ambientais como fato que **não descaracteriza** o segurado especial, remetendo ao **art. 12 §9º VIII da Lei 8.212**. A IN foi publicada em **19/10/2022**, DOU seção 1, p.46. Esse suporte oficial melhora a evidência em relação à edição secundária mencionada na F1-D.

**Limite:** a ficha RFB lista ao menos **IN 2.185/2024, IN 2.289/2025 e IN 2.321/2026** como alteradoras. A plataforma não permitiu nesta rodada um confronto estruturado dos atos completos por dispositivo que comprovasse **que o inciso IX do §5º permaneceu textualmente inalterado em 14/10/2026**. Como os resultados da própria fonte contêm antigas e novas redações de dispositivos diversos, **a evidência recuperável certifica a redação publicada/original, não autoriza afirmar, por ela somente, um texto consolidado único certificado em 2026**.

**Lei formal:** a [Lei 14.119/2021, art.23](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14119.htm) incluiu §9º VIII na [Lei 8.212, art.12](https://www.planalto.gov.br/ccivil_03/leis/l8212compilado.htm); não aparece §8º VIII de conteúdo análogo na [Lei8.213 art.11](https://www.planalto.gov.br/ccivil_03/leis/l8213cons.htm). **Divergência estrutural demonstrada**; interpretação administrativa do INSS, consequências de renda, tributação e aposentadoria continuam Q. T29.M02 e T12 são interfaces, **não editar nesses módulos**.

## 5. Mandatos eletivos — duas publicações autênticas e efeitos distintos

- [Senado, Lei 9.506/1997, edição DOU **31/10/1997**, p.24.529](https://legis.senado.leg.br/norma/551382): origem da alínea **h**, sem amparo para convalidá-la retroativamente após EC20.
- [LexML federal, Lei 10.887/2004, edição DOU **21/06/2004**, p.1](https://www.lexml.gov.br/urn/urn%3Alex%3Abr%3Afederal%3Alei%3A2004-06-18%3B10887): origem distinta da alínea **j**, base pós-EC20.
- [Resolução Senado26/2005, DOU **22/06/2005**](https://planalto.gov.br/ccivil_03/_ato2004-2006/2005/congresso/ressf26-05.htm): ato de suspensão dirigido especificamente à **Lei 8.212 art.12 I h**, não j, nem expressamente Lei8.213 art.11 I h.
- [STF Tema691 RE626837](https://portal.stf.jus.br/jurisprudenciaRepercussao/verAndamentoProcesso.asp?classeProcesso=RE&incidente=3916429&numeroProcesso=626837&numeroTema=691): julgada contribuição posterior à **Lei10.887/2004** a mandatário não filiado ao RPPS, sem convalidação retroativa da antiga lei de 1997.

**Limite:** estas fontes comprovam data de publicação e origem, mas o confronto de **cada competência contributiva e eventual anterioridade nonagesimal** permanece especializado T29.M02/T12. Não desdobrar aqui todo o sistema de contribuição.

## 6. Filiação facultativa 14/16 — decisão não vinculante e proteção constitucional

[Lei8.212 art14](https://www.planalto.gov.br/ccivil_03/leis/l8212compilado.htm) e [Lei8.213 art13](https://www.planalto.gov.br/ccivil_03/leis/l8213cons.htm): maior de **14 anos**; [Decreto3048 art11/18§2](https://www2.camara.leg.br/legin/fed/decret/1999/decreto-3048-6-maio-1999-368532-normaatualizada-pe.html): **16**. O [TRF3 11ª Turma Recursal/SP, processo 5002988-56.2025.4.03.6322](https://web.trf3.jus.br/acordaos/Acordao/BuscarDocumentoPje/395087868) afastou, no caso, impedimento exclusivamente etário à filiação aos 15, mas negou salário-maternidade por fundamento de filiação instrumental de recolhimento isolado; **não vinculante nacionalmente**. [STF ADIs2110/2111](https://portal.stf.jus.br/noticias/verNoticiaDetalhe.asp?idConteudo=530062&tip=UN) invalidaram carência de salário-maternidade para categorias determinadas, mas **não decidiram diretamente todos os requisitos da inscrição de adolescente facultativo sem trabalho**. É necessário distinguir filiação, recolhimento, carência, fraude comprovada e proteção à maternidade; não equiparar decreto a revogação da lei.

## 7. Portas de qualidade, FEITO/PENDENTE/PRÓXIMO

**FEITO nesta rodada:** publicação original MP1523/1996 **lida**, nova correção em F1-C, precedente vinculante STJ Tema732 e datas; fontes oficiais de DOU 1997/2004 identificadas e vinculadas; texto original de RFB encontrado em índice institucional; mapa rastreável de **19 eventos** em [F1E_CADEIAS_FONTE_19_EVENTOS.csv](F1E_CADEIAS_FONTE_19_EVENTOS.csv). **Nenhum documento de outro módulo modificado.**

**PENDENTE:** (i) texto e efeitos das **reedições da MP1523** entre outubro de 1996 e conversão em 1997; (ii) eventual ato posterior ou julgamento de **Tema1271**; (iii) conteúdo completo do acórdão STF ADIs4878/5083 e modulação; (iv) versão do **inciso IX da IN RFB2110** após INs 2185/2289/2321, sem inferir preservação do texto por falta de ato; (v) efeitos do acórdão TRF3 e limites de filiação facultativa; (vi) verificação dos 198 inventários funcionais por unidades literais e F2 sistema vigente; (vii) repercussões formais de C0/C1/M, instrumentos DEC016, CF futura e status CI.

**PRÓXIMO — T29.M01/F1-F:** resolver **cadeia MP1523/1996 e reedições** com cada texto original, data e cláusula de convalidação e, se possível, aferir **alcance temporal do Tema732** perante a EC103/Tema1271. Como tarefa secundária de qualidade, verificar se IN RFB 2185/2289/2321 tocou art9§5 IX; integrar resposta de T29.M02 quando existir. **Entregável:** quadro normativo por fase com origem/destino e testes de direitos preservados, apto para iniciar F2 sem engolir controvérsia constitucional. **Critério de aceite:** nenhum período de 1996/1997 chamado de direito inalterado por presunção e nenhuma Q promovida a solução jurídica sem fonte.

**Arquitetura recomendável ainda provisória:** unificar no futuro conceitos gerais de sujeito previdenciário apenas depois do mapeamento de diferenças e manter módulos M01 (qualidade) / M02 (custeio) / M05 (pensões), com remissões cruzadas, respeito ao ECA, STF, STJ, EC103 e normas transitórias. Não há redação nem aprovação M nesta rodada.
