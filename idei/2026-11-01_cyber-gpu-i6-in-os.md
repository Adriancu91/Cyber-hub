# Cyber-GPU: primele scrieri în placă direct din Cyber Universe (I6), cu jurnal complet

- **Propus de:** `cyber-gpu` · **Data:** 2026-11-01
- **Proiecte implicate:** `cyber-gpu`, `cyber-universe`
- **Stare:** propus

## Ideea (pe înțelesul lui Adrian, 3–6 rânduri)
Toate verificările de citire au trecut (I0–I4). Cum pe placa reală rulează doar Cyber Universe (decizia din 1 nov 12:00), prima scriere se
face cu driverul nostru, din OS. Propunem trei lucruri în OS: (1) `gpu pregatire-i6` — **doar citește** ce îi trebuie lui I6 (fără risc);
(2) jurnalul fiecărei citiri/scrieri pe stick, cu ora, în clipa în care se face; (3) `gpu i6 --scrie` — doar în stick-ul de test, cu
confirmare „DA”: Bus Master pornit, FWSEC (programul semnat NVIDIA din VBIOS) încărcat în placă, Bus Master oprit la loc.

## Ce ar face fiecare proiect
- `cyber-gpu`: gata (doar SIMULARE) — `fuse`, `i6_check`, `i6_log`, `fwsec::read_ucode_and_signature`, `gpu_pci::bus_master`,
  `Journal::with_sink` (commit `d879742`); planul `docs/FEREASTRA_C-49.md`; schița pentru OS `integration/cyber-universe/C-49_gpu-pregatire-i6.md`.
- `cyber-universe` (doar cu „da”-ul centrului de comandă): fixarea `cyber-gpu` ≥ `d879742`; fereastra BAR0 doar-citire de 16 MiB;
  `gpu pregatire-i6`; jurnalul pe loc; apoi `gpu i6 --scrie` (zonă de RAM pentru DMA sub 4 GiB, fereastra BAR0 cu scriere doar pentru comanda asta).

## Cost și riscuri
- (1) și (2): mici, fără nicio scriere în placă.
- (3): 1 scriere PCI (Bus Master) + 18 registre în fereastra GSP + 1 scriere PCI la loc. VBIOS-ul nu se poate scrie; siguranțele doar se
  citesc; totul se șterge la oprirea completă. Riscul real: ecranul se stinge/blocare → oprire completă (cablul scos 30 s).

## Decizia lui Adrian
- 

## Discuție
- 2026-11-01 `cyber-gpu`: actualizat după C-51 (fără tinygrad); pașii ferestrei, cu dovada recitită la fiecare, în `docs/FEREASTRA_C-49.md`.
