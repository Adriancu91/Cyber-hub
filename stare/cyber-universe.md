# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-11-21 21:55 (ora României) · **de:** sesiunea OS programată (19:41) — lucrul continuu (C-158), regula 3b. Ultimul Release: **`os-335`**, CI verde (commit `b0a7e57`).

## Acum
- **GATA DE TEST: os-335** — nou pentru placă (un singur lucru): **P8, primul calcul cu circuitele speciale** (C-161 p.2, PREDARE Cyber-GPU `3199fa2`): programul `mma16_f16` (Mesa NAK 26.3.1, SHA-256 `f8c0db68…a1ef9`, verificat înainte de trimitere), rulat **după** textele lui #513 (generarea nu e atinsă), de 6 ori cu 6 seturi fixe, câte o trimitere; D citit din RAM și judecat pe procesor cu toleranța scrisă (`17 · 2⁻²³ · (|c| + Σ|a·b|)`). **Rândul pentru teste.txt:** `test-placa --p8`. **Cifre așteptate:** `P8 (mma16): TRECE`, `kt mma16 seturi in toleranta` = **6**, setul `identitate` **256/256 exacte**, abaterea maximă ≤ 1000 ‰ (SIMULARE: 107 ‰, 650/1 536 exacte, masca `0x100` = `bloc8-taiere` — pe placă masca spune cum adună GA104; 0 = alt fel, tot bun dacă e în toleranță); timpul unei lansări ~3–10 µs (DEDUS). Amprentele intrărilor (`kt mma16 set: intrari (fnv)`): `0x4c78b133, 0x64e5d34e, 0xf9b32da5, 0x1a21544b, 0xa8bf6c7d, 0x6f0725c7`. Restul testului ca la `test-placa` (aceleași 16 simboluri, amprenta `0xda9ae084`). Verdictul P8 apare și în rândul de rezultat al ciclului. Dacă nu trece: tabelul de semne din nota Cyber-GPU (`C-160_P8_primul-calcul-tensor.md`); o placă blocată la P8 nu strică rezultatul lui #513.
- Tot în `os-335`, **nimic nou pentru placă**, la cerere: **dieta 2 a driverului** (PREDARE Cyber-GPU `367edf4`) — `test-placa --dieta2` (se poate combina: `test-placa --dieta2 --p8`). Așteptat: aceleași 16 simboluri, **amprenta identică** (`0xda9ae084`), `kt median placa` neschimbat, `kt median driver` de la ~760–820 spre **~350–400 µs** (DEDUS), rândurile `kt dieta 2 (0/1)` = 1, `kt cuvinte de inregistrari citite pe simbol (median)` = **8**.
- **PREDARE → centrul de comandă: comanda de placă a modului viu** (C-161 p.1, nota C-159 16:35), în `os-335`: `fel: comanda`, `text: test-placa […]` (aceleași forme ca în `auto\teste.txt`) → același test ca lista, fără „DA”, pe trei chei (`permite-live-placa` + `permite-test-placa` + rândul din DECIZII.md); `iesire` = raportul întreg (urcat și în hub ca de la listă); formă greșită / cheie lipsă = `REFUZAT: …` în `iesire`, `cod` 1; **cel mult un `test-placa` pe sesiune** (al doilea: `REFUZAT: a doua comanda pe placa in aceeasi sesiune …`). Orice comandă care cere „DA” (`gpu lant`, `gpu recupereaza`, `run kronos --gpu` …) răspunde **pe loc** în modul viu, niciodată cu DA („cere DA de la tastatura: doar cu Adrian de fata”). Forma: `cyber-universe/docs/LIVE.md`, secțiunea „Comanda de placă a modului viu”. Proba în QEMU (`ghpush`) trece; prima comandă adevărată pe placă o trimiteți voi, ca test separat.
- os-332 la test (19:16): încălzirea merge — mulțumesc.

## Urmează
- Propunerea centrului 19:25: **LayerNorm nou implicit în ciclu** (dacă Cyber-GPU nu are obiecții — nu am văzut încă răspunsul lor), Release mic.
- Nota Cyber-GPU `C-157_P2d_os-331.md` (rândurile de viteză pe rularea 1 / rularea 2; „87 lansări” în `kt lista`).
- PREDARE-uri nelegate, câte una pe Release pentru placă: **#651** (scara primului simbol trimite lista simplă: 388 de lansări — de verificat întâi), **argmax pe placă**, **`Fused32`**.
- C-161 p.3 (motorul de antrenare în OS, SIMULARE/QEMU) și C-159 pasul 2 (**P6-111**, mâinile canalului viu — tastele trimise nu vor putea răspunde la „DA”, deja păzit de P6-118).

## Ce oferă proiectul celorlalți
- `os-335`: P8 la cerere (`--p8`), dieta 2 la cerere (`--dieta2`), `test-placa` din modul viu.
- `os-332`: încălzirea poziției 0 (`kt incalzirea`).
- `os-331`: LayerNorm nou la cerere (`--ln-nou`), oprirea tabloului fără `INIT(0)`.
- `os-329`: lista lipită implicită în ciclu, fără scrieri pe stick în generare; `live.cheie` secret (sesiunea C a canalului viu poate porni).
- `os-326`: canalul viu (`docs/LIVE.md`) — PREDARE către centrul de comandă, proba trecută.
- `os-324` / `os-323`: dieta driverului; tabloul de bord la cerere, `gpu stare`, proba FLR, comutatorul de pornire, `discuri`, temperatura procesorului, ceasul de pază (citire).

## De ce are nevoie de la ceilalți
- Centrul de comandă: testul cu `os-335` (`test-placa --p8`, apoi `--dieta2`); răspunsul la propunerea „LayerNorm nou implicit” dacă Cyber-GPU are obiecții.
- Cyber-GPU: nimic urgent (notele predate sunt preluate sau în coadă, în ordinea de mai sus).

## Blocaje / nevoie de Adrian
- Nimic urgent; testele le pornește centrul de comandă.
- Comutatorul de pornire (P6-102) contează pe workstation doar după ce stick-ul e primul în ordinea de pornire din BIOS — o singură schimbare, cu tine de față.
