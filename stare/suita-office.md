# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-21 21:31 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- O singură aplicație desktop (Electron + React + TypeScript), scrisă de la zero, totul local, fără cont și fără internet:
  Docs, Sheets, PDF, Slides, Imagini, Video, Notițe. Interfața e în română.
- Etapa 1 (compatibilitate) e gata: 529 de fișiere reale de test, 0 erori la deschidere (verificat din nou azi, la 21:30).
- Etapa 2 (toate funcțiile) e în lucru. Scoruri față de aplicațiile de referință: Word 78,1%, Excel 77,9%, Clipchamp 77,1%, Notițe 75,2%,
  PowerPoint 73,6%, Acrobat 69,2%, Photoshop 68,8%, formule de calcul 97,1% (100% fără cele care cer internet).
- Ultima sesiune (7 pași): în Sheets, forme și casete de text peste celule; în Docs, temele documentului (temă, fonturi, culori);
  în Imagini, mărimea pozei după conținut (oamenii nu se turtesc); în Slides, tranziția Transformare (și în .pptx); în PDF, trecerea
  în tonuri de gri; în Notițe, înregistrarea video cu camera; în Video, efectele de mișcare (tremurat, rotire lentă, pulsare).

## Urmează
- Restul funcțiilor din etapa 2 (Sheets: formele scrise ca forme în .xlsx, previzualizare în Analiza rapidă, gruparea manuală în Rezumat; Docs: culorile temei în paleta de culori, secțiuni; PDF: câmp cod de bare din formular, editarea textului existent).
- Etapa 3, calitate: viteză, stabilitate, memorie pe 8 GB, teste automate pentru fiecare modul.
- Etapa 5: pachet de instalare pentru Windows și testare cu colegii lui Adrian, cu formular de raportare.

## Ce oferă proiectul celorlalți
- Aplicațiile de birou pentru modulul Cyberspace (Kronos) și pentru setul de aplicații al Cyber Universe (după testarea umană).
- Fiecare aplicație e separată (`src/<modul>/`) și are `module.toml` după `standarde/modul-v0.md`.
- Motorul de formule (~500 de funcții, cu nume românești), rezolvitorul de optimizare (simplex + ramificare + Nelder–Mead), prognoza
  cu netezire exponențială și sezon, statisticile și analizele (regresie, ANOVA, teste F / t / z), generatorul de coduri QR,
  criptarea (și a fișierelor .docx/.xlsx/.pptx cu parolă), formularele, semnarea, verificarea și conversia PDF/A, accesibilitatea PDF,
  compararea PDF-urilor, graficele SVG, scalarea pozelor după conținut, trecerea PDF-urilor în tonuri de gri, citările, îmbinarea de corespondență, cititorul EXIF, cele 66 de filtre de imagine,
  cititorii și scriitorii .rtf / .txt / .ods / .gif animat, importul/exportul .docx/.xlsx/.pptx/.pdf/.odt/.psd pot fi refolosite.

## De ce are nevoie de la ceilalți
- Nimic acum.

## Blocaje / nevoie de Adrian
- De verificat (nu blochează): un .xlsx cu model de Rezolvitor salvat din Suite, deschis în programul de calcul de la serviciu (Solver): trebuie să arate aceleași condiții.
- De verificat (nu blochează): un fișier (și o foaie protejată) salvat cu parolă din Suite, deschis în programul de birou de la serviciu (pe laptop nu e altul instalat).
- De verificat (nu blochează): un .docx protejat din Suite („🔐 Restricționează editarea” cu parolă), deschis la serviciu: trebuie să ceară parola la oprirea protecției.
- De verificat (nu blochează): un cod QR pus din Suite (Docs → ▣ Cod QR), scanat cu camera telefonului: trebuie să arate textul scris.
- De verificat (nu blochează): un PDF făcut cu „Fă-l PDF/A”, trecut printr-un validator PDF/A oficial (pe laptop nu e niciunul).
- Întrebare (nu blochează): marcajul de timp la semnarea PDF are nevoie de un server de timp pe internet (se trimite doar amprenta
  documentului, nu documentul). Îl adăugăm ca opțiune, cu un server ales de Adrian? Până atunci semnăturile au ora calculatorului.
- Codul e doar local, pe laptop; pus pe GitHub doar dacă Adrian decide.
