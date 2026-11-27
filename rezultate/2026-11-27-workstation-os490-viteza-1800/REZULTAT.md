# os-490 — viteza maximă 1 800 s (aprobată de Adrian) — timpii reali dX/dW: frâna era doar măsurarea

- Rulat: 27 nov 14:55 (ciclul 15:20), rândul `test-placa --tablou-viteza --viteza-1800 --mm-tc --mm-tc-v6 --mm-tc-v7 --mm-tc-64k --mm-tc-dxdw`; OS-ul a găsit aprobarea în DECIZII.md (27 nov 14:35) și a cerut 1 800 s.
- Paza ferestrei: lanțul a rulat 1 190 s din 1 800 → **IN fereastră; 0 seturi în afara ei**. Toate variantele: aceiași biți ca `mm_tc`.

| program @64k | qkv (înainte) | dX | dW (A transpus) |
|---|---|---|---|
| v6 | 1,26 ms | 1,38 | 1,96 |
| **v7** | **1,19** | **1,15** | **1,46** |
| (mm_tc simplu) | 21,1 | 21,0 | 21,2 |

- **Corectură față de os-485 / os-486:** dW „14–18 ms” și dX v6/v7 „11–13 ms” erau măsurați cu placa ieșită din viteza maximă. Cu placa la viteză tot timpul, **v7@64k e cel mai bun pe toate trei formele** (×14,5–18 față de `mm_tc`). dW NU e o frână reală.
- Pentru pas: v7@64k peste tot (P6: `--pas-v7` / alegerea v7). Estimare (DEDUS): pasul lot 6 de la 200 ms spre ~150–170 ms.
- Sursa: `rezultate/os-automat/2026-11-27/ciclu-auto-20261127-1520.txt`.
