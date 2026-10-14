# T43.M04 — F1-F: 183 subunidades adicionais, vetos e art. 32 restaurado
**Data-corte:** 14/10/2026. **PR #43** (rascunho); Lei 14.129/2021 **vigente fora do CLF**. Este é um espelho textual estruturado da versão atualizada da [Câmara dos Deputados](https://www2.camara.leg.br/legin/fed/lei/2021/lei-14129-29-marco-2021-791203-normaatualizada-pl.html), **não equivalência C0-J, consolidação final nem reconstrução histórica completa**.

## FEITO — unidades finas e evidência
[Script `extrair_t43_restante_fino.py`](../../../scripts/extrair_t43_restante_fino.py) e [workflow `extrair-t43-fino.yml`](../../../.github/workflows/extrair-t43-fino.yml) extraíram com classificação artigo-local caputs, parágrafos, incisos e alíneas dos **44 artigos remanescentes** (arts. 10–41 e 44–55), mantendo os arts. 51–54 como **blocos de alteração de outras leis** a fim de não recodificá-los como comandos independentes de Governo Digital.

**CI [execução #38561552561](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38561552561) aprovada**, [artefato CSV/JSON e SHA-256 da fonte](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38561552561/artifacts/11893440118):
- **44 artigos e 183 subunidades** extraídas e identificadas por ID de fonte;
- **4 vetos ainda sem conteúdo normativo nesse recorte**: Lei 14.129/2021 art. 28 §5º, art. 29 §1º VII e §3º, e art. 46 inteiro;
- o **art. 32 NÃO é veto mantido**. Foi inicialmente vetado, mas o veto foi rejeitado pelo Congresso; a anotação oficial da Câmara informa a publicação no **DOU de 11/06/2021**. Seu texto dispõe que inconsistências na base de dados não impedem atender solicitação de abertura. **Sua vigência atual está registrada e não se poderá descartar o artigo com base no histórico inicial de veto**;
- nos arts. 24 e 28 foram conferidos marcos de alíneas do art. 24 I a/b e dos incisos do art. 28 §1º I a XV; há ainda incisos e parágrafos do art. 29 que impõem condições específicas de publicidade e proteção dos dados.

**Cobertura conjunta atual:** 76 registros estruturais anteriores dos arts. 1º–9º e 42–43 + **183 registros novos** (sem interseção de artigos) = **259 registros estruturais em todo o diploma** nesta extração. Desses, **seis registram vetos sem comando** (dois no recorte anterior, quatro neste); **quatro artigos alteradores** e **um artigo de vigência histórica** demandam tratamento formal próprio. A soma não é contagem de “259 normas independentes vigentes” e não estabelece competência legislativa do CLF.

## Qualidade e limitações
O script aplica regex a linhas do HTML oficial e exige ausência de colisões por ID, localização dos marcadores de hierarquia complexa, identificação específica dos vetos e preservação do art.32. **O texto completo de 183 unidades está no artefato gerado**, passível de consulta e reexecução. Ainda faltam auditoria humana individual de todos os fragmentos, revisão da integridade semântica das linhas quebras, comparação da publicação original de 2021 com alterações posteriores, DOU e cadeia de leis complementares/ordinárias, atos locais de adoção e identificação das normas alteradas pelos arts.51–54.

**Controle federativo:** art.2º III/§2º condiciona a adoção por outros entes, inclusive disposições sobre transparência, interoperabilidade e identificação; art.55 (vigência histórica de 90/120/180 dias) não significa adesão automática local. **Proteção de dados:** os arts. 29, 38–40 continuam dependentes de LGPD/LAI, sigilos legais e normas de finalidade/fonte/acesso, não de publicidade irrestrita.

## Próximo ciclo
F1-G: conferir todos os 259 registros contra texto original/DOU e no mínimo 30 subunidades críticas por revisão independente (29 transparência e vetos, 30 proteção de requerente, 32 restauração, 38–40 interoperabilidade e direitos, 42/43 ciência digital, 51–55 alterações/vigência). Mapear Lei7.116/1983, Lei12.527/2011, Lei12.682/2012, Lei13.460/2017 com destino e vigência atual para que os artigos alteradores **não sejam duplicados**. Só depois liberar estudos C0-T específicos, mantendo todos C0-J Q e DEC016 em aberto.

## FEITO / PENDENTE / PRÓXIMO
**FEITO:** extração por unidade fina de todos os artigos do diploma, 259 IDs estruturais reconstituíveis em dois workflows, seis vetos sem norma, art.32 restaurado, incidência e limites documentados. **PENDENTE:** concordância textual/jurídica definitiva, cadeia DOU e comparação com a edição original, destinação de dispositivos alteradores, competências e R1/R2/DEC016. **PRÓXIMO:** revisão F1-G em amostragem crítica com matrizes de remissões e direitos, sem transposição CLF enquanto Q.
