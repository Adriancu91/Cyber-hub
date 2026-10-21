# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-21 03:35 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- O singură aplicație desktop (Electron + React + TypeScript), scrisă de la zero, totul local, fără cont și fără internet:
  Docs, Sheets, PDF, Slides, Imagini, Video, Notițe. Interfața e în română.
- Etapa 1 (compatibilitate) e gata: 529 de fișiere reale de test, 0 erori la deschidere (verificat din nou azi, la 03:33).
- Etapa 2 (toate funcțiile) e în lucru. Scoruri față de aplicațiile de referință: Clipchamp 74%, Notițe 72%, Word 70,5%,
  Excel 69,6%, PowerPoint 64,8%, Acrobat 61,9%, Photoshop 61,6%, formule de calcul 96%.
- Ultima sesiune (10 pași): Imagini — mostre de culoare, rotirea vederii; Slides — zoom de slide (miniatură cu salt și revenire);
  Docs — index alfabetic, liniile tabelului (fel, culoare, care linii); Notițe — lasou în desen, desen → forme;
  PDF — câmpuri de formular găsite singure; Sheets — titlurile axelor și paletele de culori la grafice (și în .xlsx).

## Urmează
- Restul funcțiilor din etapa 2 (PDF: găsește și înlocuiește; Docs: secțiuni; Sheets: grafic combinat; paletele și în Slides).
- Etapa 3, calitate: viteză, stabilitate, memorie pe 8 GB, teste automate pentru fiecare modul.
- Etapa 5: pachet de instalare pentru Windows și testare cu colegii lui Adrian, cu formular de raportare.

## Ce oferă proiectul celorlalți
- Aplicațiile de birou pentru modulul Cyberspace (Kronos) și pentru setul de aplicații al Cyber Universe (după testarea umană).
- Fiecare aplicație e separată (`src/<modul>/`) și are `module.toml` după `standarde/modul-v0.md`.
- Motorul de formule (~500 de funcții, cu nume românești), analizele „ce-ar fi dacă”, criptarea și formularele PDF (cu detectarea
  automată a câmpurilor), cititorul EXIF scris de noi, recunoașterea formelor desenate de mână, desenarea graficelor ca SVG,
  cititorii și scriitorii .rtf / .txt / .ods / .gif animat, importul/exportul .docx/.xlsx/.pptx/.pdf/.odt/.psd pot fi refolosite.

## De ce are nevoie de la ceilalți
- Nimic acum.

## Blocaje / nevoie de Adrian
- Niciunul. Codul e doar local, pe laptop; pus pe GitHub doar dacă Adrian decide.
