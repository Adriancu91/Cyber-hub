# Stare: Cyber-GPU (`cyber-gpu`)

**Actualizat:** 2026-10-28 01:45 (ora României) · **de:** sesiunea Cyber-GPU 11 (cloud, fără placă)

## Acum
- **Nimic nu s-a testat pe RTX 3070 Ti.** Tot ce „merge” e verificat doar pe calculator (SIMULARE sau comparație cu antetele NVIDIA).
  Codul care ar scrie în placă stă în spatele opțiunii `hw-write`, oprită implicit; nu a rulat pe placă.
- C-18 și C-20 gata. În noaptea asta, un pas „fără placă”:
  - **I9b — „harta” plăcii scrisă în memoria ei:** driverul scrie tabelele de pagini în memoria video printr-o fereastră de 1 MiB a plăcii,
    recitește fiecare cuvânt și apoi îi spune plăcii să-și golească memoria rapidă de adrese (TLB). Atinge doar 4 registre, toate în jurnal;
    zona ecranului și zona firmware-ului sunt protejate (refuzate înainte de orice acces). Verificat pe un model scris separat, cu 3 defecte
    simulate (scriere pierdută, fereastră blocată, golire care nu se termină) — toate raportate, niciunul ascuns.
  - **Rândul „ecran:” din os-192 (C-26, mulțumim OS-ului)** se transformă acum automat în zona din memoria plăcii pe care driverul n-o atinge.
- 220 de teste trec; CI verde (rulările 43–44; 45–46 verificate la final).

## Urmează
- Fără placă: încărcătorul ucode-ului prin DMA (în spatele `hw-write`); treapta 6 matmul; `SET_PAGE_DIRECTORY` pentru canal.
  După asta, aproape tot ce a rămas (I0–I10 reale) cere placa.
- Fereastra pe workstation (~30 min, **os-192**): citiri I0–I3 + FWSEC + fișierele de pe stick + poza rândului „ecran:” din `hw`, **0 scrieri**
  (`docs/TEST_MATRIX.md` B0).
- După B0, doar cu Adrian de față: proba tinygrad (partea P).

## Ce oferă proiectul celorlalți
- `cyber-universe`: crate-urile no_std `gpu-core`, `gpu-pci`, `nvidia-ga104`, `gpu-compute`, `gpu-sim` (teste), MIT. Fixarea pe `dac2e32` rămâne valabilă.
  După `dac2e32`, **doar adăugări**: `nvidia-rm570`, `qmd`, `gsp::{registry,sysinfo,rmapi,golden,falcon,sequencer}`, `fw_hdr`, `mmu`, **`vram_window`** (nou;
  scrie în placă, cere `hw-write` — OS-ul nu-l cheamă; `screen_vram_range` e doar aritmetică), `Mmio::is_simulation`; în `gpu-compute`: `fma_f32`, `ftz`,
  `matmul_fma(_ftz)`; în `gpu-sim`: procesorul de comenzi, GSP/RM fals, VRAM simulată, fereastra simulată (`pramin`). La o nouă fixare: `nvidia-ga104`
  depinde și de `gpu-memory` (același repo). Detalii: `integration/cyber-universe/UTILIZARE.md`.
- Pentru o fixare mai clară (cererea OS-ului): ramura `main` n-o creăm noi (regula sesiunii); tag-ul nu se poate urca din cloud (403) — vezi blocajele.
- `kronos` / K6-CPU: operatorii lui Kronos pe procesor, neschimbați.

## De ce are nevoie de la ceilalți
- De la `kronos`: workstation-ul, doar în fereastra aprobată de Adrian.
- De la `cyber-universe`: nimic nou (rândul „ecran:” din C-26 e exact ce trebuia).

## Blocaje / nevoie de Adrian
- **Fereastra pe workstation (~30 min), cu os-192:** lista în `docs/TEST_MATRIX.md` partea B0; 0 scrieri în placă.
- **Înainte de fereastră, fișierele firmware pe stick:** din https://gitlab.com/kernel-firmware/linux-firmware, folderul `nvidia/ga102/gsp/`,
  cele 4 fișiere `*-570.144.bin` în `firmware\nvidia\ga102\gsp\` pe stick (+ `LICENCE.nvidia` în `firmware\`); sumele în
  `docs/COMPATIBILITATE_FIRMWARE.md`. **Nu le urca nicăieri.**
- **Opțional, pentru proba tinygrad (partea P, scrie în placă, doar cu tine de față, după B0):** un al doilea stick cu Ubuntu 24.04 live și laptopul pentru SSH.
- Tag-ul `stabil-2026-10-23` (tot 403 din cloud; nu blochează nimic): GitHub → cyber-gpu → Releases → „Draft a new release” → tag `stabil-2026-10-23`, Target commit `41e44ba` → pre-release → Publish.
- Fără fereastra pe workstation, pașii „fără placă” se termină curând (după încărcătorul DMA și treptele matmul).
