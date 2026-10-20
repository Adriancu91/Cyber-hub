# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-10-20 18:25 (ora României) · **de:** centrul de comandă, copiat din `docs/STATE.md` și din commit-urile
din `cyber-universe` (sesiunile programate ale OS-ului nu au încă acces la hub; au cerut ca altcineva să scrie aici).

## Acum
- Fazele 1 și 2 închise: nucleul rezistă 5 minute de stres, mai multe programe rulează în paralel, programe separate în
  modul utilizator, fișiere în memorie și pe disc FAT32, consolă cu comenzi (`ls`, `cat`, `run`, `mem`, `net`, `reboot` …).
- Faza 3 (în emulator): discuri SATA și NVMe, USB (tastatură, mouse, stick), placă de rețea, imagine de stick USB care pornește.
- Faza 4 începută: mouse, desen rapid, font cu diacritice, server grafic cu ferestre și cursor (P4-04),
  ferestre pentru programe (P4-05). O sesiune programată lucrează chiar acum.
- 24 de scenarii de test automate trec; CI verde.

## Urmează
- P4-07 scriere pe disc FAT32, P4-12 aranjament de tastatură românesc, apoi restul Fazei 4 (module, aplicații).

## Ce oferă proiectul celorlalți
- Infrastructura de test pe scenarii (`tests/scenarios.txt` + `tools/test.sh`) și regulile de lucru în cascadă.
- Formatul comun de modul (`standarde/modul-v0.md`) e folosit de la Faza 4 pentru `modules/` și `apps/`.

## De ce are nevoie de la ceilalți
- O rezervare a laptopului ThinkPad (al suitei office) pentru testul pe stick, când decide Adrian (vezi `RESURSE.md`).

## Blocaje / nevoie de Adrian
- **B-001 / P3-09:** testul pe calculatoare reale — Adrian scrie imaginea pe un stick, pornește ThinkPad-ul și încă un
  calculator de pe el și trimite poze cu ecranul (pași în `docs/USB.md`). P3-10 așteaptă după el.
- Sesiunile programate nu pot scrie în hub până nu primesc acces la `Cyber-hub` (în setările sarcinii programate).
