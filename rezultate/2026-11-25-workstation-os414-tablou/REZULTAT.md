# os-414 — tabloul plăcii citit ÎN TIMPUL pașilor #513 (A4, P6-192) — frâna NU e ceasul

**Data:** 25 nov 2026, pornire 00:18. Raport: `rezultate/os-automat/2026-11-25/ciclu-auto-20261125-0018.txt`. Rulat fără `--cursa-mm` (os-414 avea încă varianta blocată `mm_tv_64x64k8`).

| În timpul celor 10 pași #513 | valoare |
|---|---|
| ceasul nucleului | **1 950 MHz** (constant; 110 % din boost-ul public 1 770) |
| ceasul memoriei | 9 501 MHz (constant) |
| încărcarea nucleului | 100 % (mediana) |
| puterea | **127 W** mediana (90–140) din 290 W — **44 %** |
| starea P | P0 ×10 |
| motivele încetinirii | **niciunul** |
| temperatura maximă | 50 °C |

- Pasul #513: 474,3 ms = 2 159 simb/s, TRECE = oracolul (ca os-412/413).
- **Concluzie:** placa merge la ceasul maxim, fără nicio frână de putere sau temperatură, dar consumă doar 44 % din putere. Deci **programul de înmulțire nu ține unitățile de calcul ocupate** (așteaptă după memorie / ocupare / instrucțiuni). Bănuiala „ceasul / starea P” e exclusă. Calea e cea din cursă: plăci mai mari (`128x128`: ×1,50 pe qkv), apoi tensor cores.
- Bonus: placa e rece (50 °C), deci avem tot spațiul termic pentru lucru mai greu.
