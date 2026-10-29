# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-29 12:38 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- Plusurile alese de Adrian: P1 (diacritice), P2 (e-Factura) și P3 (extrase de cont) sunt gata; **P4 (semnături digitale) e gata în afară de LTV**, care așteaptă răspunsul lui Adrian.
- Lucrăm la „funcțiile care lipsesc”. Sesiunea 11:43–12:38, 5 pași, testele trec:
  - Sheets (Rezumat / tabel pivot): **grupuri alese de mână** pe rânduri („Nord” = Cluj + Iași), **elemente calculate** („Diferență” = Cluj - Iași; rândul Total nu le mai adună de două ori), rezumatul făcut **din tabelul cu nume** (fără rândul Total adus din .xlsx, urmărit după nume la reîmprospătare).
  - Sheets (formule): MATCH / VLOOKUP / ISNUMBER pe o zonă și IFERROR / IFNA / ISNA pe liste dau câte un rezultat pe rând (de exemplu `FILTER(…;ISNUMBER(MATCH(…)))`, des întâlnită în tabelele primite, dădea greșit).
- O singură aplicație desktop (Electron + React + TypeScript), de la zero, totul local: Docs, Sheets, PDF, Slides, Imagini, Video, Notițe, în română sau engleză.
- Scoruri: Word 88,0%, **Excel 87,2%** (era 86,7%), PowerPoint 89,2%, Clipchamp 79,8%, Notițe 78,7%, Acrobat 78,4%, Photoshop 78,7%, formule 97,1%. Colecția de test: 455 / 541 fișiere reale fără pierderi, 0 erori.

## Urmează
- Sheets: filtrul de raport din Rezumat cu mai multe valori alese.
- Alte funcții „parțial” / „nu” din inventar, câte una pe pas.

## Ce oferă proiectul celorlalți
- Nimic nou acum. Mai târziu (după testarea de către oameni): motorul de calcul, citirea documentelor (PDF / .docx → text), motorul de diacritice românești și semnarea / verificarea XML (XML-DSig, scrise de la zero).

## De ce are nevoie de la ceilalți
- Nimic.

## Blocaje / nevoie de Adrian
- Să încerce Sheets → Tabel Pivot pe un tabel real cu „+ Grupează categorii” (de exemplu orașele pe regiuni) și „+ Element calculat” (diferența dintre două categorii): e ușor de folosit și cifrele sunt cele așteptate?
- Să încerce Sheets → Tabel Pivot pe un tabel real cu Agent pe coloane și „Încă un câmp pe coloane” (de exemplu Produs), sau cu o coloană de date pe coloane grupată pe luni: cifrele și subtotalurile sunt cele așteptate?
- Să încerce Imagini → Ctrl+Shift+S → PNG cu bifa 2× și GIF cu Culori: 32: fișierele ies bine?
- Să deschidă în Imagini un .psd de-al lui cu text → ⓘ Proprietăți → Text → ✎ Rescrie textul, apoi Ctrl+S ca .psd și să-l deschidă la serviciu: noul text arată ca originalul și rămâne text pe care îl poate edita?
- Să încerce Slides → Fișier → Fă video din prezentare (MP4)… pe o prezentare cu tranziții: trecerile din film seamănă cu cele din prezentare? Și Imagini → ✒ Traseu → ◐ Mască din traseu: e ușor de folosit?
- Să încerce Slides → Inserare → 𝒜 Text artistic ▾ → „Arc auriu”, apoi Export .pptx deschis la serviciu: textul stă tot pe arc? Și Sheets → Ctrl+Q pe un tabel: previzualizarea la trecerea mouse-ului e utilă sau încurcă?
- Să tipărească din Docs (Ctrl+P) un document cu „Numerotează paginile” pe imprimanta lui: apar numerele jos, marginile sunt albe și textul e clar?
- Să încerce Docs → Corespondență → 📨 Începere îmbinare → 🖨 Tipărește exemplarele (de la … până la …) pe imprimanta lui, și Sheets → Date → Preluare date → Din PDF… cu un extras / o factură PDF reală.
- Să încerce Docs → Corespondență → 🏷 Etichete → „O etichetă pentru fiecare rând dintr-un tabel” și ✉ Plicuri → „Un plic pentru fiecare rând” cu un tabel de clienți de-al lui: ies bine adresele? Tipărite pe o foaie de etichete adevărată, cad pe etichete?
- Să încerce Sheets → Diagramă → tipul „Radar (pânză de păianjen)” și să salveze .xlsx deschis la serviciu: graficul rămâne radar?
- Să deschidă în Slides câteva .pptx reale de la serviciu cu diagrame SmartArt și scheme logice: apar toate, cu textul lor? Și Slides → tabel → Proiectare tabel → Culoarea stilului.
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
