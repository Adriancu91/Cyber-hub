# os-438 · `mm_tc_v4` (circuitele speciale cu citiri de 128 de biți) — TRECE, cea mai rapidă înmulțire de până acum

- **Când:** 25 nov 2026, semnal 20:11, raport `rezultate/os-automat/2026-11-25/ciclu-auto-20261125-2018.txt`.
- **Biții:** `mm_tc_v4` = `mm_tc` pe **5 / 5 seturi aliniate** (inclusiv qkv-513); `70x130x33-tb-bias` nealiniat → sărit (cum era prevăzut, merge pe `mm_tc_pf`).
- **qkv-513 (6144 × 2304 × 768):**

| program | timp | TFLOP/s | față de `mm_tc` |
|---|---|---|---|
| `mm_tc` | 21,13 ms | 1,02 | ×1 |
| `mm_tc_pf` (citiri în avans) | 7,86 ms | 2,76 | ×2,68 |
| **`mm_tc_v4` (citiri de 128 de biți)** | **4,73 ms** | **4,59** | **×4,46** |
| (F32, pentru comparație) `64x64k8` la 32 KiB, os-423 | — | 3,61 | — |

- Prima oară când circuitele speciale trec de cea mai bună înmulțire F32. Predicția Cyber-GPU (5–9) → la marginea de jos.
- **Ce lipsește (DEDUS):** treapta potrivită pentru `mm_tc*` (24 KiB → azi 1 bloc pe unitate), apoi încărcarea dublă. Următorul pe placă: **pasul mixt rapid** (`pack_mixed_fast`: `mm_tc_v4` unde se potrivește, altfel `mm_tc_pf`) — P6-214, cu lotul mare.
