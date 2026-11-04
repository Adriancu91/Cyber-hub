# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-11-05 01:40 (ora României) · **de:** sesiunea OS programată (23:42) · **Release `os-238`** (CI verde): F2 + F3 + F4 + F6a în `main`

## Acum
- **F1 (mașina virtuală) anulat** de Adrian la 23:10: era gata (discul VM pornea în QEMU ca stick, cu rețea) și a fost scos curat din repo și din CI.
- **F3 gata (P6-50) — actualizare de sine cu revenire:** `actualizeaza` păstrează versiunea de acum în `boot/vechi/`; prima pornire a versiunii noi e o
  **încercare**, confirmată după ce ajunge la desktop/shell și merge 60 s; dacă nu se confirmă, la pornirea următoare sistemul **pune singur la loc versiunea veche**
  și repornește. `actualizare-automata` (fișier gol pe stick) = se actualizează singur la pornire. Raport la fiecare confirmare / revenire pe stick
  (`raport/actualizare-*.txt`), trimis în hub doar dacă e `github.token` pe stick. Testat în QEMU (scenariile `revenire`, `update`) și cu nucleul normal.
  Limita, spusă cinstit: un nucleu care pică înainte să citească stick-ul nu revine singur (fișierele vechi rămân în `boot/vechi/`). Detalii: `docs/ACTUALIZARE.md`.
- **F9 pas 1 (P6-52):** comanda `compara <f1> <f2>` arată rândurile diferite între două rapoarte (pe lista albă).
- **F6a gata (P6-53) — browserul text `web`:** `web <adresă>` arată o pagină ca text (titluri, liste, tabele, legături numerotate `[N]`), `web <N>` deschide
  legătura N, `web --pagina P` pagina de ecran următoare. Pagini simple și documentație (fără JavaScript). Analizor HTML scris de noi.
- **F4 (P6-51) și F2 (P6-49) integrate în `main`** (lucrate pe ramurile paralele): `hw lista [--detalii]` (doar citiri, „0 scrieri”) și consola prin rețea
  `remote porneste|opreste|stare` (cheia doar pe stick, doar lista albă, **încă fără criptare → doar în rețeaua de acasă**). Părțile mașinii virtuale scoase.
- **CI verde (run 41929038638) → Release `os-238`.** Un CI roșu de pe drum (meniul desktop cu `/bin/web`) a fost reparat.

## Urmează
- F8/F9 restul (editor / git simplu în OS) — F2 e acum în `main`.
- Remote cu criptare (TLS), înainte de folosirea pe o rețea care nu e de încredere.

## Ce oferă proiectul celorlalți
- Actualizarea cu revenire automată (orice stick Cyber Universe), `compara` pentru rapoarte, `hw lista`, browserul text `web`.
- Biblioteci Rust proprii: `crypto/`, `tls/`, `json/`, `rtl8168/`, `e1000e/`; a doua implementare KGR1 pentru Kronos.

## De ce are nevoie de la ceilalți
- `cyber-gpu`: după fereastră, `verifica_jurnal_i6` pe jurnalele I6 noi din `rezultate/`.

## Blocaje / nevoie de Adrian
- **Fereastra următoare pe workstation (~25 min), Release `os-238`** (I6 rămâne pe stick-ul de test din `os-238`):
  1. **I6, stick-ul de test** (`cyber-universe-gpu-scrie-usb.img`): pornire rece (cablul scos 30 s), `gpu pregatire-i6` → poză, `gpu i6 --scrie` + `DA` **o singură dată** → poză, `raport`.
  2. **Kronos, stick-ul normal:** `run kronos --control`; `run kronos --profil --fara-ecran --n 64 Buna ziua`; același cu `--fara-cedari` → poze.
  3. **Nou — actualizarea cu revenire (F3), cu Release-ul nou:** pe stick-ul normal `actualizeaza`, repornire → pe ecran „prima pornire a versiunii …”; după 1 minut
     `log actualizare` → poză (trebuie „confirmata”).
  4. **Nou — hardware (F4):** `hw lista --detalii` → poze (completăm numele plăcilor necunoscute). Opțional browserul: `run web example.com`.
  5. Pozele + `raport\*.txt` → `rezultate/<data>-workstation-<release>/`.
- **Pentru rapoartele urcate singure în hub (F3):** un token GitHub „fine-grained” doar pentru `Adriancu91/Cyber-hub`, drept „Contents: Read and write”, pus ca
  `github.token` pe stick — când vrei.
- Bucla automată (prima tură, `docs/BUCLA_AUTOMATA.md`), `claude.key`, P5-07: mai târziu.
