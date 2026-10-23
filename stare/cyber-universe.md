# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-10-23 20:05 (ora României) · **de:** sesiunea OS programată (19:09) — C-15 gata, Release os-187

## ## Acum
- **C-15 gata.** Repo-ul e public → verificările automate (CI) merg din nou, gratuit. **Release nou: `os-187`** = toată munca din C-14
  (rețeaua I219, SSE/AVX, toate nucleele, memorie mare, fire multiple într-un program).
- CI-ul e mai econom: nu mai rulează când se schimbă doar documente; o rulare nouă o oprește pe cea veche; testul lung de stabilitate
  rulează o dată pe săptămână; uneltele se instalează în 22 de secunde (înainte ~20 de minute).
- Prima rulare a găsit o greșeală într-un test (nu în sistem): pe 4 nuclee testul își amesteca notițele. Reparat; acum verde.
- `actualizeaza` de pe stick **nu mai are nevoie de token** (doar `gh-trimite` îl mai cere). Se confirmă la primul test pe stick.

## Urmează
- Când se întoarce Adrian: listele de mai jos (cu `os-187`), apoi C-7, C-11. Până atunci coada OS-ului nu are nimic de făcut fără hardware.

Ce oferă proiectul celorlalți
- Biblioteci Rust fără dependențe (MIT): `crypto/`, `tls/` (TLS 1.3), `json/`, `rtl8168/`, `e1000e/` (Intel 8254x/82574/I219).
- Pentru `cyber-gpu`: comanda `gpu` (nivel 0, doar citire), pe orice magistrală-rădăcină.
- Pentru Kronos („Kronos în OS pe procesor”): SSE/AVX/AVX2 în programe, fire pe toate nucleele, regiuni de memorie de GiB (`mem_map`), **fire multiple în același program** (`cyber_user::thread`).

## De ce are nevoie de la ceilalți
- Nimic nou.

## Blocaje / nevoie de Adrian
- **Nimic urgent.** Problema cu CI-ul e rezolvată (repo public). Totul de mai jos e pentru când se întoarce (Release-ul de folosit: `os-187` sau mai nou):
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
- `github.token`: nu mai trebuie pentru `actualizeaza` (repo public); doar pentru `gh-trimite`, mai târziu. `claude.key`: încă nu — după ce trece (R). B-003 / P5-07: mai târziu.
