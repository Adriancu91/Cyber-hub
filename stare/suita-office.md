# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-20 19:47 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- O singură aplicație desktop (Electron + React + TypeScript), scrisă de la zero, totul local, fără cont și fără internet:
  Docs, Sheets, PDF, Slides, Imagini, Video, Notițe. Interfața e în română.
- Etapa 1 (compatibilitate) e gata: 529 de fișiere reale de test, 0 erori la deschidere.
- Etapa 2 (toate funcțiile) e în lucru. Scoruri față de aplicațiile de referință: Notițe 70%, Excel 66%, Clipchamp 66%,
  Word 65%, PowerPoint 63%, Acrobat 58%, Photoshop 55%, formule de calcul 96%.
- Ultima sesiune (7 pași): Notițe: mărimea și fontul textului, fontul întregii notițe, alinierea rândurilor (Ctrl+L/E/R/J);
  PDF: proprietățile câmpurilor de formular (nume, indiciu, obligatoriu, font, culori, chenar) și ordinea Tab;
  Slides: set de culori propriu; Docs: stilurile de tabel; Imagini: Potrivește culoarea (din altă poză) și Umplere la stilurile de strat.

## Urmează
- Restul funcțiilor din etapa 2 (Imagini: umplere după conținut; Video: imagine în imagine; Docs: casete de text; PDF: butoane cu acțiuni).
- Etapa 3, calitate: viteză, stabilitate, memorie pe 8 GB, teste automate pentru fiecare modul.
- Etapa 5: pachet de instalare pentru Windows și testare cu colegii lui Adrian, cu formular de raportare.

## Ce oferă proiectul celorlalți
- Aplicațiile de birou pentru modulul Cyberspace (Kronos) și pentru setul de aplicații al Cyber Universe (după testarea umană).
- Fiecare aplicație e separată (`src/<modul>/`) și are `module.toml` după `standarde/modul-v0.md`.
- Motorul de formule (~500 de funcții, cu nume românești), formatele de număr, criptarea PDF (AES-256), formularele PDF
  (date .xfdf/.csv, proprietăți, ordinea Tab), transformarea în perspectivă și potrivirea culorilor pozelor,
  importul/exportul .docx/.xlsx/.pptx/.pdf/.odt/.psd pot fi refolosite.

## De ce are nevoie de la ceilalți
- Nimic acum.

## Blocaje / nevoie de Adrian
- Niciunul. Codul e doar local, pe laptop; pus pe GitHub doar dacă Adrian decide.
