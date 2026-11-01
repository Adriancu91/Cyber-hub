# Cyber-GPU: turul de citire pentru bucla automată (`gpu tur`) și pașii în lanț la fereastră (`gpu lant`)

- **Propus de:** `cyber-gpu` · **Data:** 2026-11-01
- **Proiecte implicate:** `cyber-gpu`, `cyber-universe`
- **Stare:** propus (din C-54)

## Ideea (pe înțelesul lui Adrian, 3–6 rânduri)
Pentru bucla automată (fără Adrian): o comandă OS `gpu tur` care **doar citește** din placă tot ce am citit deja în siguranță (identitatea,
pornirea firmware-ului plăcii, așezarea VBIOS, FWSEC, pregătirea I6) și scrie rezultatul în raport, rând cu rând. Sesiunea Cyber-GPU compară
apoi raportul cu simularea și repară simularea unde greșește. Pentru fereastra cu Adrian: `gpu lant` face pașii unul după altul
(pregătire → Bus Master → I6 → I7 …) și se oprește singur la primul eșec, punând placa la loc (Bus Master oprit).

## Ce ar face fiecare proiect
- `cyber-gpu`: gata (doar SIMULARE) — `nvidia_ga104::{read_tour, chain, board_compare}`, `gpu_sim::observed`, unealta `compara_raport`
  (commit-uri `14a0b57`, `43abf87`, `911e6d0` pe `g0-g2-fundatie`); schița pentru OS: `cyber-gpu/integration/cyber-universe/C-54_gpu-tur-si-lant.md`.
- `cyber-universe` (doar cu „da”): `gpu tur` pe lista albă a modului automat (C-53); `gpu lant` doar cu „DA” tastat, **nu** în modul automat.

## Cost și riscuri
- `gpu tur`: mic; 0 scrieri (driverul refuză rezultatul dacă apare vreo scriere). 3 registre noi de citit (pregătirea I6), citiri simple.
- `gpu lant`: aceleași scrieri ca `gpu i6 --scrie` (C-52), nimic în plus; I7 nu se încearcă (nu e gata) — lanțul se oprește acolo.

## Decizia lui Adrian
- (așteaptă)

## Discuție
- 2026-11-01 `cyber-gpu`: pe cele 3 rapoarte reale (28 oct, 29 oct, 1 nov) simularea nouă dă exact ce a dat placa (33 de valori la fel, 0 diferite).
