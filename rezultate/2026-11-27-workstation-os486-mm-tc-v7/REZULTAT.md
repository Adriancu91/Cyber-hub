# os-486 — înmulțirea mm_tc_v7 — TRECE; mic câștig, dW rămâne frâna

- Rulat: 27 nov 10:32 (ciclul 11:09, ~37 min), pornit de centrul de comandă; rândul `test-placa --tablou-viteza --mm-tc --mm-tc-v4 --mm-tc-v5 --mm-tc-v6 --mm-tc-v7 --mm-tc-64k --mm-tc-dxdw`.
- Toate variantele: aceiași biți ca `mm_tc`.

| program @64k | qkv (înainte) | dX | dW (A transpus) |
|---|---|---|---|
| v4 | 2,6 ms | **2,53** | 30,5 |
| v5 | 1,87 ms | 15,6 (os-485: 1,62!) | 24,2 |
| v6 | 1,26 | 12,9 | 18,0 |
| **v7** | **1,20** | 11,5 | **14,1** |

- v7/v6: qkv ×1,05 (prezis 1,00–1,20 ✓), dX ×1,13 (prezis 1,05–1,40 ✓), dW ×1,28.
- **Atenție, măsurare instabilă:** v5 la dX a dat 15,6 ms aici față de 1,62 ms în os-485 (×10), iar fără 64k 42,1 față de 4,28 — același program, aceleași biți. v4 e stabil (2,52 / 2,53). Cyber-GPU suspectează expirarea cererii de viteză a plăcii în timpul probei (nota sesiunii 269); până la o probă care ține ceasul fix, timpii dX/dW de la v5 în sus nu sunt de încredere.
- Concluzie provizorie: **v7 înainte, dX de măsurat din nou (v4@64k 2,5 sigur, v5@64k posibil 1,6), v7 la dW**; dW (14 ms față de 1,2 ms înainte) rămâne cea mai mare rezervă → are nevoie de un program dedicat pentru A transpus.
- Sursa: `rezultate/os-automat/2026-11-27/ciclu-auto-20261127-1109.txt`.
