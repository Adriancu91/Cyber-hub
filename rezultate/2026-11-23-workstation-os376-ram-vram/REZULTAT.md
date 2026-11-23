# os-376 pe placa reală — viteza RAM ↔ VRAM cu motorul de copiere, 23 nov 2026 17:36

Planul de rezervă al lui Adrian (23 nov 08:24). Semnal 17:33, două teste. Rapoarte: `rezultate/os-automat/2026-11-23/ciclu-auto-20261123-1736.txt` și `-1738.txt`.

**TRECE (corect), dar la jumătate din prezis:** sus (RAM → VRAM) **5,97 GB/s** (prezis 11–13), jos (VRAM → RAM) **6,76 GB/s** (prezis 11–13,5); 4 copii în paralel nu adaugă nimic (1 048 / 1 000 ‰). Octeții verificați. Pentru comparație, VRAM → VRAM: 282 GB/s (92,8 % din 608). Testul 2: 16 identice, **657,48 simb/s** (cel mai bun până acum).

Întrebare pentru Cyber-GPU: ~6 GB/s seamănă cu PCIe 3.0 x8 sau 2.0 x16 — de citit lățimea și viteza legăturii (LnkSta) și de încercat RAM fixată în alt loc / blocuri mai mari, înainte de studiul mutării în RAM.
