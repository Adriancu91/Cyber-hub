# os-468 · `attn_back_tile_tc16_v4` în pasul mixt #513 — TRECE, dar fără câștig de viteză

- **Când:** 26 nov 2026, 19:58 (lot 2) și 20:03 (lot 6); rapoarte `rezultate/os-automat/2026-11-26/ciclu-auto-20261126-1958.txt`, `…-2003.txt`.
- Alegerile: `mm_tc_v4` 147 + **`attn_back_tile_tc16_v4` 12**.
- **Lot 2:** oracolul mixt = ACELEAȘI NUMERE (pașii 1–6, aceleași abateri ca os-462 → aceleași numere); **placa 99,8 ms, pasul 111,5 ms = 9 187 simb/s** (os-462: 99,4 / 110,8 / 9 239).
- **Lot 6:** placa 273,1 ms, **pasul 272,9 ms = 11 256 simb/s** (os-465: 272,6 / 11 270); în afara plăcii 0 µs. „NU TRECE” = criteriul sintetic.
- **Citire:** varianta v4, ×1,67 mai rapidă singură (os-465), **nu schimbă pasul** (diferența e în zgomot, ±0,5 %). Prezis −0,2…−1,0 ms → la lot 2 câștigul așteptat era sub zgomotul măsurătorii; la lot 6 nici atât. DEDUS: partea înapoi a atenției nu mai e frâna pasului; următorii pași de viteză trebuie căutați în înmulțiri (69 %) și în pasul persistent.
