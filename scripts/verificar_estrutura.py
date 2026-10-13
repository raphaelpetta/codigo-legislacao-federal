#!/usr/bin/env python3
"""Valida a integridade estrutural dos catálogos CLF. NÃO confere direito vigente."""
from __future__ import annotations

import csv
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
CAT = ROOT / "catalogo"
ISSUES: list[str] = []


def fail(message: str) -> None:
    ISSUES.append(message)


def read_csv(path: pathlib.Path, required: set[str]) -> list[dict[str, str]]:
    if not path.is_file():
        fail(f"Arquivo ausente: {path.relative_to(ROOT)}")
        return []
    with path.open(encoding="utf-8-sig", newline="") as handle:
        try:
            reader = csv.DictReader(handle, strict=True)
            columns = reader.fieldnames or []
            missing = required - set(columns)
            if missing:
                fail(f"{path.name}: colunas ausentes: {', '.join(sorted(missing))}")
            rows = list(reader)
            for row_i, row in enumerate(rows, 2):
                if None in row:
                    fail(f"{path.name}:{row_i}: mais campos que colunas")
                if any(value is None for value in row.values()):
                    fail(f"{path.name}:{row_i}: menos campos que colunas")
            return rows
        except (csv.Error, UnicodeError) as exc:
            fail(f"{path.name}: erro ao ler: {exc}")
            return []


def unique(rows: list[dict[str, str]], field: str, label: str) -> None:
    seen: set[str] = set()
    for index, row in enumerate(rows, 2):
        value = (row.get(field) or "").strip()
        if not value:
            fail(f"{label}:{index}: {field} vazio")
        elif value in seen:
            fail(f"{label}:{index}: ID duplicado {value}")
        seen.add(value)


titles = read_csv(CAT / "02_INDICE_48_TITULOS.csv", {
    "id_titulo", "parte", "nome_parte", "titulo", "modulos_preliminares",
})
modules = read_csv(CAT / "03_CATALOGO_MODULOS.csv", {
    "id_modulo", "id_titulo", "titulo", "regime_juridico", "status",
})
interfaces = read_csv(CAT / "10_MATRIZ_COMPATIBILIDADE_CONSTITUCIONAL.csv", {
    "id_interface", "artigos_anteprojeto_v0_1", "titulos_clf", "modulos_piloto",
})
unique(titles, "id_titulo", "titulos")
unique(modules, "id_modulo", "modulos")
unique(interfaces, "id_interface", "interfaces")
title_ids = {r["id_titulo"] for r in titles}
module_ids = {r["id_modulo"] for r in modules}
module_count = {key: 0 for key in title_ids}
for index, row in enumerate(titles, 2):
    if not re.fullmatch(r"T\d{2}", row["id_titulo"]):
        fail(f"titulos:{index}: identificador malformado {row['id_titulo']}")
for index, row in enumerate(modules, 2):
    mid, tid = row["id_modulo"], row["id_titulo"]
    if not re.fullmatch(r"T\d{2}\.M\d{2}", mid) or not mid.startswith(tid + "."):
        fail(f"modulos:{index}: módulo/título incompatíveis {mid} / {tid}")
    if tid not in title_ids:
        fail(f"modulos:{index}: título inexistente {tid}")
    else:
        module_count[tid] += 1
for index, row in enumerate(titles, 2):
    key = row["id_titulo"]
    try:
        expected = int(row["modulos_preliminares"])
    except (TypeError, ValueError):
        fail(f"titulos:{index}: contagem não numérica")
        continue
    if module_count[key] != expected:
        fail(f"titulos:{index}: {key} diz {expected} mas tem {module_count[key]}")
for index, row in enumerate(interfaces, 2):
    if not re.fullmatch(r"IC-\d{4}-\d{3}", row["id_interface"]):
        fail(f"interfaces:{index}: identificador malformado {row['id_interface']}")
    for name, registry in [("titulos_clf", title_ids), ("modulos_piloto", module_ids)]:
        for value in (row[name] or "").split(";"):
            if value and value not in registry:
                fail(f"interfaces:{index}: referência inexistente em {name}: {value}")

for relative_path, cols in [
    ("modelos/18_MODELO_INVENTARIO_NORMATIVO.csv", {"id_fonte", "url_oficial", "data_consulta", "dispositivo", "vigencia_situacao"}),
    ("modelos/19_MODELO_CONCORDANCIA.csv", {"id_origem", "id_destino", "categoria", "justificativa", "status_verificacao"}),
]:
    read_csv(ROOT / relative_path, cols)

# Só checar links Markdown locais explícitos, não URLs remotas ou remissões em code spans.
for md in [ROOT / "README.md", *ROOT.glob("docs/*.md")]:
    if not md.exists():
        continue
    contents = md.read_text(encoding="utf-8")
    for target in re.findall(r"\]\(([^)]+)\)", contents):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = target.split("#", 1)[0]
        if target and not (md.parent / target).exists():
            fail(f"{md.relative_to(ROOT)}: link local ausente {target}")


# Verificações estruturais dos CSVs produzidos por módulos (não analisam mérito jurídico).
for path in sorted((ROOT / "modulos").glob("**/*.csv")):
    name = path.name
    if name.startswith("INVENTARIO"):
        recs = read_csv(path, {
            "id_fonte", "tipo_ato", "dispositivo", "url_oficial",
            "data_consulta", "vigencia_situacao", "modulo_candidato",
        })
        unique(recs, "id_fonte", str(path.relative_to(ROOT)))
        for idx, rec in enumerate(recs, 2):
            if not (rec.get("url_oficial") or "").startswith("https://"):
                fail(f"{path.relative_to(ROOT)}:{idx}: URL oficial vazia ou nao HTTPS")
    elif name.startswith("CONCORDANCIA"):
        recs = read_csv(path, {
            "id_origem", "id_destino", "tipo_relacao", "categoria",
            "justificativa", "status_verificacao",
        })
        for idx, rec in enumerate(recs, 2):
            if rec.get("categoria") not in {"C0", "C1", "M", "Q"}:
                fail(f"{path.relative_to(ROOT)}:{idx}: categoria de mudança inválida")
            if not (rec.get("id_origem") and rec.get("id_destino")
                    and rec.get("status_verificacao")):
                fail(f"{path.relative_to(ROOT)}:{idx}: correspondência incompleta")
    elif name.startswith("MAPA_PROBLEMAS"):
        recs = read_csv(path, {"id_problema", "descricao", "estado"})
        unique(recs, "id_problema", str(path.relative_to(ROOT)))
    elif name.startswith("MATRIZ_ESPECIES"):
        recs = read_csv(path, {
            "id_caso", "dispositivo_ou_instituto", "especie_origem",
            "reserva_material", "iniciativa_ou_competencia", "estado_prova",
            "fonte_primaria", "pergunta_pendente",
        })
        unique(recs, "id_caso", str(path.relative_to(ROOT)))
        for idx, rec in enumerate(recs, 2):
            if not re.fullmatch(r"FJ-\d{3}", rec.get("id_caso", "")):
                fail(f"{path.relative_to(ROOT)}:{idx}: ID de caso malformado")
            if not (rec.get("fonte_primaria") or "").startswith("https://"):
                fail(f"{path.relative_to(ROOT)}:{idx}: fonte primaria deve ser URL HTTPS")
    elif name.startswith("RESULTADOS_TESTE"):
        recs = read_csv(path, {
            "id_teste", "caso", "fonte_origem", "reserva_material",
            "iniciativa_relevante", "categoria_clf",
            "resultado_constitucional_preliminar", "status_temporal",
        })
        unique(recs, "id_teste", str(path.relative_to(ROOT)))
        for idx, rec in enumerate(recs, 2):
            if not re.fullmatch(r"TC-\d{3}", rec.get("id_teste", "")):
                fail(f"{path.relative_to(ROOT)}:{idx}: identificador TC incorreto")
            if rec.get("categoria_clf") not in {"C0", "C1", "M", "Q"}:
                fail(f"{path.relative_to(ROOT)}:{idx}: categoria C0/C1/M/Q incorreta")
    elif name.startswith("CENARIOS_INICIATIVA"):
        recs = read_csv(path, {
            "id_cenario", "modalidade", "operacao_proposta",
            "iniciativa_proponente", "risco_formal", "estado_conclusao",
        })
        unique(recs, "id_cenario", str(path.relative_to(ROOT)))
        for idx, rec in enumerate(recs, 2):
            if not re.fullmatch(r"IC-C0-\d{3}", rec.get("id_cenario", "")):
                fail(f"{path.relative_to(ROOT)}:{idx}: identificador de cenario incorreto")
    elif name.startswith("MATRIZ_MODELOS_PROMULGACAO"):
        recs = read_csv(path, {
            "id_teste", "modelo", "questao_de_validade", "cenario",
            "classe_material", "resultado_condicional", "status_de_pesquisa",
        })
        unique(recs, "id_teste", str(path.relative_to(ROOT)))
        for idx, rec in enumerate(recs, 2):
            if not re.fullmatch(r"PM-\d{3}", rec.get("id_teste", "")):
                fail(f"{path.relative_to(ROOT)}:{idx}: ID PM malformado")
            if rec.get("modelo") not in {"P0", "P1", "P2", "P3", "P4", "P5"}:
                fail(f"{path.relative_to(ROOT)}:{idx}: modelo nao cadastrado")
    elif name.startswith("MATRIZ_ETAPAS_CP_CE"):
        recs = read_csv(path, {
            "id_etapa", "modelo", "componente", "origem_fonte",
            "etapa", "estado_da_simulacao", "efeito_juridico_real",
        })
        unique(recs, "id_etapa", str(path.relative_to(ROOT)))
        keys = {(r["modelo"], r["componente"], r["etapa"]) for r in recs}
        expected = {
            (m, c, f"S{i:02d}") for m in ("CP", "CE")
            for c in ("T", "O", "J") for i in range(12)
        }
        if keys != expected:
            fail(f"{path.relative_to(ROOT)}: matriz incompleta, sobrando={len(keys-expected)}, faltando={len(expected-keys)}")
        for idx, rec in enumerate(recs, 2):
            if not re.fullmatch(r"SIM-(CP|CE)-(T|O|J)-S\d{2}", rec["id_etapa"]):
                fail(f"{path.relative_to(ROOT)}:{idx}: ID SIM invalido")
            if rec.get("efeito_juridico_real") != "NENHUM_TESTE_PROMULGOU_NORMA":
                fail(f"{path.relative_to(ROOT)}:{idx}: status juridico da simulacao inconsistente")
    elif name.startswith("FALHAS_E_DECISOES_CP_CE"):
        recs = read_csv(path, {
            "id_falha", "modelo", "fase", "evento_hipotetico",
            "resultado_do_teste", "situacao",
        })
        unique(recs, "id_falha", str(path.relative_to(ROOT)))
        for idx, rec in enumerate(recs, 2):
            if not re.fullmatch(r"FCE-\d{3}", rec["id_falha"]):
                fail(f"{path.relative_to(ROOT)}:{idx}: ID FCE invalido")
            if rec["modelo"] not in ("CP", "CE"):
                fail(f"{path.relative_to(ROOT)}:{idx}: modelo FCE invalido")
    elif name.startswith("MATRIZ_TESTES"):
        recs = read_csv(path, {"id_teste", "hipotese_adversarial",
                               "resultado_do_teste_de_texto", "status"})
        unique(recs, "id_teste", str(path.relative_to(ROOT)))


if ISSUES:
    for issue in ISSUES:
        print(f"ERRO: {issue}", file=sys.stderr)
    sys.exit(1)
print(f"OK estrutural: {len(titles)} títulos, {len(modules)} módulos, "
      f"{len(interfaces)} interfaces; modelos CSV e links README/docs conferidos.")
print("ATENÇÃO: não foram verificados vigência, conteúdo jurídico, jurisprudência ou exaustividade.")
