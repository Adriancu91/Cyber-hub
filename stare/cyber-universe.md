# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-10-28 15:30 (ora României) · **de:** sesiunea OS programată · ultimul Release **`os-197`** (CI oprit de la 14:51)

## Acum
- **C-32 gata (P6-30):** licența e proprietară de la commit-ul de după `0bf1303` („toate drepturile rezervate”); versiunile până la
  `0bf1303` rămân MIT (notat în `LICENSE`). Decizia D-015 o înlocuiește pe cea veche cu MIT; CLAUDE.md, README-urile și regulile
  clean-room actualizate; firmware-ul NVIDIA nu-l distribuim niciodată (îl descarci tu).
- **C-31 BLOCAT (B-005):** de când `cyber-gpu` e privat, sesiunea OS nu-l mai poate citi. OS-ul folosește bibliotecile lui, deci acum
  **nu se poate construi și testa nimic** din OS (nici C-31, nici altă sarcină de cod).
- **CI oprit:** de când repo-ul e privat, GitHub Actions nu mai pornește („spending limit”), ca pe 23 oct. Nu am plătit nimic.
  Fără CI nu apar Release-uri noi pentru stick; `os-197` (cu C-29) rămâne cel de testat.

## Urmează
- După răspunsul tău la B-005: C-31 (`gpu vbios --detalii`) + Release pentru fereastra de pe workstation. Până atunci, opriri scurte.

## Ce oferă proiectul celorlalți
- Biblioteci Rust fără dependențe (proprietare de la 28 oct; până la `0bf1303` MIT): `crypto/`, `tls/` (TLS 1.3), `json/`, `rtl8168/`, `e1000e/`.
- Pentru Kronos: o a doua implementare independentă a KGR1 **și a tokenizerului** (`user/src/kgr.rs`, `user/src/bpe.rs`) — verificare
  încrucișată a specificației; descrierea tokenizerului s-a dovedit completă (nicio întrebare deschisă).
- Pentru `cyber-gpu`: adresa framebuffer-ului în `hw` (C-26).

## De ce are nevoie de la ceilalți
- `kronos` / Adrian: Release-ul privat `kronos-kgr1-459` (comanda din `integrare/kronos/MODEL.md`), ca fișierul să ajungă pe stick.
- `cyber-gpu`: o ramură `main` sau un tag ar fi mai clar de fixat decât `dac2e32`; nu blochează.

## Blocaje / nevoie de Adrian
- **B-005 — alege una (2 minute):** (a) adaugă repo-ul `cyber-gpu` la sarcina programată a OS-ului (depozitele sesiunii, în aplicația
  Claude); pentru CI ar trebui și un token doar-citire pus ca secret; (b) „da” ca bibliotecile Cyber-GPU să fie copiate direct în repo-ul
  OS-ului (același autor, aceeași licență); (c) `cyber-gpu` din nou public. Fără una din ele OS-ul nu se mai poate construi în sesiuni.
- **CI / Release-uri:** repo privat = GitHub Actions oprit (minute terminate). Decizia ta (public, plată, sau Release-uri făcute din sesiune).
- **Workstation, viteza lui Kronos (~25 min, `os-197`; pe stick rămân `kronos/kronos_459_q8_0.kgr` + `.sha256` și `cyber.rw`):**
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
