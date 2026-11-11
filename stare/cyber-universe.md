# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-11-11 17:10 (ora României) · **de:** sesiunea OS programată (15:00) — P6-76 (os-283), P6-77 (cod gata, CI blocat extern).

## Acum
- **Release `os-283` (15:44, CI verde) — pe acesta îl folosește Adrian la testul următor.** Conține reparația candidat pentru `0x59` (cyber-gpu `2bbd0b3`: `bDmemStack = 1`, singura diferență față de RM, tinygrad, nouveau, nova — C-107) + C-105 (ciclu-test, oprit). `os-282` nu există (CI anulat).
- **P6-77 (C-102 continuare 2):** cyber-gpu `d3c5351` (conținutul celor 2 mesaje PMU în jurnal, doar citiri) legat în `main` (`61a308d`, 10/10 scenarii GPU local). **CI 284 atârnă la instalarea pachetelor pe mașinile GitHub** (pasul „Unelte sistem”, nu codul nostru): prima rulare oprită la 60 min, re-rulată la 16:57. Când trece → `os-284` (= os-283 + jurnalul PMU).
- **C-105 partea OS (P6-75):** `ciclu-test os-<N>` din hub e gata și testat în QEMU, dar **oprit** până la cele două chei ale lui Adrian.
- Din azi, tot în os-283: `hub asculta` (C-104), `gpu recupereaza` (C-103, pe placă neîncercat), jurnalul NOCAT decodat (C-102).

## Urmează
- CI 284 verde → Release `os-284`. Dacă tot atârnă, re-rulare; la a doua oprire, propun ca pasul de instalare să pice repede (limită de timp + reîncercări).
- Jurnalul testului cu `os-283`/`os-284`: reușită = `rpc_result … = 0x00000000` și începe I8e; eșec = tot `0x59` → cyber-gpu încearcă rezervele (`bIsPassthru`, `CLOCK_BOOST`, `RMDevidCheckIgnore`), câte una pe rulare.
- Prima probă `gpu recupereaza` pe placă (după un lanț oprit); dacă merge, propun legarea în `gpu lant` — doar cu „da”.

## Ce oferă proiectul celorlalți
- `gpu lant` I6 → I14, `gpu recupereaza`, `kronos --gpu` pe stick-ul de test (I8–I14 doar în SIMULARE); jurnale + rapoarte trimise singure în hub (cu token).
- `hub ruleaza` / `hub asculta` (comenzi din hub, răspuns pe comandă), `test tot`, `kronos --conversatie`, git pe ramuri `os/…`, `web`, `files`; bibliotecile `crypto/`, `tls/`, `json/`, `rtl8168/`, `e1000e/`.

## De ce are nevoie de la ceilalți
- **`cyber-gpu`:** după jurnalul cu `os-283`/`os-284`, pasul următor pentru 0x59 (dacă `bDmemStack` nu a fost cauza). Mai târziu: zona de comenzi de 32 KiB pentru modelul de 24 de straturi.
- **`kronos`:** Release-ul `kronos-kgr1-513` (opțional).

## Blocaje / nevoie de Adrian

**Testul cu `os-283` (sau `os-284`, dacă apare până atunci) pe workstation, la următoarea venire (C-106: nu înainte de joi 13 nov):**
1. Din Release-ul **`os-283`** (sau `os-284`) (github.com/Adriancu91/cyber-universe → Releases) iei `cyber-universe-gpu-scrie-usb.img` și îl scrii cu Rufus pe **stick-ul de test**. Stick-ul normal rămâne cum e.
2. **Oprire completă**, cablul scos **30 s**; pornești de pe stick-ul de test (F8), cu ambele stick-uri.
3. `gpu lant` → `DA` + Enter. Ce contează: rândul `valoare GSP_INIT_DONE: rpc_result … = 0x…` — `0x00000000` înseamnă că reparația a mers; tot `0x59` = nu încă. **Poze** la rândul acesta, la rândurile `text NOCAT …` și la rezumatul de la final.
4. **Nou (C-103):** imediat după, `gpu recupereaza` → `DA`. Poză la rândul „pas C-103 Booter Unload …” și la „pregatirea I6 trece din nou” / „NU trece”. Dacă trece, poți rula `gpu lant` încă o dată **fără** să scoți cablul.
5. `raport` (+ `trimite` dacă ai token). Pozele + `raport\gpu-jurnal-*.txt` în `rezultate/<data>-workstation-os283/` (sau os-284).

**Opțional (C-104, ~5 min):** tokenul pentru `hub asculta` — pașii exacți în `docs/USB.md` punctul 15 (token fin, doar `Cyber-hub`, Contents read and write, fișierul `github.token` DOAR pe stick).

**Când vrei (C-105, fără grabă):** ciclul de test complet automat (`ciclu-test os-<N>` din hub) e gata în Release-urile de la `os-283` încolo, dar **oprit**. Îl pornești doar tu, cu două chei: (1) pe stick-ul de test, în dosarul `hub`, un fișier gol `permite-test-placa`; (2) o decizie nouă în `DECIZII.md` (prin centrul de comandă), un rând cu exact `ciclu-test activat`. Până atunci rămâne regula „scrieri pe placă doar cu tine de față”. Pașii: `docs/USB.md` punctul 16. Îl oprești oricând ștergând fișierul de pe stick.
