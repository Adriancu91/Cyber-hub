# Stare: Cyber-GPU (`cyber-gpu`)

**Actualizat:** 2026-10-27 19:55 (ora României) · **de:** sesiunea Cyber-GPU 10 (cloud, fără placă)

## Acum
- **Nimic nu s-a testat pe RTX 3070 Ti.** Tot ce „merge” e verificat doar pe calculator (SIMULARE, compilare sau comparație cu antetele NVIDIA).
  Codul care ar scrie în placă stă în spatele opțiunii `hw-write`, oprită implicit; nu a rulat pe placă.
- C-18 și C-20 gata. Azi seara, doi pași „fără placă”:
  - **Tabelele de pagini ale plăcii (I9a):** driverul își împarte singur memoria video și face „harta” adreselor pe care o folosește placa
    (5 niveluri, pagini de 4 KiB), după formatul din antetele NVIDIA 570.144 (MIT, generat automat). Fiecare tabelă e golită înainte de folosire.
    Pasul „golden image” rulează acum cap-coadă cu tabelele adevărate, iar un cititor scris separat verifică pagină cu pagină cele 10 buffere.
  - **Înmulțirea de matrice, treapta 5** (fiecare fir calculează 8×8 rezultate): compilată cu Mesa NAK, identică bit cu bit cu calculul de control în model.
    Am observat că fără o indicație explicită compilatorul punea sumele într-o memorie pe care lansatorul nostru nu o pregătește — reparat în program.
- 211 teste trec; CI verde (rularea 39; 40–42 verificate la final).

## Urmează
- Fără placă: încărcătorul ucode-ului prin DMA (în spatele `hw-write`); I9b (scrierea tabelelor în placă + golirea cache-ului de adrese, în spatele `hw-write`);
  treapta 6 matmul.
- Fereastra pe workstation (~30 min): citiri I0–I3 + FWSEC + fișierele de pe stick, **0 scrieri** (`docs/TEST_MATRIX.md` B0); în plus, dacă OS-ul o afișează,
  adresa imaginii ecranului (ca driverul să nu scrie peste ea).
- După B0, doar cu Adrian de față: proba tinygrad (partea P).

## Ce oferă proiectul celorlalți
- `cyber-universe`: crate-urile no_std `gpu-core`, `gpu-pci`, `nvidia-ga104`, `gpu-compute`, `gpu-sim` (teste), MIT. os-191 e fixat pe `dac2e32`: rămâne valabil.
  După `dac2e32`, **doar adăugări** (nimic șters sau redenumit): `nvidia-rm570` (date din antetele NVIDIA, acum și formatele tabelelor de pagini),
  `qmd`, `gsp::{registry,sysinfo,rmapi,golden,falcon,sequencer}` (ultimele două cer `hw-write` pe placa reală — OS-ul nu le cheamă), `fw_hdr`, **`mmu`** (nou),
  `Mmio::is_simulation`; în `gpu-compute`: `fma_f32`, `ftz`, `matmul_fma(_ftz)`; în `gpu-sim`: procesorul de comenzi (+ treptele matmul 1–5), GSP-ul fals,
  RM-ul fals, VRAM simulată. **La o nouă fixare:** `nvidia-ga104` depinde acum și de `gpu-memory` (același repo). Detalii: `integration/cyber-universe/UTILIZARE.md`.
- Observație nouă pentru OS (doar citire, opțională): `integration/cyber-universe/B0_adresa-ecranului.md` — o linie în `hw` cu adresa framebuffer-ului.
- `kronos` / K6-CPU: operatorii lui Kronos pe procesor, neschimbați.

## De ce are nevoie de la ceilalți
- De la `kronos`: workstation-ul, doar în fereastra aprobată de Adrian.
- De la `cyber-universe` (opțional, doar cu „da”-ul lui Adrian): linia cu adresa framebuffer-ului în `hw`.

## Blocaje / nevoie de Adrian
- **Fereastra pe workstation (~30 min):** lista în `docs/TEST_MATRIX.md` partea B0 (Release-ul OS os-191 e gata).
- **Înainte de fereastră, fișierele firmware pe stick:** din https://gitlab.com/kernel-firmware/linux-firmware, folderul `nvidia/ga102/gsp/`,
  cele 4 fișiere `*-570.144.bin` în `firmware\nvidia\ga102\gsp\` pe stick (+ `LICENCE.nvidia` în `firmware\`); sumele în
  `docs/COMPATIBILITATE_FIRMWARE.md`. **Nu le urca nicăieri.**
- **Opțional, pentru proba tinygrad (partea P, scrie în placă, doar cu tine de față, după B0):** un al doilea stick cu Ubuntu 24.04 live și laptopul pentru SSH.
- Tag-ul `stabil-2026-10-23` (tot 403 din cloud; nu blochează nimic): GitHub → cyber-gpu → Releases → „Draft a new release” → tag `stabil-2026-10-23`, Target commit `41e44ba` → pre-release → Publish.
- Fără fereastra pe workstation, pașii rămași „fără placă” se împuținează: după I9b, încărcătorul DMA și treptele matmul, restul (I0–I10 reale) cere placa.
