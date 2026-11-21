# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-11-21 15:30 (ora României) · **de:** sesiunea OS programată (13:40) — lucrul continuu (C-158). Ultimul Release: **`os-329`**, CI verde.

## Acum
- **GATA DE TEST: os-329** — nou (un singur lucru pentru placă, cum a cerut nota de la 13:00): **pozițiile lente (P6-112)** + **lista lipită implicită în ciclu**. (1) Cât rulează textele lui `kronos --gpu`, jurnalul nu mai scrie pe stick între poziții (rândurile de rutină stau în memorie și se scriu după ultima poziție; peste 1024 se aruncă cele vechi, numărate); (2) rândurile ținute se scriu ÎNAINTE de poziția 0, în afara ceasului ei; (3) umbrele uită doar cuvintele scrise (`forget_range`). Implicit `test-placa` trimite acum #513 **doar cu lista lipită** (a trecut bit cu bit în os-328); `--simplu` = lista simplă (ca os-324), `--lipit` = amândouă, comparate. **Rândul pentru teste.txt:** `test-placa`. **Cifre așteptate:** `kt pozitii lente (peste 2 x mediana)` = **0** (sau cel mult una mică); media „cu driverul” aproape de mediană, **~280–300 simb/s** (os-328: 120 față de 304,5); `kt randuri de rutina aruncate` = 0; `kt lista` = 1; aceleași 16 simboluri ca procesorul; amprenta logit-urilor `0xda9ae084` (aceeași ca os-324 și os-328); `kt cuvinte VRAM pe simbol` ~130; poziția 0 fără cei ~13 ms de jurnal. Rând nou în raport: „jurnalul in generare: nicio scriere pe stick intre pozitii …; 0 randuri de rutina aruncate”.
- **Răspunsuri la nota de la 13:00:** (1) `kt lipit fata de simplu` lipsea din raport fiindcă `/bin/kronos` trece în raport doar rândurile care conțin `kronos --gpu` — acum au prefixul (cu `--lipit`) și sunt și în jurnal (`kt lipit fata de simplu: logit-uri diferite` = 0, `… simboluri identice` = 1). (2) Pauza de ~0,9 s din prima rulare (lista simplă, 17,57 simb/s) = scrierea pe stick la a 16-a poziție a tuturor rândurilor ținute (și ale scării) — exact ce scoate os-329.
- **PREDARE → centrul de comandă: `live.cheie` e acum fișier secret (P6-113, în `os-329`)**, cum a cerut nota C-159 de la 13:00/13:35: (1) `live.cheie` și `permite-live-placa` sunt secrete oriunde sub `/usb/hub` (orice adâncime, orice majuscule) și **doar ale nucleului** — nici `cat`, nici `compara`, nici vreun program nu le poate citi (programele nici nu le pot cere); (2) `iesire`, `ecran` și `sistem` din fiecare `r-NNNN.json` trec prin ascunderea secretelor înainte să plece (valorile cheilor și token-ului, brute și ca hex → `[ascuns]`, plus orice arată a cheie); (3) la fel pentru `permite-live-placa` dacă are conținut. Testat în QEMU (`drepturi`, `ghpush`). Din partea OS, sesiunea C (cheia pentru placă) poate porni pe `os-329`.

## Urmează
- C-159 pasul 2 (**P6-111**, mâinile: `scrie`, `tasta`, `muta`, `clic`, `ecran`, `captura`) — nota de proiectare e în `cyber-universe/docs/plans/P6-111.md` (sesiunea vie trece pe un fir separat ca tastele să aibă cine le citească).
- Apoi, câte una pe Release pentru placă: LayerNorm nou (C-155 p.2), cursa pe sferturi `Fused32` (C-155 p.4), #651 (C-158 p.3), mai multe teste într-o pornire (p.5).

## Ce oferă proiectul celorlalți
- PREDARE → centrul de comandă: canalul viu (`os-326`, `docs/LIVE.md`) — vezi mai sus.
- `os-329`: lista lipită implicită în ciclu, fără scrieri pe stick în generare; `live.cheie` secret.
- `os-328`: P3 la cerere (`test-placa --lipit`) + rândurile pozițiilor lente (în orice test).
- `os-324`: dieta driverului în ciclu (testată pe placă: driverul 3 081 → 1 347 us).
- `os-323`: tabloul de bord la cerere (`--tablou`), `gpu stare`; proba FLR la cerere, comutatorul de pornire, `discuri`, temperatura procesorului, ceasul de pază.

## De ce are nevoie de la ceilalți
- Centrul de comandă: testul cu `os-329` (`test-placa`); sesiunea C a canalului viu pe `os-329`.
- Cyber-GPU: nimic urgent (notele predate sunt toate preluate sau în coadă).

## Blocaje / nevoie de Adrian
- Nimic urgent; testele le pornește centrul de comandă.
- Comutatorul de pornire (P6-102) contează pe workstation doar după ce stick-ul e primul în ordinea de pornire din BIOS — o singură schimbare, cu tine de față.
