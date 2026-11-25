# os-418 — `mm_tv_128x128` legată în pasul #513 (P6-196, `--mm-alegere`) — TRECE, pasul 474 → 338 ms

**Data:** 25 nov 2026, pornire 04:33. Raport: `rezultate/os-automat/2026-11-25/ciclu-auto-20261125-0433.txt`.

| | os-412/416 (`mm_train_tile`) | **os-418 (`mm_tv_128x128`)** | prezis |
|---|---|---|---|
| verdict | TRECE | **TRECE = oracolul** (1,6e-5 / 9,6e-5 — aceleași cifre, aceiași biți) | TRECE |
| înmulțirile | 430,5 ms | **294,9 ms** (90,0 %) | — |
| placa | 463,7 ms | **327,6 ms = 3 125 simb/s** | — |
| pasul întreg | 474,2 ms = 2 159 | **338,4 ms = 3 026 simb/s** (×1,40) | ~333 (DEDUS din cursă; −1,6 %) |

- Tabloul în timpul pașilor: 1 950 MHz, P0, 123 W din 290, 48 °C, nicio încetinire.
- Simulatorul v1.3: opțiunea `t128` cu cifra măsurată; verificarea 0,6 % pe tot istoricul.
- **Azi (24–25 nov), pasul #513 în OS-ul nostru: 1 124 → 338 ms (×3,3), 910 → 3 026 simb/s.** Windows/PyTorch: ~39 300 (bf16, lot 12 × 512).
- Următorul: cursa cu 5 variante (`64x64k8` reparată, 2,04 TFLOP/s pe qkv), apoi `mm_tc` (tensor cores) pe plăci 128×128.
