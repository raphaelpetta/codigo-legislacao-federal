# Padrão de dados, identificadores e proveniência normativa do CLF

**ID:** CLF-GOV-017 | **Versão:** 0.3 | **Data:** 13/10/2026
**Escopo:** registro de fontes, concordância e interoperabilidade entre módulos.

## 1. Identidades distintas

- **Título:** `T01`, ...; **módulo:** `T01.M04`; estes IDs identificam unidades **de trabalho** e podem ter nomes provisórios.
- **Dispositivo de origem:** identificar espécie, número, data, artigo, parágrafo/inciso e versão temporal; exemplo *ilustrativo de formato*, `BR-LEI-AAAA-NNNN-ART-XX-PAR-YY`. **Não inferir existência de artigo de um identificador.**
- **Dispositivo de trabalho CLF:** ID estável `CLF-T01-M04-N0001` (exemplo de formato), independente do número editorial/ordinal final. Nunca reaproveitar IDs antigos para regras materialmente diferentes; criar histórico de desdobramento e fusão.
- **Constituição proposta:** enquanto não existir convenção aprovada de ID estável, referir como `CFP-v0.1:art.174` e versão/fonte verificadas. Ao renumerar artigo, atualizar matriz de correspondência sem presumir identidade semântica.
- **Solicitações:** `CR-AAAA-NNN` para governança CLF, `IC-AAAA-NNN` para interface constitucional, `PROB-Txx-0001` para diagnóstico de problema.

## 2. Fonte e validade

Todo registro normativo, quando possível, terá:
`id_fonte`, `tipo_ato`, `numero_ato`, `data_ato`, `dispositivo`, `texto_versao`, `url_oficial`, `data_consulta`, `vigencia_situacao`, `competencia`, `especie_reserva`, `evidencia_verificacao`, `modulo_candidato`, `pendencia`.

Separar **texto oficial da norma**, **anotação editorial compilada**, **interpretação administrativa/jurisdicional**, **anteprojeto** e **proposta CLF**. Uma página compilada é fonte de consulta útil, mas a cadeia original de alterações deve ser recuperável em caso de divergência.

A vigência deve ser comprovada no recorte e data, não deduzida de simples aparição em página web. Identificar expressamente normas exauridas, efeitos residuais, dispositivos suspensos, medidas provisórias, promulgação e vacatio legis quando relevantes. Se não verificado, usar `A_VERIFICAR` — não inferir `VIGENTE`.

Atributos de proveniência mínimos: URL ou referência oficial, data da leitura, versão/commit quando aplicável e **o que foi efetivamente examinado** (diploma completo, artigo, ementa, resumo ou decisão). Não declarar que a jurisprudência é vinculante sem identificar fundamento e extensão de seus efeitos.

## 3. Correspondência não é necessariamente 1:1

Relações possíveis:
- `1:1`: disposição original para única disposição proposta;
- `1:N`: fonte desdobrada por função em vários destinos;
- `N:1`: várias fontes fundidas, com justificativa de equivalência ou reforma;
- `N:N`: reorganização complexa, exigindo registros intermediários.

Cada registro conserva `id_origem`, `id_destino` (ou destino externo/sem destino justificado), `categoria` C0/C1/M/Q, `efeito`, `justificativa`, `transicao`, `status_verificacao`. **Q não é uma modalidade de revogação e M não é mera renumeração.** Normas novas sem antecedente terão `origem=PROPOSTA_NOVA` e motivo.

Nenhuma disposição desaparece por omissão da tabela. O catálogo poderá registrar `FORA_DO_CODIGO`, `NORMA_ESPECIAL_MANTIDA`, `TEMPORARIA`, `ARQUIVADA`, `REVOGACAO_PROPOSTA` ou `PENDENTE`. Propor revogação não significa reconhecer revogação vigente.

## 4. Estrutura de arquivos

- `catalogo/02_INDICE_48_TITULOS.csv`: títulos candidatos; manter seus IDs únicos.
- `catalogo/03_CATALOGO_MODULOS.csv`: módulos de trabalho; chave `id_modulo` única, vínculo `id_titulo` existente.
- `catalogo/10_MATRIZ_COMPATIBILIDADE_CONSTITUCIONAL.csv`: correspondências por *faixas de artigos* e módulos; **triagem não exaustiva**.
- `modelos/18_MODELO_INVENTARIO_NORMATIVO.csv`: apenas cabeçalhos para uso nos módulos; não é inventário concluído.
- `modelos/19_MODELO_CONCORDANCIA.csv`: apenas cabeçalhos para destino e rastreabilidade; não é concordância concluída.
- `modulos/T01/M04/`: dossiê piloto e futuros registros deste regime.
- `governanca/04_REGISTRO_DE_DECISOES.md`: escolhas explicitamente confirmadas ou hipóteses. Não preencher `CONFIRMADA_PELO_USUARIO` por inferência a partir de um rascunho escrito pelo assistente.

## 5. Controles de qualidade dos dados

- IDs não duplicados; vínculos válidos entre módulo e título; contagens documentadas;
- campos obrigatórios por estágio; nenhuma fonte ou remissão órfã em trabalhos marcados `INTEGRADO`;
- versões e datas explícitas, inclusive `A_VERIFICAR` para lacunas;
- ausência de fontes inexistentes inventadas e de URLs presumidas;
- contraste entre norma vigente e proposta, inclusive cenário constitucional alternativo;
- verificações automáticas apenas para integridade **sintática/estrutural**; elas não certificam validade jurídica.

## 6. Privacidade, segurança e licenças

Preferir fontes públicas oficiais e evitar colocar dados pessoais de clientes, peças processuais identificáveis ou credenciais nos repositórios. O fato de um repositório ser privado não autoriza publicar material protegido sem controle. Registrar direitos autorais e permissões de reprodução em fontes doutrinárias. **Não enviar credenciais, tokens nem URLs assinadas temporárias** para o GitHub. Estudos comparados podem ser resumidos e citados sem reproduzir extensivamente textos protegidos.

Mudanças significativas requerem PR, descrição, teste e revisão humana; instrumentos de pesquisa gerados por IA não constituem validação independente.
