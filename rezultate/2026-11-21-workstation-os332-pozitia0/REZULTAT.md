# os-332 pe placa reală — încălzirea poziției 0 (P6-116), 21 nov 2026 ~19:16

Test pornit de centrul de comandă (stick verificat identic, `ceas 40` + `test-placa --ln-nou`, semnal 19:08, pornit de paznic 19:11:53, înapoi în Windows ~19:19). Raport: `rezultate/os-automat/2026-11-21/ciclu-auto-20261121-1916.txt`.

## Verdict: TRECE
- `kt incalzirea`: poziția 0 trimisă o dată înainte de ceas pe 2 liste (15 553 µs în afara ceasului, 12 687 cuvinte VRAM la prima).
- **Prima rulare** (lista lipită, LayerNorm vechi — testul obișnuit): mediana 2 421 µs, **cea mai lentă 2 494 µs** → nicio poziție lentă (os-329: poziția 0 ~12 ms). 291,41 simb/s pe ceasul plăcii cu pauzele driverului (os-329: 287,89).
- **A doua rulare** (LayerNorm nou): `pozitiile lente: 0 din 18`, **media cu driverul 351,39 simb/s**, doar lansările 507,15 simb/s; simbolul median 2 884 µs (placa 1 977, driver 818, jurnal 61). LayerNorm nou față de vechi: max |d| 6,9e-6, TRECE.
- 16 simboluri identice cu procesorul în ambele rulări; amprenta 0x46a07914 (ca os-331).

## Față de Windows
Kronos #513 în Windows/PyTorch (20 nov): 129,12 simb/s → **351,39 / 129,12 = de 2,72 ori**. Cinstit: (a) încălzirea (15,5 ms, o dată pe text) e în afara ceasului — ca „citirea textului dat”, nu ca generare; (b) Windows = cum rulează Kronos azi acolo (F32, fără memoria de context), nu cel mai bun PyTorch posibil; (c) LayerNorm nou e încă „la cerere”, nu implicit.

## Ce urmează
Driverul 818 µs → dieta 2 (predată); înmulțirile (fc/proj/qkv ~1,27 ms din 1,98) → cursa înmulțirilor și P8. Prezentarea actualizată (pagina 5: 351 / 507, de 2,7 ori).
