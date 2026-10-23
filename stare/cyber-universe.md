# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-10-23 16:10 (ora României) · **de:** sesiunea OS programată (14:40) — C-14: K6-02b, K6-03

## Acum
- **K6-02b: firele rulează pe toate nucleele procesorului** (după `cpu porneste`; pornirea obișnuită rămâne pe un nucleu). Fiecare nucleu
  are datele lui, încuietorile opresc întreruperile, nicio „trezire” nu se mai pierde între nuclee, iar paginile scoase din memoria nucleului
  sunt șterse și din memoria rapidă (TLB) a celorlalte nuclee. Test în QEMU pe 4 nuclee: firele merg pe toate 4, 8 programe în paralel,
  tot testul obișnuit al sistemului și testul de stres trec și pe 4 nuclee.
- **K6-03: memorie mare pentru programe.** Apeluri noi `mem_map` / `mem_unmap`: un program cere, de exemplu, 1 GiB și îl primește în pagini
  de 2 MiB (mai rapide), plin de zero; la eliberare memoria revine exact. Test: `/bin/memorie` alocă 1 GiB, scrie, verifică, eliberează.
- 68 de scenarii automate trecute local (+1 sărit fără internet). **CI-ul GitHub nu mai pornește** (vezi Blocaje) → fără Release nou.

## Urmează
- K6-04 (opțional): fire multiple într-un proces. Apoi, când se întoarce Adrian: listele de mai jos, C-7, C-11.

## Ce oferă proiectul celorlalți
- Biblioteci Rust fără dependențe (MIT): `crypto/`, `tls/` (TLS 1.3), `json/`, `rtl8168/`, `e1000e/` (Intel 8254x/82574/I219).
- Pentru `cyber-gpu`: comanda `gpu` (nivel 0, doar citire), pe orice magistrală-rădăcină.
- Pentru Kronos („Kronos în OS pe procesor”): SSE/AVX/AVX2 în programe, **fire pe toate nucleele**, **regiuni de memorie de GiB** (`mem_map`).

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
