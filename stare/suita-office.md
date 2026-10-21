# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-21 05:54 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- O singură aplicație desktop (Electron + React + TypeScript), scrisă de la zero, totul local, fără cont și fără internet:
  Docs, Sheets, PDF, Slides, Imagini, Video, Notițe. Interfața e în română.
- Etapa 1 (compatibilitate) e gata: 529 de fișiere reale de test, 0 erori la deschidere (verificat din nou azi, la 05:53).
- Etapa 2 (toate funcțiile) e în lucru. Scoruri față de aplicațiile de referință: Clipchamp 74%, Notițe 73,2%, Word 72,6%,
  Excel 71,6%, PowerPoint 66,3%, Photoshop 63,4%, Acrobat 62,9%, formule de calcul 96%.
- Ultima sesiune (9 pași): Docs — citări și bibliografie (APA, MLA, ISO 690); Sheets — hartă de suprafețe, vederea paginilor
  la tipărire, grafice recomandate; Slides — marker și culori în prezentare (desenele se pot păstra), durata tranziției în secunde;
  PDF — rezumatul comentariilor ca PDF; Imagini — Reselectează, grila de decupare; Notițe — anulare pentru tot caietul.

## Urmează
- Restul funcțiilor din etapa 2 (PDF: editarea adevărată a textului existent; Docs: secțiuni și citirea numerotărilor din .docx; grafic „soare” și bursier).
- Etapa 3, calitate: viteză, stabilitate, memorie pe 8 GB, teste automate pentru fiecare modul.
- Etapa 5: pachet de instalare pentru Windows și testare cu colegii lui Adrian, cu formular de raportare.

## Ce oferă proiectul celorlalți
- Aplicațiile de birou pentru modulul Cyberspace (Kronos) și pentru setul de aplicații al Cyber Universe (după testarea umană).
- Fiecare aplicație e separată (`src/<modul>/`) și are `module.toml` după `standarde/modul-v0.md`.
- Motorul de formule (~500 de funcții, cu nume românești), analizele „ce-ar fi dacă”, criptarea și formularele PDF, compararea
  vizuală a PDF-urilor, graficele desenate ca SVG (inclusiv statistice, cascadă, pâlnie, hartă de suprafețe), citările și bibliografia,
  cititorul EXIF, cititorii și scriitorii .rtf / .txt / .ods / .gif animat, importul/exportul .docx/.xlsx/.pptx/.pdf/.odt/.psd pot fi refolosite.

## De ce are nevoie de la ceilalți
- Nimic acum.

## Blocaje / nevoie de Adrian
- Niciunul. Codul e doar local, pe laptop; pus pe GitHub doar dacă Adrian decide.
