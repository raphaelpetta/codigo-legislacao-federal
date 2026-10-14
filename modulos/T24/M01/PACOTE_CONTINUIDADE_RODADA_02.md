# T24.M01 — Pacote de continuidade da rodada 02 (F1-A)

**Data de corte:** 14/10/2026 · **Responsável:** frente especializada T24.M01 · **Issue:** [#37](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/37) · **PR:** [#38 draft](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/38).  
**CLF main início e rechecagem:** `16fba172c875c7a0de388288fe70005c944021d6`. **CF main apenas identificada (sem auditoria integral nesta rodada):** `f6b95d977bfe293fd393972d499ca5d1965a1bcd`.  
**Branch:** `modulo/T24-M01-jurisdicao-sujeitos-f0-f1-20261014`. **Commits documentais desta rodada antes do pacote:** `bd0b90797e3c193752fba25b5224ff39d04f0e5b`, `bbad6961ec9db9fe0eaacd01881b15599d73ff11`, `278090a2ecff227b47dc957b079154359e5cc4b4`.

## FEITO

| Entrega | Arquivo e estado | Prova e qualidade |
|---|---|---|
| Cotejo manual dos 20 arts. 1º–20 e 28 arts. 42–69 do CPC = **48 artigos**, com função, interface, possível destino primário e ressalvas | [F1A_MATRIZ_48_ARTIGOS.csv](F1A_MATRIZ_48_ARTIGOS.csv); branch PR #38 | Publicação original e consolidada da Câmara de 14/10/2026; não equivalência C0 |
| Discriminação de **98 unidades subordinadas**, inclusive parágrafos, incisos e alíneas relevantes | [F1A_SUBUNIDADES_01-20_42-69.csv](F1A_SUBUNIDADES_01-20_42-69.csv); branch | Verificação estrutural simples por leitura dos arquivos: 48 registros na sequência prevista; 98 IDs de subunidades sem repetição; quatro mudanças textuais marcadas |
| Identificação das quatro alterações textuais em três artigos: **12 caput**, **53 I d**, **63 §1 e §5** | [RELATORIO_F1A_COTEJO_E_EFEITOS.md](RELATORIO_F1A_COTEJO_E_EFEITOS.md); branch | Lei 13.256/2016; Lei 13.894/2019; Lei 14.879/2024; cotejo manual nas fontes originais |
| Diferenciação de interpretação constitucional e alteração textual: **46 §5, 52 parágrafo único, 53** | Idem; branch | STF ADIs 5.492/5.737 e 6.792/7.055; notícia e andamento oficiais, **inteiro teor pendente** |
| Intertemporalidade do **art. 63**: CC 206.933/SP | Idem; branch | STJ Segunda Seção 2025; informativo oficial; restrição do regime novo a ações posteriores a 04/06/2024 |
| Proposta **provisória** de distribuição T24.M01 / T24.M02 / T01 / T23 | Matrizes e relatório | Integração/ratificação central ainda requerida |

**Procedência e data de leitura (14/10/2026):** publicação original e atualizada da Lei 13.105/2015 (Câmara), compilação do Planalto (seleção), Leis 13.256/2016, 13.894/2019 e 14.879/2024 (texto do ato modificador), STF decisões referidas (andamento e notícia, não inteiro teor), STJ Informativo 842 (tese CC 206.933/SP). URLs integrais e alcance da consulta constam no [relatório](RELATORIO_F1A_COTEJO_E_EFEITOS.md).

**Matriz de mudanças:** apenas mudanças legislativas pré-existentes encontradas; **nenhuma alteração C0, C1 ou M redigida no CLF**, nem revogação planejada. Questões Q registradas.

## PENDENTE / NÃO VERIFICADO

| Pendência | Requisito de conclusão | Bloqueio |
|---|---|---|
| Ausência de registro literal original/atual de todas as unidades | Exportação textual fiel, versionada, teste automatizado de diferenças e validação do DOU em caso de divergência | C0/C1 |
| Históricos completos de leis e possíveis alterações não sinalizadas na compilação | Auditoria da cadeia modificativa, inclusive veto/republicação/efeitos temporais | F1 exaustivo |
| STF ADIs 5.492/5.737 e 6.792/7.055 | Dispositivos de acórdãos, modulação, extensão subjetiva/objetiva | Integração constitucional |
| Art. 63 e aplicação temporal da Lei 14.879/2024 | Conferir a ementa e inteiro teor do CC 206.933/SP e decisões mais recentes; publicação em 05/06/2024 | Parecer F2 completo |
| Classificação final art. 12 em T24.M02; art. 13 em T23; arts. 14–15 em T01 | Deliberação central após confronto com T01 e T23 | Arquitetura CLF |
| Interface constitucional futura | Ler CF main atual, não somente SHA; comparar garantias e organização da Justiça com CF/1988 | Cenário B condicional |
| CI/validação jurídica | Checks no SHA final, revisão adversarial e concordância por dispositivo | Merge e estabilização |

**Estado do módulo:** F0 realizada; F1-A documental avançada, F1 global parcial; F2–F8 ainda não concluídas; status global **PLANEJADO**, não `INVENTARIADO`.

## PRÓXIMO (tarefa prioritária)

**T24.M01 — F1-B, sujeitos e representação: CPC arts. 70–81 e 98–102**, com localização e verificação do acervo normativo especial da gratuidade, capacidade processual, intervenções do MP/Defensoria e acesso.  
**Entregável:** inventário por unidade, versão original/atual, alterações materiais, efeitos STF/STJ e remissões T06/T13/T32/T24.M02.  
**Critério de aceite:** texto completo de todas as unidades do recorte mapeado; ausência de omissão de alteração, destino e direitos protetivos; quadro de normas especiais; testes de competência e reserva de espécie.  
**Fila:** F1-B outros arts. 82–187; T23 arts. 21–41; confirmação dos acórdãos constitucionais e histórico integral das alterações aqui detectadas.

## COORDENAÇÃO

- **Versão/proveniência:** CLF main baseline `16fba17…`; PR #38 contém arquivos ainda não integrados. Não presumir sincronização automática das Fontes do projeto.
- **Módulos afetados:** T01.M01/M04; T03; T06; T12; T13; T17; T19; T20; T23; T24.M02/M03/M04/M05/M06/M07; T32. Sem editar outros módulos.
- **CF/1988:** cenário A do vigente; **CF proposta:** cenário B futuro, ainda não cotejado nesta rodada. Interfaces antigas IC-2026-003/013/014/023/027/028 são referências condicionais, não decisões aprovadas.
- **Controle automatizado local de dados:** 48 linhas sequenciais corretas + 98 IDs únicos de subunidades + quatro referências de alteração detectadas; valida apenas estrutura dos CSVs.
- **CI oficial do PR:** a verificar no SHA terminal; não declarar sucesso por ausência de relatório. **Sem merge** e **sem aprovação material**.

- [x] Consultei main e PR em aberto antes de escrever.
- [x] Classifiquei revisões legislativas versus interpretações judiciais.
- [x] Registrei fontes, cortes, destinos provisórios e lacunas.
- [x] Produzi FEITO/PENDENTE/PRÓXIMO na branch.
- [ ] Confirmei equivalência literal de cada subunidade por cotejo automatizado/DOU.
- [ ] Concluí F1 global e concordância.
- [ ] Recebi decisão arquitetural ou material do usuário.
