# Código da Legislação Federal — corpus único experimental (vista de trabalho)

**Corte:** 15/10/2026 · **Estado:** minutas editoriais em PR **draft**, não legislação vigente, nem texto homologado, nem revogações ou atos de promulgação. **DEC-001**: objetivo de corpus único mantido. **DEC-016**: veículo/espécie/iniciativa/veto/transição **pendente**.


## Vista única gerada do corpus efetivamente integrado

[Ler o **Código experimental integrado em texto corrido**](CODIGO_DE_TRABALHO.md), gerado por `python3 scripts/gerar_codigo_integrado.py --write` a partir de `produto/fontes/indice_livros.json` e conferido com `--check`. **A versão atual reúne T07**. A prévia parcial T24 (17 artigos, 106 subunidades) está disponível abaixo como **candidata ainda fora do índice de Livros integrados**, aguardando gate de integração experimental, não ratificação jurídica.

## Ponto de leitura: duas partes do produto, sem pretender completude

**Parte III — Administração Pública e Finanças**
- [Livro de Processo Administrativo Federal — T07.M03, prévia integral de 78 artigos](vistas/T07_PROCESSO_ADMINISTRATIVO_PREVIA.md). Proveniência: PR #45, fonte fixa, [manifesto](fontes/T07_M03_v4.json); 214 unidades positivas (203 C0-T local, 11 C1 potenciais/Q), 1 registro histórico, nenhuma unidade C0-J homologada.
- [Auditoria dos 11 C1 potenciais T07](../central/03_T07_GATE_C1_11_EFEITOS_20261015.csv), com efeitos, alternativas conservadoras, provas faltantes e riscos. Os destinatários, o âmbito e a subsidiariedade dos processos especiais permanecem Q.

**Parte V — Direito Internacional Privado, Justiça e Sanções**
- [Livro de Processo Civil — T24.M01, prévia PARCIAL de 17 artigos de origem (CPC 70–81 e 98–102)](vistas/T24_PROCESSO_CIVIL_PREVIA_PARCIAL.md). Fonte setorial PR #38 em commit fixado, [manifesto](fontes/T24_M01_106_v1.json), [concordância 1:1 das 106 unidades](concordancia/T24_M01_106_ORIGEM_DESTINO.csv). **106 Q / zero C0-J**, CPC completo não transposto. A fonte foi transcrita manualmente no PR #38 e sua verificação jurídica independente permanece pendente.

**Em pesquisa, ainda fora do corpus de leitura:** T01.M04 (formalização/DEC-016), T25 (Parte Geral penal), T29 (RGPS), T43 (Governo Digital) e [T13.M01, inventário inicial de 19 unidades CC 1–5](../modulos/T13/M01/NOTA_ABERTURA_CAPACIDADE_CIVIL_20261015.md), entre outras frentes a abrir. Nenhuma dessas pesquisas constitui Livro completo de CLF. O mapa de 48 títulos é provisório, não universo exaustivo da legislação.

## Convenção de proveniência e montagens

- **Fontes canônicas setoriais fixadas por commit**: `integracao/25_...` e `26_...` no PR #45 (T07); `modulos/T24/M01/F1C2_ESPELHO_UNIFICADO_106.csv` no PR #38 (T24). Os arquivos `vistas/` não são fonte paralela editável.
- **T07**: `python3 scripts/gerar_produto_experimental.py --setorial-root setorial --check` (com o checkout de origem T07 declarado no manifesto); `--write` regenera somente a vista derivada.
- **T24**: `python3 scripts/gerar_previa_t24.py --setorial-root setorial --check` (checkout de origem T24 no SHA declarado), verificando 106 IDs, 106 destinos, 17 artigos, hashes de blob, estado Q e equivalência exata da prévia; `--write` também regenera somente vista.
- **CI documental separada:** workflows [T07](../.github/workflows/conferir-produto-experimental.yml) e [T24](../.github/workflows/conferir-t24-previsao.yml). As execuções GitHub Actions desta rodada exibiram **failure sem etapas visíveis**; controle independente de correspondência T24 foi efetuado por leitura dos arquivos. **Não declarar CI aprovado nem C0-J**.
- **Produto futuro:** montar uma versão limpa concatenada dos recortes sob fonte e índice único, mais versão comentada com variantes, concordância N:N, remissões, índice de lacunas e transições. Hoje as vistas são componentes preliminares do corpus, sem índice jurídico integral ou renumeração final.

## Indicadores, não confundir denominadores

| Objeto | Artigos visíveis na prévia | Unidades positivas | Unidade histórica | C0-J homologadas |
|---|---:|---:|---:|---:|
| T07 — Lei 9.784/1999 | 78 | 214 | 1 | 0 |
| T24 — CPC (faixas 70–81 e 98–102) | 17 | 106 | 0 | 0 |
| **Total atual das vistas** | **95** | **320** | **1** | **0** |

As 320 unidades são **registros textuais de origens e recortes distintos**, não porcentagem de cobertura do direito federal, artigos renumerados ou 320 normas juridicamente certificadas.

[Central CLF #48](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/48) · [Auditoria dos 48 títulos](../central/01_MATRIZ_AUDITORIA_48_TITULOS_20261015.csv) · [Central CF #103](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/103).
