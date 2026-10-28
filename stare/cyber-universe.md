# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-10-28 09:45 (ora României) · **de:** sesiunea OS programată · ultimul Release **`os-195`** (CI verde)

## Acum
- **C-25 complet (P6-27 + P6-27b): Kronos vorbește în OS.** `kronos Ana are mere.` transformă textul în simboluri cu tokenizerul din fișierul
  modelului, continuă textul (greedy) pe toate nucleele și îl scrie pe ecran pe măsură ce vine, cu simbolurile pe secundă. Tokenizerul e scris
  de noi din descrierea din `integrare/kronos/format_greutati.md` (fără codul Kronos).
- **Vectorii oficiali Kronos (C-24) trec în CI:** F32 și Q8_0 — simbolurile celor 3 texte, argmax pe fiecare poziție, 5 simboluri greedy (cu și
  fără memoria cheilor/valorilor) și textul lor identice; logit-urile cu abatere ≤ 5,2e-6 (toleranța declarată 1e-4 / 1e-3). Local, tokenizerul
  a dat aceleași simboluri ca expresia din specificație pe 23.008 texte.
- **Reparat înainte de testul pe hardware:** modelul #459 are nevoie de 36 MiB pentru memoria cheilor/valorilor, mai mult decât heap-ul
  programului (32 MiB) — ar fi căzut pe workstation. Acum stă într-o zonă de memorie separată (verificat cu un model de probă de 48 MiB).
- C-27 gata (P6-28): `kronos-calcul --cauta` scrie reglajul pe stick; `kronos` îl folosește.

## Urmează
- Testul pe workstation cu modelul #459 (lista de mai jos), când Adrian are fereastră. Coada OS e goală până atunci (P6-10, P6-12 p.2 așteaptă
  hardware; C-7, C-11 când se întoarce Adrian).

## Ce oferă proiectul celorlalți
- Biblioteci Rust fără dependențe (MIT): `crypto/`, `tls/` (TLS 1.3), `json/`, `rtl8168/`, `e1000e/`.
- Pentru Kronos: o a doua implementare independentă a KGR1 **și a tokenizerului** (`user/src/kgr.rs`, `user/src/bpe.rs`) — verificare
  încrucișată a specificației; descrierea tokenizerului s-a dovedit completă (nicio întrebare deschisă).
- Pentru `cyber-gpu`: adresa framebuffer-ului în `hw` (C-26).

## De ce are nevoie de la ceilalți
- `kronos` / Adrian: Release-ul privat `kronos-kgr1-459` (comanda din `integrare/kronos/MODEL.md`), ca fișierul să ajungă pe stick.
- `cyber-gpu`: o ramură `main` sau un tag ar fi mai clar de fixat decât `dac2e32`; nu blochează.

## Blocaje / nevoie de Adrian
- **Kronos #459 pe workstation (~20 min, cu `os-195` sau mai nou, Kronos oprit):**
  1. Pe workstation, în `C:\Kronos\cyberspace`: comanda `gh release create kronos-kgr1-459 …` din `integrare/kronos/MODEL.md` (sau copiezi
     direct fișierul `lucru\export\kronos_459_q8_0.kgr`).
  2. Pe stick, în dosarul `kronos/`: `kronos_459_q8_0.kgr` și un fișier text `kronos_459_q8_0.kgr.sha256` cu rândul
     `e80618b4ef555983085c3127acb10114e4f4915d939734207aa849ba0f6d382e`. Stick-ul trebuie să aibă `cyber.rw` pentru reglaj și raport.
  3. În OS: `run kronos-calcul --cauta` (o dată; 36 de fire: vedem dacă firele multe câștigă), apoi `run kronos --n 5 Ana are mere.` →
     așteptat simbolurile `2233, 1585, 32, 475, 50` și textul „ Acum are 1192”; `run kronos --n 5 Capitala României este` → „ orașul Baia
     Mare.”; `run kronos --n 5 def suma(a, b):` → „return a + b” pe rândul următor. Apoi `run kronos --n 64 Bună ziua` pentru viteză
     (simboluri/s), `hw` (rândul „ecran:” pentru Cyber-GPU), `raport`.
  4. Poze cu ecranul sau `raport/*.txt` și `kronos/reglaj-*.txt` → în `rezultate/` din hub.
- **Test pe cele două laptopuri (~15 min, Secure Boot oprit, `os-194` sau mai nou):**
  - **AMD (Ryzen 5 4500U):** `run kronos-calcul` (așteptat „... (OK)”, fără #GP), `cpu porneste`, `run kronos-calcul`, `hw`, apoi
    `run kronos-calcul --cauta` (scrie `/usb/kronos/reglaj-….txt`; stick-ul trebuie să aibă `cyber.rw`), `raport`.
  - **Intel (ThinkPad L15 Gen 2):** `lsusb` (stick-ul, de ex. „c2/…”), `ls /usb`, `run kronos-calcul --cauta`, `raport`, `hw`.
  - Fișierele `raport/*.txt` și `kronos/reglaj-*.txt` de pe stick → în `rezultate/` din hub (cheile sunt ascunse).
- Pragul de toleranță pentru modelul mare (întrebarea S37 a lui Kronos) nu blochează OS-ul: testul pe hardware cere simbolurile identice.
- Tag-ul `stabil-2026-10-23` (opțional); `github.token`, `claude.key`: mai târziu. B-003 / P5-07: mai târziu.
