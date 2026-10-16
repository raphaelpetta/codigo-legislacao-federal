#!/usr/bin/env python3
"""R23: controles documentais, sem certificação de norma, decisão ou DOU."""
from pathlib import Path
import hashlib,csv,json
R=Path(__file__).resolve().parents[1]
for path,a,u in [("produto/fontes/T15_M01_CCNJ_7_R23_v1.json",4,7),
("produto/fontes/T32_M01_ECA_5_R23_v1.json",3,5),
("produto/fontes/T16_M01_CCRESP_7_R23_v1.json",4,7)]:
 m=json.loads((R/path).read_text(encoding="utf-8"))
 raw=(R/m["source_path"]).read_bytes()
 h=hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
 assert h==m["source_blob_sha"],path
 with (R/m["source_path"]).open(encoding="utf-8",newline="") as f:rows=list(csv.DictReader(f))
 assert len(rows)==m["count_expected"]==u
 assert len({r["artigo"] for r in rows})==m["articles_expected"]==a
 assert len({r["id_origem"] for r in rows})==u and len({r["id_destino_simbolico"] for r in rows})==u
 assert sum(r["unidade"]=="C" for r in rows)==a
 assert all(r["texto_fonte_editorial"]==r["texto_destino_documental"] and r["estado_juridico"]=="Q_SEM_C0_J" for r in rows)
 assert m["dou_facsimile_checked"] is False and m["material_approved"] is False and m["dec016"]=="PENDENTE"
 view=(R/m["view_path"]).read_text(encoding="utf-8")
 assert sum(x.startswith("**Art. ") for x in view.splitlines())==a
 assert all(r["texto_destino_documental"] in view for r in rows) and h in view
idx=json.loads((R/"produto/fontes/indice_livros.json").read_text(encoding="utf-8"))
books=idx["livros"]
assert len(books)==54 and len({b["titulo"] for b in books})==36
assert sum(b["artigos"] for b in books)==292 and sum(b["registros_documentais"] for b in books)==980
counts={t:(sum(b["artigos"] for b in books if b["titulo"]==t),sum(b["registros_documentais"] for b in books if b["titulo"]==t)) for t in {b["titulo"] for b in books}}
assert counts["T15"]==(4,7) and counts["T32"]==(3,5) and counts["T16"]==(7,13)
with (R/"central/01_MATRIZ_AUDITORIA_48_TITULOS_20261015.csv").open(encoding="utf-8",newline="") as f:mat=list(csv.DictReader(f))
assert len(mat)==48 and len({x["id_titulo"] for x in mat})==48
for x in mat:
 a,u=counts.get(x["id_titulo"],(0,0))
 if x["id_titulo"]=="T07":u-=1
 assert int(x["artigos_na_vista"])==a and int(x["unidades_positivas_na_vista"])==u and int(x["C0_J_homologadas"])==0
assert sum(int(x["artigos_na_vista"]) for x in mat)==292
assert sum(int(x["unidades_positivas_na_vista"]) for x in mat)==979
with (R/"central/PAINEL_GERADO.csv").open(encoding="utf-8",newline="") as f:p=list(csv.DictReader(f))
assert len(p)==48
for x in p:
 a,u=counts.get(x["id_titulo"],(0,0))
 assert int(x["livros_em_vista"])==sum(b["titulo"]==x["id_titulo"] for b in books)
 assert int(x["artigos_experimentais"])==a and int(x["registros_documentais_na_fonte"])==u
with (R/"central/FILA_TRABALHO.csv").open(encoding="utf-8",newline="") as f:q=list(csv.DictReader(f))
assert len(q)==72 and len({x["id"] for x in q})==72
code=(R/"produto/CODIGO_DE_TRABALHO.md").read_text(encoding="utf-8")
assert sum(line.startswith("**Art. ") for line in code.splitlines())==292
first=books[0]
anchor=f"## {first['titulo']} — {first['modulo']} [{first['id']}; {first['estado']}]"
prefix=code[:code.index(anchor)]
expected=prefix+"".join(f"## {b['titulo']} — {b['modulo']} [{b['id']}; {b['estado']}]\n\n"+(R/b["vista"]).read_text(encoding="utf-8").rstrip()+"\n\n" for b in books)
assert expected.rstrip()+"\n"==code
print("R23 QA DOCUMENTAL: 54 componentes, 36 títulos, 292 artigos, 979 positivas + 1 histórico")
print("SEM autenticação DOU, C0-J, aprovação M, DEC016 ou CI verde")
