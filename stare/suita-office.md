# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-20 16:41 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- O singură aplicație desktop (Electron + React + TypeScript), scrisă de la zero, totul local, fără cont și fără internet:
  Docs, Sheets, PDF, Slides, Imagini, Video, Notițe. Interfața e în română.
- Etapa 1 (compatibilitate) e gata: 529 de fișiere reale de test, 0 erori la deschidere (verificat din nou azi, după schimbări).
- Etapa 2 (toate funcțiile) e în lucru. Scoruri față de aplicațiile de referință: Word 63%, Excel 64%, PowerPoint 62%,
  Clipchamp 66%, Photoshop 53%, formule de calcul 96%.
- Ultima sesiune (9 pași): Video: zoom pe bandă, forma de undă a muzicii; Docs: numere de rând (și în .docx / .odt);
  Slides: fundal în degrade și poză ca fundal (și în .pptx); Sheets: motor propriu pentru formatele de număr (TEXT) și
  „Format particularizat” pe celule, cu formatele din .xlsx păstrate întocmai; `module.toml` în fiecare aplicație.

## Urmează
- Restul funcțiilor din etapa 2 (Sheets: fereastra completă de formatare a celulelor; Docs: panoul Stiluri; Video: unda și la voce).
- Etapa 3, calitate: viteză, stabilitate, memorie pe 8 GB, teste automate pentru fiecare modul.
- Etapa 5: pachet de instalare pentru Windows și testare cu colegii lui Adrian, cu formular de raportare.

## Ce oferă proiectul celorlalți
- Aplicațiile de birou pentru modulul Cyberspace (Kronos) și pentru setul de aplicații al Cyber Universe (după testarea umană).
- Fiecare aplicație e separată (`src/<modul>/`) și are acum `module.toml` după `standarde/modul-v0.md`.
- Motorul de formule (~500 de funcții, cu nume românești), motorul de formate de număr și importul/exportul
  .docx/.xlsx/.pptx/.pdf/.odt pot fi refolosite.

## De ce are nevoie de la ceilalți
- Nimic acum.

## Blocaje / nevoie de Adrian
- Niciunul. Codul e doar local, pe laptop; pus pe GitHub doar dacă Adrian decide.
