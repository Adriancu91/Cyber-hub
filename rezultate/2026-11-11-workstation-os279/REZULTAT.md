# Test workstation 11 nov 2026 (12:20) — os-279 (C-102, jurnal de diagnostic)

**Rezultat:** I6, I7 TREC; I8 ESUAT „eroare hardware 0x59” (1777 scrieri), ca la os-278. Curățarea a rulat, tur-după TRECE.
Fișiere: `gpu-jurnal-007.txt` (3145 rânduri), `raport-20261111-2.txt`, `foto-1.jpg`.

## Ce spune jurnalul nou (rândurile `valoare …`)
- **Înainte de pornirea SEC2** (#419 CORE_RESUME): SCRATCH_14 = `0x13100000` (bit 26 = 0), SEC2 CPUCTL `0x50`, SEC2 MAILBOX0/1 = 0,
  GSP RISCV_CPUCTL `0x10` (oprit), GSP MAILBOX0 = `0x09c76000`.
- **După predarea etapei 3:** SCRATCH_14 = `0x17100000` (bit 26 = 1 → Booter-ul A RULAT, 2–3 µs nu era bit vechi), SEC2 CPUCTL `0x20` (oprit), SEC2 MAILBOX0 = 0 (Booter fără eroare),
  **GSP RISCV_CPUCTL `0x80` = RISC-V activ**, GSP MAILBOX0 = 0.
- **GSP-RM a pornit și a răspuns:** `GSP_INIT_DONE` cu **`rpc_result = 0x59` = `NV_ERR_OPERATING_SYSTEM`** (și `rpc_result_private = 0x59`). „nota: I8: eroarea vine din GSP_INIT_DONE”.
- Mesaje sărite de driver: **843 × funcția `0x1020`** (cele mai multe înainte de secvențiator) și **2 × `0x100c`** chiar înainte de GSP_INIT_DONE.
  Conținutul lor nu e jurnalizat. Probabil acolo e explicația firmware-ului (de verificat în antetele 570.144: ce evenimente sunt 0x1020 și 0x100c — posibil
  jurnal LIBOS / înregistrare de eroare).

## Concluzie
Lanțul de pornire (FWSEC → Booter → GSP RISC-V → GSP-RM) **merge până la capăt**; GSP-RM însuși refuză inițializarea (NV_ERR_OPERATING_SYSTEM).
Pas următor: jurnalizarea conținutului mesajelor 0x100c/0x1020 (text/cod), apoi corectarea parametrilor trimiși (ex. GspSystemInfo / registry / argumentele de boot).
