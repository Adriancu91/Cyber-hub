# Comenzile `gpu firmware` și `gpu fwsec` în OS (doar citire), pentru fereastra C-36

- **Propus de:** `cyber-gpu` · **Data:** 2026-10-28
- **Proiecte implicate:** `cyber-universe`, `cyber-gpu`
- **Stare:** propus

## Ideea (pe înțelesul lui Adrian, 3–6 rânduri)
La fereastra de pe workstation (C-36, posibil 29 oct), după `gpu vbios`, vrem să vedem pe ecranul OS-ului două lucruri, fără nicio scriere
în placa video: (1) `gpu fwsec` — unde se află în placa video programul FWSEC (pasul I3b); (2) `gpu firmware` — dacă cele 4 fișiere
firmware 570.144 de pe stick sunt exact cele oficiale și dacă driverul nostru le înțelege antetul (pasul I4; nu atinge deloc placa).
Fără ele, la pasul 2 rămâne doar verificarea sumelor pe Windows (merge, dar nu verifică și codul nostru).

## Ce ar face fiecare proiect
- `cyber-gpu` (gata, 28 oct, sesiunea 15): `nvidia_ga104::fw_check` + `FwsecLocation::lines()` + fișiere de probă `gpu_sim::fw_stick`,
  commit `2c9c90c` (ramura `g0-g2-fundatie`, în copia din hub `integrare/cyber-gpu/snapshot/`); schița de cod pentru OS:
  `integration/cyber-universe/C-36_gpu-firmware-fwsec.md` din repo-ul cyber-gpu (o compilare de probă într-o copie a OS-ului a trecut,
  build normal și `test-gpu-sim`). Față de fixarea actuală `8313973`: doar adăugări.
- `cyber-universe` (de făcut, dacă e aprobat): mută fixarea cyber-gpu pe `2c9c90c` sau mai nou; adaugă `gpu fwsec [--sim]` și
  `gpu firmware [--sim]` (rândurile vin gata din bibliotecă) + 2 rânduri în `gpu plan`; teste QEMU: `--sim` → `criteriul I3b: TRECE` /
  `criteriul I4: TRECE (fisiere oficiale 4/4, antete citite 4/4)`; fără `--sim` în QEMU → 4 × „LIPSESTE”. Apoi stick nou prin hub (C-35).

## Cost și riscuri
- OS: ~1 oră (două comenzi mici + teste + stick). Risc pentru placă: niciunul (`gpu firmware` nu atinge placa; `gpu fwsec` citește
  aceeași fereastră PROM ca `gpu vbios`). Fișierele firmware nu intră în repo, în teste sau în arhiva stick-ului (le pune Adrian).
- Dacă nu se face până la fereastră: pașii din `cyber-gpu/docs/FEREASTRA_C-36.md` au varianta B (fără aceste comenzi).

## Decizia lui Adrian
- (completează Adrian sau centrul de comandă)

## Discuție
- 2026-10-28 `cyber-gpu`: testat doar în SIMULARE; nimic din asta nu a rulat pe placă sau pe fișierele reale.
