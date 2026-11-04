# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-11-05 00:55 (ora României) · **de:** sesiunea OS programată (23:00) · **C-68 preluat:** F1 anulat de Adrian, **F3 gata (P6-50)**, F9 pas 1 (P6-52)

## Acum
- **F1 (mașina virtuală) anulat** de Adrian la 23:10: era gata (discul VM pornea în QEMU ca stick, cu rețea) și a fost scos curat din repo și din CI.
- **F3 gata (P6-50) — actualizare de sine cu revenire:** `actualizeaza` păstrează versiunea de acum în `boot/vechi/`; prima pornire a versiunii noi e o
  **încercare**, confirmată după ce ajunge la desktop/shell și merge 60 s; dacă nu se confirmă, la pornirea următoare sistemul **pune singur la loc versiunea veche**
  și repornește. `actualizare-automata` (fișier gol pe stick) = se actualizează singur la pornire. Raport la fiecare confirmare / revenire pe stick
  (`raport/actualizare-*.txt`), trimis în hub doar dacă e `github.token` pe stick. Testat în QEMU (scenariile `revenire`, `update`) și cu nucleul normal.
  Limita, spusă cinstit: un nucleu care pică înainte să citească stick-ul nu revine singur (fișierele vechi rămân în `boot/vechi/`). Detalii: `docs/ACTUALIZARE.md`.
- **F9 pas 1 (P6-52):** comanda `compara <f1> <f2>` arată rândurile diferite între două rapoarte (pe lista albă).
- **Lucru în paralel** (alte sesiuni, fișierele lor de stare `cyber-universe-F2.md`, `cyber-universe-F4.md`): F4 (`hw lista`) e în `main`; F2 (remote) se integrează
  acum; browserul text `/bin/web` (P6-53) e în `main`. Am reparat CI-ul roșu apărut după `/bin/web` (meniul are acum 22 de programe).
- CI pentru `main` cu toate acestea: în curs (rulările se tot repornesc la fiecare push al sesiunilor paralele); testele mele locale trec. Ultimul Release: `os-224`.

## Urmează
- F8/F9 restul (editor / terminal / git simplu în OS) după ce F2 intră în `main`.
- Release nou când CI e verde (cu F3, F4, F6a și, după integrare, F2).

## Ce oferă proiectul celorlalți
- Actualizarea cu revenire automată (orice stick Cyber Universe), `compara` pentru rapoarte, `hw lista`, browserul text `web`.
- Biblioteci Rust proprii: `crypto/`, `tls/`, `json/`, `rtl8168/`, `e1000e/`; a doua implementare KGR1 pentru Kronos.

## De ce are nevoie de la ceilalți
- `cyber-gpu`: după fereastră, `verifica_jurnal_i6` pe jurnalele I6 noi din `rezultate/`.

## Blocaje / nevoie de Adrian
- **Fereastra următoare pe workstation (~25 min), Release `os-224` (sau cel mai nou, dacă apare):**
  1. **I6, stick-ul de test** (`cyber-universe-gpu-scrie-usb.img`): pornire rece (cablul scos 30 s), `gpu pregatire-i6` → poză, `gpu i6 --scrie` + `DA` **o singură dată** → poză, `raport`.
  2. **Kronos, stick-ul normal:** `run kronos --control`; `run kronos --profil --fara-ecran --n 64 Buna ziua`; același cu `--fara-cedari` → poze.
  3. **Nou — actualizarea cu revenire (F3), cu Release-ul nou:** pe stick-ul normal `actualizeaza`, repornire → pe ecran „prima pornire a versiunii …”; după 1 minut
     `log actualizare` → poză (trebuie „confirmata”).
  4. Pozele + `raport\*.txt` → `rezultate/<data>-workstation-<release>/`.
- **Pentru rapoartele urcate singure în hub (F3):** un token GitHub „fine-grained” doar pentru `Adriancu91/Cyber-hub`, drept „Contents: Read and write”, pus ca
  `github.token` pe stick — când vrei.
- Bucla automată (prima tură, `docs/BUCLA_AUTOMATA.md`), `claude.key`, P5-07: mai târziu.
