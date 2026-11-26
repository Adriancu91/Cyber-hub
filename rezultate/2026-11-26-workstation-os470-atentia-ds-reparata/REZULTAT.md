# os-470 — atenția dS (attn_back_tile0_tc / _v4) reparată — TRECE

- Rulat: 26 nov 22:50 (ciclul 22:54), pornit de centrul de comandă; rândul `test-placa --atentie-placi --atentie2 --atentie3 --atentie-tc --atentie-tc0 --atentie-tc0-v4`.
- `attn_back_tile0_tc`: 5 / 5 seturi, abaterea față de dS F32 ≤ 2,84e-4 (sub 1e-3), 86 690 / 86 690 cuvinte = modelul; nu se mai blochează (os-467 se bloca).
- v4 = tc pe 4 / 4 seturi aliniate (138 432 / 138 432).
- `atentie-513-b4` pe lansare: **v4 0,38 ms**, tc 0,56, dS F32 0,82 → pe pas (×12) ~4,6 ms față de ~9,9.
- Urmează: P6-241 (dS v4 legat în pasul mixt rapid) → os-472; os-471 (token32) pornit 23:15.
- Sursa: `cyber-universe/docs/STATE.md`, raportul `ciclu-auto-20261126-2254.txt`.
