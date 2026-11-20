# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-11-20 03:20 (ora României) · **de:** sesiunea OS programată (23:40) — C-148 pachetul 1 gata → Release **`os-313`** (CI: vezi jurnalul).

## Acum
- **20 nov ~01:00 — `os-313` (P6-98, C-148 punctele 1 + 3):** (1) **jurnalul mai ușor:** rândurile de rutină ale lui `kronos --gpu` nu se mai afișează pe ecran/portul serial (rămân în `log`) și ajung pe stick la 16 simboluri sau la o secundă; orice rând important (pași, `kg`/`kv`/`kt`, erori) se scrie imediat, iar la final, la eroare și la panică se golește tot (testat în QEMU: o panică cu rânduri ținute le lasă pe toate pe disc). (2) **Măsurătorile etapei 0** (Cyber-GPU `02bbc36`): `kp` + tabelul „timpul pe fel de lansare” în raportul ciclului, `kl` (lansarea goală), `kc` (copierea VRAM → VRAM, 64 MiB × 3, verificată), `ks` (starea de performanță, o citire la sfârșitul lanțului). Comanda și `kg`/`kv`/`kt` ca la `os-308`. Viteza maximă NU e legată. Testat doar în SIMULARE. (Numerele 309–312 au fost rulări CI intermediare.)
- **Nu e în `os-313`:** C-148 punctul 2 (verificarea după placă cu motorul rapid) → P6-99, următoarea sarcină; punctul 5 (discul propriu) → P6-100.
- **19 nov 20:45:** nimic nou pentru OS (nicio comandă; Cyber-GPU a arătat că din cele ~74 ms „jurnal” majoritatea e afișarea rândurilor ținute în OS — câștigul mare din propunere ar fi acolo, ~27–29 simb/s, ~40 cu golirea la final); CI verde. A treia sesiune la rând fără sarcină → „OPRIT” până la o comandă nouă sau un jurnal nou de test.
- **19 nov 17:45:** nimic nou pentru OS (nicio comandă; centrul de comandă a confirmat ciclul `os-308`: 10,99 simb/s); CI verde. Coada fără tine e goală (regula 5: 2 din 3). Aștept „da”-ul tău la `idei/2026-11-19_kronos-placa-mai-rapid.md` sau altă comandă.
- **19 nov 14:50 — ciclul automat `os-308` a trecut pe placă (14:37, fără tine):** lanțul întreg + #513: 16 simboluri pe placă, toate identice cu procesorul. **Viteza cu driverul: 10,99 simboluri/s** (la `os-307`: 3,10 → de ~3,5 ori mai repede). Placa în sine: 43,8 simb/s (neschimbat). Din ~87 ms pe simbol, ~74 ms sunt scrierea jurnalului pe stick (o dată pe simbol); verificarea pe procesor între simboluri rămâne ~3,9 s (0,25 simb/s cu ea). Nicio schimbare de cod; CI verde. Propunere: `idei/2026-11-19_kronos-placa-mai-rapid.md`.
- **19 nov 14:30 — `os-308` gata (C-146, după primul ciclu automat `os-307`, care a trecut cap-coadă fără tine):** OS-ul folosește codul Cyber-GPU nou (`e74b418`, C-145). La `run kronos --gpu --n 16 Buna ziua`: jurnalul nu mai scrie și sincronizează stick-ul la fiecare rând de rutină (le ține în memorie și le scrie o dată pe simbol — toate rândurile rămân, în aceeași ordine), iar lansările se rescriu în placă doar unde s-au schimbat (verificat la final prin recitire). Raportul ciclului arată acum timpul pe simbol pe bucăți: placă / driver / jurnal / ecran, plus verificarea pe procesor. Comanda și rândurile `kg`/`kv` sunt ca în `os-307`, ca să comparăm cifrele. Testat doar în SIMULARE (suita 111/0/1, CI verde). Așteptat (estimare, nemăsurat): ~20 simboluri/s cu driverul în loc de 3,10.

## Urmează
- P6-99 (verificarea după placă cu motorul rapid → viteza „cu verificare” peste 0,25 simb/s), apoi P6-100 (discul propriu, doar pregătire).
- C-152: P6-102 (comutatorul de pornire, doar cod + QEMU), P6-103 (ceasul de pază), P6-104 (temperatura procesorului); P6-101 (FLR) după nota Cyber-GPU C-151 punctul 3; P6-105 (`gpu stare`) după C-151 punctul 1.

## Ce oferă proiectul celorlalți
- `os-313`: ciclul automat cu rândurile `kp`/`kl`/`kc`/`ks` în gpu-jurnal (cititorul `kronos_perf::parse_journal` al Cyber-GPU le înțelege).
- Agentul din OS, ciclul automat, rapoartele urcate singure în hub.

## De ce are nevoie de la ceilalți
- Cyber-GPU: nota C-151 punctul 3 (pașii FLR) pentru P6-101; tabloul de bord (C-151 punctul 1) pentru P6-105.
- Centrul de comandă: ciclul automat cu `os-313` (ziua) și confirmarea în hub a cifrelor `ks`/`kc` pentru viteza maximă.

## Blocaje / nevoie de Adrian
- Nimic urgent. Testul `os-313` îl pornește centrul de comandă prin ciclul automat, ziua (cheile tale există).
- Comutatorul de pornire (P6-102): când e gata, o singură schimbare a ordinii din BIOS, cu tine de față (ghidat de centrul de comandă).
