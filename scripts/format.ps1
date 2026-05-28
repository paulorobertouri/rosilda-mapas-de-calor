# scripts/format.ps1 — format with ruff
$ErrorActionPreference = "Stop"
$Root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path

Push-Location $Root
try {
    uv run ruff format .
    Write-Host "Format complete."
} finally {
    Pop-Location
}
