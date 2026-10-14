#!/usr/bin/env python3
"""Auditoria da cadeia de vetos na Lei 14.129/2021.

Compara a publicação original (30/03/2021) à compilação Câmara (2026);
usa a matriz de vetos do portal da Câmara como autoridade para estado
jurídico. A nota do veto sobre o art32 PU é mais relevante que a mera
presença gráfica de texto na publicação original.
"""
import csv
import hashlib
import importlib.util
import json
import pathlib
import re
import sys
import time
import urllib.request
from datetime import datetime, timezone
from bs4 import BeautifulSoup

ROOT=pathlib.Path(__file__).resolve().parents[1]
SCRIPT=ROOT/"scripts/extrair_t43_restante_fino.py"
spec=importlib.util.spec_from_file_location("f1f",SCRIPT)
f1f=importlib.util.module_from_spec(spec)
spec.loader.exec_module(f1f)
SPEC_76=importlib.util.spec_from_file_location("f1c",ROOT/"scripts/extrair_t43_76.py")
f1c=importlib.util.module_from_spec(SPEC_76)
SPEC_76.loader.exec_module(f1c)
DIRECTORY=ROOT/"modulos/T43/M04"
URL_ORIGINAL="https://www2.camara.leg.br/legin/fed/lei/2021/lei-14129-29-marco-2021-791203-publicacaooriginal-162567-pl.html"
URL_VETOS="https://www2.camara.leg.br/legin/fed/lei/2021/lei-14129-29-marco-2021-791203-norma-pl.html"
URL_PROMULG="https://www2.camara.leg.br/legin/fed/lei/2021/lei-14129-29-marco-2021-791203-promulgacaodevetos-162975-pl.html"
def original():
    req=urllib.request.Request(URL_ORIGINAL,headers={"User-Agent":"CLF-auditoria-vetos/2026"})
    err=None
    for n in range(3):
        try:
            with urllib.request.urlopen(req,timeout=65) as r:raw=r.read(8_000_000)
            soup=BeautifulSoup(raw,"html.parser")
            for tag in soup(["script","style","nav","footer"]):tag.decompose()
            lines=[f1f.norm(x) for x in soup.get_text("\n",strip=True).splitlines()]
            return [x for x in lines if x],{
                "url":URL_ORIGINAL,"sha256":hashlib.sha256(raw).hexdigest(),
                "obtido_utc":datetime.now(timezone.utc).isoformat(),"bytes":len(raw)}
        except (OSError,TimeoutError) as e:
            err=e
            if n<2:time.sleep(4*(n+1))
    raise RuntimeError(f"Falha na publicação original: {err!r}")
def main():
    with (DIRECTORY/"MATRIZ_F1G_NOVE_POSICOES_VETOS_2021.csv").open(encoding="utf-8-sig",newline="") as f:
        rows=list(csv.DictReader(f))
    if len(rows)!=9 or len({r["id_historico"] for r in rows})!=9:
        raise AssertionError("Exatamente nove posições históricas de veto")
    oldlines,ometa=original()
    lines,nmeta=f1f.source()
    old=f1f.parse(oldlines)
    current=f1f.parse(lines)
    # O F1-F, por definição, não varre os arts. 1–9. A história dos
    # vetos desses dispositivos exige o parser específico F1-C.
    old_early=f1c.extract(oldlines)
    now_early=f1c.extract(lines)
    for key in [(4,"I"),(7,"P1-V")]:
        old[key]=old_early.get(key,"")
        current[key]=now_early.get(key,"")
    expected_rejected={(32,"C"),(35,"C")}
    expected_maintained={(4,"I"),(7,"P1-V"),(28,"P5"),(29,"P1-VII"),(29,"P3"),(32,"PU"),(46,"C")}
    keyset=set()
    verified=[]
    for row in rows:
        m=re.search(r"ART-(\d{4})-(.+)$",row["id_historico"])
        if not m:raise AssertionError(f"ID histórico inválido: {row}")
        key=(int(m.group(1)),m.group(2))
        keyset.add(key)
        rejected=row["resultado_veto_congresso"]=="REJEITADO"
        if (key in expected_rejected)!=rejected:
            raise AssertionError(f"Veto sem classificação correta {key}")
        if key in expected_maintained and row["resultado_veto_congresso"]!="MANTIDO":
            raise AssertionError(f"Veto mantido mal classificado {key}")
        a=old.get(key,"")
        b=current.get(key,"")
        if key in expected_rejected:
            if "(VETADO)" not in a[:70] or not b or "(VETADO)" in b[:80]:
                raise AssertionError(f"Promulgação não documentada em duas fotos: {key}: {a[:80]} / {b[:80]}")
        elif key==(32,"PU"):
            # A publicação inicial traz uma redação para o parágrafo único,
            # mas a Câmara indica que o veto a ele foi MANTIDO.
            # O texto não pode ser recodificado como vigente.
            if not a or b:
                raise AssertionError("Art32 PU vetado ficou indevidamente vigente/ausente no original")
        else:
            if "(VETADO)" not in b[:80]:
                raise AssertionError(f"Veto mantido sem marcação na compilação: {key} {b[:80]}")
        verified.append({
            "id":row["id_historico"],"resultado_veto":row["resultado_veto_congresso"],
            "texto_original_presente":bool(a),"texto_compilado_presente":bool(b),
            "amostra_original":a[:160],"amostra_compilado":b[:160],
            "aprovacao_tecnica":"ESTADO_RECONCILIADO","equivalencia_juridica":"Q"
        })
    if keyset!=expected_rejected|expected_maintained:raise AssertionError("Cobertura das nove posições divergente")
    if "10 (dez) dias" not in current[(35,"C")]:
        raise AssertionError("Prazo recursal art35 caput não encontrado")
    if "5 (cinco) dias" not in current[(35,"PU")]:
        raise AssertionError("Prazo da autoridade superior art35 PU não encontrado")
    if "inconsistências" not in current[(32,"C")]:
        raise AssertionError("Caput restaurado art32 faltante")
    output={
        "escopo":"Posições de veto (9), origens 2021 e compilação 2026. DOU identificado pelo portal da Câmara; não é parecer C0-J.",
        "fontes":{"original":ometa,"compilada":nmeta,"ficha_veto":URL_VETOS,"promulgacao":URL_PROMULG},
        "posicoes":9,"vetos_mantidos":7,"vetos_rejeitados":2,
        "art32_paragrafo_unico":"VETO_MANTIDO_SEM_TEXTO_VIGENTE",
        "art35_paragrafo_unico":"VIGENTE_COM_PROMULGACAO_DO_ARTIGO",
        "registros":verified}
    pathlib.Path("/tmp/t43-f1g-vetos.json").write_text(json.dumps(output,ensure_ascii=False,indent=2),encoding="utf8")
    print("F1-G VETOS OK: 9 posições; 7 mantidos (6 visíveis na compilação + art32 PU suprimido); 2 rejeitados (arts32 e35).")
    print("Art35 caput e PU presentes (10 dias recurso; 5 dias autoridade); art32 PU sem vigência. C0-J Q.")
if __name__=="__main__":
    try:main()
    except Exception as exc:
        print(f"FALHA_F1G_VETOS: {type(exc).__name__}: {exc}",file=sys.stderr)
        sys.exit(2)
