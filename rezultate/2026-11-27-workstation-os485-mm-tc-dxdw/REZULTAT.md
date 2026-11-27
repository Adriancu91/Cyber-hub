# os-485 — înmulțirile pasului înapoi (dX, dW) — corecte, dar dW e frâna mare

- Rulat: 27 nov 09:24 (ciclul 09:52), pornit de centrul de comandă; rândul `test-placa --tablou-viteza --mm-tc --mm-tc-v4 --mm-tc-v5 --mm-tc-v6 --mm-tc-64k --mm-tc-dxdw`.
- Toate variantele: aceiași biți ca `mm_tc` pe qkv-513-dx și qkv-513-dw.

| program | qkv (înainte) | dX (6144×768×2304) | dW (A transpus) |
|---|---|---|---|
| mm_tc | 21,1 ms | 21,0 ms | 21,3 ms |
| v4@64k | 2,63 | 2,52 | 30,4 |
| v5@64k | 1,87 | **1,62** | 25,2 |
| v6@64k | **1,26** | 13,2 | **17,8** |

- **dX:** cel mai bun v5@64k 1,62 ms; v6@64k e de 8× mai lent (prezis v6/v5 ×1,00–1,10 → **GREȘIT**).
- **dW (A transpus):** toate variantele rapide sunt mai lente sau abia egale cu `mm_tc`; cel mai bun v6@64k 17,8 ms (v6/v5 ×1,42, prezis ×1,15–1,70 → CONFIRMAT). **dW e de ~14× mai lent decât aceeași înmulțire înainte** → cea mai mare rezervă de viteză din pas acum.
- Concluzie pentru pas: alegere pe formă — v6 înainte, v5 la dX, v6 la dW — și un program nou pentru A transpus (dW).
- Sursa: `rezultate/os-automat/2026-11-27/ciclu-auto-20261127-0952.txt`.
