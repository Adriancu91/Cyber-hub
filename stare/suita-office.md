# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-22 13:09 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- O singură aplicație desktop (Electron + React + TypeScript), scrisă de la zero, totul local, fără cont și fără internet:
  Docs, Sheets, PDF, Slides, Imagini, Video, Notițe. Interfața e în română.
- Etapa 1 (compatibilitate) e gata: 529 de fișiere reale de test, 0 erori la deschidere.
- Etapa 2 (toate funcțiile) e în lucru. Scoruri față de aplicațiile de referință: Word 80,1%, Excel 79,5%, Clipchamp 77,1%, PowerPoint 76,2%,
  Notițe 76,4%, Acrobat 72,8%, Photoshop 72,0%, formule de calcul 97,1% (100% fără cele care cer internet).
- Funcții noi (sesiunea 12:22–13:09): în Docs **Verifică compatibilitatea** (ce se pierde la .docx / .odt / .txt) și **controlul rândurilor
  văduve / orfane**; în Sheets **graficul cu bule**, **ecuații pe foaie**, **rezumate (pivot) recomandate** dintr-un clic și **copiază celulele
  ca imagine**; în Slides **alegerea ecranului** pentru prezentare (proiector / doar laptopul / un monitor anume); în Imagini filtrul **Ramă**
  (lemn, aurie, paspartu…); în Video 4 stiluri noi de text (casetă, contur, film, citat); în Notițe **Trimite prin e-mail**.
- Reparat: graficele „Soare” și „Bursier” din Sheets deveneau „Coloane” la redeschiderea fișierului.
- Toate aplicațiile pornesc fără erori; testele noi trec în aplicația reală; testul de compatibilitate: 0 erori.
- Într-o sesiune separată s-a pregătit programul de instalare Windows 0.9.0 (pentru etapa 5, testarea cu oameni).

## Urmează
- Restul funcțiilor din etapa 2 (Docs: secțiuni și verificarea compatibilității; Slides: narațiune înregistrată pe slide-uri; PDF: linearizarea).
- Etapa 3, calitate; etapa 5: pachet de instalare și testare cu colegii lui Adrian.

## Ce oferă proiectul celorlalți
- Aplicațiile de birou pentru modulul Cyberspace (Kronos) și pentru setul de aplicații al Cyber Universe (după testarea umană).
- Fiecare aplicație e separată (`src/<modul>/`) și are `module.toml` după `standarde/modul-v0.md`.
- Cadrul comun de interfață (panglica cu file, mini-bara, clic dreapta, panourile andocate), motorul de formule (~500 de funcții),
  dicționarul de sinonime și despărțirea în silabe în română, OCR-ul în 5 limbi, criptarea, formularele și semnarea PDF, PDF/A,
  cele 67 de filtre de imagine, cititorii și scriitorii .docx / .xlsx / .pptx / .pdf / .odt / .rtf / .psd pot fi refolosite.

## De ce are nevoie de la ceilalți
- Nimic acum.

## Blocaje / nevoie de Adrian
- De încercat (nu blochează): un .xlsx cu forme (un balon cu text) făcut în Suite, deschis în programul de la serviciu: se poate edita forma?
- De încercat (nu blochează): un .docx cu „Despărțire în silabe → Automat” din Suite, deschis în programul de la serviciu: desparte și el cuvintele?
- De încercat (nu blochează): PDF → Text din scanare… pe un act în engleză sau maghiară, cu limba aleasă: iese textul corect?
- De încercat (nu blochează): Slides → Prezentare → 🖵 Ecran, cu un proiector sau al doilea monitor legat (aici s-a testat doar cu un ecran închipuit).
- De încercat (nu blochează): un .pptx cu declanșator făcut în Suite, deschis în programul de prezentări de la serviciu.
- De verificat (nu blochează): noile file din toate aplicațiile. Găsești tot ce foloseai? Ce buton folosit des a ajuns prea ascuns?
- De verificat (nu blochează): .xlsx cu Rezolvitor, fișiere cu parolă și .docx protejat din Suite, deschise în programele de la serviciu.
- De verificat (nu blochează): un cod QR din Suite scanat cu telefonul; un PDF „Fă-l PDF/A” trecut printr-un validator oficial.
- Întrebare (nu blochează): marcajul de timp la semnarea PDF cere un server de timp pe internet (se trimite doar amprenta documentului).
  Îl adăugăm ca opțiune, cu un server ales de Adrian? Până atunci semnăturile au ora calculatorului.
- Codul e doar local, pe laptop; pus pe GitHub doar dacă Adrian decide.
