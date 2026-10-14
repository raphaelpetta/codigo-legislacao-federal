#!/usr/bin/env python3
"""T43 F1-J: confronto de cinco redações literais 2021, 2023 e compiladas.

Fontes: Lei 14.129/2021 como veículo alterador, Lei 14.534/2023 como
alteração posterior, e os dois diplomas de destino na Câmara.
Distingue redação de origem, inovação material, vigência e implementação.
Não constitui homologação C0-J. Falha fechada quando fontes não coincidem.
"""
import csv, hashlib, json, pathlib, re, sys, time, unicodedata, urllib.request
from bs4 import BeautifulSoup
from datetime import datetime,timezone
BASE=pathlib.Path(__file__).resolve().parents[1]/"modulos/T43/M04"
CSV=BASE/"F1J_COTEJO_LITERAL_5_POSICOES_2021_2023.csv"
def norm(s):
    s=unicodedata.normalize("NFC",s.replace("\u00a0"," ").replace("\u200b",""))
    s=s.replace("“",'"').replace("”",'"').replace("‘","'").replace("’","'")
    return re.sub(r"\s+"," ",s).strip()
def fetch(url):
    err=None
    for k in range(3):
        try:
            req=urllib.request.Request(url,headers={"User-Agent":"CLF-auditoria-2026/0.4"})
            with urllib.request.urlopen(req,timeout=60) as r:raw=r.read(7_000_000)
            bs=BeautifulSoup(raw,"html.parser")
            for t in bs(["script","style","nav","footer"]):t.decompose()
            lines=[norm(x) for x in bs.get_text("\n",strip=True).splitlines() if norm(x)]
            return norm(" ".join(lines)),{"url":url,"sha256":hashlib.sha256(raw).hexdigest(),"bytes":len(raw)}
        except (OSError,TimeoutError) as e:
            err=e
            if k<2:time.sleep(3*(k+1))
    raise RuntimeError(f"Fonte inacessível: {url}: {err}")
with CSV.open(encoding="utf-8-sig",newline="") as f:rows=list(csv.DictReader(f))
assert len(rows)==5 and len({r["id_destino"] for r in rows})==5
urls={r[k] for r in rows for k in ("fonte_redacao_2021","fonte_redacao_2023","fonte_texto_vigente")}
sources={u:fetch(u) for u in sorted(urls)}
report=[]
failed=[]
for r in rows:
    checks={}
    for col,field in (("texto_redacao_lei14129_2021","fonte_redacao_2021"),
                      ("texto_redacao_lei14534_2023","fonte_redacao_2023"),
                      ("texto_redacao_lei14534_2023","fonte_texto_vigente")):
        actual=sources[r[field]][0]
        expected=norm(r[col])
        found=actual.count(expected)
        checks[f"{col}_em_{field}"]=found
        if found<1:failed.append([r["id_destino"],col,field,expected[:110]])
    report.append({"id":r["id_destino"],"classificacao":r["classificacao_alteracao"],
                    "checagens":checks,"C0_J":"Q"})
out={"auditado_utc":datetime.now(timezone.utc).isoformat(),"fontes":{u:m for u,(_,m) in sources.items()},
     "posicoes":len(rows),"divergencias":failed,"resultados":report,
     "limite":"Duas leis alteradoras e suas versões de destino; sem facsimile DOU, homologacao C0-J ou novo prazo de vigência."}
path=pathlib.Path("/tmp/t43-f1j-cotejo5.json")
path.write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding="utf8")
print("T43 F1-J: cinco alterações, quatro fontes oficiais, divergências=",len(failed))
for error in failed:print("FALTA_LITERAL",error)
if failed:sys.exit(1)
print("Confronto literal aprovado nas duas redações e no destino compilado; todos C0-J Q.")
