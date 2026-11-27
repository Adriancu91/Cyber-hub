# os-489 — paza ferestrei de viteză maximă — confirmă: timpii lenți erau în afara ferestrei

- Rulat: 27 nov 14:10 (ciclul 14:42), rândul corectat `test-placa --tablou-viteza --mm-tc --mm-tc-v4 --mm-tc-v5 --mm-tc-v6 --mm-tc-64k --mm-tc-dxdw` (cel de la 13:26 fusese refuzat: v5 fără v4).
- Toate variantele: aceiași biți ca `mm_tc`.
- Paza nouă: „lanțul a mai rulat 1 597 s după cererea acceptată (cererea ține 600 s): IEȘIT din fereastră; seturi de timpi în afara ferestrei: 10”.
- În fereastră: qkv v6@64k 1,26 ms; **dX v5@64k 1,62 ms (confirmat a doua oară)**. În afara ferestrei (deci nesigure): dX v6@64k 13,0, dW v5@64k 25,3, dW v6@64k 17,9.
- Concluzie: diferența ×10 de la os-486 (v5 dX 15,6 vs 1,62) = placa ieșită din viteza maximă, nu programul. Adrian a aprobat 1 800 s (DECIZII 27 nov 14:35) → următorul: `--viteza-1800` (os-490).
- Sursa: `rezultate/os-automat/2026-11-27/ciclu-auto-20261127-1442.txt`.
