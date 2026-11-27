# os-486 — înmulțirea mm_tc_v7 — TRECE; mic câștig, dW rămâne frâna

- Rulat: 27 nov 10:32 (ciclul 11:09, ~37 min), pornit de centrul de comandă; rândul `test-placa --tablou-viteza --mm-tc --mm-tc-v4 --mm-tc-v5 --mm-tc-v6 --mm-tc-v7 --mm-tc-64k --mm-tc-dxdw`.
- Toate variantele: aceiași biți ca `mm_tc`.

| program @64k | qkv (înainte) | dX | dW (A transpus) |
|---|---|---|---|
| v5 | 1,87 ms | **1,62** | 25,2 |
| v6 | 1,26 | 12,9 | 18,0 |
| **v7** | **1,20** | 11,5 | **14,1** |

- v7/v6: qkv ×1,05 (prezis 1,00–1,20 ✓), dX ×1,13 (prezis 1,05–1,40 ✓, dar tot de 7× mai lent decât v5), dW ×1,28.
- Concluzie: alegerea pe formă în pas = **v7 înainte, v5 la dX, v7 la dW**; dW (14 ms față de 1,2 ms înainte) rămâne cea mai mare rezervă → are nevoie de un program dedicat pentru A transpus.
- Sursa: `rezultate/os-automat/2026-11-27/ciclu-auto-20261127-1109.txt`.
