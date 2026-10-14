#!/usr/bin/env python3
"""T43.M04 F1-F: indexacao de caputs, paragrafos, incisos, alineas dos arts10-41,44-55.

NUNCA interpreta este espelho como texto normativo CLF, C0-J ou historico DOU.
Para 51-54 (leis alteradoras) apenas cabecalho e bloco integro, sem integrar
como se a lei alterada nao existisse. O art32 foi vetado e restaurado pelo
Congresso, conforme nota da Camara/DOU 11/06/2021. Vetos mantidos identificados.
"""
import argparse
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
URL="https://www2.camara.leg.br/legin/fed/lei/2021/lei-14129-29-marco-2021-791203-normaatualizada-pl.html"
REMAINING=set(range(10,42))|set(range(44,56))
ARTICLE=re.compile(r"^Art\.\s*(\d{1,2})(?:º|\.)\s*(.*)$")
PAR=re.compile(r"^§\s*(\d+)\s*º\s*(.*)$")
SINGLE=re.compile(r"^Parágrafo único\.\s*(.*)$",re.I)
ROMAN=re.compile(r"^(I|II|III|IV|V|VI|VII|VIII|IX|X|XI|XII|XIII|XIV|XV|XVI|XVII|XVIII|XIX|XX|XXI|XXII|XXIII|XXIV|XXV|XXVI)\s*[-–]\s*(.*)$")
LETTER=re.compile(r"^([a-z])\)\s+(.*)$")
HEAD=re.compile(r"^(?:CAPÍTULO|SEÇÃO|Seção|Subseção|DA |DO |DAS |DOS |DISPOSIÇÕES|Subseção|Brasília,)\b",re.I)

def norm(s):
    return " ".join(s.replace("\u00a0"," ").replace("\u200b","").split()).strip()

def source():
    req=urllib.request.Request(URL,headers={"User-Agent":"CLF-norma-cotejo-fino/2026"})
    last=None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req,timeout=65) as resp:raw=resp.read(9_000_000)
            soup=BeautifulSoup(raw,"html.parser")
            for element in soup(["script","style","nav","footer"]):element.decompose()
            lines=[norm(x) for x in soup.get_text("\n",strip=True).splitlines()]
            lines=[x for x in lines if x]
            if len(lines)<250:raise ValueError("Fonte oficial com cobertura insuficiente")
            return lines,{"url":URL,"sha256":hashlib.sha256(raw).hexdigest(),"data_utc":datetime.now(timezone.utc).isoformat(),"bytes":len(raw)}
        except (OSError,TimeoutError) as exc:
            last=exc
            print(f"Falha transitoria leitura Câmara {attempt+1}/3: {type(exc).__name__}",flush=True)
            if attempt!=2:time.sleep(4*(attempt+1))
    raise ConnectionError(f"Erro ao obter fonte oficial: {last}")

def parse(lines):
    """Um inciso pertence ao ultimo paragrafo se este nao foi encerrado.
    Artigos alteradores 51-54 mantidos como 1 bloco com seu texto integral,
    para nao confundir artigos das leis alteradas com a lei fonte.
    """
    result={}
    art=None
    par=None
    inc=None
    last=None
    for line in lines:
        m=ARTICLE.match(line)
        if m:
            n=int(m.group(1))
            art=n if n in REMAINING else None
            par=inc=last=None
            if art is not None:
                key=(art,"C")
                if key in result:raise ValueError(f"Artigo principal duplicado: {key}")
                result[key]=line
                last=key
            continue
        if art is None:continue
        # Disposições 51–54 alteram outras leis: manter artigo inteiro,
        # inclusive marcadores internos de dispositivos reproduzidos.
        if art>=51 and art<=54:
            result[(art,"C")]=norm(result[(art,"C")]+" "+line)
            continue
        if HEAD.match(line):
            last=None
            continue
        m=PAR.match(line)
        if m:
            par="P"+m.group(1)
            inc=None
            key=(art,par)
            if key in result:raise ValueError(f"Paragrafo duplicado {key}, linha={line[:100]}")
            result[key]=line
            last=key
            continue
        m=SINGLE.match(line)
        if m:
            par="PU";inc=None
            key=(art,par)
            if key in result:raise ValueError(f"Paragrafo unico duplicado {key}")
            result[key]=line;last=key
            continue
        m=ROMAN.match(line)
        if m:
            inc=m.group(1)
            # Dentro de um artigo, apos paragrafo anterior, ha em certos
            # artigos um novo conjunto romano dentro do caput? Auditar
            # sequencia e rejeitar colisao; nao normalizar silenciosamente.
            unit=f"{par}-{inc}" if par else inc
            key=(art,unit)
            if key in result:raise ValueError(f"Inciso duplicado {key}; linha={line[:100]}")
            result[key]=line;last=key
            continue
        m=LETTER.match(line)
        if m:
            letter=m.group(1)
            if not inc:
                raise ValueError(f"Alinea sem inciso artigo {art}: {line[:100]}")
            unit=f"{par+'-' if par else ''}{inc}-{letter}"
            key=(art,unit)
            if key in result:raise ValueError(f"Alinea repetida: {key}")
            result[key]=line;last=key
            continue
        if last:
            result[last]=norm(result[last]+" "+line)
    return result

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--csv",required=True)
    parser.add_argument("--json",required=True)
    args=parser.parse_args()
    with (ROOT/"INVENTARIO_F1E_RESTANTE_ARTIGOS_10_41_44_55.csv").open(encoding="utf-8-sig",newline="") as f:
        inventory=list(csv.DictReader(f))
    article_ids={int(row["dispositivo"].split()[1]) for row in inventory}
    if len(article_ids)!=44 or article_ids!=REMAINING:raise ValueError("Inventario de 44 artigos faltante")
    lines,metadata=source()
    data=parse(lines)
    articles={x[0] for x in data}
    if articles!=REMAINING:
        raise ValueError(f"Artigos incompletos; ausentes={sorted(REMAINING-articles)} extras={sorted(articles-REMAINING)}")
    if len(data)<160:
        raise ValueError(f"Menos de 160 unidades nos 44 artigos: {len(data)}. Parser/HTML suspeitos")
    must_contain={(24,"I-a"),(24,"I-b"),(28,"P1-I"),(28,"P1-XV"),(28,"P5"),
                  (29,"P1-VII"),(29,"P3"),(29,"P2-XII"),(32,"C"),(46,"C"),
                  (45,"X"),(47,"PU-III")}
    # Em art.47 os incisos pertencem ao parágrafo único.
    missing=must_contain-set(data)
    if missing:raise ValueError(f"Subunidades obrigatorias nao detectadas: {sorted(missing)}")
    if "(VETADO)" not in data[(28,"P5")] or "(VETADO)" not in data[(29,"P1-VII")] or "(VETADO)" not in data[(29,"P3")]:
        raise ValueError("Vetos internos dos arts28 e29 não foram capturados")
    if "(VETADO)" not in data[(46,"C")]:
        raise ValueError("Art46 não parece VETADO")
    if "(VETADO)" in data[(32,"C")][:80]:
        raise ValueError("Art32 reintegrado por derrubada de veto não pode ser classificado como vetado atual")
    if "passa" not in data[(51,"C")][:150].lower():
        raise ValueError("Lei alteradora art51 incorretamente extraida")
    kinds={int(row["dispositivo"].split()[1]):row["natureza_do_artigo"] for row in inventory}
    out=[]
    for (art,unit),val in sorted(data.items(),key=lambda x:(x[0][0],len(x[0][1]),x[0][1])):
        veto="(VETADO)" in val[:140]
        out.append({
            "id_fonte":f"BR-LEI-2021-14129-ART-{art:04}-{unit}",
            "artigo":art,"subunidade":unit,
            "texto_extraido":val,
            "situacao":"VETADO_SEM_COMANDO" if veto else ("ALTERADOR_NAO_RECODIFICAR_DUPLICADO" if 51<=art<=54 else "TEXTO_CONSOLIDADO_A_AUDITAR"),
            "categoria_artigo":kinds[art],
            "url_oficial":URL,"data_consulta":"2026-10-14",
            "estado_equivalencia":"Q_NAO_HOMOLOGADO",
            "pendencia":"DOU/cadeia historica, conferência manual, remissoes e competencia; art32 veto derrubado"
        })
    veto=[z["id_fonte"] for z in out if z["situacao"]=="VETADO_SEM_COMANDO"]
    expected_veto={f"BR-LEI-2021-14129-ART-{a:04}-{u}" for a,u in [(28,"P5"),(29,"P1-VII"),(29,"P3"),(46,"C")]}
    if set(veto)!=expected_veto:
        raise ValueError(f"Vetos divergentes: {veto}")
    pathlib.Path(args.csv).parent.mkdir(parents=True,exist_ok=True)
    pathlib.Path(args.json).parent.mkdir(parents=True,exist_ok=True)
    with open(args.csv,"w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(out[0]));w.writeheader();w.writerows(out)
    result={"fonte":metadata,"qtd_44_artigos":len(articles),"total_unidades_finas":len(out),"vetos_internos_e_artigo":veto,
            "art32_veto_derrubado":"TEXTO_VIGENTE_NA_EDICAO_CÂMARA_COM_NOTA_DOU_2021_06_11",
            "texto_sem_concordancia_juridica":True,"unidades":out}
    with open(args.json,"w",encoding="utf-8") as f:json.dump(result,f,ensure_ascii=False,indent=2)
    print(f"T43 F1-F: {len(articles)} artigos, {len(out)} unidades, {len(veto)} vetos; art32 vigente após derrubada do veto.")
    print("Todas Q jurídico. Artigos alteradores mantidos fora de recodificação duplicada.")
if __name__=="__main__":
    try:main()
    except Exception as e:
        print(f"FALHA_F1F: {type(e).__name__}: {e}",file=sys.stderr)
        sys.exit(2)
