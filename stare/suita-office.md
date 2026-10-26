# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-27 01:23 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- Lucrul continuu merge pe plusurile alese de Adrian (P1–P4), înaintea funcțiilor care lipsesc. P1 (diacritice), P2 (e-Factura) și **P3 (extrase de cont) sunt gata**; P4 (semnături digitale) e în lucru.
- Sesiunea de noapte (00:36–01:23), 4 commituri, testele trec:
  - **Extrasul de cont și din PDF**: Sheets → Fișier → Import extras de cont citește și PDF-ul băncii (cu text), pe mai multe pagini; antetul băncii, numerele de pagină și notele se sar.
  - **Reguli de categorii editabile**: foaia Reguli (cuvânt → categorie) și Fișier → Aplică regulile de categorii; regulile se țin minte. Cu asta, P3 e gata.
  - **Semnătura cu certificatul de pe calculator sau de pe token / card** (P4): în PDF → 🔏 Semnează digital → „Folosește un certificat de pe calculator sau token…”. PIN-ul îl cere fereastra tokenului; Suite nu-l vede.
  - **Semnătura .p7s pentru orice fișier**: 🔏 Semnează un fișier (.p7s)… (fișierul rămâne neschimbat, semnătura alături).
- O singură aplicație desktop (Electron + React + TypeScript), de la zero, totul local: Docs, Sheets, PDF, Slides, Imagini, Video, Notițe, în română sau engleză.
- Scoruri: Word 81,7%, Excel 81,1%, PowerPoint 80,6%, Clipchamp 79,4%, Notițe 76,4%, Acrobat 74,2%, Photoshop 72,8%, formule 97,1%.

## Urmează
- P4: verificarea unui .p7s / .p7m primit, marca temporală (PAdES B-T), apoi semnătura în .docx / .xlsx / .pptx.
- Apoi ținta „funcțiile care lipsesc” (Slides: coordonatoarele; PDF: fontul / culoarea textului existent; Sheets: formatarea graficului).

## Ce oferă proiectul celorlalți
- Nimic nou acum. Mai târziu (după testarea de către oameni): motorul de calcul, citirea documentelor (PDF / .docx → text) și motorul de diacritice românești.

## De ce are nevoie de la ceilalți
- Nimic.

## Blocaje / nevoie de Adrian
- Să încerce semnarea cu tokenul lui real (n-am avut unul la test): PDF → 🔏 Semnează digital → Folosește un certificat de pe calculator sau token…; dacă apare o eroare, mesajul ne spune ce să reparăm.
- Să încerce o factură reală: Sheets → Șabloane → Factură (e-Factura) → Export e-Factura (XML), apoi încărcarea în SPV (validarea oficială n-o putem face noi).
- Dacă vrea: un extras de cont real (.pdf / .csv / .xlsx), ca să-l punem anonimizat în colecția de test.
- Când vrea kitul 0.9.3 (are licența nouă, în engleză, și plusurile de azi).
- Dacă suita se va vinde: o verificare juridică a licenței.
