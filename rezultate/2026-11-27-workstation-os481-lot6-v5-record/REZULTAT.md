# RECORD — lot 6 cu v5 în pas, fără tablou (nucleul os-481): 15 339 simb/s

- Rulat: 27 nov 08:17 (ciclul 08:24), pornit de centrul de comandă; rândul `test-placa --antrenare-mini --vram --antrenare-513 --placi3 --mm-placi --colsum-impartit --mixt-513 --mixt-513-rapid --lot-prin-ram --doua-locuri --atentie-tc16 --atentie-v4 --atentie-ds --pas-v5 --lot-513 6`.
- **Pasul întreg 200,3 ms (mediană, 10 pași) = 15 339 simb/s; placa 200,4 ms; în afara plăcii ~0.** Pașii 2–10: 197–201 ms, foarte stabili.
- Față de recordul vechi 11 270 (os-465): **×1,36**; Windows/PyTorch ≈ 39 300 → **39 %** (ieri 29 %, alaltăieri dimineață 2 %).
- Cauza celor 71 ms din ciclul 07:49: **citirile tabloului de bord pe fiecare pas** (`--tablou-viteza`). De rezolvat la OS: tabloul citit mai rar sau în afara pasului.
- La lot 6 nu există oracol; la lot 2 același pas = oracolul mixt (os-481, ACELEAȘI NUMERE). „NU TRECE” = criteriul sintetic cunoscut; toate numerele finite.
- Sursa: `rezultate/os-automat/2026-11-27/ciclu-auto-20261127-0824.txt`.
