# os-395 — pasul de antrenare al lui Kronos #513 pe placa reală (P6-172) — RULEAZĂ, dar NU TRECE + lent

**Data:** 24 nov 2026, pornire 10:58. Rapoarte: `rezultate/os-automat/2026-11-24/ciclu-auto-20261124-1058.txt` și `-1100.txt`.

## Ce a mers
- Antrenarea mini cu arena în VRAM: TRECE (= oracolul), ca în os-390.
- #513 (98 032 128 greutăți, lot 2 × 512, context 512) a rulat cap-coadă pe placă: arena 2 560 MiB urcată în VRAM în 41 de bucăți, 450 ms; 10 pași, 385 de lansări în 2 trimiteri; **toate cele 98 de milioane de greutăți finale sunt numere** (0 NaN/Inf). Prima rulare a unei arene de GiB — fără blocaj.
- Test 2 (`--argmax-fara-copie --dieta2`, după FLR): TRECE 18/18.

## Ce NU a mers
1. **Criteriul „ultima pierdere sub prima” a picat:** pasul 1 9,849 (ln 16 384 = 9,704; +1,5%, în limita de 2%), pasul 10 **10,177**. Norma gradientului scade normal (3,27 → ~0,9), dar urcă la 1,65 la pasul 10.
   - Atenție: loturile sunt **sintetice (aleatoare, MT19937)**; pe date aleatoare pierderea nu are ce învăța, deci nu e sigur că e o greșeală de calcul. Lipsa oracolului pe procesor înseamnă că nu știm încă. **Cerere Cyber-GPU:** oracol pe procesor pentru 1–2 pași #513 (chiar lent) sau aceleași 10 pași #513 în PyTorch pe Windows cu aceleași loturi, ca să se vadă dacă 10,18 e corect.
2. **Viteza: 911 simboluri/s pe placă (1,123 s/pas), pasul întreg 936 simb/s.** Windows/PyTorch #513: ~39 300 simb/s → **de ~43 de ori mai lent**.
   - Mini (os-390) e rapid pentru că modelul e de 85 de ori mai mic; la #513 contează calculele mari (înmulțiri F32 fără tensor cores, atenție pe context 512, backward).
   - **Cerere Cyber-GPU:** timpul pe fel de program (ca la generare: qkv, atenție, fc, logit, backward, AdamW) pentru pasul #513, ca să știm unde se duce secunda. Apoi: bf16/tensor cores (P8, deja verificate la generare) în înmulțirile antrenării.
3. Mic: „placa 1 149 541 µs” > „pasul întreg 1 115 457 µs” la pasul 1 — cele două ceasuri nu se potrivesc (de verificat de OS).
