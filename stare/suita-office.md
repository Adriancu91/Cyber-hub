# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-22 11:37 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- O singură aplicație desktop (Electron + React + TypeScript), scrisă de la zero, totul local, fără cont și fără internet:
  Docs, Sheets, PDF, Slides, Imagini, Video, Notițe. Interfața e în română.
- Etapa 1 (compatibilitate) e gata: 529 de fișiere reale de test, 0 erori la deschidere.
- Etapa 2 (toate funcțiile) e în lucru. Scoruri față de aplicațiile de referință: Word 79,0%, Excel 78,0%, Clipchamp 77,1%, PowerPoint 76,0%,
  Notițe 76,0%, Acrobat 72,8%, Photoshop 71,9%, formule de calcul 97,1% (100% fără cele care cer internet).
- Butoanele grupate în file (cererea lui Adrian) sunt gata în toate cele 7 aplicații.
- Funcții noi (sesiunea 10:52–11:37): **dicționar de sinonime** în Docs și Slides (Shift+F7 și clic dreapta, ~1.000 de cuvinte, scris de noi);
  **despărțire automată în silabe** în Docs (regulile românești, și în .docx / .odt); **OCR în mai multe limbi** (română, engleză, maghiară,
  germană, franceză, fără internet); în Docs adresele web devin singure **legături** și 1/2 devine ½; în Slides bifa **„Folosește duratele”**.
- Toate aplicațiile pornesc fără erori; testele noi trec în aplicația reală.

## Urmează
- Restul funcțiilor din etapa 2 (Slides: narațiune înregistrată pe slide-uri; Sheets: formele în .xlsx; Docs: secțiuni; PDF: linearizarea).
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
- De încercat (nu blochează): un .docx cu „Despărțire în silabe → Automat” din Suite, deschis în programul de la serviciu: desparte și el cuvintele?
- De încercat (nu blochează): PDF → Text din scanare… pe un act în engleză sau maghiară, cu limba aleasă: iese textul corect?
- De încercat (nu blochează): PDF → ⚙ Lot… pe câteva acte scanate, cu „Fă-l căutabil”: merge căutarea în fișierele „-lot”?
- De încercat (nu blochează): un .pptx cu declanșator făcut în Suite, deschis în programul de prezentări de la serviciu.
- De verificat (nu blochează): noile file din toate aplicațiile. Găsești tot ce foloseai? Ce buton folosit des a ajuns prea ascuns?
- De verificat (nu blochează): .xlsx cu Rezolvitor, fișiere cu parolă și .docx protejat din Suite, deschise în programele de la serviciu.
- De verificat (nu blochează): un cod QR din Suite scanat cu telefonul; un PDF „Fă-l PDF/A” trecut printr-un validator oficial.
- Întrebare (nu blochează): marcajul de timp la semnarea PDF cere un server de timp pe internet (se trimite doar amprenta documentului).
  Îl adăugăm ca opțiune, cu un server ales de Adrian? Până atunci semnăturile au ora calculatorului.
- Codul e doar local, pe laptop; pus pe GitHub doar dacă Adrian decide.
