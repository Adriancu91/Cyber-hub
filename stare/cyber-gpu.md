# Stare: Cyber-GPU (`cyber-gpu`)

**Actualizat:** 2026-10-27 13:55 (ora României) · **de:** sesiunea Cyber-GPU 9 (cloud, fără placă)

## Acum
- **Nimic nu s-a testat pe RTX 3070 Ti.** Tot ce „merge” e verificat doar pe calculator (SIMULARE, compilare sau comparație cu antetele NVIDIA).
  Codul care ar scrie în placă (pornirea GSP) stă în spatele opțiunii `hw-write`, oprită implicit; nu a rulat pe placă.
- C-18 și C-20 gata. Azi, pașii „fără placă” care urmau:
  - **„Golden image” (pasul de după pornirea GSP):** driverul își face primul „client” la GSP: dispozitiv, spațiu de adrese, un canal de comenzi,
    bufferele de context ale motorului de calcul (promovate ca model pentru toate canalele de mai târziu), apoi obiectul de calcul.
    Structurile mesajelor sunt luate automat din antetele NVIDIA 570.144 (MIT); ordinea și câteva valori găsite prin încercări sunt după tinygrad
    (marcate „DEDUS”). Secvența rulează cap-coadă prin cozile reale către un „RM fals” scris separat, care o acceptă; refuzurile lui se văd ca erori.
  - **Înmulțirea de matrice, treapta 4** (fiecare fir calculează 8 rezultate, plăci în memoria rapidă): compilată cu Mesa NAK, lansată în model,
    identică bit cu bit cu calculul de control.
- 196 de teste trec; CI verde (rulările 36–37).

## Urmează
- Fără placă: încărcătorul ucode-ului prin DMA (în spatele `hw-write`); alocatorul de memorie video + tabelele de pagini (I9); treapta 5 matmul.
- Fereastra pe workstation (~30 min): citiri I0–I3 + FWSEC + fișierele de pe stick, **0 scrieri** (`docs/TEST_MATRIX.md` B0).
- După B0, doar cu Adrian de față: proba tinygrad (partea P) — jurnalul ei se compară cu GSP-ul fals, cu RM-ul fals și cu QMD-ul nostru.

## Ce oferă proiectul celorlalți
- `cyber-universe`: crate-urile no_std `gpu-core`, `gpu-pci`, `nvidia-ga104`, `gpu-compute`, `gpu-sim` (teste), MIT. os-191 e fixat pe `dac2e32`: rămâne valabil.
  După `dac2e32`, **doar adăugări** (nimic șters sau redenumit): `nvidia-rm570` (date din antetele NVIDIA: `sysinfo`, acum și `rmapi`), `qmd`
  (+ `encode_with_shared`), `gsp::registry`, `gsp::sysinfo`, `gsp::rmapi`, `gsp::golden`, `gsp::falcon`/`sequencer` (cer `hw-write` pe placa reală —
  OS-ul nu le cheamă), `fw_hdr`, `Mmio::is_simulation` (valoare implicită); în `gpu-compute`: `fma_f32`, `ftz`, `matmul_fma(_ftz)`; în `gpu-sim`:
  procesorul de comenzi (+ treptele matmul 1–4), GSP-ul fals și RM-ul fals. Detalii: `integration/cyber-universe/UTILIZARE.md`.
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
- Fără fereastra pe workstation, pașii rămași „fără placă” se împuținează: după I9 și treptele matmul, restul (I0–I10 reale) cere placa.
