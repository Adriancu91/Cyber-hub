# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-21 09:41 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- O singură aplicație desktop (Electron + React + TypeScript), scrisă de la zero, totul local, fără cont și fără internet:
  Docs, Sheets, PDF, Slides, Imagini, Video, Notițe. Interfața e în română.
- Etapa 1 (compatibilitate) e gata: 529 de fișiere reale de test, 0 erori la deschidere (verificat din nou azi, la 09:40).
- Etapa 2 (toate funcțiile) e în lucru. Scoruri față de aplicațiile de referință: Clipchamp 75,6%, Word 74,3%, Notițe 74,0%,
  Excel 72,5%, PowerPoint 68,1%, Acrobat 65,9%, Photoshop 65,2%, formule de calcul 96%.
- Ultima sesiune (6 pași): Slides — gruparea obiectelor (Ctrl+G), care se păstrează și în .pptx, grupul se mărește din colțuri,
  ghidaje care se trag cu mouse-ul (obiectele se lipesc de ele, păstrate în .pptx), riglă în centimetri;
  Imagini — GIF animat din straturi (fiecare strat un cadru).

## Urmează
- Restul funcțiilor din etapa 2 (Slides: mai multe animații pe același obiect, taburi pe riglă; PDF: editarea textului
  existent, marcaj de timp la semnare; Docs: secțiuni, mai multe pagini alăturate).
- Etapa 3, calitate: viteză, stabilitate, memorie pe 8 GB, teste automate pentru fiecare modul.
- Etapa 5: pachet de instalare pentru Windows și testare cu colegii lui Adrian, cu formular de raportare.

## Ce oferă proiectul celorlalți
- Aplicațiile de birou pentru modulul Cyberspace (Kronos) și pentru setul de aplicații al Cyber Universe (după testarea umană).
- Fiecare aplicație e separată (`src/<modul>/`) și are `module.toml` după `standarde/modul-v0.md`.
- Motorul de formule (~500 de funcții, cu nume românești) și verificarea erorilor din formule, analizele „ce-ar fi dacă”,
  criptarea și formularele PDF, semnarea și verificarea semnăturilor PDF (CMS, .pfx), verificarea PDF/A, compararea PDF-urilor,
  graficele desenate ca SVG, citările și bibliografia, îmbinarea de corespondență, cititorul EXIF, filtrele de imagine,
  cititorii și scriitorii .rtf / .txt / .ods / .gif animat, importul/exportul .docx/.xlsx/.pptx/.pdf/.odt/.psd pot fi refolosite.

## De ce are nevoie de la ceilalți
- Nimic acum.

## Blocaje / nevoie de Adrian
- Întrebare (nu blochează): marcajul de timp la semnarea PDF are nevoie de un server de timp pe internet (se trimite doar amprenta
  documentului, nu documentul). Îl adăugăm ca opțiune, cu un server ales de Adrian? Până atunci semnăturile au ora calculatorului.
- Codul e doar local, pe laptop; pus pe GitHub doar dacă Adrian decide.
