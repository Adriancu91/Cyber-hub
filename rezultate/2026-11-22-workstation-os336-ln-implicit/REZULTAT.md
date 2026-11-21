# os-336 pe placa reală — LayerNorm nou implicit, 22 nov 2026 00:06

Pornit de centrul de comandă (`ceas 40` + `test-placa`, semnal 00:00). Raport: `rezultate/os-automat/2026-11-22/ciclu-auto-20261122-0006.txt`.

**TRECE.** O singură listă (`lipita-ln`, 88 de lansări pe simbol), amprenta `0x46a07914` = ACEEAȘI, 16 simboluri identice cu procesorul, 0 poziții lente. **Media cu driverul 347,17 simb/s** într-o singură rulare (os-332, a doua rulare: 351,39); mediana 2 900 µs (placa 1 977, driver 814, jurnal 64). Windows/PyTorch 129,12 → ×2,69 (limita comparației: fără memoria pașilor în PyTorch).
