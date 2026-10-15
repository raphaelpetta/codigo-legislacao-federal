# Plano diretor operacional do CLF e interface com a CF

**ID:** CLF-OPS-021 · **Data:** 15/10/2026 · **Versão de interface:** COORD-CFCLF-20261015-01 · **Status:** proposta de governança em PR, não decisão normativa.

## Integração sem subordinação
A direção programática compartilhada registra prioridades e dependências; cada repositório mantém decisões, textos normativos e histórico autônomos. Usar [CF-GOV-018](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/blob/main/governanca/18_PLANO_DIRETOR_EXECUCAO.md) apenas como plano transversal quando integrado; `main` de cada projeto é autoridade documental local. CF/1988 continua direito positivo; cenário CF futura não legitima transposição no CLF vigente.

## Produto do CLF
1. Construir cobertura documentada de fontes federais gerais e permanentes, com histórico/temporário/especial mantidos e indexados.
2. Produzir um **corpus codificado único** e normativamente coerente, com direitos/obrigações/procedimentos, regras gerais, exceções, remissões e variantes de reforma claramente identificados; DEC-001 não foi abandonada.
3. Elaborar **plano de positivação autônomo** para o corpus: competências, espécies, iniciativa, sanção/veto, revogações, eficácia temporal e articulação com CF futura sob hipóteses explícitas. DEC-016 permanece pendente.
4. Revisar efeitos de cada transposição (C0/C1/M/Q), garantias e sanções por evidência e classe de risco; nenhum C0 textual equivale automaticamente a C0 jurídico.

## Portas de saída e continuidade
- `MAPEADO` exige fontes/recorte/lacunas; `RECONSTRUIDO` exige versão do direito aplicável e regras interpretativas do recorte; `PROPOSTO` exige minuta e alternativas; `INTEGRADO_PROVISORIO` exige destino/rastreabilidade e interface na versão de trabalho; `AUDITADO_NO_RECORTE` exige provas e testes proporcionais, não mera execução de script.
- A escolha `Q` é resultado legítimo de investigação quando bem delimitada, sem vir a ser automaticamente uma decisão/revogação. Usar `PESQUISA_FOCAL` somente se evidência específica puder alterar solução e justificar custo; senão preparar deliberação e continuar outra unidade.
- A ausência de decisão DEC-016 bloqueia a **promulgação**, não a elaboração de texto experimental e seus metadados, desde que as dependências sejam explícitas e não se simule vigência.

## Fila de frente CLF (revalidável)
1. T07.M03: verificação jurídica por efeitos de transposição e conflitos com especiais; PR #45/#39.
2. T01.M04: concordância da arquitetura única e alternativa de atos de positivação; issue #14/#16.
3. T25.M01: reconstrução e auditagem da Parte Geral penal em PR #32, principalmente preservação de legalidade/garantias.
4. T24.M01: jurisdição, tutela coletiva e sujeitos, com interface CF M06; PR #38.
5. T29.M01/T43.M04: RGPS e digital, respectivamente, sob escopo F0/F1 documentado.
6. T12.M01–02: verificar atualização do CTN pela LC 236/2026 com fontes oficiais; issue #13.

Projetos que dependam de parecer/credencial/dados externos devem mudar de frente sem perder o registro do bloqueio; manter normalmente no máximo duas frentes substantivas CLF ativas e uma interface com CF.

## Inventário e integridade
Catalogar primeiro fonte e versão em dados reprocessáveis; conferir vigência e texto fonte antes de afirmar cobertura. Campos, normalização, controle de duplicatas e lacunas seguem CLF-GOV-017. O overlay `catalogo/04_FRENTES_EM_EXECUCAO.csv` não substitui `03_CATALOGO_MODULOS.csv`, cuja classificação inicial é defasada; avançar para reconciliação auditável e evitar modificar 273 estados por inferência.

## Prestação de contas e revisão
Cada execução deve gerar delta de pesquisa/redação verificável e pequeno handoff, não relatórios vazios. A cada 14 dias medir cobertura por unidade normativa de universo demonstrado, êxito das verificações, PRs reaproveitados, controvérsias encaminhadas e retrabalho. Não certificar conclusão sem denominador, sem revisão jurídica pertinente ou a partir do CI. Ratificação de reforma material, supressão/restrição de garantias e decisão de veículo formal não decorrem de integração documental.

**Situação:** plano em PR; não aprova direitos materiais, legislação ou Constituição; conferir ambos os repositórios ao realizar integração.
