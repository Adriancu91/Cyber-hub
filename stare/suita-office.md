# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-21 07:23 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- O singură aplicație desktop (Electron + React + TypeScript), scrisă de la zero, totul local, fără cont și fără internet:
  Docs, Sheets, PDF, Slides, Imagini, Video, Notițe. Interfața e în română.
- Etapa 1 (compatibilitate) e gata: 529 de fișiere reale de test, 0 erori la deschidere (verificat din nou azi, la 07:21).
- Etapa 2 (toate funcțiile) e în lucru. Scoruri față de aplicațiile de referință: Clipchamp 74,8%, Word 74,1%, Notițe 73,6%,
  Excel 72,1%, PowerPoint 66,8%, Photoshop 64,0%, Acrobat 63,5%, formule de calcul 96%.
- Ultima sesiune (10 pași): Docs — la Îmbinarea de corespondență, lista destinatarilor (filtru, ordonare, bife), „Bloc de adresă”
  și „Formulă de salut”; Slides — stiluri de fundal și prezentarea doar a slide-urilor de la … la …; PDF — verificare PDF/A
  (e bun pentru arhivare?) și rezumatul diferențelor la comparare; Imagini — radieră de fundal; Sheets — tabelul pivot arată
  și procente; Notițe — reluarea desenului linie cu linie; Video — 15 filtre de culoare.

## Urmează
- Restul funcțiilor din etapa 2 (PDF: editarea textului existent, verificarea criptografică a semnăturilor;
  Docs: secțiuni; Slides: mai multe animații pe același obiect).
- Etapa 3, calitate: viteză, stabilitate, memorie pe 8 GB, teste automate pentru fiecare modul.
- Etapa 5: pachet de instalare pentru Windows și testare cu colegii lui Adrian, cu formular de raportare.

## Ce oferă proiectul celorlalți
- Aplicațiile de birou pentru modulul Cyberspace (Kronos) și pentru setul de aplicații al Cyber Universe (după testarea umană).
- Fiecare aplicație e separată (`src/<modul>/`) și are `module.toml` după `standarde/modul-v0.md`.
- Motorul de formule (~500 de funcții, cu nume românești), analizele „ce-ar fi dacă”, criptarea și formularele PDF, cititorul
  de semnături PDF, verificarea PDF/A, compararea PDF-urilor (vizuală și pe text, cu rezumat), graficele desenate ca SVG,
  citările și bibliografia, îmbinarea de corespondență, cititorul EXIF, filtrele de imagine, cititorii și scriitorii
  .rtf / .txt / .ods / .gif animat, importul/exportul .docx/.xlsx/.pptx/.pdf/.odt/.psd pot fi refolosite.

## De ce are nevoie de la ceilalți
- Nimic acum.

## Blocaje / nevoie de Adrian
- Niciunul. Codul e doar local, pe laptop; pus pe GitHub doar dacă Adrian decide.
