# os-407 — pasul #513 corect (= oracolul) + atenția pe plăci — TRECE amândouă

**Data:** 24 nov 2026, pornire 16:08. Rapoarte: `ciclu-auto-20261124-1608.txt`, `-1612.txt`.

## Test 1: `--antrenare-513` (verdict nou: oracolul procesorului)
- **TRECE — ACELEAȘI NUMERE ca procesorul** în pașii 1–9 (pierdere 2,3e-5, normă 1,1e-4; toleranță 1e-3). Pierderea care urca pe loturi sintetice (os-395) era deci corectă, nu o greșeală.
- 1 124 ms/pas = 910 simb/s (ca os-403).

## Test 2: `--antrenare-513 --placi3` (atenția pe plăci gen 3)
- **TRECE** = oracolul (1,5e-5 / 9,4e-5).
- **Atenția: 371 ms → ~20,5 ms pe pas** (fwd 6,2 + back 9,2 + 5,2 ms) — ×18.
- **Pasul: 1 124 → 778 ms = 1 315 simb/s** (pasul întreg 761 ms = 1 345). Prezis: 770–800 ms / ~1 300. ✔
- Acum `mm_train` (~718 ms) e ~92 % din pas → `mm_train_tile` (Cyber-GPU sesiunea 208, ×3–6 estimat) e următorul.

Windows/PyTorch: ~39 300 simb/s (bf16, lot 12 × 512) — banc identic în lucru (C-162).
