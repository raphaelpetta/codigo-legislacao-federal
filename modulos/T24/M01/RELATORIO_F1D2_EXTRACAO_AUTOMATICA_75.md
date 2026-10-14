# T24.M01 — F1-D2: extração externa independente dos arts. 82–97 do CPC
**Corte de pesquisa:** 14/10/2026 · **PR #38 (draft)** · **base main:** `16fba172c875c7a0de388288fe70005c944021d6`. Estes documentos não são redação CLF promulgada nem cotejo jurídico C0-J.

## 1. Prova técnica nova e execução
- [Script versionado](../../../scripts/extrair_f1d_t24.py), executado por [workflow específico](../../../.github/workflows/extrair-cpc-f1d.yml), extrai texto **por artigo e subunidade** da [publicação original Câmara](https://www2.camara.leg.br/legin/fed/lei/2015/lei-13105-16-marco-2015-780273-publicacaooriginal-146341-pl.html) e da [compilada Câmara](https://www2.camara.leg.br/legin/fed/lei/2015/lei-13105-16-marco-2015-780273-normaatualizada-pl.html), registrando URLs, SHA-256 de cada HTML e instante UTC de acesso.
- [Execução GitHub Actions #38526972117](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38526972117), job `extrair_75`, aprovado; [**artefato JSON e CSV com 75 resultados**](https://github.com/raphaelpetta/codigo-legislacao-federal/actions/runs/38526972117/artifacts/11875918126). O JSON inclui campos de texto extraído original e atual e a classificação Q por linha, de modo que o leitor pode verificar diretamente diferenças.
- O controle estrutural da PR e o teste F1-C de 106 unidades também foram aprovados no SHA da execução; validar de novo se novos arquivos forem alterados.

## 2. Resultado discriminado — não confundir correspondência textual com transformação legal
**75 identificadores do inventário F1-D processados, sem faltantes na versão atual, com quatro acréscimos historicamente esperados:**
- **45** unidades com texto original/atual idêntico *segundo normalização e extração realizada*.
- **4** unidades presentes na versão atual e ausentes no original, atribuídas a acréscimos legislativos posteriores: CPC 82 §3º pela [Lei 15.109/2025](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15109.htm) e CPC 85 §§6º-A, 8º-A e 20 pela [Lei 14.365/2022](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2022/lei/l14365.htm).
- **26** pares com **`DIVERGENCIA_DE_EXTRACAO_OU_EDICAO_A_AUDITAR`**. **Não são 26 alterações legislativas demonstradas:** a extração em linhas do HTML pode produzir falsos positivos por divisão de elementos, anotações editoriais, pontuação e remissões. Conferir cada par no artefato, diante da publicação autêntica e das cadeias legais; não classificar C0-T ou mudança M enquanto não resolvidos.

**Qualidade efetivamente alcançada:** cobertura de 75/75 unidades do inventário, extração artigo-local em duas fontes externas oficiais e preservação de material probatório. O algoritmo passa na cobertura, mas **não certifica 75/75 igualdades textuais**, e as quatro unidades adicionadas também carecem conferência histórica na lei alteradora/DOU. Teste C0-J inexistente.

## 3. Hierarquia dos problemas jurídicos relevantes
**Q-D2-01 — CPC art.82 §3º (2025):** exceção de adiantamento de custas por advogado na cobrança/execução de honorários. Ver alcance do tipo tributário/taxa e competência dos entes, litígios em curso e causa para transferência final ao réu/executado. Não codificar como dispensa irrestrita de todas as despesas e preparo de advogado em qualquer causa.

**Q-D2-02 — CPC art.85 §§6º-A,8º-A,20 (2022):** limites para apreciação equitativa, tabela seccional OAB, honorários arbitrados. [STJ Tema 1076](https://processo.stj.jus.br/repetitivos/temas_repetitivos/pesquisa.jsp?cod_tema_final=1076&cod_tema_inicial=1076&novaConsulta=true&tipo_pesquisa=T) fixou a aplicação prioritária dos percentuais; a própria [ficha STF Tema 1255](https://portal.stf.jus.br/jurisprudenciaRepercussao/tema.asp?num=1255) permanece sem julgamento de mérito na informação oficial consultada e há recorte próprio para causas envolvendo Fazenda Pública. Comparar também disciplina de EAOAB e controle de constitucionalidade dos dispositivos acrescidos, sem declarar resolvida a controvérsia.

**Q-D2-03 — CPC art.91/95 e art.98:** relação entre custeio orçamentário de perícias requeridas por MP/Fazenda/Defensoria, honorários periciais de beneficiário da gratuidade, art.95 §5º (proibição de utilizar fundo de custeio da Defensoria) e suspensão de exigibilidade no art.98 §3º. Ao condensar normas, evitar perda de mecanismo concreto de acesso à prova de hipossuficiente; separar custeio imediato, responsabilidade final, reembolso e exclusões.

**Q-D2-04 — competências e destinatários:** CPC federal pode instituir normas processuais, mas alíquotas/tabelas de taxas judiciárias estaduais, organização orçamentária e fundos pertencem a outras esferas competenciais; T24.M01/T24.M02/T06/T32/T01 precisam decidir localização antes de minuta normativa.

## 4. Método de correção das 26 linhas não coincidentes
Para cada divergência: (1) comparar a unidade no HTML original/atual por DOM localizado, não por texto global; (2) identificar se o fragmento mudou por quebras de linha, hiperlinks/nota, pontuação editorial ou ato legislativo verdadeiro; (3) confrontar Planalto consolidado e DOU de lei modificadora quando necessário; (4) registrar ato, edição, data e razão; (5) só então mudar `Q` para classificação textual técnica, ainda sem C0-J. Guardar os pares brutos antes de corrigir, não apagar registro de divergência para fazer CI passar.

## 5. FEITO / PENDENTE / PRÓXIMO
**FEITO:** inventário F1-D de 75 unidades anteriormente iniciado; agora primeiro extrator externo artigo-local com script/CI e CSV+JSON verificáveis, 45 matches técnicos, quatro acréscimos detectados, 26 divergências triadas sem alegar inovações inexistentes.
**PENDENTE:** auditoria manual/automática melhorada dos 26 pares, legislação histórica completa, jurisprudência por unidade, competência/espécie normativa e efeitos temporais, C0-J e DEC-016; transcrição literal final aceita por revisão jurídica ainda inexistente.
**PRÓXIMO:** resolver prioritariamente divergências das unidades de arts. 82, 85, 91 e 95; revisar casos de custeio judicial de perícias e custas nas hipóteses de JG; construir matriz de equivalência jurídico-material verificando titular, efeito, exceção, termo temporal e remissões. Não abrir novo PR ou alterar `main` antes de coordenação.
