#!/usr/bin/env python3
"""T43.M04: 16 unidades literais dos arts.2,42,43 Lei 14.129/2021.

Controla IDs estruturais 76 e dois vetos, busca o texto das 16 unidades
na página atualizada Câmara com SHA256. Não faz concordância DOU/C0-J.
"""
import csv
import hashlib
import json
import pathlib
import re
import sys
import time
import unicodedata
import urllib.request
from datetime import datetime, timezone
from bs4 import BeautifulSoup

ROOT=pathlib.Path(__file__).resolve().parents[1]
FOLDER=ROOT/"modulos/T43/M04"
URL="https://www2.camara.leg.br/legin/fed/lei/2021/lei-14129-29-marco-2021-791203-normaatualizada-pl.html"
def normalize(v):
    v=unicodedata.normalize("NFC",str(v).replace("\u00a0"," ").replace("\u200b",""))
    v=re.sub(r"\s+"," ",v).strip()
    v=re.sub(r"\s+([,;:.])",r"\1",v)
    return v

def source():
    req=urllib.request.Request(URL,headers={"User-Agent":"CLF-legislative-research/0.1"})
    err=None
    for n in range(3):
        try:
            with urllib.request.urlopen(req,timeout=65) as response:
                data=response.read(5_000_000)
            soup=BeautifulSoup(data,"html.parser")
            for tag in soup(["script","style","nav","footer"]):tag.decompose()
            full=normalize(soup.get_text(" ",strip=True))
            if len(full)<8000 or "Art. 43." not in full:
                raise ValueError("Conteúdo da fonte insuficiente")
            return full,{"url":URL,"sha256":hashlib.sha256(data).hexdigest(),
                         "consulta_utc":datetime.now(timezone.utc).isoformat(),
                         "bytes":len(data)}
        except (OSError, TimeoutError) as exc:
            err=exc
            print(f"Tentativa Câmara {n+1}/3 falhou: {type(exc).__name__}",flush=True)
            if n<2:time.sleep(4*(n+1))
    raise RuntimeError(f"Fonte inacessível após três tentativas: {err!r}")

def main():
    with (FOLDER/"INVENTARIO_F1_PRIORITARIO.csv").open(encoding="utf-8",newline="") as f:
        all_rows=list(csv.DictReader(f))
    with (FOLDER/"F1A_ESPELHO_LITERAL_02_42_43.csv").open(encoding="utf-8",newline="") as f:
        rows=list(csv.DictReader(f))
    ids={r["id_fonte"] for r in all_rows}
    if len(all_rows)!=76 or len(ids)!=76: raise ValueError("Inventário não contém 76 unidades únicas")
    veto=[r["id_fonte"] for r in all_rows if r["vigencia_situacao"]=="VETADO_SEM_TEXTO_NORMATIVO"]
    if len(veto)!=2 or not any("-ART-0004-I" in x for x in veto) or not any("-ART-0007-P1-V" in x for x in veto):
        raise ValueError("Registro dos dois vetos incompleto")
    if len(rows)!=16 or len({r["id_fonte"] for r in rows})!=16: raise ValueError("Espelho não contém 16 unidades")
    if any(r["id_fonte"] not in ids for r in rows):raise ValueError("Espelho com ID fora do inventário")
    page,src=source()
    tests=[]
    for r in rows:
        norm=normalize(r["texto_compilado_camara_2026"])
        count=page.count(norm)
        tests.append({"id":r["id_fonte"],"ocorrencias_em_pagina":count,
                      "resultado":"LOCALIZADO" if count>=1 else "NAO_LOCALIZADO"})
    report={"fonte":src,"inventario_total":len(all_rows),"itens_vetados":veto,
            "texto_focal_total":len(rows),"nao_localizados":sum(x["resultado"]!="LOCALIZADO" for x in tests),
            "Q_juridico":True,"resultados":tests}
    output=pathlib.Path("/tmp/validacao_t43_f1a_16.json")
    output.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
    print("T43.M04 F1A: 76 IDs estruturais, 2 vetos e 16 textos; divergências:",report["nao_localizados"])
    for x in tests:
        if x["resultado"]!="LOCALIZADO":print("ERRO_TEXTUAL",x["id"])
    if report["nao_localizados"]:return 1
    print("Texto localizado externamente, não equivale a C0-J ou DOU.")
    return 0
if __name__=="__main__":
    try:sys.exit(main())
    except Exception as e:
        print(f"INCONCLUSIVO_T43: {type(e).__name__}: {e}",file=sys.stderr)
        sys.exit(2)
