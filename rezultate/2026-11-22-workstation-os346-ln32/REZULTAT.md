# os-346 pe placa reală — lista `lipita-ln-32` (sferturi + LayerNorm nou), 22 nov 2026 10:06

`test-placa --ln-32`, semnal 10:02. Raport: `rezultate/os-automat/2026-11-22/ciclu-auto-20261122-1006.txt`.

**TRECE.** Față de `lipita-ln`: CORECT (aceleași simboluri, max |d| 1,0e-5). 16 simboluri identice cu procesorul, 0 poziții lente. Mediana pe simbol: placa **1 071 µs**, driver 825, jurnal 60 = 1 986 µs. **Media cu driverul 508,74 simb/s** (doar lansările 935,90). Windows/PyTorch 129,12 → ×3,9 (limita: PyTorch fără memoria pașilor). Acum driverul (825 µs) e aproape cât placa → dieta 2 e următorul câștig mare.
