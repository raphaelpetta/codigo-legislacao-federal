#!/usr/bin/env python3
"""F1-D10 — gera REDLINE DOCUMENTAL art85 CPC em texto integral (36 unidades).

Compara textos de duas edições da Câmara, como documento de pesquisa.
Não altera numeração jurídica, não aprova C0-J nem a forma de CLF.
"""
import argparse
import csv
import json
import pathlib
import subprocess
import sys
import tempfile
from collections import defaultdict

ROOT=pathlib.Path(__file__).resolve().parents[1]
MODULE=ROOT/"modulos/T24/M01"
def load(name):
    with (MODULE/name).open(encoding="utf-8-sig",newline="") as f:
        return list(csv.DictReader(f))
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--markdown",required=True)
    p.add_argument("--index",required=True)
    args=p.parse_args()
    with tempfile.TemporaryDirectory() as d:
        j=str(pathlib.Path(d)/"art85.json")
        c=str(pathlib.Path(d)/"art85.csv")
        subprocess.run([sys.executable,str(ROOT/"scripts/espelho_art85_t24.py"),
            "--json",j,"--csv",c],check=True)
        obj=json.loads(pathlib.Path(j).read_text(encoding="utf8"))
    units=obj["resultados"]
    cross=load("F1D9_CROSSWALK_35_REMISSOES_SIMBOLICAS.csv")
    if len(units)!=36 or len(cross)!=35:
        raise AssertionError("Exigir 36 unidades e 35 referências")
    symbolic={r["id_fonte"]:r["secao_simbolica_origem"] for r in cross}
    rem=defaultdict(list)
    for r in cross:rem[r["id_fonte"]].append(r["secao_simbolica_destino"])
    added={"P6A","P8A","P20"}
    got_added={u["subunidade"] for u in units if u["status_cotejo_textual"].startswith("ACRESCIDO")}
    if got_added!=added:raise AssertionError("Precisam ser só três acréscimos: §§6A,8A,20")
    lines=[
        "# CPC art. 85 — redline documental completo de 36 unidades",
        "",
        "Corte: 14/10/2026. Pesquisa de duas fotografias oficiais, sem cadeia DOU completa.",
        "Não é norma CLF aprovada, renumeração válida nem concordância C0-J.",
        "Os marcadores T24.M01.HON.* são IDs internos e não artigos.",
        "Jurisprudência em parecer F1-D7 e modulação Tema1190 em F1-D8.",
        "Original: "+obj["fontes"]["original"]["url"],
        "Compilada: "+obj["fontes"]["compilada"]["url"],
        "SHA-256 original: "+obj["fontes"]["original"]["sha256"],
        "SHA-256 compilada: "+obj["fontes"]["compilada"]["sha256"],
        "",
        "## Contagens",
        "36 unidades: 33 iguais nos dois retratos, 3 acréscimos Lei14.365/2022; C0-J Q.",
        ""
    ]
    index=[["id_origem","unidade","destino_simbolico","resultado_comparativo","remissoes_expressas","estado"]]
    for n,u in enumerate(units,1):
        key=u["id_fonte"]
        unit=u["subunidade"]
        symbol=symbolic.get(key,"T24.M01.HON."+unit)
        inserted=unit in added
        old=u["texto_publicacao_2015"]
        new=u["texto_compilado_2026"]
        if not new or new=="AUSENTE":raise AssertionError("Texto compilado ausente "+unit)
        if inserted:
            if old!="INEXISTENTE_PUBLICACAO_ORIGINAL_2015":raise AssertionError("Acréscimo com texto de 2015: "+unit)
            classification="INSERCAO_DE_2022"
        else:
            if old!=new:raise AssertionError("Mudança não explicada "+unit)
            classification="SEM_DIFERENCA_ENTRE_DOIS_RETRATOS"
        index.append([key,unit,symbol,classification,len(rem[key]),"Q_NAO_HOMOLOGADO"])
        lines.extend([
            "## "+str(n).zfill(2)+" — "+key+" ("+unit+")",
            "",
            "Classificação: "+classification+". Destino simbólico: "+symbol+".",
            "Referências explícitas: "+("; ".join(rem[key]) if rem[key] else "nenhuma indexada")+".",
            "",
            "**Publicação original de 2015**",
            "",
            "~~~text",old,"~~~","",
            "**Texto compilado de 2026**",
            "",
            "~~~text",new,"~~~","",
            "Gate: Q jurídico; falta DOU, escopo, garantias, remissões e competência.",
            ""
        ])
    if sum(r[3]=="INSERCAO_DE_2022" for r in index[1:])!=3:
        raise AssertionError("Contagem de inserções inválida")
    pathlib.Path(args.markdown).parent.mkdir(parents=True,exist_ok=True)
    pathlib.Path(args.markdown).write_text("\n".join(lines),encoding="utf-8")
    with open(args.index,"w",encoding="utf-8",newline="") as f:
        csv.writer(f).writerows(index)
    print("F1-D10 OK: 36 unidades textuais integrais, 33 iguais, 3 acréscimos em 2022, 35 remissões; todos Q.")
if __name__=="__main__":main()
