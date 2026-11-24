# Viteza legăturii după mutarea plăcii în SLOT2 (x16) — TRECE, de 2 ori mai rapid

**Data:** 24 nov 2026. Placa mutată de Adrian la 13:17 din SLOT1 („PCIe3X16 (8,4,1)”) în SLOT2 („PCIe3X16 75W”). Dell a șters intrarea de pornire a stick-ului după schimbare; o repornire din Windows (13:51) a refăcut-o. Pornire 13:56 cu os-403. Rapoarte: `ciclu-auto-20261124-1356.txt`, `-1401.txt`.

## Test 1: `test-placa --ram-vram` (os-376 refăcut)
| | SLOT1 x8 (23 nov) | **SLOT2 x16 (azi)** | prezis |
|---|---|---|---|
| sus RAM → VRAM | 5,97 GB/s | **12,38 GB/s** (×2,07) | 11–13 |
| jos VRAM → RAM | 6,76 GB/s | **13,53 GB/s** (×2,00) | 11–13,5 |
- Octeți corecți; 4 copii în paralel nu adaugă nimic (plafonul e legătura). 12,4/13,5 GB/s ≈ 79/86 % din plafonul brut gen3 x16 (15,75 GB/s) — normal.

## Test 2: `test-placa --antrenare-mini --vram --lot-ram`
- TRECE ambele variante (bit cu bit, = oracolul). Arena urcată în 2,44 ms (înainte ~4,9 ms), adusă înapoi în 2,06 ms (înainte 4,1 ms).
- Pasul întreg: 3 921 µs = 16 322 simb/s (os-397: 3 935). Pasul mini nu depinde de legătură, cum era de așteptat.

## Urmări
- Problema PCIe din 23 nov 20:11 e rezolvată (cât se poate pe Precision 5820: toate sloturile sunt gen3).
- Ridicarea condiției „nimic din antrenare în RAM” = decizia lui Adrian.
