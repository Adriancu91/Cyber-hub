# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-28 22:30 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- Plusurile alese de Adrian: P1 (diacritice), P2 (e-Factura) și P3 (extrase de cont) sunt gata; **P4 (semnături digitale) e gata în afară de LTV**, care așteaptă răspunsul lui Adrian.
- Lucrăm la „funcțiile care lipsesc”, câte una pe pas. Sesiunea 21:52–22:30, 3 pași, testele trec, textele noi traduse (engleza verificată pe tot ecranul):
  - **Docs → Tipărește / Ctrl+P:** pe hârtie ies acum și numerele paginilor, sigla, prima pagină / paginile pare diferite și antetul propriu al fiecărei secțiuni (se tipărește chiar PDF-ul aplicației). Reparat și la PDF: marginile foii nu mai ies gri închis.
  - **Docs → Corespondență → Etichete:** o etichetă pentru fiecare rând dintr-un tabel (.xlsx / CSV / tabel Suite), cu «Bloc de adresă» sau coloanele alese.
  - **Docs → Corespondență → Plicuri:** un plic pentru fiecare rând dintr-un tabel.
- În paralel, o altă sesiune lucrează la feedback-ul colegilor (extrasul de cont în Sheets: coloana Partener, foaia Parteneri).
- O singură aplicație desktop (Electron + React + TypeScript), de la zero, totul local: Docs, Sheets, PDF, Slides, Imagini, Video, Notițe, în română sau engleză.
- Scoruri: Word 87,5%, Excel 85,9%, PowerPoint 88,8%, Clipchamp 79,8%, Notițe 78,7%, Acrobat 78,4%, Photoshop 78,6%, formule 97,1%.

## Urmează
- Alte funcții „parțial” / „nu” din inventar, câte una pe pas (de ex. variantele stilurilor de tabel în Slides).
- Lipirea conectorilor de elipse în .pptx: doar după un fișier real care o arată.
- P4: LTV, doar după răspunsul lui Adrian (vezi mai jos).

## Ce oferă proiectul celorlalți
- Nimic nou acum. Mai târziu (după testarea de către oameni): motorul de calcul, citirea documentelor (PDF / .docx → text), motorul de diacritice românești și semnarea / verificarea XML (XML-DSig, scrise de la zero).

## De ce are nevoie de la ceilalți
- Nimic.

## Blocaje / nevoie de Adrian
- Să tipărească din Docs (Ctrl+P) un document cu „Numerotează paginile” pe imprimanta lui: apar numerele jos, marginile sunt albe și textul e clar?
- Să încerce Docs → Corespondență → 🏷 Etichete → „O etichetă pentru fiecare rând dintr-un tabel” și ✉ Plicuri → „Un plic pentru fiecare rând” cu un tabel de clienți de-al lui: ies bine adresele? Tipărite pe o foaie de etichete adevărată, cad pe etichete?
- Să încerce Slides → două dreptunghiuri unul sub altul → Săgeată → Traseu → ┐ Conector frânt, lipită de punctele albastre de jos / sus, apoi Export .pptx și deschiderea la serviciu: săgeata arată la fel și rămâne lipită când muți un dreptunghi?
- Să încerce Slides → Inserare → 📷 Cameo cu camera laptopului, și în prezentare (F5): se vede bine, fără să încetinească?
- Să încerce Video → ▭ Carton → stilul „Pastilă colorată” și trecerea „Jaluzele” între două poze: arată bine în filmul exportat?
- Să încerce PDF → Comprimă… → 🧹 Optimizează structura, ☰ Meniu → Elimină informațiile ascunse… și PDF → Semnează… → 🔍 Caută și redactează pe PDF-uri reale de-ale lui: după Salvează ca…, fișierul arată la fel și nu rămâne nimic din ce a fost redactat?
- Să încerce Docs → Revizuire → Compară cu un .docx… → 📝 Document marcat pe un contract real; și .docx cu secțiuni (Pagina următoare, Orientare / Margini doar pentru secțiune, antet propriu cu 🔗 Legat de anterior debifat) deschise la serviciu: arată la fel?
- Să încerce Sheets → Date → Preluare date → Din imagine… cu o poză a unui tabel adevărat și Sheets → Vizualizare → ⊟ Scindare pe un tabel lung: merg bine?
- Să încerce Imagini → Fișier → ✂ Felii… cu „Și o pagină web (.html)” și o legătură pe o felie: poza apare întreagă în browser și legătura merge?
- Să încerce Slides → Animații → Cale desenată de mână, ✍ Formă liberă, § Zoom de secțiune, 🎙 Înregistrează și 🖵 Înregistrare ecran (cu sunet și în MP4), apoi Export .pptx deschis la serviciu.
- Să încerce Docs → Revizuire → ✓ Gramatică pe un document adevărat: arată greșeli care nu sunt greșeli? Și Docs → Vizualizare → ⊟ Scindare, Slides → 📏 Riglă, Notițe → 📌 Lipește pe margine: sunt ușor de folosit?
- Să deschidă la serviciu fișierele salvate din Suite pe care aici nu le-am putut verifica: .ics din Notițe, .docx din PDF cu poze, .docx / .mht din Notițe, .pptx cu gradient, 3-D și conectori, .xlsx cu fonturile temei și comentarii cu răspunsuri, .odp din Slides, .fdf din PDF, .docx cu formular, filigran, siglă, cuprins și urmărirea formatării: arată la fel?
- **LTV:** ca o semnătură să poată fi verificată și peste ani, Suite ar trebui să întrebe pe internet serverele emitentului certificatului (OCSP / CRL), la semnare. E în regulă, doar la cererea ta, ca la marca temporală?
- Să încerce un .docx semnat din Suite la serviciu și semnarea cu tokenul lui real (PDF → 🔏 Semnează digital); dacă are un .p7m / .p7s sau un .docx semnat real, ni-l poate da pentru colecția de test.
- Să încerce o factură reală: Sheets → Șabloane → Factură (e-Factura) → Export e-Factura (XML), apoi încărcarea în SPV.
- Kitul 0.9.3 e gata (Office-Suite-Test-Instalare-0.9.3.exe, cu lista CE-E-NOU-0.9.3.txt, din commitul d009e246); noutățile de după el intră în 0.9.4. Pe acest laptop Smart App Control din Windows blochează kitul nesemnat (JURNAL.md, 28.10, ora 15:00).
- Dacă suita se va vinde: o verificare juridică a licenței.
