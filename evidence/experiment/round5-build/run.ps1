# Round 5 runner — one arm per invocation, in that arm's dedicated worktree.
# Usage:  .\run.ps1 -Arm control -Runs 6
#         .\run.ps1 -Arm treatment -Runs 6
# Each run n copies the pristine fixture into the arm's worktree and plays
# prompts p1..p5 as FRESH `codex exec` sessions (no shared context between
# prompts — cross-session recall is the thing under test). Prompts are piped
# via stdin; codex exec reads instructions from stdin when no arg is given.
param(
    [Parameter(Mandatory = $true)][ValidateSet('control', 'treatment')][string]$Arm,
    [int]$Runs = 6,
    [int]$StartAt = 1
)
$ErrorActionPreference = 'Stop'

$worktree = "E:\PROJEKTI\saidwhen-r5-$Arm"
if (-not (Test-Path $worktree)) {
    throw "Worktree not found: $worktree  (create: git worktree add -b round5-$Arm $worktree main)"
}
$fixture = Join-Path $PSScriptRoot "fixtures\$Arm"
$prompts = Get-ChildItem (Join-Path $PSScriptRoot 'prompts') -Filter 'p*.md' | Sort-Object Name

for ($n = $StartAt; $n -lt ($StartAt + $Runs); $n++) {
    $runDir = Join-Path $worktree "evidence\experiment\round5-build\runs\$Arm-$n"
    $app = Join-Path $runDir 'app'
    if (Test-Path $app) { throw "Run dir already exists, refusing to overwrite: $app" }
    New-Item -ItemType Directory -Force -Path $app | Out-Null
    if (Test-Path (Join-Path $fixture '*')) {
        Copy-Item -Path (Join-Path $fixture '*') -Destination $app -Recurse -Force
    }
    foreach ($p in $prompts) {
        $k = $p.BaseName
        Write-Host "[$Arm-$n] $k ..."
        $promptText = Get-Content $p.FullName -Raw
        $events = Join-Path $runDir "$k.events.jsonl"
        $last = Join-Path $runDir "$k.md"
        $promptText | codex exec --sandbox workspace-write --cd $app --json --output-last-message $last |
            Out-File -Encoding utf8 $events
        if ($LASTEXITCODE -ne 0) { Write-Warning "[$Arm-$n] $k exited with code $LASTEXITCODE" }
    }
    Write-Host "[$Arm-$n] done -> $runDir"
}
