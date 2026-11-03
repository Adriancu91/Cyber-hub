# Fixarea cyber-gpu după C-58 (verificarea capătului WPR2)

- **Propus de:** `cyber-gpu` · **Data:** 2026-11-03
- **Proiecte implicate:** `cyber-gpu`, `cyber-universe`
- **Stare:** propus

## Ideea (pe înțelesul lui Adrian, 3–6 rânduri)
Pe 3 nov, primul I6 pe placă a spus „NU TRECE”, dar placa a făcut, cel mai probabil, exact ce trebuia: zona protejată a pornit unde am cerut,
iar verificarea noastră aștepta capătul zonei scris altfel decât îl scrie placa. Am reparat verificarea (acceptă și forma „ultima pagină”)
și acum, dacă ceva nu se potrivește, mesajul spune exact care registru și ce valori. Sesiunea OS trebuie doar să mute fixarea pe versiunea nouă.

## Ce ar face fiecare proiect
- `cyber-gpu`: gata (`af02bea`, docs `3286a3b`), doar SIMULARE. Detalii: `cyber-gpu/integration/cyber-universe/C-58_wpr2-capat.md`.
- `cyber-universe`: mută fixarea cyber-gpu ≥ `af02bea` (doar adăugări față de `4e6f747`; codul OS nu trebuie schimbat); opțional, după I6
  afișează și LO/HI brute (`falcon::check_frts_detail`, 3 citiri). Release nou pentru stick-ul de test.

## Cost și riscuri
- Puțin lucru (o schimbare de fixare). Nimic nou scris în placă.
- Ce rămâne de confirmat: valoarea HI exactă din `raport/gpu-jurnal-002.txt` (pe stick-ul de test) — la fereastra următoare Adrian îl copiază în
  `rezultate/`, noi îl verificăm cu `i6_log::wpr2_after_i6`, apoi I6 se repetă (pornire rece, cablul scos 30 s).

## Decizia lui Adrian
-

## Discuție
- 2026-11-03 `cyber-gpu`: sursele publice (RM 570.144, nova-core) verifică după FWSEC doar începutul zonei; capătul nu-l verifică nimeni.
