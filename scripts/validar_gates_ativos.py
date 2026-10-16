#!/usr/bin/env python3
"""QA focal e reusavel de matrizes R24 e R25 em snapshot evolutivo."""
import csv
from pathlib import Path
R=Path(__file__).resolve().parents[1]
def rows(p):
    with (R/p).open(encoding="utf-8",newline="") as f:
        return list(csv.DictReader(f, strict=True))
r24=rows("central/32_R24_AUDITORIA_EFEITO_PROVENIENCIA_MULTIFRENTE.csv")
r25=rows("central/35_R25_MATRIZ_R3_23_CONTROLES_20261015.csv")
assert len(r24)==12 and len({r["id"] for r in r24})==12
assert len(r25)==23 and len({r["id"] for r in r25})==23
assert all("C0_J_HOMOLOGADO" not in r["estado_juridico"] for r in r24)
assert all(r["classificacao"].startswith("Q_") and r["prova_pendente"] for r in r25)
assert (sum(x["titulo"]=="T07" for x in r25),
        sum(x["titulo"]=="T24" for x in r25),
        sum(x["titulo"]=="T25" for x in r25))==(11,6,6)
t07=rows("central/03_T07_GATE_C1_11_EFEITOS_20261015.csv")
assert len(t07)==11
assert all(x["status"]=="GATE_ABERTO" and x["classe_local"]=="C1_POTENCIAL_Q" for x in t07)
ids={r["id_origem"] for r in t07}
assert ids == {g["recorte"].split("(")[-1].removesuffix(")") for g in r25 if g["titulo"]=="T07"}
v24=(R/"produto/vistas/T24_CPC_70_102_PREVIA_CONTINUA_Q.md").read_text(encoding="utf-8")
v25=(R/"produto/vistas/T25_PENAL_PARTE_GERAL_CP1_12_PREVIA.md").read_text(encoding="utf-8")
v07=(R/"produto/vistas/T07_PROCESSO_ADMINISTRATIVO_PREVIA.md").read_text(encoding="utf-8")
assert all(s in v24 for s in ["**Art. 75.**","**Art. 82.**","**Art. 98.**","**Art. 99.**","condição suspensiva de exigibilidade"])
assert all(s in v25 for s in ["**Art. CP-001.**","**Art. CP-012.**","As regras gerais deste Código aplicam-se aos fatos incriminados por lei especial"])
assert "Os processos administrativos específicos continuarão a reger-se por lei própria" in v07
with (R/"central/42_R29_AUDITORIA_MUSEUS_VETO_E_TRANSICOES_20261016.csv").open(encoding="utf-8",newline="") as f:
    r29=list(csv.DictReader(f,strict=True))
assert len(r29)==11 and len({x["id"] for x in r29})==11
assert all(x["categoria"].startswith("Q_") or x["categoria"]=="BLOQUEADO_CI_P0" for x in r29)
print("R29 11 gates de veto, remissões e eficácia classificados Q/CI.")
print("R26 QA GATES: R24 12 + R25 23 sem promocao juridica; T07 11 C1 abertos.")
