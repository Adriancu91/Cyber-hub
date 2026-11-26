# os-476 — înmulțirea mm_tc_v5 — TRECE, ×1,41 față de v4

- Rulat: 27 nov 01:06 (ciclul 01:15), pornit de centrul de comandă; rândul `test-placa --tablou-viteza --mm-tc --mm-tc-v4 --mm-tc-v5 --mm-tc-64k`.
- `mm_tc_v5` și `mm_tc_v5@64k`: aceiași biți ca `mm_tc` pe 5 / 5 seturi aliniate (1 sărit, nealiniat).
- qkv-513: **v5@64k 1,87 ms = 11,6 TFLOP/s** față de v4@64k 2,63 ms (8,3 TFLOP/s) → **×1,41**; prezis 1,59–1,94 ms → CONFIRMAT. Fără 64k, v5 ≈ v4 (4,74 ms).
- Ce înseamnă: înmulțirile sunt ~69 % din pasul de antrenare; dacă toate 147 merg la fel (DEDUS), pasul la lot 6 ar coborî spre ~210–220 ms → ~14 000 simb/s. Trebuie întâi legat în pas (`pack_mixed_fast` cu v5, la Cyber-GPU).
- Sursa: `rezultate/os-automat/2026-11-27/ciclu-auto-20261127-0115.txt`, rândurile 137–152.
