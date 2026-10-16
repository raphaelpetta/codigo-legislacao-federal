#!/usr/bin/env python3
"""CLF R30: T18 3 artigos / 8 unidades Q, sem C0-J ou DOU."""
import csv,hashlib,json
from pathlib import Path
P=Path(__file__).resolve().parents[1]
m=json.loads((P/"produto/fontes/T18_M01_SA_8_R30_v1.json").read_text(encoding="utf-8"))
raw=(P/m["source_path"]).read_bytes()
sha=hashlib.sha1(b"blob "+str(len(raw)).encode("ascii")+b"\0"+raw).hexdigest()
assert sha==m["source_blob_sha"]
with (P/m["source_path"]).open(encoding="utf-8",newline="") as f:rows=list(csv.DictReader(f,strict=True))
assert len(rows)==m["count_expected"]==8
assert len({r["id_origem"] for r in rows})==len({r["id_destino_simbolico"] for r in rows})==8
assert len({r["artigo"] for r in rows})==m["articles_expected"]==3
assert sum(r["unidade"]=="C" for r in rows)==3
assert {r["unidade"] for r in rows if r["artigo"]=="1"}=={"C"}
assert {r["unidade"] for r in rows if r["artigo"]=="2"}=={"C","P1","P2","P3"}
assert {r["unidade"] for r in rows if r["artigo"]=="3"}=={"C","P1","P2"}
assert all(r["texto_fonte_editorial"]==r["texto_destino_documental"] and r["estado_juridico"]=="Q_SEM_C0_J" for r in rows)
view=(P/m["view_path"]).read_text(encoding="utf-8")
assert sha in view and all(r["texto_destino_documental"] in view for r in rows)
assert sum(line.startswith("**Art. ") for line in view.splitlines())==3
# T18 REMISSAO R3: impedir destino ambiguo do art. 3, paragrafo 2.
# A fonte externa art. 97 nao integra este recorte; renumeracao futura exige gate N:N.
referencia=next(r for r in rows if r["artigo"]=="3" and r["unidade"]=="P2")
assert referencia["id_origem"]=="LEI-1976-6404-ART003-P2"
assert referencia["id_destino_simbolico"]=="CLF-T18-M01-SA-ART003-P2"
assert "(artigo 97)" in referencia["texto_fonte_editorial"]
assert "(artigo 97)" in referencia["texto_destino_documental"]
assert referencia["texto_destino_documental"] in view
codigo=(P/"produto/CODIGO_DE_TRABALHO.md").read_text(encoding="utf-8")
assert referencia["texto_destino_documental"] in codigo
porta=P/"modulos/T18/M01_GATE_REMISSAO_ART3P2_A97_20261016.md"
assert porta.is_file() and "Lei 8.934/1994" in porta.read_text(encoding="utf-8")
assert m["dec016"]=="PENDENTE" and m["material_approved"] is False and m["dou_facsimile_checked"] is False
with (P/"central/44_R30_AUDITORIA_T18_T34_T36_CI_20261016.csv").open(encoding="utf-8",newline="") as f:g=list(csv.DictReader(f,strict=True))
assert len(g)==9 and len({r["id"] for r in g})==9
assert sum(r["titulo"]=="T18" for r in g)==6
books=json.loads((P/"produto/fontes/indice_livros.json").read_text(encoding="utf-8"))["livros"]
t18=[b for b in books if b["titulo"]=="T18"]
assert len(t18)==1 and t18[0]["artigos"]==3 and t18[0]["registros_documentais"]==8
print("OK T18 documental: 3 artigos/8 unidades Q, nove gates, SHA conferido.")
print("DOU, CI verde, C0-J e DEC-016 nao certificados.")
