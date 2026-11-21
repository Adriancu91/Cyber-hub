# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-11-21 16:56 (ora României) · **de:** sesiunea OS programată (15:41) — lucrul continuu (C-158), regula 3b. Ultimul Release: **`os-331`**, CI verde.

## Acum
- **GATA DE TEST: os-331** — nou pentru placă (un singur lucru): **LayerNorm nou** (C-155 punctul 2, programul `layernorm256`: 256 de fire, `shfl` + barieră — primul de felul acesta pe placă), **doar la cerere**. **Rândul pentru teste.txt:** `test-placa --ln-nou`. #513 rulează de două ori pe același text cu lista lipită: întâi cu LayerNorm vechi (ca os-329), apoi cu cel nou, comparate. **Cifre așteptate:** ambele texte trec oracolul procesorului, aceleași 16 simboluri ca procesorul; rândul `kt ln nou fata de vechi: max |d| = …` **sub 1e-4** (SIMULARE Cyber-GPU: 3,1e-7), `simboluri identice: da`, `kt ln nou fata de vechi: TRECE`; `kt lista` = 3; în `kp` LayerNorm (ln1/ln2/ln_final) mult mai mic: ~3–5 µs pe lansare în loc de ~21,8 → **~0,45 ms mai puțin pe simbol** (DEDUS) la a doua rulare. Dacă nu trece: lanțul se oprește cu diagnosticul obișnuit; `test-placa` simplu (lista lipită cu LayerNorm vechi) rămâne neschimbat.
- Tot în `os-331`, **nimic nou pentru placă**: oprirea tabloului de bord fără `INIT(0)` (PREDARE Cyber-GPU `fb22ffb`) — contează doar cu `--tablou`: o comandă mai puțin, așteptat niciun refuz în rândurile `kd` („oprirea zonei = nu se trimite …, ca driverul NVIDIA”).
- os-329 la test (15:56): media 262 simb/s — mulțumesc; nimic de reparat din partea OS.

## Urmează
- PREDARE-uri Cyber-GPU nelegate, câte una pe Release pentru placă: **#651** (C-158 p.3, nota `C-157_P4_k651-limite.md`: limitele pe lista care rulează + opțiunea `test-placa --k651`; de verificat întâi scara primului simbol, care trimite lista simplă de 388 de lansări), **dieta 2** (nimic nou pentru placă), argmax pe placă, `Fused32`.
- Apoi C-159 pasul 2 (**P6-111**, mâinile canalului viu; nota de proiectare în `cyber-universe/docs/plans/P6-111.md`).

## Ce oferă proiectul celorlalți
- `os-331`: LayerNorm nou la cerere (`--ln-nou`), oprirea tabloului fără `INIT(0)`.
- `os-329`: lista lipită implicită în ciclu, fără scrieri pe stick în generare; `live.cheie` secret (sesiunea C a canalului viu poate porni).
- `os-326`: canalul viu (`docs/LIVE.md`) — PREDARE către centrul de comandă, proba trecută.
- `os-324` / `os-323`: dieta driverului; tabloul de bord la cerere, `gpu stare`, proba FLR, comutatorul de pornire, `discuri`, temperatura procesorului, ceasul de pază (citire).

## De ce are nevoie de la ceilalți
- Centrul de comandă: testul cu `os-331` (`test-placa --ln-nou`).
- Cyber-GPU: nimic urgent (notele predate sunt preluate sau în coadă, în ordinea de mai sus).

## Blocaje / nevoie de Adrian
- Nimic urgent; testele le pornește centrul de comandă.
- Comutatorul de pornire (P6-102) contează pe workstation doar după ce stick-ul e primul în ordinea de pornire din BIOS — o singură schimbare, cu tine de față.
