# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-27 17:27 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- Plusurile alese de Adrian: P1 (diacritice), P2 (e-Factura) și P3 (extrase de cont) sunt gata; **P4 (semnături digitale) e gata în afară de LTV**, care așteaptă răspunsul lui Adrian.
- Lucrăm la „funcțiile care lipsesc”. Sesiunea 16:37–17:30, 5 commituri, testele trec (și testul mare de compatibilitate: 530 de fișiere, 0 erori), toate textele noi traduse (verificat și pe ecran, în engleză):
  - **Sheets:** **fonturile temei** (Aspect pagină → Aa Fonturi: 8 perechi Titluri / Corp); fontul obișnuit al celulelor urmează tema; se scriu și se citesc în .xlsx.
  - **Slides:** **rotirea 3-D** la forme și poze (perspectivă și izometric, păstrată în .pptx); **5 stiluri de poză noi** (reflexie, perspectivă cu umbră, culcată pe masă); **textul cu reflexie** și un stil WordArt cu reflexie.
- O singură aplicație desktop (Electron + React + TypeScript), de la zero, totul local: Docs, Sheets, PDF, Slides, Imagini, Video, Notițe, în română sau engleză.
- Scoruri: Word 84,2%, Excel 84,8%, PowerPoint 84,6%, Clipchamp 79,4%, Notițe 76,4%, Acrobat 75,4%, Photoshop 72,8%, formule 97,1%.

## Urmează
- Alte funcții „parțial” / „nu” din inventar (Word, Excel, PowerPoint), câte una pe pas.
- Slides: umplerea textului cu gradient; Excel: efectele temei.
- P4: LTV, doar după răspunsul lui Adrian (vezi mai jos).

## Ce oferă proiectul celorlalți
- Nimic nou acum. Mai târziu (după testarea de către oameni): motorul de calcul, citirea documentelor (PDF / .docx → text), motorul de diacritice românești și semnarea / verificarea XML (XML-DSig, scrise de la zero).

## De ce are nevoie de la ceilalți
- Nimic.

## Blocaje / nevoie de Adrian
- Să deschidă la serviciu un .pptx salvat din Suite cu o formă rotită 3-D (Slides → bara formei → Rotire 3-D → Perspectivă: stânga) și un .xlsx cu fonturile temei schimbate (Sheets → Aspect pagină → Aa Fonturi → Carte): arată la fel? (aici n-am avut cu ce testa).
- Să deschidă la serviciu un .xlsx colorat (de exemplu un tabel cu rânduri albastru deschis): culorile apar în Sheets ca în original? Și invers: Sheets → Aspect pagină → 🎨 Teme → Pădure → Salvează ca .xlsx: programul de la serviciu arată aceeași paletă?
- Dacă are la serviciu un program de prezentări care deschide .odp: să deschidă o prezentare salvată din Suite cu Slides → Fișier → Export .odp… (titluri, liste, forme, poze, un grafic): arată la fel? (aici n-am avut cu ce testa).
- Să deschidă la serviciu un .docx salvat din Suite cu formular (Docs → Inserare → ☐ Casetă, ▾ Listă verticală, 📅 Selector de dată), cu filigran din imagine și cu sigla în antet (Aspect → Pagină… → Imagine în antet): merg controalele, se văd sigla și filigranul? (aici n-am avut cu ce testa).
- Să deschidă la serviciu un .docx cu cuprins salvat din Suite (Docs → Referințe → Cuprins → Salvează ca .docx): programul întreabă de actualizarea câmpurilor și pune numerele paginilor?
- Să deschidă la serviciu un .xlsx salvat din Suite cu comentarii cu răspunsuri (Sheets → Revizuire → 💬 Comentariu nou): apar ca discuții?
- **LTV:** ca o semnătură să poată fi verificată și peste ani, Suite ar trebui să întrebe pe internet serverele emitentului certificatului (OCSP / CRL), la semnare. E în regulă, doar la cererea ta, ca la marca temporală?
- Să încerce un .docx semnat din Suite în programul de birou de la serviciu (Docs → „.docx semnat digital…”): îl recunoaște ca semnat?
- Să încerce semnarea cu tokenul lui real: PDF → 🔏 Semnează digital → Folosește un certificat de pe calculator sau token…; dacă apare o eroare, mesajul ne spune ce să reparăm.
- Dacă are de la furnizorul certificatului adresa unui server de marcă temporală: s-o încerce cu bifa „Adaugă marca temporală”.
- Dacă primește un .p7m / .p7s sau un .docx semnat real: ni-l poate da ca să-l punem în colecția de test.
- Să încerce o factură reală: Sheets → Șabloane → Factură (e-Factura) → Export e-Factura (XML), apoi încărcarea în SPV.
- Când vrea kitul 0.9.3 (are licența nouă, în engleză, și plusurile din ultimele zile).
- Dacă suita se va vinde: o verificare juridică a licenței.
