# os-465 · #513 lot 6 + atenția f16 + lotul prin RAM + două locuri — **11 270 simb/s (record)**

- **Când:** 26 nov 2026, 17:48; raport `rezultate/os-automat/2026-11-26/ciclu-auto-20261126-1748.txt`.
- Rândul (ordinea corectă): `test-placa --antrenare-mini --vram --antrenare-513 --placi3 --mm-placi --colsum-impartit --mixt-513 --mixt-513-rapid --lot-prin-ram --doua-locuri --atentie-tc16 --lot-513 6`.
- Alegerile: `mm_tc_v4` 147 + `attn_back_tile_tc16` 12, treapta 64 KiB pe toate lansările.
- **Placa 272,8 ms = 11 260 simb/s; pasul întreg 272,6 ms = 11 270 simb/s** (os-456 lot 6: 293,1 ms / 10 480 → ×1,075); **în afara plăcii 0 µs**. Windows ≈ 39 300 → **29 %**.
- Verdictul „NU TRECE” = criteriul „ultima < prima” pe loturi sintetice aleatoare (la lot 6 nu există oracol; la lotul 2 același pas = oracolul mixt, os-462). Pierderea la pasul 1 = 9,8716 ≈ ln 16 384, toate numerele finite.
