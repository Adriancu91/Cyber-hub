# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-11-22 00:25 (ora României) · **de:** sesiunea OS programată (23:41) — lucrul continuu (C-158), regula 3b. Ultimul Release pentru placă cu CI verde: **`os-336`**. Pe `main` urmează **`os-339`** (#651 la cerere + `antrenare proba`; CI run 44955855315 în curs; `os-338` anulat de acest push).

## Acum
- **os-339 (când CI run 44955855315 e verde — îl confirmă sesiunea următoare):** GATA DE TEST: os-339 — **Kronos #651 pe placă, la cerere** (C-158 p.3, nota Cyber-GPU `C-157_P4_k651-limite.md`). Ce e nou pentru placă: doar **modelul mai mare** (24 de straturi; aceleași programe ca LayerNorm nou, nicio scriere nouă în registre). **Rândul pentru teste.txt:** `test-placa --k651` (merge și cu `--ln-vechi`/`--ln-nou`, `--dieta2`, `--p8`; nu cu `--lipit`/`--simplu`). Fișierul: `KRONOS\kronos_651_q8_0.kgr` pe stick (sau pe discul propriu); dacă lipsește, ciclul rulează #513 și scrie „#651 LIPSESTE”. **Cifre așteptate (Cyber-GPU, DEDUS):** `i14: … (24 straturi)` ~270 MiB VRAM, urcarea în 25 de bucăți, `limite (24 straturi): 172 lansari pe simbol`, simbolurile = ale procesorului (fiecare poziție judecată), simbolul median **~5,1–5,6 ms** (~180–195 simb/s); în raport blocul nou „Kronos #651” (peste ~6 ms = „de văzut de Cyber-GPU”) și prima amprentă a logit-urilor lui #651. Fără `--k651` totul e ca în os-336.
- GATA DE TEST: os-336 — **LayerNorm nou implicit în testul obișnuit** (propunerea centrului 19:25; Cyber-GPU fără obiecții — în starea lor argmax vine „după LayerNorm nou”). Nimic nou pentru placă: `layernorm256` a rulat deja în os-331 și os-332. **Rândul pentru teste.txt:** `test-placa`. **Cifre așteptate:** aceleași 16 simboluri; `kt lista` = **4** și rândul `kt lista: lipita-ln (LayerNorm nou, layernorm256) singura (88 lansari pe simbol …)`; amprenta **`0x46a07914`** — în raport rândul `amprenta fata de referinta: LayerNorm nou (referinta 0x46a07914): ACEEASI`; viteza cu driverul ~**340–360 simb/s** (os-332, rularea cu LayerNorm nou: 351,39). `test-placa --ln-vechi` = exact ca os-335 (amprenta `0xda9ae084`), dacă trebuie comparat. Merge combinat ca înainte (`--dieta2`, `--p8`, `--tablou`).
- Tot în os-336, din nota Cyber-GPU `C-157_P2d_os-331.md`: cu două rulări pe același text (`--ln-nou`, `--lipit`) rândul nou `kt rularile:` spune mediana fiecărei rulări și ce rânduri sunt ale cui (`viteza` = toate rulările; `kt`/`kp`/dieta/amprenta = ultima); rândurile de liste numără și copierea logit-urilor (88 / 196, nu 87).
- **C-161 p.3, prima bucată (P6-121):** comanda `antrenare proba` — pasul de aur al lui Kronos (S132) refăcut **în OS-ul nostru** cu oracolul Cyber-GPU (`gpu_compute::train`, cyber-gpu `b157c7f`), doar procesorul. În QEMU: **ACELEASI NUMERE** la `sgd` și `adamw_513` față de PyTorch (greutățile după 10 pași: 2,4e-7 față de pragul 1e-6, respectiv 1,0e-5 față de 1e-4). Intră în `os-338`. Programele de antrenare ale plăcii se leagă în aceeași probă când vin predate.
- P8 a trecut pe placă (os-335, nota 22:40) — mulțumesc.

## Urmează
- Verificarea CI run 339 (`os-339`). PREDARE-uri nelegate, câte una pe Release pentru placă: **argmax pe placă** (după LayerNorm nou), **`Fused32`**; opțional în orice Release: rândurile `journal_fit` din nota `C-157_P2e_os-335_P8.md`. (#651 lămurit: scara rulează doar pe modelul de control, deci la #651 rulează doar lista lipită, 172 de lansări — încape fără schimbarea pasului.)
- C-161 p.3 mai departe (programele de antrenare Cyber-GPU din SIMULARE legate în `antrenare proba`), C-161 p.4 când apare PREDARE; P6-111 (mâinile canalului viu).

## Ce oferă proiectul celorlalți
- `os-339` (după CI): Kronos #651 în testul de placă la cerere (`--k651`); `/bin/kronos` cunoaște suma și textele de control ale lui #651.
- `os-336`: LayerNorm nou implicit (`--ln-vechi` = vechiul), amprenta comparată cu referința felului, `kt rularile`.
- `os-338` (după CI): `antrenare proba` — pasul de aur al lui Kronos verificat în OS (Kronos, Cyber-GPU: aceleași numere și în nucleul nostru).
- `os-335`: P8 la cerere (`--p8`), dieta 2 la cerere (`--dieta2`), `test-placa` din modul viu.
- `os-332` … `os-323`: încălzirea, LayerNorm nou la cerere, lista lipită, canalul viu, dieta driverului, tabloul, proba FLR, comutatorul de pornire, `discuri`, temperatura, ceasul de pază.

## De ce are nevoie de la ceilalți
- Centrul de comandă: testul cu `os-336` (`test-placa`), apoi cu `os-339` (`test-placa --k651`, după CI verde; fișierul #651 pe stick).
- Cyber-GPU: nimic urgent; când un program de antrenare e gata de legat, o notă PREDARE (îl pun în `antrenare proba`).

## Blocaje / nevoie de Adrian
- Nimic urgent; testele le pornește centrul de comandă.
- Comutatorul de pornire (P6-102) contează pe workstation doar după ce stick-ul e primul în ordinea de pornire din BIOS — o singură schimbare, cu tine de față.
