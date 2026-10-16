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
    # T13 mantém inventário literal por dispositivo (inclusive históricos), com
    # campos próprios e origem verificável. Não deve ser tratado como o modelo
    # genérico de inventário de diplomas normativos.
    if path == ROOT / "modulos/T13/M01/INVENTARIO_CC_ART1_5_20261015.csv":
        recs = read_csv(path, {
            "id_origem", "diploma", "artigo", "unidade",
            "texto_atual_transcrito_camara", "natureza",
            "marcador_problema", "destino_experimental_candidato",
            "categoria_editorial", "estado_juridico", "fonte_oficial",
            "corte", "nota",
        })
        unique(recs, "id_origem", str(path.relative_to(ROOT)))
        for idx, rec in enumerate(recs, 2):
            if not (rec.get("fonte_oficial") or "").startswith("https://"):
                fail(f"{path.relative_to(ROOT)}:{idx}: fonte oficial vazia ou nao HTTPS")
            if not (rec.get("artigo") or "").strip() or not (rec.get("unidade") or "").strip():
                fail(f"{path.relative_to(ROOT)}:{idx}: dispositivo de origem incompleto")
            if not (rec.get("estado_juridico") or "").startswith("Q_"):
                fail(f"{path.relative_to(ROOT)}:{idx}: estado documental Q ausente")
    elif name.startswith("INVENTARIO") and not name.startswith("INVENTARIO_ARTIGOS_INTEGRAL_14"):
        recs = read_csv(path, {
            "id_fonte", "tipo_ato", "dispositivo", "url_oficial",
            "data_consulta", "vigencia_situacao", "modulo_candidato",
        })
        unique(recs, "id_fonte", str(path.relative_to(ROOT)))
        for idx, rec in enumerate(recs, 2):
            if not (rec.get("url_oficial") or "").startswith("https://"):
                fail(f"{path.relative_to(ROOT)}:{idx}: URL oficial vazia ou nao HTTPS")
    elif name.startswith("CONCORDANCIA") and not name.startswith(("CONCORDANCIA_DOCUMENTAL_11", "CONCORDANCIA_INTEGRAL_ART1_ART2_13", "CONCORDANCIA_LITERAL_ART3_17_15", "CONCORDANCIA_LITERAL_ART18_28_16", "CONCORDANCIA_LITERAL_ART29_47_17", "CONCORDANCIA_LITERAL_ART48_50_CICLO18", "CONCORDANCIA_LITERAL_ART51_70_CICLO19")):
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
        keys = {(r["modelo"], r["componente"], r["id_etapa"].split("-")[-1]) for r in recs}
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
    elif name.startswith("MATRIZ_VETO_DEPENDENCIAS"):
        recs = read_csv(path, {
            "id_cenario", "tipo", "modelo", "referencia",
            "substituto_S", "revogacao_R", "resultado_normativo_preliminar",
            "status_de_verificacao", "fonte_oficial",
        })
        unique(recs, "id_cenario", str(path.relative_to(ROOT)))
        nums = {r.get("id_cenario") for r in recs}
        want = {f"VR-{i:03d}" for i in range(1, 25)}
        if nums != want:
            fail(f"{path.relative_to(ROOT)}: universo VR incompleto/duplicado")
        for idx, rec in enumerate(recs, 2):
            if rec["tipo"] not in {"FATO_DOCUMENTADO", "SIMULACAO"}:
                fail(f"{path.relative_to(ROOT)}:{idx}: tipo de teste invalido")
            if rec["modelo"] not in {"DIREITO_VIGENTE", "BASE_SEM_DEPENDENCIA", "V1", "V2"}:
                fail(f"{path.relative_to(ROOT)}:{idx}: modelo desconhecido")
            if rec["tipo"] == "SIMULACAO" and rec["status_de_verificacao"] == "OFICIAL_EM_2026_10_13":
                fail(f"{path.relative_to(ROOT)}:{idx}: simulacao tratada como ato oficial")
            if rec["tipo"] == "FATO_DOCUMENTADO" and rec["modelo"] != "DIREITO_VIGENTE":
                fail(f"{path.relative_to(ROOT)}:{idx}: fato atribuido a modelo futuro")
            if not rec["fonte_oficial"].startswith("https://"):
                fail(f"{path.relative_to(ROOT)}:{idx}: fonte de controle sem HTTPS")
    elif name.startswith("MATRIZ_UNIDADE_VETO"):
        recs = read_csv(path, {
            "id_teste", "modelo", "evento", "posicao_da_condicao",
            "unidade_vetavel", "resultado_do_teste", "natureza",
            "regra_proveniencia", "estado", "fonte",
        })
        unique(recs, "id_teste", str(path.relative_to(ROOT)))
        expected = {f"UV-M{i}-E{j}" for i in range(4) for j in range(9)}
        found = {r["id_teste"] for r in recs}
        if expected != found:
            fail(f"{path.relative_to(ROOT)}: faltam {len(expected - found)}, sobram {len(found - expected)} testes UV")
        for idx, rec in enumerate(recs, 2):
            if rec["modelo"] not in {"M0", "M1", "M2", "M3"} or rec["evento"] not in {f"E{i}" for i in range(9)}:
                fail(f"{path.relative_to(ROOT)}:{idx}: classe e evento invalidos")
            if rec["id_teste"] != f"UV-{rec['modelo']}-{rec['evento']}":
                fail(f"{path.relative_to(ROOT)}:{idx}: chave diverge da classe/evento")
            if rec["natureza"] != "SIMULACAO" or rec["regra_proveniencia"] != "SIMULACAO_NAO_PROMULGADA":
                fail(f"{path.relative_to(ROOT)}:{idx}: simulacao representada como direito vigente")
            if not rec["fonte"].startswith("https://"):
                fail(f"{path.relative_to(ROOT)}:{idx}: fonte sem HTTPS")
    elif name.startswith("MATRIZ_NORMATIVA_HIPOTETICA"):
        recs = read_csv(path, {
            "id_nexo", "origem_fonte", "origem_dispositivo",
            "destino_experimental", "suporte_normativo_proposto",
            "efeito_juridico_real", "estado_pesquisa", "fonte_primaria",
        })
        unique(recs, "id_nexo", str(path.relative_to(ROOT)))
        if {r["id_nexo"] for r in recs} != {f"N11-{i:03d}" for i in range(1, 13)}:
            fail(f"{path.relative_to(ROOT)}: amostra N11 incompleta")
        for idx, rec in enumerate(recs, 2):
            if rec["efeito_juridico_real"] != "NENHUMA_LEI_APROVADA_PELO_TESTE":
                fail(f"{path.relative_to(ROOT)}:{idx}: modelo hipotetico recebeu forca legislativa")
            if not rec["fonte_primaria"].startswith("https://"):
                fail(f"{path.relative_to(ROOT)}:{idx}: falta fonte HTTPS")
    elif name.startswith("CONCORDANCIA_DOCUMENTAL_11"):
        recs = read_csv(path, {
            "id_registro", "origem_ato", "origem_dispositivo",
            "destino_experimental", "classe_relacao",
            "efeito_legislativo", "nexo_normativo_id", "status_prova",
        })
        unique(recs, "id_registro", str(path.relative_to(ROOT)))
        if {r["id_registro"] for r in recs} != {f"D11-{i:03d}" for i in range(1, 17)}:
            fail(f"{path.relative_to(ROOT)}: amostra D11 incompleta")
        for idx, rec in enumerate(recs, 2):
            if rec["efeito_legislativo"] != "NENHUM":
                fail(f"{path.relative_to(ROOT)}:{idx}: concordancia D criou efeito legislativo")
            if rec["classe_relacao"] not in {"1:1", "1:N", "N:1", "EXTERNO", "HISTORICO", "OMITIDO", "0:1", "INCERTO"}:
                fail(f"{path.relative_to(ROOT)}:{idx}: classe de relacao inesperada")
    elif name.startswith("TESTES_CONCORDANCIA_11"):
        recs = read_csv(path, {
            "id_teste", "arquitetura", "evento", "efeito_juridico_simulado",
            "risco", "resultado", "status_prova",
        })
        unique(recs, "id_teste", str(path.relative_to(ROOT)))
        if {r["id_teste"] for r in recs} != {f"T11-{i:03d}" for i in range(1, 21)}:
            fail(f"{path.relative_to(ROOT)}: amostra T11 incompleta")
        for idx, rec in enumerate(recs, 2):
            if rec["arquitetura"] not in {"A", "B", "C", "D"}:
                fail(f"{path.relative_to(ROOT)}:{idx}: arquitetura desconhecida")
    elif name.startswith("AUDITORIA_LITERAL_DISPOSITIVOS_12"):
        recs = read_csv(path, {
            "id_auditoria", "ato_fonte", "dispositivo_fonte", "texto_fonte",
            "texto_espelho_experimental", "destino_provisorio",
            "comparacao_textual", "classe_juridica", "status_ato_futuro",
            "fonte_primaria",
        })
        unique(recs, "id_auditoria", str(path.relative_to(ROOT)))
        expected = {f"L12-{i:03d}" for i in range(1, 25)}
        if {r["id_auditoria"] for r in recs} != expected:
            fail(f"{path.relative_to(ROOT)}: amostra literal incompleta")
        for idx, rec in enumerate(recs, 2):
            if rec["comparacao_textual"] != "LITERAL":
                fail(f"{path.relative_to(ROOT)}:{idx}: tipo de comparação incorreto")
            if rec["texto_fonte"] != rec["texto_espelho_experimental"]:
                fail(f"{path.relative_to(ROOT)}:{idx}: espelho não é literalmente idêntico")
            if rec["classe_juridica"] != "Q":
                fail(f"{path.relative_to(ROOT)}:{idx}: igualdade literal não certifica equivalência jurídica")
            if rec["status_ato_futuro"] != "NAO_PROMULGADO":
                fail(f"{path.relative_to(ROOT)}:{idx}: pesquisa alegou promulgação de norma")
            if not rec["fonte_primaria"].startswith("https://"):
                fail(f"{path.relative_to(ROOT)}:{idx}: fonte primária precisa HTTPS")
    elif name.startswith("EVENTOS_ANEXOS_VETOS_12"):
        recs = read_csv(path, {
            "id_evento", "caso", "evento", "ato_afetado",
            "data_evento", "status_em_2026_10_13", "tipo_de_documento",
            "natureza_probatória", "efeito_constatado", "fonte_oficial",
        })
        unique(recs, "id_evento", str(path.relative_to(ROOT)))
        if {r["id_evento"] for r in recs} != {f"EV12-{i:03d}" for i in range(1, 12)}:
            fail(f"{path.relative_to(ROOT)}: amostra de eventos incompleta")
        for idx, rec in enumerate(recs, 2):
            if rec["caso"] not in {"AN01", "AN02", "AN03"} or rec["natureza_probatória"] != "ATO_OFICIAL":
                fail(f"{path.relative_to(ROOT)}:{idx}: classificação de evento inadequada")
            if not rec["fonte_oficial"].startswith("https://"):
                fail(f"{path.relative_to(ROOT)}:{idx}: URL de evento inválida")
    elif name.startswith("TESTES_CONTEXTUAIS_12"):
        recs = read_csv(path, {
            "id_teste", "objeto", "hipotese", "controle",
            "resultado", "impacto", "status", "fonte_principal",
        })
        unique(recs, "id_teste", str(path.relative_to(ROOT)))
        if {r["id_teste"] for r in recs} != {f"CTX12-{i:03d}" for i in range(1, 19)}:
            fail(f"{path.relative_to(ROOT)}: testes contextuais incompletos")
        for idx, rec in enumerate(recs, 2):
            if rec["status"] != "SIMULACAO_NAO_PROMULGADA":
                fail(f"{path.relative_to(ROOT)}:{idx}: teste com efeito jurídico afirmado indevidamente")
    elif name.startswith("CONCORDANCIA_INTEGRAL_ART1_ART2_13"):
        recs = read_csv(path, {
            "id_unidade", "dispositivo_original", "destino_provisorio",
            "texto_fonte_literal", "texto_espelho_literal",
            "comparacao_textual", "equivalencia_juridica", "status_destino",
            "sinal_alerta", "fonte_oficial",
        })
        unique(recs, "id_unidade", str(path.relative_to(ROOT)))
        ids1 = {"01-C", "01-P1", "01-P2", "01-P2-I", "01-P2-II", "01-P2-III"}
        ids2 = {"02-C", "02-PU"} | {
            f"02-PU-{x}" for x in
            ("I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII")
        }
        expected = {f"P13-{x}" for x in ids1 | ids2}
        if {r["id_unidade"] for r in recs} != expected:
            fail(f"{path.relative_to(ROOT)}: universo de 21 unidades art1/art2 incompleto")
        for idx, rec in enumerate(recs, 2):
            if rec["texto_fonte_literal"] != rec["texto_espelho_literal"]:
                fail(f"{path.relative_to(ROOT)}:{idx}: espelho não é idêntico")
            if rec["comparacao_textual"] != "LITERAL" or rec["equivalencia_juridica"] != "Q":
                fail(f"{path.relative_to(ROOT)}:{idx}: cópia não certifica C0 jurídico")
            if rec["status_destino"] != "NAO_PROMULGADO":
                fail(f"{path.relative_to(ROOT)}:{idx}: norma experimental declarada promulgada")
            if not rec["fonte_oficial"].startswith("https://"):
                fail(f"{path.relative_to(ROOT)}:{idx}: fonte HTTPS ausente")
        text = (path.parent / "PILOTO_13_ARTIGOS_1_2_LEI9784.md").read_text(encoding="utf-8")
        for r in recs:
            if r["texto_espelho_literal"] not in text:
                fail(f"{path.relative_to(ROOT)}: espelho não consta integralmente da minuta: {r['id_unidade']}")
    elif name.startswith("MAPA_DEPENDENCIAS_SISTEMICAS_13"):
        recs = read_csv(path, {
            "id_dependencia", "origem_dispositivo_piloto",
            "norma_dependente", "tipo_vinculo", "classe_dependencia",
            "estado_migracao", "fonte_primaria",
        })
        unique(recs, "id_dependencia", str(path.relative_to(ROOT)))
        if {r["id_dependencia"] for r in recs} != {f"DEP13-{i:03d}" for i in range(1, 17)}:
            fail(f"{path.relative_to(ROOT)}: dependências sistêmicas incompletas")
    elif name.startswith("TESTES_VETO_CONTEXTO_TRANSICAO_13"):
        recs = read_csv(path, {
            "id_teste", "classe", "hipotese_adversarial", "resultado",
            "estado_direito", "status_normativo", "fonte",
        })
        unique(recs, "id_teste", str(path.relative_to(ROOT)))
        if {r["id_teste"] for r in recs} != {f"T13-{i:03d}" for i in range(1, 31)}:
            fail(f"{path.relative_to(ROOT)}: testes piloto13 incompletos")
        for idx, r in enumerate(recs, 2):
            if r["estado_direito"] != "SIMULACAO_JURIDICA" or r["status_normativo"] != "NAO_PROMULGADO":
                fail(f"{path.relative_to(ROOT)}:{idx}: simulação indevidamente tratada como norma")
    elif name.startswith("INVENTARIO_ARTIGOS_INTEGRAL_14"):
        recs = read_csv(path, {
            "id", "artigo", "capitulo", "tema_capitulo",
            "origem_base_ou_insercao", "estado_artigo_2026",
            "partes_vetadas_ou_alteradas", "situacao_transposicao_clf",
            "categoria_equivalencia", "destino_hipotetico", "fonte_primaria",
        })
        unique(recs, "id", str(path.relative_to(ROOT)))
        base = {str(i) for i in range(1, 71)}
        extra = {"49-A", "49-B", "49-C", "49-D", "49-E",
                 "49-F", "49-G", "64-A", "64-B", "69-A"}
        expected = base | extra
        found = {r["artigo"].replace("Art. ", "") for r in recs}
        if found != expected or len(recs) != 80:
            fail(f"{path.relative_to(ROOT)}: devem constar 80 posições exatas de artigo")
        veto_integral = {r["artigo"] for r in recs
                         if r["estado_artigo_2026"] == "VETADO_INTEGRAL"}
        if veto_integral != {"Art. 49-C"}:
            fail(f"{path.relative_to(ROOT)}: art.49-C vetado integral não isolado")
        vetos_parciais = {r["artigo"] for r in recs
                         if r["estado_artigo_2026"] == "VIGENTE_COM_PARTES_VETADAS"}
        if vetos_parciais != {"Art. 49-A", "Art. 49-G", "Art. 69-A"}:
            fail(f"{path.relative_to(ROOT)}: status de veto parcial inconsistente")
        for idx, r in enumerate(recs, 2):
            if r["categoria_equivalencia"] != "Q":
                fail(f"{path.relative_to(ROOT)}:{idx}: artigo sem auditoria promovido a C0-J")
            if r["situacao_transposicao_clf"] not in {
                "C0_TEXTUAL_NAO_C0_JURIDICO",
                "NAO_ESPELHADO_NESTA_ETAPA"
            }:
                fail(f"{path.relative_to(ROOT)}:{idx}: artigo ficticiamente incorporado")
            if not r["fonte_primaria"].startswith("https://"):
                fail(f"{path.relative_to(ROOT)}:{idx}: fonte sem HTTPS")
        # No resumo de artigo se autoriza presumir transcrição de incisos.
    elif name.startswith("HISTORICO_ALTERACOES_VETOS_14"):
        recs = read_csv(path, {
            "id_evento", "natureza", "ato_origem", "unidades_afetadas",
            "situacao_na_fonte_consolidada", "fonte_primaria",
        })
        unique(recs, "id_evento", str(path.relative_to(ROOT)))
        if {r["id_evento"] for r in recs} != {
            f"ALT14-{i:03d}" for i in range(1, 17)
        }:
            fail(f"{path.relative_to(ROOT)}: histórico legislativo com lacunas")
        vetted = [r for r in recs if r["natureza"] == "VETO"]
        if len(vetted) != 5:
            fail(f"{path.relative_to(ROOT)}: vetos históricos não cobertos")
    elif name.startswith("MATRIZ_REMISSOES_INTERDEPENDENCIAS_14"):
        recs = read_csv(path, {
            "id_vinculo", "origem_artigo", "destino_artigo_ou_referencia",
            "classe", "situacao_auditoria", "fonte_primaria",
        })
        unique(recs, "id_vinculo", str(path.relative_to(ROOT)))
        if {r["id_vinculo"] for r in recs} != {
            f"REF14-{i:03d}" for i in range(1, 51)
        }:
            fail(f"{path.relative_to(ROOT)}: matriz de 50 referências incompleta")
        allowed = {str(i) for i in range(1, 71)} | {
            "49-A", "49-B", "49-C", "49-D", "49-E", "49-F",
            "49-G", "64-A", "64-B", "69-A"
        }
        for idx, r in enumerate(recs, 2):
            if r["origem_artigo"] not in allowed:
                fail(f"{path.relative_to(ROOT)}:{idx}: referência de origem inválida")
            if r["destino_artigo_ou_referencia"] not in allowed | {"STJ633"}:
                fail(f"{path.relative_to(ROOT)}:{idx}: referência de destino inválida")
            if r["situacao_auditoria"] != "PENDENTE_DE_COTEJO_INTEGRAL":
                fail(f"{path.relative_to(ROOT)}:{idx}: referência tratada como C0-J")
    elif name.startswith("CONCORDANCIA_LITERAL_ART3_17_15"):
        recs = read_csv(path, {
            "id_unidade", "dispositivo_origem", "unidade",
            "texto_fonte_literal", "texto_espelho_literal",
            "status_textual", "equivalencia_juridica", "ato_clf",
            "fonte_primaria",
        })
        unique(recs, "id_unidade", str(path.relative_to(ROOT)))
        required_counts = {
            "3": 5, "4": 5, "5": 1, "6": 7, "7": 1,
            "8": 1, "9": 5, "10": 1, "11": 1, "12": 2,
            "13": 4, "14": 4, "15": 1, "16": 1, "17": 1
        }
        from collections import Counter
        import re as _re
        cnt = Counter()
        for idx, r in enumerate(recs, 2):
            m = _re.fullmatch(r"EXP15-(\d+)-(C|PU|P[1-9]|I|II|III|IV|V)", r["id_unidade"])
            if not m:
                fail(f"{path.relative_to(ROOT)}:{idx}: ID literal 15 invalido")
                continue
            num, unit = m.groups()
            cnt[num] += 1
            if r["dispositivo_origem"] != f"Lei 9.784/1999, art. {num}" or r["unidade"] != unit:
                fail(f"{path.relative_to(ROOT)}:{idx}: identidade de origem divergente")
            if r["texto_fonte_literal"] != r["texto_espelho_literal"]:
                fail(f"{path.relative_to(ROOT)}:{idx}: espelho divergente da origem")
            if r["equivalencia_juridica"] != "Q" or r["ato_clf"] != "NAO_PROMULGADO":
                fail(f"{path.relative_to(ROOT)}:{idx}: transposicao juridica indevidamente homologada")
            if not r["fonte_primaria"].startswith("https://"):
                fail(f"{path.relative_to(ROOT)}:{idx}: fonte primaria ausente")
        if dict(cnt) != required_counts or len(recs) != 40:
            fail(f"{path.relative_to(ROOT)}: amostra textual 3 a 17 incompleta (40 unidades)")
    elif name.startswith("CONCORDANCIA_LITERAL_ART18_28_16"):
        recs = read_csv(path, {
            "id_unidade", "origem_dispositivo", "unidade",
            "texto_fonte_literal", "texto_espelho_literal",
            "status_textual", "equivalencia_juridica", "ato_clf",
            "fonte_oficial",
        })
        unique(recs, "id_unidade", str(path.relative_to(ROOT)))
        expected_counts = {
            "18": 4, "19": 2, "20": 1, "21": 1,
            "22": 5, "23": 2, "24": 2, "25": 1,
            "26": 12, "27": 2, "28": 1,
        }
        from collections import Counter
        cc = Counter()
        target_doc = (path.parent / "PILOTO_16_ARTIGOS_18_28.md").read_text(encoding="utf-8")
        for idx, r in enumerate(recs, 2):
            if not r["id_unidade"].startswith("EXP16-"):
                fail(f"{path.relative_to(ROOT)}:{idx}: identificador experimental inválido")
                continue
            nameparts = r["id_unidade"].split("-", 2)
            if len(nameparts) != 3:
                fail(f"{path.relative_to(ROOT)}:{idx}: ID incompleto")
                continue
            num, unit = nameparts[1:]
            if r["origem_dispositivo"] != f"Lei 9.784/1999, art. {num}" or r["unidade"] != unit:
                fail(f"{path.relative_to(ROOT)}:{idx}: divergência da unidade de origem")
            cc[num] += 1
            if r["texto_fonte_literal"] != r["texto_espelho_literal"]:
                fail(f"{path.relative_to(ROOT)}:{idx}: origem e espelho divergentes")
            if r["texto_espelho_literal"] not in target_doc:
                fail(f"{path.relative_to(ROOT)}:{idx}: texto da unidade ausente no espelho MD")
            if r["status_textual"] != "C0_T_LITERAL" or r["equivalencia_juridica"] != "Q":
                fail(f"{path.relative_to(ROOT)}:{idx}: cópia textual homologada indevidamente")
            if r["ato_clf"] != "NAO_PROMULGADO":
                fail(f"{path.relative_to(ROOT)}:{idx}: dispositivo futuro indicado como promulgado")
            if not r["fonte_oficial"].startswith("https://"):
                fail(f"{path.relative_to(ROOT)}:{idx}: fonte oficial obrigatória")
        if dict(cc) != expected_counts or len(recs) != 33:
            fail(f"{path.relative_to(ROOT)}: universo incompleto de 33 unidades dos arts18-28")
    elif name.startswith("TESTES_ADVERSARIAIS_ART18_28_16"):
        recs = read_csv(path, {
            "id_teste", "classe", "evento_hipotetico", "resultado_preliminar",
            "status", "efeito_legislativo", "fonte",
        })
        unique(recs, "id_teste", str(path.relative_to(ROOT)))
        if {r["id_teste"] for r in recs} != {f"T16-{i:03d}" for i in range(1, 31)}:
            fail(f"{path.relative_to(ROOT)}: casos adversariais ciclo16 incompletos")
        for idx, r in enumerate(recs, 2):
            if r["status"] != "SIMULACAO_ADVERSARIAL" or r["efeito_legislativo"] != "NAO_PROMULGADO":
                fail(f"{path.relative_to(ROOT)}:{idx}: cenário hipotético tratado como direito positivo")
    elif name.startswith("MAPA_DEPENDENCIAS_ART18_28_16"):
        recs = read_csv(path, {
            "id_vinculo", "origem_artigo", "destino_artigo_ou_referencia",
            "tipo", "estado_auditoria", "fonte",
        })
        unique(recs, "id_vinculo", str(path.relative_to(ROOT)))
        if {r["id_vinculo"] for r in recs} != {f"DEP16-{i:03d}" for i in range(1, 21)}:
            fail(f"{path.relative_to(ROOT)}: dependências do ciclo16 incompletas")
        for idx, r in enumerate(recs, 2):
            if r["estado_auditoria"] != "PENDENTE_EQUIVALENCIA_JURIDICA":
                fail(f"{path.relative_to(ROOT)}:{idx}: dependência considerada validada sem prova")
    elif name.startswith("CONCORDANCIA_LITERAL_ART29_47_17"):
        recs = read_csv(path, {
            "id_unidade", "origem_dispositivo", "unidade",
            "texto_fonte_literal", "texto_espelho_literal",
            "categoria_textual", "equivalencia_juridica", "situacao_clf",
            "fonte_primaria",
        })
        unique(recs, "id_unidade", str(path.relative_to(ROOT)))
        required_counts = {"29": 3, "30": 1, "31": 3, "32": 1, "33": 1, "34": 1,
                           "35": 1, "36": 1, "37": 1, "38": 3, "39": 2, "40": 1,
                           "41": 1, "42": 3, "43": 1, "44": 1, "45": 1, "46": 1,
                           "47": 1}
        from collections import Counter
        counts = Counter()
        corpus = (path.parent / "PILOTO_17_INSTRUCAO_ART29_47.md").read_text(encoding="utf-8")
        for idx, r in enumerate(recs, 2):
            if not r["id_unidade"].startswith("EXP17-"):
                fail(f"{path.relative_to(ROOT)}:{idx}: ID experimental inválido")
                continue
            parts = r["id_unidade"].split("-", 2)
            if len(parts) != 3:
                fail(f"{path.relative_to(ROOT)}:{idx}: ID incompleto")
                continue
            art, unit = parts[1:]
            counts[art] += 1
            if r["origem_dispositivo"] != f"Lei 9.784/1999, art. {art}" or r["unidade"] != unit:
                fail(f"{path.relative_to(ROOT)}:{idx}: divergência da referência original")
            if r["texto_fonte_literal"] != r["texto_espelho_literal"]:
                fail(f"{path.relative_to(ROOT)}:{idx}: textos de origem/espelho diferem")
            if r["texto_espelho_literal"] not in corpus:
                fail(f"{path.relative_to(ROOT)}:{idx}: texto integral não está no piloto MD")
            if r["categoria_textual"] != "C0_T_LITERAL" or r["equivalencia_juridica"] != "Q":
                fail(f"{path.relative_to(ROOT)}:{idx}: equivalência jurídica declarada antes do exame")
            if r["situacao_clf"] != "NAO_PROMULGADO":
                fail(f"{path.relative_to(ROOT)}:{idx}: simulação não pode ser lei promulgada")
            if not r["fonte_primaria"].startswith("https://"):
                fail(f"{path.relative_to(ROOT)}:{idx}: fonte primária ausente")
        if dict(counts) != required_counts or len(recs) != 28:
            fail(f"{path.relative_to(ROOT)}: universo do Capítulo X incompleto (28 unidades)")
    elif name.startswith("TESTES_ADVERSARIAIS_INSTRUCAO_17"):
        recs = read_csv(path, {
            "id_caso", "bloco", "artigo", "evento_hipotetico", "resultado_preliminar",
            "status", "efeito_normativo", "fonte",
        })
        unique(recs, "id_caso", str(path.relative_to(ROOT)))
        if {r["id_caso"] for r in recs} != {f"T17-{i:03d}" for i in range(1, 37)}:
            fail(f"{path.relative_to(ROOT)}: 36 cenários necessários")
        for idx, r in enumerate(recs, 2):
            if r["status"] != "SIMULACAO_ADVERSARIAL" or r["efeito_normativo"] != "NENHUM":
                fail(f"{path.relative_to(ROOT)}:{idx}: teste hipóteses tratado como norma")
    elif name.startswith("DEPENDENCIAS_INSTRUCAO_17"):
        recs = read_csv(path, {
            "id_relacao", "artigo_origem", "artigo_referenciado", "fundamento_do_nexo",
            "classe", "risco", "status", "fonte",
        })
        unique(recs, "id_relacao", str(path.relative_to(ROOT)))
        if {r["id_relacao"] for r in recs} != {f"NEX17-{i:03d}" for i in range(1, 35)}:
            fail(f"{path.relative_to(ROOT)}: 34 relações necessárias")
        for idx, r in enumerate(recs, 2):
            if r["status"] != "PENDENTE_C0_J":
                fail(f"{path.relative_to(ROOT)}:{idx}: nexo declarado validado antes da prova")
    elif name.startswith("CONCORDANCIA_LITERAL_ART48_50_CICLO18"):
        recs = read_csv(path, {"id", "artigo", "unidade", "texto_fonte_literal",
                               "texto_espelho_literal", "status_textual",
                               "equivalencia_juridica", "efeito_normativo",
                               "situacao_codificacao", "fonte_oficial"})
        unique(recs, "id", str(path.relative_to(ROOT)))
        positive = {"48", "49", "49-A", "49-B", "49-D", "49-E",
                    "49-F", "49-G", "50"}
        ids = set()
        doc = (path.parent / "PILOTO_18_DECISAO_COORDENADA_MOTIVACAO.md").read_text(encoding="utf-8")
        for n, r in enumerate(recs, 2):
            aid = r["artigo"]
            if aid not in positive or aid == "49-C":
                fail(f"{path.relative_to(ROOT)}:{n}: unidade vetada ou fora do escopo")
            ids.add(aid)
            if r["texto_fonte_literal"] != r["texto_espelho_literal"]:
                fail(f"{path.relative_to(ROOT)}:{n}: texto espelhado diverge da origem")
            if r["texto_espelho_literal"] not in doc:
                fail(f"{path.relative_to(ROOT)}:{n}: texto não consta do dossiê integral")
            if (r["status_textual"] != "C0-T_VERIFICACAO_AUTOMATICA_DE_IDENTIDADE"
                or r["equivalencia_juridica"] != "Q"
                or r["situacao_codificacao"] != "NAO_PROMULGADO"
                or r["efeito_normativo"] != "NENHUM"):
                fail(f"{path.relative_to(ROOT)}:{n}: efeito ou equivalência jurídica indevidamente homologados")
            if not r["fonte_oficial"].startswith("https://"):
                fail(f"{path.relative_to(ROOT)}:{n}: falta fonte HTTPS")
        if len(recs) != 40 or ids != positive:
            fail(f"{path.relative_to(ROOT)}: são necessárias 40 unidades positivas em nove artigos")
    elif name.startswith("REGISTRO_VETOS_LEI14210_CICLO18"):
        recs = read_csv(path, {"id", "artigo", "unidade", "situacao",
                               "proibido_incorporar_direito_positivo", "fonte_primaria"})
        unique(recs, "id", str(path.relative_to(ROOT)))
        if len(recs) != 6:
            fail(f"{path.relative_to(ROOT)}: registro deve conter seis unidades de veto")
        for n, r in enumerate(recs, 2):
            if r["proibido_incorporar_direito_positivo"] != "SIM":
                fail(f"{path.relative_to(ROOT)}:{n}: veto histórico apresentado como texto positivo")
            if not r["fonte_primaria"].startswith("https://"):
                fail(f"{path.relative_to(ROOT)}:{n}: falta fonte de veto")
    elif name.startswith("TESTES_ADVERSARIAIS_DECISAO_18"):
        recs = read_csv(path, {"id", "artigo", "cenario", "classe_preliminar",
                               "risco", "estado", "fonte_oficial"})
        unique(recs, "id", str(path.relative_to(ROOT)))
        if {r["id"] for r in recs} != {f"T18-{i:03d}" for i in range(1, 37)}:
            fail(f"{path.relative_to(ROOT)}: 36 cenários adversariais necessários")
        for n, r in enumerate(recs, 2):
            if r["estado"] != "SIMULACAO_NAO_APROVADA":
                fail(f"{path.relative_to(ROOT)}:{n}: simulação indevidamente aprovada")
    elif name.startswith("DEPENDENCIAS_DECISAO_18"):
        recs = read_csv(path, {"id", "origem", "destino", "nexo", "classe",
                               "equivalencia_juridica", "fonte_oficial"})
        unique(recs, "id", str(path.relative_to(ROOT)))
        if {r["id"] for r in recs} != {f"NX18-{i:03d}" for i in range(1, 31)}:
            fail(f"{path.relative_to(ROOT)}: 30 nexos necessários")
        for n, r in enumerate(recs, 2):
            if r["equivalencia_juridica"] != "Q":
                fail(f"{path.relative_to(ROOT)}:{n}: nexo tratado como equivalência provada")
    elif name.startswith("CONCORDANCIA_LITERAL_ART51_70_CICLO19"):
        recs = read_csv(path, {"id_unidade", "artigo", "unidade",
                               "texto_fonte_literal", "texto_espelho_literal",
                               "classificacao_temporal", "classe_textual",
                               "equivalencia_juridica", "efeito_normativo",
                               "status_codificacao", "fonte_primaria"})
        unique(recs, "id_unidade", str(path.relative_to(ROOT)))
        expected_ids = {str(i) for i in range(51, 71)} | {"64-A", "64-B", "69-A"}
        actual = {r["artigo"] for r in recs}
        if len(recs) != 53 or actual != expected_ids:
            fail(f"{path.relative_to(ROOT)}: 53 unidades em 23 artigos finais exigidas")
        doc = (path.parent / "PILOTO_19_RECURSOS_REVISAO_VIGENCIA.md").read_text(encoding="utf-8")
        for idx, r in enumerate(recs, 2):
            if r["texto_fonte_literal"] != r["texto_espelho_literal"]:
                fail(f"{path.relative_to(ROOT)}:{idx}: espelho diverge da fonte")
            if r["texto_espelho_literal"] not in doc:
                fail(f"{path.relative_to(ROOT)}:{idx}: unidade não aparece no dossiê")
            if (r["classe_textual"] != "C0-T_LITERAL" or
                r["equivalencia_juridica"] != "Q" or
                r["status_codificacao"] != "NAO_PROMULGADO" or
                r["efeito_normativo"] != "NENHUM"):
                fail(f"{path.relative_to(ROOT)}:{idx}: equivalência ou vigência atribuída indevidamente")
            if r["artigo"] == "70" and r["classificacao_temporal"] != "HISTORICO_VIGENCIA":
                fail(f"{path.relative_to(ROOT)}:{idx}: art.70 não é vigência do Código")
            if r["artigo"] == "69-A" and r["unidade"] in {"III", "P3", "P4"}:
                fail(f"{path.relative_to(ROOT)}:{idx}: texto vetado transposto como positivo")
            if not r["fonte_primaria"].startswith("https://"):
                fail(f"{path.relative_to(ROOT)}:{idx}: falta fonte oficial")
    elif name.startswith("VETOS_HISTORICOS_ART69A_CICLO19"):
        recs = read_csv(path, {"id_veto", "artigo", "unidade",
                               "estado_na_lei_consultada", "fonte_da_lei",
                               "efeito_legislativo", "classe_juridica"})
        unique(recs, "id_veto", str(path.relative_to(ROOT)))
        if {(r["artigo"], r["unidade"]) for r in recs} != {
            ("69-A", "III"), ("69-A", "P3"), ("69-A", "P4")
        } or len(recs) != 3:
            fail(f"{path.relative_to(ROOT)}: registros de veto 69-A incompletos")
        for idx, r in enumerate(recs, 2):
            if (r["estado_na_lei_consultada"] != "VETADO_ORIGINARIAMENTE" or
                r["efeito_legislativo"] != "NENHUM" or
                r["classe_juridica"] != "HISTORICO_NAO_POSITIVO"):
                fail(f"{path.relative_to(ROOT)}:{idx}: veto confundido com lei vigente")
    elif name.startswith("TESTES_ADVERSARIAIS_ART51_70_CICLO19"):
        recs = read_csv(path, {"id_teste", "artigo", "hipotese_adversarial",
                               "resultado_preliminar", "status", "efeito_normativo", "fonte"})
        unique(recs, "id_teste", str(path.relative_to(ROOT)))
        if {r["id_teste"] for r in recs} != {f"T19-{i:03d}" for i in range(1, 45)}:
            fail(f"{path.relative_to(ROOT)}: são necessários 44 testes adversariais")
        for idx, r in enumerate(recs, 2):
            if r["status"] != "SIMULACAO_NAO_APROVADA" or r["efeito_normativo"] != "NENHUM":
                fail(f"{path.relative_to(ROOT)}:{idx}: simulação com efeito indevido")
    elif name.startswith("DEPENDENCIAS_ART51_70_CICLO19"):
        recs = read_csv(path, {"id_nexo", "origem_artigo",
                               "destino_artigo_ou_jurisprudencia",
                               "razao_do_vinculo", "status_equivalencia", "fonte"})
        unique(recs, "id_nexo", str(path.relative_to(ROOT)))
        if {r["id_nexo"] for r in recs} != {f"NX19-{i:03d}" for i in range(1, 38)}:
            fail(f"{path.relative_to(ROOT)}: 37 nexos necessários")
        for idx, r in enumerate(recs, 2):
            if r["status_equivalencia"] != "PENDENTE_C0_J":
                fail(f"{path.relative_to(ROOT)}:{idx}: nexo indevidamente homologado")
    elif name.startswith("MATRIZ_TRIAGEM_215_UNIDADES_CICLO20"):
        recs = read_csv(path, {
            "id_auditoria", "origem_unidade", "id_espelho",
            "destino_funcional_proposto", "texto_fonte", "sinalizadores_de_risco",
            "urgencia_triagem", "estado_auditoria_juridica", "equivalencia_juridica",
            "classificacao_mudanca", "status_efeito_normativo", "fonte_primaria"
        })
        unique(recs, "id_auditoria", str(path.relative_to(ROOT)))
        if {r["id_auditoria"] for r in recs} != {
            f"AUD20-{i:03d}" for i in range(1, 216)
        }:
            fail(f"{path.relative_to(ROOT)}: triagem incompleta (215 unidades esperadas)")
        # Garantia mais forte: cotejar os 215 registros com os seis CSVs
        # originais que os alimentam, e não só os dois campos da triagem.
        files = [
            "CONCORDANCIA_INTEGRAL_ART1_ART2_13.csv",
            "CONCORDANCIA_LITERAL_ART3_17_15.csv",
            "CONCORDANCIA_LITERAL_ART18_28_16.csv",
            "CONCORDANCIA_LITERAL_ART29_47_17.csv",
            "CONCORDANCIA_LITERAL_ART48_50_CICLO18.csv",
            "CONCORDANCIA_LITERAL_ART51_70_CICLO19.csv",
        ]
        originals: dict[str, str] = {}
        for name_orig in files:
            orig_rows = read_csv(path.parent / name_orig, {
                "texto_fonte_literal", "texto_espelho_literal"
            })
            for ori in orig_rows:
                uid = ori.get("id_unidade") or ori.get("id")
                if not uid or uid in originals:
                    fail(f"{path.relative_to(ROOT)}: fonte duplicada/sem identificador {name_orig}:{uid}")
                else:
                    originals[uid] = ori["texto_fonte_literal"]
                if ori["texto_fonte_literal"] != ori["texto_espelho_literal"]:
                    fail(f"{path.relative_to(ROOT)}: fonte de espelho divergente {uid}")
        if len(originals) != 215:
            fail(f"{path.relative_to(ROOT)}: universo de origem não soma 215")
        used: set[str] = set()
        for idx, r in enumerate(recs, 2):
            uid = r["id_espelho"]
            if uid in used or uid not in originals:
                fail(f"{path.relative_to(ROOT)}:{idx}: origem não única/inexistente {uid}")
            used.add(uid)
            if r["texto_fonte"] != originals.get(uid, ""):
                fail(f"{path.relative_to(ROOT)}:{idx}: texto da triagem diverge da origem {uid}")
            if r["estado_auditoria_juridica"] != "NAO_AUDITADA_JURIDICAMENTE":
                fail(f"{path.relative_to(ROOT)}:{idx}: triagem alegou auditoria jurídica concluída")
            if (r["equivalencia_juridica"] != "Q" or
                r["classificacao_mudanca"] != "NAO_CLASSIFICADA" or
                r["status_efeito_normativo"] != "NENHUM"):
                fail(f"{path.relative_to(ROOT)}:{idx}: triagem promoveu norma sem prova")
            if not r["destino_funcional_proposto"].startswith("TITULO_"):
                fail(f"{path.relative_to(ROOT)}:{idx}: não pertence a título do Livro uno")
            if not r["fonte_primaria"].startswith("https://"):
                fail(f"{path.relative_to(ROOT)}:{idx}: falta fonte")
        if used != set(originals):
            fail(f"{path.relative_to(ROOT)}: espelho ausente da triagem")
    elif name.startswith("CONTRAPROVAS_SEMANTICAS_CICLO20"):
        recs = read_csv(path, {
            "id_teste_semantico", "unidade_de_risco", "tema",
            "transformacao_a_testar", "veredito_preliminar",
            "fundamentacao", "condicao_para_minuta",
            "estado_aprovacao", "fonte_primaria"
        })
        unique(recs, "id_teste_semantico", str(path.relative_to(ROOT)))
        if {r["id_teste_semantico"] for r in recs} != {
            f"Q20-{i:03d}" for i in range(1, 33)
        }:
            fail(f"{path.relative_to(ROOT)}: contraprovas semânticas incompletas")
        for idx, r in enumerate(recs, 2):
            if r["estado_aprovacao"] != "NAO_APROVADO":
                fail(f"{path.relative_to(ROOT)}:{idx}: teste classificado como decisão")
            if not r["fonte_primaria"].startswith("https://"):
                fail(f"{path.relative_to(ROOT)}:{idx}: fonte necessária")
    elif name.startswith("MATRIZ_INTERFACES_EXTERIORES_CICLO20"):
        recs = read_csv(path, {
            "id_interface", "referencia_lei_9784", "norma_ou_jurisprudencia_externa",
            "assunto", "tipo", "risco_legal", "fonte_primaria",
            "verificacao_de_vigencia", "decisao_de_inclusao",
            "equivalencia_C0J"
        })
        unique(recs, "id_interface", str(path.relative_to(ROOT)))
        if {r["id_interface"] for r in recs} != {
            f"EX20-{i:03d}" for i in range(1, 16)
        }:
            fail(f"{path.relative_to(ROOT)}: interfaces externas incompletas")
        for idx, r in enumerate(recs, 2):
            if (r["verificacao_de_vigencia"] != "PENDENTE_POR_DISPOSITIVO" or
                r["decisao_de_inclusao"] != "NAO_DELIBERADA" or
                r["equivalencia_C0J"] != "Q"):
                fail(f"{path.relative_to(ROOT)}:{idx}: interface presumida incluída/validada")
            if not r["fonte_primaria"].startswith("https://"):
                fail(f"{path.relative_to(ROOT)}:{idx}: interface sem fonte")
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
