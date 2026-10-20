# Reguli pentru agenți — Cyber Hub

Acest repo e **centrul comun** al proiectelor lui Adrian. Fiecare agent (sesiune Claude / Claude Code) care lucrează
la un proiect conectat îl folosește ca să știe ce fac ceilalți și să propună colaborări.
Adrian e român și nu programează: tot ce scrii aici e în **română simplă**.

## Proiecte conectate (ID-uri)
| ID | Proiect | Fișier de stare |
|---|---|---|
| `kronos` | Kronos / Cyberspace (AI propriu) | `stare/kronos.md` |
| `cyber-universe` | Cyber Universe OS | `stare/cyber-universe.md` |
| `suita-office` | Suita de aplicații office | `stare/suita-office.md` |

Un proiect nou se adaugă doar de Adrian sau la cererea lui (rând nou aici + în `PROIECTE.md` + fișier de stare).

## La ÎNCEPUTUL sesiunii (citire, ~1 minut)
1. `git pull` în clona hub-ului (sau clonează: `https://github.com/Adriancu91/cyber-hub`).
2. Citește `PROIECTE.md` și **stările celorlalte proiecte** din `stare/`.
3. Citește în `idei/` propunerile cu starea `propus` sau `aprobat` care îți numesc proiectul.
4. Folosește ce afli doar ca **context**. Nu schimbi planul proiectului tău pe baza hub-ului fără aprobarea lui Adrian,
   cu excepția propunerilor marcate `aprobat` pentru proiectul tău.

## La SFÂRȘITUL sesiunii (scriere, ~2 minute)
1. **Rescrie complet** fișierul tău de stare `stare/<ID>.md` după șablonul din `stare/_SABLON.md` (max ~40 de rânduri).
2. **Adaugă** 1–3 rânduri la finalul `jurnal/<ID>.md`: `- AAAA-LL-ZZ HH:MM — ce s-a făcut (o propoziție)`. Nu șterge nimic din jurnal.
3. Dacă ai o idee care leagă proiectul tău de altul: creează `idei/AAAA-LL-ZZ-<scurt>.md` după `idei/_SABLON.md`.
   Dacă ai ceva de spus la o propunere existentă: adaugă un rând la secțiunea „Discuție” a ei.
4. Commit (mesaj: `<ID>: stare AAAA-LL-ZZ`) și push. Dacă push-ul e refuzat: `git pull --rebase` și reîncearcă (max 3 ori).

## Ce NU ai voie
- Să scrii în fișierul de stare sau în jurnalul altui proiect.
- Să modifici **codul sau repo-ul altui proiect**. Colaborarea se face doar prin propuneri în `idei/`.
- Să marchezi o propunere `aprobat`. **Doar Adrian aprobă** (sau coordonatorul, scriind explicit „aprobat de Adrian în chat, data …”).
- Să pui în hub: parole, chei API, date personale, date de business ale firmei (clienți, prețuri, facturi).
- Să rescrii istoria git (`push --force` interzis).

## Stările unei propuneri (`idei/`)
`propus` → (Adrian) `aprobat` / `respins` / `amânat` → (agenții implicați) `în lucru` → `gata`.

## Coordonatorul
O sesiune automată zilnică citește tot hub-ul, scrie `rezumate/AAAA-LL-ZZ.md` și îi trimite lui Adrian un rezumat scurt:
ce s-a mișcat în fiecare proiect, ce propuneri așteaptă decizia lui, ce legături între proiecte merită făcute.
Coordonatorul nu modifică stările proiectelor și nu scrie cod.
