# os-445 · pasul mixt rapid (`mm_tc_v4` la 64 KiB pe toate înmulțirile) — #513: **116,9 ms = 8 758 simb/s**

- **Când:** 25 nov 2026, semnal ~21:50; rapoarte `rezultate/os-automat/2026-11-25/ciclu-auto-20261125-2158.txt` (mini) și `…-2202.txt` (#513).

## 1. `antrenare mini --mixt --mixt-rapid` — TRECE
- 27 / 27 înmulțiri pe `mm_tc_v4`; **= oracolul** (pierderea 1,3e-5, norma 1,5e-4 față de toleranțele 1e-3 / 2e-3).

## 2. #513 `--mixt-513 --mixt-513-rapid` (lot 2 × 512) — viteza ×2,28, verdictul strict „DIFERA”
- 147 / 147 înmulțiri pe `mm_tc_v4`, treapta 64 KiB pe toate lansările.
- **Pasul întreg 116,9 ms = 8 758 simb/s; placa 106,0 ms = 9 660 simb/s.** Față de F32 lot 2 (os-431: 266,8 ms / 3 837) = **×2,28**; față de azi-dimineață (1 124 ms) = **×9,6**. Windows ≈ 39 300 → **22 %** (dimineață 2 %).
- Față de oracolul F32: **DIFERA** — abaterea pierderii 7,2e-3 (toleranța 1e-3), a normei 1,3e-2 (2e-3). Pierderile urmăresc oracolul la a 3-a zecimală (9,8493 / 9,8749 / 9,8293 / 9,9085 față de 9,8493 / 9,8750 / 9,8293 / 9,9083), greutățile toate numere.
- **Citire (DEDUS):** abaterea vine din rotunjirea f16 pe 98 M de greutăți (toleranța e cea a pasului F32); modelul mic, cu aceleași programe, iese exact. Nu e o greșeală de program, dar **dacă f16 strică învățarea se vede doar pe date reale**: cerere OS + Kronos — o comparație scurtă pe text real (F32 față de mixt, aceleași 200–500 de pași, aceeași sămânță) și toleranța pasului mixt fixată din ea.
