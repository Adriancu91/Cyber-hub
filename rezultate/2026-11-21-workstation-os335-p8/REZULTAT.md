# os-335 pe placa reală — P8, primul calcul cu circuitele speciale (tensor cores), 21 nov 2026 ~22:21

Pornit de centrul de comandă (stick verificat identic, `ceas 40` + `test-placa --p8`, semnal 22:17). Raport: `rezultate/os-automat/2026-11-21/ciclu-auto-20261121-2221.txt`. Aprobat de Adrian: DECIZII.md 21 nov 16:18.

## Verdict: TRECE
- `P8 (mma16): TRECE: 6 / 6 seturi in toleranta, identitate 256/256 exacte, abaterea maxima 148 promile din toleranta, timp median 6144 ns`.
- Programul `mma16_f16` (1 248 octeți, SHA-256 `f8c0db68b654372d…`), 6 trimiteri, rulat după textele lui #513.
- 642 / 1 536 de elemente exacte; niciun model de rotunjire din lista Cyber-GPU nu se potrivește pe toate seturile (de lămurit de Cyber-GPU cum adună GA104 — rezultatul e oricum în toleranță).
- Restul testului neatins: 16 simboluri identice cu procesorul, amprenta `0xda9ae084` (ca os-329), 0 poziții lente; media cu driverul **305,15 simb/s** (LayerNorm vechi; os-332 cu LayerNorm nou: 351,39); driverul 774 µs pe simbol (os-332: 818).
