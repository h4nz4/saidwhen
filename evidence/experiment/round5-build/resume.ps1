# Round 5 resume after the 2026-07-08 Codex usage-limit interruption.
# Finishes the interrupted sequences at their next prompt (every prompt is an
# independent fresh session, so this is protocol-clean; disclosed in results),
# then runs the remaining whole sequences via run.ps1.
param(
    [Parameter(Mandatory = $true)][ValidateSet('control', 'treatment')][string]$Arm
)
$ErrorActionPreference = 'Stop'

function Invoke-Prompt($runDir, $k) {
    $app = Join-Path $runDir 'app'
    $p = Join-Path $PSScriptRoot "prompts\$k.md"
    $events = Join-Path $runDir "$k.events.jsonl"
    $last = Join-Path $runDir "$k.md"
    Write-Host "[resume] $runDir $k ..."
    Get-Content $p -Raw | codex exec --sandbox workspace-write --cd $app --json --output-last-message $last |
        Out-File -Encoding utf8 $events
    if ($LASTEXITCODE -ne 0) { Write-Warning "[resume] $k exited with code $LASTEXITCODE" }
}

if ($Arm -eq 'control') {
    $r3 = "E:\PROJEKTI\saidwhen-r5-control\evidence\experiment\round5-build\runs\control-3"
    foreach ($k in 'p3', 'p4', 'p5') { Invoke-Prompt $r3 $k }
    & (Join-Path $PSScriptRoot 'run.ps1') -Arm control -StartAt 4 -Runs 3
} else {
    $t3 = "E:\PROJEKTI\saidwhen-r5-treatment\evidence\experiment\round5-build\runs\treatment-3"
    foreach ($k in 'p4', 'p5') { Invoke-Prompt $t3 $k }
    & (Join-Path $PSScriptRoot 'run.ps1') -Arm treatment -StartAt 4 -Runs 3
}
