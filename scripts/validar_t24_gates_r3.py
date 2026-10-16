#!/usr/bin/env python3
"""Portas documentais R3 do CPC70–102: 106 fontes setoriais + 75 editoriais Q.

Não atesta vigência, DOU, jurisprudência, C0-J, renumeração ou DEC-016.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PR38="3fdbfa10b8d288b1cef56c78b47cf3cb1eb28745"

def need(condition,description):
    if not condition:
        raise ValueError(description)

def sha(path):
    body=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(body)).encode()+b"\0"+body).hexdigest()

def rows(path):
    with path.open(encoding="utf-8-sig",newline="") as h:
        return list(csv.DictReader(h,strict=True))

def local(rel,expected):
    p=Path(rel)
    need(not p.is_absolute() and ".." not in p.parts,"Caminho inseguro: "+rel)
    f=(ROOT/p).resolve()
    need(f.is_relative_to(ROOT.resolve()) and f.is_file(), "Fonte local ausente: "+rel)
    need(sha(f)==expected,"Drift SHA local: "+rel)
    return f

def audit(setorial):
    manifest=json.loads((ROOT/"produto/fontes/T24_CPC_70_102_181_v1.json").read_text(encoding="utf-8"))
    m106=json.loads((ROOT/"produto/fontes/T24_M01_106_v1.json").read_text(encoding="utf-8"))
    need(manifest["setorial_commit"]==m106["setorial_commit"]==PR38,"SHA original PR38 modificado")
    need(manifest["status_juridico"]==m106["status_juridico"]=="Q_SEM_C0_J"
         and manifest["material_approved"] is False and m106["material_approved"] is False
         and manifest["dec016"]==m106["dec016"]=="PENDENTE","Estado jurídico alterado")
    comps=manifest["components"]
    need(len(comps)==2 and [x["count"] for x in comps]==[106,75],"Composição mudou")
    p=Path(m106["source_path"])
    need(not p.is_absolute() and ".." not in p.parts,"Fonte PR38 insegura")
    source=(setorial/p).resolve()
    need(source.is_relative_to(setorial.resolve()) and source.is_file(),"Fonte PR38 não disponível")
    need(sha(source)==m106["source_blob_sha"]=="a0562c236cda3a49b842417bb27417e84484f363",
         "SHA da origem setorial incorreto")
    originals=rows(source)
    need(len(originals)==106 and len({r["id_origem"] for r in originals})==106,
         "106 origens não identificadas")
    need(all(r["estado_proposta_clf"]=="NAO_C0_NAO_C1_NAO_M" for r in originals),
         "Classificação jurídica do setorial promovida")
    old=rows(local(comps[0]["concordance_path"],comps[0]["concordance_git_blob"]))
    need(len(old)==106 and len({r["id_origem"] for r in old})==106, "Concordância 106 insuficiente")
    byorig={r["id_origem"]:r for r in originals}
    for r in old:
        x=byorig.get(r["id_origem"])
        need(x is not None and r["texto_origem_transcrito"]==x["texto_atual_manual"]
             and r["texto_destino_experimental"]==x["texto_atual_manual"]
             and r["status_juridico"]=="Q_SEM_C0_J"
             and r["categoria_transposicao"]=="Q_NAO_C0_T_CERTIFICADO",
             "Fonte 106, conteúdo ou status divergente: "+r["id_origem"])
    local(comps[0]["path"],comps[0]["git_blob"])
    src75=rows(local(comps[1]["path"],comps[1]["git_blob"]))
    cw75=rows(local(comps[1]["concordance_path"],comps[1]["concordance_git_blob"]))
    local(comps[1]["view_part_path"],comps[1]["view_part_git_blob"])
    need(len(src75)==len(cw75)==75, "Fonte 75 ou concordância incompleta")
    need(len({r["id_origem"] for r in src75})==75 and
         len({r["id_origem"] for r in cw75})==75, "Origem duplicada 75")
    allids={r["id_origem"] for r in old}|{r["id_origem"] for r in cw75}
    need(len(allids)==181,"Sobreposição 106/75 ou destino ausente")
    dests={r["destino_simbolico"] for r in old}|{r["destino_experimental"] for r in cw75}
    need(len(dests)==181,"Destinos repetidos entre fontes")
    by75={r["id_origem"]:r for r in src75}
    for r in cw75:
        x=by75.get(r["id_origem"])
        need(x is not None and r["texto_origem_camara_transcrito"]==x["texto_atual_manual"]
             and r["texto_destino_experimental"]==x["texto_atual_manual"]
             and r["estado_juridico"]==x["estado_juridico"]=="Q_SEM_C0_J"
             and r["marco"]==x["marco_alterador"],"Drift fonte editorial 75: "+r["id_origem"])
    need({int(r["artigo"]) for r in originals}==set(range(70,82))|set(range(98,103)),
         "Artigos setoriais não cobrem 70-81 e 98-102")
    need({int(r["artigo"]) for r in src75}==set(range(82,98)),
         "Lacuna em 82-97")
    byunit={(r["artigo"],r["subunidade"]):r for r in src75}
    markers={
        ("82","P3"):("LEI_15109_2025","dispensado de adiantar o pagamento de custas"),
        ("85","P6A"):("LEI_14365_2022","proibida a apreciação equitativa"),
        ("85","P8A"):("LEI_14365_2022","Conselho Seccional"),
        ("85","P20"):("LEI_14365_2022","honorários fixados por arbitramento judicial"),
    }
    for key,(alter,phrase) in markers.items():
        z=byunit.get(key)
        need(z is not None and z["marco_alterador"]==alter
             and phrase in z["texto_atual_manual"],
             "Norma alteradora 2022/2025 ausente: "+str(key))
    need(Counter(r["artigo"] for r in src75)["85"]==36
         and Counter(r["artigo"] for r in src75)["95"]==8,
         "CPC85 ou CPC95 perderam posições")
    def orig(art,un):
        return next((x["texto_atual_manual"] for x in originals
                     if x["artigo"]==art and x["unidade"]==un),"")
    checks={
        ("98","§3"):"condição suspensiva de exigibilidade",
        ("99","§2"):"devendo, antes de indeferir",
        ("99","§3"):"Presume-se verdadeira",
        ("99","§6"):"é pessoal, não se estendendo",
        ("101","§1"):"dispensado do recolhimento",
    }
    for (art,un),text in checks.items():
        need(text in orig(art,un),f"Gratuidade, contraditório ou prazo perdeu garantia {art}/{un}")
    need("recursos do fundo de custeio da Defensoria Pública" in byunit[("95","P5")]["texto_atual_manual"],
         "Proteção de recursos da Defensoria perdida")
    need("art. 465, § 4º" in byunit[("95","P2")]["texto_atual_manual"],
         "Remissão CPC95→465 desapareceu")
    cpc=local(manifest["view_path"],sha(ROOT/manifest["view_path"])).read_text(encoding="utf-8")
    need("§ 3º" in cpc and "honorários" in cpc and "gratuidade da justiça" in cpc,
         "Vista CPC perde institutos centrais")
    idx=json.loads((ROOT/"produto/fontes/indice_livros.json").read_text(encoding="utf-8"))
    target=[b for b in idx["livros"] if b["id"]=="CLF-LIV-T24-M01-CPC70-102-181-v1"]
    need(len(target)==1 and target[0]["artigos"]==33 and target[0]["registros_documentais"]==181,
         "Livro CPC incompleto no índice")
    return {"origens_setoriais":106,"editoriais_sem_revisao_independente":75,
            "artigos":33,"registros":181,"alteracoes_2022_2025":4,
            "garantias_gratuidade_verificadas":len(checks),"c0_j_aprovadas":0}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--setorial-root",type=Path,required=True)
    args=parser.parse_args()
    try:
        print("PASSOU T24 R3 (NÃO C0-J): "+json.dumps(audit(args.setorial_root),ensure_ascii=False,sort_keys=True))
    except (ValueError,OSError,KeyError,csv.Error,StopIteration) as exc:
        parser.exit(1,f"FALHA T24 R3: {exc}\n")
if __name__=="__main__":
    main()
