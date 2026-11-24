# os-386 pe placa reală — arena antrenării în VRAM + atenția gen 4, 24 nov 2026 02:37–02:44

Semnal 02:32. Rapoarte: `rezultate/os-automat/2026-11-24/ciclu-auto-20261124-0237.txt` și `-0241.txt`.

**1) `--antrenare-mini --vram`: TRECE, ACELEAȘI NUMERE** (pierdere 9,9e-8, normă 6,3e-7, greutăți 8,8e-6 în 10 pași). Arena 26 MiB urcată o dată (4,9 ms); pe pas doar 1 284 B sus / 260 B jos (os-380: 18 MiB / 13 MiB). **Placa: 3,65 ms pe pas = 17 534 simboluri/s la antrenare** (os-380: 25,6 ms → de 7 ori mai rapid). **Dar pasul întreg: ~370 ms (173 simb/s)** — de 100 de ori mai mult decât placa: timpul se pierde în afara plăcii (lotul sus, așteptarea, citirea pierderii / normei) — de găsit și tăiat înainte de orice comparație.

**2) atenția gen 4:** 6/6 în margine, identică bit cu bit; `attn_back_tile_4` 1,33 ms (gen 3: 1,60; estimat 1,2–1,35) → lanțul atenției ~3,16 ms (gen 1: 8,30). Generarea: 16 identice.
