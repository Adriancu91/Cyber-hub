# os-392 — pasul lipit al antrenării pe placa reală (P6-175) — TRECE

**Data:** 24 nov 2026, pornire 08:19. Rapoarte: `rezultate/os-automat/2026-11-24/ciclu-auto-20261124-0819.txt` și `-0821.txt`.

## Test 1: `test-placa --antrenare-mini --vram --pas-lipit`
- Singurul lucru nou pentru placă: 2 programe lipite (`ln_back_res`, `mm_train_gelu`) — **au mers din prima**.
- **Lipit = nelipit bit cu bit:** 69 lansări în loc de 75; 10/10 pași cu aceeași pierdere și normă; greutățile ACEIAȘI BIȚI (0 diferite din 1 150 720). Ambele = oracolul (pierdere 9,9e-8, normă 6,3e-7, greutăți 8,8e-6).
- Placa: 3 602 µs lipit vs 3 628 µs nelipit (−0,7%) = 17 767 simb/s.
- **Pasul întreg: 4 141 µs = 15 455 simb/s** (os-390: 4 150 / 15 421).
- Bucăți: așteptarea plăcii 3 503 µs (85%), golire VRAM 299, pierderi jos 71, pushbuffer 71 µs. 0 scrieri pe stick în pași.
- Concluzie: pentru modelul mini câștigul din lipire e mic (lansările sunt deja ieftine); placa e acum cea care contează — urmează bf16 (`--mixt`) și pasul #513.
- Același mic defect ca la os-390: rezumatul final spune „antrenare mini: niciun rezultat”.

## Test 2: `test-placa --argmax-fara-copie --dieta2` (după FLR)
- TRECE 18/18; **636,13 simb/s**.
