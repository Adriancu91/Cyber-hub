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
- 2026-10-21 10:05 — Cyber Universe OS: **rămâne oprit** (nu se închide Faza 5, nu pornește Faza 6) până la testul pe un
  calculator real (B-001 / P3-09). Adrian face testul pe alt calculator când are timp; sesiunile OS reiau lucrul abia după
  rezultatele testului (P3-09, P3-10) sau după o comandă nouă în `COMENZI.md`. Nu e nevoie să mai întrebe.
- 2026-10-21 10:05 — Kronos: S13 aprobat (#407 în fila „Întreabă din text”); S8 reaprobat, cu standardul copiat în
  `cyberspace/plan/hub_modul-v0.md`. Regulă: executantul Kronos nu poate citi hub-ul; ce are de citit de acolo ajunge în `plan/`.
- 2026-10-21 22:15 — Primul test al Cyber Universe OS pe hardware real a reușit (Lenovo ThinkPad, altul decât al suitei): desktop,
  touchpad, tastatură, editor. OS-ul e deblocat (comanda C-2): completează HARDWARE/USB/BLOCKERS, pregătește testul 2, apoi continuă.
- 2026-10-21 22:25 — **Direcția Fazei 6 a Cyber Universe OS (Adrian): OS-ul devine loc de lucru cu Claude înăuntru**, pe laptopul de test
  (AMD Ryzen, rețea Realtek 10ec:8168). Ordinea: (1) driver Realtek RTL8168 după documentația publică; (2) rădăcinile reale de încredere,
  ca HTTPS să meargă cu site-uri adevărate; (3) aplicația „Claude” în OS: chat prin API cu cheia lui Adrian ținută local, cu voie să citească/scrie
  fișiere pe disc și să ruleze comenzi în OS (agent înăuntru); (4) auto-actualizare: OS-ul descarcă ultima versiune construită de CI de pe GitHub
  și o scrie pe stick; (5) trimitere pe GitHub din OS, prin API. Construirea OS-ului rămâne în cloud (CI); compilarea din interiorul OS-ului nu e
  un obiectiv acum. Faza 5 se consideră închisă fără P5-07/P5-08 (mutate după suită). Wi-Fi (Intel AX200, firmware) rămâne pentru mai târziu.
- 2026-10-22 01:42 — **Direcția nouă a lui Kronos (Adrian, trei „da”)**, după S15 (tipurile văzute 30/30, nevăzute 6/50) și strategia din
  `cyberspace/docs/rapoarte/2026-10-22_0200_strategie_nucleu_fara_llm.md`: (1) ținta e un AI propriu **fără LLM** (nicio inteligență
  străină ca nucleu, profesor sau evaluator), cu „performanță de top” măsurată pe **domenii cu verificator** (documente în română, cod cu
  teste, gramatică), nu pe conversație liberă; metoda: auto-joc cu verificator (H3) + specialiști mici cu ruter (H4) + memorie mare în RAM (H2);
  autonomia crește pe trepte (L1 date proprii → L2 bucla singură în buget → L3 programe verificate), nu prin permisiuni. (2) **Qwen iese din
  rolul de judecător** la „răspuns din text”; notarea se face cu verificatoare proprii (E0). Dependențele rămase (Qwen pentru poveștile vechi,
  TinyStories, Claude în cascadă) se declară și se înlocuiesc pe rând. (3) Supraveghetorul primește E0 → E1 în `plan/coada.md`; nu se mai fac
  nopți de antrenare cu rețeta veche pentru tipuri nevăzute.
