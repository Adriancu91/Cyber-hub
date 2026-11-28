# os-505 — înmulțirea mm_tc_v8r — TRECE; cea mai rapidă la qkv și dX (22,2 TFLOP/s)

- Rulat a treia oară: 28 nov ~10:06 (ciclul 10:51), `ceas 70`, nucleul os-505 (`9e2218e`). Prima pornire (07:48) oprită de ceasul de siguranță la 40 min; a doua (08:41) doar a curățat lista întreruptă.
- Rândul: `test-placa --tablou-viteza --viteza-1800 --mm-tc --mm-tc-v6 --mm-tc-v7 --mm-tc-v8 --mm-tc-v8r --mm-tc-64k --mm-tc-dxdw` (verificat cu `tools/verifica-rand.py`).
- v8r și v8r@64k: 7 / 7 seturi cu aceiași biți ca `mm_tc`.
- Lanțul a rulat 2 429 s (fereastra 1 800) → **5 seturi în afara ferestrei** (toate dW de la v8 în sus: 12–15 ms = placa încetinită, NU se folosesc).

| program @64k | qkv | dX | dW |
|---|---|---|---|
| v7 | 1,197 ms | 1,145 | 1,451 (în fereastră) |
| v8 | 1,065 | 1,037 | (afară) |
| v8n | 1,015 | 0,948 | (afară) |
| **v8r** | **0,981** (22,2 TFLOP/s) | **0,933** | (afară) |

- v8r/v8: qkv ×1,09, dX ×1,11. v8r/v7: qkv ×1,22, dX ×1,23. Pas estimat (DEDUS) cu v8r pe qkv/dX: ~140 → ~135 ms.
- dW la v8+ trebuie remăsurat **în fereastră** → proba trebuie împărțită (sau dW măsurat primul).
- Sursa: `rezultate/os-automat/2026-11-28/ciclu-auto-20261128-1051.txt`.
