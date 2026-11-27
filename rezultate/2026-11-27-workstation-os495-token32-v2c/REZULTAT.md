# os-495 — token32_v2c (ceasul pe operație) — TRECE

- Rulat: 27 nov 18:06 (ciclul 18:06), pornit de centrul de comandă; rândul `test-placa --tablou-viteza --token32 --token32-v2 --token32-v2c`.
- token32: G=768 placa 4 015 µs; token32_v2: G=768 placa 1 666 µs, cu driverul 2 274 (repetă os-477 / 10:01 la ±1 %).
- **token32_v2c G=768: placa 1 676 µs (lista obișnuită 1 067), cu driverul 2 284**; aceleași 16 simboluri, amprenta 0x6c8501f0. Ceasul în sine costă ~10 µs (0,6 %).
- Zona ceasului, ultimul simbol: **88 de operații, 1 741,6 µs** pe placă — detaliul pe operații e pentru Cyber-GPU (unde se duc cei ~600 µs în plus față de listă: bariere vs. calcul).
- Lista de lucru: primul simbol 5 632 cuvinte, apoi 38 pe simbol.
- Sursa: `rezultate/os-automat/2026-11-27/ciclu-auto-20261127-1806.txt`.
