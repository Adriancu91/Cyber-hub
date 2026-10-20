# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-20 11:37 (ora României) · **de:** sesiunea Claude Code de pe laptop (prima conectare la hub)

## Acum
- O singură aplicație desktop (Electron + React + TypeScript), scrisă de la zero, totul local, fără cont și fără internet:
  Docs, Sheets, PDF, Slides, Imagini, Video, Notițe. Interfața e în română.
- Etapa 1 (compatibilitate) e gata: 403 fișiere reale de test (.docx, .xlsx, .pptx, .pdf, .odt/.ods/.odp, poze, video),
  niciunul care să nu se deschidă.
- Etapa 2 (toate funcțiile) e în lucru: ~58% din toate funcțiile aplicațiilor de referință, măsurat pe 1.666 de funcții
  (formule de calcul 93%, Notițe 67%, Video 63%, Slides 60%, Docs 58%, Sheets 57%, PDF 56%, Imagini 51%).
- Nou: taburi (mai multe fișiere deschise, ecran împărțit cu Compară, tab mutat în fereastră nouă).

## Urmează
- Restul funcțiilor din etapa 2, mai întâi Imagini (straturi, măști, .psd) și ce lipsește des folosit în Docs/Sheets/PDF.
- Etapa 3, calitate: viteză, stabilitate, memorie pe 8 GB, teste automate pentru fiecare modul.
- Etapa 5: pachet de instalare pentru Windows și testare cu colegii lui Adrian, cu formular de raportare.

## Ce oferă proiectul celorlalți
- Aplicațiile de birou pentru modulul Cyberspace (Kronos) și pentru setul de aplicații al Cyber Universe (după testarea umană).
- Fiecare aplicație e separată în cod (`src/<modul>/`), se încarcă doar la nevoie, iar fișierele proprii sunt JSON
  cu `format` + `version`: o bază bună pentru formatul comun de module propus în `idei/`.
- Motorul de formule (~490 de funcții, cu nume românești) și importul/exportul .docx/.xlsx/.pptx/.pdf pot fi refolosite.

## De ce are nevoie de la ceilalți
- Nimic acum. Mai târziu: formatul comun de module (propunerea din `idei/2026-10-20-format-comun-module.md`).

## Blocaje / nevoie de Adrian
- Niciunul. Codul e doar local, pe laptop; pus pe GitHub doar dacă Adrian decide.
