# Regra de continuidade de cada rodada — Código da Legislação Federal

**ID:** CLF-GOV-018 · **Data:** 14/10/2026 · **Regra operacional:** por solicitação expressa de coordenação do usuário. Complementa `05_PROTOCOLO_DE_TRABALHO.md`, `07_STATUS_E_DEPENDENCIAS.md`, `17_PADRAO_DADOS_E_PROVENIENCIA.md`.  
**Âmbito:** todos os módulos Txx.Myy, estudos de T01, notas CF–CLF, minutas, auditorias, dados e scripts.

## Regra obrigatória

**Depois de CADA trabalho sucessivo com resultado substantivo, registrar sempre:**

1. **FEITO:** entregas comprovadas, origem/destino de normas quando houver, fontes oficiais efetivamente consultadas, arquivos/PR/commit e o que foi ou não incorporado à `main`.
2. **PENDENTE / NÃO VERIFICADO:** lacunas de inventário e concordância, Q em C0/C1/M/Q, alterações intertemporais, dependências, conflitos de PR, decisões não ratificadas, CI e outras incertezas; não apresentar teste sintético como dado empírico real.
3. **PRÓXIMO PASSO:** uma tarefa prioritária executável, com módulo, issue, insumo necessário, entregável e critério objetivo de conclusão; outras tarefas ficam em fila.
4. **COORDENAÇÃO:** proprietário funcional, módulos/interseções, vínculo constitucional atual e CF proposta (se pertinente), estado do CLF/CF, SHAs, repercussões de revogação/veto/competência e pedido de integração.
5. **CONTROLE:** informar status real dos testes no último SHA e distinguir validação estrutural, concordância literal, cobertura normativa, equivalência jurídica e decisão aprovada.

## Ao iniciar

- Conferir `main` atual do CLF, `05_PROTOCOLO_DE_TRABALHO.md`, `04_REGISTRO_DE_DECISOES.md`, `07_STATUS_E_DEPENDENCIAS.md`, cadastro e PRs/branches concorrentes.
- Se houver interface constitucional, conferir também `main` do projeto CF e [quadro de coordenação CF](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/blob/main/governanca/13_QUADRO_DE_COORDENACAO.md). **Não** importar hipóteses H como direito vigente.
- Identificar a versão-base dos estudos e da norma oficial; verificar se outra frente pesquisa a mesma matéria. Não duplicar normas gerais ou substituir arquivo mais recente.
- Separar direito vigente, fonte de legislação consolidada, minuta de Código e anteprojeto de CF.

## Durante

Manter inventário por dispositivo quando a tarefa envolver transposição; vincular cada mudança a origem/destino, categoria C0/C1/M/Q, exceção, subsidiariedade e efeitos revogatórios. A conclusão de um teste documental não prova equivalência jurídico-material, integridade de toda a lei nem autorização de revogação. Encaminhar conflitos para CR/nota de integração versionada; não editar unilateralmente outro título.

## Ao encerrar

- Salvar um **pacote de continuidade**, com as seções FEITO / PENDENTE / PRÓXIMO / FONTES / INTERFACES / SHAs, **na mesma branch/PR**, segundo `modelos/20_PACOTE_CONTINUIDADE.md`. 
- Se a mudança for transversal, acrescentar referência em `governanca/07_STATUS_E_DEPENDENCIAS.md` ou issue, sem substituir o quadro por narrativa antiga.
- Na resposta ao usuário, apresentar explicitamente as três seções, sem prometer trabalho futuro como se já realizado.
- Quando não houver acesso de escrita, entregar o conteúdo e dizer que **não está persistido**.
- Se `main` mudou durante a rodada, comparar/diferenciar e atualizar o pacote. Evitar conflitos por PRs múltiplos.

## Coordenação com a Constituição

A regra CF-GOV-012 e esta regra são **compatíveis no procedimento**, mas mantêm conteúdos e categorias jurídicas independentes. CF é cenário constitucional proposto; CLF é proposta infraconstitucional; direito vigente vem de CF/1988 e atos normativos oficiais. A interface é formal via `docs/09_INTERFACE_CONSTITUCIONAL.md`, `governanca/12_REGISTRO_INTERFACE_CONSTITUCIONAL.md` e pedidos/decisões documentados.

## Critério de qualidade de conclusão

Uma rodada está **documentalmente encerrada** somente se possui entregas reais, pendências ou justificativa de sua ausência, próximo trabalho executável, versões, origem normativa e interfaces quando aplicável. Isso não significa que módulo esteja juridicamente `AUDITADO`, `INTEGRADO` ou `ESTABILIZADO`.

**Fotografia de implantação:** baseline CLF `194bc08931fb24fdc7865e4790401baeef5f1b6d`, e a coordenação CF já foi implantada na `main` por PR #51. Atualizar essas referências quando reutilizadas.

## Adendo de continuidade antitravamento — proposta 15/10/2026

Aplicar [CLF-GOV-020](20_EXECUCAO_CAMADAS_E_AUDITORIA.md) e [CLF-OPS-021](../docs/21_PLANO_DIRETOR_EXECUCAO.md). No FEITO distinguir delta substancial de mera documentação de processo. No PENDENTE identificar se o bloqueio impede positivação, apenas uma variante ou pesquisa; se não impedir outra entrega, registrar próxima opção desbloqueada. Limitar diagnóstico repetitivo de CI já falho a uma nova hipótese técnica por ciclo; na ausência, trabalhar outra frente. Registrar em cada pacote risco R1/R2/R3, maturidade do **recorte**, estado da proposta legislativa e destino das garantias; não impor status de módulo inteiro a partir de pequena amostra. Manter idealmente três opções executáveis independentes e até duas frentes CLF ativas mais interface. A investigação é concluível quando fontes decisivas, alternativas, objeções, efeitos, lacunas e decisão necessária forem delimitados, sem exigir certeza impossível.
