# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-21 08:57 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- O singură aplicație desktop (Electron + React + TypeScript), scrisă de la zero, totul local, fără cont și fără internet:
  Docs, Sheets, PDF, Slides, Imagini, Video, Notițe. Interfața e în română.
- Etapa 1 (compatibilitate) e gata: 529 de fișiere reale de test, 0 erori la deschidere (verificat din nou azi, la 08:57).
- Etapa 2 (toate funcțiile) e în lucru. Scoruri față de aplicațiile de referință: Clipchamp 75,6%, Word 74,3%, Notițe 74,0%,
  Excel 72,5%, PowerPoint 67,2%, Acrobat 65,9%, Photoshop 64,9%, formule de calcul 96%.
- Ultima sesiune (7 pași): PDF — semnătura digitală cu certificat (ID digital făcut în Suite, cu parolă, sau certificat
  din .pfx / .p12, cu lanțul), verificarea semnăturilor existente (cele reale din formularele ANAF ies valide), certificarea
  documentului, semnarea prin adăugare (mai mulți semnatari, semnăturile vechi rămân valabile); Imagini — „Extinde după culoare”
  și „Culori similare” la selecții, poligon cu 3–12 laturi. Semnăturile au fost verificate și cu openssl.

## Urmează
- Restul funcțiilor din etapa 2 (PDF: marcaj de timp la semnare, .pfx cu criptarea veche, editarea textului existent;
  Docs: secțiuni, mai multe pagini alăturate; Slides: mai multe animații pe același obiect).
- Etapa 3, calitate: viteză, stabilitate, memorie pe 8 GB, teste automate pentru fiecare modul.
- Etapa 5: pachet de instalare pentru Windows și testare cu colegii lui Adrian, cu formular de raportare.

## Ce oferă proiectul celorlalți
- Aplicațiile de birou pentru modulul Cyberspace (Kronos) și pentru setul de aplicații al Cyber Universe (după testarea umană).
- Fiecare aplicație e separată (`src/<modul>/`) și are `module.toml` după `standarde/modul-v0.md`.
- Motorul de formule (~500 de funcții, cu nume românești) și verificarea erorilor din formule, analizele „ce-ar fi dacă”,
  criptarea și formularele PDF (inclusiv câmpuri de semnătură), cititorul de semnături PDF, verificarea PDF/A, semnarea și verificarea semnăturilor PDF (CMS, .pfx), compararea
  PDF-urilor, graficele desenate ca SVG, citările și bibliografia, îmbinarea de corespondență, cititorul EXIF, filtrele de imagine,
  cititorii și scriitorii .rtf / .txt / .ods / .gif animat, importul/exportul .docx/.xlsx/.pptx/.pdf/.odt/.psd pot fi refolosite.

## De ce are nevoie de la ceilalți
- Nimic acum.

## Blocaje / nevoie de Adrian
- Întrebare (nu blochează): marcajul de timp la semnarea PDF are nevoie de un server de timp pe internet (se trimite doar amprenta
  documentului, nu documentul). Îl adăugăm ca opțiune, cu un server ales de Adrian? Până atunci semnăturile au ora calculatorului.
- Codul e doar local, pe laptop; pus pe GitHub doar dacă Adrian decide.
