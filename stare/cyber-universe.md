# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-10-28 20:42 (ora României) · **de:** sesiunea OS programată (oprire scurtă) · ultimul Release **`os-197`** (CI oprit de la 14:51; `gpu vbios --detalii` NU e încă pe niciun stick)

## Acum
- **C-31 gata în cod (P6-31):** `gpu vbios --detalii` listează structura VBIOS (imagini, PCIR, NPDE, rupturi, tabela BIT, rezumatul cu
  „criteriul I3”), doar citire, cu „0 scrieri”; rândurile apar și în `raport`. Testat doar în SIMULARE (modelul plăcii cu imaginile „NV” la `0x24600`).
  Cyber-GPU fixat pe `8313973`. Suita de teste locală trece (79/80, al 80-lea instabilul cunoscut, trecut la reluare).
- **B-005 rezolvat pentru sesiuni:** OS-ul se construiește din copia `cyber-gpu` din hub (`integrare/cyber-gpu/snapshot/`), cu `tools/cyber-gpu-local.sh`.
- **CI / Release încă oprite:** GitHub Actions nu pornește (repo privat, minute terminate; run 199 picat în 6 s). Fără Release nu există
  stick nou cu C-29 + C-31 împreună; `os-197` are doar C-29. Nu am plătit nimic.
- C-32 (licența proprietară) gata de la 15:30.

## Urmează
- Coada nu are sarcini libere (hardware / după întoarcerea ta). Opriri scurte până la o comandă nouă sau la răspunsul despre Release.

## Ce oferă proiectul celorlalți
- Biblioteci Rust fără dependențe (proprietare de la 28 oct; până la `0bf1303` MIT): `crypto/`, `tls/` (TLS 1.3), `json/`, `rtl8168/`, `e1000e/`.
- Pentru Kronos: o a doua implementare independentă a KGR1 **și a tokenizerului** (`user/src/kgr.rs`, `user/src/bpe.rs`) — verificare
  încrucișată a specificației; descrierea tokenizerului s-a dovedit completă (nicio întrebare deschisă).
- Pentru `cyber-gpu`: adresa framebuffer-ului în `hw` (C-26).

## De ce are nevoie de la ceilalți
- `kronos` / Adrian: Release-ul privat `kronos-kgr1-459` (comanda din `integrare/kronos/MODEL.md`), ca fișierul să ajungă pe stick.
- `cyber-gpu`: să țină la zi copia din hub (C-34); o ramură `main` sau un tag ar fi mai clar de fixat decât un commit; nu blochează.

## Blocaje / nevoie de Adrian
- **Cum ajunge stick-ul nou la tine (alege una):** (1) repo-urile `cyber-universe` + `cyber-gpu` din nou publice → CI și Release gratuite;
  (2) minute GitHub plătite + un token doar-citire pentru `cyber-gpu` pus ca secret (doar cu „da”-ul tău); (3) construiesc imaginea în sesiune
  și o pun într-un loc privat de unde o descarci (spune unde). Până atunci `gpu vbios --detalii` nu se poate testa pe workstation.
- **Workstation, viteza lui Kronos (~25 min, `os-197` sau stick-ul nou; cu stick-ul nou, după pasul 6: `gpu vbios` și `gpu vbios --detalii` → poze cu toate rândurile; pe stick rămân `kronos/kronos_459_q8_0.kgr` + `.sha256` și `cyber.rw`):**
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
