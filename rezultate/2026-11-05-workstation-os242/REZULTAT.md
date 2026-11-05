# Workstation 5 nov 2026 — os-242, Adrian de față de la 08:30

## Kronos #477 în OS (stick normal)
- `--cauta`: 32 variante, 0 respinse; cea mai bună: AVX2+FMA, **35 fire (un procesor liber), t-j, un bloc pe simbol, 1 bucată pe fir** — 2040 µs/simbol doar produsele (2198 fără bloc).
  Bariera goală 1,18 µs pe 35 fire.
- CONTROL **TRECE**.
- `--profil --fara-ecran --n 64`: **256,0 simb/s** (4 nov: 206,4; 3 nov: 125,4). 3,99 ms/simbol. qkv 22,98 GB/s (4 nov: 12,5), proiecția 9,04 GB/s (4 nov: 6,0) — încă cea mai lentă;
  ieșire MLP 26,3 GB/s 30 %; așteptarea firelor 13,3 % (59,3 bariere/simbol, 9 µs medie). Ținta următoare: proiecția și ieșirea MLP la ~60 GB/s ca fc 4E.

## Placa (stick de test os-242, cyber-gpu a2f9736, pornire rece)
- `gpu pregatire-i6`: TRECE, 0 scrieri.
- `gpu lant` + DA: **pregatire-i6 TRECE, bus-master-pornit TRECE, i6-fwsec-frts TRECE, i6-wpr2-citit TRECE** — **I6 TRECE oficial pe placa reală**.
  WPR2 = RIDICAT 0x1ffe00000..0x1ffee0000 (LO `0x1fa824` = 0x01ffe000, HI `0x1fa828` = 0x01ffee00). I7–I10: oprit cinstit („pas fără implementare în OS”, C-72 în lucru).
  Bus Master oprit TRECE, tur după TRECE; 722 scrieri; jurnal `gpu-jurnal-002.txt` (771 rânduri). Observație: faptul `i6.trece = nu` din turul de citire folosește încă criteriul vechi (de corectat).

## os-246 — I7 + I8 (stick de test refăcut ca FAT32 MBR „TESTGPU” cu `firmware\` copiat de pe stick-ul normal, C-74; 12:35)
- `gpu lant` + DA: pregatire-i6 TRECE, bus-master-pornit TRECE, i6-fwsec-frts TRECE, i6-wpr2-citit TRECE, **i7-booter-gsp TRECE, i7-citit TRECE**,
  **i8-gsp-init: EȘUAT** — „blocat: cozi GSP: antetul cozii de stare nu are forma 570.144 (GSP nu a pornit sau altă versiune)”. Bus Master oprit TRECE, tur după TRECE; 1449 scrieri;
  jurnal `gpu-jurnal-002.txt` (1519 rânduri).
- În turul de după: WPR2 = RIDICAT **0x1f4100000..0x1ffee0000** (LO `0x1fa824` = 0x01f41000) — după I7 zona protejată s-a lărgit de la FRTS la o zonă de ~190 MiB:
  semn că Booter a rulat și a pregătit WPR2 pentru GSP-RM. De aceea faptul `i6.trece` din tur iese acum „nu” (compară cu FRTS) — de ajustat (după I7 e normal).
- Întrebarea deschisă: GSP a pornit (RISC-V) dar n-a scris încă coada, sau nu a pornit deloc? Răspunsul e în jurnal (de copiat de pe E:\raport\).
