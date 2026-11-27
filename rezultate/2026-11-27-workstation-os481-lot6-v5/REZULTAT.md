# Lot 6 cu v5 în pas (nucleul os-481) — placa ×1,34, dar 71 ms pierduți în afara plăcii

- Rulat: 27 nov 07:42 (ciclul 07:49), pornit de centrul de comandă; rândul `test-placa --tablou-viteza --antrenare-mini --vram --antrenare-513 --placi3 --mm-placi --colsum-impartit --mixt-513 --mixt-513-rapid --lot-prin-ram --doua-locuri --atentie-tc16 --atentie-v4 --atentie-ds --pas-v5 --lot-513 6`.
- Toți cei 10 pași au rulat (fără oprire termică): temperatura 42–50 °C, „motivele încetinirii văzute: niciunul”, 169 W din 290.
- **Placa: 203,1 ms pe pas (mediană) = 15 128 simb/s** (prezis 202–222 → CONFIRMAT; os-465: 272,8) → **×1,34 pe placă; 38 % din Windows**.
- **Pasul întreg: 274,3 ms = 11 200 simb/s** — ~71 ms în afara plăcii (os-465: 0 µs), deși „două locuri: 18 părți trimise cât placa lucra, 0 amânate”. Pasul 6: 575 ms. Bănuiala: citirile tabloului de bord (`--tablou-viteza`, nou în rândul de lot 6) pe fiecare pas, sau așteptarea dintre cele două locuri. NU e record pe pasul întreg (11 270 rămâne), deși placa e mult mai rapidă.
- „NU TRECE” = criteriul sintetic „ultima pierdere < prima” la lot 6 (fără oracol, cunoscut din os-465); toate numerele finite, pierderea 1 = 9,8716 ≈ ln 16 384.
- Următorul: același rând FĂRĂ `--tablou-viteza` (dacă dispar cei 71 ms → ~15 000 simb/s).
- Sursa: `rezultate/os-automat/2026-11-27/ciclu-auto-20261127-0749.txt`, rândurile 178–241.
