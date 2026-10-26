# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-26 23:55 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- Lucrul continuu merge pe plusurile alese de Adrian (P1–P4), înaintea funcțiilor care lipsesc.
- Sesiunea de noapte (23:07–23:55), 4 commituri, testele trec:
  - **P1 gata — Diacritice automate** (Docs, Notițe, Slides: Revizuire › Diacritice): „sedinta de sambata” → „ședința de sâmbătă”; cuvintele cu mai multe forme corecte („fata” / „față”) se arată pentru alegere; un singur pas de anulare. Motor propriu, cu dicționarul românesc al aplicației: 99,5% și 97,9% cuvinte corecte pe două texte de probă (ținta: 97%).
  - **P2, cea mai mare parte — e-Factura din Sheets**: șablonul „Factură (e-Factura)” (TVA pe cote 21 / 11 / 0 / scutit, sumă în litere, număr care crește singur, furnizor ținut minte) și, în Fișier, **Export e-Factura (XML)** (UBL 2.1 / CIUS-RO, verificat local: CUI, județ, sector, IBAN, unități, scutiri) și **Factură PDF** pentru client. Nimic nu pleacă pe internet; XML-ul îl încarcă Adrian în SPV.
- O singură aplicație desktop (Electron + React + TypeScript), de la zero, totul local: Docs, Sheets, PDF, Slides, Imagini, Video, Notițe, în română sau engleză.
- Scoruri: Word 81,7%, Excel 81,1%, PowerPoint 80,6%, Clipchamp 79,4%, Notițe 76,4%, Acrobat 74,0%, Photoshop 72,8%, formule 97,1%.

## Urmează
- P2: facturi în altă monedă și citirea unui XML înapoi în foaie; apoi P3 (extrasul de cont → tabel), P4 (semnături digitale, inclusiv certificate calificate pe token).
- Apoi ținta „funcțiile care lipsesc” (Slides: coordonatoarele; PDF: fontul / culoarea textului existent; Sheets: formatarea graficului).

## Ce oferă proiectul celorlalți
- Nimic nou acum. Mai târziu (după testarea de către oameni): motorul de calcul, citirea documentelor (PDF / .docx → text) și motorul de diacritice românești.

## De ce are nevoie de la ceilalți
- Nimic.

## Blocaje / nevoie de Adrian
- Să încerce o factură reală: Sheets → Șabloane → Factură (e-Factura) → Export e-Factura (XML), apoi încărcarea în SPV (validarea oficială n-o putem face noi).
- Când vrea kitul 0.9.3 (are licența nouă, în engleză, și plusurile de azi).
- Dacă suita se va vinde: o verificare juridică a licenței.
