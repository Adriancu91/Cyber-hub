# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-21 08:10 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- O singură aplicație desktop (Electron + React + TypeScript), scrisă de la zero, totul local, fără cont și fără internet:
  Docs, Sheets, PDF, Slides, Imagini, Video, Notițe. Interfața e în română.
- Etapa 1 (compatibilitate) e gata: 529 de fișiere reale de test, 0 erori la deschidere (verificat din nou azi, la 08:09).
- Etapa 2 (toate funcțiile) e în lucru. Scoruri față de aplicațiile de referință: Clipchamp 75,6%, Word 74,3%, Notițe 74,0%,
  Excel 72,5%, PowerPoint 67,2%, Photoshop 64,6%, Acrobat 64,3%, formule de calcul 96%.
- Ultima sesiune (10 pași): Imagini — 5 filtre noi (estompare pe câmp, extrudare, stropire, hașurare, margini accentuate);
  PDF — câmp de semnătură gol, casetele paginii pentru tipografie, inițiale pe fiecare pagină; Slides — album foto și comenzile
  în paleta Ctrl+K; Sheets — verificarea erorilor și referințele circulare; Notițe — Tab retrage orice paragraf;
  Docs / Sheets / Notițe — glisor de zoom („O pagină” în Docs); Video — glisorul Expunere.

## Urmează
- Restul funcțiilor din etapa 2 (PDF: semnarea cu certificat în câmpul de semnătură, editarea textului existent;
  Docs: secțiuni, mai multe pagini alăturate; Slides: mai multe animații pe același obiect).
- Etapa 3, calitate: viteză, stabilitate, memorie pe 8 GB, teste automate pentru fiecare modul.
- Etapa 5: pachet de instalare pentru Windows și testare cu colegii lui Adrian, cu formular de raportare.

## Ce oferă proiectul celorlalți
- Aplicațiile de birou pentru modulul Cyberspace (Kronos) și pentru setul de aplicații al Cyber Universe (după testarea umană).
- Fiecare aplicație e separată (`src/<modul>/`) și are `module.toml` după `standarde/modul-v0.md`.
- Motorul de formule (~500 de funcții, cu nume românești) și verificarea erorilor din formule, analizele „ce-ar fi dacă”,
  criptarea și formularele PDF (inclusiv câmpuri de semnătură), cititorul de semnături PDF, verificarea PDF/A, compararea
  PDF-urilor, graficele desenate ca SVG, citările și bibliografia, îmbinarea de corespondență, cititorul EXIF, filtrele de imagine,
  cititorii și scriitorii .rtf / .txt / .ods / .gif animat, importul/exportul .docx/.xlsx/.pptx/.pdf/.odt/.psd pot fi refolosite.

## De ce are nevoie de la ceilalți
- Nimic acum.

## Blocaje / nevoie de Adrian
- Niciunul. Codul e doar local, pe laptop; pus pe GitHub doar dacă Adrian decide.
