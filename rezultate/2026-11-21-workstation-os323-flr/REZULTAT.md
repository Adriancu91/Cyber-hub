# Rezultat: proba de reset al plăcii din interior (FLR) pe placa reală (os-323, ciclu automat) — 21 nov 2026, 08:32

- **Unde:** workstation (RTX 3070 Ti, GA104), ciclul automat, fără om de față. Semnal la ~08:26, testul a început la 08:32:40, a ținut 217 s, Windows înapoi la ~08:37.
- **Versiunea:** `os-323` (`81d042f`), cyber-gpu `de4887d`. Rândul din listă: `test-placa --flr-proba` (fără tablou).
- **Fișierele brute** (urcate singure de OS): `rezultate/os-automat/2026-11-21/ciclu-auto-20261121-0832.txt`, `gpu-jurnal-020.txt`, `gpu-jurnal-021.txt` (primul lanț), `gpu-jurnal-022.txt` (resetul + al doilea lanț).

## Ce era nou: resetul din interior (C-151 punctul 3, C-152 punctul 1) — MERGE
1. Primul lanț a rulat ca de obicei și a lăsat zona protejată a plăcii ridicată (WPR2 0x1f4100000..0x1ffee0000) — starea în care, până azi, un al doilea lanț cerea repornirea calculatorului.
2. Resetul: Bus Master oprit → FLR declanșat → **placa răspunde din nou după 131 348 µs (0,13 s)** → configurația rescrisă → programul de pornire al plăcii gata după 206 084 µs → **WPR2 coborât (0)**. Rândul: `kf wpr2-coborat wpr2_inainte=0x1f4100000..0x1ffee0000 wpr2_dupa=0 gata_us=131348 gfw_us=206084`.
3. **Al doilea lanț, în aceeași pornire: toți pașii au trecut** (2 373 de scrieri): pregătirea (I6), pornirea programului plăcii, I10 (64 de rezultate identice bit cu bit cu procesorul), I13, I14 (cele trei texte de control TREC; 29 de simboluri, abaterea maximă 3,58e-6), turul de citire de la sfârșit TRECE. Avertizările interne ale plăcii: 44 de rânduri / 4 ASSERT, exact ca la un lanț obișnuit.

Concluzia: „varianta 1” din studiul Cyber-GPU e dovedită pe placă. Rezerva (Booter Unload) n-a fost necesară.

**De lămurit (nimic n-a picat):** rândul „adaptoarele OS au REFUZAT 11 scrieri cerute în afara gardului” la al doilea lanț. Apare prima dată într-un raport de ciclu (rapoartele dinainte nu aveau un `gpu lant` simplu cu care să compar). → sesiunea OS: care sunt cele 11 scrieri și dacă sunt cele așteptate (gardul lasă la rescrierea configurației doar antetul 0x04–0x3c, PCIe control și MSI).

## Testul obișnuit din aceeași rulare (primul lanț)
- 16 simboluri din 16 identice cu procesorul; cu driverul **94,53 simb/s**; doar placa 381,90; procesorul 72,72; cu verificarea 38,17.
- Timpul pe simbol: placa 2 623 µs, driverul 3 075 µs, jurnalul 61 µs = 5 793 µs. Înainte de cererea de viteză placa era în P0 (ca la 08:21).

## Ce deschide
- **Mai multe teste într-o singură pornire** (C-158 punctul 5): cu resetul între ele, de la 2–4 teste pe zi spre 10–20.
- Uneltele treptei 1: tabloul de bord și resetul sunt acum dovedite pe placă; rămân comutatorul de pornire (cu Adrian, BIOS) și armarea ceasului de pază.
