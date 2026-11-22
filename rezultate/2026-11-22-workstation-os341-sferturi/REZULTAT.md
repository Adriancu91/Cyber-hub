# os-341 pe placa reală — cursa înmulțirilor pe sferturi, 22 nov 2026 05:06

`test-placa --sferturi`, semnal 05:02. Raport: `rezultate/os-automat/2026-11-22/ciclu-auto-20261122-0506.txt`.

**TRECE.** Sferturi față de lipit: CORECT (aceleași simboluri, max |d| 1,1e-5). Mediana pe simbol pe placă 2 419 → **1 516 µs**; **media cu driverul 414,46 simb/s** (LayerNorm VECHI în această listă; os-336 cu LayerNorm nou: 347,17); doar lansările 661 simb/s. Cursa (µs pe simbol, lipit → sferturi): fc 486→224, proj 405→142, qkv 381→175, logit 186→87, out 149→72 — 5 feluri trec (regula +50 ‰), total +373 ‰. 16 simboluri identice, 0 poziții lente. Windows/PyTorch 129,12 → ×3,2 (limita: PyTorch fără memoria pașilor). Următorul: lista „sferturi + LayerNorm nou” (Cyber-GPU alege), așteptat ~450–500 simb/s (DEDUS).
