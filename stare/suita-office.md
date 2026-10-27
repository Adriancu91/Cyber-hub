# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-27 04:43 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- Plusurile alese de Adrian: P1 (diacritice), P2 (e-Factura) și P3 (extrase de cont) sunt gata; **P4 (semnături digitale) e gata în afară de LTV**, care așteaptă răspunsul lui Adrian.
- Lucrăm la „funcțiile care lipsesc”. Sesiunea de noapte (04:09–04:45), 5 commituri, testele trec, totul în Sheets → grafice:
  - **Stiluri rapide**: 8 stiluri dintr-un clic (umbre, degrade, fundal închis…), păstrate și în .xlsx.
  - **Serii**: debifezi o serie și dispare din grafic (datele rămân în tabel).
  - **Comutare rând/coloană**: seriile devin rândurile tabelului; „Selectare date” e acum completă.
- O singură aplicație desktop (Electron + React + TypeScript), de la zero, totul local: Docs, Sheets, PDF, Slides, Imagini, Video, Notițe, în română sau engleză.
- Scoruri: Word 81,7%, Excel 81,6%, PowerPoint 81,9%, Clipchamp 79,4%, Notițe 76,4%, Acrobat 75,2%, Photoshop 72,8%, formule 97,1%.

## Urmează
- Slides: alinierea și spațierea pe fiecare paragraf (acum se aplică pe toată caseta).
- PDF: reașezarea paragrafului la editarea textului.
- P4: LTV, doar după răspunsul lui Adrian (vezi mai jos).

## Ce oferă proiectul celorlalți
- Nimic nou acum. Mai târziu (după testarea de către oameni): motorul de calcul, citirea documentelor (PDF / .docx → text), motorul de diacritice românești și semnarea / verificarea XML (XML-DSig, scrise de la zero).

## De ce are nevoie de la ceilalți
- Nimic.

## Blocaje / nevoie de Adrian
- **LTV:** ca o semnătură să poată fi verificată și peste ani, Suite ar trebui să întrebe pe internet serverele emitentului certificatului (OCSP / CRL), la semnare. E în regulă, doar la cererea ta, ca la marca temporală?
- Să încerce un .docx semnat din Suite în programul de birou de la serviciu (Docs → „.docx semnat digital…”): îl recunoaște ca semnat? (aici n-am avut cu ce testa).
- Să încerce semnarea cu tokenul lui real: PDF → 🔏 Semnează digital → Folosește un certificat de pe calculator sau token…; dacă apare o eroare, mesajul ne spune ce să reparăm.
- Dacă are de la furnizorul certificatului adresa unui server de marcă temporală: s-o încerce cu bifa „Adaugă marca temporală”.
- Dacă primește un .p7m / .p7s sau un .docx semnat real: ni-l poate da ca să-l punem în colecția de test.
- Să încerce o factură reală: Sheets → Șabloane → Factură (e-Factura) → Export e-Factura (XML), apoi încărcarea în SPV.
- Când vrea kitul 0.9.3 (are licența nouă, în engleză, și plusurile din ultimele zile).
- Dacă suita se va vinde: o verificare juridică a licenței.
