# os-473 — dS-ul atenției pe circuitele speciale, în pasul de antrenare #513 — TRECE

- Rulat: 27 nov 00:26 (ciclul 00:33), pornit de centrul de comandă; rândul `test-placa --tablou-viteza --antrenare-mini --vram --antrenare-513 --placi3 --mm-placi --colsum-impartit --mixt-513 --mixt-513-rapid --atentie-tc16 --atentie-v4 --atentie-ds`.
- Alegerile: mm_tc_v4 147, attn_back_tile_tc16_v4 12, attn_back_tile0_tc_v4 12 = cum era prezis.
- Oracolul pasului mixt: ACELEAȘI NUMERE (pașii 1–6: pierderea 2,7e-5, norma 3,2e-4); TRECE.
- **Lot 2: 108,3 ms pe pas = 9 453 simb/s** (os-468, aceeași listă fără dS pe circuite: 111,5 ms = 9 187) → −3,1 ms, +2,9 %. Prezis ~4–5 ms (−6…−9 ms în banda Cyber-GPU pentru pasul întreg); câștigul real ~jumătate din predicție, ca de obicei.
- Lot 6 nerulat în acest test; recordul rămâne 11 270 simb/s (os-465). Estimat la lot 6 cu dS pe circuite: ~11 500 (DEDUS, de măsurat).
- Bonus: Kronos a scris pe placă 16 simboluri identice cu procesorul.
- Sursa: `rezultate/os-automat/2026-11-27/ciclu-auto-20261127-0033.txt`.
