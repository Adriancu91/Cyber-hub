# os-512 — v8r + GELU lipit în pas, plus lot 6 pe datele reale — TREC; viteza pe loc

- Rulat: 28 nov ~15:46, trei rânduri într-o pornire (ciclurile 15:54, 15:59, 16:13), `ceas 60`, nucleul os-512 (`1e22371`); rândurile verificate cu `tools/verifica-rand.py`.
- **Lot 2:** oracolul pasului mixt ACELEAȘI NUMERE; pasul 59,6 ms = 17 181 simb/s (os-508: 59,9).
- **Lot 6 (loturi sintetice):** 118,8 ms = 25 867 simb/s (os-508: 25 865) → **fără câștig**. La lot 6 regula alege `mm_tc_v8n` (122 lansări) — v8r nu se folosește la formele astea; GELU lipit (`mm_tc_v8n_gelu` 9,7 ms) a înlocuit `gelu` dar câștigul e ~0.
- **Lot 6 pe datele reale:** = oracolul S141 (ACELEAȘI NUMERE, pierderea 4,2e-5, norma 5,6e-4); **118,0 ms = 26 031 simb/s** (cel mai bun număr măsurat; diferența față de 25 867 e în zgomot). 66 % din Windows. Max 61 °C.
- Profilul pasului (lot 6): înmulțiri v8n + v8n_gelu + v7 = 85,5 ms (**72 %**), atenția înapoi 11,8, Adam 4,8, sumele 3,4, atenția înainte 3,1, LN 1,9, pierderea 1,5.
- Concluzie: **platou la ~119 ms**; aproape tot ce a rămas e în înmulțirile v8n la formele lotului 6 (~19 TFLOP/s medie). Următorul câștig mare cere o înmulțire nouă pentru formele astea (F2), nu mai multe lipiri mărunte.
- Sursa: `rezultate/os-automat/2026-11-28/ciclu-auto-20261128-1554.txt`, `-1559`, `-1613`.
