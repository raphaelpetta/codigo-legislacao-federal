#!/usr/bin/env bash
# Validacao offline CLF: requer checkout setorial fixado para conferir T07.
set -euo pipefail
cd "$(dirname "$0")/.."

# Modo corpus atual R24: os validadores R10-R23 possuem asserts de snapshot
# (48/51/54 vistas etc.) e nao podem rodar contra a fotografia de 55 vistas.
# Historicos continuam disponiveis na branch/commit de cada rodada.
if [[ -f produto/fontes/T23_M01_LINDB_DIP_6_R24_v1.json ]]; then
  python3 scripts/verificar_estrutura.py
  python3 scripts/controle_operacional.py --check
  python3 -m unittest discover -s tests -p 'test_controle_operacional.py' -v
  python3 scripts/validar_corpus_ativo.py
  python3 scripts/validar_r24_t23_e_auditoria.py
  python3 scripts/validar_r25_auditoria_r3.py
  python3 scripts/gerar_codigo_integrado.py --check
  if [[ $# -lt 1 ]]; then
    echo "PARCIAL R24: T07/T24/T25 externos nao cotejados; indique os tres checkouts nos SHAs dos manifestos." >&2
    exit 2
  fi
  python3 scripts/gerar_produto_experimental.py --setorial-root "$1" --check
  if [[ -f produto/fontes/T24_M01_106_v1.json ]]; then
    if [[ $# -lt 2 ]]; then
      echo "PARCIAL R24: T24 setorial ausente; informe segundo checkout." >&2
      exit 2
    fi
    python3 scripts/gerar_previa_t24.py --setorial-root "$2" --check
  fi
  if [[ -f produto/fontes/T25_CP1_12_v1.json ]]; then
    if [[ $# -lt 3 ]]; then
      echo "PARCIAL R24: T25 setorial ausente; informe terceiro checkout." >&2
      exit 2
    fi
    python3 scripts/gerar_previa_t25.py --setorial-root "$3" --check
  fi
  echo "OK QA DOCUMENTAL R24 no snapshot atual (sem DOU, C0-J ou execucao CI)." 
  exit 0
fi

python3 scripts/verificar_estrutura.py
python3 scripts/controle_operacional.py --check
python3 -m unittest discover -s tests -p 'test_controle_operacional.py' -v
python3 scripts/gerar_t24_cpc_181.py --check
python3 scripts/gerar_previa_t05.py --check
python3 scripts/gerar_previa_t05_23.py
python3 scripts/gerar_previa_t48.py
python3 scripts/validar_r10_t48_t37.py
python3 scripts/validar_r11_t28_t37_t48.py
python3 scripts/validar_r12_t03_t37_t48.py
python3 scripts/validar_r13_t03_t48.py
python3 scripts/validar_r14_horizontal_matriz.py
python3 scripts/validar_r15_horizontal_matriz.py
python3 scripts/validar_r16_horizontal.py
python3 scripts/validar_r17_horizontal.py
python3 scripts/validar_r18_horizontal_e_proveniencia.py
python3 scripts/validar_r19_horizontal_ci.py
python3 scripts/validar_r20_horizontal.py
python3 scripts/validar_r21_horizontal.py
python3 scripts/validar_r22_fonte_e_codigo.py
python3 scripts/validar_r23_corpus_auditoria.py
python3 scripts/validar_r24_t23_e_auditoria.py
python3 scripts/gerar_codigo_integrado.py --check
if [[ $# -lt 1 ]]; then
  echo "PARCIAL: T07 NAO CONFERIDO. Informe caminho do checkout setorial no SHA do manifesto:" >&2
  echo "  bash scripts/validar_operacao_local.sh /caminho/checkout-PR45" >&2
  exit 2
fi
python3 scripts/gerar_produto_experimental.py --setorial-root "$1" --check
if [[ -f produto/fontes/T24_M01_106_v1.json ]]; then
  if [[ $# -lt 2 ]]; then
    echo "PARCIAL: T24 NAO CONFERIDO. Use os checkouts de origem T07 e T24:" >&2
    echo "  bash scripts/validar_operacao_local.sh /checkout-PR45 /checkout-PR38" >&2
    exit 2
  fi
  python3 scripts/gerar_previa_t24.py --setorial-root "$2" --check
fi
if [[ -f produto/fontes/T25_CP1_12_v1.json ]]; then
  if [[ $# -lt 3 ]]; then
    echo "PARCIAL: T25 NAO CONFERIDO. Forneca tres checkouts nos SHAs dos manifestos:" >&2
    echo "  bash scripts/validar_operacao_local.sh /checkout-PR45 /checkout-PR38 /checkout-PR32" >&2
    exit 2
  fi
  python3 scripts/gerar_previa_t25.py --setorial-root "$3" --check
fi
echo "OK DOCUMENTAL LOCAL CLF (sem certificacao de equivalencia juridica)."
