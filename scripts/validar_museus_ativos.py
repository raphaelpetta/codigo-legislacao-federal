#!/usr/bin/env python3
"""CLF Museus R29: 10+11 unidades Q e veto historico excluido, sem C0-J."""
from pathlib import Path
import json,csv,hashlib
P=Path(__file__).resolve().parents[1]
paths=["produto/fontes/T34_M01_MUSEUS_10_R28_v1.json","produto/fontes/T34_M01_MUSEUS_11_R29_v1.json"]
for path,arts,units in zip(paths,[2,4],[10,11]):
 m=json.loads((P/path).read_text(encoding="utf-8"))
 raw=(P/m["source_path"]).read_bytes()
 sha=hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
 assert sha==m["source_blob_sha"]
 with (P/m["source_path"]).open(encoding="utf-8",newline="") as f:r=list(csv.DictReader(f,strict=True))
 assert len(r)==units==m["count_expected"]
 assert sum(x["unidade"]=="C" for x in r)==arts==m["articles_expected"]
 assert len({x["id_origem"] for x in r})==units==len({x["id_destino_simbolico"] for x in r})
 assert all(x["estado_juridico"]=="Q_SEM_C0_J" and x["texto_fonte_editorial"]==x["texto_destino_documental"] for x in r)
 view=(P/m["view_path"]).read_text(encoding="utf-8")
 assert sha in view and all(x["texto_destino_documental"] in view for x in r)
 assert sum(t.startswith("**Art. ") for t in view.splitlines())==arts
 assert m["material_approved"] is False and m["dec016"]=="PENDENTE"
m=json.loads((P/paths[1]).read_text(encoding="utf-8"))
assert len(m["historical_nonpositive"])==1
v=m["historical_nonpositive"][0]
assert v["article"]=="5" and v["unit"]=="P3" and v["status"]=="VETADO" and v["positive_count"]==0
with (P/m["source_path"]).open(encoding="utf-8",newline="") as f:r=list(csv.DictReader(f))
assert not any(x["artigo"]=="5" and x["unidade"]=="P3" for x in r)
with (P/"central/42_R29_AUDITORIA_MUSEUS_VETO_E_TRANSICOES_20261016.csv").open(encoding="utf-8",newline="") as f:g=list(csv.DictReader(f,strict=True))
assert len(g)==11 and len({x["id"] for x in g})==11
assert any(x["controle"]=="VETO" and x["categoria"]=="Q_HISTORICO_EXCLUIDO" for x in g)
assert all(x["categoria"]!="C0_J_HOMOLOGADO" for x in g)
books=json.loads((P/"produto/fontes/indice_livros.json").read_text(encoding="utf-8"))["livros"]
t=[b for b in books if b["titulo"]=="T34"]
assert len(t)==2 and sum(b["artigos"] for b in t)==6 and sum(b["registros_documentais"] for b in t)==21
print("OK Q T34 6 artigos/21 unidades, 1 veto histórico excluído, 11 gates.")
