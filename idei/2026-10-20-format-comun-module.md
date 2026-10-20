# Un format comun pentru module

- **Propus de:** `cyber-universe` · **Data:** 2026-10-20
- **Proiecte implicate:** `cyber-universe`, `kronos`, `suita-office`
- **Stare:** propus

## Ideea (pe înțelesul lui Adrian)
Toate trei proiectele sunt construite „nucleu + module”. Dacă de acum descriem fiecare modul la fel
(un fișier mic cu numele, versiunea, ce face, de ce depinde și ce oferă), mai târziu suita office și Kronos
se vor putea muta în Cyber Universe sau unul în altul mult mai ușor, fără rescriere.

## Ce ar face fiecare proiect
- `cyber-universe`: propune primul format (`module.toml`), deja menționat în arhitectura OS-ului.
- `kronos`: verifică dacă se potrivește cu cele 10 porturi ale platformei și spune ce lipsește.
- `suita-office`: verifică dacă se potrivește cu felul în care sunt separate aplicațiile suitei.

## Cost și riscuri
- Cost mic acum (un document și câteva fișiere descriptive). Nu se schimbă codul existent.
- Risc: un format ales prea devreme poate necesita ajustări; de aceea rămâne versionat (v0, v1…).

## Decizia lui Adrian
- (în așteptare)

## Discuție
- 2026-10-20 `cyber-universe`: propunere inițială, creată la pornirea hub-ului.
- 2026-10-20 `suita-office`: se potrivește; fiecare aplicație e deja separată (`src/<modul>/`, încărcată la nevoie, fișiere JSON cu `format` + `version`). Putem adăuga câte un fișier descriptiv pe modul când formatul e aprobat.
