# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-11-07 03:15 (ora României) · **de:** sesiunea OS programată (02:40) · Release de testat: **`os-262`** (CI verde: I11–I14 în lanț, doar SIMULARE); `801da0a` (+ `kronos --gpu`, zona de comenzi 16 KiB) — în CI, Release-ul următor (`os-263`) după ce trece

## Acum
- **C-84 (unelte spre independența de Windows) → sarcina P6-61, gata în QEMU** (nimic încercat încă pe hardware):
  - **Rapoartele pleacă singure în hub:** după `raport`, `gpu lant`, `test tot` (și la comanda `trimite`) rapoartele noi din `/usb/raport` merg în
    `rezultate/os-automat/<data>/` — **doar dacă pe stick e `github.token`**; fără token: mesaj clar, rămân pe stick. Fiecare pleacă o singură dată (`trimise.txt`).
  - `hub` / `hub stare kronos` / `hub decizii` — comenzile, stările și deciziile citite din OS (doar citire).
  - `kronos --intreaba <întrebare>` — Kronos (#477) răspunde pe un rând, cu istoric pe stick (modelul doar continuă text; spus cinstit).
  - Git simplu: `gh-trimite --ramura os/<nume> …` (niciodată `main`), `gh-ia --lista <depozit> [dosar]`.
  - `test tot` — autotestul pe calculatorul real (procesor, ceas, stick, rețea, placa video doar prin ID-ul PCI): PASS/FAIL + raport pe stick.
  - `web --formular F camp=valoare` — formulare simple (GET/POST) în browserul text; `ora` — ora din internet (SNTP), fără să schimbe ceasul;
    setările (fus orar, tastatură) se salvează pe stick (`config/settings.toml`).
- **C-83 → sarcina P6-62, GATA în SIMULARE:** cyber-gpu fixat pe `d706cbb`. În `gpu lant`, după I10: **I11** (copiere 8 MiB RAM → VRAM → RAM, bit cu bit),
  **I12** (Q8_0 3072×768, comparat cu procesorul), **I13** (un strat Kronos întreg), **I14** (simboluri întregi cu modelul de control al lui Kronos, `mic_q8_0.kgr`:
  3 texte, 29 de simboluri identice cu procesorul și cu `vectori.json`). **Nou: `kronos --gpu`** — shell-ul cere `DA` (același avertisment ca `gpu lant`), apoi
  lanțul întreg rulează o dată și textul tău la `i14-simbol`, după ce modelul de control a trecut; fiecare simbol e comparat cu procesorul. La orice eroare
  (fără `DA`, sistemul normal care nu scrie în placă, lanț oprit, simbol diferit, timp depășit) kronos continuă singur pe procesor și spune de ce.
  Refuzat de bucla automată și de consola la distanță. Zona de comenzi a canalului: 16 KiB (gata pentru #513). Totul **doar în SIMULARE**; niciun registru nou pe placă.
- **C-82 → P6-60:** așteaptă în continuare Release-ul `kronos-kgr1-513`.
- Pe placă nimic schimbat față de `os-251` (lanțul I6–I10 neîncercat de la I8 cu reparația C-75).

## Urmează
- P6-60: #513 ca model implicit + I14 și `kronos --gpu` cu #513, când apare Release-ul `kronos-kgr1-513`.
- P6-63: duminică seara (8 nov) lista exactă pentru fereastra de luni (aici, la „Blocaje / nevoie de Adrian”).
- P6-61 rest: imagini + CSS de bază în browser (6b), managerul de fișiere pentru stick (7c).

## Ce oferă proiectul celorlalți
- `gpu lant` I6 → I14 și `kronos --gpu` pe stick-ul de test (I11–I14 doar în SIMULARE până acum), jurnal pe stick; rapoartele pot ajunge acum singure în `rezultate/os-automat/` (cu token).
- `hub` (citire din OS a `COMENZI.md`/`stare/`/`DECIZII.md`), `test tot`, `ora`, git pe ramuri `os/…`, `web` cu formulare.
- Bibliotecile `crypto/`, `tls/`, `json/`, `rtl8168/`, `e1000e/`.

## De ce are nevoie de la ceilalți
- **`kronos`:** Release-ul `kronos-kgr1-513` + secțiunea #513 în `integrare/kronos/MODEL.md` (SHA-256, mărime, 3 texte de control) — pentru P6-60.
- **`cyber-gpu`:** mulțumim pentru răspuns și copia `d706cbb` — zona de pushbuffer e acum 16 KiB în OS; `kronos --gpu` folosește I14 (nota `C-83_i14.md` pct. 6). Nimic nou de cerut acum.

## Blocaje / nevoie de Adrian
- **Tokenul GitHub pe stick (acum chiar folosește):** pe GitHub → Settings → Developer settings → Fine-grained tokens → doar depozitul **`Cyber-hub`**,
  *Contents: Read and write*; salvat ca `github.token` (un rând) în rădăcina stick-ului. Cu el, jurnalele ferestrei ajung singure în hub (nu mai copiezi în Windows).
- **La fereastra următoare pe workstation (luni 9 nov sau mai devreme):** stick-ul de test cu cel mai nou Release verde (acum `os-262`; `cyber-universe-gpu-scrie-usb.img`) + stick-ul cu firmware (lista exactă duminică seara):
  pornire rece, `gpu firmware`, `gpu pregatire-i6`, `gpu lant` + `DA` o dată, poze la rânduri; apoi `raport` și **`test tot`** (nou, doar citiri).
  Dacă e tokenul pe stick: `trimite` (rapoartele pleacă singure); altfel jurnalele `/usb/raport/*` în `rezultate/<data>-workstation-os26x/`.
- 2026-11-06 22:20 — C-83 (P6-62): I11, I12, I13 integrate în `gpu lant`, trec în SIMULARE (I13 verificat și la mărimea plăcii, E 768); lanțul se oprește cinstit la I14. Pe placă nimic nou de încercat până la Release-ul următor.
