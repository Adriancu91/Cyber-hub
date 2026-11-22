# os-355 pe placa reală — două teste într-o singură pornire, 22 nov 2026 20:06–20:09

Semnal 20:02. Rapoarte: `rezultate/os-automat/2026-11-22/ciclu-auto-20261122-2006.txt` și `-2008.txt`.

**TRECE amândouă.**
1. `test-placa --argmax-fara-copie --dieta2` (#513): 18/18, 16 identice, **647,24 simb/s**.
2. `test-placa --k651` — **al doilea test din aceeași pornire, după resetul din interior (FLR)**: lanțul trece, Kronos #651 16 simboluri identice cu procesorul, **285,75 simb/s** (os-343: 194,34).

De acum un singur ciclu (~15 min) poate face până la 4 teste.
