# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-27 00:38 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- Lucrul continuu merge pe plusurile alese de Adrian (P1–P4), înaintea funcțiilor care lipsesc. P1 (diacritice) și **P2 (e-Factura) sunt gata**; P3 e în lucru.
- Sesiunea de noapte (23:57–00:38), 4 commituri, testele trec:
  - **Facturi în altă monedă** (EUR, USD, GBP, CHF…): pe foaia Factură se alege moneda și se scrie cursul BNR; XML-ul declară TVA-ul și în lei, cum cer regulile; suma în litere e în moneda facturii („… de euro și cincizeci de eurocenți”).
  - **Import e-Factura (XML)** în Sheets: o factură primită (XML sau ZIP din SPV) se deschide ca foaie Factură completată, de corectat și refolosit; ce nu încape pe foaie (cote vechi, reduceri, avans) se spune într-o fereastră.
  - **Extrasul de cont → tabel** (P3): Fișier → Import extras de cont, din .csv, .xlsx, .xls sau .ods. Iese foaia Extras (data, descriere, încasări, plăți, sold, categorie) și foaia Rezumat pe luni și categorii, cu formule. Coloanele, datele și sumele se recunosc singure, oricum le scrie banca.
- O singură aplicație desktop (Electron + React + TypeScript), de la zero, totul local: Docs, Sheets, PDF, Slides, Imagini, Video, Notițe, în română sau engleză.
- Scoruri: Word 81,7%, Excel 81,1%, PowerPoint 80,6%, Clipchamp 79,4%, Notițe 76,4%, Acrobat 74,0%, Photoshop 72,8%, formule 97,1%.

## Urmează
- P3: extrasul ca PDF și regulile de categorii editabile; apoi P4 (semnături digitale, inclusiv certificate calificate pe token).
- Apoi ținta „funcțiile care lipsesc” (Slides: coordonatoarele; PDF: fontul / culoarea textului existent; Sheets: formatarea graficului).

## Ce oferă proiectul celorlalți
- Nimic nou acum. Mai târziu (după testarea de către oameni): motorul de calcul, citirea documentelor (PDF / .docx → text) și motorul de diacritice românești.

## De ce are nevoie de la ceilalți
- Nimic.

## Blocaje / nevoie de Adrian
- Să încerce o factură reală: Sheets → Șabloane → Factură (e-Factura) → Export e-Factura (XML), apoi încărcarea în SPV (validarea oficială n-o putem face noi).
- Dacă vrea: un extras de cont real (.csv / .xlsx / PDF), ca să-l punem anonimizat în colecția de test.
- Când vrea kitul 0.9.3 (are licența nouă, în engleză, și plusurile de azi).
- Dacă suita se va vinde: o verificare juridică a licenței.
