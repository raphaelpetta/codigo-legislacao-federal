#!/usr/bin/env python3
"""CLF R28: QA documental e de classes de vigência, não DOU ou C0-J."""
import csv, hashlib, json
from pathlib import Path
P=Path(__file__).resolve().parents[1]
m=json.loads((P/"produto/fontes/T34_M01_MUSEUS_10_R28_v1.json").read_text(encoding="utf-8"))
raw=(P/m["source_path"]).read_bytes()
sha=hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
assert sha==m["source_blob_sha"]
with (P/m["source_path"]).open(encoding="utf-8",newline="") as f:rs=list(csv.DictReader(f,strict=True))
assert len(rs)==m["count_expected"]==10
assert len({r["artigo"] for r in rs})==m["articles_expected"]==2
assert len({r["id_origem"] for r in rs})==10 and len({r["id_destino_simbolico"] for r in rs})==10
assert sum(r["unidade"]=="C" for r in rs)==2
assert {r["unidade"] for r in rs if r["artigo"]=="1"}=={"C","PU"}
assert {r["unidade"] for r in rs if r["artigo"]=="2"}=={"C","PU","I","II","III","IV","V","VI"}
assert all(r["estado_juridico"]=="Q_SEM_C0_J" and r["texto_fonte_editorial"]==r["texto_destino_documental"] for r in rs)
view=(P/m["view_path"]).read_text(encoding="utf-8")
assert sha in view and all(r["texto_destino_documental"] in view for r in rs)
assert sum(line.startswith("**Art. ") for line in view.splitlines())==2
assert m["dec016"]=="PENDENTE" and m["material_approved"] is False and m["dou_facsimile_checked"] is False
with (P/"central/40_R28_MUSEUS_PNC_URBANISMO_VIGENCIA_20261016.csv").open(encoding="utf-8",newline="") as f:g=list(csv.DictReader(f,strict=True))
assert len(g)==7 and len({r["id"] for r in g})==7
status={r["id"]:r["estado_no_corte"] for r in g}
assert status["R28-MUSEU-003"]=="PLANO_2010_2024_ENCERRADO"
assert status["R28-MUSEU-004"]=="PROPOSICAO_SEM_POSITIVACAO"
assert status["R28-URB-001"]=="EFICAZ_NO_CORTE"
assert status["R28-URB-002"]=="NAO_EFICAZ_EM_2026_10_16"
assert status["R28-URB-003"]=="NAO_APLICAR_REVOGACAO_EM_2026"
idx=json.loads((P/"produto/fontes/indice_livros.json").read_text(encoding="utf-8"))["livros"]
assert sum(b["artigos"] for b in idx if b["titulo"]=="T34")==2
assert sum(b["registros_documentais"] for b in idx if b["titulo"]=="T34")==10
print("R28 DOCUMENTAL: 10 unidades T34 e 7 gates de vigência/PNC, sem C0-J.")
