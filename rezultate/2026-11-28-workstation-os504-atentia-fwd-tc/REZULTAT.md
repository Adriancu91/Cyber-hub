# os-504 — atenția înainte pe circuitele speciale (C-168 p.4, attn_fwd_tc) — TRECE, ×5,45 la #513

- Rulat: 28 nov 07:09, două rânduri într-o pornire (ciclurile 07:18 și 07:23), pornit de centrul de comandă; nucleul os-504 (`84ad1de`); rândurile verificate cu `tools/verifica-rand.py`.
- `attn_fwd_tc` față de `attn_fwd_tile3`: **5 / 5 seturi în margine** (O ≤ 1e-3, P ≤ 2e-3; la #513: O 1,9e-4, P 5,2e-5 — mai bine decât H3).
- Timpi: tc-t64 ×2,40; tc-t192-b2 ×2,24; tc-t256-h2 ×1,94; tc-t320 ×2,05; **atentie-513-b4: tile3 1,003 ms → tc 0,184 ms = ×5,45**.
- În pas (DEDUS): 12 lansări × ~1,34 ms (16,1 ms) → ~3 ms → **pasul lot 6 ~140,6 → ~127 ms ≈ 24 000 simb/s** când e legat.
- **Lot 6 repetat (v8 pe formă):** pasul 140,5 ms = **21 859 simb/s** → recordul confirmat (21 837 la 06:08; diferență 0,1 %). Max 62 °C.
- Sursa: `rezultate/os-automat/2026-11-28/ciclu-auto-20261128-0718.txt` și `-0723.txt`.
