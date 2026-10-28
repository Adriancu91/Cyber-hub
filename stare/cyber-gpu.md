# Stare: Cyber-GPU (`cyber-gpu`)

**Actualizat:** 2026-10-28 19:50 (ora României) · **de:** sesiunea Cyber-GPU 14 (cloud, fără placă)

## Acum
- **C-33 gata:** codul cyber-gpu e **proprietar** („toate drepturile rezervate”, fișierul `LICENSE`) de la commit-ul de după `8313973`;
  versiunile până la `8313973` inclusiv rămân MIT. Fișierele generate din antetele NVIDIA rămân MIT NVIDIA. Firmware-ul NVIDIA nu-l distribuim
  deloc: Adrian îl descarcă singur (notat și în `RESEARCH_I4_I8.md` §5.1). Codul driverului nu s-a schimbat.
- **C-34 gata:** copia pentru sesiunea OS e la zi: `integrare/cyber-gpu/snapshot/cyber-gpu.bundle`, vârf `9da10f0` (verificată + clonare de probă cu teste verzi).
- Din sesiunea 13 (pe placa reală): I0, I1, I2 trec; I3 a picat la imaginea „NV”, reparat **doar în SIMULARE** (C-30) — de verificat la fereastra următoare.
- 243 de teste trec **în sesiune**. **CI-ul GitHub nu mai pornește** de când repo-ul e privat (joburile pică în 3 s, fără jurnal: fără minute gratuite).
  Conform C-32 nu se repară prin plată. Nimic nu scrie în placă.

## Urmează
- Sesiunea OS: C-31 (`gpu vbios --detalii`), din bundle-ul din hub (orice vârf ≥ `4538f90`).
- Fereastra următoare pe workstation: `gpu vbios` + `gpu vbios --detalii` (poze). Dacă I3 trece: I3b (FWSEC) și fișierele de pe stick (I4).
- Fără placă: treapta 6 matmul (cere construirea compilatorului Mesa NAK; în sesiunea asta instalarea uneltelor a fost refuzată de permisiuni); `SET_PAGE_DIRECTORY`.

## Ce oferă proiectul celorlalți
- `cyber-universe`: crate-urile no_std `gpu-core`, `gpu-pci`, `nvidia-ga104`, `gpu-compute`, `gpu-sim` (teste). **Licența: proprietară** de la
  commit-ul de după `8313973` (până atunci MIT); în `Cargo.toml` `license` → `license-file` (doar metadate). Codul și interfața publică: neschimbate
  față de `4538f90`, doar adăugări față de `dac2e32`. Diagnosticul VBIOS: `nvidia_ga104::vbios_diag::diagnose` + `VbiosDiag::lines()`
  (`integration/cyber-universe/C-31_gpu-vbios-detalii.md`). Sursa: bundle-ul din hub (repo-ul e privat). Detalii: `integration/cyber-universe/UTILIZARE.md`.
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
- **De decis (fără grabă):** testele automate GitHub nu mai rulează cu repo-ul privat. Merge și așa (testele rulează în fiecare sesiune), dar
  fără a doua verificare independentă.
- **Opțional, pentru proba tinygrad (scrie în placă, doar cu tine de față, după I3/I4):** un al doilea stick cu Ubuntu 24.04 live și laptopul pentru SSH.
- Tag-ul `stabil-2026-10-23` (tot 403 din cloud; nu blochează nimic): GitHub → cyber-gpu → Releases → „Draft a new release” → tag `stabil-2026-10-23`, Target commit `41e44ba` → pre-release → Publish.
