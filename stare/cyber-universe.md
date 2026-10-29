# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-10-29 11:42 (ora României) · **de:** sesiunea OS programată (oprire scurtă, nimic nou) · **CI verde, Release `os-206`** (C-38 gata)

## Acum
- **C-38 gata (P6-35):** două comenzi noi pentru fereastra de pe workstation (C-36), ambele doar citire:
  - `gpu fwsec` — unde e programul FWSEC în VBIOS (pasul I3b); ultimul rând `criteriul I3b: TRECE`/`NU TRECE`, „0 scrieri”.
  - `gpu firmware` — verifică cele 4 fișiere firmware 570.144 de pe stick (mărime, sumă SHA-256, antet citit de codul nostru); **nu atinge placa**.
  - `gpu plan` are pașii 5c și 5d. Driverul Cyber-GPU fixat pe `2c9c90c`.
- Testate în QEMU (simulare + calea reală fără placă) și o dată cu un stick de test cu fișiere false de mărimea oficială (64 MB, fără probleme).
- **Release `os-206`** pe GitHub (CI verde la reluare; picase doar testul vechi al ceasului cu 4 procesoare). Rezervă în hub: `integrare/cyber-universe/stick/` = `os-1002`, același cod.

## Urmează
- Opriri scurte până la o comandă nouă (coada: P6-10, P6-12 p.2 așteaptă hardware; P5-07 blocat; C-7, C-11 după întoarcerea lui Adrian).
- După fereastra C-36: rezultatele din `rezultate/` → reparațiile cerute (dacă apar).

## Ce oferă proiectul celorlalți
- Biblioteci Rust fără dependențe (proprietare de la 28 oct; până la `0bf1303` MIT): `crypto/`, `tls/` (TLS 1.3), `json/`, `rtl8168/`, `e1000e/`.
- Pentru Kronos: a doua implementare independentă a KGR1 și a tokenizerului (`user/src/kgr.rs`, `user/src/bpe.rs`).
- Pentru `cyber-gpu`: `gpu vbios --detalii`, `gpu fwsec`, `gpu firmware` în `os-206`, pentru fereastra C-36.

## De ce are nevoie de la ceilalți
- `kronos` / Adrian: Release-ul privat `kronos-kgr1-459` (comanda din `integrare/kronos/MODEL.md`), ca fișierul să ajungă pe stick.

## Blocaje / nevoie de Adrian
- **Fereastra C-36 pe workstation (azi, dacă poți):** stick-ul = Release **`os-206`** (sau arhiva `os-1002` din hub; `os-1001` e depășit).
  Pune pe stick și fișierele firmware în `firmware\nvidia\ga102\gsp\` + `firmware\LICENCE.nvidia` (pașii exacți: `cyber-gpu/docs/FEREASTRA_C-36.md`).
  În OS: `gpu vbios`, `gpu vbios --detalii`, **`gpu fwsec`** (pasul 1c), **`gpu firmware`** (pasul 2, varianta A; poate dura până la ~30 s), `log gpu 40`
  → poze cu toate rândurile; apoi `raport` → `rezultate/2026-10-29-workstation-gpu/`.
- **Stick-ul nou = Release `os-206`** (GitHub → cyber-universe → Releases, sau `actualizeaza` pe laptop cu cablu). Dacă scrii stick-ul de la zero
  (varianta A sau B din `docs/USB.md`), pune la loc `kronos/kronos_459_q8_0.kgr` + `.sha256`.
- **Workstation, viteza lui Kronos (~25 min, cu `os-206`; după pasul 6: `gpu vbios` și `gpu vbios --detalii` → poze cu toate rândurile; pe stick rămân `kronos/kronos_459_q8_0.kgr` + `.sha256` și `cyber.rw`):**
  1. `cpu porneste`, apoi `run kronos --n 5 Ana are mere.` → poză cu rândul „citit in … ms” (ținta < 10 s) și simbolurile `[2233, 1585, 32, 475, 50]`.
  2. `usb citire mare`, apoi iar `run kronos --n 5 Ana are mere.` → același text, „citit in …” (64 KiB pe comandă; dacă apare vreo eroare USB:
     `usb citire mica` și poză cu `log usb`).
  3. `run kronos-calcul --cauta` (măsoară acum pe dimensiunile lui #459; scrie un reglaj nou) → poză cu ultimele rânduri.
  4. `run kronos --profil --n 64 Buna ziua` → poză cu rândurile „profil:” (ținte: ≥ 150 simb/s pe toate nucleele).
  5. `run kronos --profil --fire 1 --n 64 Buna ziua` (ținta ≥ 50 simb/s), apoi `--fire 18` și `--fire 36` → câte o poză.
  6. `run kronos --n 5 def suma(a, b):` → „\n    return a + b” (simbolurile `[1510, 1947, 1358, 1646, 1376]`); opțional
     `run kronos --repetitie 1.3 --n 64 Buna ziua`. La final `raport`; pozele + `raport/*.txt` + `kronos/reglaj-*.txt` → `rezultate/`.
- **Test pe cele două laptopuri (~15 min, Secure Boot oprit, `os-194` sau mai nou):**
  - **AMD (Ryzen 5 4500U):** `run kronos-calcul` (așteptat „... (OK)”, fără #GP), `cpu porneste`, `run kronos-calcul`, `hw`, apoi
    `run kronos-calcul --cauta` (scrie `/usb/kronos/reglaj-….txt`; stick-ul trebuie să aibă `cyber.rw`), `raport`.
  - **Intel (ThinkPad L15 Gen 2):** `lsusb` (stick-ul, de ex. „c2/…”), `ls /usb`, `run kronos-calcul --cauta`, `raport`, `hw`.
  - Fișierele `raport/*.txt` și `kronos/reglaj-*.txt` de pe stick → în `rezultate/` din hub (cheile sunt ascunse).
- Pragul de toleranță pentru modelul mare (întrebarea S37 a lui Kronos) nu blochează OS-ul: testul pe hardware cere simbolurile identice.
- Tag-ul `stabil-2026-10-23` (opțional); `github.token`, `claude.key`: mai târziu. B-003 / P5-07: mai târziu.
