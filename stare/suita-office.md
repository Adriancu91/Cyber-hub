# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-22 01:25 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- O singură aplicație desktop (Electron + React + TypeScript), scrisă de la zero, totul local, fără cont și fără internet:
  Docs, Sheets, PDF, Slides, Imagini, Video, Notițe. Interfața e în română.
- Etapa 1 (compatibilitate) e gata: 529 de fișiere reale de test, 0 erori la deschidere (verificat din nou azi, la 23:46).
- Etapa 2 (toate funcțiile) e în lucru. Scoruri față de aplicațiile de referință: Word 78,1%, Excel 78,0%, Clipchamp 77,1%, Notițe 75,2%,
  PowerPoint 74,7%, Acrobat 70,8%, Photoshop 70,5%, formule de calcul 97,1% (100% fără cele care cer internet).
- Ultima sesiune (lucrul cerut de Adrian: butoanele grupate în file): **Docs e mutat complet în panglică**. Nou azi: fila Aspect cu liste rapide
  (Margini, Orientare, Mărime, Coloane, Filigran, Culoarea și Chenarul paginii, plus retrageri și spații la paragraf), fila **Imagine** care apare
  singură la clic pe o poză, **mini-bara** de formatare lângă textul ales, **clic dreapta** cu comenzile locului (text, tabel, imagine) și **Recente** în Fișier.
- Niciun buton nu a dispărut (verificat automat, 136 de controale); pentru Imagini e gata lista de bază (83 de controale) înainte de mutare.

## Urmează
- Prima prioritate: aceleași file în Imagini (file sus, bara verticală de unelte, panourile din dreapta), apoi Sheets, PDF, Slides, Video și Notițe.
- Restul funcțiilor din etapa 2 (Imagini: poziția proprie a straturilor; PDF: linearizarea; Sheets: formele în .xlsx; Docs: secțiuni; Video: clipul liber pe pânză).
- Etapa 3, calitate; etapa 5: pachet de instalare și testare cu colegii lui Adrian.

## Ce oferă proiectul celorlalți
- Aplicațiile de birou pentru modulul Cyberspace (Kronos) și pentru setul de aplicații al Cyber Universe (după testarea umană).
- Fiecare aplicație e separată (`src/<modul>/`) și are `module.toml` după `standarde/modul-v0.md`.
- Motorul de formule (~500 de funcții, cu nume românești), rezolvitorul de optimizare (simplex + ramificare + Nelder–Mead), prognoza
  cu netezire exponențială și sezon, statisticile și analizele (regresie, ANOVA, teste F / t / z), generatorul de coduri QR,
  criptarea (și a fișierelor .docx/.xlsx/.pptx cu parolă), formularele, semnarea, verificarea și conversia PDF/A, accesibilitatea PDF,
  compararea PDF-urilor, separările de culoare, portofoliile PDF, exportul PDF → XML, graficele SVG, scalarea pozelor după conținut, trecerea PDF-urilor în tonuri de gri, citările, îmbinarea de corespondență, cititorul EXIF, cele 67 de filtre de imagine,
  cititorii și scriitorii .rtf / .txt / .ods / .gif animat, importul/exportul .docx/.xlsx/.pptx/.pdf/.odt/.psd pot fi refolosite.

## De ce are nevoie de la ceilalți
- Nimic acum.

## Blocaje / nevoie de Adrian
- De verificat (nu blochează): noile file din Docs (Pornire, Inserare, Aspect…), mini-bara de lângă textul ales și clicul dreapta (pe un cuvânt greșit, într-un tabel, pe o poză). Găsești tot ce foloseai? Ce buton folosit des a ajuns prea ascuns?
- De verificat (nu blochează): un .xlsx cu model de Rezolvitor salvat din Suite, deschis în programul de calcul de la serviciu (Solver): trebuie să arate aceleași condiții.
- De verificat (nu blochează): un fișier (și o foaie protejată) salvat cu parolă din Suite, deschis în programul de birou de la serviciu (pe laptop nu e altul instalat).
- De verificat (nu blochează): un .docx protejat din Suite („🔐 Restricționează editarea” cu parolă), deschis la serviciu: trebuie să ceară parola la oprirea protecției.
- De verificat (nu blochează): un cod QR pus din Suite (Docs → ▣ Cod QR), scanat cu camera telefonului: trebuie să arate textul scris.
- De verificat (nu blochează): un PDF făcut cu „Fă-l PDF/A”, trecut printr-un validator PDF/A oficial (pe laptop nu e niciunul).
- Întrebare (nu blochează): marcajul de timp la semnarea PDF are nevoie de un server de timp pe internet (se trimite doar amprenta
  documentului, nu documentul). Îl adăugăm ca opțiune, cu un server ales de Adrian? Până atunci semnăturile au ora calculatorului.
- Codul e doar local, pe laptop; pus pe GitHub doar dacă Adrian decide.
