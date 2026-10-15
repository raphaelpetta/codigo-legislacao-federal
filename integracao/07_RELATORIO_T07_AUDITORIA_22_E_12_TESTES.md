# T07 — auditoria do primeiro núcleo (22 unidades) e doze testes aplicados

**ID:** CLF-INT-008. **Data:** 14/10/2026. **Estado:** F5/F6 parciais, revisão jurídica Q. **Base CLF main:** 16fba172c875c7a0de388288fe70005c944021d6. **PR central:** #45 draft; módulo titular T07 PR #39/issue #35. Este documento representa análise jurídica de pesquisa e testes estáticos da minuta, não homologação C0-J nem parecer assinado.

## 1. Fontes conferidas nesta rodada

- Lei 9.784/1999, edição **atualizada** Câmara: https://www2.camara.leg.br/legin/fed/lei/1999/lei-9784-29-janeiro-1999-322239-normaatualizada-pl.html (arts. 1º–17, 26, 38, 41, 49-A, 64–66, 69).
- Edição original Câmara, para conferência histórica inicial dos arts. 1º–17, sem auditoria por fac-símile DOU: https://www2.camara.leg.br/legin/fed/lei/1999/lei-9784-29-janeiro-1999-322239-publicacaooriginal-1-pl.html .
- Lei 14.129/2021 atualizada Câmara, especialmente **art. 2º, arts. 5º–9º e arts. 42–43**: https://www2.camara.leg.br/legin/fed/lei/2021/lei-14129-29-marco-2021-791203-normaatualizada-pl.html .
- STJ **Súmula 633**, aplicação subsidiária a estados/municípios se inexistente norma local e específica: https://processo.stj.jus.br/jurisprudencia/externo/informativo/?livre=%40CNOT%3D017068 .
- STF **Súmula Vinculante 5**, limite à exigência constitucional universal de advogado em PAD: https://portal.stf.jus.br/jurisprudencia/sumariosumulas.asp?base=26&sumula=1199 .

Os testes textuais automatizados abaixo cotejam **texto do CSV da main** contra a **minuta do PR**, e não diretamente os bytes das páginas de Câmara/Planalto. O confronto das normas externas foi feito por leitura jurídica, sem autenticação de fac-símile ou auditoria exaustiva da cadeia de alterações.

## 2. Concordância unitária executada

[05_CONCORDANCIA_T07_22_UNIDADES_20261014.csv](05_CONCORDANCIA_T07_22_UNIDADES_20261014.csv) contém **22 linhas e 22 IDs distintos**, cada uma com dispositivo original, texto integral de origem, destino, texto proposto, delta, risco, testes relacionados, status e fonte. **22/22 textos de destino constam na minuta F5-Q consultada**, com as ressalvas de verificação e classificação jurídica.

Classificações textuais documentadas:
- **15 sem delta local** (art. 2º e incisos), preservação literal na comparação entre CSV e minuta; não C0-J.
- **3 referentes alterados** em art. 1º ('Esta/desta Lei' → 'Este/deste Livro'), potencialmente C1 ou M se alterarem escopo de fato.
- **3 pontos de pontuação** em definições de art. 1º §2º ('órgão -' etc. → dois pontos); ajuste editorial candidato.
- **1 deslocamento e mudança de referente**, art. 69 → LPA-Q-003. Sua colocação antes dos capítulos específicos pode tornar a subsidiariedade mais visível, mas também ampliar o alcance se o futuro Livro for organizado de maneira diversa. Não é C0-J presumido.

O uso do rótulo C0-T local se refere **apenas ao campo textual da amostra**, não à prova de que os 215 registros estão juridicamente substituídos. A totalidade do Livro não foi projetada, numerada ou redigida.

## 3. Resultado aplicado dos doze testes, sem inflar status

[06_TESTES_ADVERSARIAIS_EXECUTADOS_T07_12.csv](06_TESTES_ADVERSARIAIS_EXECUTADOS_T07_12.csv) registra cada hipótese, norma vigente, fato relevante, fragmento proposto, resultado, prova estática e bloqueio. São **testes efetivamente aplicados à amostra** por leitura e marcadores do texto, não julgamento de casos reais nem suíte capaz de certificar C0-J.

| Resultado | IDs | Alcance real |
| --- | --- | --- |
| **Passa apenas no recorte** | G01, G02, G12 | A minuta delimita os demais Poderes ao exercício administrativo e não contém revogação normativa |
| **Passa com ressalva** | G03 | A abrangência federal não invadiu diretamente entes locais; a Súmula 633 e a futura eficácia do Código permanecem em análise |
| **Condicional** | G04, G05 | Subsidiariedade conservada verbalmente; comunicação digital obrigatória não imposta neste recorte, sem prova da convivência completa com normas especiais |
| **Bloqueado** | G06, G07, G08, G09, G10, G11 | Faltam comunicação/ciência, recusa fundamentada de prova, antecedência de diligência, recurso x revisão, contagem contínua e exclusões de decisão coordenada |

**Achado principal:** a minuta não diminui explicitamente direitos do recorte 1º–2º, mas a mera permanência de palavras não impede perdas **pela omissão** dos dispositivos do Livro que lhe conferem efeitos. A mesma preocupação vale para a classificação de 'deste Livro', que não é referência válida até existir corpo normativo com escopo fechado e sistema de remissões consistente.

### Comentário específico sobre governo digital

Lei 14.129, art. 2º, tem âmbito e condições próprias para outros entes, com exclusões. Seus **arts. 5º–6º** regulam a utilização do meio digital e exceções; **arts. 42–43** disciplinam a opção do usuário para comunicações eletrônicas, requisitos das ferramentas e prova de emissão/recebimento *ainda que não de leitura*. Logo, quatro acontecimentos são conceitualmente diferentes: disponibilização, emissão, recebimento no sistema e ciência juridicamente eficaz. O art. 43 não permite, isoladamente e para todo regime especial, equiparar os quatro. É indispensável determinar **norma aplicável, período, escolha do usuário, ferramenta, situação do destinatário e regime específico de intimação** antes de atribuir prazo ou nulidade.

### Comentário federativo

A Lei 9.784 limita seu âmbito básico à Administração Federal e abrange órgãos dos demais Poderes da União na função administrativa. A **Súmula 633/STJ** permite aplicação subsidiária a outros entes sem lei local e específica na matéria — não cria regra federal universal cogente nem licença para suprimir autonomia legislativa local. A redação 'este Livro' deve ser testada contra esse uso subsidiário concreto e a regulação constitucional da legislação federal.

## 4. Fase seguinte F5: direitos, deveres, interessados e competência

A main já possui **40 transcrições** dos arts. 3º–17 da Lei 9.784, em `modulos/T07/M03/CONCORDANCIA_LITERAL_ART3_17_15.csv`. Em vez de copiá-las pela terceira vez, abrir [primeira amostra F5-Q dessas unidades](09_T07_DIREITOS_INTERESSADOS_COMPETENCIA_F5Q.md) e analisar blocos funcionais:

1. **Arts. 3º–4º:** direito de ciência, vista, alegações e assistência facultativa de advogado versus dever de cooperação/boa-fé. SV 5 não elimina direito de assistência, exigências especiais ou contraditório; também não cria advogado obrigatório em todo PAD.
2. **Arts. 5º–8º:** iniciativa de ofício/a pedido, requisitos e saneamento do requerimento, padronização e pluralidade; e interface digital 14.129/2021, preservando atendimento e exceções.
3. **Arts. 9º–10:** interessados titulares, indiretos, associações e direitos difusos; capacidade legal processual e regimes especiais. Não confundir ser titular do direito material com a legitimidade para iniciar/participar.
4. **Arts. 11–17:** competência irrenunciável, delegação parcial, proibições de delegação (normas, recursos, exclusividade), publicidade, revogação, avocação excepcional e competência subsidiária. Agrupar sem omitir essas travas muda o direito.

**Alerta estrutural:** não centralizar regras de competência de todos os Poderes em um órgão ou atribuir à administração federal poderes constitucionais do Legislativo/Judiciário. T07 disciplina o procedimento, sem reformar automaticamente competência orgânica.

## 5. Decisão jurídica e próximo gate

**Nenhuma unidade foi homologada C0-J ou M.** DEC-016 segue pendente. T07 titular precisa avaliar os efeitos do Livro integral; T43 precisa certificar a interface específica de intimações; T01 deve avaliar as regras de promulgação/revogação e o controle de competência. Após o controle 22/22, próximo universo de trabalho são as 40 unidades dos arts. 3º–17, com concordância contextual e redação dentro do mesmo Livro. Não mesclar a branch setorial nem presumir que a minuta concluída é lei vigente.
