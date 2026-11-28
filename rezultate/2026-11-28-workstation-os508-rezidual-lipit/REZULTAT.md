# os-508 — reziduurile înapoi lipite (C-168 p.5, P5a) — TRECE, record mic: 25 865 simb/s

- Rulat: 28 nov ~12:53, două rânduri într-o pornire (ciclurile 12:59 și 13:04), `ceas 60`, nucleul os-508 (`c4ebc1e`); rândurile verificate cu `tools/verifica-rand.py`.
- **Lot 2:** oracolul pasului mixt ACELEAȘI NUMERE (pierderea 6,3e-6, norma 6,4e-5); pasul 59,9 ms = 17 084 simb/s (os-507: 60,8 / 16 845).
- **Lot 6:** pasul întreg 118,8 ms = **25 865 simb/s** (os-507: 119,8 / 25 635 → +0,9 %, −1 ms). 66 % din Windows. Max 62 °C.
- Câștig mic, cum era de așteptat pentru prima lipire; drumul mare la F4 rămâne Adam + GELU + sumele.
- `live/os-agent.md`: MAC-ul acum mascat (`xx:xx:…`) — cererea de la 10:52 rezolvată.
- Sursa: `rezultate/os-automat/2026-11-28/ciclu-auto-20261128-1259.txt` și `-1304.txt`.
