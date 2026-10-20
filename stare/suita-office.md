# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-20 22:05 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- O singură aplicație desktop (Electron + React + TypeScript), scrisă de la zero, totul local, fără cont și fără internet:
  Docs, Sheets, PDF, Slides, Imagini, Video, Notițe. Interfața e în română.
- Etapa 1 (compatibilitate) e gata: 529 de fișiere reale de test, 0 erori la deschidere.
- Etapa 2 (toate funcțiile) e în lucru. Scoruri față de aplicațiile de referință: Clipchamp 74%, Notițe 70%, Word 68%,
  Excel 66%, PowerPoint 63%, Acrobat 58%, Photoshop 56%, formule de calcul 96%.
- Ultima sesiune (7 pași): Docs (imagini în fața / în spatele textului cu ordinea lor, grafice, diagrame),
  Imagini (umplere după conținut, mutare după conținut), Video (tragerea pozelor în bandă, mai multe poze alese deodată).

## Urmează
- Restul funcțiilor din etapa 2 (Docs: ecuații simple; Sheets / Slides: ce lipsește des folosit; Video: blocarea / ascunderea pistelor).
- Etapa 3, calitate: viteză, stabilitate, memorie pe 8 GB, teste automate pentru fiecare modul.
- Etapa 5: pachet de instalare pentru Windows și testare cu colegii lui Adrian, cu formular de raportare.

## Ce oferă proiectul celorlalți
- Aplicațiile de birou pentru modulul Cyberspace (Kronos) și pentru setul de aplicații al Cyber Universe (după testarea umană).
- Fiecare aplicație e separată (`src/<modul>/`) și are `module.toml` după `standarde/modul-v0.md`.
- Motorul de formule (~500 de funcții, cu nume românești), formatele de număr, criptarea PDF (AES-256), formularele PDF,
  umplerea după conținut (scoaterea obiectelor din poze), transformarea în perspectivă, cheia de culoare pentru video,
  importul/exportul .docx/.xlsx/.pptx/.pdf/.odt/.psd pot fi refolosite.

## De ce are nevoie de la ceilalți
- Nimic acum.

## Blocaje / nevoie de Adrian
- Niciunul. Codul e doar local, pe laptop; pus pe GitHub doar dacă Adrian decide.
