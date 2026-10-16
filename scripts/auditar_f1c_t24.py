#!/usr/bin/env python3
"""Auditoria textual independente de 106 subunidades CPC na publicação Câmara.

Lê dois HTML externos ao CLF; registra hash da fonte e ocorrências de cada unidade.
Não certifica vigência, DOU, equivalência C0-J ou sentido jurídico.
Exit 0 somente com 106 correspondências em cada versão e ausências esperadas.
"""
import argparse
import csv
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
CPC = ROOT / "modulos/T24/M01"
FILES = [
    "F1C_COTEJO_LITERAL_ART70_81_73_UNIDADES.csv",
    "F1C_COTEJO_LITERAL_ART98_102_33_UNIDADES.csv",
]
URL_ORIGINAL = "https://www2.camara.leg.br/legin/fed/lei/2015/lei-13105-16-marco-2015-780273-publicacaooriginal-146341-pl.html"
URL_ATUAL = "https://www2.camara.leg.br/legin/fed/lei/2015/lei-13105-16-marco-2015-780273-normaatualizada-pl.html"


def normalize(text):
    text = unicodedata.normalize("NFC", str(text)).replace("\u00a0", " ").replace("\u200b", "")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "CLF-normative-audit/0.1 (academic research)"})
    with urllib.request.urlopen(req, timeout=40) as resp:
        raw = resp.read(5_000_000)
        content_type = resp.headers.get("Content-Type", "")
    if b"Art. 70" not in raw and b"Art. 70" not in raw.replace(b"&nbsp;", b" "):
        # A ausência do marcador em bytes pode decorrer de HTML com marcação; a
        # confirmação real virá após parsing abaixo.
        pass
    soup = BeautifulSoup(raw, "html.parser")
    for tag in soup(["script", "style", "nav", "footer"]):
        tag.decompose()
    full = normalize(soup.get_text(" ", strip=True))
    if len(full) < 10000 or "Art. 70" not in full or "Art. 99" not in full:
        raise ValueError(f"Fonte inacessível/inadequada: {url}, caracteres={len(full)}")
    return {
        "url": url, "sha256": hashlib.sha256(raw).hexdigest(),
        "retrieved_utc": datetime.now(timezone.utc).isoformat(),
        "content_type": content_type, "length_html": len(raw),
        "length_plain": len(full), "plain": full
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", required=True)
    args = parser.parse_args()
    sources = {"original": fetch(URL_ORIGINAL), "atual": fetch(URL_ATUAL)}
    rows = []
    for filename in FILES:
        with (CPC / filename).open(encoding="utf-8-sig", newline="") as stream:
            for r in csv.DictReader(stream):
                r["_arquivo"] = filename
                rows.append(r)
    seen = [r["id_origem"] for r in rows]
    if len(rows) != 106 or len(set(seen)) != 106:
        raise ValueError(f"Esperadas 106 origens únicas; localizadas {len(rows)} linhas e {len(set(seen))} IDs")
    result = []
    for r in rows:
        finding = {"id": r["id_origem"], "artigo": r["artigo"],
                   "subunidade": r["subunidade"], "arquivo": r["_arquivo"]}
        for key, field in (("original", "texto_publicacao_2015"), ("atual", "texto_compilado_2026")):
            query = normalize(r[field])
            if query == "INEXISTENTE_NA_PUBLICACAO_ORIGINAL":
                status = "AUSENTE_ESPERADO_POR_HISTORICO"
                # Critério negativo confirmado por ausência da variante nova no texto antigo:
                candidate = normalize(r["texto_compilado_2026"])
                # Não é prova absoluta de ausência de unidade: apenas não encontrou redação nova.
                present = candidate in sources[key]["plain"]
                status = "INCONSISTENCIA_NOVO_TEXTO_NO_ORIGINAL" if present else status
                finding[key] = {"status": status, "nova_redacao_presente": present}
            else:
                hits = sources[key]["plain"].count(query)
                finding[key] = {"status": "LOCALIZADO_LITERAL" if hits else "NAO_LOCALIZADO",
                                "ocorrencias": hits, "caracteres": len(query)}
        result.append(finding)
    bad = [r for r in result if any(
        r[k]["status"] not in ("LOCALIZADO_LITERAL", "AUSENTE_ESPERADO_POR_HISTORICO")
        for k in ("original", "atual")
    )]
    external = {k: {kk:vv for kk,vv in data.items() if kk!="plain"} for k,data in sources.items()}
    report = {"criterio": "busca literal normalizada do conteúdo das unidades no texto integral da fonte externa; não equivalência jurídica",
              "fontes": external, "unidades": len(result), "falhas": len(bad),
              "classificacao": "Q_C0_J_PENDENTE",
              "resultados": result}
    report_path = pathlib.Path(args.report)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"CPC T24/F1-C: {len(result)} subunidades; {len(bad)} divergências; hashes externos no JSON.")
    for b in bad[:35]:
        print(f"NAO CONFERIDO: {b['id']} original={b['original']['status']} atual={b['atual']['status']}")
    if bad:
        print("INCONCLUSIVO: corrigir transcrições/normalização ou conferir fonte; não certificar C0-T.")
        return 1
    print("CONFERENCIA TEXTUAL POSITIVA na publicação original e compilada, sujeita a DOU/efeitos/escopo.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        print(f"AUDITORIA INCONCLUSIVA: {type(exc).__name__}: {exc}", file=sys.stderr)
        sys.exit(2)
