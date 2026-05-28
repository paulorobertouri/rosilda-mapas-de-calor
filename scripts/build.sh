#!/bin/bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "$ROOT"
echo "Building rosilda-mapas-de-calor..."
uv run python -m compileall backend/src 2>/dev/null || true
echo "Build check complete."
