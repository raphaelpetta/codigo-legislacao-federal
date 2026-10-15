#!/usr/bin/env python3
"""Regenera e confere uma vista experimental sem alterar sua fonte setorial.

Uso:
 python3 scripts/gerar_produto_experimental.py --setorial-root setorial --check
 python3 scripts/gerar_produto_experimental.py --setorial-root setorial --write

'setorial' deve conter o checkout EXATO do commit do PR #45 declarado no
manifesto, nao uma copia editada da vista. Somente biblioteca-padrao.
Os testes sao documentais, nunca homologacao de equivalencia juridica.
"""
from __future__ import annotations

import argparse
import csv
import difflib
import hashlib
import io
import json
import re
import sys
from collections import Counter
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
MANIFESTO = RAIZ / "produto/fontes/T07_M03_v4.json"


def blob_sha(bytes_: bytes) -> str:
    """SHA do blob Git, nao SHA simples do arquivo."""
    return hashlib.sha1(b"blob " + str(len(bytes_)).encode() + b"\\0" + bytes_).hexdigest()


def exigir(condicao: bool, mensagem: str) -> None:
    if not condicao:
        raise ValueError(mensagem)


def ler_fonte(raiz: Path, rel: str, sha: str) -> str:
    caminho = raiz / rel
    exigir(caminho.is_file(), f"Fonte ausente: {caminho}. Obter checkout setorial fixado no manifesto.")
    dados = caminho.read_bytes()
    exigir(blob_sha(dados) == sha, f"Fonte divergente do blob Git fixado: {rel}")
    return dados.decode("utf-8")


def auditar(texto: str, concordancia: str, meta: dict) -> dict:
    linhas = list(csv.DictReader(io.StringIO(concordancia)))
    cont = meta["contagens_esperadas"]
    exigir(len(linhas) == cont["fontes"], "Universo de registros diferente do manifesto")
    exigir(all(linha.get("id_fonte") for linha in linhas), "Registro sem ID de origem")
    exigir(len(set(linha["id_fonte"] for linha in linhas)) == len(linhas), "IDs de origem duplicados")
    exigir(all(linha["status_juridico"] == "Q_SEM_C0_J" for linha in linhas), "Homologacao juridica nao registrada no gate")
    exigir(all(linha["situacao"] == "NAO_APROVADO_NAO_PROMULGADO" for linha in linhas), "Status de aprovacao divergente")
    historicas = [x for x in linhas if x["destino_experimental"].startswith("HIST-")]
    positivas = [x for x in linhas if not x["destino_experimental"].startswith("HIST-")]
    exigir(len(historicas) == cont["historicas"] and len(positivas) == cont["positivas"],
           "Destinos positivos/historicos divergentes")
    exigir(len(set(x["destino_experimental"] for x in positivas)) == len(positivas),
           "ID de destino positivo duplicado")
    exigir(all(x["categoria_preliminar"] == "HISTORICO" for x in historicas),
           "Historico sem arquivo proprio")
    classes = Counter(x["categoria_preliminar"] for x in positivas)
    exigir(classes == {"C0_T_APENAS": cont["c0_t_local"], "C1_POTENCIAL_Q": cont["c1_potencial_q"]},
           f"Classes preliminares inesperadas: {dict(classes)}")
    artigos = re.findall(r"(?m)^\\*\\*Art\\. (LPA-SEQ4-\\d{3})\\.", texto)
    exigir(len(artigos) == cont["artigos"] and len(set(artigos)) == len(artigos),
           "Quantidade de artigos ou IDs de artigo divergente")
    exigir(artigos == [f"LPA-SEQ4-{numero:03d}" for numero in range(1, len(artigos) + 1)],
           "Ordem dos artigos experimentais nao continua")
    artigos_de_destino = set()
    for registro in positivas:
        m = re.match(r"^(LPA-SEQ4-\\d{3})-", registro["destino_experimental"])
        exigir(m is not None, f"Destino positivo sem artigo identificavel: {registro['id_fonte']}")
        artigos_de_destino.add(m.group(1))
    exigir(artigos_de_destino == set(artigos), "Concordancia e texto divergem nos artigos destinatarios")
    exigir(meta["estado_juridico"] == "Q_SEM_C0_J"
           and meta["aprovacao_material"] == "NAO"
           and meta["dec016"] == "PENDENTE",
           "Manifesto perdeu ressalvas juridicas essenciais")
    return {"fontes": len(linhas), "positivas": len(positivas),
            "historicas": len(historicas), "artigos": len(artigos),
            "c0_t_local": classes["C0_T_APENAS"],
            "c1_potencial_q": classes["C1_POTENCIAL_Q"], "c0_j_homologadas": 0}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--setorial-root", type=Path, default=RAIZ,
                        help="Diretorio do checkout separado do PR #45 no SHA declarado")
    modo = parser.add_mutually_exclusive_group()
    modo.add_argument("--check", action="store_true", help="Confere equivalencia bit a bit, modo padrao")
    modo.add_argument("--write", action="store_true", help="Regera apenas a vista derivada")
    args = parser.parse_args()
    meta = json.loads(MANIFESTO.read_text(encoding="utf-8"))
    fonte = ler_fonte(args.setorial_root, meta["texto_relativo"], meta["texto_blob_sha"])
    matriz = ler_fonte(args.setorial_root, meta["concordancia_relativa"], meta["concordancia_blob_sha"])
    achados = auditar(fonte, matriz, meta)
    gerado = meta["cabecalho_editorial"] + fonte
    destino = RAIZ / meta["vista_relativa"]
    if args.write:
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_bytes(gerado.encode("utf-8"))
        print("REGERADO:", destino.relative_to(RAIZ), json.dumps(achados, ensure_ascii=False))
        return 0
    exigir(destino.is_file(), f"Vista nao existe: {destino}")
    atual = destino.read_bytes()
    esperado = gerado.encode("utf-8")
    if atual != esperado:
        delta = difflib.unified_diff(atual.decode("utf-8").splitlines(),
                                     gerado.splitlines(),
                                     fromfile="vista_committed", tofile="vista_gerada", lineterm="")
        print("\\n".join(list(delta)[:65]), file=sys.stderr)
        raise ValueError("DRIFT: a vista nao coincide com o commit setorial e o manifesto")
    print("OK: vista identica ao setorial fixado, sem homologacao juridica:",
          json.dumps(achados, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (ValueError, OSError, UnicodeError, KeyError) as erro:
        print(f"FALHA DE INTEGRIDADE: {erro}", file=sys.stderr)
        sys.exit(1)
