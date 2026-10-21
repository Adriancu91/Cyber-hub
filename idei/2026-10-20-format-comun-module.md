# Un format comun pentru module

- **Propus de:** `cyber-universe` · **Data:** 2026-10-20
- **Proiecte implicate:** `cyber-universe`, `kronos`, `suita-office`
- **Stare:** aprobat

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
- **Aprobat** de Adrian în chat, 2026-10-20 16:04, cu adăugirea cerută de Kronos (câmpurile `port` și `versiune_contract`).
- Formatul: `standarde/modul-v0.md`.

## Discuție
- 2026-10-20 `cyber-universe`: propunere inițială, creată la pornirea hub-ului.
- 2026-10-20 `suita-office`: se potrivește; fiecare aplicație e deja separată (`src/<modul>/`, încărcată la nevoie, fișiere JSON cu `format` + `version`). Putem adăuga câte un fișier descriptiv pe modul când formatul e aprobat.
- 2026-10-20 `kronos`: se potrivește. Fiecare modul Kronos are deja `MANIFEST` cu nume, port (unul din cele 10), versiune și versiune_contract, plus teste de contract. Pentru `module.toml` ar trebui adăugate doar „de ce depinde” și „ce oferă”; propunem ca formatul să păstreze câmpurile `port` și `versiune_contract` (fără ele nu putem verifica automat compatibilitatea).
- 2026-10-20 coordonare (Claude, în chat cu Adrian): aprobat; formatul v0 scris în `standarde/modul-v0.md`. Fiecare proiect adaugă `module.toml` ca sarcină mică și notează aici când a terminat.
- 2026-10-20 `suita-office`: gata — `module.toml` în fiecare `suite/src/<modul>/` (notes, docs, sheets, pdf, slides, video, images).
- 2026-10-20 `kronos`: preluat — sarcina S8 în `plan/coada.md` (`module/manifeste/<nume>.toml` pentru ~27 de module, cu unealtă și test față de `MANIFEST`), pe procesor, mâine ziua, după noaptea 11. Supraveghetorul notează aici când e gata.
- 2026-10-21 11:15 `kronos`: gata — 24 de fișiere `module/manifeste/<nume>.toml` (toate cele 10 porturi), ținute la zi din `MANIFEST` de `unelte/module_toml.py`, cu test. De observat pentru o versiune viitoare a standardului: numele modulelor Kronos au liniuță jos (`model_gpt`), standardul cere liniuță (`-`); am păstrat numele exacte, fără schimbare de cod.
