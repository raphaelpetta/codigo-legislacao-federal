#!/usr/bin/env python3
"""Checagem documental do espelho F1-C2 (NÃO valida vigência nem equivalência jurídica)."""
from pathlib import Path
import csv
import collections
import sys

ROOT = Path(__file__).resolve().parent
FILE = ROOT / "F1C2_ESPELHO_UNIFICADO_106.csv"
EXPECTED_ARTICLES = list(range(70, 82)) + list(range(98, 103))
with FILE.open(encoding="utf-8-sig", newline="") as handle:
    entries = list(csv.DictReader(handle))
errors = []
if len(entries) != 106:
    errors.append(f"total incorreto: {len(entries)}, esperado 106")
ids = [r["id_origem"] for r in entries]
if len(set(ids)) != len(ids):
    errors.append("IDs de origem duplicados")
articles = sorted(set(int(r["artigo"]) for r in entries))
if articles != EXPECTED_ARTICLES:
    errors.append(f"artigos incompatíveis: {articles}")
statuses = collections.Counter(r["classificacao_comparacao"] for r in entries)
if sum(v for k,v in statuses.items() if k.startswith("IGUAL_")) != 102:
    errors.append("esperadas 102 unidades manualmente iguais")
if statuses["ALTERADO_2022"] != 1 or statuses["ACRESCIDO_2022"] != 1 or statuses["ACRESCIDO_2021"] != 1:
    errors.append("esperadas três alterações/acréscimos expressos")
if statuses["DIVERGENCIA_EDITORIAL_CAMARA_PLANALTO_NAO_LEGISLATIVA_DEMONSTRADA"] != 1:
    errors.append("divergência art. 77, VI não classificada corretamente")
for r in entries:
    s = r["classificacao_comparacao"]
    before, after = r["texto_original_manual"], r["texto_atual_manual"]
    if not before or not after:
        errors.append("texto vazio: " + r["id_origem"])
    if s.startswith("IGUAL_") and before != after:
        errors.append("mesmo status com textos diversos: " + r["id_origem"])
    if s.startswith("ACRESCIDO_") and before != "INEXISTENTE_EM_2015":
        errors.append("acréscimo sem marca de inexistência: " + r["id_origem"])
    if (s.startswith("ALTERADO_") or s.startswith("DIVERGENCIA_")) and before == after:
        errors.append("alterado/divergente sem diferença textual: " + r["id_origem"])
    if r["estado_proposta_clf"] != "NAO_C0_NAO_C1_NAO_M":
        errors.append("estado jurídico irregular: " + r["id_origem"])
if errors:
    print("\n".join(errors), file=sys.stderr)
    raise SystemExit(1)
print(f"PASSOU: {len(entries)} linhas, {len(set(ids))} IDs, 17 artigos, 102 identidades manuais, 3 mudanças explícitas, 1 divergência editorial.")
print("NOTA: teste estrutural, NÃO comprova fonte original, cadeia normativa nem equivalência jurídico-semântica.")
