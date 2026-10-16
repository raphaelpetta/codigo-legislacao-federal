# T05.M06 — portas A, B e C para a primeira integração incremental do CLF

**Unidade:** Lei nº 9.709, de 18 de novembro de 1998, **«Regulamenta a execução do disposto nos incisos I, II e III do art. 14 da Constituição Federal»**. **Recorte estrito:** arts. 1º e 2º (caputs, incisos I–III e §§ 1º–2º), **sete posições Q**, duas cabeças de artigo. **Data de corte:** 16/10/2026. **Risco R3** (direitos políticos, consulta popular, repartição de competências, alcance territorial, processo democrático). Esta ficha documenta revisão localizada e ressalvas, **não certifica C0-J**.

## Porta A — diploma, tempo e fonte

- Fonte oficial [TSE — Lei 9.709/1998](https://www.tse.jus.br/legislacao/codigo-eleitoral/leis-ordinarias/lei-nb0-9.709-de-18-de-novembro-de-1998), conferida no recorte contra [Planalto — Lei 9.709/1998](https://www.planalto.gov.br/ccivil_03/leis/l9709.htm), com identificação congruente do diploma e dos arts. 1º–2º. As duas apresentações registram publicação no **DOU de 19/11/1998**; **não há fac-símile DOU autenticado nem cadeia alteradora integral cotejada nesta rodada**.
- **Diferença editorial detectada:** o TSE apresenta no art. 1º «desta lei», e o Planalto «desta Lei»; mantida a grafia do espelho de origem e registrada a diferença. Igualdade byte a byte entre espelho e vista **não equivale** à identidade de edições oficiais.
- O art. 15 prevê vigência a partir da publicação, mas é **fora do recorte integrado**. A questão de efeitos de alterações eleitorais em 2026 (CF art. 16), regime constitucional e eventuais alterações posteriores exige controle temporal por dispositivo antes de qualquer afirmação global de vigência. Não inferir a situação jurídica atual da lei inteira a partir da página compilada.

## Porta B — correspondência, proveniência e extensão

- O [espelho 1:1](M06_ESPELHO_LEI9709_ART1_2_7_Q.csv) preserva sete IDs de origem distintos, destinos simbólicos e texto documental, com SHA Git de blob **`9008a1845503a2789b398e80c97850b0a0e1bdb8`**. Mesmos bytes demonstrados no commit de origem **`f2c12d61997b5e545d30703cbcf25cda179bd399`** do PR #49. Manifesto `produto/fontes/T05_M06_9709_7_v1.json`, gerador original `scripts/gerar_previa_t05.py`, vista e gerador único `scripts/gerar_codigo_integrado.py`. CI exige regeneração idêntica, contagens e estado Q.
- **Referente obrigatório:** art. 1º «nos termos desta Lei» = **Lei 9.709/1998**, não «nos termos do Código da Legislação Federal»; eventual mudança seria C1 com contraprova jurídica. Numeração é localizador originário, não renumeração CLF.
- **Limite:** arts. 3º–15 e regras de convocação, competência, transições territoriais, iniciativa popular, regimentos e publicidade não constam do Livro. Nada autoriza interpretar silêncio como revogação ou consolidação global do regime eleitoral. O índice da main inclui somente este fragmento; PRs #49–#80 mantêm o corpus maior sem merge.

## Porta C — contraprova adversarial R3 (não homologada)

| Risco | Contraprova e garantia que não se pode perder | Saída |
|---|---|---|
| Participação popular | CF art. 14 I–III distingue plebiscito, referendo e iniciativa popular; não transformar o caput em autorização geral para substituir eleições periódicas ou dispensar regras constitucionais de sufrágio. | Q/R3 |
| Temporalidade da consulta | Art. 2º §§ 1º–2º distingue consulta anterior e posterior ao ato; não colapsar convocação e ratificação num procedimento único. | Q/R3 |
| Competência e território | CF arts. 18 §§ 3º–4º e 49 XV, e Lei 9.709 arts. 3º–8º **fora do recorte**; não atribuir ao CLF ou ao órgão errado iniciativa/competência de convocação e efeitos de alteração territorial. | Q/R3 |
| Iniciativa popular | Art. 1º, III, não esgota os requisitos constitucionais e da Lei 9.709 art. 13, além da CF art. 61 § 2º; não omitir quórum ou requisitos sob pretexto de compilação. | Q/R3 |
| Transição/efeitos | CF art. 16, eventual disciplina de eleições e resoluções do TSE: **nenhuma regra eleitoral nova foi aprovada**, nem se presume aplicação em 2026. | Q/R3 |

**Melhor objeção à integração:** embora o texto literal preservado não altere a lei, a localização dentro de um futuro Código pode deslocar o alcance de «desta Lei» e sugerir completude ou competência inexistentes. **Resposta condicional:** admitir apenas **vista documental parcial, expressamente não ratificada**, com origem e recorte em destaque, e exigir tabela de remissões/efeitos e revisão independente antes de C0-J, alteração C1, destino definitivo ou positivação.

**Resultado:** `INTEGRADO_EXPERIMENTAL_PARCIAL_Q` no plano editorial; `Q_SEM_C0_J` na classificação jurídica, `material_approved=false` e `dec016=PENDENTE`. **Não** houve autenticação DOU, revisão humana independente ou ratificação normativa. Próximos recortes devem ter nova porta A/B/C, e qualquer divergência de fonte altera o gate, nunca a vista à mão.
