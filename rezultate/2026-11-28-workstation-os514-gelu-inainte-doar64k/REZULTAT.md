# os-514 — GELU înainte lipit (C-168 p.5, P5c) + proba `--mm-tc-doar-64k` în fereastră — TREC

- Rulat: 28 nov ~17:33, trei rânduri într-o pornire (ciclurile 17:39, 17:44, 18:10), `ceas 75`, nucleul os-514 (`052c79b`); rândurile verificate cu `tools/verifica-rand.py`.
- **Lot 2:** oracolul pasului mixt ACELEAȘI NUMERE; pasul 59,1 ms = 17 316 simb/s (os-512: 59,6).
- **Lot 6:** 117,8 ms = **26 085 simb/s** (os-512: 118,8 sintetic / 118,0 real) → record mic (+0,8 %). Max 60 °C.
- **Proba scurtată (doar @64k), toată în fereastră (0 seturi afară):**

| program @64k | qkv | dX | dW |
|---|---|---|---|
| v7 | 1,197 ms | 1,148 | **1,455** |
| v8 | 1,066 | 1,037 | 1,654 |
| v8n | 1,026 | **0,910** | 1,459 |
| v8r | **0,981** | 0,935 | 1,546 |

- dW măsurat acum corect: cel mai bun v7 (1,455) ≈ v8n (1,459). Cele 12–15 ms din os-500/505 erau doar placa încetinită.
- Concluzie: toate variantele stau între 0,9 și 1,65 ms (~18–22 TFLOP/s); niciuna nu sare de ~46 % din vârf. Pasul rămâne ~118 ms.
- Sursa: `rezultate/os-automat/2026-11-28/ciclu-auto-20261128-1739.txt`, `-1744`, `-1810`.
