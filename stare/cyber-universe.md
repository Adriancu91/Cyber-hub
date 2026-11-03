# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-11-03 16:30 (ora României) · **de:** sesiunea OS programată (14:41, în paralel cu cea de la 13:41) · ultima sarcină: **C-61 gata (P6-44), Release `os-219`**

## Acum
- **Release `os-219`** (CI verde) = C-59 (Kronos: se așteaptă doar firele cu lucru) + C-61 (Cyber-GPU fixat pe `3286a3b`: capătul WPR2 acceptat
  ca „ultima pagină”; după I6 OS-ul scrie și registrele brute: „WPR2 citit dupa I6: LO … HI … (capat: …)”), cu stick-ul de test `gpu-scrie`.
- **Greșeală reală în nucleu, reparată:** un lacăt putea fi eliberat de firul greșit când alt fir doar „încerca” să-l ia. Pe mai multe nuclee asta
  strica lista de fire a unui program sau bloca totul (de aici CI-ul roșu la `kronos-calcul`). Reprodusă local de 8 ori din 12, apoi 0 din 10.
- **P6-45 — ideile tale din C-59, început:** `--profil` desparte acum așteptarea în „trezire / așteptat cel mai lent / adunare” (spune care ipoteză
  din simulare e adevărată); „bucățele”: `kronos --bucati N` (cine termină ia următoarea bucată), măsurate de `kronos-calcul --cauta` (1/2/4/8 pe fir)
  și scrise în reglaj doar dacă bat varianta de acum. Aceleași simboluri în QEMU. Implicit oprit. CI verde → **Release `os-220`** (= `os-219` + acestea).

## Urmează
- P6-45 mai departe: echipe 9×4 / 6×6, un singur bloc pe simbol (fără clopoțel), un fir liber — toate în `--cauta`; câștigă măsurătoarea.
- Fereastra I6 (pasul următor după C-58), testul Kronos pe workstation, prima tură a buclei automate.

## Ce oferă proiectul celorlalți
- Pentru `cyber-gpu`: `gpu tur` (rândurile `fapt …`), `gpu lant`, `gpu pregatire-i6`, `gpu i6 --scrie` (acum cu LO/HI brute după I6), jurnalul pe loc pe stick.
- Biblioteci Rust proprii: `crypto/`, `tls/`, `json/`, `rtl8168/`, `e1000e/`; a doua implementare KGR1 pentru Kronos.

## De ce are nevoie de la ceilalți
- `cyber-gpu`: verificarea lui `raport\gpu-jurnal-002.txt` (de pe stick-ul de test, după ce ajunge în `rezultate/`) cu `i6_log::wpr2_after_i6`.

## Blocaje / nevoie de Adrian
- **Kronos pe workstation (~5 min, stick-ul normal, Release-ul `os-220`):** `cpu porneste`, `run kronos-calcul --cauta`,
  `run kronos --control`, `run kronos --profil --fara-ecran --n 64 Buna ziua`, `run kronos --profil --n 64 Buna ziua` → poze (mai ales rândurile
  „bariere” și „bariera in medie: trezire / cel mai lent / adunare”), `raport` → `rezultate/`.
- **I6 (C-58/C-61):** la fereastra următoare copiezi întâi `raport\gpu-jurnal-002.txt` de pe stick-ul de test vechi în `rezultate/`; Cyber-GPU îl
  verifică. Abia după aceea I6 se repetă cu stick-ul de test nou (`cyber-universe-gpu-scrie-usb.img` din `os-220`): pornire rece (cablul scos 30 s),
  `gpu pregatire-i6` → poză (trebuie „WPR2 coborat”, „TRECE”, „0 scrieri”), `gpu i6 --scrie` + `DA` → poză (rândul nou „WPR2 citit dupa I6”), `raport`.
  Pozele + `raport\*.txt` + `raport\gpu-jurnal-*.txt` → `rezultate/<data>-workstation-i6/`. Dacă ecranul se blochează: 1 minut, oprire, nu repeta azi.
- **Bucla automată:** prima tură (pașii din `docs/BUCLA_AUTOMATA.md` din repo-ul OS) — când ai ~20 min.
- `github.token`, `claude.key`, tag-ul `stabil-2026-10-23`, P5-07: mai târziu.
