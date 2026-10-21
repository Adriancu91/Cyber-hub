# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-21 04:26 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- O singură aplicație desktop (Electron + React + TypeScript), scrisă de la zero, totul local, fără cont și fără internet:
  Docs, Sheets, PDF, Slides, Imagini, Video, Notițe. Interfața e în română.
- Etapa 1 (compatibilitate) e gata: 529 de fișiere reale de test, 0 erori la deschidere (verificat din nou azi, la 04:25).
- Etapa 2 (toate funcțiile) e în lucru. Scoruri față de aplicațiile de referință: Clipchamp 74%, Notițe 72%, Word 70,7%,
  Excel 70,4%, PowerPoint 65%, Acrobat 62,5%, Photoshop 62,5%, formule de calcul 96%.
- Ultima sesiune (8 pași): PDF — găsește și înlocuiește (Ctrl+H), comparare vizuală a două PDF-uri;
  Sheets — grafic combinat (și cu a doua axă), histogramă, Pareto, cutie cu mustăți; Slides — toate tipurile de grafice,
  culori și titlurile axelor (și în .pptx); Imagini — 3 filtre noi; Docs — câmpuri în antet (data, fișierul, autorul, titlul).

## Urmează
- Restul funcțiilor din etapa 2 (PDF: editarea adevărată a textului existent; Docs: secțiuni; grafice: etichete cu valori).
- Etapa 3, calitate: viteză, stabilitate, memorie pe 8 GB, teste automate pentru fiecare modul.
- Etapa 5: pachet de instalare pentru Windows și testare cu colegii lui Adrian, cu formular de raportare.

## Ce oferă proiectul celorlalți
- Aplicațiile de birou pentru modulul Cyberspace (Kronos) și pentru setul de aplicații al Cyber Universe (după testarea umană).
- Fiecare aplicație e separată (`src/<modul>/`) și are `module.toml` după `standarde/modul-v0.md`.
- Motorul de formule (~500 de funcții, cu nume românești), analizele „ce-ar fi dacă”, criptarea și formularele PDF, compararea
  vizuală a PDF-urilor, graficele desenate ca SVG (inclusiv statistice: histogramă, Pareto, cutie cu mustăți), cititorul EXIF,
  cititorii și scriitorii .rtf / .txt / .ods / .gif animat, importul/exportul .docx/.xlsx/.pptx/.pdf/.odt/.psd pot fi refolosite.

## De ce are nevoie de la ceilalți
- Nimic acum.

## Blocaje / nevoie de Adrian
- Niciunul. Codul e doar local, pe laptop; pus pe GitHub doar dacă Adrian decide.
