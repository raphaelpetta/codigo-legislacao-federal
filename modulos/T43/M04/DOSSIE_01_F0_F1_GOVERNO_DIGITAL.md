# T43.M04 — F0/F1: Governo Digital, lei de origem e delimitação de interfaces
**Corte:** 14/10/2026. **Issue #42**; branch `modulo/T43-M04-governo-digital-f0-f1-20261014`; main-base `16fba172c875c7a0de388288fe70005c944021d6`. **Estado:** F0 delimitado e F1 seletivo iniciado. Sem lei do CLF promulgada, sem consolidação C0-J, sem decisão material M e sem aprovação da arquitetura R2 de T07.

## F0 — função e perímetro
**Objeto:** princípios, garantias e requisitos de prestação digital dos serviços públicos, digitalização de processos, assinaturas, registros e plataformas governamentais, domicílio eletrônico, interoperabilidade, riscos e preservação de dados. O piloto documental utiliza a [Lei 14.129/2021 compilada da Câmara](https://www2.camara.leg.br/legin/fed/lei/2021/lei-14129-29-marco-2021-791203-normaatualizada-pl.html); Planalto [texto legal](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14129.htm). Não declarar legislação subnacional uniforme.

**Incluído na F1 desta rodada:** arts. **1º a 9º e 42 a 43**, com **76 unidades textuais localizadas estruturalmente** (caputs, parágrafos e incisos; dois dispositivos **vetados, sem conteúdo normativo**), em [inventário com proveniência](INVENTARIO_F1_PRIORITARIO.csv). São **unidades localizadas**, *não* 76 transcrições de texto e nem concordância jurídica certificada. Art. 3º inclui 26 princípios, art. 4º onze definições e parágrafo único; art. 7º remete à Lei 14.063/2020, Lei 12.682/2012, legislação de assinaturas e anonimato.

**Excluído da análise profunda nesta rodada:** arts. **10–41, 44–55**, disposições finais, alterações da LAI, Lei 13.460, Lei 12.682, Lei 7.116, dispositivos com redação alterada/vetada e a totalidade das normas infralegais e locais de implementação. **Não estão revogados nem incorporados**: são parte do F1 a completar. Especializar também LGPD, LAI, normas arquivísticas, regime de interoperabilidade e guarda documental.

**Regime positivo atual:** Constituição 1988 e leis da União aplicáveis; projeto constitucional alternativo é cenário futuro e **não altera o alcance da lei vigente**. A codificação deve distinguir o que a Lei 14.129 estabelece para órgãos federais e o que outros entes aplicam **somente após ato próprio** (art. 2º, III e §2º). Mesmo no âmbito federal, seu art. 2º, I e II, não pode ser resumido a “toda empresa estatal”: §1º exclui empresa estatal não prestadora de serviço público.

## F1 — blocos e riscos jurídicos
| Artigos | Principal função | Não confundir |
|---|---|---|
| 1º–2º | Objeto, interfaces com LAI/LGPD/CTN/LC105 e incidência por órgão/ente | Extensão compulsória aos municípios ou a estatais econômicas não prestadoras |
| 3º–4º | 26 princípios, definições, conceitos LGPD | Princípio orientador ≠ nova infração ou sanção |
| 5º–6º | Serviços/processos digitais e exceções para usuário, inviabilidade, indisponibilidade e dano relevante | Protocolo digital obrigatório em qualquer circunstância |
| 7º | Assinaturas eletrônicas proporcionais a risco; remissões a outras leis; veto no §1º V | Assinatura digital única para tudo, sem ressalvas |
| 8º–9º | Data/hora **de ato protocolado**, recibo e vista pelo interessado | Recibo de protocolo de petição ≠ ciência de intimação anterior |
| 42–43 | Opção/opt-out de comunicações digitais e meios de comprovação de autoria/emissão/**recebimento sem leitura**, auditabilidade e guarda mínima **cinco anos** | Confundir entrega, recebimento, consulta, leitura, ciência jurídica e início de prazo; art. 43 III não elimina termo legal especial |

As condições do art. 42 referem-se **aos sujeitos do art. 2º**, e as ferramentas do art. 43 referem-se **aos atos do art. 42**; eventual domicílio eletrônico legalmente obrigatório de procedimento especial requer pesquisa própria. O art. 43, III, permite ferramenta eletrônica mesmo que lei especial mencione pessoal/postal, dentro de seu regime de incidência, **mas não fixa dia universal de intimação**.

## Interdependência formal T07/T43 — hipóteses R1 e R2
**T07.M03 PR #39:** responsável pelas garantias, exigências de comunicação, contagem de prazo, nulidade e aplicação subsidiária da Lei 9.784/1999, ressalvadas leis especiais como [Decreto 70.235/1972 art. 23](https://www.planalto.gov.br/ccivil_03/decreto/d70235compilado.htm). O [contrato T07↔T43 proposto no ciclo 28](https://github.com/raphaelpetta/codigo-legislacao-federal/blob/pesquisa/t07-m03-ciclo21-ambito-intimacao-digital-20261014/modulos/T07/M03/CONTRATO_CICLO28_T07_T43.md) é *proposta*, não arquitetura ratificada. Aqui a F0/F1 de T43 inaugura **um inventário próprio** para que a interface seja auditada bilateralmente.

**Alternativa R1:** todos os requisitos de intimação procedimental residem em T07, com remissão pontual aos standards digitais da legislação vigente.

**Alternativa R2:** T43 mantém prova de autoria, emissão e recebimento, auditoria, retenção e opções digitais no seu âmbito, enquanto T07 conserva os efeitos processuais e prazos. A repartição é **candidata preferencial**, não homologada; **não criar dois artigos competindo sobre o termo inicial**. O `DEC-016` sobre espécie/iniciativa e forma do Código único continua aberto.

## Dez situações adversariais (todas Q)
1. Usuário não opta pelo canal eletrônico nos casos de opção exigida: sem presumir consentimento.
2. Usuário faz opt-out: registrar efeito para comunicações futuras no âmbito legal.
3. Domicílio tributário especial, com entrega e ficção de 15 dias: não incorporar automaticamente Lei 14.129 como se revogasse a disciplina do art. 23 do Decreto 70.235.
4. Plataforma emite, mas não comprova recebimento: art. 43 II exige ferramenta com essa capacidade quando aplicável.
5. Mensagem recebida, mas nunca lida: art. 43 II não exige comprovação universal de leitura; a ciência será definida por lei do procedimento.
6. Pedido protocolado às 23h58: art. 8º §1º disciplina tempestividade de ato praticado **pelo interessado**, não ciência pelo órgão.
7. Indisponibilidade da plataforma: art. 8º §2º requer regulamentação de prorrogação, art. 6º contempla meios alternativos; não criar suspensão universal arbitrária.
8. Empresa pública não prestadora de serviço público: art. 2º §1º exclui-a do âmbito da lei.
9. Município sem ato próprio de adoção: art. 2º III/§2º impede aplicação direta das regras estaduais/municipais por simples referência genérica.
10. Dados sigilosos e saúde: restringir acesso, aplicar LGPD e LAI, não tornar todos os logs públicos em nome da auditabilidade.

## Portas de qualidade
**F0:** recorte delimitado, interfaces e riscos. **F1:** apenas 76 IDs estruturais e fonte oficial; texto **não transcrito**, cadeia DOU/retificações pendente e estado Q jurídico. **F2 e C0-T:** não concluídos. **C0-J:** não homologado. **C1/M:** não deliberados. **DEC-016:** pendente. Interface T07/T43 sem efeito normativo aprovado.

**PRÓXIMO:** (a) cotejar fielmente texto histórico e vigente dos arts. 2º/42/43, (b) inventariar arts. 10–41 e 44–55, (c) auditar LGPD/LAI/assinatura e normas especiais, (d) cruzar formalmente 26 campos propostos de T07 com lei vigente sem inventar obrigação legal, (e) resolver formatação de Códigos separados/lei ordinária, e só então ensaiar redação com cautelas federativas.
