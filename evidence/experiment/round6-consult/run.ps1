# Round 6 runner — consult prompts against the completed round-5 apps.
# Usage: .\run.ps1 -Arm control   |   .\run.ps1 -Arm treatment
# Fresh `codex exec` session per prompt per app; apps are NOT modified.
# Lean execution per protocol Addendum 2: apps 1-3, probes c1+c3 only,
# default model at low reasoning effort (identical both arms).
param(
    [Parameter(Mandatory = $true)][ValidateSet('control', 'treatment')][string]$Arm
)
$ErrorActionPreference = 'Stop'

$worktree = "E:\PROJEKTI\saidwhen-r5-$Arm"
$prompts = Get-ChildItem (Join-Path $PSScriptRoot 'prompts') -Filter 'c*.md' |
    Where-Object { $_.BaseName -in @('c1', 'c3') } | Sort-Object Name

for ($n = 1; $n -le 3; $n++) {
    $app = Join-Path $worktree "evidence\experiment\round5-build\runs\$Arm-$n\app"
    if (-not (Test-Path (Join-Path $app 'index.html'))) { throw "Missing round-5 app: $app" }
    $runDir = Join-Path $worktree "evidence\experiment\round6-consult\runs\$Arm-$n"
    New-Item -ItemType Directory -Force -Path $runDir | Out-Null
    $timing = Join-Path $runDir 'timing.csv'
    if (-not (Test-Path $timing)) { 'prompt,start,end' | Out-File -Encoding utf8 $timing }
    foreach ($p in $prompts) {
        $k = $p.BaseName
        $last = Join-Path $runDir "$k.md"
        if (Test-Path $last) { Write-Host "[$Arm-$n] $k already done, skipping"; continue }
        Write-Host "[$Arm-$n] $k ..."
        $start = (Get-Date).ToString('o')
        Get-Content $p.FullName -Raw | codex exec -c 'model_reasoning_effort="low"' --sandbox workspace-write --cd $app --json --output-last-message $last |
            Out-File -Encoding utf8 (Join-Path $runDir "$k.events.jsonl")
        if ($LASTEXITCODE -ne 0) { Write-Warning "[$Arm-$n] $k exited with code $LASTEXITCODE" }
        "$k,$start,$((Get-Date).ToString('o'))" | Out-File -Encoding utf8 -Append $timing
    }
    Write-Host "[$Arm-$n] done"
}
