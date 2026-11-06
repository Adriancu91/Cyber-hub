# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-11-06 19:30 (ora României) · **de:** sesiunea OS (pornire manuală 19:26) · Release de testat: **`os-259`** (CI verde; pe placă identic cu `os-251`)

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
- **C-83 → sarcina P6-62:** partea OS (pașii I11–I14 în `gpu lant`, `kronos --gpu` cu întoarcere pe procesor) se face când cyber-gpu publică I11+.
- **C-82 → P6-60:** așteaptă în continuare Release-ul `kronos-kgr1-513`.
- Pe placă nimic schimbat față de `os-251` (lanțul I6–I10 neîncercat de la I8 cu reparația C-75).

## Urmează
- P6-62 imediat ce cyber-gpu publică I11 (copierea mare RAM↔VRAM) și următorii; P6-60 când apare `kronos-kgr1-513`.
- P6-61 rest: imagini + CSS de bază în browser (6b). Duminică seara (8 nov): lista exactă pentru fereastra de luni.

## Ce oferă proiectul celorlalți
- `gpu lant` I6 → I10 pe stick-ul de test, jurnal pe stick; rapoartele pot ajunge acum singure în `rezultate/os-automat/` (cu token).
- `hub` (citire din OS a `COMENZI.md`/`stare/`/`DECIZII.md`), `test tot`, `ora`, git pe ramuri `os/…`, `web` cu formulare.
- Bibliotecile `crypto/`, `tls/`, `json/`, `rtl8168/`, `e1000e/`.

## De ce are nevoie de la ceilalți
- **`kronos`:** Release-ul `kronos-kgr1-513` + secțiunea #513 în `integrare/kronos/MODEL.md` (SHA-256, mărime, 3 texte de control) — pentru P6-60.
- **`cyber-gpu`:** mulțumim pentru I11–I14 (`e681bea`)! **Vă rugăm să reîmprospătați copia din hub** (`integrare/cyber-gpu/snapshot/cyber-gpu.bundle`,
  C-34): acum e tot la `657e209`, iar sesiunea OS nu poate clona repo-ul privat (B-005) → P6-62 nu poate începe până nu apare `e681bea` în copie.

## Blocaje / nevoie de Adrian
- **Tokenul GitHub pe stick (acum chiar folosește):** pe GitHub → Settings → Developer settings → Fine-grained tokens → doar depozitul **`Cyber-hub`**,
  *Contents: Read and write*; salvat ca `github.token` (un rând) în rădăcina stick-ului. Cu el, jurnalele ferestrei ajung singure în hub (nu mai copiezi în Windows).
- **La fereastra următoare pe workstation (luni 9 nov sau mai devreme):** stick-ul de test cu `os-259` (`cyber-universe-gpu-scrie-usb.img`; `os-251` e identic pe placă) + stick-ul cu firmware:
  pornire rece, `gpu firmware`, `gpu pregatire-i6`, `gpu lant` + `DA` o dată, poze la rânduri; apoi `raport` și **`test tot`** (nou, doar citiri).
  Dacă e tokenul pe stick: `trimite` (rapoartele pleacă singure); altfel jurnalele `/usb/raport/*` în `rezultate/<data>-workstation-os259/`.
