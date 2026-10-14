#!/usr/bin/env python3
"""T24 F1-D11 — teste de completude de segunda leitura do CPC art85.

Verifica IDs, dimensões e ressalvas críticas, sem certificar C0-J.
"""
import csv
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]/"modulos/T24/M01"
def read(f):
    with (BASE/f).open(encoding="utf-8-sig",newline="") as h:return list(csv.DictReader(h))
prior=read("MAPA_36_UNIDADES_ART85_REMISSOES_E_GATE.csv")
rows=read("MATRIZ_F1D11_REEXAME_MATERIAL_36.csv")
ids={x["id_norma_origem"] for x in prior}
found={x["id_origem"] for x in rows}
if len(prior)!=36 or len(rows)!=36 or found!=ids:raise AssertionError("Exatamente 36 IDs preservados")
if any(x["status_revisao"]!="Q_SEGUNDA_LEITURA_NAO_HOMOLOGADA" for x in rows):
    raise AssertionError("Promocao C0-J prematura")
critical={
"P3":"FAZENDA_PUBLICA_COMO_PARTE",
"P5":"PROGRESSAO_SUCESSIVA",
"P6A":"SALVO_P8",
"P7":"SEM_HONORARIOS_ADICIONAIS",
"P8A":"OAB_OU_MINIMO_10_APLICA_MAIOR",
"P11":"TETOS_P2_P3",
"P12":"MULTAS_SANCOES_ART77",
"P13":"ACRESCEM_DEBITO",
"P14":"ALIMENTAR_SEM_COMPENSACAO",
"P16":"MORA_DO_TRANSITO",
"P17":"HONORARIOS_DEVIDOS",
"P18":"ACAO_AUTONOMA",
"P20":"10_REMISSOES_EXATAS"
}
by={x["unidade"]:x for x in rows}
for unit,term in critical.items():
    facts="|".join(by[unit][col] for col in (
        "fato_normativo","sujeito_destinatario","criterio_tempo_base"))
    if term not in facts:
        raise AssertionError(f"Gate incorreto {unit}: {term} nao localizado nos campos juridicos")
print("T24 F1-D11 OK: 36/36 IDs, 13 invariantes de sujeito/base/tempo, todos Q.")
print("Porta estatica nao atesta legitimidade de nova norma CLF.")
