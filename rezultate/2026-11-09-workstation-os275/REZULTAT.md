# Workstation 9 nov 2026 ~08:02 — os-275, `gpu lant` (I6 → I14)

- `gpu firmware`: 4/4 fișiere oficiale 570.144, criteriul I4 TRECE (0 scrieri).
- `gpu lant` + DA (pornire rece, ambele stick-uri):
  - pregatire-i6, bus-master-pornit, i6-fwsec-frts, i6-wpr2-citit, **i7-booter-gsp, i7-citit: TRECE** (WPR2 0x1f4100000..0x1ffee0000, ca pe 5 nov)
  - **i8-gsp-init: ESUAT — „argument invalid: secventiator: marime sau index in afara bufferului”** (eroare în codul nostru, înainte de răspunsul GSP)
  - i8e…i14: sărite; bus-master-oprit TRECE; tur-după TRECE; **1452 scrieri**, pașii de curățare au rulat.
- Jurnal: `/usb/raport/gpu-jurnal-003.txt` (1523 rânduri) + `/usb/raport/20261109-1.txt` (142 887 octeți) — se urcă aici imediat ce Adrian revine în Windows.
- Poze: 01–03 în acest dosar.

## Jurnalul (adăugat 08:15) — `gpu-jurnal-003.txt` (1524 rânduri) + `raport-20261109-1.txt`
- I7: 0x840040/44 = 0 (Booter fără eroare), **0x111388 = 0x00000080** (pe 5 nov era 0xa0 — de comparat), WPR2 0x1f4100000..0x1ffee0000.
- I8: `bar0 w 0x110c00 = 0` (soneria) la 203,16 s → **ESEC la 204,99 s (~1,8 s după sonerie)** cu „secventiator: marime sau index in afara bufferului”.
  Pe 5 nov eroarea era „antetul cozii de stare nu are forma 570.144”; acum antetul trece și eșuează **parsarea secvențiatorului** → foarte probabil GSP-RM
  **a trimis deja primul mesaj** (cererea „rulează secvențiatorul CPU”), iar parserul nostru calculează greșit o mărime/un index. De verificat în jurnal/raport.
- Curățare: Bus Master oprit, tur după OK; I6 pregătire după = „WPR2 deja ridicat, trebuie pornire rece” (normal după lanț).
