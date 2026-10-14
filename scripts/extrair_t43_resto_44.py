#!/usr/bin/env python3
"""T43 F1-E: 44 artigos restantes da Lei 14.129/21 na Câmara consolidada.

Espelho de ARTIGOS, não de suas subunidades. Distingue artigos alteradores
de outras leis, um veto e vacatio. NÃO verifica C0-J, DOU ou revogação.
"""
import csv
import hashlib
import json
import pathlib
import re
import sys
import time
import urllib.request
from datetime import datetime,timezone
from bs4 import BeautifulSoup

ROOT=pathlib.Path(__file__).resolve().parents[1]/"modulos/T43/M04"
SRC="https://www2.camara.leg.br/legin/fed/lei/2021/lei-14129-29-marco-2021-791203-normaatualizada-pl.html"
EXPECTED=set(range(10,42))|set(range(44,56))
ART=re.compile(r"^Art\.\s*(\d{1,2})(?:º|\.)\s*(.*)$")
def fetch():
    req=urllib.request.Request(SRC,headers={"User-Agent":"CLF-edicao-legal-check/2026"})
    last=None
    for k in range(3):
        try:
            with urllib.request.urlopen(req,timeout=65) as response:
                data=response.read(8_000_000)
            soup=BeautifulSoup(data,"html.parser")
            for t in soup(["script","style","nav","footer"]):t.decompose()
            lines=[" ".join(x.replace("\u00a0"," ").split()) for x in soup.get_text("\n",strip=True).splitlines()]
            lines=[x for x in lines if x]
            if len(lines)<200:raise ValueError("Fonte HTML curta demais")
            return lines,{"url":SRC,"bytes":len(data),"sha256":hashlib.sha256(data).hexdigest(),"obtido_utc":datetime.now(timezone.utc).isoformat()}
        except (OSError,TimeoutError) as e:
            last=e
            if k<2:time.sleep(4*(k+1))
    raise ConnectionError(f"Fonte Câmara indisponível: {last}")
def blocks(lines):
    bodies={}
    current=None
    for s in lines:
        match=ART.match(s)
        if match:
            n=int(match.group(1))
            # Apenas artigos primários: art. 3º e art. 12 nas normas
            # ALTERADAS aparecem entre aspas, portanto não são cabeçalhos.
            if n in bodies:raise ValueError(f"Artigo principal duplicado: {n}")
            current=n
            bodies[n]=[s]
        elif current is not None:
            if s.startswith("Brasília, 29 de março de 2021"):
                current=None
            else:
                bodies[current].append(s)
    return {n:"\n".join(lines) for n,lines in bodies.items()}
def main():
    with (ROOT/"INVENTARIO_F1E_RESTANTE_ARTIGOS_10_41_44_55.csv").open(encoding="utf-8-sig",newline="") as f:
        arr=list(csv.DictReader(f))
    nums=[int(x["dispositivo"].split()[1]) for x in arr]
    if len(nums)!=44 or len(set(nums))!=44 or set(nums)!=EXPECTED:
        raise ValueError(f"Inventário restante deve ser exatamente 44 artigos; recebido {nums}")
    lines,meta=fetch()
    data=blocks(lines)
    expected_all=set(range(1,56))
    if set(data)!=expected_all:
        raise ValueError(f"Artigos principais fora de 1–55: ausentes={sorted(expected_all-set(data))}; extras={sorted(set(data)-expected_all)}")
    out=[]
    for row in arr:
        n=int(row["dispositivo"].split()[1])
        chunk=data[n]
        kind=row["natureza_do_artigo"]
        if n==46:
            if "VETADO" not in chunk[:300]:
                raise ValueError("Art.46 deveria ser VETADO, conferir texto")
        if n in (51,52,53,54) and "passa" not in chunk[:300].lower():
            raise ValueError(f"Artigo alterador {n} não traz comando 'passa'")
        if n==55 and not all(x in chunk for x in ("90 (noventa) dias","120 (cento e vinte) dias","180 (cento e oitenta) dias")):
            raise ValueError("Art.55 não contém três vacatios escalonadas")
        out.append({"id_fonte":row["id_fonte"],"artigo":n,"natureza":kind,
                    "texto_consolidado_camara":chunk,"status_juridico":"Q",
                    "pendencia":"DOU original e consolidado; cadeia historica; auditoria por subunidade; alcance federativo",
                    "fonte":SRC})
    results={"fonte":meta,"artigos_principais_detectados":len(data),
             "artigos_restantes":len(out),
             "natureza_contagens":{x:sum(z["natureza"]==x for z in out) for x in sorted({z["natureza"] for z in out})},
             "resultados":out}
    pathlib.Path("/tmp").mkdir(exist_ok=True)
    with open("/tmp/t43-44-artigos.json","w",encoding="utf8") as f:json.dump(results,f,indent=2,ensure_ascii=False)
    with open("/tmp/t43-44-artigos.csv","w",newline="",encoding="utf8") as f:
        w=csv.DictWriter(f,fieldnames=out[0].keys());w.writeheader();w.writerows(out)
    print(f"OK: 55 artigos principais até art.55; {len(out)} restantes, categorias={results['natureza_contagens']}")
    print("Apenas texto extraído por artigo. C0-J pendente. Norma alteradora não deve ser copiada em duplicidade.")
if __name__=="__main__":
    try:main()
    except Exception as exc:
        print(f"FALHA_EXTRACAO_RESTANTE: {type(exc).__name__}: {exc}",file=sys.stderr)
        sys.exit(2)
