#!/usr/bin/env python3
"""T24 F1-D14: registro de OCORRÊNCIAS textuais, distinto de PARES de remissão.

Captura expressões de remissão no texto compilado art.85. Não inventa
equivalência C0-J ou esgota remissões implícitas e contextuais. A saída é
artefato de CI com offsets verificáveis por subunidade de origem.
"""
import argparse,csv,json,pathlib,re,subprocess,sys,tempfile
from collections import Counter
ROOT=pathlib.Path(__file__).resolve().parents[1]
BASE=ROOT/"modulos/T24/M01"
# Alternativas em ordem: símbolos de parágrafos, artigo, incisos e caput.
PAT=re.compile(
 r"§§?\s*\d+(?:[º°ª])?(?:[-–][A-Z])?(?:\s*(?:a|e|,)\s*(?:§§?\s*)?\d+(?:[º°ª])?(?:[-–][A-Z])?)*"
 r"|art(?:igo)?s?\.?\s*\d+(?:[º°ª])?"
 r"|\bincisos?\s+(?:I{1,3}|IV|V|VI{0,3}|IX|X)(?:\s*(?:a|e|,)\s*(?:I{1,3}|IV|V|VI{0,3}|IX|X))*"
 r"|\bcaput\b",re.IGNORECASE)
def body(unit,txt):
    # Evita registrar o cabeçalho do § analisado como AUTORREFERÊNCIA.
    if unit.startswith("P"):
        txt=re.sub(r"^§\s*\d+(?:º|°)?(?:[-–]A)?\.\s*","",txt,count=1)
    return txt
def classify(fragment):
    s=fragment.lower()
    if s.startswith("§§"):return "MULTIPLOS_PARAGRAFOS_POR_OCORRENCIA"
    if s.startswith("§"):return "PARAGRAFO_EXPRESSO"
    if s.startswith("art"):return "ARTIGO_EXPRESSO"
    if s.startswith("incis"):return "INCISOS_EXPRESSOS_COM_CONTEXTO"
    return "REFERENCIA_GENERICA_CAPUT"
ap=argparse.ArgumentParser()
ap.add_argument("--csv",required=True)
ap.add_argument("--json",required=True)
opt=ap.parse_args()
with tempfile.TemporaryDirectory() as tmp:
    src=str(pathlib.Path(tmp)/"source.json")
    csvsrc=str(pathlib.Path(tmp)/"source.csv")
    subprocess.run([sys.executable,str(ROOT/"scripts/espelho_art85_t24.py"),
       "--json",src,"--csv",csvsrc],check=True)
    record=json.loads(pathlib.Path(src).read_text(encoding="utf8"))
items=record["resultados"]
assert len(items)==36
out=[]
for unit in items:
    src=unit["id_fonte"]
    txt=body(unit["subunidade"],unit["texto_compilado_2026"])
    for m in PAT.finditer(txt):
        frag=m.group(0)
        out.append({"id":f"F1D14-{len(out)+1:03}",
                    "id_unidade_fonte":src,"unidade":unit["subunidade"],
                    "ocorrencia_lexical":frag,"offset_inicio":m.start(),
                    "offset_fim":m.end(),"categoria_lexical":classify(frag),
                    "trecho_contexto":txt[max(0,m.start()-45):min(len(txt),m.end()+45)],
                    "versao":"CPC_COMPILADO_2026","status":"Q_SEM_C0_J"})
pairs=[]
for name in ["GRAFO_F1D7_REMISSOES_EXPRESSAS_ART85.csv",
             "MATRIZ_F1D12_DEZ_REMISSOES_P4_INCISOS.csv"]:
    with (BASE/name).open(encoding="utf-8-sig",newline="") as f:
        pairs+=list(csv.DictReader(f))
assert len(pairs)==45
from collections import defaultdict
by=defaultdict(list)
for e in out:by[e["unidade"]].append(e["ocorrencia_lexical"])
p11=by["P11"]
assert len(p11)>=2,f"§11 deveria ter duas ocorrências explícitas, encontrou {p11}"
assert any("6º" in t or "6°" in t for t in p11),f"Falta intervalo §§2–6: {p11}"
assert sum("2º" in t or "2°" in t for t in p11)>=2,f"§11 repete §2 em duas frases: {p11}"
# O §20 enumera dez alvos; podem aparecer em uma expressão por agrupamento.
assert len(by["P20"])>=1,f"§20 sem referências: {by['P20']}"
assert len(out)>=18,f"Inventário lexical improvavelmente pequeno: {len(out)}"
assert {e["status"] for e in out}=={"Q_SEM_C0_J"}
res={"fontes":record["fontes"],"corte":"2026-10-14","36_subunidades":36,
     "pares_semanticos_historicos":45,"ocorrencias_lexicais":len(out),
     "nota":"Uma citação pode remeter a cinco destinos; §11 repete dois destinos; §4 remete por contexto. Não equiparar ocorrência e par.",
     "ocorrencias_paragrafo_11":p11,"ocorrencias_paragrafo_20":by["P20"],
     "classificacoes":dict(Counter(x["categoria_lexical"] for x in out)),
     "registros":out}
for target in (opt.csv,opt.json):pathlib.Path(target).parent.mkdir(parents=True,exist_ok=True)
with open(opt.csv,"w",encoding="utf8",newline="") as f:
    wr=csv.DictWriter(f,fieldnames=list(out[0]));wr.writeheader();wr.writerows(out)
pathlib.Path(opt.json).write_text(json.dumps(res,ensure_ascii=False,indent=2),encoding="utf8")
print(f"T24 F1-D14: {len(out)} ocorrências lexicais em 36 unidades versus 45 pares de dependência.")
print("§11:",p11,"; §20:",by["P20"])
print("C0-J Q; não se afirma exaustividade normativa.")
