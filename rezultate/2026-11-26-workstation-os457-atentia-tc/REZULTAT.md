# os-457 · atenția înapoi (dQ, dK, dV) pe circuitele f16 — corectă ca în SIMULARE, ×1,8 față de F32 (sub predicție)

- **Când:** 26 nov 2026, 09:43; raport `rezultate/os-automat/2026-11-26/ciclu-auto-20261126-0943.txt`.
- **Corectitudine:** exact ce prezisese SIMULAREA: **4 / 5 seturi în margine** (`ascutit` iese — subnormale f16, știut la Cyber-GPU), **`tc16` = `tc` cuvânt cu cuvânt 5 / 5**, abaterea față de F32 ≤ 3,02e-4, gărzile neatinse. Verdictul formal „NU TRECE” = setul `ascutit` (așteptat).
- **Viteza (atentie-513-b4, mediana a 5):** pe lansare `tc` 1,16 ms, **`tc16` 0,87 ms**, F32 1,59 ms → **×1,83**; pe pasul #513 (× 12, la forma b4): tc16 10,5 ms față de 19,2 ms.
- La lotul 2 (profilul os-456: `attn_back_tile_3` 9,2 ms) asta înseamnă ~5 ms (DEDUS) — **câștig ~4 ms pe pas (~4 %)**; Cyber-GPU prezisese 2,4–4,5 ms → partea înapoi iese de ~1,2–2× mai lentă decât modelul lor.
- **Cereri Cyber-GPU:** (1) de ce `tc16` e de 2× peste predicție (ocuparea? 16 KiB → câte blocuri pe unitate la 64 KiB?); (2) setul `ascutit` — subnormalele f16 (scară / ieșire F32 pe dS mici); (3) apoi legarea în pasul mixt + atenția înainte.
