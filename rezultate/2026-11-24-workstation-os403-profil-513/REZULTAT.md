# os-403 — profilul pasului #513 pe placa reală (P6-180..182)

**Data:** 24 nov 2026, pornire 12:58. Rapoarte: `ciclu-auto-20261124-1258.txt`, `-1300.txt`.

- Mini cu arena în VRAM: TRECE. #513: ca os-395 (1 123 ms/pas = 911 simb/s; pierderea 9,85 → 10,18 pe loturi sintetice, NU TRECE pe criteriul „scade”; 0 NaN). Rezumatul arată acum verdictele (P6-181 merge). Test 2: TRECE, 638,50 simb/s.

## Unde se duce secunda (median, 10 pași, 385 lansări)
| program | timp | % |
|---|---|---|
| `mm_train` (înmulțiri F32, 147 lansări) | 718 ms | **63,9 %** |
| `attn_fwd` (atenția înainte, 12) | 212 ms | **18,8 %** |
| `attn_back` (atenția înapoi, 24) | 159 ms | **14,1 %** |
| `colsum` | 24 ms | 2,1 % |
| AdamW (`opt_step`) + restul | ~10 ms | <1 % |

Pe etape: înapoi 59 %, înainte 40,5 %, AdamW 0,4 %.

## Ce înseamnă (calcul DEDUS al centrului)
- Un pas #513 cere ~6 × 98 M × 1 024 ≈ 6,0 × 10¹¹ operații de înmulțire. `mm_train` le face în 0,72 s ≈ **0,84 TFLOP/s**. RTX 3070 Ti poate ~21,7 TFLOP/s în F32 și ~87 în bf16 cu tensor cores. Folosim deci **~4 % din F32**. Programul de înmulțire nu e încă împărțit în plăci (tiling) pentru antrenare.
- Windows (bf16, lot 12 × 512) ≈ 39 300 simb/s ≈ 23 TFLOP/s efectiv.
- Atenția înainte: 17,7 ms pe strat la context 512 — tot fără plăci și fără tensor cores.

## Ordinea propusă (C-157/C-160)
1. **`mm_train` cu tiling + bf16/tensor cores** (programele P8 au trecut deja la generare) — 64 % din pas.
2. **Atenția înainte și înapoi** cu blocuri (în stilul FlashAttention, scris de noi) — 33 %.
3. Lotul mai mare (12 × 512 ca Windows; încape în 6 GiB?) și criteriul de pierdere pe date reale, nu sintetice.
Țintă intermediară: ×10 față de acum (~9 000 simb/s) doar din 1–2.
