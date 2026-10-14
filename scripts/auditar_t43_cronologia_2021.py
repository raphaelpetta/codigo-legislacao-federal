#!/usr/bin/env python3
"""T43 F1-H: indexacao de cinco publicacoes oficiais 2021.

Reconstitui a cadeia editorial sem presumir equivalencia normativa.
As paginas HTML servem como prova publicada, nao prova do inteiro DOU.
"""
import csv, hashlib, json, pathlib, re, sys, time, urllib.request
from bs4 import BeautifulSoup
from datetime import datetime,timezone
BASE=pathlib.Path(__file__).resolve().parents[1]/"modulos/T43/M04"
NAME="MATRIZ_F1H_CINCO_EVENTOS_DOU_2021.csv"
def textnorm(s):return " ".join(s.replace("\u00a0"," ").split())
def fetch(url):
    err=None
    for i in range(3):
        try:
            req=urllib.request.Request(url,headers={"User-Agent":"CLF-f1h-auditoria/2026"})
            with urllib.request.urlopen(req,timeout=65) as f:raw=f.read(6_000_000)
            soup=BeautifulSoup(raw,"html.parser")
            for x in soup(["script","style","nav","footer"]):x.decompose()
            body=textnorm(soup.get_text(" ",strip=True))
            if len(body)<400:raise RuntimeError("pagina muito curta")
            return body,hashlib.sha256(raw).hexdigest()
        except (OSError,TimeoutError) as ex:
            err=ex
            if i<2:time.sleep(3*(i+1))
    raise RuntimeError(f"Falha transporte da Câmara: {err}")
with (BASE/NAME).open(encoding="utf-8-sig",newline="") as f:rows=list(csv.DictReader(f))
if len(rows)!=5 or [x["data"] for x in rows]!=["2021-03-30","2021-04-14","2021-04-27","2021-06-10","2021-06-11"]:
    raise AssertionError("cinco marcos precisam de ordem estrita")
by_url={}
results=[]
for item in rows:
    url=item["url_camara"]
    if url not in by_url:by_url[url]=fetch(url)
    body,sha=by_url[url]
    tag=item["evento"]
    if tag=="PUBLICACAO_ORIGINAL":
        if "VETADO" not in body or "Art. 32." not in body:raise AssertionError("original incompleta")
    elif tag=="REPUBLICACAO_ART32":
        if "REPUBLICAÇÃO" not in body or "Art. 32." not in body or "VETADO" not in body:
            raise AssertionError("republicacao art32 não encontrada")
    elif tag=="RETIFICACAO_RAZOES_VETO_ART32":
        if "RETIFICAÇÃO" not in body or "Leia-se:" not in body or "inconsistências" not in body:
            raise AssertionError("retificacao de RAZÕES não encontrada")
    elif tag in ("PROMULGACAO_ASSINATURA","PUBLICACAO_PROMULGACAO"):
        if "Art. 35." not in body or "10 (dez) dias" not in body or "5 (cinco) dias" not in body:
            raise AssertionError("arts32/35 não restaurados em publicação de promulgação")
    if item["c0_j"]!="Q":raise AssertionError("evento histórico não homologa C0-J")
    results.append({"data":item["data"],"tipo":tag,"url":url,"hash_sha256":sha,
       "marcadores_oficiais":"CONFERIDOS","natureza":item["natureza_juridica"],"c0_j":"Q"})
out={"data_auditoria_utc":datetime.now(timezone.utc).isoformat(),
     "fontes_distintas":len(by_url),"eventos":results,
     "limite":"HTML Camara, sem facsimiles DOU e sem homologacao juridica C0-J"}
path=pathlib.Path("/tmp/t43-f1h-cronologia.json")
path.write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding="utf8")
print("T43 F1-H OK: cinco marcos, quatro páginas oficiais distintas, SHA256, estados Q.")
