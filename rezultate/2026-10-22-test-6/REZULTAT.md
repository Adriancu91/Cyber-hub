# Testul 6 pe hardware real — os-138 (pașii A–D) și os-125 (pașii E–F) — CAUZA GĂSITĂ

**Data:** 2026-10-22, 17:30–17:57 · **Făcut de:** Adrian, pas cu pas, cu centrul de comandă · **Scris de:** centrul de comandă (din poze)
**Calculator:** Lenovo ThinkPad NB-7211174, cablu băgat. **BIOS setat de Adrian la 14:43 să pornească direct de pe stick** (fără meniul F12).

## Pașii și rezultatele
| Pas | Versiune | Cum a pornit | Comanda | trimise / primite | poza |
|---|---|---|---|---|---|
| A | os-138 | direct de pe stick (rece) | `net`, `log rtl` | **0 / 0** | 01, 02 |
| B | os-138 | — | `rtl porneste rxdv` → `net` | 0 / 0 (poarta RXDV era deja deschisă) | 03 |
| C | os-138 | — | `rtl porneste rxdv bloc` → `net` | 0 / 0 | 04 |
| D | os-138 | Restart din Windows, cu stick-ul băgat (direct) | `net` | 0 / 0 (legătura la 100 Mbit/s după Windows) | 05 |
| E | **os-125** | oprit complet → pornit direct de pe stick (rece) | `net` | **0 / 0** | 06 |
| F | **os-125** | **meniul de boot F12 → stick** | `net` | **17 / 23**, 1000 Mbit/s, inelul avansează (23 → 25) | 07 |

Registre la A (`log rtl`, poza 02): CR 0c, RCR 0000c70a, TCR 53900f00, IMR 0, ISR 0020, RMS 2048, MISC 0000003f, MCU 22, PHY 93;
inelele RDSAR 00000000_003d8000 / TNPDS 00000000_003d9000; buffer-e RX la 3db000, 3db800, 3dc000 (contigue, sub 4 GB); RAM 7299 MiB,
memorie și peste 4 GB; PCI Command 0007 (Bus Master da), Device Control 2010 (doar citit). La B și C placa repornită: RCR devine 0002c70a
la repornirea cu „rxdv”, MCU alternează 22/32; tot 0/0.

## Concluzii
1. **Cauza „0 / 0” de la testele 5 și 6: pornirea de la rece.** Aceeași versiune (os-125) nu merge pornită direct (E) și merge pornită din
   meniul F12 (F). Ca să afișeze meniul, firmware-ul UEFI pornește driverul lui de rețea și lasă cipul inițializat (și la 1000 Mbit/s).
   La testele 1–4 Adrian pornea mereu din meniu — de aceea mergea. După setarea BIOS-ului (14:43), firmware-ul nu mai atinge placa, iar
   **driverul nostru nu face singur inițializarea completă a cipului** (trezirea PHY/MAC după reset, pașii specifici reviziilor 8168G/H).
   Nu a fost regresie în cod: os-136/os-138 au fost testate doar la rece.
2. **Ipotezele infirmate azi:** No Snoop (era oprit), Relaxed Ordering (schimbarea lui n-a contat), poarta RXDV (era deschisă), buffer-e
   necontigue sau peste 4 GB (sunt contigue, sub 4 GB), bitul 17 din RCR (apare la a doua inițializare, fără efect), „trezit de Windows”
   (D: nu). Toate verificate pe laptop, nu în cod.
3. **Problema a doua rămâne, și e independentă:** la F, primul cadru e citit corect (`0800/udp67`), următoarele 7 sunt `0000`; DHCP 0 răspunsuri.
   Driverul citește conținut zero pentru cadrele 2+. Diagnosticul pe cadru (`log rx` cu adrese și primii octeți) există în os-138, dar
   trebuie rulat **la cald** (F12) ca să existe cadre de citit.
4. **Avem acum două moduri de test reproductibile:** „rece” = pornire directă (BIOS), „cald” = meniul F12. Fiecare reparație se verifică în
   ambele.
