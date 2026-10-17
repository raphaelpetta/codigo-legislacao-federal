#!/usr/bin/env python3
"""Gate de 23 unidades Q da Lei 9.709/1998, arts. 3–15. NÃO C0-J.

Manifestações institucionais podem divergir editorialmente. O CSV é uma
fotografia fiel da transcrição experimental (Câmara HTML), não do DOU.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PR80="37babdb31da5b37b7c905ae51f3b7590b39e85f7"
BLOB="1923dcd2ec15f7ebccd1458c9100567b1376924c"
REQUIRED={
 "3":("decreto legislativo","um terço","compõem"),
 "4":("plebiscito","lei complementar","Assembléias Legislativas"),
 "5":("plebiscito","Assembléia Legislativa"),
 "6":("Estados","Distrito Federal","Municípios"),
 "7":("população diretamente interessada","total da população consultada"),
 "8":("Presidente do Congresso Nacional","Justiça Eleitoral"),
 "9":("sustada sua tramitação","resultado das urnas"),
 "10":("maioria simples","Tribunal Superior Eleitoral"),
 "11":("trinta dias","promulgação"),
 "12":("Regimento Comum do Congresso Nacional",),
 "13":("um por cento do eleitorado nacional","cinco Estados","três décimos por cento"),
 "14":("cumprimento das exigências","art. 13"),
 "15":("Esta Lei entra em vigor na data de sua publicação.",),
}
EXPECTED_UNITS={"3":{"C"},"4":{"C","P1","P2","P3","P4"},"5":{"C"},"6":{"C"},
"7":{"C"},"8":{"C","I","II","III","IV"},"9":{"C"},"10":{"C"},"11":{"C"},
"12":{"C"},"13":{"C","P1","P2"},"14":{"C"},"15":{"C"}}

def need(condition,why):
    if not condition:
        raise ValueError(why)

def blob(path):
    data=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()

def csvrows(path):
    with path.open(encoding="utf-8-sig",newline="") as handle:
        return list(csv.DictReader(handle,strict=True))

def verify(rows,meta):
    need(meta["source_blob_sha"]==BLOB and meta["source_commit"]==PR80
         and meta["setorial_commit"] is None
         and meta["origem_hist_declara_commit_ausente"]=="13027681729f3cbe7f77fe5e08be521fa27bd4b2",
         "Proveniência histórica ou materializada trocada sem auditoria")
    need(meta["status_juridico"]==meta["legal_status"]=="Q_SEM_C0_J"
         and meta["material_approved"] is False and meta["dec016"]=="PENDENTE"
         and meta["evidencia_independente"]=="PENDENTE_DOU_1998_E_SEGUNDA_TRANSCRICAO",
         "Estado ou autenticidade alegada indevidamente")
    need(len(rows)==meta["count_expected"]==23
         and len({r["id_origem"] for r in rows})==23
         and len({r["id_destino_simbolico"] for r in rows})==23,
         "Fonte 23x23 sem unicidade")
    seen={}
    for row in rows:
        art=row["artigo"]
        need(art in EXPECTED_UNITS,"Artigo fora de 3–15: "+art)
        seen.setdefault(art,set()).add(row["unidade"])
        need(row["id_origem"]==f"BR-LEI-1998-9709-ART{int(art):03d}-{row['unidade']}"
             and row["id_destino_simbolico"]==f"CLF-T05-M06-9709-ART{int(art):03d}-{row['unidade']}",
             "ID de origem/destino adulterado")
        need(row["texto_fonte_camara_html"]==row["texto_destino_documental"]
             and row["status_juridico"]=="Q_SEM_C0_J"
             and row["classificacao_editorial"]=="C0_T_CANDIDATO_Q",
             "Mudança invisível ou promoção de status: "+row["id_origem"])
    need(seen==EXPECTED_UNITS,"Unidades/artigos perdidos, duplicados ou reorganizados")
    by={(r["artigo"],r["unidade"]):r["texto_destino_documental"] for r in rows}
    for art,phrases in REQUIRED.items():
        text=by[(art,"C")]
        need(all(p in text for p in phrases),"Garantia fundamental ausente no art"+art)
    need("a às frentes suprapartidárias" in by[("8","IV")]
         and "nos meios de comunicação" in by[("8","IV")],
         "Variante Câmara art8 IV corrigida sem DOU (não é permitido corrigir silenciosamente)")
    need("fixar a data" in by[("8","I")]
         and "tornar pública a cédula" in by[("8","II")]
         and "expedir instruções" in by[("8","III")],
         "Garantias de Justiça Eleitoral omitidas")
    need("não poderá ser rejeitado por vício de forma" in by[("13","P2")]
         and "um só assunto" in by[("13","P1")],
         "Iniciativa popular descaracterizada")
    need(by[("15","C")].strip()=="Esta Lei entra em vigor na data de sua publicação.",
         "Art15 histórico convertido em cláusula de vigência nova")
    return {"artigos":13,"unidades_q":23,"variantes_criticas_pendentes":2,
            "vigencia_art15":"HISTORICA_1998","c0_j":0}

def main():
    a=argparse.ArgumentParser(description=__doc__)
    a.add_argument("--source-root",required=True,type=Path)
    opts=a.parse_args()
    meta=json.loads((ROOT/"produto/fontes/T05_M06_9709_23_v1.json").read_text(encoding="utf-8"))
    src=ROOT/meta["source_path"]
    rel=Path(meta["source_path"])
    need(not rel.is_absolute() and ".." not in rel.parts,"path inseguro")
    snap=(opts.source_root/rel).resolve()
    need(snap.is_relative_to(opts.source_root.resolve()),"snapshot externo")
    need(blob(src)==BLOB and blob(snap)==BLOB,"Fonte local difere do snapshot PR80 imutável")
    values=verify(csvrows(src),meta)
    view=(ROOT/meta["view_path"]).read_text(encoding="utf-8")
    need(len(re.findall(r"(?m)^\*\*Art\. \d+\.\*\*",view))==13
         and all(z["texto_destino_documental"] in view for z in csvrows(src)),
         "Vista não reproduz texto literal 23x23")
    print("PASSOU T05 SUPLEMENTO (NÃO C0-J): "+json.dumps(values,ensure_ascii=False,sort_keys=True))

if __name__=="__main__":
    try:
        main()
    except (OSError,ValueError,KeyError,csv.Error) as e:
        raise SystemExit("FALHA T05 SUPLEMENTO: "+str(e))
