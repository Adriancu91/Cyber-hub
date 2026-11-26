# os-469 · atenția pe circuitele speciale la treapta 64 KiB — TRECE; explică de ce v4 n-a câștigat în pas

- **Când:** 26 nov 2026, 20:29; raport `rezultate/os-automat/2026-11-26/ciclu-auto-20261126-2029.txt`.
- **Biții:** tc@64k = tc 5/5, tc16@64k = tc16 5/5, v4@64k = v4 4/4, v4pf@64k = v4pf 4/4.
- **atentie-513-b4 pe lansare:** tc 1,16 → 0,69 ms (×1,67); **tc16 0,87 → 0,41 ms (×2,08)**; v4 0,52 → 0,34 ms (×1,50); v4pf 0,64 → 0,45 ms.
- **Citire:** pasul mixt #513 rulează deja totul la 64 KiB (`--treapta-pas`), deci în pas tc16 era deja ~0,41 ms; v4 aduce doar ~0,07 ms × 12 ≈ 0,8 ms la b4 — de aceea os-468 n-a arătat câștig. Atenția înapoi pe circuitele speciale costă acum ~4–5 ms din ~100 ms pe pas (lot 2): **nu mai e frâna**.
