# os-417 — proba `mm_tv_64x64k8` cu pagină de pază (P6-195) — TERMINĂ, aceiași biți, cea mai rapidă pe qkv

**Data:** 25 nov 2026, pornire 03:48. Raport: `rezultate/os-automat/2026-11-25/ciclu-auto-20261125-0348.txt`.
- `mm_tv_64x64k8` pe qkv (1024 × 2304 × 768): **1 768 µs = 2,04 TFLOP/s, aceiași biți** (martorul 2 839 µs = 1,27; `128x128` la os-416: 1 890 µs = 1,91).
- **Cauza blocajului de la os-413 confirmată și reparată:** citirea în avans a instrucțiunilor după capătul codului; cu pagina de pază după fiecare program, varianta termină. Poate reveni în cursă.
- Pasul #513: 474,3 ms, TRECE = oracolul; generarea de după corectă (simbolurile identice).
- Următorul: cursa cu toate 5 variantele pe toate formele (alegerea pe formă poate da ~2 TFLOP/s pe formele mari), după `--mm-alegere` (os-418).
