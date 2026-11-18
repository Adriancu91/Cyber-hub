# C-138 (Adrian, 18 nov 2026): curatenie pe C: - modele intermediare si stari de reluare ale liniilor terminate.
# Fara -Sterge: doar verificare (scrie ce AR sterge). Cu -Sterge: sterge doar fisierele din lista, cu plasa de siguranta.
param([switch]$Sterge)
$ErrorActionPreference = 'Stop'
$root = 'C:\Kronos\cyberspace'
$mod  = Join-Path $root 'lucru\stocare\modele'
$out  = 'C:\Kronos\curatenie'
$mode = if ($Sterge) { 'STERGERE' } else { 'VERIFICARE' }
$log  = Join-Path $out ("raport_C138_" + $mode + ".txt")
New-Item -ItemType Directory -Force -Path $out | Out-Null
Set-Content -Path $log -Value '' -Encoding UTF8
$L = New-Object System.Collections.Generic.List[string]
function Say($s) { $L.Add($s); Write-Host $s; Add-Content -Path $log -Value $s -Encoding UTF8 }
trap { Say ("EROARE: " + $_.Exception.Message + " (linia " + $_.InvocationInfo.ScriptLineNumber + ")"); exit 2 }

$listaModele = @(590..640) + @(645..650) + @(665,666,667,677,678,679,689,690,691) +
          @(517,523,525,528,529,532,533,534,535,540,542,544,546,548,550,551,552,553,558,562) +
          @(286,299,300,314,316,317,337,363,394,405,413,424,428,431,436,443,446,451,462,466,471,499,505,508,575,576)
$pastreaza = @(252,257,262,295,312,353,373,385,401,407,415,422,429,438,441,459,477,513,536,554,563,577,641,651,668,680,692)
$keepDirs = @('w2_mare_24zcf','w2_mare_24zch','w2_mare_24zcc','w2_mare_24zc','w2_mare_24z2','w2_mare','stocare')

Say ("C-138 " + $mode + " - " + (Get-Date -Format 'yyyy-MM-dd HH:mm:ss'))
foreach ($n in $listaModele) { if ($pastreaza -contains $n) { Say "OPRIT: #$n e si in lista de pastrat"; exit 1 } }

# nicio antrenare in curs
$tr = Get-CimInstance Win32_Process | Where-Object { $_.Name -like 'python*' -and $_.CommandLine -match 'antrenare|_proba\\s1|s12[0-9]\.py|orchestrator' }
if ($tr) { Say "OPRIT: ruleaza o antrenare / un lant:"; $tr | ForEach-Object { Say ("  " + $_.ProcessId + " " + $_.CommandLine) }; exit 1 }

$free0 = (Get-PSDrive C).Free
Say ("C: liber inainte: {0:N1} GB" -f ($free0/1e9))

# referinte active in cod/configurari
$files = Get-ChildItem (Join-Path $root 'config'),(Join-Path $root 'unelte'),(Join-Path $root 'module'),(Join-Path $root 'kronos') -Recurse -File -Include *.toml,*.py,*.ps1 -ErrorAction SilentlyContinue | Where-Object { $_.FullName -notmatch '__pycache__' }
$txt = ($files | ForEach-Object { Get-Content $_.FullName -Raw -ErrorAction SilentlyContinue }) -join "`n"
Say ("fisiere de cod/configurari verificate: " + $files.Count)

$total = 0; $nDel = 0
Say ""; Say "== Modele (lucru\stocare\modele) =="
foreach ($n in $listaModele) {
  $f = Join-Path $mod ("experiment_$n.pt")
  if (-not (Test-Path $f)) { Say "  lipseste deja: #$n"; continue }
  $pat = "(--experiment|--porneste-din|--experiment-text)[ =]+$n\b|experiment_$n\b|model_in_uz\s*=\s*$n\b|experimente\s*=\s*\[[^\]]*\b$n\b|#$n\b"
  if ($txt -match $pat) { Say ("  PASTRAT din prudenta: #$n (folosit in cod/configurari: '" + $Matches[0] + "')"); continue }
  $sz = (Get-Item $f).Length
  if ($Sterge) { Remove-Item -LiteralPath $f -Force; Say ("  sters #$n  {0:N2} GB" -f ($sz/1e9)) } else { Say ("  AR STERGE #$n  {0:N2} GB" -f ($sz/1e9)) }
  $total += $sz; $nDel++
}

Say ""; Say "== Stari de reluare (gpt*.pt) din dosarele antrenarilor terminate =="
$lim = (Get-Date).AddHours(-12)
Get-ChildItem (Join-Path $root 'lucru') -Directory | Where-Object { $keepDirs -notcontains $_.Name } | ForEach-Object {
  $d = $_
  Get-ChildItem $d.FullName -File -Filter 'gpt*.pt' -ErrorAction SilentlyContinue | ForEach-Object {
    if ($_.LastWriteTime -gt $lim) { Say ("  PASTRAT (modificat in ultimele 12 ore): " + $d.Name + "\" + $_.Name); return }
    if ($Sterge) { Remove-Item -LiteralPath $_.FullName -Force; Say ("  sters {0}\{1}  {2:N2} GB" -f $d.Name, $_.Name, ($_.Length/1e9)) } else { Say ("  AR STERGE {0}\{1}  {2:N2} GB" -f $d.Name, $_.Name, ($_.Length/1e9)) }
    $script:total += $_.Length; $script:nDel++
  }
}

Say ""
Say ("Total {0}: {1} fisiere, {2:N1} GB" -f ($(if ($Sterge) {'sters'} else {'de sters'})), $nDel, ($total/1e9))
Say ("C: liber acum: {0:N1} GB" -f ((Get-PSDrive C).Free/1e9))
Say "Pastrate mereu: #252 #257 #262 #295 #312 #353 #373 #385 #401 #407 #415 #422 #429 #438 #441 #459 #477 #513 #536 #554 #563 #577 #641 #651 #668 #680 #692; starile din w2_mare_24zcf/24zch/24zcc/24zc/24z2 si w2_mare\gpt_24.pt; datele, examenele, jurnalul, codul."
