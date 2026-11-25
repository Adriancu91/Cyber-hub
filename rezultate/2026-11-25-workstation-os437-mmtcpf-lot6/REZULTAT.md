# os-437 · `mm_tc_pf` + lotul 6 + agentul cu veghe — rezultate

- **Când:** 25 nov 2026, 17:02 (testul 1) și 17:07 (testul 2, aceeași pornire); rapoarte `rezultate/os-automat/2026-11-25/ciclu-auto-20261125-1702.txt`, `…-1707.txt`; agentul `live/os-agent.md`, `rezultate/os-automat/2026-11-25/agent-20261125.txt`.

## 1. `--mm-tc --mm-tc-pf` — TRECE
- `mm_tc_pf` = **aceiași biți ca `mm_tc` pe toate 6 seturile**, inclusiv qkv-513.
- qkv-513: `mm_tc` 21,15 ms (1,02 TFLOP/s) → **`mm_tc_pf` 7,88 ms = 2,75 TFLOP/s (×2,68)**. Prezis 3–5 → sub țintă, dar citirile în avans sunt confirmate ca frână.
- Încă sub `mm_train_tile` cu treapta (3,48) și `64x64k8` (3,61) pe F32. Mai lipsesc: treapta potrivită pentru `mm_tc` (24 KiB + 248 registre → tot 1 bloc pe unitate, DEDUS) și citirile de 128 de biți (`mm_tc_v4`, 128 registre).

## 2. `--lot-513 6` — arena încape, viteza ×1,25, verdict „NU TRECE” fals (DEDUS)
- `arena 4 689 MiB + zona lansărilor + rezerva 256 MiB încap` (VRAM liber 7 474 MiB) — arena fără plafon merge.
- **Placa 637,9 ms pe pas = 4 816 simb/s; pasul întreg 656,4 ms = 4 680 simb/s** (lotul 2, os-431: 3 837) → **×1,22–1,25**. Pe F32 placa e deja aproape plină: lotul mare ajută puțin până nu trecem pe circuitele speciale.
- „NU TRECE” vine din criteriul „ultima pierdere sub prima”, aplicat **pe loturi sintetice aleatoare** (nu se pot învăța): și la lotul 2 (os-431) pierderea a urcat 9,849 → 10,174, dar acolo oracolul a dat „ACELEASI NUMERE”. La lotul 6 nu există oracol. Pierderea la pasul 1 = 9,8716 ≈ ln 16 384, toate numerele finite, norma scade 1,85 → 0,53 → **pasul pare corect**; de confirmat.
- **Cerere OS:** (a) la lot > 2 pe date sintetice criteriul = pasul 1 ≈ 9,7 ± 2 %, toate finite, norma finită (fără „scade”); sau (b) date reale pe stick (`/usb/antrenare/date/index.json`) — preferabil, ca să vedem și învățarea; sau (c) oracolul lotului 6 = trei loturi de 2 cumulate (dacă e ieftin).

## 3. Agentul de bord cu veghe — MERGE, de corectat 3 lucruri
- Veghea a scris singură în hub (`live/os-agent.md`), cu cache (3 600–4 300 simboluri citite din cache); **cost ~0,11–0,14 $ pe rezumat** (mare parte din ieșire: 600–840 simboluri) → la 10 min ≈ 0,8 $/oră.
- **(1) Adresa MAC a plăcii de rețea apărea în hub** (rândul `net`) — regula lui Adrian: niciun MAC / serial în hub. Am ascuns-o de mână (17:35). **OS: `net` în veghe fără MAC** (și fără alte serii).
- **(2) Rezumatul a citit greșit două rânduri de rutină ca erori:** „tur-dupa ESUAT” și cele 11 scrieri refuzate la `i8e-golden` apar la fiecare pornire (paza lucrează corect). OS: în instrucțiunile agentului, lista rândurilor normale.
- **(3) Rezumate mai scurte** (≤ 250 de simboluri ieșire) → ~3× mai ieftin.
