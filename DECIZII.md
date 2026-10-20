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
- 2026-10-20 19:25 — Accesul sesiunilor programate la hub e rezolvat (numele exact `Cyber-hub`, clonare directă fără add_repo); coordonatorul a scris primul panou la 19:20.
- 2026-10-20 19:40 — Direcția Cyber Universe OS (Adrian): OS de la zero, fără cod copiat și fără alte licențe — doar documentație
  publică și analiză vizuală/funcțională, apoi reconstruim. Citirea codului open-source pentru idei rămâne permisă, copiatul interzis
  (confirmat). Fiind de la zero, OS-ul trebuie să meargă pe hardware-ul actual de pe piață, cu drivere proprii scrise după specificații
  publice; se compară cu Windows pe același calculator. Înainte de mutarea pe laptop: analiză a ThinkPad-ului sub Windows (ce hardware și
  drivere vede, ce performanță are), păstrată ca referință; când OS-ul e funcțional, se compară punct cu punct și diferențele devin
  sarcini. Comanda pentru scriptul de analiză: amânată de Adrian („nu acum”).
- 2026-10-20 19:45 — Nu ne mutăm acum cu OS-ul pe laptop: pe ThinkPad se lucrează la suita office, care își atinge ținta în 1–2 săptămâni
  cel mult. Ținta suitei: o suită office făcută de la zero care să depășească Microsoft Office, Adobe și aplicațiile office Google.
  Pașii OS-ului pe laptop (inclusiv analiza Windows) vin după ce suita atinge ținta.
- 2026-10-20 19:50 — Suita office nu se dirijează prin hub: Adrian îi dă comenzile direct, în chatul ei (lucrează deja autonom, cu lista ei).
  În hub, suita doar raportează starea și poate propune colaborări. Comenzile prin `COMENZI.md` sunt pentru `kronos` și `cyber-universe`.
- 2026-10-20 20:10 — Suita office: licența (probă 30 de zile cu cheie înregistrată pe server + amprentă a calculatorului, abonament
  ~10–15 €/lună pentru tot pachetul, mod de citire după expirare) se face la SFÂRȘIT, ca strat separat. Aplicațiile și varianta de
  modul pentru Kronos și Cyber Universe rămân fără licență. Nicio propunere din hub nu include licențierea.
- 2026-10-20 22:35 — Cyber Universe OS: criptografia pentru HTTPS (TLS 1.3) se scrie în proiect, după standardele publice, fără
  biblioteci externe (D-011 în repo-ul OS; „da” dat de Adrian direct sesiunii OS, confirmat în centrul de comandă la 23:09).
  Condiție: fiecare funcție trece exemplele oficiale de test; până la o verificare separată, nu se folosește pentru date sensibile.
