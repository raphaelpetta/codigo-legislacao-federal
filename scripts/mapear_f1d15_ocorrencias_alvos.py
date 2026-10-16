#!/usr/bin/env python3
"""T24 F1-D15: ligar cada OCORRÊNCIA lexical a destinos jurídicos candidatos.

Não substitui leitura da oração completa. 45 pares são um grafo de
dependência semântica, que pode conter contextos e alvos sem marcador
repetido na frase. Referências anafóricas NÃO são inventadas.
"""
import argparse,csv,json,pathlib,re,subprocess,sys,tempfile
from collections import defaultdict
B=pathlib.Path(__file__).resolve().parents[1]
MOD=B/"modulos/T24/M01"
def load(path):
    with (MOD/path).open(encoding="utf-8-sig",newline="") as h:return list(csv.DictReader(h))
def fragment_targets(unit,frag,edges):
    fs=frag.replace("–","-").replace("°","º")
    eligible={x["id_destino"] for x in edges}
    if "inciso" in fs.lower():
        romans=re.findall(r"\b(?:I|II|III|IV|V|VI|VII|VIII|IX|X)\b",fs)
        seq=["I","II","III","IV","V","VI","VII","VIII","IX","X"]
        if " a " in fs and len(romans)>=2:
            lo,hi=seq.index(romans[0]),seq.index(romans[-1])
            romans=seq[lo:hi+1] if lo<=hi else []
        return {s for s in eligible if s.rsplit("-",1)[-1] in romans}
    if fs.lower().startswith("art"):
        nums=re.findall(r"\d+",fs)
        return {x for x in eligible if any(f"ART-{int(n):04}" in x for n in nums)}
    if fs.startswith("§"):
        parts=re.findall(r"\d+(?:º)?(?:-[A-Z])?",fs)
        values=[re.sub(r"-(?=[A-Z])","",re.sub(r"º","",p)) for p in parts]
        if " a " in fs and len(values)>=2:
            try:
                x,y=int(values[0]),int(values[-1])
                if x<=y and y-x<30:values=[str(k) for k in range(x,y+1)]
            except ValueError:pass
        # Se o texto cita apenas "§2º" mas o grafo contém seus INCISOS,
        # há uma dependência por desdobramento grupal, jamais citação
        # literal individual a cada inciso.
        direct={s for s in eligible if any(s.endswith("-P"+v) for v in values)}
        if direct:return direct
        if unit=="P8" and "2" in values:
            return {s for s in eligible if s.endswith(tuple("-P2-"+x for x in ("I","II","III","IV")))}
        return set()
    return set()
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--csv",required=True)
    ap.add_argument("--json",required=True)
    args=ap.parse_args()
    with tempfile.TemporaryDirectory() as d:
        ocsv=str(pathlib.Path(d)/"occ.csv");ojson=str(pathlib.Path(d)/"occ.json")
        subprocess.run([sys.executable,str(B/"scripts/inventariar_f1d14_ocorrencias.py"),
                        "--csv",ocsv,"--json",ojson],check=True)
        with open(ocsv,encoding="utf-8",newline="") as f:occ=list(csv.DictReader(f))
        meta=json.loads(pathlib.Path(ojson).read_text(encoding="utf8"))
    edges=load("MATRIZ_F1D13_45_PARES_LITERAL_CONTEXTO.csv")
    assert len(occ)==19 and len(edges)==45
    by=defaultdict(list)
    for e in edges:by[e["id_origem"]].append(e)
    matched=set()
    out=[]
    for o in occ:
        candidates=fragment_targets(o["unidade"],o["ocorrencia_lexical"],by[o["id_unidade_fonte"]])
        matched|={(o["id_unidade_fonte"],x) for x in candidates}
        explicit="CONFERIDO_LITERAL_GRUPO" if candidates else "SEM_ALVO_DETERMINADO_NESTE_GRAFO"
        if o["unidade"] in ("P4-I","P4-II") and candidates:
            explicit="CONTEXTO_DEPENDE_CAPUT_P4"
        elif o["unidade"] in ("P3","P8") and candidates:
            explicit="DESDOBRAMENTO_GRUPO_NO_TEXTO"
        out.append({
           "ocorrencia_id":o["id"],"unidade":o["unidade"],
           "id_fonte":o["id_unidade_fonte"],
           "fragmento_exato":o["ocorrencia_lexical"],
           "offset_inicio":o["offset_inicio"],"offset_fim":o["offset_fim"],
           "destinos_candidatos":";".join(sorted(candidates)),
           "quantidade_destinos":len(candidates),
           "qualidade_ligacao":explicit,
           "estado":"Q_NAO_HOMOLOGADO",
        })
    p11=[o for o in out if o["unidade"]=="P11"]
    assert len(p11)==2 and sorted(o["quantidade_destinos"] for o in p11)==[2,5],p11
    p20=[o for o in out if o["unidade"]=="P20"]
    assert len(p20)==1 and p20[0]["quantidade_destinos"]==10,p20
    unresolved=[e for e in edges if (e["id_origem"],e["id_destino"]) not in matched]
    for o in out:
        if o["estado"]!="Q_NAO_HOMOLOGADO":raise AssertionError("C0-J promovido prematuramente")
    result={"corte":"2026-10-14","ocorrencias":len(out),
       "pares_no_grafo":len(edges),"pares_associados_a_alguma_ocorrencia":len(matched),
       "pares_sem_vinculo_automatico":len(unresolved),
       "sem_vinculo":[{"origem":x["id_origem"],"destino":x["id_destino"],
                       "categoria":x["categoria_ligacao"]} for x in unresolved],
       "registros":out,
       "observacao":"A ocorrência §11 de §§2–6 corresponde a 5 alvos; outra de §§2–3 corresponde a 2 (repetidos). §20 corresponde a 10. Ligação automática sujeita a revisão humana.",
       "C0_J":"Q"}
    for p in (args.csv,args.json):pathlib.Path(p).parent.mkdir(exist_ok=True,parents=True)
    with open(args.csv,"w",encoding="utf8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(out[0]));w.writeheader();w.writerows(out)
    pathlib.Path(args.json).write_text(json.dumps(result,indent=2,ensure_ascii=False),encoding="utf8")
    print("T24 F1-D15 OK",json.dumps({k:result[k] for k in ("ocorrencias","pares_no_grafo","pares_associados_a_alguma_ocorrencia","pares_sem_vinculo_automatico")},ensure_ascii=False))
    for e in unresolved:
        print("SEM_LIGACAO_AUTOMATICA:",e["id_origem"],"->",e["id_destino"],e["categoria_ligacao"])
    print("§11: 5 e 2 destinos com sobreposição; §20: 10 destinos. Sem equivalência C0-J.")
if __name__=="__main__":main()
