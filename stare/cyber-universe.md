# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-11-11 14:50 (ora României) · **de:** sesiunea OS programată (13:30) — C-102 continuare, C-104, C-103 (partea OS).

## Acum
- **Numerotare (15:40):** `os-282` nu există (CI-ul lui anulat de push-ul P6-76). Reparația `bDmemStack` + C-105 vin împreună în **`os-283`** (CI 283 în lucru).
- **C-105 partea OS (P6-75):** comanda din hub `ciclu-test os-<N>` (actualizare → repornire → `gpu recupereaza` + `gpu lant` → raport → ascultă din nou) e gata și testată în QEMU, dar **oprită**: pornește doar cu cele două chei ale lui Adrian (fișierul `hub/permite-test-placa` pe stick + o decizie în `DECIZII.md` cu `ciclu-test activat`).
- **Release `os-281` (14:39, CI verde) — pe acesta îl folosește Adrian.** Conține tot din `os-280` (14:13) plus două lucruri noi.
- **C-102 continuare (P6-72):** jurnalul `os-279` a arătat că GSP-RM pornește, dar refuză singur inițializarea (`0x59` = `NV_ERR_OPERATING_SYSTEM`) după 843 de mesaje de diagnostic (NOCAT) pe care nu le citeam. cyber-gpu `bcc314e` le decodează (doar citiri) → jurnalul spune acum **de ce**. Nu e o reparație.
- **C-104 (P6-73):** „agentul de comenzi” — `hub asculta` (la fiecare 2 min, Esc oprește; pornit singur dacă pe stick e `hub/asculta`) ia comenzile noi din `integrare/cyber-universe/os-comenzi.md`, doar lista albă, fiecare o dată; răspunsul fiecăreia în `integrare/cyber-universe/raspunsuri/K-<nr>.txt`. Test QEMU trece.
- **C-103 partea OS (P6-74):** `gpu recupereaza` (cere DA, doar stick-ul de test) — Booter Unload coboară WPR2 fără repornire, apoi verifică că I6 poate rula din nou. `gpu identifica` arată ce reset suportă placa (doar citire). Test QEMU (SIMULARE) trece; pe placă neîncercat.

## Urmează
- Jurnalul testului cu `os-281` → rândurile `text NOCAT …` + rezumatul de la final → cyber-gpu face reparația 0x59.
- Prima probă `gpu recupereaza` pe placă (după lanțul oprit la I8); dacă merge, propun legarea în `gpu lant` (a doua încercare fără cablu) — doar cu „da”.

## Ce oferă proiectul celorlalți
- `gpu lant` I6 → I14, `gpu recupereaza`, `kronos --gpu` pe stick-ul de test (I8–I14 doar în SIMULARE); jurnale + rapoarte trimise singure în hub (cu token).
- `hub ruleaza` / `hub asculta` (comenzi din hub, răspuns pe comandă), `test tot`, `kronos --conversatie`, git pe ramuri `os/…`, `web`, `files`; bibliotecile `crypto/`, `tls/`, `json/`, `rtl8168/`, `e1000e/`.

## De ce are nevoie de la ceilalți
- **`cyber-gpu`:** după jurnalul cu `os-281`, reparația pentru 0x59. Mai târziu: zona de comenzi de 32 KiB pentru modelul de 24 de straturi.
- **`kronos`:** Release-ul `kronos-kgr1-513` (opțional).

## Blocaje / nevoie de Adrian

**Testul cu `os-281` (workstation), când poți:**
1. Din Release-ul **`os-281`** (github.com/Adriancu91/cyber-universe → Releases) iei `cyber-universe-gpu-scrie-usb.img` și îl scrii cu Rufus pe **stick-ul de test**. Stick-ul normal rămâne cum e.
2. **Oprire completă**, cablul scos **30 s**; pornești de pe stick-ul de test (F8), cu ambele stick-uri.
3. `gpu lant` → `DA` + Enter. Probabil se oprește iar la I8 cu 0x59 — e de așteptat. **Poze** la rândurile `text NOCAT …` și la rezumatul de la final.
4. **Nou (C-103):** imediat după, `gpu recupereaza` → `DA`. Poză la rândul „pas C-103 Booter Unload …” și la „pregatirea I6 trece din nou” / „NU trece”. Dacă trece, poți rula `gpu lant` încă o dată **fără** să scoți cablul.
5. `raport` (+ `trimite` dacă ai token). Pozele + `raport\gpu-jurnal-*.txt` în `rezultate/2026-11-11-workstation-os281/` (sau data zilei).

**Opțional (C-104, ~5 min):** tokenul pentru `hub asculta` — pașii exacți în `docs/USB.md` punctul 15 (token fin, doar `Cyber-hub`, Contents read and write, fișierul `github.token` DOAR pe stick).

**Când vrei (C-105, fără grabă):** ciclul de test complet automat (`ciclu-test os-<N>` din hub) e gata în Release-urile de la `os-283` încolo, dar **oprit**. Îl pornești doar tu, cu două chei: (1) pe stick-ul de test, în dosarul `hub`, un fișier gol `permite-test-placa`; (2) o decizie nouă în `DECIZII.md` (prin centrul de comandă), un rând cu exact `ciclu-test activat`. Până atunci rămâne regula „scrieri pe placă doar cu tine de față”. Pașii: `docs/USB.md` punctul 16. Îl oprești oricând ștergând fișierul de pe stick.
