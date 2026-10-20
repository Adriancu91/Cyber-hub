# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-20 21:21 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- O singură aplicație desktop (Electron + React + TypeScript), scrisă de la zero, totul local, fără cont și fără internet:
  Docs, Sheets, PDF, Slides, Imagini, Video, Notițe. Interfața e în română.
- Etapa 1 (compatibilitate) e gata: 529 de fișiere reale de test, 0 erori la deschidere.
- Etapa 2 (toate funcțiile) e în lucru. Scoruri față de aplicațiile de referință: Clipchamp 73%, Notițe 70%, Excel 66%,
  Word 67%, PowerPoint 63%, Acrobat 58%, Photoshop 55%, formule de calcul 96%.
- Ultima sesiune (6 pași, toți în Docs): casete de text (și citite/scrise în .docx), 15 forme recolorabile, rotirea și oglindirea imaginilor,
  decuparea imaginilor, stiluri de poză (ramă, umbră, colțuri rotunjite, oval), text artistic.

## Urmează
- Restul funcțiilor din etapa 2 (Imagini: umplere după conținut; Docs: aducere în față / trimitere în spate; PDF: butoane cu acțiuni; Video: tragerea pozelor în bandă).
- Etapa 3, calitate: viteză, stabilitate, memorie pe 8 GB, teste automate pentru fiecare modul.
- Etapa 5: pachet de instalare pentru Windows și testare cu colegii lui Adrian, cu formular de raportare.

## Ce oferă proiectul celorlalți
- Aplicațiile de birou pentru modulul Cyberspace (Kronos) și pentru setul de aplicații al Cyber Universe (după testarea umană).
- Fiecare aplicație e separată (`src/<modul>/`) și are `module.toml` după `standarde/modul-v0.md`.
- Motorul de formule (~500 de funcții, cu nume românești), formatele de număr, criptarea PDF (AES-256), formularele PDF,
  transformarea în perspectivă, potrivirea culorilor, cheia de culoare (ecran verde) pentru video,
  importul/exportul .docx/.xlsx/.pptx/.pdf/.odt/.psd pot fi refolosite.

## De ce are nevoie de la ceilalți
- Nimic acum.

## Blocaje / nevoie de Adrian
- Niciunul. Codul e doar local, pe laptop; pus pe GitHub doar dacă Adrian decide.
