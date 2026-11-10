# Workstation 10 nov 2026 ~10:47 — os-276 (reparația C-91), `gpu lant`
- `gpu firmware`: I4 TRECE (4/4 oficiale).
- pregatire-i6, bus-master, i6-fwsec-frts, i6-wpr2, **i7-booter-gsp, i7-citit: TRECE** (a treia oară; WPR2 0x1f4100000..0x1ffee0000).
- **i8-gsp-init: ESUAT — „eroare hardware 0xbadf5620”** (1455 scrieri, curățare rulată). Față de 9 nov: secvențiatorul nu mai cade la parsare (reparația C-91 merge);
  acum o **citire de registru întoarce 0xbadf5620** (tiparul NVIDIA „bad register / PRI timeout”) — probabil în timpul executării comenzilor secvențiatorului CPU
  trimise de GSP-RM (registru dintr-un domeniu oprit/în reset, sau citit înainte ca falcon-ul să iasă din reset). Detaliile: `gpu-jurnal-004.txt` (1527 rânduri) — vine de la Adrian.
