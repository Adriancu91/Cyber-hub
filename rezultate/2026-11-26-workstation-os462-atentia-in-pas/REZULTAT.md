# os-462 · atenția înapoi pe f16 în pasul mixt #513 — TRECE; pasul 110,8 ms = 9 239 simb/s (lot 2)

- **Când:** 26 nov 2026, semnal 15:41; rapoarte `rezultate/os-automat/2026-11-26/ciclu-auto-20261126-1548.txt` (testul 1) și `…-1553.txt` (testul 2).
1. **Atenția tc cu marginea subnormalelor (os-460/P6-230): TRECE 5 / 5** (marginea veche 4 / 5), `tc16` = `tc` 5 / 5, abaterea ≤ 3,02e-4.
2. **#513 mixt rapid + `--atentie-tc16`, lot 2:** alegerile `mm_tc_v4` 147 + `attn_back_tile_tc16` 12; **oracolul mixt: ACELEAȘI NUMERE (mixt)** în pașii 1–6 (5,5e-6 / 4,1e-5); **placa 99,4 ms (os-456: 106,2 → −6,8 ms, prezis −2…−4) = 10 298 simb/s pe placă; pasul întreg 110,8 ms = 9 239 simb/s** (os-456: 117,5 / 8 713).
3. **Al treilea rând (lot 6 + lotul prin RAM + două locuri + `--atentie-tc16`) NU a rulat** — pe stick nu există un al treilea raport, `teste.txt` consumat, nicio eroare în raportul 2. **Cerere OS:** de ce s-a oprit lista după testul 2 (limita de timp `ceas 40`? lungimea rândului?). Îl reiau în testul următor.
