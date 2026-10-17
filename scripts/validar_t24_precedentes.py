#!/usr/bin/env python3
"""Testa o vínculo entre nove anotações jurídicas e origem literal T24.

Este gate NÃO consulta tribunais em tempo real, NÃO autentica DOU e NÃO
homologa C0-J/M. A situação processual é fotografia datada revisável.
"""
from __future__ import annotations
import csv
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
MATRIX=ROOT/"produto/analises/T24_PRECEDENTES_EFEITOS_20261016.json"
S106=ROOT/"produto/concordancia/T24_M01_106_ORIGEM_DESTINO.csv"
S75=ROOT/"produto/fontes/T24_CPC_82_97_TEXTO_ATUAL_75_Q.csv"
BLOBS={
 S106:"b3542c54db70d9f5721fbe64ec372164b99b56ef",
 S75:"5a1b1123e29b95f5777ec2bffb8eda5b84e4a18b",
}
# ID: fonte documental, artigo, marcador, precedente, situação, âmbito e efeito.
EXPECTED={
 "T24-J01":("SETORIAL_106","99","§3","STJ_TEMA_1178","TESE_FIRMADA_TRANSITO","PESSOA_NATURAL","VEDADO_INDEFERIMENTO_IMEDIATO_CRITERIO_OBJETIVO"),
 "T24-J02":("SETORIAL_106","99","§2","STJ_TEMA_1178","TESE_FIRMADA_TRANSITO","PESSOA_NATURAL","EXIGIR_MOTIVOS_CONCRETOS_E_OUVIDA_PREVIA"),
 "T24-J03":("SETORIAL_106","99","§2","STJ_TEMA_1178","TESE_FIRMADA_TRANSITO","PESSOA_NATURAL","CRITERIOS_OBJETIVOS_SOMENTE_SUPLEMENTARES_NUNCA_EXCLUSIVOS"),
 "T24-J04":("SETORIAL_106","99","§6","CPC_99_PARAGRAFO_6","TEXTO_LEGAL_VIGENCIA_NAO_CERTIFICADA","BENEFICIARIO_INDIVIDUAL","PESSOAL_NAO_ESTENDE_AUTOMATICAMENTE_A_LITISCONSORTE_SUCESSOR"),
 "T24-J05":("SETORIAL_106","98","§3","CPC_98_PARAGRAFO_3","TEXTO_LEGAL_VIGENCIA_NAO_CERTIFICADA","CONDENACAO_SUCUMBENCIA_BENEFICIARIO","CONDICAO_SUSPENSIVA_COM_PRAZO_5_ANOS"),
 "T24-J06":("EDITORIAL_75","85","P6A","STJ_TEMA_1076","TESE_REPETITIVA_COM_RECORTE_STF_PENDENTE","HONORARIOS_CPC85_COM_EXCECOES_LEGAIS","EQUIDADE_NAO_PRESUMIDA_SO_POR_VALOR_ELEVADO"),
 "T24-J07":("EDITORIAL_75","85","P6A","STF_TEMA_1255","QUESTAO_DE_ORDEM_SEM_TESE_FINAL_DE_MERITO_CONFIRMADA","FAZENDA_PUBLICA_PARTE_NO_PROCESSO","RECORTE_QO_MERITO_A_MONITORAR_NAO_AFIRMAR_TESE_NOVA"),
 "T24-J08":("EDITORIAL_75","82","P3","LEI_15109_2025","NORMA_ALTERADORA_ART82_P3_NAO_C0_J","COBRANCA_E_EXECUCAO_HONORARIOS","DISPENSA_ADIANTAMENTO_NAO_ISENCAO_GERAL"),
 "T24-J09":("EDITORIAL_75","95","P5","CPC_95_PARAGRAFO_5","TEXTO_LEGAL_VIGENCIA_NAO_CERTIFICADA","CUSTEIO_PERICIA_BENEFICIARIO","VEDADO_FUNDO_CUSTEIO_DEFENSORIA"),
}
PHRASES={
 "T24-J01":("Presume-se verdadeira","pessoa natural"),
 "T24-J02":("O juiz somente poderá indeferir","devendo, antes de indeferir"),
 "T24-J03":("elementos que evidenciem","determinar à parte a comprovação"),
 "T24-J04":("é pessoal","salvo requerimento e deferimento expressos"),
 "T24-J05":("condição suspensiva de exigibilidade","5 (cinco) anos"),
 "T24-J06":("proibida a apreciação equitativa","salvo nas hipóteses expressamente"),
 "T24-J07":("proibida a apreciação equitativa","§ 8º deste artigo"),
 "T24-J08":("dispensado de adiantar o pagamento de custas","se tiver dado causa ao processo"),
 "T24-J09":("vedada a utilização de recursos","Defensoria Pública"),
}
URLS={
 "STJ_TEMA_1178":"processo.stj.jus.br/repetitivos/temas_repetitivos/",
 "STJ_TEMA_1076":"processo.stj.jus.br/repetitivos/temas_repetitivos/",
 "STF_TEMA_1255":"portal.stf.jus.br/processos/detalhe.asp",
 "LEI_15109_2025":"www.planalto.gov.br/ccivil_03/",
 "CPC_99_PARAGRAFO_6":"planalto.gov.br/ccivil_03/",
 "CPC_98_PARAGRAFO_3":"planalto.gov.br/ccivil_03/",
 "CPC_95_PARAGRAFO_5":"planalto.gov.br/ccivil_03/",
}
def require(condition,why):
    if not condition:
        raise ValueError(why)

def git_blob(path):
    data=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()

def csv_rows(path):
    with path.open(encoding="utf-8-sig",newline="") as h:
        return list(csv.DictReader(h,strict=True))

def documents():
    for path,wanted in BLOBS.items():
        require(git_blob(path)==wanted,"Fonte T24 mudou sem cotejo e atualização de matriz: "+str(path))
    old=csv_rows(S106)
    new=csv_rows(S75)
    require(len(old)==106 and len(new)==75,"Concordâncias T24 incompletas")
    require(all(row["status_juridico"]=="Q_SEM_C0_J" for row in old+new),
            "Promoção indevida de estado Q")
    docs={}
    for x in old:
        art=x["artigo_origem"].removeprefix("CPC ")
        k=("SETORIAL_106",art,x["unidade_origem"])
        require(k not in docs,"Localizador origem setorial duplicado")
        require(x["texto_origem_transcrito"]==x["texto_destino_experimental"],
                "Mudança oculta origem/destino 106")
        docs[k]=x["texto_origem_transcrito"]
    for x in new:
        k=("EDITORIAL_75",x["artigo"],x["subunidade"])
        require(k not in docs,"Localizador origem editorial duplicado")
        require(x["estado_juridico"]=="Q_SEM_C0_J",
                "Estado editorial alterado")
        docs[k]=x["texto_atual_manual"]
    return docs

def validate(data,docs):
    require(data["schema_version"]==1 and data["corte"]=="2026-10-16",
            "Corte jurídico ou schema alterado sem reauditoria")
    require(data["natureza"]=="ANOTACOES_JURISPRUDENCIA_E_RESTRICOES_NAO_TRANSPOSICAO_NORMATIVA"
            and data["estado_juridico"]=="Q_SEM_C0_J" and data["material_approved"] is False
            and data["dec016"]=="PENDENTE","Aprovação jurídica ou normativa não autorizada")
    require(data["fonte_editorial_75_sha"]==BLOBS[S75]
            and data["concordancia_setorial_106_sha"]==BLOBS[S106],
            "Hashes da matriz de precedentes divergem")
    items=data["cenarios"]
    require(len(items)==9 and {x["id"] for x in items}==set(EXPECTED),
            "Um dos nove efeitos jurídicos está ausente ou duplicado")
    for x in items:
        ident=x["id"]
        origin,art,unit,precedent,tipo,escopo,efeito=EXPECTED[ident]
        # Normalização explícita de § para P nos IDs de destino do índice.
        marker="P"+unit[1:] if unit.startswith("§") else unit
        require((x["documental"],x["unit"],x["precedente"],x["tipo"],x["escopo"],x["efeito"])
                ==(origin,f"CPC{art}-{marker}",precedent,tipo,escopo,efeito),
                "Referente, tipo jurídico ou fase processual alterada: "+ident)
        source=docs.get((origin,art,unit))
        require(source is not None,"Unidade documental sem contraparte: "+ident)
        require(all(v in source for v in PHRASES[ident]),"Garantia textual perdida: "+ident)
        require(URLS[precedent] in x["url"] and x["url"].startswith("https://"),
                "Origem institucional inválida: "+ident)
    return {"efeitos":len(items),"tema1178":3,"tema1255":"QO_RECORTE_SEM_MERITO_CONFIRMADO",
            "documentos_q":181,"aprovacoes":0}

def main():
    data=json.loads(MATRIX.read_text(encoding="utf-8"))
    result=validate(data,documents())
    print("PASSOU R3 T24 PRECEDENTES, NÃO C0-J: "+json.dumps(result,ensure_ascii=False,sort_keys=True))
if __name__=="__main__":
    try:
        main()
    except (ValueError,OSError,KeyError,TypeError,UnicodeError,csv.Error) as e:
        raise SystemExit("FALHA T24 PRECEDENTES: "+str(e))
