# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-27 02:46 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- Lucrul continuu merge pe plusurile alese de Adrian (P1–P4), înaintea funcțiilor care lipsesc. P1 (diacritice), P2 (e-Factura) și P3 (extrase de cont) sunt gata; **P4 (semnături digitale) e gata în afară de LTV**.
- Sesiunea de noapte (01:58–02:46), 5 commituri, testele trec:
  - **.docx / .xlsx / .pptx semnate se verifică la deschidere**: „semnătura e validă” sau „NU e validă: documentul s-a schimbat după semnare” (forma canonică a XML-ului scrisă de la zero, verificată pe semnături făcute independent).
  - **Semnarea lor din Suite**: Docs / Sheets / Slides → Export … semnat digital, și PDF → 🔏 Semnează un fișier; cu ID-ul Suite, .pfx sau certificatul de pe calculator / token; mai multe semnături una după alta.
  - **Marca temporală și la documente** (XAdES-T, confirmată independent cu openssl) și **certificatul semnatarului legat de semnătură** (XAdES SigningCertificate; un certificat înlocuit e prins).
- O singură aplicație desktop (Electron + React + TypeScript), de la zero, totul local: Docs, Sheets, PDF, Slides, Imagini, Video, Notițe, în română sau engleză.
- Scoruri: Word 81,7%, Excel 81,1%, PowerPoint 80,6%, Clipchamp 79,4%, Notițe 76,4%, Acrobat 74,6%, Photoshop 72,8%, formule 97,1%.

## Urmează
- P4: LTV (lanțul și revocarea păstrate în semnătură), doar după răspunsul lui Adrian (vezi mai jos).
- Apoi ținta „funcțiile care lipsesc” (Slides: coordonatoarele; PDF: fontul / culoarea textului existent; Sheets: formatarea graficului).

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
- Când vrea kitul 0.9.3 (are licența nouă, în engleză, și plusurile de azi).
- Dacă suita se va vinde: o verificare juridică a licenței.
