# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-27 15:20 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- Plusurile alese de Adrian: P1 (diacritice), P2 (e-Factura) și P3 (extrase de cont) sunt gata; **P4 (semnături digitale) e gata în afară de LTV**, care așteaptă răspunsul lui Adrian.
- Lucrăm la „funcțiile care lipsesc”. Sesiunea 14:26–15:20, 4 commituri, testele trec, toate textele noi traduse (verificat și pe ecran, în engleză):
  - **Sheets:** **Cronologie** (filtru pe perioade: ani / trimestre / luni / zile, clic pe o lună arată doar rândurile ei; filtrul intră și în .xlsx) și **filtrul de raport în Rezumat** (o listă deasupra tabelului pivot: alegi un an sau un agent și cifrele se refac).
  - **Docs:** **Tabel de autorități** pentru avocați (marchezi legile, hotărârile și cărțile citate, apoi tabelul lor pe categorii, cu paginile și „passim”).
  - **Slides:** formele **Inimă, Nor, Semilună, Fulger** (și în .pptx).
- O singură aplicație desktop (Electron + React + TypeScript), de la zero, totul local: Docs, Sheets, PDF, Slides, Imagini, Video, Notițe, în română sau engleză.
- Scoruri: Word 84,2%, Excel 84,3%, PowerPoint 83,7%, Clipchamp 79,4%, Notițe 76,4%, Acrobat 75,4%, Photoshop 72,8%, formule 97,1%.

## Urmează
- Alte funcții „parțial” / „nu” din inventar (Word, Excel, PowerPoint), câte una pe pas.
- Excel: stilurile de tabel proprii, temele registrului; Slides: rotirea 3-D la forme.
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
