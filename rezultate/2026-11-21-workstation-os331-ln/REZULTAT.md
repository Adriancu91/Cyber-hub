# os-331 pe placa reală — LayerNorm nou (P6-114), 21 nov 2026 ~17:26

Test pornit de centrul de comandă (stick verificat identic, `ceas 40` + `test-placa --ln-nou`, semnal 17:22). Raport: `rezultate/os-automat/2026-11-21/ciclu-auto-20261121-1726.txt`, jurnal `gpu-jurnal-030.txt`.

## Verdict: TRECE
- LayerNorm nou față de vechi: `max |d| = 6.914139e-6` (prag 1e-4), **simboluri identice: da**, `TRECE`.
- 16 simboluri identice cu procesorul, ambele rulări: [44, 10, 73, 2524, 10766, 1438, 1505, 1428, 1765, 99, 1547, 3644, 44, 10, 15879, 1505]; abaterea maximă față de procesor 1,74e-5.
- Amprenta logit-urilor se schimbă (LayerNorm nou): **0x46a07914** (os-329: 0xda9ae084) — de așteptat, calculul e altul; simbolurile aceleași.

## Cifre (rularea cu LayerNorm nou)
| | os-329 | os-331 |
|---|---|---|
| LayerNorm pe lansare | ~21,8 µs | **~4 µs** (ln1 48 µs/simbol, ln2 46, ln_final 4) |
| placa pe simbol (median) | 2 420 µs | **1 977 µs** (506,88 simb/s doar lansările) |
| driverul pe simbol (median) | 844 µs | 819 µs |
| simbolul median (placă + driver + jurnal) | 3 338 µs | **2 885 µs** |
| **media cu driverul** | **262,04 simb/s** | **348,47 simb/s** |
| poziții lente | 1 (poziția 0) | 0 |
| Kronos în Windows/PyTorch (#513, 20 nov) | 129,12 | → **de 2,70 ori** |

## Cinstit
- Câștigul LayerNorm-ului: **~0,45 ms pe simbol**, exact cât a estimat Cyber-GPU (DEDUS → MĂSURAT).
- **„0 poziții lente” vine din faptul că rularea cu LayerNorm nou e a doua în aceeași pornire** (placa deja „încălzită” de prima rulare). Reparația poziției 0 pentru o singură rulare e os-332 (în lucru la OS). Cifra 348 e deci a doua rulare; după os-332 se măsoară pe prima.
- Comparația cu Windows rămâne „cu felul în care rulează Kronos azi în Windows” (F32, fără KV cache), nu cel mai bun PyTorch posibil.
- Restul lanțului: `oprit la tur-dupa` = sfârșitul obișnuit al ciclului (ca la os-329).

## Ce urmează
Cel mai mare cost pe placă acum: înmulțirile (fc 487, proj 405, qkv 381 µs pe simbol) → cursa înmulțirilor (C-155 p.4, predată) și, mai departe, circuitele speciale (P8). Driverul: 819 µs → dieta 2 (predată, țintă ~330–410 µs).
