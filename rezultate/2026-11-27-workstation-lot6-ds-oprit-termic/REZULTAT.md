# Lot 6 cu dS pe circuite (nucleul os-476) — OPRIT de paza termică după pasul 2

- Rulat: 27 nov 01:38 (ciclul 01:44), pornit de centrul de comandă; rândul `test-placa --tablou-viteza --antrenare-mini --vram --antrenare-513 --placi3 --mm-placi --colsum-impartit --mixt-513 --mixt-513-rapid --lot-prin-ram --doua-locuri --atentie-tc16 --atentie-v4 --atentie-ds --lot-513 6`.
- Rândul a fost acceptat; antrenarea mini TRECE; arena 4 690 MiB urcată în 419 ms.
- #513 lot 6: pasul 1 placa 278,3 ms; **pasul 2 placa 264,9 ms** (os-465 fără dS pe circuite: 272,6 ms pe pas întreg) → indiciu ~11 600 simb/s pe placă, NEconfirmat (doar 2 pași, fără oracol, fără medie).
- **Apoi: „ceasul termic după pasul 2: OPRIRE: încetinire termică / de urgență (motive 0x20); proba oprită, fără reîncercare”.** Paza a făcut ce trebuia: a oprit, placa a revenit, Kronos a scris apoi 16 simboluri corecte.
- Prima dată când ceasul termic (pornit de `--tablou-viteza`) rulează la lot 6; os-465 (lot 6) a rulat fără el, deci nu știm dacă încetinirea era și atunci.
- De lămurit (Cyber-GPU / OS): ce înseamnă exact 0x20 pe această placă (încetinire termică din software vs. de urgență), ce temperatură avea placa (rândurile tabloului lipsesc din raport), dacă 0x20 apare și la lot 2. Până atunci: fără alte probe lungi la lot 6 în noaptea asta.
- Sursa: `rezultate/os-automat/2026-11-27/ciclu-auto-20261127-0144.txt`, rândurile 167–180.
