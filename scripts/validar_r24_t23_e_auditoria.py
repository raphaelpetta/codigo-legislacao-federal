#!/usr/bin/env python3
"""CLF R24: QA documental apenas, sem DOU, CI ou C0-J."""
import csv, hashlib, json
from pathlib import Path
P=Path(__file__).resolve().parents[1]
m=json.loads((P/"produto/fontes/T23_M01_LINDB_DIP_6_R24_v1.json").read_text(encoding="utf-8"))
raw=(P/m["source_path"]).read_bytes()
sha=hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
assert sha==m["source_blob_sha"]
with (P/m["source_path"]).open(encoding="utf-8",newline="") as f:rows=list(csv.DictReader(f))
assert len(rows)==6 and len({r["id_origem"] for r in rows})==6
assert len({r["id_destino_simbolico"] for r in rows})==6
assert sum(r["unidade"]=="C" for r in rows)==2
assert all(r["estado_juridico"]=="Q_SEM_C0_J" and r["texto_fonte_editorial"]==r["texto_destino_documental"] for r in rows)
assert m["dou_facsimile_checked"] is False and m["material_approved"] is False and m["dec016"]=="PENDENTE"
view=(P/m["view_path"]).read_text(encoding="utf-8")
assert sum(x.startswith("**Art. ") for x in view.splitlines())==2
assert all(r["texto_destino_documental"] in view for r in rows) and sha in view
with (P/"central/32_R24_AUDITORIA_EFEITO_PROVENIENCIA_MULTIFRENTE.csv").open(encoding="utf-8",newline="") as f:audit=list(csv.DictReader(f))
assert len(audit)==12 and len({r["id"] for r in audit})==12
assert all(r["estado_juridico"]!="C0_J_HOMOLOGADO" for r in audit)
idx=json.loads((P/"produto/fontes/indice_livros.json").read_text(encoding="utf-8"))
books=idx["livros"]
assert len(books)==55 and len({b["titulo"] for b in books})==37
assert sum(b["artigos"] for b in books)==294
assert sum(b["registros_documentais"] for b in books)==986
counts={t:(sum(b["artigos"] for b in books if b["titulo"]==t),sum(b["registros_documentais"] for b in books if b["titulo"]==t)) for t in {b["titulo"] for b in books}}
assert counts["T23"]==(2,6) and "T13" not in counts
with (P/"central/01_MATRIZ_AUDITORIA_48_TITULOS_20261015.csv").open(encoding="utf-8",newline="") as f:mat=list(csv.DictReader(f))
assert len(mat)==48
for r in mat:
 a,u=counts.get(r["id_titulo"],(0,0))
 if r["id_titulo"]=="T07":u-=1
 assert int(r["artigos_na_vista"])==a and int(r["unidades_positivas_na_vista"])==u and r["C0_J_homologadas"]=="0"
with (P/"central/PAINEL_GERADO.csv").open(encoding="utf-8",newline="") as f:panel=list(csv.DictReader(f))
assert len(panel)==48
for r in panel:
 a,u=counts.get(r["id_titulo"],(0,0))
 assert int(r["artigos_experimentais"])==a and int(r["registros_documentais_na_fonte"])==u
 assert int(r["livros_em_vista"])==sum(b["titulo"]==r["id_titulo"] for b in books)
with (P/"central/FILA_TRABALHO.csv").open(encoding="utf-8",newline="") as f:q=list(csv.DictReader(f))
assert len(q)==74 and len({r["id"] for r in q})==74
code=(P/"produto/CODIGO_DE_TRABALHO.md").read_text(encoding="utf-8")
assert sum(x.startswith("**Art. ") for x in code.splitlines())==294
first=books[0]
anchor=f"## {first['titulo']} — {first['modulo']} [{first['id']}; {first['estado']}]"
prefix=code[:code.index(anchor)]
expected=prefix+"".join(f"## {b['titulo']} — {b['modulo']} [{b['id']}; {b['estado']}]\n\n"+(P/b["vista"]).read_text(encoding="utf-8").rstrip()+"\n\n" for b in books)
assert expected.rstrip()+"\n"==code
print("OK R24 documental: 55 componentes/37 títulos/294 artigos/985 positivas+1 histórica, 12 gates")
