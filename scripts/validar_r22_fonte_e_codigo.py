#!/usr/bin/env python3
"""CLF R22: checagem documental; não autentica DOU, vigência ou C0-J."""
import csv
import hashlib
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
for p,na,nu in [
 ("produto/fontes/T06_M05_OAB_11_R22_v1.json",2,11),
 ("produto/fontes/T16_M01_CC_6_R22_v1.json",3,6),
 ("produto/fontes/T10_M01_LAI_5_R22_v1.json",2,5)]:
 m=json.loads((R/p).read_text(encoding="utf-8"))
 b=(R/m["source_path"]).read_bytes()
 h=hashlib.sha1(b"blob "+str(len(b)).encode("ascii")+b"\0"+b).hexdigest()
 assert h==m["source_blob_sha"],p
 with (R/m["source_path"]).open(encoding="utf-8",newline="") as f: rows=list(csv.DictReader(f))
 assert len(rows)==nu==m["count_expected"] and len({r["artigo"] for r in rows})==na==m["articles_expected"]
 assert len({r["id_origem"] for r in rows})==nu and len({r["id_destino_simbolico"] for r in rows})==nu
 assert sum(r["unidade"]=="C" for r in rows)==na
 assert all(r["estado_juridico"]=="Q_SEM_C0_J" and r["texto_fonte_editorial"]==r["texto_destino_documental"] for r in rows)
 assert not m["dou_facsimile_checked"] and not m["material_approved"] and m["dec016"]=="PENDENTE"
 view=(R/m["view_path"]).read_text(encoding="utf-8")
 assert sum(line.startswith("**Art. ") for line in view.splitlines())==na
 assert all(r["texto_destino_documental"] in view for r in rows)
 assert h in view
 print("OK R22 manifesto",p,nu)
idx=json.loads((R/"produto/fontes/indice_livros.json").read_text(encoding="utf-8"))
books=idx["livros"]
assert len(books)==51 and len({b["titulo"] for b in books})==34
assert sum(b["artigos"] for b in books)==281 and sum(b["registros_documentais"] for b in books)==961
cnt={t:(sum(b["artigos"] for b in books if b["titulo"]==t),sum(b["registros_documentais"] for b in books if b["titulo"]==t)) for t in {b["titulo"] for b in books}}
assert cnt["T10"]==(6,27)
with (R/"central/01_MATRIZ_AUDITORIA_48_TITULOS_20261015.csv").open(encoding="utf-8",newline="") as f: matrix=list(csv.DictReader(f))
assert len(matrix)==48 and len({x["id_titulo"] for x in matrix})==48
for row in matrix:
 a,u=cnt.get(row["id_titulo"],(0,0))
 if row["id_titulo"]=="T07":u-=1
 assert int(row["artigos_na_vista"])==a and int(row["unidades_positivas_na_vista"])==u
 assert row["C0_J_homologadas"]=="0"
assert sum(int(x["unidades_positivas_na_vista"]) for x in matrix)==960
with (R/"central/PAINEL_GERADO.csv").open(encoding="utf-8",newline="") as f: panel=list(csv.DictReader(f))
assert len(panel)==48
for x in panel:
 a,u=cnt.get(x["id_titulo"],(0,0))
 assert int(x["livros_em_vista"])==sum(b["titulo"]==x["id_titulo"] for b in books)
 assert int(x["artigos_experimentais"])==a and int(x["registros_documentais_na_fonte"])==u
with (R/"central/FILA_TRABALHO.csv").open(encoding="utf-8",newline="") as f: queue=list(csv.DictReader(f))
assert len(queue)==69 and len({x["id"] for x in queue})==69
code=(R/"produto/CODIGO_DE_TRABALHO.md").read_text(encoding="utf-8")
assert sum(line.startswith("**Art. ") for line in code.splitlines())==281
first=books[0]
anchor=f"## {first['titulo']} — {first['modulo']} [{first['id']}; {first['estado']}]"
prefix=code[:code.index(anchor)]
generated=prefix+"".join(f"## {b['titulo']} — {b['modulo']} [{b['id']}; {b['estado']}]\n\n"+(R/b["vista"]).read_text(encoding="utf-8").rstrip()+"\n\n" for b in books)
assert generated.rstrip()+"\n"==code
print("OK R22: 51 componentes Q em 34 títulos, 281 artigos, 960 positivas +1 histórica")
print("QA documental não é CI verde, nem certificação DOU ou homologação C0-J")
