# os-507 — PRIMA ANTRENARE PE DATELE REALE în OS + RECORD 25 635 simb/s (atenția înainte în pas)

- Rulat: 28 nov ~11:14, **patru rânduri într-o pornire** (ciclurile 11:27, 11:33, 11:47, 11:52), `ceas 60`, nucleul os-507 (`dc04bfd`); rândurile verificate cu `tools/verifica-rand.py`. Pornit de centrul de comandă.

## 1. Datele reale (C-168 p.1–2, E1 închisă)
- Greutățile de pornire #513 de pe stick (Kronos S143, SHA-256 verificat), loturile din bucățile #651 (sămânța 1134, ca S141).
- **Lot 2:** față de oracolul PyTorch S141 (F32): **ACELEAȘI NUMERE** — pașii 1–10, abaterea pierderii 5,2e-5, a normei 2,8e-4 (toleranța 1e-3 / 2e-3); pasul 1 = **1,067859** (S141 1,067867). Pasul 64,9 ms = 15 770 simb/s.
- **Lot 6:** **ACELEAȘI NUMERE** — pașii 1–10, pierderea 4,0e-5, norma 3,2e-4; pasul 1 = **1,010690** (S141 1,010662). Pasul 140,5 ms = 21 861 simb/s.
- → Pentru prima dată, Kronos se antrenează în sistemul nostru pe datele lui adevărate, cu aceleași numere ca în PyTorch.

## 2. Atenția înainte pe circuite, în pas (C-168 p.4)
- **Lot 2:** oracolul pasului mixt ACELEAȘI NUMERE (pierderea 6,3e-6, norma 6,4e-5); pasul 60,8 ms = 16 845 simb/s.
- **Lot 6: pasul întreg 119,8 ms = 25 635 simb/s** (recordul vechi 21 859 → **×1,17**); estimat ~127 ms → mai bine decât estimarea. **65 % din Windows** (~39 300).
- Temperatura max 44 / 56 / 49 / 61 °C, fără opriri.
- Sursa: `rezultate/os-automat/2026-11-28/ciclu-auto-20261128-1127.txt`, `-1133`, `-1147`, `-1152`.
