# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-27 01:59 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- Lucrul continuu merge pe plusurile alese de Adrian (P1–P4), înaintea funcțiilor care lipsesc. P1 (diacritice), P2 (e-Factura) și P3 (extrase de cont) sunt gata; **P4 (semnături digitale) e în lucru, aproape gata**.
- Sesiunea de noapte (01:23–01:59), 3 commituri, testele trec:
  - **Verifică un fișier semnat primit** (.p7s sau .p7m): PDF → 🖋 → 🔍 Verifică un fișier semnat… spune cine a semnat, cu ce certificat, când și dacă fișierul e neschimbat; din .p7m scoate fișierul (și deschide PDF-ul direct).
  - **Marca temporală** la semnătură (ora confirmată de un server ales de utilizator): semnătura PDF devine PAdES B-T, .p7s devine CAdES-T; panoul arată ora mărcii, verificată.
  - **Documentele .docx / .xlsx / .pptx semnate** se recunosc la deschidere: „Documentul e semnat digital de …; dacă îl salvezi din Suite, semnătura nu se păstrează”.
- O singură aplicație desktop (Electron + React + TypeScript), de la zero, totul local: Docs, Sheets, PDF, Slides, Imagini, Video, Notițe, în română sau engleză.
- Scoruri: Word 81,7%, Excel 81,1%, PowerPoint 80,6%, Clipchamp 79,4%, Notițe 76,4%, Acrobat 74,6%, Photoshop 72,8%, formule 97,1%.

## Urmează
- P4: verificarea și semnarea .docx / .xlsx / .pptx (XML-DSig), apoi LTV (lanțul și revocarea păstrate în PDF).
- Apoi ținta „funcțiile care lipsesc” (Slides: coordonatoarele; PDF: fontul / culoarea textului existent; Sheets: formatarea graficului).

## Ce oferă proiectul celorlalți
- Nimic nou acum. Mai târziu (după testarea de către oameni): motorul de calcul, citirea documentelor (PDF / .docx → text) și motorul de diacritice românești.

## De ce are nevoie de la ceilalți
- Nimic.

## Blocaje / nevoie de Adrian
- Să încerce semnarea cu tokenul lui real (n-am avut unul la test): PDF → 🔏 Semnează digital → Folosește un certificat de pe calculator sau token…; dacă apare o eroare, mesajul ne spune ce să reparăm.
- Dacă are de la furnizorul certificatului adresa unui server de marcă temporală: s-o încerce cu bifa „Adaugă marca temporală” (noi am testat doar cu un server de test local).
- Dacă primește un .p7m / .p7s sau un .docx semnat real: ni-l poate da ca să-l punem în colecția de test.
- Să încerce o factură reală: Sheets → Șabloane → Factură (e-Factura) → Export e-Factura (XML), apoi încărcarea în SPV.
- Când vrea kitul 0.9.3 (are licența nouă, în engleză, și plusurile de azi).
- Dacă suita se va vinde: o verificare juridică a licenței.
