# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-10-29 02:35 (ora României) · **de:** sesiunea OS programată · **CI verde, Release `os-205`** (C-37 gata)

## Acum
- **C-37 gata (P6-34):** cheia `CYBER_GPU_TOKEN` merge. Cauza era cea bănuită: `actions/checkout` lăsa în urmă tokenul lui GitHub, trimis
  în locul cheii. Reparat (`persist-credentials: false` + verificare fără antetul rămas), confirmat local și în CI.
- **`phase4` (testul cu mouse-ul în „Module”, „instabilul” din ultimele zile) — cauza găsită:** ordinea pachetelor pe discul de test depindea
  de mașina CI. Aplicația Module le sortează acum alfabetic; reprodus și reparat local.
- **Run 205 verde la prima încercare → Release `os-205`** (primul după `os-197`): C-29 (viteza lui Kronos), C-31 (`gpu vbios --detalii`), C-32 și
  reparațiile de mai sus. Stick-ul se poate actualiza din nou cu `actualizeaza` sau din Release (`docs/USB.md`). `os-1001` din hub e depășit.

## Urmează
- Opriri scurte până la o comandă nouă (coada: P6-10, P6-12 p.2 așteaptă hardware; P5-07 blocat; C-7, C-11 după întoarcerea lui Adrian).
- Propunerea `idei/2026-10-28_cyber-universe_gpu-firmware-fwsec.md` (`gpu fwsec` + `gpu firmware`, doar citire, pentru fereastra C-36): ~1 oră,
  **doar dacă e aprobată** (o comandă în `COMENZI.md`).

## Ce oferă proiectul celorlalți
- Biblioteci Rust fără dependențe (proprietare de la 28 oct; până la `0bf1303` MIT): `crypto/`, `tls/` (TLS 1.3), `json/`, `rtl8168/`, `e1000e/`.
- Pentru Kronos: a doua implementare independentă a KGR1 și a tokenizerului (`user/src/kgr.rs`, `user/src/bpe.rs`).
- Pentru `cyber-gpu`: `gpu vbios --detalii` în `os-205`, pentru fereastra de pe workstation.

## De ce are nevoie de la ceilalți
- `kronos` / Adrian: Release-ul privat `kronos-kgr1-459` (comanda din `integrare/kronos/MODEL.md`), ca fișierul să ajungă pe stick.

## Blocaje / nevoie de Adrian
- **Stick-ul nou = Release `os-205`** (GitHub → cyber-universe → Releases, sau `actualizeaza` pe laptop cu cablu). Dacă scrii stick-ul de la zero
  (varianta A sau B din `docs/USB.md`), pune la loc `kronos/kronos_459_q8_0.kgr` + `.sha256`.
- **Workstation, viteza lui Kronos (~25 min, cu `os-205`; după pasul 6: `gpu vbios` și `gpu vbios --detalii` → poze cu toate rândurile; pe stick rămân `kronos/kronos_459_q8_0.kgr` + `.sha256` și `cyber.rw`):**
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
