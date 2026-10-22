# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-22 10:51 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- O singură aplicație desktop (Electron + React + TypeScript), scrisă de la zero, totul local, fără cont și fără internet:
  Docs, Sheets, PDF, Slides, Imagini, Video, Notițe. Interfața e în română.
- Etapa 1 (compatibilitate) e gata: 529 de fișiere reale de test, 0 erori la deschidere.
- Etapa 2 (toate funcțiile) e în lucru. Scoruri față de aplicațiile de referință: Word 78,1%, Excel 78,0%, Clipchamp 77,1%, Notițe 76,0%,
  PowerPoint 75,5%, Acrobat 72,6%, Photoshop 71,9%, formule de calcul 97,1% (100% fără cele care cer internet).
- **Butoanele grupate în file (cererea lui Adrian) sunt gata în toate cele 7 aplicații.** Ultima sesiune a încheiat-o:
  **Sheets** are fila Grafic (clic pe un grafic) și o mini-bară de formatare la clic dreapta pe celulă; **PDF** are fila Câmp
  (cursorul într-un câmp de formular) și clic dreapta pe comentariile din fișier (Răspunde, Starea, Bifat).
- Funcții noi (sesiunea 10:07–10:51): **Slides**: Variante ale temelor (4 variante de culori pe temă) și **declanșatoare** pentru animații
  (o animație pornește doar la click pe o casetă aleasă, de exemplu un buton „Răspuns”; ajung și în .pptx); **PDF**: după OCR, lista
  cuvintelor nesigure, fiecare cu bucata ei de pagină, de corectat înainte de a intra în PDF; **Imagini**: bara de unelte se poate
  personaliza (ascunzi uneltele nefolosite); **Notițe**: riglă și raportor în fereastra Desen (linii drepte la orice unghi și arce).
- Toate aplicațiile pornesc fără erori; testele noi trec în aplicația reală.

## Urmează
- Restul funcțiilor din etapa 2 (Sheets: formele în .xlsx; Docs: secțiuni; PDF: linearizarea; Imagini: puncte trase pe poză la Tilt-Shift / Iris).
- Etapa 3, calitate; etapa 5: pachet de instalare și testare cu colegii lui Adrian.

## Ce oferă proiectul celorlalți
- Aplicațiile de birou pentru modulul Cyberspace (Kronos) și pentru setul de aplicații al Cyber Universe (după testarea umană).
- Fiecare aplicație e separată (`src/<modul>/`) și are `module.toml` după `standarde/modul-v0.md`.
- Cadrul comun de interfață (panglica cu file, mini-bara, clic dreapta, panourile andocate), motorul de formule (~500 de funcții),
  rezolvitorul de optimizare, statisticile, generatorul de coduri QR, criptarea, formularele și semnarea PDF, PDF/A, cele 67 de filtre de imagine,
  cititorii și scriitorii .docx / .xlsx / .pptx / .pdf / .odt / .rtf / .psd pot fi refolosite.

## De ce are nevoie de la ceilalți
- Nimic acum.

## Blocaje / nevoie de Adrian
- De încercat (nu blochează): PDF → ⚙ Lot… pe câteva acte scanate, cu „Fă-l căutabil”: merge căutarea în fișierele „-lot”?
- De încercat (nu blochează): un .pptx cu declanșator făcut în Suite (Animații → ⚡ Declanșator), deschis în programul de prezentări de la serviciu: animația pornește la click pe caseta aleasă?
- De verificat (nu blochează): noile file din toate aplicațiile. Găsești tot ce foloseai? Ce buton folosit des a ajuns prea ascuns?
  Noutăți de încercat: Sheets — clic pe un grafic (fila Grafic) și clic dreapta pe o celulă (mini-bara); PDF — clic într-un câmp de formular (fila Câmp).
- De verificat (nu blochează): un .xlsx cu model de Rezolvitor salvat din Suite, deschis în programul de calcul de la serviciu: aceleași condiții.
- De verificat (nu blochează): un fișier (și o foaie protejată) salvat cu parolă din Suite, deschis în programul de birou de la serviciu.
- De verificat (nu blochează): un .docx protejat din Suite („🔐 Restricționează editarea” cu parolă), deschis la serviciu: cere parola la oprire.
- De verificat (nu blochează): un cod QR pus din Suite (Docs → ▣ Cod QR), scanat cu camera telefonului.
- De verificat (nu blochează): un PDF făcut cu „Fă-l PDF/A”, trecut printr-un validator PDF/A oficial.
- Întrebare (nu blochează): marcajul de timp la semnarea PDF cere un server de timp pe internet (se trimite doar amprenta documentului).
  Îl adăugăm ca opțiune, cu un server ales de Adrian? Până atunci semnăturile au ora calculatorului.
- Codul e doar local, pe laptop; pus pe GitHub doar dacă Adrian decide.
