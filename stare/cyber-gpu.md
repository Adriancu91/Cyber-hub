# Stare: Cyber-GPU (`cyber-gpu`)

**Actualizat:** 2026-10-28 13:50 (ora României) · **de:** sesiunea Cyber-GPU 13 (cloud, fără placă)

## Acum
- **Prima dată pe placa reală (fereastra de azi, os-195, doar citire): I0, I1, I2 trec pe RTX 3070 Ti** (cipul recunoscut, GFW gata în 3 µs, 0 scrieri).
  **I3 (VBIOS) a picat** la `0x24600`: acolo imaginea începe cu „NV” (`0x4e56`) în loc de `0xAA55`.
- **C-30 gata (în SIMULARE):**
  - **Diagnosticul VBIOS** (doar citire): listează rând cu rând fiecare imagine (offset, semnătură, câmpurile PCIR/NPDE), rupturile cu
    primii 16 octeți, ce mai e după ultima imagine; fără conținutul imaginilor; rezumat cu „0 scrieri”.
  - **Parserul acceptă imaginile „NV”**, cum fac nouveau (MIT) și nova-core; orice altă semnătură e tot refuzată. Pe o imagine sintetică
    făcută după placă, I3 trece și FWSEC e găsit. **Pe placa reală: netestat încă.**
- Ecranul firmware-ului e la începutul BAR1 (`0xe0000000`) → primii ~8,5 MiB din memoria plăcii sunt protejați în driver (test cu valorile reale).
- 243 de teste trec; CI verde (o rulare roșie pe drum: format uitat, reparat imediat). Nimic nu scrie în placă.

## Urmează
- Sesiunea OS: C-31 (`gpu vbios --detalii`), cu fixarea pe `cyber-gpu` `4538f90` sau mai nou — OS-ul se construiește cu ea (verificat).
- Fereastra următoare pe workstation: `gpu vbios` + `gpu vbios --detalii` (poze). Dacă I3 trece: I3b (FWSEC) și fișierele de pe stick (I4).
- Fără placă: treapta 6 matmul; `SET_PAGE_DIRECTORY` pentru canal.

## Ce oferă proiectul celorlalți
- `cyber-universe`: crate-urile no_std `gpu-core`, `gpu-pci`, `nvidia-ga104`, `gpu-compute`, `gpu-sim` (teste), MIT. Fixarea pe `dac2e32` rămâne valabilă.
  După `dac2e32`, **doar adăugări**; nou azi: **`nvidia_ga104::vbios_diag::diagnose` + `VbiosDiag::lines()`** (pentru `gpu vbios --detalii`, C-31),
  `vbios::read_layout` acceptă imaginile „NV”, `gpu_sim::rom::asus_like_chain()` pentru `--sim`. Instrucțiuni: `integration/cyber-universe/C-31_gpu-vbios-detalii.md`.
  La o nouă fixare `nvidia-ga104` depinde și de `gpu-memory` și `nvidia-rm570` (același repo). Detalii: `integration/cyber-universe/UTILIZARE.md`.
- Pentru mai târziu (doar în fereastra cu Adrian): pornirea reală a GSP va cere de la OS o zonă de RAM contiguă (sub 2^49) și Bus Master pentru placă.
- `kronos` / K6-CPU: operatorii lui Kronos pe procesor, neschimbați.

## De ce are nevoie de la ceilalți
- De la `cyber-universe`: C-31 (afișarea diagnosticului în OS + Release pentru fereastră, împreună cu C-29).
- De la `kronos`: workstation-ul, doar în fereastra aprobată de Adrian.

## Blocaje / nevoie de Adrian
- **Fereastra următoare pe workstation (~15 min, cu Release-ul care are C-31):** `gpu vbios` și `gpu vbios --detalii` → poze cu toate rândurile; 0 scrieri.
- **Înainte de fereastră, fișierele firmware pe stick:** din https://gitlab.com/kernel-firmware/linux-firmware, folderul `nvidia/ga102/gsp/`,
  cele 4 fișiere `*-570.144.bin` în `firmware\nvidia\ga102\gsp\` pe stick (+ `LICENCE.nvidia` în `firmware\`); sumele în
  `docs/COMPATIBILITATE_FIRMWARE.md`. **Nu le urca nicăieri.**
- **Opțional, pentru proba tinygrad (scrie în placă, doar cu tine de față, după I3/I4):** un al doilea stick cu Ubuntu 24.04 live și laptopul pentru SSH.
- Tag-ul `stabil-2026-10-23` (tot 403 din cloud; nu blochează nimic): GitHub → cyber-gpu → Releases → „Draft a new release” → tag `stabil-2026-10-23`, Target commit `41e44ba` → pre-release → Publish.
