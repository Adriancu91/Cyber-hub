# Workstation (GA104) — 19 nov 2026 14:27–14:45, os-308 (cyber-gpu e74b418, C-145/C-146), al doilea ciclu automat, fără Adrian de față

- Pregătire (centrul de comandă): Release `os-308` (CI verde la a doua rulare a părții 2/2; arhiva SHA-256 `7671558d…c2eb` = SHA256SUMS; VERSIUNE commit `0822b5c`); pe stick doar `BOOT\kernel` (14.255.848 B), `BOOT\initrd.tar`, `VERSIUNE`, recitite cu sume identice; `auto\teste.txt` pus din nou (`ceas 40` + `test-placa`; cel de dimineață se consumase → `teste-facut-20261119-0848.txt`). Semnal la 14:27 → paznicul → pornire pe stick.
- 14:37 raportul `rezultate/os-automat/2026-11-19/ciclu-auto-20261119-1437.txt` + `gpu-jurnal-012.txt` (recupereaza) + `gpu-jurnal-013.txt` au urcat singure; test 197 s; apoi repornire → Windows, workstation-ul răspunde din nou prin aplicația Claude (~14:50).
- Lanțul I0→I14: toți pașii au trecut (2.895 de scrieri). **Kronos #513: 16 simboluri pe placă, toate identice cu procesorul**, același text ca dimineața (`,\nImi doresc sa ma intorc la mine,\nSa ma`); abaterea maximă a logit-urilor 1,75·10⁻⁵.
- **Viteza, față de os-307 (08:52):**
  | | os-307 | os-308 |
  |---|---|---|
  | lansările pe placă (ceasul plăcii) | 43,93 simb/s | 43,82 simb/s |
  | cu driverul, jurnalul și ecranul | **3,10 simb/s** (294,8 ms) | **10,99 simb/s** (86,8 ms) |
  - timpul pe simbol (`kt`, median): placă 22,96 ms · driver 0 ms · **jurnal 73,9 ms** · ecran 0 → 11,51 simb/s; „umbra lansărilor” recitită la final: identică (placa nu rescrie sloturile); jurnalul: 646 de rânduri de rutină ținute în memorie, scrise în 24 de goliri (o dată pe simbol).
  - verificarea pe procesor (motorul de referință, 1 nucleu) rămâne separată: 3,85 s pe poziție (0,25 simb/s — cifra „0,25 cu pauzele” din raport o include); motorul optimizat al OS-ului pe procesor: 72,7 simb/s.
- **Concluzie:** reparația C-145 a scos rescrierea lansărilor (driver 41 → 0 ms) și a mutat jurnalul în memorie → **×3,5**. Ce a mai rămas e aproape tot golirea jurnalului pe stick o dată pe simbol (~74 ms); cu golire doar la final, ținta e ~40+ simb/s (cât fac lansările). Pas următor propus lui Adrian.
