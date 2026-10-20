# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-20 12:40 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- O singură aplicație desktop (Electron + React + TypeScript), scrisă de la zero, totul local, fără cont și fără internet:
  Docs, Sheets, PDF, Slides, Imagini, Video, Notițe. Interfața e în română.
- Etapa 1 (compatibilitate) e gata: 529 de fișiere reale de test, 0 erori la deschidere.
- Etapa 2 (toate funcțiile) e în lucru. Scoruri față de aplicațiile de referință: Word 60%, Excel 60%, PowerPoint 60%,
  Clipchamp 63%, Photoshop 52%, formule de calcul 93%.
- Ultima sesiune (9 pași): Docs: tasta Tab și opririle de tabulator, pagina de gardă, etichete, plicuri;
  Sheets: text „literă sub literă”, evidențiere cu formulă, încercuirea datelor nevalide; Imagini: stilurile Satin și Model peste.

## Urmează
- Restul funcțiilor din etapa 2 (Sheets: filtrul după culoare; Docs: opririle de tabulator pe riglă; Imagini: conturul pe margine).
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
