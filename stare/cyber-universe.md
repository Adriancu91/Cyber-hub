# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-10-28 23:20 (ora României) · **de:** sesiunea OS programată · stick nou **`os-1001`** în hub (`integrare/cyber-universe/stick/`), construit în sesiune

## Acum
- **C-35 gata (P6-32):** stick-ul `os-1001` (commit `02f2043`, 6,9 MB, fără model Kronos și fără firmware NVIDIA) e în hub, cu
  `VERSIUNE.txt` (suma SHA-256) și `README.md`. Are tot: C-29 (viteza lui Kronos) + C-31 (`gpu vbios --detalii`) + C-32.
  Testat înainte: suita QEMU (78/80 + 2 trecute la reluare, instabilul cunoscut al ceasului), arhiva verificată și pornită în QEMU până la desktop.
- GitHub Actions e oprit de centrul de comandă (decizia 23:10) — nu-l repornesc; testele rulează în sesiune, stick-urile vin prin hub.
- `actualizeaza` de pe stick caută tot Release-urile GitHub, deci nu vede `os-1001`: stick-ul se scrie de mână (pașii din `docs/USB.md`).

## Urmează
- La fiecare schimbare care ajunge pe stick: suita QEMU + arhivă nouă în hub (doar ultima). Altfel opriri scurte până la o comandă nouă.
- Propunerea `idei/2026-10-28_cyber-universe_gpu-firmware-fwsec.md` (`gpu fwsec` + `gpu firmware`, doar citire, pentru fereastra C-36): pot s-o fac în ~1 oră + stick nou, **doar dacă o aprobi** (o comandă în `COMENZI.md`).

## Ce oferă proiectul celorlalți
- Biblioteci Rust fără dependențe (proprietare de la 28 oct; până la `0bf1303` MIT): `crypto/`, `tls/` (TLS 1.3), `json/`, `rtl8168/`, `e1000e/`.
- Pentru Kronos: o a doua implementare independentă a KGR1 și a tokenizerului (`user/src/kgr.rs`, `user/src/bpe.rs`).
- Pentru `cyber-gpu`: adresa framebuffer-ului în `hw` (C-26); `gpu vbios --detalii` pe stick pentru fereastra de pe workstation.

## De ce are nevoie de la ceilalți
- `kronos` / Adrian: Release-ul privat `kronos-kgr1-459` (comanda din `integrare/kronos/MODEL.md`), ca fișierul să ajungă pe stick.
- `cyber-gpu`: să țină la zi copia din hub (C-34); nu blochează.

## Blocaje / nevoie de Adrian
- **Stick-ul nou `os-1001`** e în hub (`integrare/cyber-universe/stick/`); centrul de comandă ți-l trimite. Scrie-l pe stick (varianta A sau B din
  `docs/USB.md`) și pune la loc `kronos/kronos_459_q8_0.kgr` + `.sha256`.
- **Workstation, viteza lui Kronos (~25 min, cu `os-1001`; după pasul 6: `gpu vbios` și `gpu vbios --detalii` → poze cu toate rândurile; pe stick rămân `kronos/kronos_459_q8_0.kgr` + `.sha256` și `cyber.rw`):**
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
