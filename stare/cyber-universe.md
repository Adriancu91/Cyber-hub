# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-11-21 19:15 (ora României) · **de:** sesiunea OS programată (17:11) — lucrul continuu (C-158), regula 3b. Ultimul Release: **`os-332`**, CI verde.

## Acum
- **GATA DE TEST: os-332** — ce e nou: **încălzirea poziției 0** (PREDARE Cyber-GPU `538e3b4`, după os-329; nota 16:35 „poziția 0 lentă”). Pentru placă **nimic nou**: aceleași lansări, același simbol, poziția 0 a fiecărei liste trimisă o dată în plus, înainte de ceas (nu intră în medie). **Rândul pentru teste.txt:** `test-placa` (cel obișnuit). **Cifre așteptate:** 16/16 simboluri identice, amprenta `0xda9ae084` (ca os-329), `kt pozitii lente` = **0** (os-329: 1, poziția 0 cu driver 9 863 µs), driverul poziției 0 ~1,8 ms, `kt cuvinte VRAM pe simbol` ~130, **~297 simb/s** cu driverul (DEDUS de Cyber-GPU; os-329: 262). Rânduri noi: `kt incalzirea: …` (1 listă, ~3–4 ms în afara ceasului, ~12 300 de cuvinte VRAM la încălzire). O sonerie de canal în plus pe listă (încălzirea).
- **GATA DE TEST: os-331** — nou pentru placă (un singur lucru): **LayerNorm nou** (C-155 punctul 2, programul `layernorm256`: 256 de fire, `shfl` + barieră — primul de felul acesta pe placă), **doar la cerere**. **Rândul pentru teste.txt:** `test-placa --ln-nou`. #513 rulează de două ori pe același text cu lista lipită: întâi cu LayerNorm vechi (ca os-329), apoi cu cel nou, comparate. **Cifre așteptate:** ambele texte trec oracolul procesorului, aceleași 16 simboluri ca procesorul; rândul `kt ln nou fata de vechi: max |d| = …` **sub 1e-4** (SIMULARE Cyber-GPU: 3,1e-7), `simboluri identice: da`, `kt ln nou fata de vechi: TRECE`; `kt lista` = 3; în `kp` LayerNorm (ln1/ln2/ln_final) mult mai mic: ~3–5 µs pe lansare în loc de ~21,8 → **~0,45 ms mai puțin pe simbol** (DEDUS) la a doua rulare. Dacă nu trece: lanțul se oprește cu diagnosticul obișnuit; `test-placa` simplu (lista lipită cu LayerNorm vechi) rămâne neschimbat.
- Tot în `os-331`, **nimic nou pentru placă**: oprirea tabloului de bord fără `INIT(0)` (PREDARE Cyber-GPU `fb22ffb`) — contează doar cu `--tablou`: o comandă mai puțin, așteptat niciun refuz în rândurile `kd` („oprirea zonei = nu se trimite …, ca driverul NVIDIA”).
- os-329 la test (15:56): media 262 simb/s — mulțumesc; nimic de reparat din partea OS.

## Urmează
- Ordinea după nota 16:35: **C-161 p.1** (comanda de placă a modului viu, nimic nou pentru placă), **dieta 2** (nimic nou pentru placă), **P8** când vine PREDARE (C-160 p.1); apoi restul.
- PREDARE-uri Cyber-GPU nelegate, câte una pe Release pentru placă: **#651** (C-158 p.3, nota `C-157_P4_k651-limite.md`: limitele pe lista care rulează + opțiunea `test-placa --k651`; de verificat întâi scara primului simbol, care trimite lista simplă de 388 de lansări), **dieta 2** (nimic nou pentru placă), argmax pe placă, `Fused32`.
- Apoi C-159 pasul 2 (**P6-111**, mâinile canalului viu; nota de proiectare în `cyber-universe/docs/plans/P6-111.md`).

## Ce oferă proiectul celorlalți
- `os-332`: încălzirea poziției 0 (`kt incalzirea`).
- `os-331`: LayerNorm nou la cerere (`--ln-nou`), oprirea tabloului fără `INIT(0)`.
- `os-329`: lista lipită implicită în ciclu, fără scrieri pe stick în generare; `live.cheie` secret (sesiunea C a canalului viu poate porni).
- `os-326`: canalul viu (`docs/LIVE.md`) — PREDARE către centrul de comandă, proba trecută.
- `os-324` / `os-323`: dieta driverului; tabloul de bord la cerere, `gpu stare`, proba FLR, comutatorul de pornire, `discuri`, temperatura procesorului, ceasul de pază (citire).

## De ce are nevoie de la ceilalți
- Centrul de comandă: testele cu `os-331` (`test-placa --ln-nou`) și `os-332` (`test-placa`).
- Cyber-GPU: nimic urgent (notele predate sunt preluate sau în coadă, în ordinea de mai sus).

## Blocaje / nevoie de Adrian
- Nimic urgent; testele le pornește centrul de comandă.
- Comutatorul de pornire (P6-102) contează pe workstation doar după ce stick-ul e primul în ordinea de pornire din BIOS — o singură schimbare, cu tine de față.
