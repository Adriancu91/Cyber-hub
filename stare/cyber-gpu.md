# Stare: Cyber-GPU (`cyber-gpu`)

**Actualizat:** 2026-10-28 07:50 (ora României) · **de:** sesiunea Cyber-GPU 12 (cloud, fără placă)

## Acum
- **Nimic nu s-a testat pe RTX 3070 Ti.** Tot ce „merge” e verificat doar pe calculator (SIMULARE, cu imagini sintetice — niciun fișier
  firmware NVIDIA real). Codul care ar scrie în placă stă în spatele opțiunii `hw-write`, oprită implicit; nu a rulat pe placă.
- C-18 și C-20 gata. Azi dimineață, pasul „fără placă” care lipsea la pornirea plăcii:
  - **Încărcătorul programelor semnate NVIDIA (I6/I7):** driverul pune FWSEC (din VBIOS) și Booter (de pe stick) în micro-procesoarele
    plăcii prin DMA și îi spune „ROM-ului de pornire” unde e semnătura — după sursa NVIDIA 570.144 (MIT). Totul se verifică înainte de
    prima scriere; atinge doar registrele GSP/SEC2, toate în jurnal.
  - **Comanda FRTS pentru FWSEC:** driverul îi spune lui FWSEC unde să facă zona protejată (1 MiB din memoria plăcii).
  - Verificat pe un model cu un motor DMA și un „ROM” simulate: pornirea FWSEC → Booter merge cap-coadă; 12 greșeli plantate intenționat
    în driver au fost toate prinse.
- 229 de teste trec; CI verde.

## Urmează
- Fără placă au mai rămas puține: treapta 6 matmul; `SET_PAGE_DIRECTORY` pentru canal. Aproape tot restul (I0–I10 reale) cere placa.
- Fereastra pe workstation (~30 min, **os-192 sau mai nou**): citiri I0–I3 + FWSEC + fișierele de pe stick + poza rândului „ecran:” din `hw`,
  **0 scrieri** (`docs/TEST_MATRIX.md` B0).
- După B0, doar cu Adrian de față: proba tinygrad (partea P).

## Ce oferă proiectul celorlalți
- `cyber-universe`: crate-urile no_std `gpu-core`, `gpu-pci`, `nvidia-ga104`, `gpu-compute`, `gpu-sim` (teste), MIT. Fixarea pe `dac2e32` rămâne valabilă.
  După `dac2e32`, **doar adăugări**: `nvidia-rm570`, `qmd`, `gsp::{registry,sysinfo,rmapi,golden,falcon,sequencer}`, **`gsp::hs_load`** (nou; scrie în
  placă, cere `hw-write` — OS-ul nu-l cheamă), `fw_hdr`, `mmu`, `vram_window`, `Mmio::is_simulation`; în `gpu-compute`: `fma_f32`, `ftz`, `matmul_fma(_ftz)`;
  în `gpu-sim`: procesorul de comenzi, GSP/RM fals (acum și cu motor DMA + „ROM” simulat), VRAM simulată, fereastra simulată. La o nouă fixare:
  `nvidia-ga104` depinde și de `gpu-memory` (același repo). Detalii: `integration/cyber-universe/UTILIZARE.md`.
- Pentru mai târziu (doar în fereastra cu Adrian, nu acum): pornirea reală a GSP va cere de la OS o zonă de RAM contiguă (adresă sub 2^49) și
  Bus Master pentru placă — RM 570.144 citește programele semnate din RAM, nu din memoria plăcii.
- `kronos` / K6-CPU: operatorii lui Kronos pe procesor, neschimbați.

## De ce are nevoie de la ceilalți
- De la `kronos`: workstation-ul, doar în fereastra aprobată de Adrian.
- De la `cyber-universe`: nimic nou acum.

## Blocaje / nevoie de Adrian
- **Fereastra pe workstation (~30 min), cu os-192 sau mai nou:** lista în `docs/TEST_MATRIX.md` partea B0; 0 scrieri în placă.
- **Înainte de fereastră, fișierele firmware pe stick:** din https://gitlab.com/kernel-firmware/linux-firmware, folderul `nvidia/ga102/gsp/`,
  cele 4 fișiere `*-570.144.bin` în `firmware\nvidia\ga102\gsp\` pe stick (+ `LICENCE.nvidia` în `firmware\`); sumele în
  `docs/COMPATIBILITATE_FIRMWARE.md`. **Nu le urca nicăieri.**
- **Opțional, pentru proba tinygrad (partea P, scrie în placă, doar cu tine de față, după B0):** un al doilea stick cu Ubuntu 24.04 live și laptopul pentru SSH.
- Tag-ul `stabil-2026-10-23` (tot 403 din cloud; nu blochează nimic): GitHub → cyber-gpu → Releases → „Draft a new release” → tag `stabil-2026-10-23`, Target commit `41e44ba` → pre-release → Publish.
- Fără fereastra pe workstation, pașii „fără placă” sunt aproape terminați.
