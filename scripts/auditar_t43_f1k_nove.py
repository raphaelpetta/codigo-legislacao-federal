#!/usr/bin/env python3
"""F1-K: nove textos da Lei14.129/2021 em suas quatro leis de destino (2026).

Conferência documental com dois lados, falha se o texto de origem não estiver
na edição da Lei14.129 ou não aparecer no diploma consolidado de destino.
Não comprova inexistência de alteração superveniente, C0-J ou espécie CLF.
"""
import csv,hashlib,json,pathlib,re,time,unicodedata,urllib.request
from bs4 import BeautifulSoup
from datetime import datetime,timezone
ROOT=pathlib.Path(__file__).resolve().parents[1]/"modulos/T43/M04"
P=ROOT/"F1K_NOVE_DESTINOS_LITERAL_2021_2026.csv"
def norm(v):
    v=unicodedata.normalize("NFC",v.replace("\u00a0"," ").replace("\u200b",""))
    v=v.replace("“",'"').replace("”",'"').replace("‘","'").replace("’","'")
    return re.sub(r"\s+"," ",v).strip()
def fetch(url):
    last=None
    for attempt in range(3):
        try:
            r=urllib.request.Request(url,headers={"User-Agent":"CLF-historico/2026-10"})
            with urllib.request.urlopen(r,timeout=60) as response:raw=response.read(9_000_000)
            soup=BeautifulSoup(raw,"html.parser")
            for e in soup(["script","style","nav","footer"]):e.decompose()
            full=norm(soup.get_text(" ",strip=True))
            if len(full)<450:raise RuntimeError("Fonte curta")
            return full,{"url":url,"sha256":hashlib.sha256(raw).hexdigest(),"bytes":len(raw)}
        except (TimeoutError,OSError) as e:
            last=e
            if attempt<2:time.sleep(4*(attempt+1))
    raise ConnectionError(f"Fonte inacessível: {url}: {last}")
with P.open(encoding="utf-8-sig",newline="") as f:rows=list(csv.DictReader(f))
assert len(rows)==9 and len({r["id_destino"] for r in rows})==9
assert {r["lei_destino"] for r in rows}=={"7116","12527","12682","13460"}
assert {r["artigo_alterador_2021"] for r in rows}=={"Lei14129 art51","Lei14129 art52","Lei14129 art53","Lei14129 art54"}
urls=sorted({r["url_alteradora"] for r in rows}|{r["url_consolidado_destino"] for r in rows})
assert len(urls)==5,"Uma fonte alteradora e quatro fontes consolidadas"
texts={u:fetch(u) for u in urls}
details=[]
errors=[]
for r in rows:
    literal=norm(r["texto_introduzido_2021"])
    origin=texts[r["url_alteradora"]][0]
    target=texts[r["url_consolidado_destino"]][0]
    origin_matches=origin.count(literal)
    target_matches=target.count(literal)
    if not origin_matches or not target_matches:
        errors.append({"id":r["id_destino"],"origem":origin_matches,"destino":target_matches,
                       "amostra":literal[:140]})
    if r["estado_c0j"]!="Q":errors.append({"id":r["id_destino"],"status":"promovido"})
    details.append({"id":r["id_destino"],"origem_ocorrencias":origin_matches,
                    "destino_ocorrencias":target_matches,"controle_juridico":r["controle_juridico"],
                    "C0_J":"Q"})
out={"corte":"2026-10-14","consultado_utc":datetime.now(timezone.utc).isoformat(),
     "fontes":{url:metadata for url,(_,metadata) in texts.items()},
     "total_posicoes":9,"resultados":details,"falhas":errors,
     "limite":"Dois retratos normativos, não reconstrução DOU completa nem certificação C0-J."}
path=pathlib.Path("/tmp/t43-f1k-nove.json")
path.write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding="utf-8")
print(f"T43 F1-K nove: {len(rows)} posições, {len(texts)} fontes oficiais, erros={len(errors)}")
for e in errors:print("DIVERGENCIA:",e)
if errors:raise AssertionError(f"{len(errors)} fragmentos precisando revisão")
print("Todas as nove redações de 2021 ainda aparecem na consolidação pesquisada; estado C0-J Q.")
