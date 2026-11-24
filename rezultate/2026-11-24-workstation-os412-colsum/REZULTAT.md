# os-412 — `colsum` împărțit în pasul #513 (P6-189) + ceasul procesorului reparat (P6-191) — TRECE

**Data:** 24 nov 2026, pornire 20:58. Rapoarte: `ciclu-auto-20261124-2058.txt` (reper), `-2103.txt` (nou).

| | reper (`--mm-placi`) | **nou (`--mm-placi --colsum-impartit`)** | prezis |
|---|---|---|---|
| verdict | TRECE = oracolul | **TRECE = oracolul** (1,6e-5 / 9,6e-5) | TRECE |
| `colsum` | 24,3 ms | **2,4 ms** (`colsum_part` 1,5 + `colsum` 0,8) — ×10 | 2,5–5 ms |
| placa pe pas | 485,6 ms = 2 108 simb/s | **463,0 ms = 2 211 simb/s** | — |
| pasul întreg | 494,9 ms = 2 068 | **473,5 ms = 2 162 simb/s** | Cyber-GPU 460–465; simulatorul v1.2: 469 (−1,0 %) |

- **Ceasul reparat (P6-191):** „placa / pasul întreg” = 977–981 ‰ (înainte 1 022 ‰). Pasul întreg al reperului e 494,9 ms în loc de 475,7 la os-410 — tot ceasul vechi, nu o încetinire. În afara plăcii rămân ~10 ms pe pas.
- Acum `mm_train_tile` = **92,9 %** din pas (430,5 ms). Tot ce nu e înmulțire: ~33 ms.
- Simulatorul: al doilea test nevăzut, eroare −1,0 % (primul, os-410: −53 % — reglat atunci).
