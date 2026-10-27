# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-27 14:25 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- Plusurile alese de Adrian: P1 (diacritice), P2 (e-Factura) și P3 (extrase de cont) sunt gata; **P4 (semnături digitale) e gata în afară de LTV**, care așteaptă răspunsul lui Adrian.
- Lucrăm la „funcțiile care lipsesc”. Sesiunea 13:47–14:25, 4 commituri, testele trec, toate textele noi traduse (verificat și pe ecran, în engleză):
  - **Sheets:** **stilurile de tabel întunecate** (tot tabelul închis, litere albe; și în .xlsx) și **fereastra completă a Foii de prognoză** (perioade, interval de încredere, sezon automat / ales / fără, goluri, dubluri, statistici).
  - **Slides:** **limba de verificare a casetelor** (Revizuire → Limbă; păstrată în .pptx; reparat: textul din .pptx-urile salvate era marcat engleză, acum română) și **6 teme noi** (Birou, Ardezie, Ocean, Vin, Cretă, Retro), fiecare cu 3 variante.
- Prezentările .pptx din colecție se deschid la fel de bine ca înainte (verificat după schimbarea la citire).
- O singură aplicație desktop (Electron + React + TypeScript), de la zero, totul local: Docs, Sheets, PDF, Slides, Imagini, Video, Notițe, în română sau engleză.
- Scoruri: Word 83,9%, Excel 83,8%, PowerPoint 83,7%, Clipchamp 79,4%, Notițe 76,4%, Acrobat 75,4%, Photoshop 72,8%, formule 97,1%.

## Urmează
- Alte funcții „parțial” / „nu” din inventar (Word, Excel, PowerPoint), câte una pe pas.
- Slides: rotirea 3-D la forme; Excel: stilurile de tabel proprii.
- P4: LTV, doar după răspunsul lui Adrian (vezi mai jos).

## Ce oferă proiectul celorlalți
- Nimic nou acum. Mai târziu (după testarea de către oameni): motorul de calcul, citirea documentelor (PDF / .docx → text), motorul de diacritice românești și semnarea / verificarea XML (XML-DSig, scrise de la zero).

## De ce are nevoie de la ceilalți
- Nimic.

## Blocaje / nevoie de Adrian
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
