# Rezultat: fără scriere pe stick în generare + lista lipită implicită (os-329, ciclu automat) — 21 nov 2026, 15:56

- **Unde:** workstation (RTX 3070 Ti), ciclul automat, fără om de față. Semnal ~15:49, test 15:56, raport urcat singur.
- **Versiunea:** `os-329` (P6-112 pozițiile lente, lista lipită implicită; P6-113 `live.cheie` secret). Rândul: `test-placa`.
- **Fișierele brute:** `rezultate/os-automat/2026-11-21/ciclu-auto-20261121-1556.txt`, `gpu-jurnal-027.txt`, `gpu-jurnal-028.txt`.

## Ce era nou: jurnalul nu mai scrie pe stick între poziții — MERGE; media a urcat de la 120 la 262 simb/s
| | os-322 (20 nov) | os-328 (azi 12:56, lipit) | **os-329 (azi 15:56)** |
|---|---|---|---|
| **media cu driverul, jurnalul și ecranul** (toate cele 18 poziții) | 94,84 | 120 | **262,04 simb/s** |
| cu pauzele driverului, pe ceasul plăcii | — | — | **287,89 simb/s** |
| simbolul median | 5 802 µs | 3 284 µs | 3 338 µs (299,6 simb/s) |
| doar placa | 381,98 | 413,6 | 413,56 simb/s |
| driverul pe simbol (median) | 3 081 µs | 759 µs | 844 µs |
| poziții lente (peste 2 × mediana) | — | 2 (0 și 16; 91 ms în plus) | **1 (poziția 0; 8,9 ms în plus)** |
- 16 simboluri din 16 identice cu procesorul; amprenta logit-urilor `0xda9ae084` (aceeași ca os-324 și os-328); 0 rânduri de rutină aruncate; „nicio scriere pe stick între poziții”; 130 de cuvinte VRAM pe simbol.
- Poziția 0: 12 250 µs = placa 2 320 + jurnal 67 + **driver 9 863** (pregătirea de la prima poziție) — singura rămasă.
- Viteza maximă: înainte P0, verdict 2 (fără efect), la final P0.

## Față de Windows — am trecut, pe tot drumul
**Același Kronos #513, aceleași 16 simboluri, același calculator:** în Windows, prin PyTorch și driverul fabricantului, **129,12 simb/s** (S130, 20 nov; FP32, fără memoria de context „KV cache”, cum rulează Kronos acolo). La noi, pe tot drumul (driver + jurnal + ecran), **262,04 simb/s în medie** → **de 2,03 ori**. Procesorul: 72,72.
Cinstit: comparația e cu felul în care rulează Kronos azi în Windows, nu cu cel mai bun PyTorch posibil (cu „KV cache” și compilare, PyTorch ar putea fi mai rapid decât 129).

## Ce urmează
- Poziția 0 (driverul ~10 ms la prima poziție) → Cyber-GPU, C-157 punctul 3 (dieta a doua, predată 15:30).
- LayerNorm nou (P6-114, sesiunea OS de la 15:43), argmax pe placă, apoi #651.
