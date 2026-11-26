# os-465 · atenția `tc16-v4` + bariera largă — TREC; rândul #513 lot 6 SĂRIT din nou

- **Când:** 26 nov 2026, semnal 16:36; rapoarte `rezultate/os-automat/2026-11-26/ciclu-auto-20261126-1633.txt` și `…-1636.txt`.
- **`teste.txt` avea 3 rânduri; au rulat doar 2.** Primul rând — `test-placa --antrenare-mini --vram --antrenare-513 --placi3 --mm-placi --colsum-impartit --mixt-513 --mixt-513-rapid --atentie-tc16 --lot-prin-ram --doua-locuri --lot-513 6` — **nu a rulat deloc**, fără niciun rând de eroare, la fel ca la os-462 (acolo era al treilea). Rândurile 2 și 3 au rulat ca „testul nr. 1 / nr. 2”. **Bănuială:** combinația `--atentie-tc16` + `--lot-prin-ram --doua-locuri --lot-513 6` e respinsă în tăcere de cititorul listei. **Cerere OS (urgentă):** rândul respins trebuie să apară în raport cu motivul; și dacă `--atentie-tc16` nu merge încă cu lotul 6, spuneți ce rând e corect.

1. **`--atentie-tc --atentie-tc16-v4`: TRECE** — `v4` = `tc16` pe 4 / 4 seturi aliniate (1 sărit), `v4pf` la fel; atentie-513-b4 pe lansare: **tc16 0,87 ms → v4 0,52 ms (×1,67)**, v4pf 0,64 ms (×1,34). Prezis 0,35–0,55 ✔ (la marginea de sus).
2. **`--bariera --bariera-larga`: TRECE** — G=48/96 TRECE; **G=384 (8 grupuri pe unitate) o barieră ≈ 2,0 µs; G=768 (16 pe unitate) ≈ 3,1 µs**, nicio blocare.
