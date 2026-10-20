# Deciziile lui Adrian (valabile pentru toate proiectele)

Doar ce a hotărât Adrian, cu data. Cea mai nouă e jos. Deciziile interne ale fiecărui proiect rămân în repo-ul lui
(de ex. `plan/REGULI_CASCADA.md` la Kronos, `docs/DECISIONS.md` la OS); aici stau cele care îi privesc pe toți.

## Principii permanente
- Totul construit de la zero, cel puțin 90% propriu. Modular: nucleu + module care se pot adăuga și scoate.
- Rapid și economic pe hardware slab. Fiecare pas reversibil.
- Niciun proiect nu modifică codul sau repo-ul altui proiect.

## Decizii
- 2026-10-19 19:35 — Kronos lucrează în cascadă: supraveghetor în cloud + executant pe workstation; granițele în `cyberspace/plan/REGULI_CASCADA.md`.
- 2026-10-20 — Cyber Universe OS pornește imediat, din cloud; pașii pe laptop vin mai târziu.
- 2026-10-20 — Suita office: întâi terminată și testată de oameni, abia apoi variantă pentru Kronos. Codul rămâne doar pe laptop până decide Adrian altfel.
- 2026-10-20 — Cyber Hub creat; Kronos, Cyber Universe OS și suita office conectate. Kronos poate scrie în hub fără să-și schimbe granițele de lucru.
- 2026-10-20 16:04 — Aprobat formatul comun de modul (`standarde/modul-v0.md`).
- 2026-10-20 18:18 — Hub-ul devine centrul de comandă: Claude îl organizează (panou, comenzi, resurse, decizii), Adrian aprobă.
  Regulă: nu se oprește niciun agent care lucrează la ceva important; comenzile se preiau după ce termină ce are în lucru.
