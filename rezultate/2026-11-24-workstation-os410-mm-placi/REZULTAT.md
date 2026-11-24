# os-410 — înmulțirile pasului #513 pe `mm_train_tile` (P6-188) — TRECE, dar doar ×1,68 (prezis ×3–6)

**Data:** 24 nov 2026, pornire 18:18. Rapoarte: `ciclu-auto-20261124-1818.txt` (reper), `-1822.txt` (nou).

| | reper (`--placi3`) | **nou (`--placi3 --mm-placi`)** | prezis |
|---|---|---|---|
| verdict | TRECE = oracolul | **TRECE = oracolul** (aceleași abateri 1,5e-5 / 9,4e-5; aceeași pierdere 9,8493 → 10,1735) | TRECE |
| înmulțirile | `mm_train` 718,1 ms | **`mm_train_tile` 428,7 ms (×1,68)** | 120–240 ms (×3–6) |
| pasul (placa) | 772,2 ms = 1 326 simb/s | **482,9 ms = 2 120 simb/s** | 180–300 ms; simulatorul: 225 ms |
| pasul întreg | 754,9 ms = 1 356 | **475,7 ms = 2 152 simb/s** | — |

- Programul nou a mers din prima pe placa reală, cu aceiași biți — prima rulare a lui `mm_train_tile` (neprobat singur înainte).
- **Câștigul e același pe toate formele** (fc 70,8 → 42,6 ms; proj 70,5 → 41,3; qkv 52,3 → 31,7; dW/dX la fel, toate ×1,65–1,70). O frână comună, nu o formă anume.
- Viteza de calcul: ~0,84 → **~1,4 TFLOP/s** (plafonul F32 al plăcii ~21,7): tot doar ~6 %.
- Acum: `mm_train_tile` 88,7 %, `colsum` 5,0 % (24 ms), atenția 4,2 % (20 ms), AdamW 1,1 %.
- Azi, în total: 1 124 → 483 ms (×2,3). Windows/PyTorch: ~39 300 simb/s (bf16, lot 12 × 512) — încă ×18.

## Întrebări pentru Cyber-GPU (C-157/C-160)
1. De ce ×1,68 și nu ×3–6, la fel pe toate formele? Bănuieli de verificat: ocuparea (34 de registre, 8 KiB partajați — câte blocuri pe SM?), citirile globale câte 4 octeți, bariera pe felia de 16, lotul mic (16 × 12 … 16 × 48 blocuri pentru 48 de SM-uri).
2. **A4 (cerut la 17:00): puterea și starea P în timpul pasului** — dacă placa trage puțin, nu calculul e frâna.
3. E cazul ideal pentru **cursa de noapte (C-165)**: variante cu plăci 32/64/128, 2×2 / 4×4 / 8×8 pe fir, felia K 16/32, citiri vectoriale — acum că programul de bază a trecut singur pe placă.
4. `colsum` împărțit (T216, gata în simulare): 24 ms = 5 % — de legat.
