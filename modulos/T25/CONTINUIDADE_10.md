# T25 — Continuidade 10: teste de dez casos e controvérsia do CPM art.35

**Data/corte:** 14/10/2026, America/Sao_Paulo. **T25.M02/M03**. **Issue [#31](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/31)**; **PR [#32 — rascunho](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/32)**; **branch** `modulo/T25-parte-geral-f0-f1`.

**Versões:** CLF `main` checada à abertura e após pesquisa: `16fba172c875c7a0de388288fe70005c944021d6` (não alterada por esta rodada). HEAD anterior da branch após ciclo09: `7d6379414d14446d07bef9978eeb190426e7fbf1`. CF alternativa `main` consultada **apenas para versão, não para importar normas**: `2a770a8136f8ca4877e865be3e3b7745a6d4b168`. Último HEAD e CI deste ciclo devem ser verificados após gravação. Não foi feito rebase, merge ou edição de arquivos centrais.

## 1. FEITO (na branch, não na main)

| Entrega | Evidência | Categoria e limite |
|---|---|---|
| 10 fatos controlados: direito vigente × A × B, sendo 9 hipotéticos e 1 referência a caso real STM | `CASOS_COMPARADOS_VIGENTE_A_B_CICLO10.csv` | 10 registros únicos; direito positivo reconstruído condicionalmente; nenhuma sentença contrafactual inventada |
| 12 lacunas e alterações materiais identificadas nas minutas A/B | `AUDITORIA_SEMANTICA_MINUTAS_AB_CICLO10.csv` | REV10-01–12, riscos M ou Q, correções alternativas e travas |
| Cotejo CPM arts.35,73,76,77 e CP arts.21,65–68 com STF Tema158/STJ 2024 | `DOSSIE_10_CASOS_E_DOSIMETRIA_A_B.md` | CPM77 PU de 2023 novo achado; STF Tema158 não julga especificamente CPM35 |
| Identificação de M implícita na A: transformação de redução facultativa do erro evitável em obrigatória | PA3 do ciclo09 × CP21 | `reduzirá` versus `poderá diminuí-la`; correção ou deliberação expressa |
| Índice e continuidade | `README.md` e este arquivo | documentação, sem texto promulgável aprovado |

**Fontes efetivamente verificadas em 14/10/2026:** [CPM Câmara atualizado, arts.35 e 69–77](https://www2.camara.leg.br/legin/fed/declei/1960-1969/decreto-lei-1001-21-outubro-1969-376258-normaatualizada-pe.html), [CP Câmara atualizado, arts.20–25 e 65–68](https://www2.camara.leg.br/legin/fed/declei/1940-1949/decreto-lei-2848-7-dezembro-1940-412868-normaatualizada-pe.html), [Lei 14.688/2023, publicação Câmara 21/09/2023](https://www2.camara.leg.br/legin/fed/lei/2023/lei-14688-20-setembro-2023-794728-publicacaooriginal-169356-pl.html), [STF Tema158, tese literal](https://portal.stf.jus.br/jurisprudenciaRepercussao/verAndamentoProcesso.asp?classeProcesso=RE&incidente=2663001&numeroProcesso=597270&numeroTema=158), [STJ Informativo823, REsp 1.869.764/MS, 3ª Seção 14/08/2024](https://processo.stj.jus.br/jurisprudencia/externo/informativo/?acao=pesquisarumaedicao&aplicacao=informativo.ea&l=10&livre=%270823%27.cod.&refinar=S.DISP.). [STM Ap 7000232-60.2024.7.00.0000 em revista institucional](https://revista.stm.jus.br/index.php/periodicos/article/download/jurisprudencia-05-v34-n1-2024/88/238), **leitura integral e verificação visual efetuadas no ciclo09**, apenas os resultados já documentados foram cotejados nesta rodada. Não foi afirmada nova leitura de inteiro teor de outros julgados.

**Resultados qualificados:** maioria STM reduziu CPM35 abaixo do mínimo até 9 meses e 18 dias de detenção; divergência da dosimetria fixaria 1 ano de reclusão; espécie e natureza da redução importam. CPM73 (piso para atenuante), CPM76 (exceção para minorante) e CPM77 PU acrescido em 2023 tornam imprescindível definir natureza legal da mitigação. Nem STF Tema158 nem STJ Súmula231 resolvem por si sós se CPM35 é genérica/atenuação própria/minorante especial.

## 2. PENDENTE / NÃO VERIFICADO

- **F5-EXP incompleta:** não há minutas A2/B2 ou redação ratificada; PA3 traz mudança M de faculdade para obrigação não justificada; PA7 §2 sem intervalo/piso; PA9 PU prometeu regra militar ainda não formulada; PB2 §2 delegou classificação do erro a regra ausente; PA5 amplia beneficiários de exculpação; PB5/PB6 dependem de jurisprudência de coação/necessidade.
- **F6 jurídico:** nenhuma equivalência C0-J; 10 testes evidenciam resultados indeterminados justamente nos pontos sensíveis.
- **História:** faltam DOU original e retificações do CPM de 1969/2023, e DOU 1984 Lei 7.209 já localizado em outro ciclo, mas imagens não conferidas. Lei 14.688/2023 possui anotação de retificação em 27/09/2023 na ficha oficial; verificar eventual pertinência antes de cotejo autêntico.
- **Constituição e direitos:** não demonstrado controle exaustivo das normas CPM35/40/42PU/45PU sob CF/1988, nem tratados nem efeitos civis, processuais e de execução.
- **Penas e tipos:** falta confronto dos dispositivos hierárquicos especiais aplicáveis ao CPM47 e todo o sistema de sanções T25.M03; não foi atribuído quantum a fatos fictícios sem tipo e faixa penal definidos.
- **Modelos A/B/C:** nenhuma decisão aprovada, nenhum dispositivo revogado ou incorporado à `main`; `DEC-016` segue Q; CF em projeto independente.
- **QA:** checar GitHub Actions do último commit; aprovação estrutural não significa constitucionalidade ou equivalência semântica.

## 3. PRÓXIMO PASSO EXECUTÁVEL

**T25 — ciclo 11:** redigir revisões **A2 e B2** com duas escolhas alternativas marcadas quanto ao erro evitável de P-A3 (`poderá` manter o direito comum versus `reduzirá` como reforma M), e quanto à **mitigação por CPM35**: atenuante sob piso ou minorante especial com fração/piso determinados. Especificar a qualidade CPM47 II, a natureza de excesso doloso CPM46, e os requisitos de força de comando CPM42 PU. Não fazer escolha M definitiva em nome do usuário.

**Critério de aceite:** reexecutar os dez mesmos casos P10-01–10 sob A2/B2, registrar resultados determináveis e pontos Q, distinguir temporalidade de lei nova benigna/gravosa e propor matriz de concordância frase por frase com fontes oficiais. Se houver efeitos irredutíveis sem sistema de pena completo, iniciar T25.M03 especificamente para arts.69–77 CPM / 59–68 CP, sem transformar hipótese em aprovação normativa.

## 4. COORDENAÇÃO E CLASSIFICAÇÃO

Módulos: T01 (decisão de veículo normativo e vigência), T02/CF atual (garantias), T16 (efeitos civis), T25.M01/M02/M03, T26 (competência/prova), T27 (execução), T45 (hierarquia), T23/T47/T48 (direito internacional). **C0-T** só para fonte compilada CP1–12 em ciclo03, não CPM; **C0-J não demonstrado**; **C1 não aprovado**; alterações **M observadas, não deliberadas**; restante **Q**.

- [x] `main`/PR/branch e versão independente CF conferidas.
- [x] 10 casos, 12 erros/lacunas e nova referência CPM77 registrados.
- [x] Fatos reais versus hipotéticos, texto vigente versus minuta, e certeza versus hipótese separados.
- [x] FEITO/PENDENTE/PRÓXIMO registrados.
- [ ] Último SHA e CI GitHub Actions, registrar na PR.

**Protocolo:** `governanca/18_PROTOCOLO_CONTINUIDADE_POR_RODADA.md`.
