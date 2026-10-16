# T07.M03 — juízo jurídico crítico F2/F6: instrução, prova e participação (arts. 29–47)

**ID:** CLF-INT-024. **Corte:** 15/10/2026. **Estado:** `F5-Q` com testes estáticos de regressão; não é parecer de equivalência C0-J e não promulga um Código federal. DEC-016, reserva de espécie e eficácia intertemporal mantidas em Q.

**Fonte:** [Lei9.784/1999, arts29–47, atualizada pela Câmara](https://www2.camara.leg.br/legin/fed/lei/1999/lei-9784-29-janeiro-1999-322239-normaatualizada-pl.html). Inventário do módulo T07 `MATRIZ_TRIAGEM_215_UNIDADES_CICLO20.csv` na main do repositório. [Concordância local 28/28](21_T07_CONCORDANCIA_ART29_47_28_UNIDADES.csv), [texto v3](22_T07_LIVRO_SEQUENCIAL_ARTS1_47_69_F5Q_V3.md) e [15 cenários](23_T07_TESTES_INSTRUCAO_15.csv). O número 28 é o total de unidades (caputs e parágrafos) dos 19 artigos da faixa, **não** número de artigos; nenhum desses 28 recebeu C0-J.

## Quatro erros codificadores concretos que precisam ser bloqueados

### 1. Ônus do interessado NÃO extingue atuação instrutória de ofício

- Art29: a Administração desenvolve a instrução e o interessado pode propor atividade probatória.
- Art36: o interessado prova os fatos alegados, **sem prejuízo** do dever instrutório do órgão e do art37.
- Art37: diante de documentos existentes na própria Administração ou em outro órgão, a autoridade **os obtém de ofício**. Ignorar esse dever cria indevido ônus da parte de reentregar o que o Estado já possui.
- Art38 §§1–2: elementos probatórios precisam constar da motivação, e indeferimento de prova só pode ocorrer por **decisão fundamentada** diante de prova ilícita, impertinente, desnecessária ou protelatória.

**Transposição:** art36 continha remissão `art. 37 desta Lei`. A minuta v3 registra substituição contextual para `art. 37 deste Livro` em *uma* unidade, classificada **C1 potencial/Q**, nunca igualdade literal automática. Tanto a remissão quanto a numeração final do Livro são hipóteses.

**Proibição:** não adotar artigo genérico "incumbe ao administrado produzir todas as provas, podendo a autoridade indeferi-las livremente". É **M regressiva** e contrariaria a Lei9.784 vigente.

### 2. Falta de documento NÃO é sempre arquivamento

Art39 determina intimação de interessados/terceiros para informações ou provas necessárias e prevê que, no silêncio, a Administração pode suprir a omissão de ofício, **sem se eximir de decidir**. Art40 tem objeto diferente: ausência de dados, atuações ou documentos solicitados e **necessários à apreciação de pedido formulado**, após prazo fixado, conduz ao arquivamento. Não confundir processo de ofício, prova de terceiros, pedido e pressupostos de admissibilidade; certificar a motivação e eventual possibilidade de saneamento.

**Cenários P08/P09:** a primeira afirmação foi preservada no recorte, a segunda fica **condicionada aos fatos**. Nenhuma regra de confissão ficta decorre dos dois artigos.

### 3. Parecer vinculante × não vinculante tem efeito processual oposto

Art42: parecer obrigatório com prazo geral de até **15 dias**, ressalvadas norma especial/necessidade comprovada. **§1º:** se obrigatório **vinculante** não for emitido no prazo, processo **não prossegue** até apresentação e há responsabilidade pelo atraso. **§2º:** se obrigatório **não vinculante** não for emitido, processo **pode prosseguir e ser decidido com sua dispensa**, sem prejuízo de responsabilização do omisso. Art43 determina solicitar novo laudo técnico a órgão com qualificação/capacidade equivalentes quando falhar o encargo de laudo no prazo.

**Proibição:** condensar em "na ausência de parecer, o processo prossegue", ou "na ausência de parecer, todo processo para"; ambas são incompatíveis com a distinção positiva.

### 4. Contraditório, cautela, acesso e sigilo NÃO são blocos permutáveis

Art41: prova/diligência com **3 dias úteis** de antecedência. Art44: direito a manifestar-se **em até 10 dias**, salvo prazo diverso legalmente fixado, depois da instrução. Art45: cautelar sem audiência prévia apenas em **risco iminente**, mediante **motivação** (não afastar controle posterior). Art46: direito à vista e cópias preservando dados de terceiros protegidos por sigilo, privacidade, honra e imagem. Art47: órgão instrutor distinto do decisor encaminha **relatório e proposta objetivamente justificada** à autoridade competente.

Interferências T43 digital, LGPD e LAI devem ser descritas com competência e direitos externos, sem desfigurar o art46 nem bloquear em massa acesso aos autos por mero rótulo de confidencialidade.

## Consulta e audiência: participação não faz alguém automaticamente parte

Art31 §2º: a pessoa que participa de consulta pública **não se torna interessado processual apenas por isso**, embora tenha direito a resposta fundamentada, eventualmente comum a alegações substancialmente iguais. Art32 audiência é faculdade antes da decisão conforme relevância; arts33–35 preveem outros canais, registro dos resultados e ata em audiência interorgânica conjunta. Não criar direito material novo de participação com efeito vinculante geral e não eliminar a resposta fundamentada prevista em lei.

## Resultados e interfaces

Dos **15 testes hipotéticos**, **10 preservam o enunciado no recorte**, **2 passam com ressalva** (remissão de art36; medida cautelar), **3 são condicionais a fatos/qualificações jurídicas** (arquivamento art40, parecer art42 e sigilo art46). Essas classificações **não** derivam de quinze processos reais, nem demonstram igualdade de efeitos no veículo codificado.

| Item de controle | Resultado nesta rodada |
| --- | --- |
| Posições da Lei 9.784 documentadas nesta faixa | 28/28 |
| Total acumulado no Livro experimental v3 | **123/215** |
| Artigos sequenciais locais (1º–47, mais art.69) | **48** |
| Remissões lexicais nesta nova faixa | uma, art36 → art37 deste Livro |
| Unidades remanescentes no inventário total | **92** |
| Gate C0-J material e DEC-016 | **abertos (Q)** |

**FEITO:** concordância completa da faixa, texto sequencial conservador, testes documentais e enumeração de regressões proibidas. **PENDENTE:** prova de que o Livro completo preserva resultados, revisão das leis especiais, fac-símile DOU e interfaces orgânicas e digitais, formalização do Código e homologação material. **PRÓXIMO:** lei positiva arts48 em diante: dever de decidir, decisões coordenadas, motivação, recursos, decadência e prazos; antes de afirmar substituição integral, auditar 215/215 unidades e efeitos de cada regime temporal.

**Dependências:** módulo T07/M03 é dono; T43/M04 para interoperabilidade, logs, direitos de acesso e dados; T01 para DEC-016 e regulação normativa, T24 para distinção do CPC, T10 para sanção. CF vigente é base de controle; CF futura não é direito positivo.
