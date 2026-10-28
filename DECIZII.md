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

- 2026-10-22 14:45 — **Cyber Universe OS: bucla de test de la distanță (Adrian, „da” la C-7).** Laptopul de test se actualizează singur din
  ultimul Release, rulează comenzile din `test/comenzi.txt` (repo-ul OS) și trimite rezultatele înapoi pe GitHub; sesiunea OS le citește și
  repară; Adrian doar ține laptopul pornit, cu cablul băgat și BIOS-ul setat să pornească automat de pe stick. Condiție: C-6 (rețeaua) gata.
  Eu, din cloud, nu intru direct în laptop (e după router): bucla merge prin GitHub, cu token limitat la depozitul OS.
- 2026-10-22 15:10 — **Kronos: placa video se folosește oricând, ziua și noaptea** (Adrian: workstation-ul e ținut pornit doar pentru
  Kronos; îl folosește foarte rar, pentru o imprimare sau un PDF). S17 pornește imediat, nu la 19:00. Supraveghetorul nu mai lasă placa
  liberă ziua când există o sarcină aprobată. Regulile de siguranță (pre-înregistrare, paznic, un singur lucru pe placă) rămân.
- 2026-10-22 16:55 — **Cyber Universe OS, regulă permanentă pentru drivere (Adrian, după regresia de la testul 5):** la un driver testat pe
  hardware real se face **o singură schimbare de comportament pe Release**, verificată pe laptop înainte de următoarea; orice registru de
  configurare (PCI, ale plăcii) se scrie doar citire → modificarea unui singur bit → scriere, cu valoarea dinainte și de după în jurnal; la
  fiecare Release, `log rtl` (și echivalentul pentru alte drivere) arată registrele cheie, ca o poză să fie de ajuns pentru comparație cu
  versiunea anterioară. O ipoteză se declară „confirmată” numai după testul pe hardware, nu după citirea codului sau după QEMU.
- 2026-10-22 18:30 — **Reper: prima ieșire pe internet a Cyber Universe OS pe hardware real** (ThinkPad, Release os-138, pornit din meniul F12,
  cu golirea cache-ului): DHCP de la routerul lui Adrian, ping, DNS, HTTPS cu TLS 1.3 și certificat verificat (`example.com`), totul cu cod
  propriu. Lecția zilei, notată ca regulă: testele pe hardware se fac cu cablul **la router**, iar fiecare reparație se verifică și la rece
  (pornire directă) și la cald (meniul F12).
- 2026-10-22 22:50 — **Mediul de test pentru OS: partajarea conexiunii din Windows (ICS)** — cablu între laptopul de test și laptopul cu
  Windows, care dă adrese 192.168.137.x și internet; echivalent cu routerul (verificat: DHCP, DNS, HTTPS). Wi-Fi în OS rămâne amânat.
- 2026-10-22 23:10 — **Drumul OS-ului, în ordine (Adrian):** (1) OS funcțional și autonom pentru lucru (pornirea la rece, bucla de test de la distanță
  C-7); (2) **câteva experimente mici cu placa video** (întâi pe laptopul de test, AMD; pe workstation doar într-o fereastră stabilită cu Adrian,
  ca să nu oprească Kronos); (3) **documentare**: studiu de fezabilitate pentru un driver propriu, din surse publice (modulele MIT ale NVIDIA,
  nova, Mesa/NVK, documentația AMD), fără cod copiat; (4) în funcție de ce aflăm, încercăm **driverul propriu de la zero**; (5) după experimente,
  bune sau rele, **decidem și măsurăm ce e mai bine pentru Kronos** (unde rulează, unde se antrenează). Pas cu pas; nicio etapă nu o ține pe
  loc pe cealaltă. Driverele originale NVIDIA nu se instalează în OS-ul nostru (ar cere un Linux în interior); Wi-Fi rămâne amânat.
  Etapa 1 „Kronos în Cyber Universe” (pe procesor și RAM, antrenarea rămâne pe workstation) și etapa 2 (OS obișnuit în jur) merg în paralel.
- 2026-10-23 02:40 — **Al patrulea proiect: Cyber-GPU (`Adriancu91/cyber-gpu`)**, pornit de Adrian cu „MASTER PROMPT — CYBER-GPU v1.0”:
  driver propriu de calcul (fără grafică) pentru RTX 3070 Ti, Rust `no_std`, clean-room, ca workspace separat care nu modifică alte repo-uri
  (schimbările în OS = patch-uri de integrare preluate de sesiunea OS). Testele pe RTX: doar pe workstation, în ferestre aprobate de Adrian.
  Regula de cinste din prompt se aplică: nimic nu e „executat pe GPU” fără demonstrație pe placa fizică; QEMU/simulările se etichetează ca atare.
  C-11 (experimentele mici + studiul) rămâne în `cyber-universe`; cele două se completează, nu se dublează.
- 2026-10-23 10:20 — **Adrian pleacă câteva zile.** Kronos în **pauză** (nimic pe placă; S20 așteaptă întoarcerea; workstation-ul rămâne în
  Windows). Lucrează automat, în cloud, fără hardware: **OS-ul** (C-13, apoi C-14: driverul de rețea I219 al workstation-ului și pregătirea
  „Kronos în OS pe procesor” — SSE/AVX, SMP, memorie mare) și **Cyber-GPU** (sesiune programată nouă, de 4 ori pe zi, cod și teste în simulare,
  fără placa reală). **Niciun test pe hardware** până la întoarcere; listele se strâng în `stare/`. Integrarea `cyber-gpu` → OS se face prin
  `integrare/cyber-gpu/` din hub (repo-ul `cyber-gpu` e privat, sesiunea OS nu-l poate citi).
- 2026-10-23 10:20 — **Kronos lucrează și cât e Adrian plecat** (pauza de la 10:15 ridicată): S20 = varianta 1 (E1 închis cu NECLAR); **E2 aprobat**
  (3 specialiști + ruter, antrenați pe rând din #415, criteriile din strategia §7); după E2, pregătirea E3 (indexul de memorie) doar pe procesor.
  Fără date noi descărcate. Când Adrian revine, workstation-ul se eliberează pentru fereastra OS/GPU (~30–60 min) între sarcini.
- 2026-10-23 19:05 — **`cyber-universe` devine public** (Adrian), ca GitHub Actions să fie gratuit: minutele pentru repo-uri private s-au terminat
  (B-004: „recent account payments have failed or your spending limit needs to be increased”). Istoricul a fost verificat înainte: nicio cheie
  reală (doar certificatele și cheile de test din `tls/tests/data/`). Regula rămâne: cheile și tokenurile nu ajung niciodată în repo sau în hub.
  19:10 — **și `cyber-gpu` devine public** (Adrian; istoricul verificat: nicio cheie). `cyberspace` și `Cyber-hub` rămân private (n-au CI pe GitHub).
  Consecință: sesiunea OS poate citi `cyber-gpu` direct; patch-urile nu mai trebuie copiate prin `integrare/cyber-gpu/` (rămâne ca arhivă).
- 2026-10-23 19:30 — **Integrarea OS + Cyber-GPU (C-16), cu punct de revenire** (Adrian): înainte de orice, tag-ul `stabil-2026-10-23` pe starea de
  acum (OS `9f67d7b`, Cyber-GPU `41e44ba`), pus de sesiunile proiectelor (centrul de comandă nu are drept de scriere în ele); integrarea pe ramură
  separată, unită în `main` doar cu toate testele trecute; copii offline (git bundle) trimise lui Adrian. Commit-urile de pe GitHub nu se pierd
  (push --force interzis), iar Release-urile testate pe hardware (os-150, os-161) rămân descărcabile.
- 2026-10-24 04:05 — **Pauză totală până luni 26 oct** (Adrian se întoarce): oprite sesiunile programate OS, Cyber-GPU, coordonatorul și
  supraveghetorul Kronos (se repornesc la cererea lui Adrian). Kronos: nicio sarcină nouă; S27 așteaptă „da”-ul. Workstation-ul se oprește singur
  în siguranță (S28: doar dacă nu rulează nimic și după ce totul e urcat pe GitHub). Suita (pe laptop) nu e atinsă de pauză.
- 2026-10-26 16:10 — **Pauza se ridică pentru Kronos; S27 aprobat** (Adrian: „dacă stă degeaba dai de lucru”): supraveghetorul Kronos repornit
  (8 treceri pe zi). S27 = E3 cu antrenare pe placă, cu pragurile propuse: confirmat la ≥ 60 % răspunsuri corecte fără text dat și cel mult
  2 puncte pierdute pe noaptea 10 / S4 cu textul dat; infirmat sub 45 %. Pre-înregistrarea se scrie înainte de pornire. Sesiunile OS,
  Cyber-GPU și coordonatorul rămân oprite până la „pornește tot”.
- 2026-10-26 17:10 — **Cyber-GPU deblocat** (Adrian: „da la toate recomandările tale actuale și viitoare despre cyber-gpu”):
  firmware-ul semnat NVIDIA **da** (versiunea 570.144, ținut separat pe stick, niciodată în repo); compilator **Mesa NAK**; tabel de compatibilitate
  (C-18); `gpu gfw` + `gpu vbios` doar citire în OS (C-19). Recomandările viitoare ale centrului de comandă pentru Cyber-GPU se consideră aprobate,
  **cu limitele care rămân valabile**: nicio scriere în placa reală fără Adrian de față, nimic ireversibil, nimic care costă bani, fără firmware
  sau cod copiat în repo, fără desfacerea firmware-ului NVIDIA. Acestea se întreabă în continuare.
- 2026-10-26 17:45 — **Delegare generală** (Adrian: „merg pe recomandările tale… orice decizie care coincide cu direcția și punctul final este aprobată
  automat de mine”). Centrul de comandă poate aproba singur ce se potrivește direcției lui Adrian (totul propriu, ≥ 90 %, modular, rapid pe hardware
  slab, reversibil; Kronos fără LLM străin; OS + driver GPU proprii care găzduiesc Kronos) și o trece aici, ca să se vadă. **Rămân la Adrian, explicit:**
  orice test sau scriere pe hardware real (doar cu el de față), orice pas ireversibil (ștergeri, rescrierea istoriei), bani și conturi, chei și parole,
  schimbarea examenului Kronos sau a paznicului, schimbări în `kronos/` (nucleu) și orice risc juridic real.
  Aprobate acum: Kronos C-21 (memoria E3, Muon, motorul fără PyTorch — după S27); OS C-22 („cutia neagră” pe stick, permisiuni pe program);
  Cyber-GPU: pregătirea probei tinygrad (A), rularea ei doar cu Adrian de față.
  **TinyStories** (generat cu GPT-3.5/4, din memorie, de verificat) rămâne deocamdată: e în examenul oficial, iar scoaterea lui ar strica toate
  comparațiile; datele NOI nu au voie să vină de la un LLM străin; înlocuirea lui se decide la linia nouă „w3”.
- 2026-10-27 18:00 — **Kronos S38 aprobat** (centrul de comandă, prin delegarea din 26 oct 17:45): o noapte cu rețeta A (sau D, după S36), din #441, cu pre-înregistrare.
- 2026-10-27 23:20 — **Kronos adevărat în OS** (centrul de comandă, prin delegare): C-24 (Kronos: specificația KGR1 + vectori de test în hub, modelul exportat ca Release privat) și C-25 (OS: motor KGR1 în Rust + comanda `kronos`, după C-23). Greutățile reale nu ajung în repo-uri publice sau în hub.
- 2026-10-27 23:35 — **OS-ul care se reglează singur, pasul 1** (centrul de comandă, prin delegare, la întrebarea lui Adrian despre Kronos care își dezvoltă singur sistemul): C-27, căutare automată verificată a celei mai bune variante de calcul pe fiecare calculator. Agentul care scrie singur cod/drivere în OS rămâne pe termen lung: Kronos e prea mic azi; când va veni, lucrează doar într-o cutie izolată, cu teste și paznic, iar schimbările intră în sistemul real doar cu aprobarea lui Adrian.
- 2026-10-27 23:45 — **E4 Kronos-Cod aprobat** (ideea lui Adrian, prin delegare): model separat ~150M doar pe cod real cu licențe permisive, apoi auto-îmbunătățire verificată prin teste rulate într-o cutie izolată (C-28, după S38). Linia română rămâne separată și neatinsă.
- 2026-10-27 23:40 — **Direcția pe termen lung (Adrian):** Kronos dedicat pe cod și autodezvoltare, care își adaptează și își îmbunătățește singur mediul Cyber Universe (sistem, drivere) ca să fie cât mai puternic pe hardware limitat. Condițiile centrului de comandă, valabile la fiecare pas: judecătorul (examenele, testele, paznicul) rămâne **în afara** controlului lui Kronos; orice schimbare se face întâi într-o cutie izolată, cu revenire garantată; autonomia crește treptat (C-27 → C-28 → mai departe), iar ce intră în sistemul real trece pe la Adrian.
- 2026-10-27 23:49 — **Adrian: „Da” pentru porturile `cautare` și `inferenta` în nucleul `kronos/`** (doar ele + contractele; toate testele trebuie să treacă).
- 2026-10-28 14:30 — **Licență proprietară pentru codul nou** al OS-ului și al driverului GPU (Adrian, „2”): „toate drepturile rezervate” de la următorul commit (C-32, C-33); versiunile publicate până la `0bf1303` (OS) și `8313973` (GPU) rămân MIT. Kronos rămâne privat. Vizibilitatea repo-urilor (public/privat) o schimbă Adrian în setări, dacă vrea; teste GitHub plătite: nu, fără acordul lui. De verificat cu un avocat înainte de investitori.
- 2026-10-28 14:33 — **`cyber-universe` și `cyber-gpu` sunt din nou private** (Adrian). Verificat: sesiunea centrului de comandă le citește în continuare (clonare și Release-uri). Dacă GitHub Actions se oprește din lipsă de minute, nu se plătește nimic fără acordul lui Adrian; testele rămân cele din sesiuni (QEMU).
- 2026-10-28 19:00 — **B-005 (OS nu mai poate citi cyber-gpu privat) ocolit prin copie în hub-ul privat**: `integrare/cyber-gpu/snapshot/cyber-gpu.bundle` (git bundle, 0,5 MB, vârf `8313973`), actualizat de sesiunea Cyber-GPU după fiecare push (C-34). Aplicația GitHub Claude are deja acces la toate repo-urile (verificat de Adrian); accesul sesiunilor programate e altă limită. Repo-urile rămân private.
