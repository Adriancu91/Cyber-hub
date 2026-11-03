# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-11-03 05:41 (ora României; **OPRIT** rămâne, verificat din nou — oprire de siguranță după 3 sesiuni fără sarcină, din lipsă de comenzi) · **de:** sesiunea OS programată · ultimele sarcini: **C-53 gata (P6-41, `os-213`)**, **C-55 gata (P6-42, `os-214`)**

## Acum
- **OPRIT: necesită analiza lui Adrian.** Ultimele 3 sesiuni programate nu au avut nicio sarcină de făcut (coada e goală fără tine), așa că regula de siguranță oprește începerea de sarcini noi. Nu e nicio eroare: CI verde, Release `os-214`, codul neschimbat. Se ridică cu o comandă nouă de la Adrian în `COMENZI.md` sau cu fereastra pe workstation.

- **C-55 gata (P6-42) — `gpu tur` și `gpu lant`, testate DOAR în simulare (Release `os-214`):**
  - `gpu tur` (**doar citire**, 0 scrieri): citește din placă tot ce s-a citit deja în siguranță (identitatea, pornirea firmware-ului plăcii,
    VBIOS, FWSEC, pregătirea I6) și scrie un rând `fapt <cheie> = <valoare>` pe fiecare lucru → Cyber-GPU compară raportul cu simularea.
    E pe lista albă a buclei automate și în lista implicită a scriptului Windows.
  - `gpu lant` (cere „DA”; **refuzat în bucla automată**): pașii ferestrei unul după altul — pregătire → Bus Master → I6 → (I7 nu e gata:
    lanțul se oprește singur) → Bus Master la loc → turul de citire după. Se oprește la primul eșec și pune placa la loc. Scrie doar pe stick-ul de test.
- Cyber-GPU fixat pe `4e6f747` (≥ `911e6d0`). Nimic nu a rulat pe placa reală.

- **C-52 gata (P6-40) — primele scrieri în placă din OS (pasul I6), construite și testate DOAR în simulare:**
  - `gpu pregatire-i6` (**doar citire**): unde e FWSEC în VBIOS, siguranța → semnătura, VRAM, WPR2, regiunea FRTS, „criteriul I6-citire”.
  - Jurnalul pe loc: fiecare citire/scriere în placă merge pe stick, cu ora, în `/usb/raport/gpu-jurnal-NNN.txt`, în clipa în care se face.
  - `gpu i6 --scrie` (cere „DA”): Bus Master pornit → FWSEC (programul semnat NVIDIA din VBIOS) încărcat prin DMA în falcon-ul GSP →
    Bus Master oprit la loc (și la eroare). Există **doar pe stick-ul de test** (`kernel-gpu-scrie` / `cyber-universe-gpu-scrie-usb.img`);
    sistemul obișnuit nu poate scrie deloc în placă. Gard în plus în OS: doar bitul Bus Master și doar fereastra GSP.
  - În simulare TRECE cap-coadă (84 de scrieri în cele 18 registre din plan, WPR2 unde trebuie, jurnalul verificat cu `i6_log` al Cyber-GPU).

- **C-53 gata (P6-41) — bucla automată, partea OS (testată doar în QEMU):**
  - Dacă pe stick există `auto\teste.txt`, sistemul rulează la pornire comenzile din listă, **doar cele care citesc** (lista albă);
    `gpu i6 --scrie`, orice `--scrie`, `reboot`, rețeaua = refuzate și notate. Raportul `auto\raport-<data>.txt` se scrie după fiecare comandă
    (și ce afișează Kronos), cu rândul „REZULTAT: n rulate, m refuzate”; lista devine `teste-facut-<data>.txt`; calculatorul repornește singur.
  - **Ceasul de siguranță:** repornire dacă lista nu termină în 10 minute (sau `ceas N`); o listă întreruptă nu se reia („INTRERUPT” în raport).
  - Scriptul pentru Windows `bucla-automata.ps1` (în Release): `pregateste` (pune Release-ul pe stick păstrând `kronos\`, `firmware\`, `cyber.rw`,
    scrie lista, „pornește o dată de pe stick”, repornește; doar 08–22) și `citeste` (rapoartele, gata de pus în `rezultate/`). Fără parole sau chei.
    **Nerulat încă** (în cloud nu există PowerShell) → prima tură cu Adrian.
  - Pregătirea cu Adrian, pas cu pas: `docs/BUCLA_AUTOMATA.md` din repo-ul OS.

## Urmează
- Fereastra I6 pe workstation **cu Adrian de față** (pașii mai jos), apoi jurnalul de pe stick → `rezultate/` → Cyber-GPU îl compară cu simularea.
- Testul Kronos cu `os-211`/`os-212` (C-48) poate intra în aceeași fereastră.
- Prima tură a buclei automate (cu `gpu tur`) → raportul în `rezultate/` → Cyber-GPU îl compară cu `compara_raport`.
- Watchdog-ul chipsetului (ceasul de siguranță „hardware”): după ce vedem placa de bază a workstation-ului.

## Ce oferă proiectul celorlalți
- Pentru `cyber-gpu`: `gpu tur` (rândurile `fapt …`), `gpu lant`, `gpu pregatire-i6`, `gpu i6 --scrie` și jurnalul pe loc (formatul `Event`, citibil cu `i6_log::parse_line`).
- Biblioteci Rust proprii: `crypto/`, `tls/`, `json/`, `rtl8168/`, `e1000e/`; a doua implementare KGR1 pentru Kronos.

## De ce are nevoie de la ceilalți
- `cyber-gpu`: după fereastră, analiza jurnalului `gpu-jurnal-NNN.txt` (din `rezultate/`).

## Blocaje / nevoie de Adrian
- **Oprirea de siguranță (OPRIT):** sesiunile OS nu mai încep sarcini până nu dai o comandă nouă în `COMENZI.md` (orice comandă nouă o ridică, ca la C-12). Dacă vrei ca sesiunile să continue singure și când coada e goală, spune ce să facă (ex. C-41 amânat, sau altă sarcină).
- **Fereastra I6 (~20 min, DOAR când ai timp să fii de față; nimic nu se face fără tine):**
  0. Pregătire: un **stick de test separat**, scris (ca de obicei, cu Rufus/balenaEtcher) din `cyber-universe-gpu-scrie-usb.img` din
     Release `os-214` (sau `os-212`) (are deja `cyber.rw`, deci jurnalul se poate scrie pe el). Workstation: **oprire completă, cablul scos 30 s**.
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
- **Bucla automată (la întoarcere, ~3 nov, ~20 min, o singură dată):** pașii din `docs/BUCLA_AUTOMATA.md` (repo OS): în BIOS Secure Boot oprit și
  Windows primul la pornire; intrarea automată în Windows (o alegi tu); PowerShell ca administrator → `.\bucla-automata.ps1 pregateste -DosarRelease <dosarul Release-ului>`;
  urmărim împreună prima tură; înapoi în Windows `.\bucla-automata.ps1 citeste`.
- `github.token`, `claude.key`, tag-ul `stabil-2026-10-23`, P5-07: mai târziu.
