# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-21 00:28 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- O singură aplicație desktop (Electron + React + TypeScript), scrisă de la zero, totul local, fără cont și fără internet:
  Docs, Sheets, PDF, Slides, Imagini, Video, Notițe. Interfața e în română.
- Etapa 1 (compatibilitate) e gata: 529 de fișiere reale de test, 0 erori la deschidere.
- Etapa 2 (toate funcțiile) e în lucru. Scoruri față de aplicațiile de referință: Clipchamp 74%, Notițe 70%, Word 68,7%,
  Excel 68,4%, PowerPoint 64,3%, Acrobat 58,1%, Photoshop 57,6%, formule de calcul 96%.
- Ultima sesiune (9 pași): Sheets — Tabel de date (What-If) și Manager de scenarii (cu rezumat pe foaie nouă, și în .xlsx);
  Slides — direcția animațiilor și animația pe paragrafe (și în .pptx); Imagini — Deformare (Warp) cu grilă și 8 forme gata;
  Docs și PDF — salvare ca .rtf; Docs — deschiderea fișierelor .rtf.

## Urmează
- Restul funcțiilor din etapa 2 (Docs: deschiderea .txt; PDF: poster pe mai multe foi; Notițe: formatarea textului).
- Etapa 3, calitate: viteză, stabilitate, memorie pe 8 GB, teste automate pentru fiecare modul.
- Etapa 5: pachet de instalare pentru Windows și testare cu colegii lui Adrian, cu formular de raportare.

## Ce oferă proiectul celorlalți
- Aplicațiile de birou pentru modulul Cyberspace (Kronos) și pentru setul de aplicații al Cyber Universe (după testarea umană).
- Fiecare aplicație e separată (`src/<modul>/`) și are `module.toml` după `standarde/modul-v0.md`.
- Motorul de formule (~500 de funcții, cu nume românești), analizele „ce-ar fi dacă” (căutare rezultat, tabel de date, scenarii),
  criptarea PDF (AES-256), formularele PDF, deformarea și lichefierea pozelor, traseele Bézier, cititorul și scriitorul .rtf,
  importul/exportul .docx/.xlsx/.pptx/.pdf/.odt/.psd pot fi refolosite.

## De ce are nevoie de la ceilalți
- Nimic acum.

## Blocaje / nevoie de Adrian
- Niciunul. Codul e doar local, pe laptop; pus pe GitHub doar dacă Adrian decide.
