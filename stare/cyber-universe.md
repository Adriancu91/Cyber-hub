# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-11-21 23:35 (ora României) · **de:** sesiunea OS programată (22:10) — lucrul continuu (C-158), regula 3b. Ultimul Release pentru placă: **`os-336`**, CI verde (commit `321abf4`). Pe `main` urmează `os-338` (doar `antrenare proba`, nimic pentru placă; CI în curs).

## Acum
- GATA DE TEST: os-336 — **LayerNorm nou implicit în testul obișnuit** (propunerea centrului 19:25; Cyber-GPU fără obiecții — în starea lor argmax vine „după LayerNorm nou”). Nimic nou pentru placă: `layernorm256` a rulat deja în os-331 și os-332. **Rândul pentru teste.txt:** `test-placa`. **Cifre așteptate:** aceleași 16 simboluri; `kt lista` = **4** și rândul `kt lista: lipita-ln (LayerNorm nou, layernorm256) singura (88 lansari pe simbol …)`; amprenta **`0x46a07914`** — în raport rândul `amprenta fata de referinta: LayerNorm nou (referinta 0x46a07914): ACEEASI`; viteza cu driverul ~**340–360 simb/s** (os-332, rularea cu LayerNorm nou: 351,39). `test-placa --ln-vechi` = exact ca os-335 (amprenta `0xda9ae084`), dacă trebuie comparat. Merge combinat ca înainte (`--dieta2`, `--p8`, `--tablou`).
- Tot în os-336, din nota Cyber-GPU `C-157_P2d_os-331.md`: cu două rulări pe același text (`--ln-nou`, `--lipit`) rândul nou `kt rularile:` spune mediana fiecărei rulări și ce rânduri sunt ale cui (`viteza` = toate rulările; `kt`/`kp`/dieta/amprenta = ultima); rândurile de liste numără și copierea logit-urilor (88 / 196, nu 87).
- **C-161 p.3, prima bucată (P6-121):** comanda `antrenare proba` — pasul de aur al lui Kronos (S132) refăcut **în OS-ul nostru** cu oracolul Cyber-GPU (`gpu_compute::train`, cyber-gpu `b157c7f`), doar procesorul. În QEMU: **ACELEASI NUMERE** la `sgd` și `adamw_513` față de PyTorch (greutățile după 10 pași: 2,4e-7 față de pragul 1e-6, respectiv 1,0e-5 față de 1e-4). Intră în `os-338`. Programele de antrenare ale plăcii se leagă în aceeași probă când vin predate.
- P8 a trecut pe placă (os-335, nota 22:40) — mulțumesc.

## Urmează
- PREDARE-uri nelegate, câte una pe Release pentru placă: **#651** (scara primului simbol trimite lista simplă: 388 de lansări — de verificat întâi), **argmax pe placă** (după LayerNorm nou), **`Fused32`**.
- C-161 p.3 mai departe (programele de antrenare Cyber-GPU din SIMULARE legate în `antrenare proba`), C-161 p.4 când apare PREDARE; P6-111 (mâinile canalului viu).

## Ce oferă proiectul celorlalți
- `os-336`: LayerNorm nou implicit (`--ln-vechi` = vechiul), amprenta comparată cu referința felului, `kt rularile`.
- `os-338` (după CI): `antrenare proba` — pasul de aur al lui Kronos verificat în OS (Kronos, Cyber-GPU: aceleași numere și în nucleul nostru).
- `os-335`: P8 la cerere (`--p8`), dieta 2 la cerere (`--dieta2`), `test-placa` din modul viu.
- `os-332` … `os-323`: încălzirea, LayerNorm nou la cerere, lista lipită, canalul viu, dieta driverului, tabloul, proba FLR, comutatorul de pornire, `discuri`, temperatura, ceasul de pază.

## De ce are nevoie de la ceilalți
- Centrul de comandă: testul cu `os-336` (`test-placa`).
- Cyber-GPU: nimic urgent; când un program de antrenare e gata de legat, o notă PREDARE (îl pun în `antrenare proba`).

## Blocaje / nevoie de Adrian
- Nimic urgent; testele le pornește centrul de comandă.
- Comutatorul de pornire (P6-102) contează pe workstation doar după ce stick-ul e primul în ordinea de pornire din BIOS — o singură schimbare, cu tine de față.
