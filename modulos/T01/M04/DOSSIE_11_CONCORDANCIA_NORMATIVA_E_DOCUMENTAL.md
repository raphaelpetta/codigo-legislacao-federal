# T01.M04 — Ciclo 11: concordância legislativa em duas camadas e revogações em escala

**ID:** CLF-T01-M04-CONC11 · **Corte:** 13/10/2026 · **Status:** F1/F2/F3/F5 PARCIAL; pesquisa e simulações, **NENHUMA norma aprovada**.  
**Baseline CLF:** `189860ee90d24eb57c698c54b7a4bf04e090270d`. **Baseline CF:** `afe67ef7cbe0aa2931b555c2936e837bb9704990`.  
**DEC-001:** objetivo de um Código juridicamente uno e integrado permanece; **DEC-016:** veículo de promulgação PENDENTE.  
**Dependências:** `TESTE_10_UNIDADE_TEXTUAL_VETO_V1.md`, `MINUTAS_EXPERIMENTAIS_10_UNIDADE_VETO.md`, CF-IC-001, LC 95/1998, CF/1988 art. 66, LINDB e direito de iniciativa reservado.  
**Planilhas:** `CONCORDANCIA_NORMATIVA_SIMULADA_11.csv` (tabela projetada e não aprovada); `CONCORDANCIA_DOCUMENTAL_11.csv` (pesquisa e proveniência); `TESTES_CONCORDANCIA_11.csv` (cenários adversariais).

## 1. Problema e conclusão preliminar

O modelo M2 do ciclo 10 evita separar **condição** e **comando revogatório** em unidades suscetíveis de veto independente, mas multiplicar um novo artigo a cada par de dispositivos antigo→novo seria tecnicamente insustentável em um Código com milhares de remissões.

**Não precisamos de um artigo distinto por mapeamento**: a unidade mínima de revogação pode ser um conjunto homogêneo e precisamente delimitado, enquanto o histórico granular fica em tabela. **Mas a tabela digital não se converte em lei**; se condições ou revogações dependem de linhas de tabela, o conteúdo normativo dessas linhas precisa fazer parte de texto **deliberado e promulgado** no procedimento constitucionalmente correto. Não se demonstrou que o art. 66, §2º, por si, confere a cada linha de ANEXO uma unidade de veto — risco a enfrentar, não suprir por analogia com artigo/inciso/alínea.

**Resultado provisório:** arquitetura dual `N` (lei promulgada, incluindo **somente se legalmente validado** anexo normativo estático incorporado) + `D` (tabela de origem/destino e provas sem força de lei), com uma camada operacional `P` de *publicação e eventos* que registra vigências e vetos sem criar disposições jurídicas. A unitização jurídica de revogação **não é automaticamente** igual à linha de tabela.

## 2. Fundamento brasileiro e limites

- **CF/1988 art. 66 §2º:** veto parcial apenas sobre *texto integral* de artigo, parágrafo, inciso ou alínea. Não pressupor que uma linha de planilha, item de anexo ou etiqueta `CSV` seja unidade constitucional vetável. O quórum e a iniciativa material continuam externos ao problema editorial (arts. 59, 61, 69, 96 e 146).
- **LC 95/1998, art. 9º:** cláusula de revogação deve enumerar **expressamente as leis ou disposições legais revogadas**. **Arts. 10–11:** unidades de articulação e redação com precisão, clareza e remissões. **Art. 13 §1º:** consolidação com revogação formal sem modificar alcance ou interromper força normativa. **Art. 14 I, §2º e §3º:** identificar diplomas revogados e distinguir consolidação, leis preexistentes e iniciativa. Uma tabela puramente documental não substitui a enumeração legislativa exigida.
- **LINDB art. 2º §§1º–3º e art. 6º:** revogação por incompatibilidade, lei nova reguladora e coexistência; não repristinação automática após revogação válida, proteção de relações juridicamente constituídas. Uma matriz não pode restabelecer norma nem mudar efeitos temporais.
- **Decreto 12.002/2024, arts. 62–64**, disciplina consolidação de atos e demonstra instrumentos procedimentais da área executiva; não amplia competência para converter leis do Congresso em regulamentos.
- **Exemplo de anexo real com consequências normativas:** Decreto 12.018/2024, art. 5º, revoga especificamente **dispositivos de um anexo** de decreto anterior; demonstra que tabelas e anexos são objetos legislativos/normativos identificáveis, mas **não demonstra** constitucionalidade de veto de linhas isoladas de uma futura lei de codificação.
- **STF:** não foi localizado nesta pesquisa precedente decisivo que sustente **exatamente** que uma **tabela anexa de remissões e revogações** tenha, por si, todas as condições de veto, iniciativa e promulgação de enunciados articulados. **Questão aberta**, não declarar inexistência definitiva de precedente.

**Fontes oficiais:**
CF https://www4.planalto.gov.br/legislacao/legis-federal/constituicao ;
LC 95 https://www2.camara.leg.br/legin/fed/leicom/1998/leicomplementar-95-26-fevereiro-1998-363948-normaatualizada-pl.html ;
LINDB https://www2.camara.leg.br/legin/fed/declei/1940-1949/decreto-lei-4657-4-setembro-1942-414605-normaatualizada-pe.html ;
D. 12.002/2024 https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2024/decreto/d12002.htm ;
D. 12.018/2024 https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2024/decreto/d12018.htm .

## 3. Três camadas com atributos e autoridade distintas

### N — Conteúdo normativo juridicamente promulgado

**N.1, corpo de artigos**: proposições, regras substitutivas, condições de eficácia e cláusulas revogatórias **expressamente votadas**, além de disposições transitórias; para proteger `V1`, manter a condição e comando de revogação no **mesmo artigo indiviso** (sem parágrafo autônomo com a condição), quando juridicamente apropriado.

**N.2, possível anexo normativo estático**: relação exaustiva e precisa de alvos revogados e substituições **com remissão legislativa expressa**; texto anexo identificado, versão imutável do momento de votação, publicado integralmente e com prova de quórum/iniciativa. **Questões abertas:** i) se essa técnica satisfaz plenamente LC 95 art. 9º; ii) como veto constitucionalmente válido incide nas linhas do anexo; iii) se condições na tabela podem ser isoladamente vetadas; iv) efeitos de posterior substituição do anexo por arquivo atualizado. **Nunca** considerar o anexo normativo automaticamente válido; testar `N.1-only` como controle de legalidade.

**N.3, cronologia/transição**: norma transicional aprovada e divulgada pela fonte autêntica determina efeitos jurídicos e ressalvas; não substituir direitos adquiridos por coluna `data` inserida pelo editor.

### D — Concordância documental verificável, sem efeito inovador

Tabela extensa de **origem→destino**, com relação 1:1, 1:N, N:1 ou nenhuma, texto de origem/versões, C0/C1/M/Q, técnica de auditoria, parecer, justificativa, quórum, iniciativa, fonte primária, `status_prova` e `vinculo_normativo`. 
- Disposição vetada aparece como **texto de projeto não promulgado**, e não como destino vigente.
- Texto histórico (LC 70/1991 art. 6º, II) fica em memória, **não** em tabela de revogações atuais do CLF.
- Lei 11.416/2006 arts. 11–13, se titular de iniciativa não participa, aparece como **fonte externa pendente**, **sem** ser declarada revogada por um simples vínculo técnico.
- Alterações documentais posteriores são rastreadas sem mutar `N`. Erros da matriz são corrigidos por retificação do metadado; erro do **ato jurídico promulgado** requer procedimento jurídico competente, que pode ser mais complexo.

### P — Registro público de eventos, também não normativo

Eventos de publicação, aprovação por Casa, veto, manutenção/derrubada de veto, promulgação, vigência, suspensão, controle judicial e efeitos transitórios. O registro é **prova indicativa**, não decide juridicamente controvérsias de interpretação.

**Invariante:** `N` só muda por ato constitucionalmente habilitado; `D` e `P` podem receber correção documentada, mas não criar/não revogar `N`.

## 4. Quatro modelos de técnica legislativa comparados

| Código | Texto legislativo | Vantagem | Risco jurídico/fático |
|---|---|---|---|
| **A — Artigos explícitos por família** | Artigos com enumeração de dispositivos revogados + condições `R+C` no mesmo texto integral, separados por regime de iniciativa/quórum e gatilho | Menor controvérsia sobre **onde está a lei**; não exige tratamento novo de linhas de anexo | Código com grande seção revogatória; remissões e condições múltiplas; precisa de desenho cuidadoso da unidade de veto |
| **B — Artigo + ANEXO N estático** | Artigo legislativo indica expressamente anexo aprovado; cada linha traz fonte, dispositivo, destino e condição | Escala melhor, tabela legível e auditável, menos prosa articulada | **Não comprovada** unidade de veto de linha de anexo; risco emenda parcial, veto, erro de planilha; verificar LC 95 art. 9º e hierarquia por matéria |
| **C — Artigo geral + tabela D sem lei** | Artigo diz “revogam-se as leis correspondentes ao portal” e tabela muda dinamicamente | Simplicidade apenas aparente | **REJEITAR**: revogação indeterminada/delegada, violação de certeza e risco de atualização editorial constitutiva; não há enumeração adequada |
| **D — Artigos setoriais + ANEXO D meramente explicativo** | Leis antigas especificamente enumeradas em artigos; anexo de rastreio/navegação sem criar direito | Preserva transparência e estabilidade de vínculo jurídico; escala informacional livre | Artigos de revogação crescem e dependências exigem correspondências claras; ainda deve testar M2 e necessidade de reforma constitucional para Código formal uno |

**Preferência para teste jurídico sob direito brasileiro vigente:** **D/A** como base defensiva, e **B** como alternativa de eficiência **juridicamente não validada**. Não presumir que técnica legislativa de anexos solucionou iniciativa, quórum ou a espécie do Código `DEC-016`.

## 5. Casos reais documentais, sem fingir transposição aprovada

| Fonte vigente/histórica | Campo de origem | Classe material e risco | Estado de destino experimental |
|---|---|---|---|
| **LC 95/1998 art. 13, §1º** | Consolidação / continuidade | Reserva LC por CF art. 59 par. único; exigiria veículo e iniciativa legítimos | `CLF:T01:M04:EXPERIMENTAL:001` **não promulgado** |
| **Lei 9.784/1999 art. 2º, caput** | Princípios do processo administrativo federal | LO em recorte, proteção de direitos constitucionais, C0 a provar | `CLF:T07:PROC:EXPERIMENTAL:002` **não promulgado** |
| **Lei 9.784/1999 art. 2º, parágrafo único, incisos** | Critérios de processo | LO / várias unidades, possível 1:N; analisar vinculação das garantias entre incisos | `CLF:T07:PROC:EXPERIMENTAL:003-A/B` **não promulgados** |
| **CTN art. 174** | Prescrição de crédito tributário | Materialmente LC; **LC 236/2026 e vetos**; versão e efeitos temporais **a verificar** | `CLF:T12:TRIB:EXPERIMENTAL:004` **Q, sem alteração/revogação** |
| **Lei 11.416/2006 arts. 11–13** | Regime de remuneração judicial federal | LO com iniciativa judicial reservada para reforma de mérito; C0 com revogação formal é Q | **REMISSÃO EXTERNA**, nenhuma revogação aprovada |
| **LC 70/1991, art. 6º, II (histórico)** | Antiga isenção COFINS | Tema 71/SV 62, revogação histórica; não vigente | **ARQUIVO HISTÓRICO**, não inclusão positiva no CLF |

**Risco adicional:** fichas de exemplo `LC 95` ou `Lei 9.784` demonstram tipos diferentes de mapeamento, **não** comprovam já validada a equivalência C0 de seus textos, nem que o universo está exaurido.

## 6. Contraprovas: alterações específicas nas duas camadas

1. **Veto ao artigo R inteiro:** o anexo D ainda aponta correspondência em projeto, mas não é capaz de causar revogação de A; registrar `VETADO` e deixar A em vigor **se nada mais válida a revogar**.
2. **Veto parcial ao artigo S:** condição do artigo R vinculada à entrada em vigor genérica de S pode disparar prematuramente; a prova de unidade indispensável tem de estar **no texto normativo N**, nunca apenas na coluna `gatilho` de D.
3. **Veto de linha do anexo N:** **Q constitucional** — não afirmar que linha seja inciso ou alínea para aplicação do art. 66 §2º; exigir parecer e desenho de anexo com unidades legais conforme técnica escolhida.
4. **Matriz D diz que A está revogada, mas N não contém regra eficaz:** **erro editorial**, corrigir D; não revogar A.
5. **Tabela D omite uma lei realmente revogada em N:** **N continua prevalente** quanto aos efeitos jurídicos, embora erro gere insegurança e deva ser retificado com histórico.
6. **Derrubada tardia de veto a S:** D/P podem registrar o fato, mas as datas e efeitos de R decorrem de N e de atos formais promulgados; não retroagir automaticamente.
7. **Revogação N já eficaz, S declarado inválido depois:** não restaurar A por anotação da tabela; analisar controle judicial, LINDB e efeitos concretos.
8. **Alteração legislativa posterior:** atualizar Código por lei/espécie/competência apropriados, gerar nova versão N e anotações D/P, **não** sobreescrever o texto autenticado histórico.
9. **Iniciativa reservada J ausente:** não publicar linha N de revogação; D documenta `REFERENCIA_EXTERNA`.
10. **Uma fonte A distribuída em vários destinos S1/S2:** necessidade de condição cumulativa ou divisão dos alvos em unidades homogêneas **aprovada em N**; não supor que `S1 em vigor` substitui integralmente A.
11. **Fontes A1/A2 fundidas em S1:** necessita demonstrar equivalência semântica das fontes, direitos e âmbitos; se mudança de mérito, classificação M e procedimento próprio, sem usar rito simples C0.
12. **Anexo normativo revogatório atualizado por commit de GitHub:** **REPROVAR** — nova disposição requer procedimento legislativo; não deixar ato legal incorporar dinamicamente conteúdo editável por URL.

## 7. Comparação com EUA, Nova Zelândia e técnica atual

**EUA (US OLRC):** a codificação positiva é preparada título a título e acompanhada por **disposition table** (destino da fonte), **source credit table** e **revision notes**. Tabelas fazem parte da explicação do projeto que acompanha o texto aprovado: **não se presume que essas tabelas, só por serem publicadas pelo OLRC, revoguem leis por poder próprio**. Nos Estados Unidos, os títulos promulgados como *positive law* são legislação positiva distinta das tabelas explicativas. Fonte: https://uscode.house.gov/codification/legislation.html .

**Nova Zelândia, Legislation Act 2019:** ss. 30–39 sobre alteração/revogação e seus efeitos, 59–62 sobre leis de revisão, 78–91 sobre versões oficiais, publicações e mudanças editoriais. A legislação vigente possui regra específica (seção 79A) sobre o status de notas de publicação: alerta para explicitar o **estatuto jurídico da camada documental**. Não copiar poderes do Parliamentary Counsel Office sem adaptar à Constituição brasileira. Fonte atualizada em 04/09/2026: https://www.legislation.govt.nz/act/public/2019/58/en/latest/sections/DLM7298272/ .

**Brasil, Decreto 12.002/2024:** critérios técnicos de consolidação úteis como parâmetro de legística, não fundamento para inovar lei federal pelo Executivo; a Constituição e LC95 prevalecem.

**Implicação estrutural:** adotar **tabelas de rastreio extensas e legíveis**, mas manter a produção de efeitos jurídicos em atos legislativos competentes. Se o projeto quiser **anexo normativo em escala**, ele precisa passar por auditoria formal específica sobre veto, publicação e quórum. **Não** transferir essa conclusão automaticamente ao projeto CF.

## 8. Próxima prova necessária

- Escolher **dois protótipos rivais** `A/D` (artigos normativos e anexo documental) e `B` (anexo normativo estático), sob a mesma amostra de 4 leis atuais + uma histórica, sem nenhuma revogação promulgada.
- Pesquisar **precedentes e pareceres jurídicos brasileiros diretamente pertinentes** sobre anexos de leis, emendas parlamentares, vetos de tabelas, e integração de remissões na LC95 art. 9º. Classificar a validade **Q** até prova.
- Implementar consistência de identificadores `fonte_versao`, `origem_id`, `destino_id`, `nexo_id`, `suporte_juridico`, `evento_veto`, `data_eficacia`, `status_prova`.
- Executar teste temporal no ramo VET 48/2026 com distinção de itens vetados, atos promulgados e efeitos posteriores, **não** afirmando dependência causal sem prova.
- Encaminhar resultado aos módulos CF-M00.02/M03.01/M14, preservando debates federativos M04 e fiscais M05; **DEC-016** continua pendente.

**Conclusão:** a distinção N/D/P é proposta de governança e técnica **testável**, não hierarquia de fontes juridicamente instituída. A tecnologia não substitui o legislador; e um corpus documental único não basta para entregar o objetivo de **Código formalmente uno**.
