# Workstation 10 nov 2026 ~10:47 — os-276 (reparația C-91), `gpu lant`
- `gpu firmware`: I4 TRECE (4/4 oficiale).
- pregatire-i6, bus-master, i6-fwsec-frts, i6-wpr2, **i7-booter-gsp, i7-citit: TRECE** (a treia oară; WPR2 0x1f4100000..0x1ffee0000).
- **i8-gsp-init: ESUAT — „eroare hardware 0xbadf5620”** (1455 scrieri, curățare rulată). Față de 9 nov: secvențiatorul nu mai cade la parsare (reparația C-91 merge);
  acum o **citire de registru întoarce 0xbadf5620** (tiparul NVIDIA „bad register / PRI timeout”) — probabil în timpul executării comenzilor secvențiatorului CPU
  trimise de GSP-RM (registru dintr-un domeniu oprit/în reset, sau citit înainte ca falcon-ul să iasă din reset). Detaliile: `gpu-jurnal-004.txt` (1527 rânduri) — vine de la Adrian.

## Jurnalul (adăugat 10:55) — `gpu-jurnal-004.txt` + `raport-20261110-1.txt`
- I7 ca pe 9 nov: 0x840040/44 = 0, 0x111388 = 0x80; Booter pornit (0x840100 ← 2), 0x110080 ← 0x0008b320.
- I8: sonerie `0x110c00 ← 0` la 169,20 s → **~1,85 s fără nicio scriere/citire jurnalizată** → `0x110040 ← 0x80000000` → „falcon: RESET_READY nu a venit; continui”
  → `0x1103c0 ← 1` apoi `← 0` (reset al falcon-ului GSP, bază 0x110000) → **ESEC 0xbadf5620** la 171,10 s.
- Bănuială de verificat (centrul de comandă, nu certitudine): o comandă a secvențiatorului (CORE_RESET / așteptare RESET_READY) e executată pe **falcon-ul GSP însuși**,
  sau înainte ca GSP-RM să fie oprit; resetul îl taie pe GSP, iar citirea următoare din domeniul lui dă 0xbadf5620. De comparat ordinea comenzilor secvențiatorului din mesaj
  (de jurnalizat fiecare comandă: tip, registru, valoare, mască) cu ordinea din specificație (OpenRM/nova: secvențiatorul CPU rulat la cererea GSP-RM).
- Cerere: jurnalizarea completă a mesajului secvențiatorului (toate comenzile, înainte de execuție) — ca la următorul test să vedem exact ce ni s-a cerut.
