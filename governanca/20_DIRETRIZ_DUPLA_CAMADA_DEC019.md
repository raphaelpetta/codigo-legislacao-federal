# CLF-GOV-020 — Diretriz preparatória da dupla camada (DEC-019)

**Adotada:** 16/10/2026 · **Decisão:** DEC-019 — alternativa A da QD-2026-004, ratificada expressamente pelo usuário. **Estado:** FC2 apenas para a escolha de arquitetura preparatória; **DEC-016 PENDENTE**. **Unidade:** DEC-001 continua objetivo confirmado.

## 1. Regra de trabalho — duas camadas, autoridades diferentes

**Camada E — Código editorial único experimental.** A elaboração mantém um corpo integrado por títulos, módulos, IDs estáveis, fontes oficiais datadas, versões, remissões, histórico, concordância origem/destino e redações propostas C0-T/C1/M/Q. Texto em `main` ou PR experimental não promulga, revoga, altera ou transporta por si só nenhuma norma. A integração de `Q` continua possível sem FC2/FC5.

**Camada P — trilhas de possível positivação futura.** Para cada recorte a converter em direito positivo, manter ficha própria de **espécie formal e reserva material, competência, titular da iniciativa, quórum, emendas/veto, autoridade de sanção/promulgação, forma e enumeração de revogações, atos de origem que permanecem, vacatio/vigência, transição, interfaces, alteração posterior e grau de evidência**. A existência de ficha **não decide** que determinado veículo é juridicamente possível: classificar `A_VERIFICAR`, `HIPOTESE_CONDICIONADA` ou `APTO_A_EXAME_JURIDICO` somente com fundamento. `VEICULO_CONFIRMADO` exige deliberação própria e autorização adequada, não decorre de DEC-019.

**Ligação E→P:** um mesmo dispositivo de origem poderá alimentar um ou mais destinos editoriais; o veículo futuro dependerá da matéria, e jamais será inferido do simples Título editorial. Conservar relação N/D/P: N = eventual conteúdo realmente aprovado por ato competente; D = rastreio e concordância não normativa; P = registro de eventos e versões. Uma planilha editorial dinâmica **não é** anexo normativo promulgado nem cláusula de revogação.

## 2. Invariantes e impedimentos

1. **DEC-001 intocada:** buscar o Código único editorial e pesquisar a viabilidade de unidade **formal** futura. A opção pela dupla camada **não** ratifica dispersão legislativa como resultado definitivo. Registrar dívida de unidade formal e condicionantes da DEC-016.
2. **DEC-016 permanece PENDENTE:** não selecionar universalmente lei complementar, lei ordinária, emenda constitucional ou outro instrumento; não pressupor possibilidade de instrumento de iniciativa mista, revogação cruzada ou anexo normativo dinâmico.
3. **Portas A/B/C:** fonte oficial e seu corte temporal; equivalência textual/estrutural e remissões; proteção material e formal proporcional R1–R3. `C0-T` ou hash idêntico não prova `C0-J`. Reforma `M` demanda ratificação expressa independente.
4. **Reserva de espécie/iniciativa:** CF/1988 arts. 59, 61, 66, 69, 96, 146 e demais reservas pertinentes sempre examinadas pelo efeito do recorte. LC 95/1998 arts. 7, 9, 13 e 14 não autorizam, por si só, reedição legislativa substitutiva de qualquer matéria constitucionalmente reservada.
5. **Sem revogação presumida:** exigir texto de revogação deliberado e promulgado pelo procedimento competente; norma original permanece referência aplicável até que evento legal efetivo se prove. Não deduzir revogação de ausência no CLF, ficha, índice ou arquivo.
6. **Proibição de atalhos:** aprovação da DEC-019 não estabiliza automaticamente redação (`FC3`), não é auditoria jurídica independente (`FC4`), não integra anteprojeto deliberado (`FC5`), não valida veículo definitivo e não resolve eventual transição.
7. **Interface CF:** tratar a CF/1988 como direito vigente e a CF proposta em repositório separado como cenário **condicionado**; encaminhar dependência específica sem importar decisões.

## 3. Implementação por recorte

Ao iniciar um lote, (a) identificar fonte e recorte; (b) gerar/manter o espelho experimental na Camada E; (c) preencher a [ficha de trilha de positivação](../modelos/21_FICHA_TRILHA_POSITIVACAO.md) na Camada P; (d) indicar expressamente `A_VERIFICAR` para toda informação formal não comprovada; (e) explicar o que permanecerá **fora** do Código positivo e não será revogado se o veículo não for válido; (f) validar concordância e gatilhos temporais; (g) submeter **nova questão decisória específica** quando houver alternativas maduras, usando fila DEC-018. As trilhas podem ser preparadas antes de F9; isso não supera portas A/B/C.

Como demonstração inicial, [T05.M06 arts. 1º–2º](../modulos/T05/M06_TRILHA_PREPARATORIA_DEC019_ART1_2_Q.md) contém ficha **Q** sem veículo escolhido. Não generalizar esse recorte para todo o T05, nem convertê-lo em homologação.

## 4. Primeiro horizonte de implementação e riscos

**Critério H/V/I/D/F:** priorizar o ganho marginal global entre abrir novos recortes, sanar fontes, integrar lotes, deliberar sobre dúvida e fechar redação **já aprovada**. A diretriz permite melhor identificação de reservas formais e dos efeitos antes de acumular transcrições; não cria quotas nem paralisa a pesquisa.

**Risco adversarial principal:** o corpus editorial permanecer indefinidamente a única versão do Código, afastando a promessa de DEC-001. Mitigação: a fila central mantém `QD-2026-001`/DEC-016 pendentes, e cada trilha indica obstáculo concreto, cenário formal possível e **próxima evidência**, sem encobrir déficits com aparência de texto promulgável.

**Reabertura:** fatos jurídicos novos, erro de premissa, conflito constitucional ou alternativa preparatória superior podem justificar revisão expressa de DEC-019 nos termos de CLF-GOV-019. A simples evolução editorial não revoga a decisão.

## 5. Proveniência da aprovação

A declaração literal do usuário foi **“Aprovo expressamente a alternativa A da QD-2026-004 como diretriz preparatória do CLF, preservadas a DEC-001 e a pendência da DEC-016.”** Esta decisão foi dada diretamente neste diálogo e transcrita na [issue central #48](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/48#issuecomment-6228937676); o comentário é **registro secundário**, não fonte primária autenticada do chat. O registro [DEC-019](04_REGISTRO_DE_DECISOES.md) e a [fila QD-2026-004](19_FILA_QUESTOES_DELIBERAVEIS.json) guardam o mesmo alcance.

**Referências:** [protocolo progressivo](19_PROCEDIMENTO_CONSTRUCAO_DELIBERACAO_FECHAMENTO.md), [política A/B/C](POLITICA_CONSOLIDACAO_E_FECHAMENTO_20261015.md), [dossiê QD-2026-004](../modulos/T01/M04/DOSSIE_DEC016_QD004_PREPARACAO_JURIDICO_FORMAL_20261016.md), [modelo de ficha](../modelos/21_FICHA_TRILHA_POSITIVACAO.md).
