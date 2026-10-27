# Stare: Cyber-GPU (`cyber-gpu`)

**Actualizat:** 2026-10-27 08:50 (ora României) · **de:** sesiunea Cyber-GPU 8 (cloud, fără placă)

## Acum
- **Nimic nu s-a testat pe RTX 3070 Ti.** Tot ce „merge” e verificat doar pe calculator (SIMULARE, compilare sau comparație cu antetele NVIDIA).
  Codul care ar scrie în placă (pornirea GSP) stă în spatele opțiunii `hw-write`, oprită implicit; nu a rulat pe placă.
- C-18 și C-20 gata (de ieri). Azi, pașii „fără placă” care urmau:
  - **Primul mesaj către GSP („informațiile despre sistem”, 928 de octeți):** structura e luată automat din antetul NVIDIA 570.144 (MIT),
    iar valorile (unde stau BAR-urile, ce placă e, mărimea paginii) sunt completate ca în driverul NVIDIA. Ce nu avem (ACPI, virtualizare)
    rămâne 0 = „absent”. Pornirea simulată cap-coadă trimite acum mesajele reale, nu umplutură. Că placa le acceptă: de văzut abia pe placă.
  - **Înmulțirea de matrice, treapta 3** (bucăți de 16×16 ținute în memoria rapidă a plăcii): compilată cu Mesa NAK, lansată în model,
    rezultat identic bit cu bit cu calculul de control (inclusiv pe margini și la „−0”). Descrierea lansării (QMD) are acum și memoria partajată.
- 184 de teste trec; CI verde (rularea 33; 34–35 verificate la final).

## Urmează
- Fără placă: treapta 4 matmul; „golden image” (pasul de după pornirea GSP) în simulare; încărcătorul ucode-ului (în spatele `hw-write`).
- Fereastra pe workstation (~30 min): citiri I0–I3 + FWSEC + fișierele de pe stick, **0 scrieri** (`docs/TEST_MATRIX.md` B0).
- După B0, doar cu Adrian de față: proba tinygrad (partea P) — jurnalul ei se compară cu GSP-ul fals și cu QMD-ul nostru.

## Ce oferă proiectul celorlalți
- `cyber-universe`: crate-urile no_std `gpu-core`, `gpu-pci`, `nvidia-ga104`, `gpu-compute`, `gpu-sim` (teste), MIT. os-191 e fixat pe `dac2e32`: rămâne valabil.
  După `dac2e32`, **doar adăugări** (nimic șters sau redenumit): `nvidia-rm570` (date din antetele NVIDIA, acum și `sysinfo`), `qmd`
  (+ `encode_with_shared`), `gsp::registry`, `gsp::sysinfo`, `gsp::falcon`/`sequencer` (cer `hw-write` pe placa reală — OS-ul nu le cheamă),
  `fw_hdr`, `Mmio::is_simulation` (valoare implicită); în `gpu-compute`: `fma_f32`, `ftz`, `matmul_fma(_ftz)`; în `gpu-sim`: procesorul de
  comenzi (+ `register_program_with_needs`) și GSP-ul fals. Detalii: `integration/cyber-universe/UTILIZARE.md`.
- `kronos` / K6-CPU: operatorii lui Kronos pe procesor, neschimbați.

## De ce are nevoie de la ceilalți
- De la `kronos`: workstation-ul, doar în fereastra aprobată de Adrian.

## Blocaje / nevoie de Adrian
- **Fereastra pe workstation (~30 min):** lista în `docs/TEST_MATRIX.md` partea B0 (Release-ul OS os-191 e gata).
- **Înainte de fereastră, fișierele firmware pe stick:** din https://gitlab.com/kernel-firmware/linux-firmware, folderul `nvidia/ga102/gsp/`,
  cele 4 fișiere `*-570.144.bin` în `firmware\nvidia\ga102\gsp\` pe stick (+ `LICENCE.nvidia` în `firmware\`); sumele în
  `docs/COMPATIBILITATE_FIRMWARE.md`. **Nu le urca nicăieri.**
- **Opțional, pentru proba tinygrad (partea P, scrie în placă, doar cu tine de față, după B0):** un al doilea stick cu Ubuntu 24.04 live și laptopul pentru SSH.
- Tag-ul `stabil-2026-10-23` (tot 403 din cloud; nu blochează nimic): GitHub → cyber-gpu → Releases → „Draft a new release” → tag `stabil-2026-10-23`, Target commit `41e44ba` → pre-release → Publish.
