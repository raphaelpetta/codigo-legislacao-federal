#!/usr/bin/env python3
"""CLF R25: verificar a matriz R3 e as portas de risco, sem homologação material."""
import csv, json
from pathlib import Path
P=Path(__file__).resolve().parents[1]
with (P/"central/35_R25_MATRIZ_R3_23_CONTROLES_20261015.csv").open(encoding="utf-8",newline="") as f: gates=list(csv.DictReader(f))
assert len(gates)==23 and len({x["id"] for x in gates})==23
assert sum(x["titulo"]=="T07" for x in gates)==11
assert sum(x["titulo"]=="T24" for x in gates)==6
assert sum(x["titulo"]=="T25" for x in gates)==6
assert all(x["classificacao"].startswith("Q_") for x in gates)
assert all(x["prova_pendente"] and x["efeito_juridico_a_proteger"] for x in gates)
c1=list(csv.DictReader((P/"central/03_T07_GATE_C1_11_EFEITOS_20261015.csv").open(encoding="utf-8",newline="")))
assert len(c1)==11
assert {r["id_origem"] for r in c1}=={x["recorte"].split("(")[-1].removesuffix(")") for x in gates if x["titulo"]=="T07"}
assert all(r["classe_local"]=="C1_POTENCIAL_Q" and r["status"]=="GATE_ABERTO" for r in c1)
pin={"T07_text":"0eea9c97a110d278d6eb4efd37f4a8bbfd61ecb0",
"T07_conc":"c9cbf7d202ea9d01b9ffd48256bf3efeba6f226c",
"T24":"a0562c236cda3a49b842417bb27417e84484f363",
"T25":"40b5c03d72f975aad1339c605399f7f66ec056d0"}
m7=json.loads((P/"produto/fontes/T07_M03_v4.json").read_text(encoding="utf-8"))
m24=json.loads((P/"produto/fontes/T24_M01_106_v1.json").read_text(encoding="utf-8"))
m25=json.loads((P/"produto/fontes/T25_CP1_12_v1.json").read_text(encoding="utf-8"))
assert m7["texto_blob_sha"]==pin["T07_text"] and m7["concordancia_blob_sha"]==pin["T07_conc"]
assert m24["source_blob_sha"]==pin["T24"] and m24["count_expected"]==106
assert m25["source_blob_sha"]==pin["T25"] and m25["count_expected"]==39
assert m7["contagens_esperadas"]=={"fontes":215,"positivas":214,"historicas":1,"artigos":78,"c0_t_local":203,"c1_potencial_q":11}
assert all(m.get("dec016")=="PENDENTE" for m in [m7,m24,m25])
assert all(m.get("material_approved",False) is False for m in [m24,m25])
view24=(P/"produto/vistas/T24_CPC_70_102_PREVIA_CONTINUA_Q.md").read_text(encoding="utf-8")
view25=(P/"produto/vistas/T25_PENAL_PARTE_GERAL_CP1_12_PREVIA.md").read_text(encoding="utf-8")
view7=(P/"produto/vistas/T07_PROCESSO_ADMINISTRATIVO_PREVIA.md").read_text(encoding="utf-8")
assert sum(x.startswith("**Art. ") for x in view24.splitlines())==33
assert sum(x.startswith("**Art. CP-") for x in view25.splitlines())==12
assert sum(x.startswith("**Art. ") for x in view7.splitlines())==78
assert "As regras gerais deste Código aplicam-se aos fatos incriminados por lei especial" in view25
assert "Art. CP-012" in view25
assert all(s in view24 for s in ["**Art. 82.**", "**Art. 98.**", "**Art. 99.**"])\nassert "condição suspensiva de exigibilidade" in view24\nassert "Presume-se verdadeira a alegação de insuficiência" in view24\nassert "Os processos administrativos específicos continuarão a reger-se por lei própria" in view7
assert "decisão coordenada" in view7.lower()
idx=json.loads((P/"produto/fontes/indice_livros.json").read_text(encoding="utf-8"))["livros"]
assert len(idx)==55 and sum(x["artigos"] for x in idx)==294
print("OK R25 R3: 23 portas Q, 11 C1 T07, fontes setoriais fixadas 4 hashes no manifesto")
print("Nota: hashes externos foram verificados remotamente; esta execução só valida a pinagem documental.")
