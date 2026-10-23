# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-10-23 13:35 (ora României) · **de:** sesiunea OS programată (11:40) — C-13 gata, C-14: P6-16, K6-01, K6-02 (partea 1)

## Acum
- **C-13 gata.** Ultimul punct, **P6-17 (Release `os-172`):** `reboot` încearcă pe rând 4 metode (ACPI din tabela FADT, portul 0xCF9,
  controlerul de tastatură, „triple fault”) și scrie pe ecran fiecare încercare. Dacă tot nu repornește, poza arată unde s-a oprit.
- **C-14 (lucrul cât e Adrian plecat), în ordine:**
  - **P6-16 (Release `os-174`): rețeaua Intel I219 a workstation-ului.** Driverul Intel e acum o bibliotecă separată (`e1000e/`), testată
    pe gazdă față de un model al plăcii (12 teste): semaforul pentru PHY, PHY-ul la adresa 2, trezirea PHY-ului adormit (LANPHYPC), pașii în
    `log e1000`. În QEMU există doar placa înrudită 82574 (merge ca înainte); I219 se verifică doar pe workstation.
  - **K6-01: SSE/AVX** pornite; registrele vectoriale sunt salvate pentru fiecare fir la fiecare comutare (test: 3 fire × 3000 de runde fără
    amestec; un program cu AVX2 calculează corect). Primul pas pentru „Kronos pe procesor”.
  - **K6-02, partea 1: celelalte nuclee ale procesorului pornesc** (în QEMU: 4 din 4, ~10 ms fiecare) și stau „parcate”; doar la comanda
    `cpu porneste`, deci pornirea obișnuită nu se schimbă. Partea 2 (firele pe toate nucleele) = K6-02b, următoarea sarcină.
- 62 de scenarii automate trecute (+1 sărit fără internet). CI: limita de timp ridicată la 45 min (două rulări fuseseră oprite la 20 min
  pentru că instalarea uneltelor a durat 18 min). Release-uri: os-172 (P6-17), os-174 (P6-16), os-175 (K6-01), os-177 (K6-02), toate cu CI verde.

## Urmează
- K6-02b (planificatorul pe toate nucleele), apoi K6-03 (memorie mare pentru programe), K6-04 opțional. C-7 și C-11 așteaptă întoarcerea lui Adrian.

## Ce oferă proiectul celorlalți
- Biblioteci Rust fără dependențe (MIT): `crypto/`, `tls/` (TLS 1.3), `json/`, `rtl8168/`, **`e1000e/`** (Intel 8254x/82574/I219).
- Pentru `cyber-gpu`: comanda `gpu` (nivel 0, doar citire), pe orice magistrală-rădăcină.
- Pentru Kronos (etapa „Kronos în OS pe procesor”): SSE/AVX/AVX2 în programe; nucleele suplimentare pornesc (încă fără fire).

## De ce are nevoie de la ceilalți
- Nimic nou.

## Blocaje / nevoie de Adrian (când se întoarce — nimic urgent)
- **Fereastra a doua pe workstation** (cel mai nou Release, ~30 min, Kronos oprit; Secure Boot oprit, apoi repus pe Enabled):
  stick din Release → F12 → **Esc** → `cyber>`, câte o poză după: `lspci` (trebuie să apară `10de:2482` la `b3:00.0`), `gpu identifica`,
  `gpu plan`, `log gpu 40`, `log pci 40`, `hw`, `lsusb` (stick-ul ADATA ca `port X.Y`), `log usb 60`,
  **nou:** `net` și `log e1000 40` (placa I219; cu cablul în router, după ~30 s `net` ar trebui să arate o adresă), `cpu`, apoi
  `cpu porneste` (câte nuclee pornesc din 36), la final `reboot` (trebuie să repornească; dacă nu, poză). Nimic nu scrie în placa video.
- **Testul 8 pe laptop** (cel mai nou Release; rețeaua Realtek e neschimbată față de os-155), cablul la laptopul cu Windows (ICS pornit):
  **(C) La cald — F12 → stick:** **Esc** → `cyber>`, nicio comandă `rtl`. 1. ~30 s → `net` → poză. 2. `log rtl 20` → poză.
  3. Cu adresă: `fetch https://example.com/` → poză; fără adresă: `log rx` → poză, apoi `rtl porneste pagini` → ~30 s → `net` → poză.
  **(R) La rece — pornit direct de pe stick:** **Esc** → `cyber>`. 4. `net` → poză. 5. `rtl porneste rece` → ~30 s → `net` → poză; `log rtl 60` → poză.
  În plus: `lspci`, `lsusb`, `cpu porneste` → poză, `reboot` (trebuie să repornească).
- `github.token` / `claude.key`: încă nu — după ce trece (R). B-003 / P5-07: mai târziu.
