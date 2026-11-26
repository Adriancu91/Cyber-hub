# os-471 — token32 (tot simbolul într-o lansare) — CORECT, dar MAI LENT

- Rulat: 26 nov 23:17 (ciclul 23:21), pornit de centrul de comandă; rândul `test-placa --token32`.
- G=384: TRECE — 16 simboluri identice, amprenta 0x6c8501f0 = lista obișnuită, contorul barierei corect 18 / 18; **placa 3 859 µs / simbol** (lista obișnuită 1 069), cu driverul 8 435 µs (lista 2 079).
- G=768: TRECE — aceleași simboluri și amprentă; **placa 4 339 µs / simbol**, cu driverul 8 915 µs.
- Predicția Cyber-GPU: ~1,26 ms la 384, ~1,0 ms la 768 → **greșită de ~3–4×**: corectitudinea e dovedită, viteza nu. Programul unic e de ~3,6× mai lent decât lista obișnuită; de înțeles de ce (barierele, 92 de registre / ocuparea, sau calcul nedistribuit) înainte de a-l folosi la scris.
- Sursa: `rezultate/os-automat/2026-11-26/ciclu-auto-20261126-2321.txt`, rândurile 66–72.
