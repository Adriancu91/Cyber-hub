# os-322 — testul automat 2 (P5: viteza maximă cerută oficial), 20 nov 2026

- **Release:** `os-322` (`dd4210e`, CI verde), `cyber-gpu 9565f68`; pus pe stick la 15:27 (sume recitite identice); test 15:31:09 → gata în 128 s; Windows înapoi singur (~15:33).
- **Fișiere:** `rezultate/os-automat/2026-11-20/ciclu-auto-20261120-1531.txt`, `gpu-jurnal-016.txt` (recuperare), `gpu-jurnal-017.txt` (lanțul).

## Rezultat — PLACA BATE PROCESORUL
- **Viteza maximă:** starea înainte **P5**, cererea `INTERNAL_PERF_BOOST_SET_2X` (600 s) **acceptată**, după cerere **P0** → verdict 1 („urcată”). La final: ștergerea cererii acceptată, starea încă P0 (coboară singură după).
- **Corect:** 16 simboluri pe placă, **identice cu procesorul**, fiecare verificat după placă cu motorul rapid; abaterea maximă a logit-urilor 1,62e-5.
- **Placa singură: 381,98 simb/s** (os-313: 43,77) — de **8,7 ori**; 2 631 µs pe simbol (os-313: 22 968).
- **Cu driverul: 94,84 simb/s** (os-313: 21,54) — de 4,4 ori. **Procesorul (motorul rapid al OS-ului): 72,72 simb/s.** → *Primul test în care Kronos pe placă, cu driverul nostru, e mai rapid decât pe procesor.*
- Cu verificarea pe procesor după placă: 38,5 simb/s (os-313: 0,25).
- Timpul pe simbol (median): placa 2 631 µs · **driver 3 081 µs** · jurnal 61 µs · ecran 0 = 5 802 µs.
- **Copierea VRAM → VRAM (`kc`): 281 572 MB/s** (os-313: 9 165) — de 30 de ori; 563 GB/s trafic = 93 % din 608 GB/s, deci memoria plăcii merge acum aproape la plafon.
- Urcarea greutăților: placa 6 168 MB/s.
- Uneltele noi (doar citire): discurile văzute de OS (NVMe 512 GB, fără `cyber.rw`), temperatura procesorului 41 °C (TjMax 86, prag 76), ceasul de pază TCO găsit, oprit.

## Ce înseamnă
1. Frâna era turația plăcii (P5/P8). Cu ea urcată, calculul s-a apropiat de ce permite memoria pentru felul de azi al programelor.
2. **Acum frâna e driverul**: 3,1 ms din 5,8 ms pe simbol (53 %), adică pregătirea și trimiterea celor 196 de lansări de pe procesor. De aici câștigul vine din **lanțul pe placă (P7)** și din **lipirea calculelor (P3)** — ambele reduc munca driverului, nu a plăcii. Cele 8 calcule mărunte cântăresc acum ~10 % din timpul plăcii (2,2 µs fiecare).
3. Pe placă, cele mai grele: fc 471, proj 400, qkv 368 µs pe simbol — ținta etapei 4 (programe mai bune).

## Următorul pas (propus centrului de comandă)
- P3 (calculele lipite, 196 → ~88; gata în SIMULARE la Cyber-GPU) + păstrarea vitezei maxime → reduce driverul cu ~jumătate.
- P6: Kronos #651 (183 M) pe placă — e pe stick.
- P7 (lanțul pe placă) — „da” separat de la Adrian.
