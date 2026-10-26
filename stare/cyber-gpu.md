# Stare: Cyber-GPU (`cyber-gpu`)

**Actualizat:** 2026-10-27 02:05 (ora României) · **de:** sesiunea Cyber-GPU 7 (cloud, fără placă)

## Acum
- **Nimic nu s-a testat pe RTX 3070 Ti.** Tot ce „merge” e verificat doar pe calculator (SIMULARE, aritmetică sau compilare). Codul care ar scrie
  în placă există acum (pornirea GSP), dar stă în spatele opțiunii `hw-write`, oprită implicit; nu a rulat pe placă.
- **C-20 gata în simulare** (B, C, D, E treptele 1–2; A doar pregătită):
  - **D:** un „GSP fals” pe registre: pornirea simulată merge cap-coadă — FWSEC (zona protejată WPR2) → Booter → GSP pornește → cererea lui de
    „secvențiator” e executată → mesajul „gata” (INIT_DONE). Fiecare defect simulat (placă blocată, cod de eroare, GSP tăcut) e raportat ca eroare.
    Scrierile cerute de firmware în afara zonelor GSP/SEC2 sunt **refuzate**.
  - **I4c:** se citesc antetele fișierelor `bootloader` și `booter_load` (doar unde stau bucățile; conținutul nu e analizat). Doar pe fișiere sintetice.
  - **E:** înmulțirea de matrice (treptele 1 și 2) compilată cu Mesa NAK pentru GA104 și lansată în modelul de comenzi, rezultat identic bit cu bit
    cu calculul de control. **Constatare:** NAK folosește „FMA cu FTZ” (o singură rotunjire, numerele foarte mici aduse la 0) — calculul de control
    face acum la fel (`matmul_fma_ftz`, verificat pe 2 milioane de cazuri).
- 176 de teste trec; CI verde (rulările 28–31).

## Urmează
- Fără placă: treapta 3 matmul (memorie partajată), apoi 2D blocktiling; încărcătorul ucode-ului (DMA, în spatele `hw-write`); `GspSystemInfo`; „golden image”.
- Fereastra pe workstation (27–28 oct, ~30 min): citiri I0–I3 + FWSEC + fișierele de pe stick, **0 scrieri** (`docs/TEST_MATRIX.md` B0).
- După B0, doar cu Adrian de față: proba tinygrad (partea P) — jurnalul ei se compară cu GSP-ul fals.

## Ce oferă proiectul celorlalți
- `cyber-universe`: crate-urile no_std `gpu-core`, `gpu-pci`, `nvidia-ga104`, `gpu-compute`, `gpu-sim` (teste), MIT. os-191 e fixat pe `dac2e32`: rămâne valabil.
  Nou după `dac2e32`, **doar adăugări**: crate-ul `nvidia-rm570` (date generate din antetele NVIDIA, MIT, fără dependențe) de care `nvidia-ga104` depinde acum;
  `nvidia-ga104::qmd`, `gsp::registry`; în `gpu-sim`: procesorul de comenzi și cititorul jurnalului.
  **Sesiunea 7, tot doar adăugări:** `Mmio::is_simulation` (metodă nouă cu valoare implicită `false` — implementările OS-ului rămân valabile; nu o
  suprascrieți pentru placa reală); `gsp::falcon`, `gsp::sequencer` (cer permisul `hw-write` pe placa reală — OS-ul nu le cheamă), `fw_hdr`;
  în `gpu-compute`: `fma_f32`, `ftz`, `add_ftz`, `matmul_fma(_ftz)`. Detalii: `integration/cyber-universe/UTILIZARE.md`.
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
