# scripts/e2e.ps1 — run heatmap generation and copy outputs as evidence
$ErrorActionPreference = "Stop"
$Root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$Mode = if ($args.Count -gt 0) { $args[0] } else { "test" }

$EvidenceDir = Join-Path $Root "tests/e2e/evidence"
New-Item -ItemType Directory -Force -Path $EvidenceDir | Out-Null

function Run-Generation {
    Write-Host "==> Generating heatmap outputs..."
    uv run python -m pytest backend/tests -v -q
}

Push-Location $Root
try {
    switch ($Mode) {
        "test" {
            Run-Generation
        }
        "evidence" {
            Run-Generation
            Write-Host "==> Copying output images as evidence..."
            Get-ChildItem -Path "$Root/.outputs" -Filter "*.png" | ForEach-Object {
                Copy-Item $_.FullName -Destination $EvidenceDir
                Write-Host "  copied: $($_.Name)"
            }
            Write-Host "Evidence saved to $EvidenceDir"
        }
        Default {
            Write-Error "Usage: .\scripts\e2e.ps1 [test|evidence]"
            exit 1
        }
    }
} finally {
    Pop-Location
}
