#!/usr/bin/env bash
# Validacao offline CLF: requer checkout setorial fixado para conferir T07.
set -euo pipefail
cd "$(dirname "$0")/.."
python3 scripts/verificar_estrutura.py
python3 scripts/controle_operacional.py --check
if [[ $# -lt 1 ]]; then
  echo "PARCIAL: T07 NAO CONFERIDO. Informe caminho do checkout setorial no SHA do manifesto:" >&2
  echo "  bash scripts/validar_operacao_local.sh /caminho/checkout-PR45" >&2
  exit 2
fi
python3 scripts/gerar_produto_experimental.py --setorial-root "$1" --check
echo "OK DOCUMENTAL LOCAL CLF (sem certificacao de equivalencia juridica)."
