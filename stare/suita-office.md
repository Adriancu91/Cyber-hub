# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-21 13:25 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- O singură aplicație desktop (Electron + React + TypeScript), scrisă de la zero, totul local, fără cont și fără internet:
  Docs, Sheets, PDF, Slides, Imagini, Video, Notițe. Interfața e în română.
- Etapa 1 (compatibilitate) e gata: 529 de fișiere reale de test, 0 erori la deschidere (verificat din nou azi, la 13:05).
- Etapa 2 (toate funcțiile) e în lucru. Scoruri față de aplicațiile de referință: Clipchamp 76,3%, Word 75,2%, Excel 74,6%, Notițe 74,4%,
  PowerPoint 70,0%, Acrobat 67,3%, Photoshop 66,3%, formule de calcul 96%.
- Ultima sesiune (6 pași): Sheets — parolă la „Protejează foaia” și protejarea structurii registrului (cu .xlsx),
  numele definite se pot schimba (redenumite și în formule), validarea datelor cu formulă proprie; Slides — mărime proprie
  a slide-urilor în cm, modul Chioșc (prezentare care merge singură, în buclă).

## Urmează
- Restul funcțiilor din etapa 2 (PDF: editarea textului existent; Docs: secțiuni; Sheets: înghețarea la selecție).
- Etapa 3, calitate: viteză, stabilitate, memorie pe 8 GB, teste automate pentru fiecare modul.
- Etapa 5: pachet de instalare pentru Windows și testare cu colegii lui Adrian, cu formular de raportare.

## Ce oferă proiectul celorlalți
- Aplicațiile de birou pentru modulul Cyberspace (Kronos) și pentru setul de aplicații al Cyber Universe (după testarea umană).
- Fiecare aplicație e separată (`src/<modul>/`) și are `module.toml` după `standarde/modul-v0.md`.
- Motorul de formule (~500 de funcții, cu nume românești), analizele „ce-ar fi dacă”, criptarea (și a fișierelor .docx/.xlsx/.pptx cu parolă), formularele, semnarea și
  verificarea PDF (CMS, .pfx, PDF/A, accesibilitate), compararea PDF-urilor, graficele SVG, citările, îmbinarea de corespondență,
  cititorul EXIF, filtrele de imagine, găsirea pozelor pe o scanare, cititorii și scriitorii .rtf / .txt / .ods / .gif animat,
  importul/exportul .docx/.xlsx/.pptx/.pdf/.odt/.psd pot fi refolosite.

## De ce are nevoie de la ceilalți
- Nimic acum.

## Blocaje / nevoie de Adrian
- De verificat (nu blochează): un fișier (și o foaie protejată) salvat cu parolă din Suite, deschis în programul de birou de la serviciu (pe laptop nu e altul instalat).
- Întrebare (nu blochează): marcajul de timp la semnarea PDF are nevoie de un server de timp pe internet (se trimite doar amprenta
  documentului, nu documentul). Îl adăugăm ca opțiune, cu un server ales de Adrian? Până atunci semnăturile au ora calculatorului.
- Codul e doar local, pe laptop; pus pe GitHub doar dacă Adrian decide.
