# Stare: Cyber-GPU (`cyber-gpu`)

**Actualizat:** 2026-10-26 17:45 (ora României) · **de:** sesiunea Cyber-GPU (cloud, fără placă)

## Acum
- **Nimic nu s-a testat pe RTX 3070 Ti.** Tot ce „merge” e verificat doar pe calculator (SIMULARE sau compilare). Niciun program pe GPU. Nicio linie de cod nu scrie în placă.
- **C-18 făcut:** deciziile tale (firmware NVIDIA 570.144 separat pe stick, compilator Mesa NAK) sunt notate și aplicate.
  - Tabelul unic `docs/COMPATIBILITATE_FIRMWARE.md`: fiecare pas I0–I10, sursa, versiunea, fișierul de cod, testul și starea (confirmat / parțial / necunoscut / SIMULARE).
  - **I4:** driverul citește cele 4 fișiere firmware de pe stick și le verifică mărimea și suma SHA-256 (sumele luate din fișierele oficiale; fișierele nu sunt în niciun repo).
  - **I5–I8, doar în SIMULARE:** tot ce îi dăm GSP-ului la pornire (descrierea memoriei, cozile de mesaje, mesajele RPC cu suma de control), testat cu un „GSP simulat”.
  - **Primul program GPU** (adunarea a 64 de numere) **compilat** cu Mesa NAK pentru placa ta, fără placă: 240 de octeți. **Nerulat** — rularea vine după I8–I10, pe placă.
- 134 de teste trec; CI verde (rulările 16–18; o rulare roșie din cauza unei reguli noi din Rust 1.99, reparată).

## Urmează
- **C-20** (comanda nouă de la 18:10, după studiul open-source) — văzută, încă nepreluată: o ia sesiunea următoare (B: antete generate, C: tinygrad ca hartă, D: GSP fals în `gpu-sim`, E: matmul cu NAK, A: doar pregătirea probei tinygrad). Primele diferențe față de codul de azi sunt notate în `docs/COMPATIBILITATE_FIRMWARE.md` („De verificat”).
- Fereastra pe workstation (27–28 oct, ~30 min, Kronos oprit): citiri I0–I3 + FWSEC + verificarea fișierelor de pe stick. **0 scrieri în placă.** Lista: `docs/TEST_MATRIX.md` partea B0.
- Fără placă: antetele fișierelor bootloader/booter (lipsesc pentru WPR meta), conținutul mesajelor SetSystemInfo/SetRegistry, registrele falcon pentru I6–I7 (scrise, dar oprite).

## Ce oferă proiectul celorlalți
- `cyber-universe`: crate-urile no_std `gpu-core`, `gpu-pci`, `nvidia-ga104`, `gpu-compute`, `gpu-sim` (teste), MIT, fără dependențe externe.
  **Pentru C-19: nu există ramura `main` la noi** — fixarea se face pe commit-ul `dac2e32` (ramura `g0-g2-fundatie`, CI verde). Față de `41e44ba`
  s-a doar adăugat; o singură valoare schimbată (`firmware::GSP_VERSION` = "570.144", OS-ul n-o folosește); `gpu plan` va arăta oprirea la I5.
  Propunere (nu e cerută de C-19): comanda `gpu firmware` (doar citire, verifică fișierele de pe stick) — `integration/cyber-universe/I4_gpu-firmware.md`.
- `kronos` / K6-CPU: operatorii lui Kronos pe procesor (matmul bf16, împărțire pe nuclee), neschimbați.

## De ce are nevoie de la ceilalți
- De la `cyber-universe`: Release-ul C-19 (`gpu gfw`, `gpu vbios`) pentru fereastră; opțional `gpu firmware`.
- De la `kronos`: workstation-ul, doar în fereastra aprobată de Adrian.

## Blocaje / nevoie de Adrian
- **Fereastra pe workstation (27 sau 28 oct, ~30 min):** lista în `docs/TEST_MATRIX.md` partea B0.
- **Înainte de fereastră, fișierele firmware pe stick:** din https://gitlab.com/kernel-firmware/linux-firmware, folderul `nvidia/ga102/gsp/`,
  cele 4 fișiere `*-570.144.bin` în `firmware\nvidia\ga102\gsp\` pe stick (+ `LICENCE.nvidia` în `firmware\`); sumele de verificat sunt în
  `docs/COMPATIBILITATE_FIRMWARE.md` (PowerShell: `Get-FileHash *.bin -Algorithm SHA256`). **Nu le urca nicăieri.**
- Tag-ul `stabil-2026-10-23` (tot 403 din cloud; nu blochează nimic): GitHub → cyber-gpu → Releases → „Draft a new release” → tag `stabil-2026-10-23`, Target commit `41e44ba` → pre-release → Publish.
