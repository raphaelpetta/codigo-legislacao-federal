# Código da Legislação Federal (CLF)

Projeto de pesquisa, auditoria crítica, sistematização e proposta de modernização da legislação brasileira em um **Código federal único, tematicamente organizado**.

> **Estado:** estrutura operacional preliminar (v0.3, outubro de 2026). Este repositório **não é fonte oficial de legislação vigente** e não contém proposta aprovada pelo Congresso.

## Objetivo

Projetar um corpo integrado de legislação federal geral e permanente, organizado inicialmente em 8 partes e 48 títulos, com tratamento modular, concordância entre disposições atuais e propostas, registro de decisões e revisão de compatibilidade constitucional e de efeitos jurídicos.

A Constituição permanece externa ao Código e superior a ele. Matérias de competência estadual e municipal, atos infralegais, tratados e normas temporárias terão classificação e registros próprios, respeitada sua natureza jurídica.

## Início rápido

1. [Leia primeiro](docs/00_LEIA_PRIMEIRO.md)
2. [Carta de arquitetura](docs/01_CARTA_ARQUITETURA.md)
3. [Índice provisório dos 48 títulos](catalogo/02_INDICE_48_TITULOS.csv)
4. [Catálogo de módulos candidatos](catalogo/03_CATALOGO_MODULOS.csv)
5. [Protocolo comum de pesquisa e redação](governanca/05_PROTOCOLO_DE_TRABALHO.md)
6. [Modelo de dossiê por módulo](modelos/06_MODELO_DOSSIE_MODULO.md)
7. [Registro de decisões](governanca/04_REGISTRO_DE_DECISOES.md)
8. [Status e dependências](governanca/07_STATUS_E_DEPENDENCIAS.md)
9. [Instruções do Projeto ChatGPT](chatgpt/08_INSTRUCOES_DO_PROJETO.txt)
10. [Plano operacional para chats, branches e integração](docs/16_PLANO_OPERACIONAL.md)
11. [Diretrizes interdisciplinares de pesquisa e reforma](governanca/13_DIRETRIZES_PESQUISA_E_MODERNIZACAO.md)
12. [Padrão de dados e proveniência](governanca/17_PADRAO_DADOS_E_PROVENIENCIA.md)
13. [Piloto T01.M04 — Consolidação e codificação](modulos/T01/M04/README.md)

## Governança

- **Chats de módulos** produzem dossiês, análises, alternativas e minutas de alterações.
- **Chat central de integração** confronta propostas com fontes, arquitetura e demais módulos.
- **Repositório** conserva versões, decisões e histórico. Alterações substanciais devem preferencialmente passar por branch e pull request antes de entrar em `main`.
- Nenhum texto de IA é considerado direito vigente ou juridicamente validado sem conferência independente das fontes pertinentes.
- A classificação de títulos e módulos é provisória; a cobertura exaustiva da legislação ainda não foi demonstrada.

## Estrutura

```text
docs/        visão geral e arquitetura
catalogo/    48 títulos e módulos candidatos
governanca/  decisões, protocolo e status
modelos/     dossiês e propostas padronizadas
chatgpt/     instruções para os chats do Projeto
modulos/     futuros dossiês e minutas de cada regime jurídico
```

**Regra central:** preservar a origem jurídica de cada disposição; distinguir transposição, melhoria editorial, reforma material e questão jurídica pendente.

**Importante:** verificações automatizadas comprovam apenas integridade estrutural de arquivos, não vigência nem validade jurídica. Os 48 títulos e 273 módulos são hipóteses organizacionais, não inventário exaustivo.

## Interface com o projeto constitucional (protocolo de trabalho v0.1)

O CLF mantém uma **interface de pesquisa** com o projeto independente de modernização da Constituição. A **CF/1988 permanece a referência do direito vigente**; o anteprojeto constitucional v0.1 é tratado como cenário condicional e suas hipóteses não são decisões aprovadas automaticamente.

- [Protocolo de interface constitucional](docs/09_INTERFACE_CONSTITUCIONAL.md)
- [Matriz inicial de 34 interfaces](catalogo/10_MATRIZ_COMPATIBILIDADE_CONSTITUCIONAL.csv)
- [Anexo constitucional para dossiês de módulos](modelos/11_ANEXO_CONSTITUCIONAL_DOSSIE.md)
- [Registro de pendências entre projetos](governanca/12_REGISTRO_INTERFACE_CONSTITUCIONAL.md)
- [Nota de encaminhamento ao projeto constitucional](docs/11_NOTA_PARA_PROJETO_CONSTITUCIONAL.md)

O **protocolo metodológico está em uso**, enquanto todas as propostas constitucionais ou legislativas materiais continuam sujeitas às decisões independentes de cada projeto.

## Controle de qualidade e operação

- [Checklist executável de integridade estrutural](scripts/verificar_estrutura.py) e [verificação automática em pull requests](.github/workflows/verificar-estrutura.yml).
- [Modelo de inventário de fontes normativas](modelos/18_MODELO_INVENTARIO_NORMATIVO.csv) e [modelo de concordância origem–destino](modelos/19_MODELO_CONCORDANCIA.csv).
- [Ficha de lacunas, antinomias e reforma](modelos/15_FICHA_PROBLEMA_NORMATIVO.md).

O GitHub conserva a versão de referência; conversas e arquivos de Projeto do ChatGPT não são automaticamente sincronizados. O anteprojeto constitucional conserva governança própria.
