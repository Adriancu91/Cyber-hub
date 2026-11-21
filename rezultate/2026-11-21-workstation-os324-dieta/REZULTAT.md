# Rezultat: „dieta driverului” pe placa reală (os-324, ciclu automat) — 21 nov 2026, 11:01

- **Unde:** workstation (RTX 3070 Ti), ciclul automat, fără om de față. Semnal ~10:54, test 11:01, raport urcat singur.
- **Versiunea:** `os-324` (`fa59b50`), dieta din cyber-gpu `4925469`. Rândul: `test-placa`.
- **Fișierele brute:** `rezultate/os-automat/2026-11-21/ciclu-auto-20261121-1101.txt`, `gpu-jurnal-023.txt`, `gpu-jurnal-024.txt` (rândurile `kt`: 4014–4030).

## Ce era nou: dieta (C-154) — MERGE, exact cât s-a estimat
| | os-322 (20 nov) | **os-324 (azi)** |
|---|---|---|
| driverul pe simbol (kt median) | 3 081 µs | **1 347 µs** (−56 %; estimarea Cyber-GPU ~1 300) |
| simbolul fără verificare (kt median) | 5 802 µs (172 simb/s) | **4 083 µs (244,9 simb/s)** |
| „cu driverul” (rândul de viteză, aceeași măsură ca 94,84) | 94,84 simb/s | **109,11 simb/s** |
| placa pe simbol | 2 631 µs | 2 624 µs |
| cuvinte VRAM scrise pe simbol | — | 238 (SIMULARE: 48) |
| citirea logit-urilor / argmax | — | 47 / 85 µs |
- 16 simboluri din 16 identice cu procesorul; abaterea maximă 0x37880000 = exact ca în os-322 → logit-urile, după cât se poate vedea, identice; amprenta nouă `0xda9ae084`. Umbra lansărilor recitită identic. Viteza maximă P8 → P0, verdict 1.

## De lămurit — pârghia următoare
**Simbolul tipic (median) ține 4,08 ms = 245 simb/s, dar media pe toată generarea dă 109 simb/s** (și „ceasul plăcii, cu pauzele driverului” 119,8 simb/s pe 18 poziții ≈ 8,3 ms în medie). Deci câteva poziții sunt mult mai lente decât restul (~80 ms în plus pe toată generarea) — prima poziție / textul dat, sau altceva. Aceeași diferență exista și în os-322 (172 față de 94,84), doar că era ascunsă sub costul driverului.
→ Cyber-GPU (C-157) și OS (C-158): un rând `kt` cu timpul **fiecărei** poziții (nu doar mediana) și ce se întâmplă în pozițiile lente; după ce le scoatem, ținta e media aproape de mediană (~245 simb/s), peste Windows/PyTorch (129,12).
- Cuvintele VRAM pe simbol (238 față de 48 în SIMULARE) — de explicat de Cyber-GPU.

## Ce urmează pe placă
P3 (calculele lipite, predat de Cyber-GPU la 09:17) într-un Release separat al sesiunii OS.
