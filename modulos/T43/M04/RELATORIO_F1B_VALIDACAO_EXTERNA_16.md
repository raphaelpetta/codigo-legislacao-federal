# T43.M04 — F1-B: resultado da validação externa das 16 unidades focais
**Corte:** 14/10/2026. **Issue #42, PR #43 draft.** O [validador `scripts/validar_t43_f1a_16.py`](../../../scripts/validar_t43_f1a_16.py) foi executado com `.github/workflows/validar-t43-f1a.yml` por meio de consulta externa à [Câmara, Lei 14.129/2021 consolidada](https://www2.camara.leg.br/legin/fed/lei/2021/lei-14129-29-marco-2021-791203-normaatualizada-pl.html). **Esta validação não constitui certificação DOU, histórico normativo, C0-J ou ratificação R2.**

## Prova reproduzível
- [Execução CI #38554726682](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38554726682): job `texto_t43` aprovado; log: **76 IDs estruturais únicos, 2 vetos e 16 textos pesquisados na fonte oficial, 0 divergências**.
- [Artefato JSON da auditoria com SHA-256 da página](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38554726682/artifacts/11888466504) para reprodução/diagnóstico.
- [Matriz com 16 transcrições](F1A_ESPELHO_LITERAL_02_42_43.csv) da edição atual: art. 2º caput/I–III/§§1–2 (6), art. 42 caput/§§1–3 (4), art. 43 caput/I–V (6).
- [Inventário F1 amplo seletivo 76 IDs](INVENTARIO_F1_PRIORITARIO.csv), dos quais **60 sem transcrição** e **2 vetos dentro dos 76**. A auditoria textual desta rodada não conferiu todo o conteúdo das 60 unidades remanescentes; não há 76 textos C0-T.
- A rotina busca ocorrência de cada segmento normalizado na **página integral**, não ancora a verificação no DOM específico de cada parágrafo. Por isso, **controle artigo-local por unidade e comparação com DOU/página original são próximos gates**, além do cotejo manual já realizado.

## Três problemas abertos que impedem transposição C0-J
**(1) "Esta Lei" no art.2º:** copiar sem especificar o objeto do Livro de Governo Digital estenderia campo de aplicação a todo o futuro CLF, em potencial reforma material inadvertida. O mesmo vale para art. 42 caput que remete ao art.2º.
**(2) Art.43 refere-se às ferramentas do art.42:** ampliar autoria/recebimento/auditoria/prazo de guarda a sistemas fora do campo subjetivo/art42 não é mera transposição fiel. A permissão do inciso III para usar meio eletrônico quando lei especial só preveja pessoal/postal **não é regra de termo inicial único**.
**(3) Direito administrativo especial e esfera federativa:** art.2º III e §2º exigem ato normativo próprio de Estado/Município/DF; art.2º §1º exclui estatal não prestadora de serviços. T07.M03 define consequências processuais (intimação, ciência, prazo) e T43 registra características técnicas, **somente se a opção R2 for aprovada** por T01/DEC016.

## FEITO / PENDENTE / PRÓXIMO
**FEITO:** F0 de âmbito T43, F1 76 IDs, transcrição e comparação externa seletiva de 16 textos, relatório e artefato/hash, duas verificações CI (texto/estrutura) aprovadas.
**PENDENTE:** DOU/edital original, comparação intertemporal, localização artigo-local automática, 60 textos não transcritos, arts.10–41 e 44–57, normas LGPD/LAI/assinaturas, ato de adesão estadual e contrato intermodular completo. C0-J Q.
**PRÓXIMO:** completar concordância artigos 2/42/43 contra publicação original e DOU e art8 (protocolo), controlar remissões e termos, coordenar T07.M03 PR39 para decisões R1/R2.
