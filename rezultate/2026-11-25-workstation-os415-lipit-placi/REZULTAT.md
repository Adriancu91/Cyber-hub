# os-415 — pasul #513 lipit pe plăcile de 64 × 64 (P6-193) — TRECE, câștig ~0

**Data:** 25 nov 2026, pornire 00:58. Raport: `rezultate/os-automat/2026-11-25/ciclu-auto-20261125-0058.txt`.
- `mm_train_tile_gelu` a mers din prima pe placă; TRECE = oracolul (1,5e-5 / 9,4e-5).
- Placa 485,6 ms, pasul întreg 494,5 ms = 2 070 simb/s — **la fel ca reperul nelipit** (os-412: 485,6 / 494,9). Prezis: 2–4 ms mai puțin. Câștigul e sub zgomot.
- Tabloul în timpul pașilor: 1 950 MHz (min 1 785), P0, 133 W din 290, nicio încetinire.
- Concluzie: lipirile mici nu mai contează cât timp înmulțirea e 93 % din pas și placa merge la 44 % din putere. Se păstrează (nu strică), dar prioritatea e cursa / plăcile mai mari / tensor cores.
