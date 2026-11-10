# Workstation 10 nov 2026 ~16:43 — os-277 (reparația C-96), `gpu lant`
- I6 + I7: TRECE (a 4-a oară).
- **i8-gsp-init: ESUAT — „timeout după 2000003 µs”**; **1776 scrieri** (față de 1455 cu os-276 → secvențiatorul a mers mai departe, eroarea 0xbadf5620 nu mai apare).
- Curățare OK. Jurnal: `gpu-jurnal-005.txt` (2272 rânduri, cu fiecare comandă a secvențiatorului jurnalizată) — urcă aici de la Adrian.

## Jurnalul (adăugat 16:52) — `gpu-jurnal-005.txt` (2272 rânduri) + `raport-20261110-2.txt`
- Soneria la 134,97 s → la 136,82 s GSP-RM trimite cererea secvențiatorului: **420 de comenzi (#0…#419)**: POLL/WRITE pe falcon-ul GSP (0x1100xx), CORE_RESET,
  copiere DMA în pași de 0x100 (0x110114/0x11011c/0x110118 ← 0x614/0x600), configurare 0x1111xx, apoi **#419 CORE_RESUME**.
- **Toate comenzile #0–#418 au trecut.** Oprirea e la **ultima, CORE_RESUME**: după `0x111668 ← 0x111`, `0x110040 ← 0x09c7a000`, `0x110044 ← 0`, `0x840100 ← 2`
  (repornirea SEC2 cu Booter, citit înapoi 0x50) → **timeout 2 s** („RESET_READY nu a venit; continui” apare chiar înainte, la resetul falcon-ului GSP).
- Deci: suntem la **ultimul pas al secvențiatorului**. De verificat: ce condiție de terminare așteaptă CORE_RESUME (SEC2 oprit + mailbox 0? GSP-RM „lockdown” eliberat /
  RISC-V pornit? un mesaj nou în coada de stare?), dacă 2 s sunt destule, și dacă `RESET_READY` care nu vine la resetul falcon-ului GSP (0x110040 / 0x1103c0) contează.
