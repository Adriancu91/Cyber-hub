# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-20 18:12 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- O singură aplicație desktop (Electron + React + TypeScript), scrisă de la zero, totul local, fără cont și fără internet:
  Docs, Sheets, PDF, Slides, Imagini, Video, Notițe. Interfața e în română.
- Etapa 1 (compatibilitate) e gata: 529 de fișiere reale de test, 0 erori la deschidere.
- Etapa 2 (toate funcțiile) e în lucru. Scoruri față de aplicațiile de referință: Word 64%, Excel 66%, PowerPoint 63%,
  Clipchamp 66%, Acrobat 57%, Photoshop 53%, Notițe 69%, formule de calcul 96%.
- Ultima sesiune (10 pași): Sheets: Umplere rapidă (Ctrl+E), urmărirea formulelor, sfârșit de pagină (și în .xlsx), fereastra Urmărire valori;
  Notițe: culori de text și evidențiere, verificarea accesibilității; Docs: efecte de text (contur, umbră, relief, gravat, cu .docx/.odt);
  Imagini: selecțiile salvate intră în .psd; Slides: înregistrare de sunet pe slide; PDF: lista fonturilor folosite.

## Urmează
- Restul funcțiilor din etapa 2 (Notițe: tabele în câmpul de scris; Imagini: panoul Canale; Sheets: săgeți la urmărirea formulelor).
- Etapa 3, calitate: viteză, stabilitate, memorie pe 8 GB, teste automate pentru fiecare modul.
- Etapa 5: pachet de instalare pentru Windows și testare cu colegii lui Adrian, cu formular de raportare.

## Ce oferă proiectul celorlalți
- Aplicațiile de birou pentru modulul Cyberspace (Kronos) și pentru setul de aplicații al Cyber Universe (după testarea umană).
- Fiecare aplicație e separată (`src/<modul>/`) și are `module.toml` după `standarde/modul-v0.md`.
- Motorul de formule (~500 de funcții, cu nume românești), motorul de formate de număr, criptarea PDF (AES-256, cu permisiuni),
  „Umplerea rapidă” din exemple și importul/exportul .docx/.xlsx/.pptx/.pdf/.odt/.psd pot fi refolosite.

## De ce are nevoie de la ceilalți
- Nimic acum.

## Blocaje / nevoie de Adrian
- Niciunul. Codul e doar local, pe laptop; pus pe GitHub doar dacă Adrian decide.
