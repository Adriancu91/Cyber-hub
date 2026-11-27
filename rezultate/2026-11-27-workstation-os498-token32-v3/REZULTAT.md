# os-498 — token32_v3 (25 LayerNorm lipite în înmulțirea următoare) — TRECE, aproape de listă

- Rulat: 27 nov 22:07 (ciclul 22:11), pornit de centrul de comandă; rândul `test-placa --tablou-viteza --token32 --token32-v2 --token32-v3` (verificat cu `tools/verifica-rand.py`).
- Aceleași 16 simboluri, amprenta 0x6c8501f0; **63 de operații pe simbol** (lista 88) = prezis.
- **G=768: placa 1 453 µs** (v2 1 666 → ×1,15; prezis 1,18–1,38 ms → **mai slab decât predicția**); **cu driverul 2 091 µs — practic egal cu lista obișnuită (2 079)**. G=384: 1 682 / 2 314.
- Lista de lucru: primul simbol 4 032 cuvinte, apoi 38.
- Concluzie: lipirea operațiilor mărunte (F4) ajută și la scris; drumul „o lansare pe simbol” a ajuns la egalitate cu lista, dar încă nu o întrece.
- Sursa: `rezultate/os-automat/2026-11-27/ciclu-auto-20261127-2211.txt`.
