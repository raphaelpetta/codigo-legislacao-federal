# T01.M04 — Quatro redações rivais de cláusula revogatória: M0–M3

**ID:** CLF-T01-M04-MIN10 · **Estado:** MINUTAS EXPERIMENTAIS NÃO APROVADAS, destinadas a teste de veto; CF/1988 e LC95 são direito vigente, estas cláusulas **não**.  
**Origem:** `TESTE_10_UNIDADE_TEXTUAL_VETO_V1.md`.  
**Dados:** substituto `S`, fonte antiga `A`, revogação `R` são símbolos de teste; em proposição legislativa real, substituir por identificação de **lei, artigo, redação, competência e data**; jamais promulgar texto com placeholders.

## M0 — Revogação no caput; condição no parágrafo (controle negativo)

**Art. R.** Fica revogado o art. A da Lei nº F, de ANO.

**Parágrafo único.** A revogação estabelecida no caput somente produz efeitos quando entrar em vigor o art. S desta lei.

**Resultado simulado:** se o parágrafo único for vetado, o comando revogatório do caput fica sem sua condição original — risco crítico. **Não selecionar** M0 como modelo.

## M1 — Revogação e condição em artigo indiviso (hipótese positiva, versão inicial)

**Art. R.** O art. A da Lei nº F, de ANO, fica revogado a partir da entrada em vigor do art. S desta lei, considerado o texto efetivamente promulgado e as regras transitórias expressas desta lei.

**Resultado simulado:** o veto parcial não pode suprimir apenas a condição sem vetar a unidade inteira deste artigo **sem subdivisões**. Mas não obriga que S seja promulgado, não impede S parcialmente vetado e não atribui competência para o Código formal uno.

**Revisão necessária:** "considerado o texto efetivamente promulgado" não é uma prova de equivalência jurídica; se S for parcialmente vetado, o art. S pode conservar parte vigente insuficiente. Depurar a remissão para subunidades indispensáveis.

## M2 — Revogação e condição em artigos indivisos pequenos, um para cada unidade S (hipótese preferencial de teste adversarial)

**Art. R1.** Fica revogado o inciso A1 do art. A da Lei nº F, de ANO, na data em que entrar em vigor o texto integral do inciso S1 do art. S desta lei, se esse inciso tiver sido promulgado segundo o procedimento competente.

**Art. R2.** Fica revogado o inciso A2 do art. A da Lei nº F, de ANO, na data em que entrar em vigor o texto integral do inciso S2 do art. S desta lei, se esse inciso tiver sido promulgado segundo o procedimento competente.

**Resultado simulado:** remissões e dependências menores limitam impacto de veto de outra subunidade e evitam declaração de revogação por gatilho genérico. **Mas** o processo legislativo, a distinção entre promulgado/eficaz, a eventual invalidade futura, a transição e a revogação tácita ainda exigem auditoria. Condições como "promulgado segundo procedimento competente" podem demandar exame jurídico em litígio, **não** declaração constitutiva de editor do CLF.

## M3 — Revogação incondicional, metadado condicionado (controle negativo)

**Art. R.** Fica revogado o art. A da Lei nº F, de ANO.

**Nota editorial externa (sem valor promulgado):** "Revogação de A será considerada eficaz apenas depois de S".

**Resultado:** nota editorial não pode criar condição que a lei não contém. **Não selecionar** M3.

## Microteste de integridade

| Pergunta | M0 | M1 | M2 | M3 |
|---|---|---|---|---|
| Veto só da condição pode deixar R sem condição? | **Sim** (parágrafo) | **Não**, em artigo indiviso | **Não**, em cada artigo indiviso | Condição nunca existiu como lei |
| Veto de S pode afetar continuidade? | Sim | Sim, mitigado por R condicional | Sim, mitigado por unidade S específica | Sim, R incondicional |
| S parcialmente promulgado pode disparar R incorretamente? | Sim | **Sim, risco residual central** | Menor se unidade S realmente indispensável e integral | Sim |
| Derrubada posterior de veto demanda cálculo temporal? | Sim | Sim | Sim | Sim |
| Editor ganha poder de decidir revogação? | Não, se lei completa | **Proibido** | **Proibido** | Nota não vinculante |
| Soluciona iniciativa e espécie do Código uno? | Não | Não | Não | Não |

**Caveat jurídico geral:** o princípio de não repristinação automática da LINDB art. 2º §3º precisa ser separado de `R nunca teve eficácia` por cláusula suspensiva. Não inventar restabelecimento de lei válida revogada por anotação de portal.

**Juízo limitado:** **M1 e M2 avançam no teste de divisibilidade do veto**, mas a prova de validade final exige vetos parciais de S, cronologia real, equivalência do texto, competência, iniciativa e auditoria adversarial. Nada homologado. `DEC-016` pendente.
