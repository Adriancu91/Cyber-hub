# Workstation 4 nov 2026 — os-222 (C-59 + P6-45 + C-61), Adrian de față 17:30–18:45

## Kronos #477 în OS
- `--cauta`: 32 variante, 0 respinse; cea mai bună: AVX2+FMA, 36 fire, t-j, **un bloc pe simbol, 4 bucăți pe fir** (2088 µs/simbol doar produsele, față de 2185 fără bloc, −4,5 %).
  Echipele (9×4, 6×6) și „un procesor liber” nu au fost mai rapide. **Bariera goală: 1,40 µs × 49 pe simbol = 68 µs/simbol** → ipoteza H1 („clopoțelul”) e greșită.
- CONTROL **TRECE** (3 texte = cele publicate).
- `--profil --fara-ecran --n 64`: **206,4 simb/s** (3 nov: 125,4; ×1,65). 5,01 ms/simbol. Așteptarea firelor **9,6 %** (3 nov: 62,9 %);
  bariere 58,8/simbol, 8,2 µs medie (trezire 0, așteptat cel mai lent 0,5 µs, adunare 0).
  Frâna rămasă: `qkv (+atenția)` 38,2 % la 12,5 GB/s și `proiecția` 26,4 % la 6,0 GB/s, față de fc 60 GB/s și MLP 34 GB/s → următoarea țintă (estimare ~350–400 simb/s dacă ajung la viteza fc/MLP).

## I6 (stick de test os-222, cyber-gpu `3286a3b`, pornire rece)
- `gpu pregatire-i6`: TRECE (VRAM 8192 MiB, WPR2 coborât, 0 scrieri).
- `gpu i6 --scrie` + DA: ucode HS încărcat prin DMA ok; FWSEC rulat; Bus Master pus la loc. **Rezultat afișat: NU TRECE** — „verificare eșuată la 0x1fa828: așteptat 0x1fff00, citit 0x1ffee0”.
- **Analiza centrului de comandă:** LO = `0x1ffe00` (ieri, exact începutul FRTS); HI citit = `0x1ffee0` → capăt `0x1ffee0000` = începutul ultimului bloc de **128 KiB** din zona de 1 MiB
  (0x1ffe00000 + 0xe0000). Deci WPR2 = exact zona FRTS cerută, cu granulație de 128 KiB → **FWSEC-FRTS a reușit pe placa reală**; verificarea noastră aștepta capătul exclusiv
  sau ultima pagină de 4 KiB, nu ultimul bloc de 128 KiB. Al doilea defect: „WPR2 citit după I6: nepermis de politica de siguranță” — citirea brută de după I6 (C-61) e oprită de paznic.
- → C-66.
