#!/usr/bin/env bash
# Validacao offline CLF: requer checkout setorial fixado para conferir T07.
set -euo pipefail
cd "$(dirname "$0")/.."
python3 scripts/verificar_estrutura.py
python3 scripts/controle_operacional.py --check
python3 -m unittest discover -s tests -p 'test_controle_operacional.py' -v
python3 scripts/gerar_t24_cpc_181.py --check
python3 scripts/gerar_previa_t05.py --check
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
