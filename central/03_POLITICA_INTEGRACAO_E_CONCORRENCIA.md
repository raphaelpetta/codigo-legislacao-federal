# Política executiva de integração e trabalho concorrente — CLF
**Natureza:** regra operacional em PR; não é decisão material nem substitui protocolos jurídicos existentes. **Corte:** 15/10/2026.
**Central do projeto:** https://github.com/raphaelpetta/codigo-legislacao-federal/issues/48.
**Interface bilateral:** https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/103.

## Três atos diferentes, dois eixos de estado
1. **PROPOR:** branch/PR com pesquisa, fonte e variante de texto; manter C0-T/C0-J/C1/M/Q separados da maturidade técnica.
2. **INTEGRAR_EXPERIMENTALMENTE:** uma minuta identificada como hipótese e não promulgada pode integrar a **versão de trabalho** após revisão proporcional ao risco, fonte, prováveis efeitos, dependências e testes documentais; não exige ratificação política material automática. Deve preservar no texto e nos metadados o caráter de proposta. Uma revisão documental nunca prova equivalência jurídica.
3. **RATIFICAR_MATERIALMENTE:** ato separado, expresso, identificado e rastreável do usuário, exigido para escolher alterações normativas substantivas como aprovadas. Silêncio, merge técnico, PR aprovado, teste verde ou ausência de objeção não ratificam.

**Regra de segurança:** uma proposta R3 sem fonte, objeção e preservação de garantias verificáveis não entra sequer no produto experimental como versão aparentemente estabilizada; pode permanecer variante em PR ou anexo de trabalho. C0-T nunca significa C0-J; DEC-001 continua objetivo e DEC-016 segue pendente. CI detecta estrutura, não substitui exame jurídico independente. Integrar uma hipótese não equivale a promulgar, revogar ou modificar norma vigente.

## Fonte e painel
- **Produto:** manifesto de Livros produto/fontes/indice_livros.json, arquivo setorial fixado por SHA e vista derivada, enquanto não houver normalização editorial única. Nunca editar apenas a vista gerada; reconciliar a origem e regenerar.
- **Painel:** central/PAINEL_GERADO.csv decorre das fontes do checkout atual; não prova completude e não apaga observações históricas nos quadros manuais. Testar com `python3 scripts/controle_operacional.py --check` ou regenerar via `--write`.
- **Fila:** central/FILA_TRABALHO.csv é a fila de execução e exclusão cooperativa por recorte. Tratar reservas como **advisory locks**, nunca como bloqueios tecnológicos incontornáveis.

## Protocolo de posse, colisão e expiração
- Antes de executar: reler `main` e branch de implantação, PRs existentes, issue central, `FILA_TRABALHO.csv` e SHA-base. A consulta não reserva a tarefa.
- Para RESERVADA ou EM_EXECUCAO registrar responsável identificável, branch, SHA-base e reserva_ate em UTC (`YYYY-MM-DDTHH:MM:SSZ`), **prazo máximo inicial de 24 h**, renovável com entrega/progresso; responsável e reserva não equivalem a exclusividade jurídica nem bloqueio no Git.
- Atualizar arquivo só com leitura prévia do blob SHA e escrita condicional; se o Git rejeitar por conflito, reler e reconciliar, nunca forçar sobrescrita. Não abrir PR concorrente sobre os mesmos IDs/fontes sem conciliação.
- Reservas expiradas são sinalizadas por verificador como aviso operacional, não transformadas automaticamente em CONCLUIDA. A central reavalia e libera explicitamente. Rotina que não consiga gravar **não pode alegar posse**.
- Tarefas em revisão exigem PR e última evidência, concluídas exigem PR/link e resultado. Bloqueios preservam causa e próxima ação. Evitar mais de duas frentes profundas por central e ciclo, preservando distribuição horizontal pelo conjunto.
- As duas centrais são soberanas quanto a seus produtos. Interface CF–CLF = questão com ID, origem, destino, cenário (vigente/proposto), condição e resposta; nunca cópia de decisão de outro projeto.

## Revisão e merge
- PR operacional/documental: comparar com PRs metodológicos anteriores (#46 e #49), verificar links e testes, registrar revisão; não duplicar protocolos ativos.
- PR de proposta experimental: conferir fonte versionada, proveniência, garantia, impacto, concordância, testes e conflitos; integrar com estado experimental explícito. Discussão material ainda aberta aparece em variantes.
- Ratificação material: exige decisão explícita própria. **Não associar merge automático a aprovação constitucional/legislativa.**
- Sem CI disponível: `scripts/controle_operacional.py --check` e os validadores legados devem ser executados por alternativa reproduzível; registrar comando, versão, saída e limitações. Não afirmar testes executados quando não foram. Falha de runner sem steps não demonstra falha do código; separar incidente da integração jurídica.
- Ao encerrar: FEITO/PENDENTE/PRÓXIMO (três candidatos) e SHA/PR, risco, revisão, base, dependências, eventual lock liberado. Reavaliar em 14 dias os resultados, não a quantidade de relatórios.

## Autoridade após merge
A `main` é a referência documental integrada do respectivo projeto, mas **não** a coleção exclusiva de decisões materiais ratificadas: ela pode conter hipóteses expressamente rotuladas. Enquanto esta política estiver em PR, o texto é proposta operacional, não regra já aprovada. Não modificar nenhum dispositivo nem decisões neste PR.
