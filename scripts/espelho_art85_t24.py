#!/usr/bin/env python3
"""T24.M01: espelho probatório artigo-local do CPC art. 85 (36 unidades).

Lê diretamente Câmara 2015 e 2026, usa o parser testado de F1-D e valida
também o texto integral dentro do artigo compilado. Escreve CSV/JSON em artefato.
Não confirma cadeia histórica intermediária/DOU nem equivalência jurídica CLF.
"""
from __future__ import annotations
import argparse, csv, json, pathlib, re, sys, importlib.util

BASE = pathlib.Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("f1d", pathlib.Path(__file__).with_name("extrair_f1d_t24.py"))
f1d = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(f1d)
INVENTORY = BASE / "modulos/T24/M01/F1D_INVENTARIO_ART82_97_SUBUNIDADES.csv"

# A legislação compilada contém precisamente três unidades acrescidas desde
# a publicação de 2015; não assumir que redações intermediárias foram estáveis.
ADDED = {
  "P6A": ("§ 6º-A.", "§ 7º", "Lei 14.365/2022"),
  "P8A": ("§ 8º-A.", "§ 9º", "Lei 14.365/2022"),
  "P20": ("§ 20.", None, "Lei 14.365/2022")
}

def strip_editorial(fragment: str) -> str:
    # Texto legislativo termina antes da anotação editorial da Câmara.
    fragment = re.sub(r"\(\s*(?:Parágrafo|Inciso|Caput)\s+(?:acrescido|alterado|com redação dada).*?\)\s*$",
                      "", fragment, flags=re.IGNORECASE)
    return f1d.norm(fragment)

def extract_added(art_text: str, unit: str) -> str:
    start, stop, _ = ADDED[unit]
    if art_text.count(start) != 1:
        raise ValueError(f"Marcador único ausente em art.85: {unit}, hits={art_text.count(start)}")
    frag = art_text.split(start, 1)[1]
    if stop:
        if stop not in frag:
            raise ValueError(f"Falta próximo marcador {stop} para {unit}")
        frag = frag.split(stop, 1)[0]
    return strip_editorial(frag)

def main() -> int:
    ap=argparse.ArgumentParser()
    ap.add_argument("--json",required=True)
    ap.add_argument("--csv",required=True)
    args=ap.parse_args()
    with INVENTORY.open(encoding="utf-8-sig", newline="") as f:
        index=[r for r in csv.DictReader(f) if r["dispositivo"]=="art. 85"]
    if len(index)!=36 or len({r["subunidade"] for r in index})!=36:
        raise ValueError(f"36 unidades art85 esperadas, encontrado {len(index)}")
    orig_lines, orig_metadata, _ = f1d.source(f1d.ORIGINAL)
    now_lines, now_metadata, _ = f1d.source(f1d.UPDATED)
    orig=f1d.extract(orig_lines)
    current=f1d.extract(now_lines)
    art_orig=f1d.article_blocks(orig_lines)[85]
    art_now=f1d.article_blocks(now_lines)[85]
    result=[]
    for it in index:
        u=it["subunidade"]
        old=orig.get((85,u))
        if u in ADDED:
            if old is not None:
                raise ValueError(f"Unidade histórica esperada não ausente de 2015: {u}")
            new=extract_added(art_now,u)
            if len(new)<65:
                raise ValueError(f"Texto de adição insuficiente: {u} len={len(new)}")
            if art_now.count(new)!=1:
                raise ValueError(f"Texto de acréscimo não está único dentro do art85: {u}")
            status="ACRESCIDO_EM_2022_CONFERIR_ATO_E_DOU"
            oldfield="INEXISTENTE_PUBLICACAO_ORIGINAL_2015"
            law=ADDED[u][2]
            method="LOCALIZACAO_ENTRE_MARCADORES_E_EXCLUSAO_NOTA_EDITORIAL"
        else:
            if old is None:
                raise ValueError(f"Unidade original não encontrada: {u}")
            oldfield=f1d.norm(old)
            # Bloqueio: não aceitar textualidade se não existir exatamente
            # uma ocorrência integral DENTRO do mesmo artigo na edição atual.
            hits=art_now.count(oldfield)
            if hits!=1:
                raise ValueError(f"Unidade art85 {u}: original não se encontra uma vez na atual: hits={hits}; prefix={oldfield[:90]}")
            new=oldfield
            status="IGUAL_2015_2026_NOS_DOIS_RETRATOS_OFICIAIS"
            law="SEM_MODIFICACAO_LITERAL_IDENTIFICADA_NOS_DOIS_RETRATOS"
            method="TEXTO_ORIGINAL_LOCALIZADO_UNICAMENTE_NO_ART85_CONSOLIDADO"
        result.append({
            "id_fonte":it["id_origem"], "artigo":"85","subunidade":u,
            "texto_publicacao_2015":oldfield,"texto_compilado_2026":new,
            "status_cotejo_textual":status,"ato_alterador_identificado":law,
            "metodo":method,"url_2015":f1d.ORIGINAL,"url_2026":f1d.UPDATED,
            "equivalencia_juridica":"Q","validacao_DOU":"PENDENTE",
            "destino_clf":"T24.M01_PROVISORIO_SEM_RENUMERACAO"
        })
    statuses={}
    for row in result: statuses[row["status_cotejo_textual"]]=statuses.get(row["status_cotejo_textual"],0)+1
    if statuses.get("ACRESCIDO_EM_2022_CONFERIR_ATO_E_DOU") != 3 or statuses.get("IGUAL_2015_2026_NOS_DOIS_RETRATOS_OFICIAIS") != 33:
        raise ValueError(f"Distribuição inesperada: {statuses}")
    out={
      "escopo":"CPC art85 completo 36 unidades; duas fotografias da Câmara; sem certificação da cadeia DOU",
      "fontes":{"original":orig_metadata,"compilada":now_metadata},
      "contagens":statuses,"total":len(result),"Q_juridico":len(result),
      "observacao":"Texto igual não garante C0-J CLF; conferir Lei14365/2022, Tema1076/STJ, Tema1313/STJ, Tema1255/STF e todos os efeitos de remissão.",
      "resultados":result
    }
    for target in [args.json,args.csv]:
        pathlib.Path(target).parent.mkdir(parents=True,exist_ok=True)
    with open(args.json,"w",encoding="utf8") as f:
        json.dump(out,f,indent=2,ensure_ascii=False)
    with open(args.csv,"w",encoding="utf8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=result[0].keys());w.writeheader();w.writerows(result)
    print("CPC85 36 unidades:",json.dumps(statuses,ensure_ascii=False), "orig_sha=",orig_metadata["sha256"],"new_sha=",now_metadata["sha256"])
    print("Cotejo textual dos retratos oficiais passou; equivalência jurídica Q.")
    return 0

if __name__=="__main__":
    try: sys.exit(main())
    except Exception as exc:
        print(f"FALHA_CPC85: {type(exc).__name__}: {exc}",file=sys.stderr)
        sys.exit(2)
