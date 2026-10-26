# Stare: Cyber-GPU (`cyber-gpu`)

**Actualizat:** 2026-10-26 19:50 (ora României) · **de:** sesiunea Cyber-GPU 6 (cloud, fără placă)

## Acum
- **Nimic nu s-a testat pe RTX 3070 Ti.** Tot ce „merge” e verificat doar pe calculator (SIMULARE, aritmetică sau comparație cu antetele NVIDIA). Nicio linie de cod nu scrie în placă.
- **C-20, în lucru (B, C, A-pregătire, D partea 1 făcute):**
  - **B:** crate nou `nvidia-rm570` — 1 419 valori luate **automat** din antetele publice NVIDIA (570.144, MIT): registrele GSP/falcon, metodele de lansare, descrierea lansării (QMD), structurile GSP. Tot ce scrisesem de mână în sesiunea 5 a fost comparat cu ele: **toate egale**.
  - **C:** mesajele mari către GSP (împărțite în bucăți) și tabelul de setări trimis la pornire (cele 2 setări folosite pe plăcile GA102) — SIMULARE.
  - **D (partea 1):** un „procesor de comenzi” simulat: primul program compilat cu NAK (adunarea a 64 de numere) e lansat cap-coadă în model, iar rezultatul e identic cu calculul de control. Programul „rulează” pe procesor, nu pe placă.
  - **A (doar pregătit):** scriptul și instrucțiunile pe minute pentru proba tinygrad (`docs/TEST_MATRIX.md` partea P) + cititorul jurnalului ei. **Nerulat.**
- 157 de teste trec; CI verde (rulările 22–26).

## Urmează
- C-20 D partea 2: „GSP fals” la nivel de registre (pornire, mailbox, INIT_DONE) în simulare.
- Antetele fișierelor `bootloader`/`booter_load` (I4c), apoi C-20 E: matmul cu NAK (Mesa de reconstruit în cloud) + comparația corectă cu FMA.
- Fereastra pe workstation (27–28 oct, ~30 min): citiri I0–I3 + FWSEC + fișierele de pe stick, **0 scrieri** (`docs/TEST_MATRIX.md` B0).

## Ce oferă proiectul celorlalți
- `cyber-universe`: crate-urile no_std `gpu-core`, `gpu-pci`, `nvidia-ga104`, `gpu-compute`, `gpu-sim` (teste), MIT. os-191 e fixat pe `dac2e32`: rămâne valabil.
  Nou după `dac2e32`, **doar adăugări**: crate-ul `nvidia-rm570` (date generate din antetele NVIDIA, MIT, fără dependențe) de care `nvidia-ga104` depinde acum;
  `nvidia-ga104::qmd`, `gsp::registry`; în `gpu-sim`: procesorul de comenzi și cititorul jurnalului. Detalii: `integration/cyber-universe/UTILIZARE.md`.
- `kronos` / K6-CPU: operatorii lui Kronos pe procesor, neschimbați.

## De ce are nevoie de la ceilalți
- De la `kronos`: workstation-ul, doar în fereastra aprobată de Adrian.

## Blocaje / nevoie de Adrian
- **Fereastra pe workstation (27 sau 28 oct, ~30 min):** lista în `docs/TEST_MATRIX.md` partea B0 (Release-ul OS os-191 e gata).
- **Înainte de fereastră, fișierele firmware pe stick:** din https://gitlab.com/kernel-firmware/linux-firmware, folderul `nvidia/ga102/gsp/`,
  cele 4 fișiere `*-570.144.bin` în `firmware\nvidia\ga102\gsp\` pe stick (+ `LICENCE.nvidia` în `firmware\`); sumele în
  `docs/COMPATIBILITATE_FIRMWARE.md`. **Nu le urca nicăieri.**
- **Opțional, pentru proba tinygrad (partea P, scrie în placă, doar cu tine de față, după B0):** un al doilea stick cu Ubuntu 24.04 live și laptopul pentru SSH.
- Tag-ul `stabil-2026-10-23` (tot 403 din cloud; nu blochează nimic): GitHub → cyber-gpu → Releases → „Draft a new release” → tag `stabil-2026-10-23`, Target commit `41e44ba` → pre-release → Publish.
