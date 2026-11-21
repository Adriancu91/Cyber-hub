# Rezultat: tabloul de bord al plăcii pe placa reală (os-323, ciclu automat) — 21 nov 2026, 08:21

- **Unde:** workstation (RTX 3070 Ti, GA104), ciclul automat, fără om de față. Paznicul a pornit testul la 08:16:53 (prima rulare fără fereastra orară), raportul la 08:21, Windows înapoi la ~08:25.
- **Versiunea:** `os-323` (`81d042f`), cyber-gpu `de4887d`. Rândul din listă: `test-placa --tablou`.
- **Fișierele brute** (urcate singure de OS): `rezultate/os-automat/2026-11-21/ciclu-auto-20261121-0821.txt`, `gpu-jurnal-018.txt`, `gpu-jurnal-019.txt` (rândurile `kd`: 4176–4213).

## Ce era nou: tabloul de bord (C-151 punctul 1, C-152 punctul 5) — MERGE
Toate cele trei cereri către programul plăcii au fost **acceptate** (pornirea zonei comune, intervalul de citire, cererea datelor: 0x0). Citirea, la 1,7 s după sfârșitul calculului (placa în repaus):

| Ce | Valoarea brută | Înseamnă |
|---|---|---|
| temperatura plăcii | 0x23d8 (÷256) | **35,8 °C** |
| ceasul nucleului | 0xe1 | 225 MHz |
| ceasul memoriei | 0x195 | 405 MHz |
| starea de performanță | 0x8 | P8 (repaus) |
| încărcarea nucleului / memoriei | 0 / 1 | repaus |
| motivele încetinirii | 0x1 | **nu termic** (termic ar fi 0x20 / 0x40); bitul 0 — de tălmăcit de Cyber-GPU (DEDUS: „placa în repaus”) |
| puterea medie | 0x627c | 25,2 W |
| limita de putere | 0x46cd0 | 290 W |
| secțiuni citite | 0x7f | toate 7; 0 ocupate după 10 încercări |

Față de SIMULARE (45 °C, 210 / 405 MHz, P8): ceasul memoriei identic, restul aproape.

**Ce n-a mers:** oprirea citirilor a fost acceptată, dar **oprirea zonei comune a fost refuzată** (0x8000001f), cu un rând nou de avertizare internă a plăcii (NOCAT `ASSERT`, adresa 0x0185eb2e; ieri 4 astfel de rânduri, azi 5; mesaje GSP-RM sărite 2 → 3). Urmarea: pagina rămâne rezervată până la repornire. Placa a mers mai departe normal (`i14-simbol: ok`, turul de citire ca ieri). → Cyber-GPU: forma mesajului de oprire sau renunțarea la el (C-157 punctul 2).

## Testul obișnuit din aceeași rulare (nimic nou; pentru comparație cu os-322)
- 16 simboluri din 16 identice cu procesorul; abaterea maximă a logit-urilor 1,62e-5.
- **Cu driverul 94,44 simb/s** (os-322: 94,84); doar placa 382,18; procesorul 69,56; cu verificarea după placă 38,71.
- Timpul pe simbol: placa 2 631 µs, **driverul 3 087 µs**, jurnalul 62 µs = 5 794 µs — același tablou ca ieri: frâna e driverul (→ dieta, `os-324`).
- Viteza maximă: **înainte P0** (ieri era P5), cererea acceptată, după P0, verdict 2 (acceptată, fără efect); la final P0, iar la 1,7 s după ștergerea cererii tabloul arată deja P8 la 225 / 405 MHz. De ce era P0 dinainte azi — de lămurit de Cyber-GPU.
- Copierea VRAM → VRAM 281 081 MB/s (92 % din plafon), 0 cuvinte greșite. Procesorul 40 °C.
- Sfârșitul lanțului („oprit la tur-dupa”, 2 871 de scrieri) e cel obișnuit, ca în os-313 și os-322.

## Ce urmează
- Proba de reset din interior (`test-placa --flr-proba`, aceeași versiune) — semnal dat la 08:27.
- C-151 punctul 2 (citirea înainte și după viteza maximă, apoi la N secunde sub lucru) are acum o bază reală: până azi nu aveam nicio temperatură a plăcii în OS-ul nostru.
