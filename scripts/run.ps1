Clear-Host

$ErrorActionPreference = "Stop"
$Root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path

Push-Location $Root
try {
    Write-Host "==> Generating heatmaps..." -ForegroundColor Green
    uv run python -m backend.src.shared.mapping.Geral
    uv run python -m backend.src.shared.mapping.Empresas
    Write-Host "Heatmaps generated."
} finally {
    Pop-Location
}