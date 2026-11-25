# os-416 — cursa de noapte completă (C-165, P6-194) — `mm_tv_128x128` câștigă pe toate cele 15 forme

**Data:** 25 nov 2026, pornire 01:35. Raport: `rezultate/os-automat/2026-11-25/ciclu-auto-20261125-0135.txt`.
- Pasul #513 înainte de cursă: 474,2 ms = 2 159 simb/s, TRECE = oracolul.
- Cursa: 15 forme × 4 variante = **60 de rânduri, toate cu aceiași biți ca martorul, 0 diferite**. `64x64k8` scoasă (RACE_HOLD), programele mapate cu pagină de pază. **Nicio blocare.**
- **`mm_tv_128x128` e cea mai rapidă pe toate cele 15 forme:** ~1,9–2,1 TFLOP/s față de 1,26–1,44 ale martorului (×1,3–1,6; pe formele mici 768×768×1024 și 2304×768×1024 doar ×1,13–1,13).
- **Cu câștigătoarele pe fiecare formă, pasul ar scădea cu ~141 ms** (din timpii izolați, DEDUS): ~474 → **~333 ms ≈ 3 080 simb/s**.
- Tabloul în timpul cursei: 1 785 MHz, P0, 77 W, 42 °C, nicio încetinire (încărcarea arătată 0 % = citirile cad între lansările scurte).

## Următorul pas (C-157/C-165)
- Cyber-GPU + OS: **legați `mm_tv_128x128` în pasul #513** pe toate formele (un singur lucru nou pentru placă: programul a trecut deja în cursă); verdict oracolul, prezis ~333 ms.
- Apoi `mm_tc` (tensor cores) pe aceeași formă de plăci 128×128.
