# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-21 02:53 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- O singură aplicație desktop (Electron + React + TypeScript), scrisă de la zero, totul local, fără cont și fără internet:
  Docs, Sheets, PDF, Slides, Imagini, Video, Notițe. Interfața e în română.
- Etapa 1 (compatibilitate) e gata: 529 de fișiere reale de test, 0 erori la deschidere (verificat din nou azi, la 02:50).
- Etapa 2 (toate funcțiile) e în lucru. Scoruri față de aplicațiile de referință: Clipchamp 74%, Notițe 70,5%, Word 69,4%,
  Excel 69,1%, PowerPoint 64,7%, Acrobat 61,7%, Photoshop 60,9%, formule de calcul 96%.
- Ultima sesiune (8 pași): Imagini — rigle și ghidaje, transformarea selecției, navigator (miniatura pozei), copiere / tăiere / lipire
  specială (în același loc, în selecție), forme noi (stea, inimă, bulă de dialog), straturi legate, înregistrarea măsurătorilor;
  PDF — formatul și validarea câmpurilor de formular (număr, procent, dată, interval min–max, verificate la completare).

## Urmează
- Restul funcțiilor din etapa 2 (Imagini: rotirea vederii, paleta de culori; PDF: găsește și înlocuiește; Slides: zoom de slide; Docs: index alfabetic).
- Etapa 3, calitate: viteză, stabilitate, memorie pe 8 GB, teste automate pentru fiecare modul.
- Etapa 5: pachet de instalare pentru Windows și testare cu colegii lui Adrian, cu formular de raportare.

## Ce oferă proiectul celorlalți
- Aplicațiile de birou pentru modulul Cyberspace (Kronos) și pentru setul de aplicații al Cyber Universe (după testarea umană).
- Fiecare aplicație e separată (`src/<modul>/`) și are `module.toml` după `standarde/modul-v0.md`.
- Motorul de formule (~500 de funcții, cu nume românești), analizele „ce-ar fi dacă”, criptarea și formularele PDF (cu validarea câmpurilor),
  cititorul EXIF scris de noi, măsurătorile pe planuri PDF, cititorii și scriitorii .rtf / .txt / .ods / .gif animat,
  importul/exportul .docx/.xlsx/.pptx/.pdf/.odt/.psd pot fi refolosite.

## De ce are nevoie de la ceilalți
- Nimic acum.

## Blocaje / nevoie de Adrian
- Niciunul. Codul e doar local, pe laptop; pus pe GitHub doar dacă Adrian decide.
