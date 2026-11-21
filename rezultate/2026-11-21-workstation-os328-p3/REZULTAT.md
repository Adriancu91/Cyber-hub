# Rezultat: P3, „calculele lipite”, pe placa reală (os-328, ciclu automat) — 21 nov 2026, 12:56

- **Unde:** workstation (RTX 3070 Ti), ciclul automat, fără om de față. Semnal ~12:49, test 12:56, raport urcat singur.
- **Versiunea:** `os-328` (`13582db`), cyber-gpu `46078f4`. Rândul: `test-placa --lipit` (#513 de două ori pe același text: lista simplă, apoi cea lipită).
- **Fișierele brute:** `rezultate/os-automat/2026-11-21/ciclu-auto-20261121-1256.txt`, `gpu-jurnal-025.txt`, `gpu-jurnal-026.txt`.

## Ce era nou: lista lipită (88 de lansări pe simbol în loc de 196) — MERGE, mai bine decât estimarea
| pe simbol (median) | os-324, lista simplă | **os-328, lista lipită** |
|---|---|---|
| simbolul fără verificare | 4 083 µs (245 simb/s) | **3 284 µs (304,5 simb/s)** (estimat ~3 600) |
| placa | 2 624 µs | **2 421 µs** (413,6 simb/s doar lansările) |
| driverul | 1 347 µs | **759 µs** |
| cuvinte VRAM scrise | 238 | **130** (estimat ~130) |
- 16 simboluri din 16 identice cu procesorul; abaterea maximă 0x37880000; **amprenta tuturor logit-urilor `0xda9ae084` = exact cea din os-324** (lista simplă) → lista lipită dă aceleași numere bit cu bit.
- Viteza maximă: P5 → P0, verdict 1.

## Pozițiile lente (rândurile noi, doar citiri de ceas) — confirmă analiza Cyber-GPU
2 din 18 poziții peste 2 × mediana, 91 ms în plus: **poziția 0** = 17,4 ms (jurnal 13,4 ms) și **poziția 16** = 80,4 ms (**jurnal 77,2 ms**). De aceea media listei lipite e 120 simb/s, deși mediana e 304,5. Vinovatul e scrierea jurnalului pe stick în mijlocul generării (reparația: P6-112).

## De lămurit de sesiunea OS
1. Rândul anunțat `kt lipit fata de simplu: identice …` **lipsește** din jurnal și din raport (identitatea se vede doar din amprentă).
2. Prima rulare (lista simplă) a ieșit la **17,57 simb/s** „cu pauzele driverului” (în os-324 aceeași listă: 119,8) — o pauză de ~0,9 s undeva în prima generare; probabil tot o scriere pe stick. Rândul de viteză „cu driverul” (31 simb/s) amestecă cele două texte și nu e de folosit.

## Ce urmează pe placă
P6-112 (fără scriere pe stick în mijlocul generării) → ținta: media ≈ mediana, ~300 simb/s, peste Windows/PyTorch (129,12). Apoi LayerNorm nou.
