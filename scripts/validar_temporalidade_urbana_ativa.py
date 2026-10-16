#!/usr/bin/env python3
"""CLF — gate temporal ativo T36, R27 e seguintes; NAO certifica C0-J ou DOU."""
import csv,json
from pathlib import Path
P=Path(__file__).resolve().parents[1]
m19=json.loads((P/"produto/fontes/T19_M01_LREF_5_R27_v1.json").read_text(encoding="utf-8"))
m36=json.loads((P/"produto/fontes/T36_M01_ECIDADE_32_R27_v1.json").read_text(encoding="utf-8"))
def rows(m):
 with (P/m["source_path"]).open(encoding="utf-8",newline="") as f: return list(csv.DictReader(f,strict=True))
x=rows(m19); y=rows(m36)
assert len(x)==m19["count_expected"]==5
assert len(y)==m36["count_expected"]==32
assert len({r["artigo"] for r in x})==3 and len({r["artigo"] for r in y})==2
assert len({r["id_origem"] for r in x})==5 and len({r["id_origem"] for r in y})==32
assert len({r["id_destino_simbolico"] for r in x})==5
assert len({r["id_destino_simbolico"] for r in y})==32
assert all(r["texto_fonte_editorial"]==r["texto_destino_documental"] and r["estado_juridico"]=="Q_SEM_C0_J" for r in x+y)
assert {r["unidade"] for r in x if r["artigo"]=="2"}=={"C","I","II"}
assert {r["unidade"] for r in y if r["artigo"]=="2"}==({"C"}|{str(i) for i in ()}|{"VI-"+a for a in "abcdefgh"}|set("I II III IV V VI VII VIII IX X XI XII XIII XIV XV XVI XVII XVIII XIX XX XXI".split()))
assert not {"XXII","XXIII"}&{r["unidade"] for r in y}
assert any(r["unidade"]=="XXI" and "higienização" in r["texto_fonte_editorial"] for r in y)
assert m36["dec016"]=="PENDENTE" and m36["material_approved"] is False
assert len(m36["excluded_future_effects"])==1 and m36["excluded_future_effects"][0]["not_counted_in_current_units"] is True
with (P/"central/38_R27_VIGENCIA_ESTATUTO_CIDADE_2026_2027.csv").open(encoding="utf-8",newline="") as f:g=list(csv.DictReader(f,strict=True))
assert len(g)==7 and len({r["id"] for r in g})==7
future=[r for r in g if "art2 XXII" in r["dispositivo"] or "art2 XXIII" in r["dispositivo"]]
assert len(future)==2 and all(r["situacao_temporal"]=="LEGISLADO_EFICACIA_FUTURA" for r in future)
print("R27 QA temporal: T19 3/5 Q, T36 2/32 Q, XXI eficaz/XXII-XXIII vigencia diferida.")
print("NAO verifica DOU em fac-simile, prova C0-J, CI ou DEC016.")
