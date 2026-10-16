# T24.M01 — F1-D15: concordância automática das ocorrências para os 45 destinos
**Corte:** 14/10/2026, PR #38 draft. **Não** atribui números do Código, não substitui o CPC e não aprova `C0-J`. Os resultados são uma concordância **dentro do universo de 45 pares já mapeados**, não um certificado de que nenhuma outra remissão exista.

## Resultado reproduzível: 19 expressões → 45 pares
O [script `mapear_f1d15_ocorrencias_alvos.py`](../../../scripts/mapear_f1d15_ocorrencias_alvos.py) executa o [inventário lexical F1-D14](../../../scripts/inventariar_f1d14_ocorrencias.py) contra [CPC art. 85 consolidado Câmara](https://www2.camara.leg.br/legin/fed/lei/2015/lei-13105-16-marco-2015-780273-normaatualizada-pl.html), associa cada ocorrência aos destinos pertinentes da [matriz F1-D13 de 45 pares](MATRIZ_F1D13_45_PARES_LITERAL_CONTEXTO.csv), sem duplicar pares. Ele registra expressões literais, offsets e destinos candidatos.

**CI [#38596068061](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38596068061) aprovada**, com [artefato CSV/JSON e lista de lacunas](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38596068061/artifacts/11910115823):
- **36 subunidades do CPC 85**, 19 ocorrências lexicais;
- **45 pares no grafo**, **45 associados a alguma ocorrência**, **0 pares órfãos desse inventário de destino**;
- **§11:** uma expressão `§§ 2º a 6º` com **cinco destinos**; outra `§§ 2º e 3º` com **dois destinos repetidos** para os tetos. Dois eventos lexicais, cinco pares únicos, e a segunda cláusula não pode ser eliminada;
- **§20:** uma expressão textual `§§ 2º, 3º, 4º, 5º, 6º, 6º-A, 8º, 8º-A, 9º e 10` corresponde a **dez destinos**, não a uma única referência genérica;
- **§4º I/II:** dez destinos resolvidos pela conjugação da expressão `incisos I a V` em cada inciso com a remissão ao §3º presente no caput. Classificação expressa `CONTEXTO_DEPENDE_CAPUT_P4`: **não** cria no texto dos incisos uma menção literal que lá não existe.

## Problemas detectados e corrigidos pela CI
1. O primeiro ensaio não reconhecia `6º-A` / `8º-A` como IDs `P6A` / `P8A`; corrigida a normalização dos sufixos com hífen.
2. O reconhecimento de `I a IV` no extrator lexical poderia encurtar `IV` a `I` pela ordem das alternativas do padrão romano; o inventário F1-D14 foi corrigido para preferir numerais mais longos.
3. No novo teste, **não sobraram três dependências §3º→§2º II–IV anteriormente sem correspondência**, porque a expressão de incisos passou a ser capturada integralmente.

## Limites que permanecem
A associação automática de todos os **45 pares já selecionados** **não atesta exaustividade semântica de todo o art.85**. Podem subsistir referências anafóricas (`deste Código`, `deste artigo`, `respectivos`), remissões a dispositivos fora do art.85, condicionantes processuais e consequências jurisprudenciais não capturadas. A correspondência lexical não prova identidade jurídica do destino se o novo Código deslocar o contexto. **Todas Q jurídico, sem C0-J**.

**FEITO:** cobertura 45/45 no recorte selecionado, auditada em execução CI, correções dos dois defeitos de tokenização, distinção entre repetição e destino único. **PENDENTE:** revisão humana de cada vínculo em frase completa, outras dependências, DOU/Lei14.365, jurisprudência atual e escolha do veículo/numeração sob DEC-016. **PRÓXIMO:** testar anáforas e remissões ao `deste Código`/art77, com mapa para o Livro correto antes de qualquer redação CLF.
