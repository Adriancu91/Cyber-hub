# os-483 — înmulțirea mm_tc_v6 — TRECE, 17,2 TFLOP/s (×1,48 față de v5)

- Rulat: 27 nov 08:53 (ciclul 09:02), pornit de centrul de comandă; rândul `test-placa --tablou-viteza --mm-tc --mm-tc-v4 --mm-tc-v5 --mm-tc-v6 --mm-tc-64k`.
- `mm_tc_v6` și `mm_tc_v6@64k`: aceiași biți ca `mm_tc` pe 5 / 5 seturi aliniate (1 sărit, nealiniat).
- qkv-513: **v6@64k 1,263 ms = 17,2 TFLOP/s** față de v5@64k 1,869 ms (11,6) → **×1,48**; prezis 1,44–1,78 ms → **mai bine decât predicția**. Fără 64k: v6 3,64 ms (v5 4,74).
- În trei zile: mm_tc 21,1 ms → v6@64k 1,26 ms la aceeași înmulțire (×16,7).
- Urmează: os-485 (`--mm-tc-dxdw`, înmulțirile transpuse ale pasului înapoi), apoi v6 legat în pas.
- Sursa: `rezultate/os-automat/2026-11-27/ciclu-auto-20261127-0902.txt`.
