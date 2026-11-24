# os-413 — prima cursă de noapte a înmulțirilor (C-165, P6-190) — o variantă blocată, cursa neterminată; câștigătoarea pe prima formă ×1,50

**Data:** 24 nov 2026, pornire 22:23. Raport: `rezultate/os-automat/2026-11-24/ciclu-auto-20261124-2223.txt`.

## Pasul #513 (ca os-412)
- TRECE = oracolul (1,6e-5 / 9,6e-5); placa 463,4 ms, pasul întreg **474,1 ms = 2 159 simb/s** (os-412: 473,5).

## Cursa (doar forma 1 din 15: 1024 × 2304 × 768, ×12 în pas — qkv)
| variantă | µs median | TFLOP/s | biți |
|---|---|---|---|
| `mm_train_tile` (martorul) | 2 838,3 | 1,27 | = |
| `mm_tv_128x64` | 2 720,3 | 1,33 | = |
| `mm_tv_64x128` | 2 709,2 | 1,33 | = |
| **`mm_tv_128x128`** | **1 889,8** | **1,91** | **=** |
| `mm_tv_64x64k8` | — | — | **NETERMINAT** — placa nu a terminat (ultima înregistrare 0x0, așteptat 0x18f08) |

- Cursa s-a oprit la prima formă, după ce varianta `64x64k8` nu a terminat. **Placa și-a revenit singură:** generarea de după a mers (aceleași 16 simboluri ca procesorul, amprenta 0x6c8501f0), sistemul a revenit în Windows și a trimis raportul. Nicio problemă de siguranță văzută.
- **`128x128` e de 1,50 ori mai rapidă** decât `mm_train_tile` pe forma qkv, cu aceiași biți. Dacă se ține pe toate formele: înmulțirile ~430 → ~285 ms, pasul ~474 → ~330 ms ≈ 3 100 simb/s (DEDUS, o singură formă măsurată).
- Rândul „pasul ar scădea cu ~0 µs” e doar pentru că cursa nu s-a terminat.

## Cereri (C-157/C-165)
1. Cyber-GPU: de ce `mm_tv_64x64k8` nu termină (doar ea; `34 registre`, felia K 8) — de scos din cursă până se lămurește.
2. OS: cursa din nou **fără `64x64k8`**, pe toate cele 15 forme; plus A4 (P6-192) cu citirile în timpul pașilor.
3. Cyber-GPU: pregătiți legarea lui `128x128` în pas (`Plan::with_mm_tile` cu varianta aleasă pe formă) — se leagă după ce cursa completă confirmă.
