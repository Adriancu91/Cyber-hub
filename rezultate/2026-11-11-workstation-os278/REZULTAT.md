# Workstation 11 nov 2026 ~10:21 — os-278 (C-99: CORE_RESUME prin CPUCTL_ALIAS + așteptări lungi), `gpu lant`
- I6 + I7: TRECE (a 5-a oară).
- **i8-gsp-init: ESUAT — „eroare hardware 0x59”**; **1777 scrieri** (1776 ieri cu timeout). Nu mai e timeout: hardware-ul a întors un **cod de eroare** (0x59) —
  foarte probabil codul din cutia poștală a SEC2 după ce Booter-ul a rulat pentru CORE_RESUME (de verificat în jurnal).
- Curățare OK. Jurnal: `gpu-jurnal-006.txt` (2274 rânduri) — urcă aici de la Adrian.

## Jurnalul (adăugat 10:28) — `gpu-jurnal-006.txt` (2274 rânduri) + `raport-20261111-1.txt`
- Secvențiatorul: #0–#418 trec ca ieri (inclusiv #417 CORE_START, #418 CORE_WAIT_FOR_HALT: „falconul GSP oprit: răspuns după 1 µs”).
- #419 CORE_RESUME (calea nouă, CPUCTL_ALIAS): reset falcon GSP (RESET_READY tot nu vine), `0x111668 ← 0x111`, `0x110040 ← 0x09c76000`, `0x110044 ← 0`,
  **`0x840130 ← 2` (pornire SEC2 prin alias) → „SEC2 (Booter) gata: răspuns după 2 µs”**, `0x110080 ← 0x0008b320`, „GSP RISC-V activ: răspuns după 2 µs”
  → ~150 ms mai târziu **ESEC „eroare hardware 0x59”**.
- Observații (de verificat, nu certitudini): (a) **2 µs pentru Booter e mult prea repede** — pare că SEC2 n-a rulat de fapt Booter-ul (în jurnal nu se vede
  o nouă încărcare DMA a Booter-ului în SEC2 și nici scrierea cutiei poștale SEC2 0x840040/44 înainte de pornire, ca la I7); (b) „GSP RISC-V activ după 2 µs” la fel de
  suspect; (c) de aflat **din ce registru** s-a citit 0x59 (SEC2 mailbox? GSP mailbox? coada de stare?) — jurnalul nu arată citirea care a dat eroarea; de adăugat.
