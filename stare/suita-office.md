# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-21 02:07 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- O singură aplicație desktop (Electron + React + TypeScript), scrisă de la zero, totul local, fără cont și fără internet:
  Docs, Sheets, PDF, Slides, Imagini, Video, Notițe. Interfața e în română.
- Etapa 1 (compatibilitate) e gata: 529 de fișiere reale de test, 0 erori la deschidere (verificat din nou azi).
- Etapa 2 (toate funcțiile) e în lucru. Scoruri față de aplicațiile de referință: Clipchamp 74%, Notițe 70,5%, Word 69,4%,
  Excel 69,1%, PowerPoint 64,7%, Acrobat 61,3%, Photoshop 59%, formule de calcul 96%.
- Ultima sesiune (9 pași): PDF — adunarea răspunsurilor din mai multe formulare într-un tabel, măsurare (distanță, perimetru, arie, cu scară
  și calibrare), „Ce ocupă loc?” în fișier, semne de tipar pentru tipografie; Imagini — tipărire, histogramă, poze recente,
  informații EXIF (aparat, dată, GPS), export rapid ca PNG.

## Urmează
- Restul funcțiilor din etapa 2 (PDF: găsește și înlocuiește; Imagini: transformarea selecției; Slides: zoom de slide; Docs: index alfabetic).
- Etapa 3, calitate: viteză, stabilitate, memorie pe 8 GB, teste automate pentru fiecare modul.
- Etapa 5: pachet de instalare pentru Windows și testare cu colegii lui Adrian, cu formular de raportare.

## Ce oferă proiectul celorlalți
- Aplicațiile de birou pentru modulul Cyberspace (Kronos) și pentru setul de aplicații al Cyber Universe (după testarea umană).
- Fiecare aplicație e separată (`src/<modul>/`) și are `module.toml` după `standarde/modul-v0.md`.
- Motorul de formule (~500 de funcții, cu nume românești), analizele „ce-ar fi dacă”, criptarea și formularele PDF, cititorul EXIF
  scris de noi, măsurătorile pe planuri PDF, cititorii și scriitorii .rtf / .txt / .ods / .gif animat, importul/exportul
  .docx/.xlsx/.pptx/.pdf/.odt/.psd pot fi refolosite.

## De ce are nevoie de la ceilalți
- Nimic acum.

## Blocaje / nevoie de Adrian
- Niciunul. Codul e doar local, pe laptop; pus pe GitHub doar dacă Adrian decide.
