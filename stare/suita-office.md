# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-22 05:15 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- O singură aplicație desktop (Electron + React + TypeScript), scrisă de la zero, totul local, fără cont și fără internet:
  Docs, Sheets, PDF, Slides, Imagini, Video, Notițe. Interfața e în română.
- Etapa 1 (compatibilitate) e gata: 529 de fișiere reale de test, 0 erori la deschidere (verificat din nou azi, la 23:46).
- Etapa 2 (toate funcțiile) e în lucru. Scoruri față de aplicațiile de referință: Word 78,1%, Excel 78,0%, Clipchamp 77,1%, Notițe 75,2%,
  PowerPoint 74,7%, Acrobat 70,8%, Photoshop 70,5%, formule de calcul 97,1% (100% fără cele care cer internet).
- Ultima sesiune (lucrul cerut de Adrian: butoanele grupate în file): **PDF e mutat în panglică**: Fișier (cu Recente, Creează și Export), Pornire, Comentarii,
  Semnătură, Editare, Pagini, Formulare, Protecție, Revizuire, Vizualizare; bara Semnează a intrat în filele Comentarii și Semnătură. Niciun buton nu a dispărut (135 din 135).
- Toate cele 91 de teste PDF rulate în aplicația reală: niciun buton negăsit; 12 teste adaptate la noile locuri. Toate modulele se deschid fără erori.

## Urmează
- PDF: contextualele Formular / Măsurare și clic dreapta pe pagină; apoi Slides, Video și Notițe în panglică; la Sheets mai rămân fila Grafic, mini-bara și cele 12 teste vechi care picau.
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
- De verificat (nu blochează): noile file din Docs, Sheets, **PDF** (Comentarii, Semnătură, Pagini) și din **Imagini** (bara de unelte din stânga, ◢ de lângă Selecție, fila Filtre, panourile cu file din dreapta, clic dreapta pe poză și pe strat). Găsești tot ce foloseai? Ce buton folosit des a ajuns prea ascuns?
- De verificat (nu blochează): un .xlsx cu model de Rezolvitor salvat din Suite, deschis în programul de calcul de la serviciu (Solver): trebuie să arate aceleași condiții.
- De verificat (nu blochează): un fișier (și o foaie protejată) salvat cu parolă din Suite, deschis în programul de birou de la serviciu (pe laptop nu e altul instalat).
- De verificat (nu blochează): un .docx protejat din Suite („🔐 Restricționează editarea” cu parolă), deschis la serviciu: trebuie să ceară parola la oprirea protecției.
- De verificat (nu blochează): un cod QR pus din Suite (Docs → ▣ Cod QR), scanat cu camera telefonului: trebuie să arate textul scris.
- De verificat (nu blochează): un PDF făcut cu „Fă-l PDF/A”, trecut printr-un validator PDF/A oficial (pe laptop nu e niciunul).
- Întrebare (nu blochează): marcajul de timp la semnarea PDF are nevoie de un server de timp pe internet (se trimite doar amprenta
  documentului, nu documentul). Îl adăugăm ca opțiune, cu un server ales de Adrian? Până atunci semnăturile au ora calculatorului.
- Codul e doar local, pe laptop; pus pe GitHub doar dacă Adrian decide.
