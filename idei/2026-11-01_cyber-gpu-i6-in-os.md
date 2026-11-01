# Cyber-GPU: verificarea I6 „doar citire” în OS acum, prima scriere în placă mai târziu

- **Propus de:** `cyber-gpu` · **Data:** 2026-11-01
- **Proiecte implicate:** `cyber-gpu`, `cyber-universe`
- **Stare:** propus

## Ideea (pe înțelesul lui Adrian, 3–6 rânduri)
Toate verificările de citire ale plăcii video au trecut (I0–I4). Următorul pas al driverului nostru (I6) ar fi prima scriere în placă.
Ca să fim siguri înainte, propunem o comandă nouă în OS, `gpu pregatire-i6`, care **doar citește** ce îi trebuie lui I6 (ce semnătură
acceptă placa, cât VRAM are, dacă zona protejată e coborâtă). Se poate rula în fereastra următoare, înaintea probei tinygrad, fără niciun risc.
Abia după proba tinygrad, într-o fereastră separată, OS-ul ar primi și partea care scrie (Bus Master + FWSEC), cu Adrian de față.

## Ce ar face fiecare proiect
- `cyber-gpu`: gata — `nvidia_ga104::{fuse, i6_check}` (commit `d6de57e`), planul `docs/FEREASTRA_C-49.md`, schița pentru OS
  `integration/cyber-universe/C-49_gpu-pregatire-i6.md`.
- `cyber-universe` (doar cu „da”-ul lui Adrian): fixarea `cyber-gpu` ≥ `d6de57e`; fereastra BAR0 doar-citire de 16 MiB în loc de 4 MiB;
  comanda `gpu pregatire-i6` (~40 de rânduri după schiță). Mai târziu, separat: Bus Master + zona de RAM pentru DMA + comanda care scrie.

## Cost și riscuri
- Partea „doar citire”: mică (o comandă, o fereastră mai mare, tot fără drept de scriere); nu atinge placa în scriere.
- Partea care scrie (după tinygrad): 18 registre în fereastra GSP + 1 scriere PCI; nu poate scrie VBIOS-ul; revenirea = oprire completă.

## Decizia lui Adrian
- 

## Discuție
- 2026-11-01 `cyber-gpu`: recomand întâi proba tinygrad (jurnalul de aur), apoi I6 cu driverul nostru — motivele în `docs/FEREASTRA_C-49.md`.
