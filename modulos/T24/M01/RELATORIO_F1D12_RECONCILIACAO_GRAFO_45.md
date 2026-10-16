# T24.M01 — F1-D12: complemento do grafo do art. 85 e auditoria de ocorrências
**14/10/2026.** [CPC art.85 §4º](https://www2.camara.leg.br/legin/fed/lei/2015/lei-13105-16-marco-2015-780273-normaatualizada-pl.html) é a base positiva. Este complemento corrige uma **subcontagem do grafo de 35 ligações** utilizado nas F1-D7/F1-D9: sua utilidade como controle estrutural não o tornava exaustivo.

## Dez destinos adicionais não indexados
O **§4º caput** do art.85 incorpora as hipóteses do **§3º**. Os incisos **I e II do §4º** mandam aplicar, respectivamente desde logo e somente na liquidação, os percentuais dos **incisos I a V** — remetidos por contexto jurídico ao §3º. O grafo anterior tinha `P4→P3` e não armazenava **`P4-I→P3-I..V` e `P4-II→P3-I..V`**: **dez pares** de origem/destino adicionais, agora documentados em [CSV complementar](MATRIZ_F1D12_DEZ_REMISSOES_P4_INCISOS.csv).

**Resultado de cobertura:** 35 pares antigos **+ 10 pares novos e distintos = 45 pares de dependência mapeados**, com **uma ligação externa** ao art.77; 44 internas se não houver duplicidade, verificação pelo script F1-D12. Os pares acrescidos são **remissões dependentes da leitura do §4º caput**, não afirmação de que os incisos I/II do §4º citam o §3º literalmente em cada linha.

**Duas ocorrências textuais do §11 foram representadas apenas uma vez no grafo de pares:** o trecho `observando ... §§ 2º a 6º` gera cinco destinos (§§2–6), e o trecho final `respectivos limites ... §§2º e 3º` cita **novamente** §§2º–3º. São dois vínculos *repetidos* no modelo de pares, mas **duas ocorrências literais a mais** para quem fizer redline. **Não somar essas duas ocorrências à contagem de 45 destinos únicos**.

## Controle de qualificação
- O novo grafo é **índice funcional de dependências interpretadas**, não inventário perfeito de toda remissão textual presente no CPC ou de todas as condições em outras normas.
- Não mudar a redação do §4º para referências diretas fictícias sem redline comparativo e exame de consequências. A base de remissão está no §4º caput, sua extensão aos incisos é dependência expressa de contexto.
- O §3º usa cinco faixas percentuais e o §5º a aplicação progressiva; a reconstrução não permite percentual único. A distinção entre sentença líquida e ilíquida permanece central e remissões adicionais precisam ter destino estável após `DEC-016`.
- `F1D9_CROSSWALK_35_REMISSOES_SIMBOLICAS.csv` permanece arquivo histórico de 35 pares; **não declarar que representa todas as dependências**. Um futuro crosswalk de 45 pares só poderá substituir essa referência depois de revisão jurídico-material integral e atualização dos controles de destino.
- Estados jurídicos **Q**; não há nova numeração CLF, C0-J, lei aprovada ou revogação.

**FEITO:** dez dependências contextuais faltantes identificadas com base no texto vigente e duas ocorrências repetidas no §11. **PENDENTE:** outros cruzamentos por hipótese, cadeia DOU, jurisprudência, destino das remissões em futuro Livro e `DEC-016`. **PRÓXIMO:** revisar as 45 arestas e marcar natureza literal ou inferida de contexto, preservando a ocorrência repetida como atributo, antes de qualquer redação legislativa.
