# os-390 — pasul întreg al antrenării, tăiat (P6-174) — TRECE

**Data:** 24 nov 2026, pornire 07:37 (semnal 07:32). Rapoarte: `rezultate/os-automat/2026-11-24/ciclu-auto-20261124-0737.txt` și `-0740.txt`.

## Test 1: `test-placa --antrenare-mini --vram`
- **TRECE — ACELEAȘI NUMERE ca oracolul:** abaterea pierderii max 9,9e-8, a normei 6,3e-7, greutățile la sfârșit 8,8e-6 (toleranță 1e-3).
- **Pasul întreg median: 4 150 µs = 15 421 simboluri/s la antrenare** (prezis 4–5 ms / 13 000–16 000). Înainte (os-386/389): ~370 ms → **de ~89 de ori mai rapid**.
- Placa singură: 3 625 µs = 17 655 simb/s (ca os-386).
- Bucățile (median): plan lot 34, lot sus 49, listă 53, trimitere+așteptare 3 944 (din care așteptarea plăcii 3 525, golire VRAM 302, TLB 24, sonerie 9), pierderi+normă jos 70 µs.
- Tăieturi: **0 scrieri pe stick în timpul pașilor**.
- Primul pas 5,3 ms, al doilea 4,6 ms (încălzire), apoi constant ~4,1 ms.
- De verificat de OS: rândul „REZULTAT TEST PLACA” de la final spune „antrenare mini pe placa: niciun rezultat” deși blocul spune TRECE — doar rezumatul nu prinde rândul nou.

## Test 2: `test-placa --argmax-fara-copie --dieta2` (după FLR)
- TRECE 18/18; **632,84 simb/s** (driver 405 µs/simbol). Ca os-353/355.

## Comparație
Windows/PyTorch (FISA_ANTRENARE, #513) ~39 300 simb/s — dar alt model (mare); modelul mini nu e direct comparabil. Comparația corectă vine cu pasul #513 pe placă (P6-172).

## Următorul
os-392 `test-placa --antrenare-mini --vram --pas-lipit` (singurul lucru nou: 2 programe lipite).
