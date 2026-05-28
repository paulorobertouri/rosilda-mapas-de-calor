#!/bin/bash
# scripts/e2e.sh — run heatmap generation and copy outputs as evidence
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MODE="${1:-test}"   # test | evidence

cd "$ROOT"

EVIDENCE_DIR="$ROOT/tests/e2e/evidence"
mkdir -p "$EVIDENCE_DIR"

run_generation() {
    echo "==> Generating heatmap outputs..."
    uv run python -m pytest backend/tests -v -q
}

case "$MODE" in
  test)
    run_generation
    ;;
  evidence)
    run_generation
    echo "==> Copying output images as evidence..."
    for f in "$ROOT/.outputs/"*.png; do
      [ -f "$f" ] || continue
      cp "$f" "$EVIDENCE_DIR/"
      echo "  copied: $(basename "$f")"
    done
    echo "Evidence saved to $EVIDENCE_DIR"
    ;;
  *)
    echo "Usage: $0 [test|evidence]" >&2
    exit 1
    ;;
esac
