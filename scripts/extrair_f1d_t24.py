#!/usr/bin/env python3
"""Auditoria F1-D: extrair 75 unidades CPC 82–97 de duas publicações da Câmara.

Resultado técnico por subunidade em CSV e JSON; não é certificação de vigência,
C0-J, cadeia DOU ou equivalência para o CLF. Exit 1 em falha de cobertura.
"""
from __future__ import annotations

import argparse
import csv
import difflib
import hashlib
import json
import pathlib
import re
import sys
import unicodedata
import urllib.request
from datetime import datetime, timezone
from bs4 import BeautifulSoup

ROOT = pathlib.Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "modulos/T24/M01/F1D_INVENTARIO_ART82_97_SUBUNIDADES.csv"
ORIGINAL = "https://www2.camara.leg.br/legin/fed/lei/2015/lei-13105-16-marco-2015-780273-publicacaooriginal-146341-pl.html"
UPDATED = "https://www2.camara.leg.br/legin/fed/lei/2015/lei-13105-16-marco-2015-780273-normaatualizada-pl.html"
ARTICLES = list(range(82, 98))
ADDED = {(82, "P3"), (85, "P6A"), (85, "P8A"), (85, "P20")}
ARTICLE = re.compile(r"^Art\.\s*(\d{1,4})\.\s*(.*)$")
PARA = re.compile(r"^§\s*(\d{1,2})[ºo°]?(?:\s*[-–]\s*([A-Z]))?\.?\s*(.*)$", re.I)
ROMAN = re.compile(r"^([IVXLCDM]{1,6})\s*[-–]\s*(.*)$", re.I)
SINGLE = re.compile(r"^Parágrafo\s+único\.\s*(.*)$", re.I)

def norm(t):
    return re.sub(r"\s+", " ", unicodedata.normalize("NFC", t.replace("\u00a0", " "))).strip()

def source(url):
    request = urllib.request.Request(url, headers={"User-Agent":"CLF textual-verifier research 2026"})
    with urllib.request.urlopen(request, timeout=50) as resp:
        raw = resp.read(10_000_000)
    soup = BeautifulSoup(raw, "html.parser")
    for tag in soup(["script","style","nav","footer"]):
        tag.decompose()
    lines = [norm(x) for x in soup.get_text("\n",strip=True).splitlines() if norm(x)]
    if sum(1 for l in lines if ARTICLE.match(l) and int(ARTICLE.match(l).group(1)) in ARTICLES) < 16:
        raise ValueError(f"Fonte sem cobertura 82–97: {url}")
    # Auditoria secundária: blocos HTML <p> preservam texto inline em uma
    # única unidade, enquanto get_text("\\n") pode separar <span>, <em> e
    # hiperlinks, criando falsos diffs. Não substituir silenciosamente fonte A.
    blocos = [norm(p.get_text(" ",strip=True)) for p in soup.find_all("p")]
    blocos = [s for s in blocos if s]
    return lines, {"url":url,"sha256":hashlib.sha256(raw).hexdigest(),"bytes":len(raw),
                   "consulta_utc":datetime.now(timezone.utc).isoformat(),
                   "paragraph_blocks":len(blocos)}, blocos

def extract(lines):
    """Captura marcadores de dispositivo dentro de cada art., nunca substring global."""
    units={}
    current=None
    paragraph=None
    previous=None
    for line in lines:
        art=ARTICLE.match(line)
        if art:
            a=int(art.group(1))
            current=a if a in ARTICLES else None
            paragraph=None
            previous=None
            if current is not None:
                key=(current,"C")
                if key in units: raise ValueError(f"Artigo duplicado na fonte: {key}; antes={units[key][:140]!r}; nova={line[:140]!r}")
                units[key]=norm(art.group(2))
                previous=key
            continue
        if current is None: continue
        # Capturar parágrafo único como unidade própria, com continuidade em outra linha.
        single=SINGLE.match(line)
        if single:
            key=(current,"PU")
            if key in units: raise ValueError(f"Parágrafo único duplicado: {key}")
            units[key]=norm(single.group(1))
            previous=key
            paragraph=None
            continue
        # Testar marcadores de parágrafos e incisos no segmento do artigo atual.
        p=PARA.match(line)
        if p:
            n=int(p.group(1))
            letter=(p.group(2) or "").upper()
            paragraph=f"P{n}{letter}"
            key=(current,paragraph)
            if key in units:
                # Fragmento de citação do parágrafo (por exemplo "§ 8º deste artigo")
                # quebrado em linha pelo HTML, não uma nova unidade.
                if previous and re.match(r"^(?:deste|desse|daquele|desta|desse|do|da|dos|das|ou|e)\b",p.group(3),re.I):
                    units[previous]=norm(units[previous]+" "+line)
                    continue
                raise ValueError(f"Parágrafo duplicado na fonte: {key}; antes={units[key][:170]!r}; nova={line[:170]!r}")
            units[key]=norm(p.group(3))
            previous=key
            continue
        roman=ROMAN.match(line)
        if roman:
            key=(current,(paragraph+"-" if paragraph else "")+roman.group(1).upper())
            if key in units: raise ValueError(f"Inciso duplicado na fonte: {key}")
            units[key]=norm(roman.group(2))
            previous=key
            continue
        # Fragmentos de continuidade: não incluir notas de editor, headings ou footnotes.
        if previous and line and not re.match(r"^(Seção|Subseção|Capítulo|Livro|Título|Texto|Lei nº|Parágrafo acrescido|Vide |Regulamenta)",line,re.I):
            if len(line)>30 and not line.startswith("(") and not line.startswith("【"):
                units[previous] = norm(units[previous]+" "+line)
    return units

def article_blocks(lines):
    """Texto de cada artigo em uma das fontes; preserva fragmentos HTML separados."""
    blocks = {}
    active = None
    for line in lines:
        m=ARTICLE.match(line)
        if m:
            num=int(m.group(1))
            active=num if num in ARTICLES else None
        if active is not None:
            blocks.setdefault(active,[]).append(line)
    return {k:norm(" ".join(v)) for k,v in blocks.items()}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--json",required=True)
    parser.add_argument("--csv",required=True)
    args=parser.parse_args()
    with INVENTORY.open(encoding="utf-8-sig",newline="") as f:
        inventory=list(csv.DictReader(f))
    if len(inventory)!=75 or len({r["id_origem"] for r in inventory})!=75:
        raise ValueError("Inventário não contém exatamente 75 origens únicas")
    orig_lines, orig_meta, orig_par=source(ORIGINAL)
    now_lines, now_meta, now_par=source(UPDATED)
    orig=extract(orig_lines)
    now=extract(now_lines)
    now_articles=article_blocks(now_lines)
    original_articles=article_blocks(orig_lines)
    secondary_error=None
    try:
        # Só aceitar extração secundária se houver os 16 caputs sem duplicação.
        orig_secondary=extract(orig_par)
        now_secondary=extract(now_par)
        if any((a,"C") not in orig_secondary or (a,"C") not in now_secondary for a in ARTICLES):
            raise ValueError("Método de blocos não localizou os 16 artigos nas duas fontes")
    except Exception as exc:
        orig_secondary={}
        now_secondary={}
        secondary_error=f"{type(exc).__name__}: {exc}"
    print("BLOCOS_HTML_ORIGINAL", len(orig_par), "ATUAL",len(now_par),
          "METODO_SECUNDARIO", secondary_error or "ATIVO")
    records=[]
    bad=[]
    for item in inventory:
        art=int(item["dispositivo"].split()[-1])
        unit=item["subunidade"]
        key=(art,unit)
        original=orig.get(key)
        current=now.get(key)
        expected_absent=key in ADDED
        if current is None:
            status="ERRO_AUSENTE_ATUAL"
        elif original is None and expected_absent:
            status="ACRESCIDO_VERIFICAR_LEI"
        elif original is None:
            status="ERRO_AUSENTE_ORIGINAL_NAO_ESPERADO"
        elif expected_absent:
            status="ERRO_ACRESCIMO_PRESENTE_ORIGINAL"
        elif norm(original)==norm(current):
            status="IGUAL_NOS_TEXTOS_EXTRAIDOS"
        else:
            status="DIVERGENCIA_DE_EXTRACAO_OU_EDICAO_A_AUDITAR"
        secundario_original=orig_secondary.get(key)
        secundario_atual=now_secondary.get(key)
        if secondary_error:
            extra="METODO_SEGUNDARIO_INDISPONIVEL"
        elif secundario_atual is None:
            extra="AUSENTE_BLOCO_ATUAL"
        elif secundario_original is None:
            extra="AUSENTE_BLOCO_ORIGINAL"
        elif norm(secundario_original)==norm(secundario_atual):
            extra="PAR_LITERAL_IGUAL_POR_BLOCO_HTML"
        else:
            extra="BLOCOS_HTML_TAMBEM_DIVERGEM"
        # Contraprova: a redação original INTEIRA existe como sequência contígua
        # dentro do MESMO artigo na edição atual? Uma diferença causada apenas
        # pelo corte do parser pode assim ser isolada da mudança legislativa.
        ocorrencias_texto_2015_no_artigo_atual = (
            now_articles.get(art,"").count(norm(original)) if original else 0)
        inteiro_atual_mesmo_artigo = ocorrencias_texto_2015_no_artigo_atual == 1
        inteiro_original_mesmo_artigo = (bool(current) and
            norm(current) in original_articles.get(art,""))
        truncado = (bool(original and current)
            and norm(original).startswith(norm(current))
            and len(norm(original))>len(norm(current)))
        if status=="DIVERGENCIA_DE_EXTRACAO_OU_EDICAO_A_AUDITAR":
            if truncado and inteiro_atual_mesmo_artigo:
                status="FALSO_POSITIVO_PARSER_FONTE_ATUAL_CONFERE_ARTIGO"
            elif inteiro_atual_mesmo_artigo:
                status="CORRESPONDENCIA_COMPLETA_FONTE_ATUAL_PARSER_DIVERGE"
        diff=""
        if original and current and norm(original)!=norm(current):
            matches=difflib.SequenceMatcher(None,norm(original),norm(current),autojunk=False)
            for tag,i1,i2,j1,j2 in matches.get_opcodes():
                if tag!="equal":
                    diff=(f"{tag}: 2015[{i1}:{i2}]={norm(original)[max(0,i1-60):i2+60]!r}; "
                          f"2026[{j1}:{j2}]={norm(current)[max(0,j1-60):j2+60]!r}")
                    break
        row={
          "id_origem":item["id_origem"],"artigo":art,"subunidade":unit,
          "original_extraido":original or "AUSENTE","atual_extraido":current or "AUSENTE",
          "texto_original_localizado_inteiro_no_artigo_atual":inteiro_atual_mesmo_artigo,
          "ocorrencias_de_texto_original_no_artigo_atual":ocorrencias_texto_2015_no_artigo_atual,
          "texto_atual_completo_conferido":(
              norm(original) if status=="FALSO_POSITIVO_PARSER_FONTE_ATUAL_CONFERE_ARTIGO"
              else (norm(current) if status=="IGUAL_NOS_TEXTOS_EXTRAIDOS"
                    else "AINDA_NAO_CERTIFICADO")),
          "metodo_prova":"OCORRENCIA_UNICA_TEXTO_LITERAL_NO_MESMO_ARTIGO_CPC",
          "texto_atual_localizado_no_artigo_original":inteiro_original_mesmo_artigo,
          "suposta_truncagem_na_versao_atual":truncado,
          "metodo_bloco":extra,"bloco_original":secundario_original or "AUSENTE",
          "bloco_atual":secundario_atual or "AUSENTE", "primeira_diferenca":diff,
          "resultado":status,"esperado_acrescimo":expected_absent,"status_juridico":"Q",
          "fonte_2015":ORIGINAL,"fonte_2026":UPDATED,"reserva":"SEM_C0_J_E_SEM_CERTIFICACAO_DOU"
        }
        records.append(row)
        if status.startswith("ERRO"): bad.append(row)
    result={"objetivo":"extracao por artigo, sem ato juridico CLF",
            "fontes":{"original":orig_meta,"atual":now_meta},
            "quantidade_prevista":75,"quantidade_processada":len(records),
            "erro_segunda_extracao":secondary_error,
            "classes_metodo_bloco":{s:sum(r["metodo_bloco"]==s for r in records) for s in sorted({r["metodo_bloco"] for r in records})},
            "falhas_estruturais":len(bad),
            "localizacoes_versao_2015":len(orig),
            "localizacoes_versao_2026":len(now),
            "resultado_contagens": {s:sum(x["resultado"]==s for x in records)
                                   for s in sorted({r["resultado"] for r in records})},
            "resultados":records}
    for target in (args.csv,args.json):
        pathlib.Path(target).parent.mkdir(parents=True, exist_ok=True)
    with open(args.csv,"w",encoding="utf-8",newline="") as f:
        writer=csv.DictWriter(f,fieldnames=records[0].keys())
        writer.writeheader()
        writer.writerows(records)
    with open(args.json,"w",encoding="utf-8") as f:
        json.dump(result,f,ensure_ascii=False,indent=2)
    print("F1-D CPC 82–97 — "+json.dumps(result["resultado_contagens"],ensure_ascii=False))
    for r in records:
        if r["resultado"] not in ("IGUAL_NOS_TEXTOS_EXTRAIDOS","ACRESCIDO_VERIFICAR_LEI"):
            # A linha permanece auditável; a existência do texto original
            # dentro do artigo atualizado é evidência, não certificação C0-J.
            
            print("EXAMINAR",r["id_origem"],r["resultado"],r["metodo_bloco"],"DIFF:",r["primeira_diferenca"][:280])
    if bad:
        print(f"FALHA DE COBERTURA: {len(bad)} registros. Não classificar C0-T/C0-J.")
        return 1
    print("Cobertura automática de 75 unidades com fontes e SHA256; revisão humana/DOU pendentes")
    return 0

if __name__=="__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"INCONCLUSIVO: {e!r}",file=sys.stderr)
        sys.exit(2)
