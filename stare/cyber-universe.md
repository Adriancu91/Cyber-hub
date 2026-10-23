# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-10-23 18:25 (ora României) · **de:** sesiunea OS programată (17:40) — C-14 gata: K6-04

## ## Acum
- **C-14 e gata (toți pașii 1–5).** Azi, în ordine: rețeaua I219 (os-174), SSE/AVX (os-175), celelalte nuclee pornite (os-177),
  firele pe toate nucleele (K6-02b), memorie mare `mem_map` (K6-03) și acum **K6-04: un program poate avea mai multe fire**
  care lucrează în aceeași memorie, pe toate nucleele. Test: `/bin/fire` — 4 fire adună împreună 64 MiB, suma iese exactă; dacă un fir
  greșește sau cere ieșirea, se oprește tot programul curat; un program cu 4 fire în buclă e oprit cu `kill`; memoria revine exact.
- 70 de scenarii automate trecute local (+1 sărit fără internet). **CI-ul GitHub tot nu pornește** → K6-02b, K6-03, K6-04 sunt pe GitHub
  (cod testat local) dar **fără Release** (ultimul: `os-177`).
- Coada OS-ului nu mai are nimic de făcut fără Adrian: restul așteaptă testele pe hardware sau decizii.

## Urmează
- Când revine CI: Release cu K6-02b..K6-04. Când se întoarce Adrian: listele de mai jos, apoi C-7, C-11.

Ce oferă proiectul celorlalți
- Biblioteci Rust fără dependențe (MIT): `crypto/`, `tls/` (TLS 1.3), `json/`, `rtl8168/`, `e1000e/` (Intel 8254x/82574/I219).
- Pentru `cyber-gpu`: comanda `gpu` (nivel 0, doar citire), pe orice magistrală-rădăcină.
- Pentru Kronos („Kronos în OS pe procesor”): SSE/AVX/AVX2 în programe, fire pe toate nucleele, regiuni de memorie de GiB (`mem_map`), **fire multiple în același program** (`cyber_user::thread`).

## De ce are nevoie de la ceilalți
- Nimic nou.

## Blocaje / nevoie de Adrian
- **Singurul lucru care poate fi făcut de pe telefon (2 minute): GitHub nu mai rulează verificările automate (CI) nici la OS**, din 14:03
  ora României — aceeași cauză ca la Cyber-GPU (probabil s-au terminat minutele gratuite GitHub Actions ale contului): GitHub →
  Settings → Billing and plans → Actions. Până atunci nu ies Release-uri noi (ultimul: `os-177`); codul e testat local și e pe GitHub.
- Restul — când se întoarce, nimic urgent:
- **Fereastra a doua pe workstation** (cel mai nou Release, ~30 min, Kronos oprit; Secure Boot oprit, apoi repus pe Enabled):
  stick din Release → F12 → **Esc** → `cyber>`, câte o poză după: `lspci` (trebuie să apară `10de:2482` la `b3:00.0`), `gpu identifica`,
  `gpu plan`, `log gpu 40`, `log pci 40`, `hw`, `lsusb` (stick-ul ADATA ca `port X.Y`), `log usb 60`,
  **nou:** `net` și `log e1000 40` (placa I219; cu cablul în router, după ~30 s `net` ar trebui să arate o adresă), `cpu`, apoi
  `cpu porneste` (câte nuclee pornesc din 36; acum ele chiar rulează fire), apoi `cpu`, la final `reboot` (trebuie să repornească; dacă nu, poză). Nimic nu scrie în placa video.
- **Testul 8 pe laptop** (cel mai nou Release; rețeaua Realtek e neschimbată față de os-155), cablul la laptopul cu Windows (ICS pornit):
  **(C) La cald — F12 → stick:** **Esc** → `cyber>`, nicio comandă `rtl`. 1. ~30 s → `net` → poză. 2. `log rtl 20` → poză.
  3. Cu adresă: `fetch https://example.com/` → poză; fără adresă: `log rx` → poză, apoi `rtl porneste pagini` → ~30 s → `net` → poză.
  **(R) La rece — pornit direct de pe stick:** **Esc** → `cyber>`. 4. `net` → poză. 5. `rtl porneste rece` → ~30 s → `net` → poză; `log rtl 60` → poză.
  În plus: `lspci`, `lsusb`, `cpu porneste` → poză, `reboot` (trebuie să repornească).
- `github.token` / `claude.key`: încă nu — după ce trece (R). B-003 / P5-07: mai târziu.
