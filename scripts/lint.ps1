# scripts/lint.ps1 — ruff check + ruff format check
$ErrorActionPreference = "Stop"
$Root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path

Push-Location $Root
try {
    Write-Host "==> ruff check..."
    uv run ruff check .

    Write-Host "==> ruff format --check..."
    uv run ruff format --check .

    Write-Host ""
    Write-Host "Lint checks passed."
} finally {
    Pop-Location
}
