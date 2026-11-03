# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-11-03 20:46 (ora României) · **de:** sesiunea OS programată (20:46, oprire scurtă — nicio comandă nouă) · ultima sarcină: **P6-45 gata, Release `os-222`**

## Acum
- **Release `os-222`** (CI verde) = `os-220` + restul ideilor tale din C-59 (P6-45). **Acesta e Release-ul pentru fereastra de mâine (C-63).**
  Fără fișier de reglaj merge exact ca `os-220`; variantele noi pornesc doar dacă `kronos-calcul --cauta` le găsește mai rapide.
- **Un singur bloc pe simbol** (`kronos --bloc`): toate calculele unui simbol sunt date firelor deodată; fiecare fir ia bucăți dintr-un contor
  comun, iar cel care termină ultima bucată a unui calcul pregătește următorul și îl „deschide” — nu mai e un fir principal care adună și
  republică de ~49 de ori pe simbol. Aceleași simboluri în QEMU.
- **Un procesor liber:** `--cauta` măsoară blocul și pe toate procesoarele minus unul (35 pe workstation).
- **Echipe** (`kronos --echipe N`): așteptare în 2 trepte (în echipă, apoi doar șefii); `--cauta` încearcă echipe de 4 (9×4) și 6 (6×6).
- `--cauta` scrie în reglaj doar varianta câștigătoare (rânduri noi posibile: `planificare = bloc`, `echipe = N`, `bucati = N`).

## Urmează
- Fereastra de mâine 07:00 (C-63) cu `os-222`; după rezultate, alegem varianta (sau, dacă procesorul liber ajută mult, fixarea firelor pe procesoare).
- Altfel coada OS nu are sarcini libere fără placă/Adrian → opriri scurte până la o comandă nouă.

## Ce oferă proiectul celorlalți
- Pentru `cyber-gpu`: `gpu tur` (rândurile `fapt …`), `gpu lant`, `gpu pregatire-i6`, `gpu i6 --scrie` (acum cu LO/HI brute după I6), jurnalul pe loc pe stick.
- Biblioteci Rust proprii: `crypto/`, `tls/`, `json/`, `rtl8168/`, `e1000e/`; a doua implementare KGR1 pentru Kronos.

## De ce are nevoie de la ceilalți
- `cyber-gpu`: verificarea lui `raport\gpu-jurnal-002.txt` (de pe stick-ul de test, după ce ajunge în `rezultate/`) cu `i6_log::wpr2_after_i6`.

## Blocaje / nevoie de Adrian
- **Kronos pe workstation (~10 min, stick-ul normal, Release-ul `os-222`):** `cpu porneste`, `run kronos-calcul --cauta` (poză la rândurile
  „bucati”, „echipe”, „un bloc pe simbol” și la ultimul rând „cea mai buna”), `run kronos --control`, `run kronos --profil --fara-ecran --n 64 Buna ziua`,
  și pentru comparație directă `run kronos --profil --fara-ecran --n 64 --bloc Buna ziua` → poze, `raport` → `rezultate/`.
- **I6 (C-58/C-61):** la fereastra următoare copiezi întâi `raport\gpu-jurnal-002.txt` de pe stick-ul de test vechi în `rezultate/`; Cyber-GPU îl
  verifică. Abia după aceea I6 se repetă cu stick-ul de test nou (`cyber-universe-gpu-scrie-usb.img` din `os-222`): pornire rece (cablul scos 30 s),
  `gpu pregatire-i6` → poză (trebuie „WPR2 coborat”, „TRECE”, „0 scrieri”), `gpu i6 --scrie` + `DA` → poză (rândul nou „WPR2 citit dupa I6”), `raport`.
  Pozele + `raport\*.txt` + `raport\gpu-jurnal-*.txt` → `rezultate/<data>-workstation-i6/`. Dacă ecranul se blochează: 1 minut, oprire, nu repeta azi.
- **Bucla automată:** prima tură (pașii din `docs/BUCLA_AUTOMATA.md` din repo-ul OS) — când ai ~20 min.
- `github.token`, `claude.key`, tag-ul `stabil-2026-10-23`, P5-07: mai târziu.
