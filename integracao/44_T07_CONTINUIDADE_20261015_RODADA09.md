# CLF/T07 — pacote de continuidade, rodada 09: recursos e revisão (15/10/2026)

**Branch:** `integracao/diagnostico-central-piloto-t07-20261014` | **PR #45** draft | Referência de partida da rodada: `fa91f98f06e6df558286dab0262991ebe8aa8877` | **Sem merge ou alteração da main**.

## FEITO
1. **30/30 subunidades** dos arts.56–65 (incluindo 64-A/64-B) reconciliadas com o espelho integral `25` e Lei9784 consolidada. Todos os 30 destinos têm **zero delta textual local**; **30 C0-T/Q**; **0 C0-J homologado**. [Matriz](40_T07_MATRIZ_30_UNIDADES_RECURSOS_REVISAO_20261015.csv).
2. [32 testes adversariais](41_T07_TESTES_RECURSOS_REVISAO_32_20261015.csv) tratados documentalmente, não como resultados empíricos em autos reais.
3. [Parecer de mérito](42_T07_PARECER_RECURSOS_REVISAO_20261015.md) com SV21, STJ RMS21981, MS11554, especialidade de PAD 8112, Lei11417/2006 e prazos art59/62/66.
4. [Alternativas R0–R5](43_T07_ALTERNATIVAS_RECURSO_E_REVISAO_20261015.md), com propostas novas em categoria **M candidata**, nenhuma decisão ratificada.
5. [Script validador F6](../scripts/validar_t07_f6_recursos_revisao.py) e [workflow CI](../.github/workflows/validar-t07-f6-recursos-revisao.yml) adicionados; teste técnico de proveniência e ausência de homologação.

## GATES ABERTOS
- **C0-J=0**, C1/M aprovados=0, revogações=0. `DEC-001` preserva objetivo de Código único; `DEC-016` pendente.
- Cotejar publicações históricas autênticas em DOU 1999/2006 e regimes especiais, competências recursais, atos eletrônicos de ciência, deposição/caução sob SV21, eventual jurisprudência constitucional específica de penalidades.
- Conferir limites federativos: não universalizar autorização federal art64, nem bloquear direitos recursais locais; caráter especial da Lei8.112 e procedimentos sancionadores.
- Não transformar o §3º de 2006, 64-A ou 64-B em texto originário de 1999. Não fazer do §2º art56 licença de violar SV21.
- **Não** agravar revisão art65 usando o rótulo de recurso art64; não tratar como revisão art65 simples reexame de benefício não sancionatório.

## PRÓXIMO CICLO PROPOSTO
F6 de **arts.66–69-A** (contagem de prazos, prorrogação, vedação de suspensão, sanção, subsidiariedade e prioridades), mais auditoria de efeitos intertemporais e regime de atos digitais. Receber T07/T43/T25/T24/T01 para parecer de interfaces; não registrar reforma nem C0-J enquanto os gates não forem satisfeitos.

**Nota técnica:** validação CI comprova apenas consistência das matrizes versionadas, nunca autenticidade DOU ou mérito jurídico; conferir execução para o HEAD antes de falar de CI aprovada.
