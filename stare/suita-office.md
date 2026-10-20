# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-20 14:16 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- O singură aplicație desktop (Electron + React + TypeScript), scrisă de la zero, totul local, fără cont și fără internet:
  Docs, Sheets, PDF, Slides, Imagini, Video, Notițe. Interfața e în română.
- Etapa 1 (compatibilitate) e gata: 529 de fișiere reale de test, 0 erori la deschidere.
- Etapa 2 (toate funcțiile) e în lucru. Scoruri față de aplicațiile de referință: Word 62%, Excel 64%, PowerPoint 60%,
  Clipchamp 63%, Photoshop 52%, formule de calcul 93%.
- Ultima sesiune (11 pași): Imagini: selecția rapidă și lasoul magnetic; Sheets: Mergi la special, calcul manual / automat,
  calcul iterativ (referințe circulare), toate notele la vedere, zoom pe selecție; Docs: vizualizarea Ciornă, afișarea și filtrarea
  modificărilor urmărite, blocarea urmăririi (și în .docx).

## Urmează
- Restul funcțiilor din etapa 2 (Docs: urmărirea modificărilor de formatare, stiluri proprii; Sheets: grafice noi; Imagini: Top 10 lipsă).
- Etapa 3, calitate: viteză, stabilitate, memorie pe 8 GB, teste automate pentru fiecare modul.
- Etapa 5: pachet de instalare pentru Windows și testare cu colegii lui Adrian, cu formular de raportare.

## Ce oferă proiectul celorlalți
- Aplicațiile de birou pentru modulul Cyberspace (Kronos) și pentru setul de aplicații al Cyber Universe (după testarea umană).
- Fiecare aplicație e separată în cod (`src/<modul>/`), se încarcă doar la nevoie, iar fișierele proprii sunt JSON
  cu `format` + `version`: o bază bună pentru formatul comun de module propus în `idei/`.
- Motorul de formule (~490 de funcții, cu nume românești) și importul/exportul .docx/.xlsx/.pptx/.pdf/.odt pot fi refolosite.

## De ce are nevoie de la ceilalți
- Nimic acum. Mai târziu: formatul comun de module (propunerea din `idei/2026-10-20-format-comun-module.md`).

## Blocaje / nevoie de Adrian
- Niciunul. Codul e doar local, pe laptop; pus pe GitHub doar dacă Adrian decide.
