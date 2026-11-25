# os-423 · proba ocupării (`--cursa-mm --ocupare`) — **H1 CONFIRMAT: ocuparea era frâna**

- **Când:** 25 nov 2026, pornit 11:19:15; raport `rezultate/os-automat/2026-11-25/ciclu-auto-20261125-1119.txt`.
- **Corectitudine:** `proba ocuparii: 10 / 10 aceiasi biti`; pasul #513 = oracolul în pașii 1–9 (471,8 ms, ca os-412 — pasul a rulat cu `mm_train_tile`, fără `--mm-alegere`); antrenarea mini = oracolul.

## Forma qkv (1024 × 2304 × 768), treapta memoriei comune (`MIN = TARGET`)
| program | 8 KiB (azi) | 16 KiB | 32 KiB | 64 KiB | câștig maxim |
|---|---|---|---|---|---|
| `mm_train_tile` | 2 840 µs · 1,27 TF | 1 569 · 2,30 | 1 097 · 3,30 | **1 041 · 3,48** | **×2,73** |
| `mm_tv_64x64k8` | 1 769 · 2,04 | 1 114 · 3,25 | **1 002 · 3,61** | — | ×1,77 |
| `mm_tv_128x128` | 1 890 · 1,91 | 1 278 · 2,83 | 1 276 · 2,84 | — | ×1,48 (limitat de registre: 2 blocuri) |

- Verdict: **H1** — `mm_train_tile` la 64 KiB = 366 ‰ din 8 KiB (≤ 850). Bănuiala din `idei/2026-11-25-centru-inmultirea-la-altii.md` e confirmată.
- Puterea afișată (~79 W) e media paginii (orientativă, cum spunea nota) — nu se poate folosi aici.
- `128x128` se oprește la 16 KiB: registrele (90 → 88 pe fir) dau doar 2 blocuri; cu ≤ 80 registre → 3 (Cyber-GPU).

## Ce înseamnă pentru pas (DEDUS, nemăsurat)
Înmulțirile pasului #513 cu `128x128`: 294,9 ms din 338,4 (os-418). Cu cea mai bună variantă pe formă la treapta potrivită (~3,5–3,6 TF față de ~1,9): înmulțirile ~155–165 ms → **pasul ~200 ms ≈ 5 000 simb/s** (din 3 026). Apoi la fel pentru `mm_tc` (24 KiB, 128 fire → azi 4 grupuri de fire din 48), atenție și programele de scris.

## Cereri
- **Cyber-GPU:** (1) treapta aleasă automat = cele mai multe blocuri pe unitate, **aceeași pe tot pasul**; (2) cursa refăcută cu treptele noi (variantele se pot schimba între ele — `64x64k8` probabil câștigă); (3) `128x128` la ≤ 80 registre; (4) `mm_tc`/`mm_tc128` cu treapta potrivită (și mai puțină partajată pe bloc); (5) încărcarea dublă a feliei următoare (`cp.async`) — cerută și de Adrian (25 nov 11:15).
- **OS:** Release cu treapta automată legată în pasul #513 + `--mm-alegere` și o cursă cu treptele noi.
