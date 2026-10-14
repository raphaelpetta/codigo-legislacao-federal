#!/usr/bin/env python3
"""Ciclo37: qualidade probatória do edital IBAMA DIPRO 1/2025.

Não certifica ciência jurídica por edital nem AR: apenas separa aquilo
que o DOU publicizou da existência real das diligências anteriores.
"""
import csv
from pathlib import Path
B=Path(__file__).resolve().parents[1]/"modulos/T07/M03"
with (B/"MATRIZ_CICLO37_EDITAL_IBAMA_2025_PROCESSOS.csv").open(encoding="utf-8-sig",newline="") as f:
    rows=list(csv.DictReader(f))
assert len(rows)==9 and len({r["evento_id"] for r in rows})==9
assert {r["evento_id"] for r in rows}=={f"37-{i:02d}" for i in range(1,10)}
assert {r["regime_art122"] for r in rows}=={"P5"}
assert all(r["estado_c0j"]=="Q" for r in rows)
assert all("data=28%2F03%2F2025" in r["fonte_dou_indexada"] for r in rows)
p={r["evento_id"]:r for r in rows}
assert p["37-01"]["identificador_processual"]=="02001.006658/2025-15"
assert {p[x]["identificador_processual"] for x in ("37-02","37-03","37-04")}=={
    "02047.102185/2017-31","02013.000055/2022-10","02048.101638/2017-01"}
assert p["37-05"]["nivel_evidencia"]=="DECLARACAO_DO_EDITAL"
assert p["37-06"]["nivel_evidencia"]=="LACUNA_DOCUMENTAL"
assert p["37-08"]["nivel_evidencia"]=="LACUNA_DOCUMENTAL"
assert p["37-09"]["nivel_evidencia"]=="LACUNA_DOCUMENTAL"
assert p["37-07"]["descricao_curta"]=="DEZ_DIAS_DESDE_PUBLICACAO"
assert all(r["data_ato"]=="DATA_NAO_APRESENTADA" for r in rows[4:6]+rows[7:9])
print("T07 ciclo37 OK: 2025 DIPRO 1/2025, 3 processos, 9 fatos/lacunas, janela P5, sem ciência presumida.")
print("A fonte DOU foi identificada por indexação; fac-símile e ARs originais NÃO foram auditados, C0-J Q.")
