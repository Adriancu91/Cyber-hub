# os-397 — lotul și rezultatele pasului prin RAM (P6-178) — TRECE

**Data:** 24 nov 2026, pornire 11:14 (aprobat de Adrian 11:04, excepție limitată doar pentru lot). Rapoarte: `ciclu-auto-20261124-1114.txt`, `-1116.txt`.

## Test 1: `test-placa --antrenare-mini --vram --lot-ram`
- **TRECE:** prin RAM = prin fereastră bit cu bit (10/10 pași, greutățile ACEIAȘI BIȚI), ambele = oracolul.
- 82 de lansări pe pas în loc de 75.
- **Pasul întreg 3 935 µs = 16 264 simb/s** (os-392: 4 142 µs / 15 455; prezis ~3,8 ms / 16 700).
- Bucăți: pierderile jos 71 → **3 µs**; golirea VRAM 299 → 98 µs; lotul sus 49 → 37 µs (prezis ~2); placa 3 625 → 3 659 µs (+34 µs pentru cele 7 copieri).
- Așteptarea plăcii: 3 559 µs din 3 935 (90%). În afara plăcii au rămas ~280 µs.

## Test 2: `test-placa --argmax-fara-copie --dieta2`
- TRECE 18/18; 633,06 simb/s.

## Concluzie
Pe modelul mini, timpul din afara plăcii e aproape tăiat complet. Ce mai contează acum e calculul plăcii, la #513: bf16/tensor cores (vezi os-395).
