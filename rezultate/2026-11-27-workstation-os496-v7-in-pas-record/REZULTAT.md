# RECORD — os-496: v7 în pasul de antrenare — 20 795 simb/s la lot 6 (53 % din Windows)

- Rulat: 27 nov 19:40, **două rânduri într-o pornire** (ciclurile 19:48 și 19:54), pornit de centrul de comandă; nucleul os-496 (`e2441a3`).
- **Lot 2:** alegerile mm_tc_v7 147 (0 pe v5 / v6) = prezis; oracolul pasului mixt **ACELEAȘI NUMERE** (pierderea 2,7e-5, norma 3,2e-4); pasul 82,7 ms = **12 375 simb/s** (os-481 cu v5: 92,0 / 11 134).
- **Lot 6:** placa 147,8 ms, **pasul întreg 147,7 ms = 20 795 simb/s** (recordul vechi 15 339 cu v5 → **×1,36**); prezis Cyber-GPU 137–162 ms → CONFIRMAT (aproape de mijloc). Windows ≈ 39 300 → **53 %** (ieri 29 %, alaltăieri 2 %).
- Paza termică pornită: temperatura max **64 °C**, fără oprire. Kronos a scris apoi 16 simboluri identice cu procesorul.
- Două rânduri într-o pornire au mers (al doilea fără „gpu recuperează”, cu resetul din interior) → mai multe măsurători pe zi.
- Sursa: `rezultate/os-automat/2026-11-27/ciclu-auto-20261127-1948.txt` și `-1954.txt`.
