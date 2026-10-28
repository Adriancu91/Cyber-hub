# Workstation + os-195: **Kronos #459 rulează în Cyber Universe OS** — 28 oct 2026, ~10:00–10:35 (Adrian de față)

Workstation Dell (i9-10980XE, 18 nuclee / 36 fire, 128 GB), pornit de pe stick (F12), stick ADATA FAT32 cu os-195 + `kronos/kronos_459_q8_0.kgr`
(110.859.040 octeți) + `.sha256`. Prima încercare: modelul lipsea de pe stick (n-a fost copiat) → recopiat din `C:\Kronos\cyberspace\lucru\export\`.

## Rezultate
- **`cpu porneste`: 36 nuclee pornite din 36** în 442 ms (`poza-0-36-nuclee.jpg`).
- **`run kronos-calcul --cauta`** (`poza-1-reglaj.jpg`): 28 de variante, 0 respinse; „cea mai bună: vectori AVX2+FMA, **1 fir**, ordine t-j (363× față de
  scalar pe 1 fir)”; scris `/usb/kronos/reglaj-Intel-R-Core-TM-i9-10980XE-CPU-3-00GHz.txt`. **Problemă:** căutarea măsoară pe o problemă minusculă
  (1 rând ~100 µs, 16 rânduri ~1–2 ms), unde firele multe doar costă; pentru modelul real alegerea „1 fir” e greșită (vezi viteza mai jos).
  `kronos-calcul` pe 16 fire: OK, 0 diferențe.
- **`run kronos`** (`poza-2-kronos-ana-def.jpg`, `poza-3-kronos-buna-ziua.jpg`) — SHA-256 `e80618b4…382e` = suma așteptată; modelul citit în ~30 s
  (q8_0, 105 MiB → ~3,5 MB/s de pe stick); 12 straturi, 12 capete, n_emb 768, context 512, vocabular 16.384, 98.022.912 parametri; tokenizer w2.
  | text | simboluri | generat | așteptat (MODEL.md) | viteză |
  |---|---|---|---|---|
  | `Ana are mere.` | [65, 1988, 1585, 2717, 46] | [2233, 1585, 32, 475, 50] „ Acum are 1192” | identic ✔ | 21,7 simb/s |
  | `def suma(a, b):` | [2082, 15746, 40, 97, 44, 1376, 1754] | [1510, 1947, 1358, 1646, 1376] „\n    return a + b” | identic ✔ | 2,6 simb/s |
  | `Buna ziua` (64) | [66, 2612, 7464] | „,\nAm fost la un concert de la Teatrul de Comedie din București, la Teatrul…” (se repetă) | — | 7,9 simb/s |
  Toate cu reglajul „1 fir”. Repetiția e a modelului (greedy), nu a motorului.
- **Concluzie: motorul KGR1 din OS e corect pe hardware real** (aceleași simboluri ca referința Python). Viteza e mult sub ce poate mașina
  (estimare: sute de simb/s pe 36 de fire), din cauza reglajului pe 1 fir și a împărțirii muncii.

## Proba cu fire (`poza-4-fire-18-36.jpg`) — `run kronos --fire N --n 64 Buna ziua`
| fire | viteză | text |
|---|---|---|
| 1 (din reglaj) | **7,9 simb/s** | identic |
| 18 | 6,2 simb/s | identic |
| 36 | 4,8 simb/s | identic |
- **Mai multe fire = mai lent**, deși ieșirea e identică (bine: determinist). Rândul `cpu:` după `cpu porneste` spune „36 nuclee pornite din 36
  (**parcate: firele rămân pe primul nucleu**)” — de verificat dacă firele programului rulează cu adevărat pe celelalte nuclee.
- Și pe 1 fir e lent: ~0,1 GB de greutăți pe simbol ar trebui să dea zeci de simb/s pe un nucleu (lățimea de bandă a memoriei), nu 8.
- Încărcarea modelului: ~31 s pentru 105 MiB (~3,5 MB/s de pe stick).

## `gpu identifica` pe placa reală (`poza-5-gpu-identifica.jpg`) — I0/I1, doar citire
- `gpu0: b3:00.0 10de:2482 NVIDIA (clasa 03:00:00) subsistem 88131043`; Command 0003 (memorie da, bus master nu), stare D0.
- BAR0 `0xf9000000` memorie (16 MiB), BAR1 `0xe0000000` 64 biți prefetch (256 MiB), BAR3 `0xf0000000` 64 biți prefetch (32 MiB), BAR5 `0xf000` I/O.
- `cyber-gpu dac2e32 nvidia-ga104: GeForce RTX 3070 Ti`; **`NV_PMC_BOOT_0 = b74000a1`, `NV_PMC_BOOT_42 = 174a1000` (consecvent true)**; cip 0x174 GA104 (Ampere).
  Față de `docs/GA104_INITIALIZATION.md` I1: `BOOT_0 & 0x1ff00000 = 0x17400000` ✔, `BOOT_42.chip_id = 0x174` ✔.
- **„zero scrieri în placă (configurație PCI și registre: doar citire; adaptorul cyber-gpu a refuzat 0 scrieri)”.**
- **Prima confirmare pe hardware real pentru Cyber-GPU (I0 + I1).** Urmează pe loc `gpu gfw` (I2) și `gpu vbios` (I3).
