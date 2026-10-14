# T24.M01 — F1-D6: espelho integral do art. 85 do CPC com verificador independente
**Data-corte:** 14/10/2026. PR #38 draft; baseline main `16fba172c875c7a0de388288fe70005c944021d6`. **Prova documental completa de 36 unidades**, não redação CLF ou equivalência C0-J ratificada.

## Fonte e método
A [publicação original do CPC/2015](https://www2.camara.leg.br/legin/fed/lei/2015/lei-13105-16-marco-2015-780273-publicacaooriginal-146341-pl.html) e a [versão compilada da Câmara consultada em 14/10/2026](https://www2.camara.leg.br/legin/fed/lei/2015/lei-13105-16-marco-2015-780273-normaatualizada-pl.html) foram buscadas externamente pelo script [`scripts/espelho_art85_t24.py`](../../../scripts/espelho_art85_t24.py), combinado ao extrator F1-D3 de 75 dispositivos. O script percorre os 36 IDs já individualizados em `F1D_INVENTARIO_ART82_97_SUBUNIDADES.csv`, guarda as duas fontes e seus hashes SHA-256, exige ocorrência única da redação de 2015 dentro do **mesmo artigo 85** da compilação e reconstrói os três parágrafos acrescentados a partir de marcadores textuais próprios, retirando anotações editoriais.

**Resultado CI:** [execução #38554226642](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38554226642), job `espelho_85` **aprovado**; [artefato CSV e JSON com os 36 textos e hashes](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38554226642/artifacts/11887718493). A prova integral está no artefato gerado pelo job, não impressa neste relatório ou inventada na matriz. Outros jobs de estrutura, 106 unidades F1-C e 75 unidades F1-D foram aprovados naquele SHA.

## Cobertura do art. 85, sem redução de dispositivos
- **36 unidades:** caput; §§ 1º a 20 e seus acréscimos §§ 6º-A e 8º-A; incisos I–IV do §2º, I–V do §3º e I–IV do §4º. O número 36 é de **subunidades**, não de artigos.
- **33 unidades** verificadas com texto igual nos retratos oficiais de 2015 e 2026, por presença literal integral única no mesmo artigo.
- **3 acréscimos** inexistentes em 2015, presentes em 2026, acrescentados pela [Lei 14.365/2022](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2022/lei/l14365.htm): art. 85 §§6º-A, 8º-A e 20. **Nenhum desses três deve ser rotulado de norma original de 2015.**
- **0 divergências literais sem explicação nesta comparação de duas edições**. Isso não prova que não tenha havido alterações intermediárias/revertidas ou retificações não analisadas.

## Mapa de integridade de direitos
A reorganização **não** pode omitir:
- art.85 caput/§1º: devedor dos honorários, titular do crédito, reconvenção, cumprimento provisório/definitivo, execução e recursos cumulados;
- §2º incisos I–IV: base de cálculo geral e critérios qualitativos;
- §§3º–5º e §§4º I–IV: regime da Fazenda Pública por faixas progressivas, sentença líquida/ilíquida, valor da causa e salário-mínimo de referência;
- §6º e §6º-A: critérios independentemente do resultado, limites da equidade;
- §7º: precatório não impugnado;
- §8º e §8º-A: equidade excepcional e questão da tabela OAB, observada jurisprudência atual;
- §§9º–10: prestações em indenização por ilícito e causalidade da perda do objeto;
- §11: majoração recursal, trabalho adicional e limite global;
- §§12–13: honorários nos recursos/embargos/cumprimento; evitar supressão por renumeração;
- §§14–19: titularidade alimentar, sociedade de advogados, juros, cumulação, ação autônoma se omissão em decisão e advogados públicos;
- §20: arbitramento judicial com remissão **expressa aos §§2º,3º,4º,5º,6º,6º-A,8º,8º-A,9º e 10**, que deve ser reendereçada dentro do futuro Livro processual civil e não genericamente ao CLF inteiro.

**Jurisprudência para concordância jurídica futura:** [Tema 1.076/STJ](https://processo.stj.jus.br/repetitivos/temas_repetitivos/pesquisa.jsp?cod_tema_final=1076&cod_tema_inicial=1076&novaConsulta=true&tipo_pesquisa=T), [Tema 1.313/STJ](https://processo.stj.jus.br/repetitivos/temas_repetitivos/pesquisa.jsp?cod_tema_final=1313&cod_tema_inicial=1313&novaConsulta=true&tipo_pesquisa=T) (prestação de saúde pública e §8º-A), AgInt no REsp 2.194.144/SP (tabela da OAB), [Tema 1.255/STF](https://portal.stf.jus.br/jurisprudenciaRepercussao/tema.asp?num=1255), sem declarar mérito definitivamente julgado enquanto isso não for demonstrado. Preservar eventual efeito de decisão vinculante e a distinção entre texto normativo e interpretação.

## Portas C0 e intertemporalidade
- **C0-T candidato/documental** para os 33 textos idênticos nos dois retratos, **não homologado** até cadeia DOU/retificações e verificação de cada remissão;
- **C0-T de origem pós-2015** para §§6º-A, 8º-A e 20, pendente de cotejo do próprio ato modificador/DOU e publicação consolidada;
- **C0-J permanece Q nas 36 unidades**, em especial mudança de referente `deste Código`, efeitos do renumeramento, jurisprudência e condições da Fazenda Pública e da equidade;
- **DEC-016** mantém aberta a validade de formato Código único misturando espécies/iniciativas e o desenho de revogações; não transformar mera concordância textual em codificação juridicamente apta.

## FEITO / PENDENTE / PRÓXIMO
**FEITO:** geração auditável e íntegra dos 36 textos art.85, 33 iguais + três acréscimos, fontes/hash/artefato persistidos no GitHub, CI aprovado.
**PENDENTE:** histórico do DOU/retificações, comparação com leis/ações de controle, jurisprudência vigente completa, compatibilidade constitucional, reendereçamento de todas as remissões internas/externas, preservação integral art.85 para eventual texto CLF.
**PRÓXIMO:** produzir tabela de remissões com ID origem→ID destino provisório sem reutilizar `art. 85` até posição decidida; desenvolver testes jurídicos por §§/incisos (Fazenda, recursal, precatório, equidade, arbitramento); revisar lei 14.365/2022 e Tema1.255/STF antes de qualquer proposta C0-J.
