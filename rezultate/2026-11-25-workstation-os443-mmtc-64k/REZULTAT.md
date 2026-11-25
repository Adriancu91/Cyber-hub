# os-443 · `mm_tc*` la treapta de 64 KiB (2 blocuri pe unitate) — TRECE; `mm_tc_v4@64k` = 8,28 TFLOP/s

- **Când:** 25 nov 2026, semnal 20:59, raport `rezultate/os-automat/2026-11-25/ciclu-auto-20261125-2105.txt`.
- **Biții:** toate variantele @64k = aceiași biți ca `mm_tc` (6/6, respectiv 5/5 aliniate la `v4`).

| qkv-513 (6144 × 2304 × 768) | treapta de azi (32 KiB) | treapta 64 KiB | câștigul treptei |
|---|---|---|---|
| `mm_tc` | 1,02 TFLOP/s | 1,99 | ×1,93 |
| `mm_tc_pf` | 2,75 | 4,85 | ×1,76 (prezis ×1,6–1,9 ✔) |
| **`mm_tc_v4`** | 4,58 | **8,28** | **×1,81** |

- **`mm_tc_v4@64k` = ×8,05 față de `mm_tc` de azi-dimineață, ×2,3 față de cea mai bună F32 (3,61).** Ținta din etapa 1 (≥ 8 TFLOP/s pe înmulțire, nota 14:40) — **atinsă pe qkv**.
- Următorul: pasul mixt rapid (P6-215 `--mixt-rapid`) **cu treapta 64 KiB și lotul mare**; Cyber-GPU: `pack_mixed_fast` să lanseze `mm_tc*` la 64 KiB (azi alege doar programul).
