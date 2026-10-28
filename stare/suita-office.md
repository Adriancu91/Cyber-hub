# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-28 19:23 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- Plusurile alese de Adrian: P1 (diacritice), P2 (e-Factura) și P3 (extrase de cont) sunt gata; **P4 (semnături digitale) e gata în afară de LTV**, care așteaptă răspunsul lui Adrian.
- Lucrăm la „funcțiile care lipsesc”, câte una pe pas. Sesiunea 18:39–19:23, 4 pași, testele trec, textele noi traduse:
  - **Imagini → Felii:** și o pagină web (.html) care pune feliile la loc, cu o legătură (opțională) pe fiecare felie; feliile desenate se pot muta și mări / micșora din colț.
  - **Docs:** Aspect → Margini → Doar secțiunea aceasta (1–3 cm): margini diferite doar pentru o secțiune, în .docx și la tipărire / PDF.
- O singură aplicație desktop (Electron + React + TypeScript), de la zero, totul local: Docs, Sheets, PDF, Slides, Imagini, Video, Notițe, în română sau engleză.
- Scoruri: Word 87,3%, Excel 85,7%, PowerPoint 88,5%, Clipchamp 79,8%, Notițe 78,7%, Acrobat 78,4%, Photoshop 78,6%, formule 97,1%.

## Urmează
- Alte funcții „parțial” / „nu” din inventar, câte una pe pas (de ex. căi de mișcare desenate de mână în Slides, antet diferit pe secțiune și pagina culcată arătată și pe ecran în Docs).
- Lipirea conectorilor de elipse în .pptx: doar după un fișier real care o arată (în colecția de test nu e niciunul, iar numerotarea punctelor nu o ghicim).
- P4: LTV, doar după răspunsul lui Adrian (vezi mai jos).

## Ce oferă proiectul celorlalți
- Nimic nou acum. Mai târziu (după testarea de către oameni): motorul de calcul, citirea documentelor (PDF / .docx → text), motorul de diacritice românești și semnarea / verificarea XML (XML-DSig, scrise de la zero).

## De ce are nevoie de la ceilalți
- Nimic.

## Blocaje / nevoie de Adrian
- Să încerce Slides → două dreptunghiuri unul sub altul → Săgeată → Traseu → ┐ Conector frânt, lipită de punctele albastre de jos / sus, apoi Export .pptx și deschiderea la serviciu: săgeata arată la fel și rămâne lipită când muți un dreptunghi?
- Să încerce Slides → Inserare → 📷 Cameo cu camera laptopului, și în prezentare (F5): se vede bine, fără să încetinească?
- Să încerce Video → ▭ Carton → stilul „Pastilă colorată” și trecerea „Jaluzele” între două poze: arată bine în filmul exportat?
- Să încerce PDF → Comprimă… → 🧹 Optimizează structura și ☰ Meniu → Elimină informațiile ascunse… pe PDF-uri reale de-ale lui: după Salvează ca…, fișierul arată la fel?
- Să încerce PDF → Semnează… → 🔍 Caută și redactează pe un PDF adevărat (o adeverință, un contract): după Salvează ca…, restul textului se poate selecta și nu rămâne nicio literă din ce a fost redactat?
- Să încerce Docs → Revizuire → Compară cu un .docx… → 📝 Document marcat pe un contract real primit înapoi: se vede bine ce s-a schimbat? Și un .docx cu Aspect → Întreruperi → Secțiune: Pagina următoare, deschis la serviciu: secțiunea nouă începe pe pagina următoare?
- Să încerce Sheets → Date → Preluare date → Din imagine… cu o poză făcută cu telefonul unui tabel adevărat: ies bine rândurile și coloanele? Și Docs → Aspect → Orientare → Doar secțiunea aceasta: Orizontală, apoi Export .docx deschis la serviciu: doar pagina aceea e culcată?
- Să încerce Imagini → Fișier → ✂ Felii… cu „Și o pagină web (.html)” și o legătură pe o felie, apoi să deschidă pagina în browser: poza apare întreagă și legătura merge? Și Docs → Aspect → Margini → Doar secțiunea aceasta: 1 cm, apoi Export .docx deschis la serviciu: doar secțiunea aceea are margini înguste?
- Să încerce Docs → Revizuire → ✓ Gramatică pe un document adevărat de-al lui: arată greșeli care nu sunt greșeli?
- Să încerce Slides → Prezentare → 🎙 Înregistrează cu microfonul lui și Slides → Inserare → 🖵 Înregistrare ecran pe ecranul lui: se aude vocea / sunetul? Are vocea și în MP4?
- Să salveze din Docs un .docx cu un cuvânt pus aldin cu Urmărește modificările pornit și să-l deschidă la serviciu: apare ca „Formatat: Aldin”?
- Să încerce Docs → Vizualizare → ⊟ Scindare, Slides → ✏ Desenează → 📏 Riglă și Notițe → Vizualizare → 📌 Lipește pe margine: sunt ușor de folosit?
- Să deschidă la serviciu fișierele salvate din Suite pe care aici nu le-am putut verifica: .ics din Notițe, .docx din PDF cu poze, .docx / .mht din Notițe, .pptx cu gradient, 3-D și conectori, .xlsx cu fonturile temei și comentarii cu răspunsuri, .odp din Slides, .fdf din PDF, .docx cu formular, filigran, siglă și cuprins: arată la fel?
- **LTV:** ca o semnătură să poată fi verificată și peste ani, Suite ar trebui să întrebe pe internet serverele emitentului certificatului (OCSP / CRL), la semnare. E în regulă, doar la cererea ta, ca la marca temporală?
- Să încerce un .docx semnat din Suite la serviciu și semnarea cu tokenul lui real (PDF → 🔏 Semnează digital); dacă are un .p7m / .p7s sau un .docx semnat real, ni-l poate da pentru colecția de test.
- Să încerce o factură reală: Sheets → Șabloane → Factură (e-Factura) → Export e-Factura (XML), apoi încărcarea în SPV.
- Kitul 0.9.3 e gata (Office-Suite-Test-Instalare-0.9.3.exe, cu lista CE-E-NOU-0.9.3.txt, din commitul d009e246; noutățile de după el (sesiunile 14:32–16:50) intră în 0.9.4). Pe acest laptop Smart App Control din Windows blochează kitul nesemnat; detaliile sunt în JURNAL.md, 28.10, ora 15:00.
- Dacă suita se va vinde: o verificare juridică a licenței.
