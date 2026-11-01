# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-11-01 ~20:45 (ora României) · **de:** sesiunea OS programată · ultima sarcină: **C-52 gata (P6-40)**; CI verde, Release `os-212`

## Acum
- **C-52 gata (P6-40) — primele scrieri în placă din OS (pasul I6), construite și testate DOAR în simulare:**
  - `gpu pregatire-i6` (**doar citire**): unde e FWSEC în VBIOS, siguranța → semnătura, VRAM, WPR2, regiunea FRTS, „criteriul I6-citire”.
  - Jurnalul pe loc: fiecare citire/scriere în placă merge pe stick, cu ora, în `/usb/raport/gpu-jurnal-NNN.txt`, în clipa în care se face.
  - `gpu i6 --scrie` (cere „DA”): Bus Master pornit → FWSEC (programul semnat NVIDIA din VBIOS) încărcat prin DMA în falcon-ul GSP →
    Bus Master oprit la loc (și la eroare). Există **doar pe stick-ul de test** (`kernel-gpu-scrie` / `cyber-universe-gpu-scrie-usb.img`);
    sistemul obișnuit nu poate scrie deloc în placă. Gard în plus în OS: doar bitul Bus Master și doar fereastra GSP.
  - În simulare TRECE cap-coadă (84 de scrieri în cele 18 registre din plan, WPR2 unde trebuie, jurnalul verificat cu `i6_log` al Cyber-GPU).
- Cyber-GPU fixat pe `9597863`. Nimic nu a rulat pe placa reală.

## Urmează
- Fereastra I6 pe workstation **cu Adrian de față** (pașii mai jos), apoi jurnalul de pe stick → `rezultate/` → Cyber-GPU îl compară cu simularea.
- Testul Kronos cu `os-211`/`os-212` (C-48) poate intra în aceeași fereastră.
- C-53 (bucla automată, P6-41) e preluată de o altă sesiune OS, în paralel; ea va actualiza starea la final.

## Ce oferă proiectul celorlalți
- Pentru `cyber-gpu`: `gpu pregatire-i6`, `gpu i6 --scrie` și jurnalul pe loc (formatul `Event`, citibil cu `i6_log::parse_line`).
- Biblioteci Rust proprii: `crypto/`, `tls/`, `json/`, `rtl8168/`, `e1000e/`; a doua implementare KGR1 pentru Kronos.

## De ce are nevoie de la ceilalți
- `cyber-gpu`: după fereastră, analiza jurnalului `gpu-jurnal-NNN.txt` (din `rezultate/`).

## Blocaje / nevoie de Adrian
- **Fereastra I6 (~20 min, DOAR când ai timp să fii de față; nimic nu se face fără tine):**
  0. Pregătire: un **stick de test separat**, scris (ca de obicei, cu Rufus/balenaEtcher) din `cyber-universe-gpu-scrie-usb.img` din
     Release `os-212` (are deja `cyber.rw`, deci jurnalul se poate scrie pe el). Workstation: **oprire completă, cablul scos 30 s**.
  1. Pornești de pe stick, Esc → `cyber>`. Scrii `gpu pregatire-i6` → **poză**. Trebuie: „VRAM 8192 MiB”, „WPR2 coborat”,
     „criteriul I6-citire: TRECE”, „0 scrieri”. Dacă NU TRECE: **stop**, poză, oprire, nu continua.
  2. Scrii `gpu i6 --scrie`, citești avertismentul, scrii `DA` + Enter. Poate dura până la ~1 minut (fiecare scriere merge pe stick).
     **Poză** cu toate rândurile; trebuie „pas I6 FWSEC-FRTS: ok”, „Bus Master oprit la loc”, „verificarea jurnalului … TRECE”, „rezultat I6: TRECE”.
  3. Scrii `raport` (salvează tot pe stick).
  4. **Oprire completă** (butonul ținut 10 s, cablul scos 30 s) → Windows → `nvidia-smi` + Kronos, ca de obicei.
  - Dacă ecranul se stinge sau se blochează: aștepți 1 minut, apoi pasul 4. Jurnalul de până atunci e pe stick. **Nu repeta** în aceeași zi.
  - După: pozele + `raport\*.txt` + `raport\gpu-jurnal-*.txt` de pe stick → `rezultate/<data>-workstation-i6/`.
- **Kronos pe workstation cu `os-211` (C-48, ~6 min):** `cpu porneste`, `run kronos-calcul --cauta`, `run kronos --control`,
  `run kronos --profil --fara-ecran --n 64 Buna ziua`, `run kronos --profil --n 64 Buna ziua`, `raport` → `rezultate/`.
- `github.token`, `claude.key`, tag-ul `stabil-2026-10-23`, P5-07: mai târziu.
