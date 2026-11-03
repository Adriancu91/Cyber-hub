# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-11-03 15:45 (ora României) · **de:** sesiunea OS programată · OPRIT ridicat de C-59 · ultima sarcină: **C-59 gata (P6-43)**

## Acum
- **C-59 gata (P6-43) — Kronos: mai puțină așteptare între fire.** Cauza găsită: fiecare din cele 49 de „așteptări ale firelor” pe simbol costa ~105 µs
  (ar trebui câteva µs). Motorul aștepta **toate** cele 35 de fire, chiar și pe cele fără nimic de făcut (la qkv + atenție și la proiecție lucrează doar 12);
  acelea, stând degeaba, își cedau procesorul și proiecția aștepta să se întoarcă — de aceea proiecția reală era mult mai lentă decât în `--cauta`.
  Acum: se așteaptă doar firele care au lucru, fiecare fir are semnalul lui „gata” (fără un contor comun pe care se calcă toate), iar firele rămân treze
  când sunt destule procesoare. Aceleași simboluri (verificat în QEMU: vectorii oficiali, `--control`). `--profil` arată acum barierele (câte pe simbol,
  câte µs fiecare), iar `kronos-calcul --cauta` costul unei bariere goale. **Viteza reală se vede doar pe workstation.**
  Release-ul: împreună cu C-61 (refixarea Cyber-GPU după C-58), pe care o face acum o altă sesiune OS (P6-44), cum cere C-61.
- CI: testul temporizatorului din QEMU cu 4 procesoare pica des pe mașina CI (84–87 bătăi pe secundă în loc de ~100, fără legătură cu Kronos);
  acum măsoară de până la 3 ori și, cu mai multe procesoare, acceptă de la 80. Cealaltă sesiune a reparat azi și o greșeală reală în nucleu
  (un lacăt care putea fi eliberat de firul greșit — blocarea lui `kronos-calcul` din CI).
- C-58 (verificarea capătului WPR2 la I6) e la Cyber-GPU; după ce o repară, refixarea în OS vine printr-o comandă nouă.

## Urmează
- Fereastra I6 pe workstation **cu Adrian de față** (pașii mai jos), apoi jurnalul de pe stick → `rezultate/` → Cyber-GPU îl compară cu simularea.
- Testul Kronos cu Release-ul nou (C-59) la fereastra următoare.
- Prima tură a buclei automate (cu `gpu tur`) → raportul în `rezultate/` → Cyber-GPU îl compară cu `compara_raport`.
- Watchdog-ul chipsetului (ceasul de siguranță „hardware”): după ce vedem placa de bază a workstation-ului.

## Ce oferă proiectul celorlalți
- Pentru `cyber-gpu`: `gpu tur` (rândurile `fapt …`), `gpu lant`, `gpu pregatire-i6`, `gpu i6 --scrie` și jurnalul pe loc (formatul `Event`, citibil cu `i6_log::parse_line`).
- Biblioteci Rust proprii: `crypto/`, `tls/`, `json/`, `rtl8168/`, `e1000e/`; a doua implementare KGR1 pentru Kronos.

## De ce are nevoie de la ceilalți
- `cyber-gpu`: după fereastră, analiza jurnalului `gpu-jurnal-NNN.txt` (din `rezultate/`).

## Blocaje / nevoie de Adrian
- **Kronos pe workstation cu Release-ul nou (C-59, ~5 min, stick-ul normal):** `cpu porneste`, `run kronos-calcul --cauta`, `run kronos --control`,
  `run kronos --profil --fara-ecran --n 64 Buna ziua`, `run kronos --profil --n 64 Buna ziua` → poze (mai ales rândul „bariere”), `raport` → `rezultate/`.
- **I6:** așteptăm repararea C-58 la Cyber-GPU; la fereastra următoare copiezi `raport\gpu-jurnal-002.txt` de pe stick-ul de test (cerut în C-58). Nu repeta `gpu i6 --scrie` până atunci.
- **Bucla automată:** prima tură (pașii din `docs/BUCLA_AUTOMATA.md` din repo-ul OS; autologin e deja pus) — când ai ~20 min.
- `github.token`, `claude.key`, tag-ul `stabil-2026-10-23`, P5-07: mai târziu.
