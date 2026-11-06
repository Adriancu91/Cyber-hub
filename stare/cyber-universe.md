# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-11-07 00:45 (ora României) · **de:** sesiunea OS programată (23:40) · Release de testat: **`os-259`** (CI verde; pe placă identic cu `os-251`); Release nou **`os-261`** (CI verde) = `os-259` + I11–I13 în lanț (doar SIMULARE); `146b4a2` (+ I14, CI în curs) dă următorul Release

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
- **C-83 → sarcina P6-62, în lucru:** cyber-gpu fixat pe `bc2f22b`. În `gpu lant`, după I10, sunt acum **I11** (copiere 8 MiB RAM → VRAM → RAM,
  verificată bit cu bit, viteza cu ceasul plăcii), **I12** (Q8_0 3072×768 pe placă, comparat cu procesorul) și **I13** (un strat Kronos întreg,
  4 poziții × 16 lansări) și acum **I14**: simboluri întregi cu **modelul de control al lui Kronos** (`mic_q8_0.kgr`, greutăți la întâmplare,
  răspuns cunoscut din `vectori.json`): 3 texte, 29 de simboluri, 36 de lansări și o sonerie pe simbol, identice cu procesorul și cu vectorii
  lui Kronos. Toate trec **doar în SIMULARE**; lanțul trece acum până la capăt. Niciun registru nou pe placă; stick-ul de test are
  `/kronos/mic_q8_0.kgr`. #513 vine după Release-ul lui (P6-60).
- **C-82 → P6-60:** așteaptă în continuare Release-ul `kronos-kgr1-513`.
- Pe placă nimic schimbat față de `os-251` (lanțul I6–I10 neîncercat de la I8 cu reparația C-75).

## Urmează
- P6-62: `kronos --gpu` cu întoarcere pe procesor; I14 cu #513 (zona de comenzi ≥ 16 KiB) când apare `kronos-kgr1-513` (P6-60).
- P6-61 rest: imagini + CSS de bază în browser (6b). Duminică seara (8 nov): lista exactă pentru fereastra de luni.

## Ce oferă proiectul celorlalți
- `gpu lant` I6 → I14 pe stick-ul de test (I11–I14 doar în SIMULARE până acum), jurnal pe stick; rapoartele pot ajunge acum singure în `rezultate/os-automat/` (cu token).
- `hub` (citire din OS a `COMENZI.md`/`stare/`/`DECIZII.md`), `test tot`, `ora`, git pe ramuri `os/…`, `web` cu formulare.
- Bibliotecile `crypto/`, `tls/`, `json/`, `rtl8168/`, `e1000e/`.

## De ce are nevoie de la ceilalți
- **`kronos`:** Release-ul `kronos-kgr1-513` + secțiunea #513 în `integrare/kronos/MODEL.md` (SHA-256, mărime, 3 texte de control) — pentru P6-60.
- **`cyber-gpu`:** mulțumim pentru copia `bc2f22b` — I11–I14 sunt integrate în OS (I14 cu `mic_q8_0.kgr`, cum ați propus). Pentru #513 mărim noi zona de pushbuffer în OS (≥ 16 KiB) — spuneți dacă preferați altfel.

## Blocaje / nevoie de Adrian
- **Tokenul GitHub pe stick (acum chiar folosește):** pe GitHub → Settings → Developer settings → Fine-grained tokens → doar depozitul **`Cyber-hub`**,
  *Contents: Read and write*; salvat ca `github.token` (un rând) în rădăcina stick-ului. Cu el, jurnalele ferestrei ajung singure în hub (nu mai copiezi în Windows).
- **La fereastra următoare pe workstation (luni 9 nov sau mai devreme):** stick-ul de test cu `os-259` (`cyber-universe-gpu-scrie-usb.img`; `os-251` e identic pe placă) + stick-ul cu firmware:
  pornire rece, `gpu firmware`, `gpu pregatire-i6`, `gpu lant` + `DA` o dată, poze la rânduri; apoi `raport` și **`test tot`** (nou, doar citiri).
  Dacă e tokenul pe stick: `trimite` (rapoartele pleacă singure); altfel jurnalele `/usb/raport/*` în `rezultate/<data>-workstation-os259/`.
- 2026-11-06 22:20 — C-83 (P6-62): I11, I12, I13 integrate în `gpu lant`, trec în SIMULARE (I13 verificat și la mărimea plăcii, E 768); lanțul se oprește cinstit la I14. Pe placă nimic nou de încercat până la Release-ul următor.
