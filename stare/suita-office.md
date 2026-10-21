# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-21 05:12 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- O singură aplicație desktop (Electron + React + TypeScript), scrisă de la zero, totul local, fără cont și fără internet:
  Docs, Sheets, PDF, Slides, Imagini, Video, Notițe. Interfața e în română.
- Etapa 1 (compatibilitate) e gata: 529 de fișiere reale de test, 0 erori la deschidere (verificat din nou azi, la 05:11).
- Etapa 2 (toate funcțiile) e în lucru. Scoruri față de aplicațiile de referință: Clipchamp 74%, Notițe 72,8%, Word 71,4%,
  Excel 70,9%, PowerPoint 65,9%, Photoshop 63,1%, Acrobat 62,7%, formule de calcul 96%.
- Ultima sesiune (10 pași): grafice — valori pe grafic, locul legendei, cascadă, pâlnie (și în .xlsx/.pptx); Slides — poze decupate
  în cerc, stea, inimă și la proporție; PDF → prezentare; Imagini — 2 filtre noi; Docs — numerotare 1.1 / 1.1.1, comentarii
  rezolvate, „Mergi la pagina…”, pagină goală; Notițe — paginile unui PDF puse în notiță ca imprimare.

## Urmează
- Restul funcțiilor din etapa 2 (PDF: editarea adevărată a textului existent; Docs: secțiuni și citirea numerotărilor din .docx; grafic bursier).
- Etapa 3, calitate: viteză, stabilitate, memorie pe 8 GB, teste automate pentru fiecare modul.
- Etapa 5: pachet de instalare pentru Windows și testare cu colegii lui Adrian, cu formular de raportare.

## Ce oferă proiectul celorlalți
- Aplicațiile de birou pentru modulul Cyberspace (Kronos) și pentru setul de aplicații al Cyber Universe (după testarea umană).
- Fiecare aplicație e separată (`src/<modul>/`) și are `module.toml` după `standarde/modul-v0.md`.
- Motorul de formule (~500 de funcții, cu nume românești), analizele „ce-ar fi dacă”, criptarea și formularele PDF, compararea
  vizuală a PDF-urilor, graficele desenate ca SVG (inclusiv statistice, cascadă și pâlnie), cititorul EXIF,
  cititorii și scriitorii .rtf / .txt / .ods / .gif animat, importul/exportul .docx/.xlsx/.pptx/.pdf/.odt/.psd pot fi refolosite.

## De ce are nevoie de la ceilalți
- Nimic acum.

## Blocaje / nevoie de Adrian
- Niciunul. Codul e doar local, pe laptop; pus pe GitHub doar dacă Adrian decide.
