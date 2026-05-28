#!/bin/bash
# scripts/run.sh — generate heatmap outputs
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "$ROOT"
echo "==> Generating heatmaps..."
uv run python -m backend.src.shared.mapping.Geral
uv run python -m backend.src.shared.mapping.Empresas
echo "Heatmaps generated."
