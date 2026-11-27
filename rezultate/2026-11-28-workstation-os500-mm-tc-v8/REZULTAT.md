# os-500 — înmulțirea mm_tc_v8 (C-168 p.3) — corectă, câștig mic; predicția ratată

- Rulat: 28 nov 00:12 (ciclul 00:49), pornit de centrul de comandă; rândul `test-placa --tablou-viteza --viteza-1800 --mm-tc --mm-tc-v6 --mm-tc-v7 --mm-tc-v8 --mm-tc-64k --mm-tc-dxdw` (verificat cu `tools/verifica-rand.py`).
- v8 și v8@64k: 7 / 7 seturi cu aceiași biți ca `mm_tc`.
- Lanțul a rulat 1 986 s (fereastra 1 800 s) → **1 set de timpi în afara ferestrei** (ultimul măsurat; de aflat care din jurnal).

| program @64k | qkv | dX | dW |
|---|---|---|---|
| v7 | 1,198 ms | 1,147 | **1,469** |
| **v8** | **1,063** (20,4 TFLOP/s) | **1,037** | 1,650 |

- v8/v7: qkv ×1,13, dX ×1,11, dW ×0,89 (mai lent). **Predicția Cyber-GPU (qkv 0,75–0,96 ms) RATATĂ** — câștigul real e ~1/3 din cel prezis.
- Pentru pas: v8 la qkv și dX, v7 la dW → estimat (DEDUS) pasul lot 6 ~147,7 → ~141 ms (~21 800 simb/s). Ținta C-168 p.3 (≥ 28 TFLOP/s) nu e atinsă: încă ~42 % din vârf.
- Sursa: `rezultate/os-automat/2026-11-28/ciclu-auto-20261128-0049.txt`.
