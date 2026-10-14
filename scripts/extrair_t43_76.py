#!/usr/bin/env python3
"""Extração artigo-local das 76 unidades T43.M04 da Lei 14.129/2021.

O inventário fornece os IDs; o HTML da Câmara fornece os textos. O teste exige
cobertura 76/76, dois vetos e concordância de 16 unidades com espelho manual.
É extração documental: NÃO atesta DOU, cadeia temporal nem C0-J do futuro CLF.
"""
import argparse
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

BASE=pathlib.Path(__file__).resolve().parents[1]/"modulos/T43/M04"
URL="https://www2.camara.leg.br/legin/fed/lei/2021/lei-14129-29-marco-2021-791203-normaatualizada-pl.html"
ARTICLES={1,2,3,4,5,6,7,8,9,42,43}
ART=re.compile(r"^Art\.\s*(\d{1,2})(?:º|\.)\s*(.*)$")
PAR=re.compile(r"^§\s*(\d+)\s*º\s*(.*)$")
SINGLE=re.compile(r"^Parágrafo único\.\s*(.*)$",re.I)
ROMAN=re.compile(r"^(I|II|III|IV|V|VI|VII|VIII|IX|X|XI|XII|XIII|XIV|XV|XVI|XVII|XVIII|XIX|XX|XXI|XXII|XXIII|XXIV|XXV|XXVI)\s*[-–]\s*(.*)$")

def norm(s):
    s=unicodedata.normalize("NFC",str(s).replace("\u00a0"," ").replace("\u200b",""))
    return re.sub(r"\s+"," ",s).strip()

def source():
    req=urllib.request.Request(URL,headers={"User-Agent":"CLF-auditoria-legislativa/0.2"})
    last=None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req,timeout=65) as resp:
                raw=resp.read(7_000_000)
            soup=BeautifulSoup(raw,"html.parser")
            for element in soup(["script","style","nav","footer"]): element.decompose()
            chunks=[norm(x) for x in soup.get_text("\n",strip=True).splitlines()]
            chunks=[x for x in chunks if x]
            if len(chunks)<200 or not any("Art. 43." in x for x in chunks):
                raise ValueError("Documento Câmara incompleto ou formato alterado")
            return chunks, {"url":URL,"sha256":hashlib.sha256(raw).hexdigest(),
                            "obtido_utc":datetime.now(timezone.utc).isoformat(),
                            "tamanho_bytes":len(raw),"linhas_extraidas":len(chunks)}
        except (OSError,TimeoutError) as e:
            last=e
            print(f"Fonte temporariamente indisponível, tentativa {attempt+1}/3: {type(e).__name__}",flush=True)
            if attempt!=2:time.sleep(4*(attempt+1))
    raise ConnectionError(f"Não foi possível consultar a fonte Câmara: {last}")

def extract(lines):
    result={}
    active=None
    para=None
    last=None
    for line in lines:
        a=ART.match(line)
        if a:
            number=int(a.group(1))
            # O art. 43 só ocorre na lei própria quando fora de citações.
            active=number if number in ARTICLES else None
            para=None
            last=None
            if active is not None:
                key=(active,"C")
                if key in result:raise ValueError(f"Artigo duplicado na edição: {key}")
                result[key]=line
                last=key
            continue
        if active is None: continue
        p=PAR.match(line)
        if p:
            unit=f"P{p.group(1)}"
            key=(active,unit)
            if key in result:
                # Uma referência quebrada à unidade não é marcador novo, mas
                # exige inspeção, não aceitação silenciosa.
                raise ValueError(f"Parágrafo duplicado: {key}; linha={line[:120]}")
            result[key]=line
            para=unit
            last=key
            continue
        s=SINGLE.match(line)
        if s:
            key=(active,"PU")
            if key in result:raise ValueError(f"Parágrafo único duplicado {key}")
            result[key]=line
            para=None
            last=key
            continue
        i=ROMAN.match(line)
        if i:
            roman=i.group(1)
            unit=f"{para}-{roman}" if active==7 and para=="P1" else roman
            key=(active,unit)
            if key in result:raise ValueError(f"Inciso duplicado: {key}")
            result[key]=line
            last=key
            continue
        if last and not re.match(r"^(?:CAPÍTULO|SEÇÃO|Seção|Subseção|DA |DO |DAS |DOS |DISPOSIÇÕES)\b",line):
            # Elementos inline frequentemente fragmentam referências, como
            # "art. 198 ..." e nomes de leis em linhas separadas.
            result[last]=norm(result[last]+" "+line)
    return result

def main():
    a=argparse.ArgumentParser()
    a.add_argument("--json",required=True)
    a.add_argument("--csv",required=True)
    args=a.parse_args()
    with (BASE/"INVENTARIO_F1_PRIORITARIO.csv").open(encoding="utf-8-sig",newline="") as f:
        inv=list(csv.DictReader(f))
    with (BASE/"F1A_ESPELHO_LITERAL_02_42_43.csv").open(encoding="utf-8-sig",newline="") as f:
        gold=list(csv.DictReader(f))
    if len(inv)!=76 or len(set(x["id_fonte"] for x in inv))!=76:raise ValueError("Inventário: 76 IDs únicos exigidos")
    if len(gold)!=16:raise ValueError("Espelho focal: 16 linhas exigidas")
    line,meta=source()
    parsed=extract(line)
    expected={}
    for row in inv:
        ident=row["id_fonte"]
        mat=re.search(r"-ART-(\d{4})-(.+)$",ident)
        if not mat:raise ValueError(f"ID inesperado: {ident}")
        key=(int(mat.group(1)),mat.group(2))
        if key in expected:raise ValueError(f"ID repetido para chave {key}")
        expected[key]=ident
    missing=set(expected)-set(parsed)
    unexpected=set(parsed)-set(expected)
    if missing or unexpected:
        raise ValueError(f"Cobertura falhou. AUSENTES={sorted(missing)}, EXTRAS={sorted(unexpected)}")
    veto={(4,"I"),(7,"P1-V")}
    if {key for key,t in parsed.items() if "(VETADO)" in t} != veto:
        raise ValueError("Dispositivos vetados divergentes dos dois identificados")
    original={row["id_fonte"]:row for row in gold}
    rows=[]
    failed=[]
    for key,ident in expected.items():
        txt=parsed[key]
        normtext=norm(txt)
        goldtext=norm(original[ident]["texto_compilado_camara_2026"]) if ident in original else ""
        igual=not goldtext or normtext==goldtext
        item={"id_fonte":ident,"artigo":key[0],"subunidade":key[1],
              "texto_extraido_compilado_2026":txt,
              "tipo":"VETADO_SEM_CONTEUDO" if key in veto else "TEXTO_EXISTENTE",
              "espelho_focal_confrontado":"SIM" if ident in original else "NAO",
              "teste_focal":"OK" if igual else "DIFERENCA_VERIFICAR",
              "estado_juridico":"Q","fonte":URL,
              "pendencia":"Revisão humana, redação original 2021/DOU, remissões, espécie e C0-J"}
        rows.append(item)
        if not igual:failed.append((ident,goldtext[:120],normtext[:120]))
    output={"fontes":{"consolidado":meta},
            "total_inventario":76,"vetos":2,"unidades_existentes":74,
            "cotejo_independente_16":len(original),"falhas_espelho_16":len(failed),
            "equivalencia_juridica":"Q","unidades":rows}
    for dest in (args.csv,args.json):pathlib.Path(dest).parent.mkdir(parents=True,exist_ok=True)
    with open(args.json,"w",encoding="utf-8") as f:json.dump(output,f,indent=2,ensure_ascii=False)
    with open(args.csv,"w",encoding="utf-8",newline="") as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]))
        writer.writeheader();writer.writerows(rows)
    print(f"T43.M04 F1-C 76/76 extraídas; 74 substantivas, dois vetos; 16 controles, divergências={len(failed)}")
    for x in failed[:16]:print(f"CONTROLE NAO COINCIDE {x}")
    if failed:return 1
    print("Apenas concordância documental com consolidação Câmara; C0-J continua Q.")
    return 0

if __name__=="__main__":
    try:sys.exit(main())
    except Exception as exc:
        print(f"FALHA_EXTRACAO_76: {type(exc).__name__}: {exc}",file=sys.stderr)
        sys.exit(2)
