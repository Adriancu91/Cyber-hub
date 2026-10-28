# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-10-28 14:35 (ora României) · **de:** sesiunea OS programată · ultimul Release **`os-197`** (CI verde)

## Acum
- **C-29 gata (P6-29): de ce era Kronos lent în OS și ce s-a schimbat.** Am găsit patru cauze în cod:
  1. Programele OS-ului făceau calculele cu virgulă **emulat în software** (fără unitatea de calcul a procesorului) — tot ce nu era produs
     matrice-vector (atenția, LayerNorm, GELU) mergea de zeci de ori mai încet. Acum folosesc procesorul (SSE2), cu aceleași rezultate.
  2. La fiecare produs (49 pe simbol) se porneau și se opreau fire noi — de aceea 36 de fire erau mai lente decât unul. Acum firele pornesc o
     dată și așteaptă fără somn; atenția se împarte și ea pe fire.
  3. Citirea de pe stick parcurgea fișierul de la început la fiecare bucată de 64 KiB → ~31 s. Acum continuă de unde a rămas.
  4. Derularea textului pe ecran citea memoria plăcii video (lentă) și intra în timpul măsurat. Acum ecranul are o copie în memorie.
- **Nou:** `kronos --profil` (unde se duce timpul fiecărui simbol), `kronos --repetitie 1.3` (opțional, contra repetițiilor), `kronos-calcul --cauta`
  măsoară pe dimensiunile modelului de pe stick; `usb citire mare` = citire de 64 KiB pe comandă (variantă nouă, **implicit oprită**, regula
  „o schimbare pe Release” la drivere).
- Suita locală și CI trec (CI verde după o reluare a testului instabil `phase4`); vectorii oficiali Kronos identici.
- Reparată și o blocare rară a nucleului la pornire (un mesaj de eroare scris pe ecran în timp ce alt fir derula textul).

## Urmează
- C-31 (`gpu vbios --detalii`) după ce Cyber-GPU termină C-30. Testul pe workstation de mai jos. Restul cozii așteaptă hardware.

## Ce oferă proiectul celorlalți
- Biblioteci Rust fără dependențe (MIT): `crypto/`, `tls/` (TLS 1.3), `json/`, `rtl8168/`, `e1000e/`.
- Pentru Kronos: o a doua implementare independentă a KGR1 **și a tokenizerului** (`user/src/kgr.rs`, `user/src/bpe.rs`) — verificare
  încrucișată a specificației; descrierea tokenizerului s-a dovedit completă (nicio întrebare deschisă).
- Pentru `cyber-gpu`: adresa framebuffer-ului în `hw` (C-26).

## De ce are nevoie de la ceilalți
- `kronos` / Adrian: Release-ul privat `kronos-kgr1-459` (comanda din `integrare/kronos/MODEL.md`), ca fișierul să ajungă pe stick.
- `cyber-gpu`: o ramură `main` sau un tag ar fi mai clar de fixat decât `dac2e32`; nu blochează.

## Blocaje / nevoie de Adrian
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
