# Código da Legislação Federal — produto experimental (primeira vista)
**Corte:** 15/10/2026 · **Natureza:** corpus único EM CONSTRUÇÃO. Não é legislação vigente, minuta aprovada nem Código promulgável.

## Entrada no corpus para leitura e crítica
**Parte III — Administração pública e finanças (organização provisória)**

**Livro do Processo Administrativo Federal (T07.M03)**

[Ler a prévia integral de 78 artigos experimentais](vistas/T07_PROCESSO_ADMINISTRATIVO_PREVIA.md).

Esta é uma fotografia derivada do PR #45: 214 unidades textuais positivas da Lei 9.784/1999 transpostas em 78 artigos de ensaio; 1 registro documental de vigência histórica separado; vetos históricos não ressuscitados. **0 unidades homologadas como equivalência C0-J.** A fonte setorial em desenvolvimento está no [PR #45](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/45); não editar a fotografia como se fosse fonte normativa primária. O corpus expandirá por Livros após criação de fontes canônicas e mecanismo de montagem; não tratar o catálogo provisório de 48 títulos como corpus material já existente.

## Áreas ainda não integradas na vista
T01.M04 codificação e iniciativa/DEC-016; T24 processo civil; T25 Direito Penal; T29 previdenciário; T43 digital — todos possuem pesquisas, mas nenhuma delas está incorporada a esta versão de leitura como regime final ou devidamente transposto. [Quadro dos 48 títulos](../central/QUADRO_PRODUTO.csv) indica apenas cobertura do produto desta vista, sem negar pesquisa existente em PR.

## Plano de montagem
- **Fonte canônica por recorte:** arquivos existentes `modulos/` ou `integracao/` (após integração documental), com concordância completa origem–destino e estados de verificação; nada de cópias divergentes editadas manualmente.
- **Geração da vista:** quando a fonte T07 e as seguintes integrarem a estrutura de trabalho, criar compilador simples de Livros com IDs estáveis, sumário, remissões e `--check` para detectar desacordo entre corpus e fontes. Até então esta prévia está fixada no SHA de origem declarado.
- **Apresentações:** texto limpo para leitura, matriz crítica C0-T/C0-J/C1/M/Q com justificativas, mapa de cobertura por norma de origem e pauta de deliberações.
- **Reserva formal:** a DEC-016 versa sobre promulgação/veículo legislativo; não impede redação do corpus experimental, mas impede alegar espécie válida, revogação ou norma em vigor.
- **Garantias:** direitos, processo, legalidade sancionatória, competências, fontes temporais e regimes especiais conferidos por efeito antes de qualquer proposta de substituição de norma.

[Central CLF](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/48) · [Interface CF](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/103).

---

## Geracao reprodutivel — rodada 01 (15/10/2026)

A vista T07 nao precisa mais ser atualizada por copias manuais: o [manifesto de proveniencia](fontes/T07_M03_v4.json) fixa o commit **PR #45 / `2a4d1eefa864f44435aec70ed0cc55a96b718b64`**, com hashes Git independentes para fonte e concordancia. O [gerador de vistas](../scripts/gerar_produto_experimental.py) valida 215 IDs, 214 destinos positivos, 78 artigos, 203 C0-T locais, 11 C1 potenciais/Q, 1 historico e estado juridico pendente.

Para verificar, obter em diretorio separado o checkout setorial exato e executar:

```bash
python3 scripts/gerar_produto_experimental.py --setorial-root setorial --check
```

`--write` apenas recompila o arquivo de visualizacao a partir da fonte fixada, **nunca** altera `integracao/25_...` ou `integracao/26_...`. [CI documental dedicada](../.github/workflows/conferir-produto-experimental.yml), sem efeito de homologacao; a execucao do GitHub Actions **ainda nao foi validada no runner**, consultar logs antes de liberar merge.

[Auditoria e fila de construcao](../central/02_AUDITORIA_GLOBAL_RODADA01_20261015.md) · [Matriz de cobertura documental dos 48 titulos](../central/01_MATRIZ_AUDITORIA_48_TITULOS_20261015.csv).

