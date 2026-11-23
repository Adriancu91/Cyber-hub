# os-380 pe placa reală — PRIMUL PAS ÎNTREG DE ANTRENARE PE PLACĂ, 23 nov 2026 23:12

`test-placa --antrenare-mini` (aprobat de Adrian 23:05 ca probă de corectitudine), semnal 23:07. Rapoarte: `rezultate/os-automat/2026-11-23/ciclu-auto-20261123-2312.txt` și `-2314.txt`.

**TRECE — ACELEAȘI NUMERE ca oracolul pe procesor:** 10 pași ai modelului mic (vocabularul lui Kronos 16 384, 2 straturi, E 64, 1,15 mil. greutăți, lot 2 × 32, AdamW), loturi sintetice (fără date pe disc); abaterea maximă a pierderii 9,9e-8, a greutăților 8,8e-6 (toleranța 1e-3). Pierderea la pornire 9,7404 (ln 16 384 = 9,7041).

Viteza (NU se socotește: arena în RAM prin PCIe x8, model minuscul): placa 25,6 ms pe pas = 2 499 simboluri/s; pasul întreg 286 ms. Testul 2 după FLR: 16 identice, 632 simb/s.

Următorul: arena în VRAM, apoi #513 și comparația cu Windows (~39 300 simb/s la antrenare).
