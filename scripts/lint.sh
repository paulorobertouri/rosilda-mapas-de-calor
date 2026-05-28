#!/bin/bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "$ROOT"
echo "==> ruff check..."
uv run ruff check .

echo "==> ruff format --check..."
uv run ruff format --check .

echo ""
echo "Lint checks passed."
