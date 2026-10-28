# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-28 09:23 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- Plusurile alese de Adrian: P1 (diacritice), P2 (e-Factura) și P3 (extrase de cont) sunt gata; **P4 (semnături digitale) e gata în afară de LTV**, care așteaptă răspunsul lui Adrian.
- Lucrăm la „funcțiile care lipsesc”, câte una pe pas. Sesiunea 08:37–09:23, 3 commituri, testele trec, textele noi traduse (verificat și pe ecran, în engleză):
  - **Slides: 🎙 Înregistrează prezentarea** (Prezentare): vocea de la microfon pe fiecare slide, cu timpii; la final narațiunea rămâne pe slide-uri și pornește singură; bifa „🔊 Redă narațiunile”; se păstrează și în .pptx.
  - **Slides: acțiunile casetelor** (🔗 Legătură): „Redă sunetul” la clic și „La trecerea mouse-ului” (fără clic), și în .pptx.
  - **Slides: Compară** (Versiuni și două taburi alăturate) arată acum și casetele mutate, mărite, recolorate, pozele înlocuite și notițele, nu doar textul.
- O singură aplicație desktop (Electron + React + TypeScript), de la zero, totul local: Docs, Sheets, PDF, Slides, Imagini, Video, Notițe, în română sau engleză.
- Scoruri: Word 86,6%, Excel 85,5%, PowerPoint 87,0%, Clipchamp 79,4%, Notițe 78,7%, Acrobat 77,0%, Photoshop 78,3%, formule 97,1%.

## Urmează
- Alte funcții „parțial” / „nu” din inventar (Acrobat, Notițe, Photoshop, Word, Excel, PowerPoint), câte una pe pas.
- De cercetat testul vechi al ecranului împărțit (meniul tabului), care dă greșeli și pe codul de dinainte.
- P4: LTV, doar după răspunsul lui Adrian (vezi mai jos).

## Ce oferă proiectul celorlalți
- Nimic nou acum. Mai târziu (după testarea de către oameni): motorul de calcul, citirea documentelor (PDF / .docx → text), motorul de diacritice românești și semnarea / verificarea XML (XML-DSig, scrise de la zero).

## De ce are nevoie de la ceilalți
- Nimic.

## Blocaje / nevoie de Adrian
- Să încerce Slides → Prezentare → 🎙 Înregistrează cu microfonul lui (aici testul folosește un microfon simulat): se aude vocea pe fiecare slide la ▶ De la început?
- Să încerce Slides → Inserare → 🖵 Înregistrare ecran pe ecranul lui (aici testul înregistrează doar fereastra lui, nu ecranul adevărat): se aude sunetul calculatorului și vocea?
- Să salveze din Docs un .docx cu un cuvânt pus aldin cu Revizuire → Urmărește modificările pornit și să-l deschidă la serviciu: apare ca „Formatat: Aldin”?
- Să încerce pe ecranul lui Docs → Vizualizare → ⊟ Scindare și Slides → ✏ Desenează → 📏 Riglă: sunt ușor de folosit?
- Să încerce Notițe → Vizualizare → 📌 Lipește pe margine: coloana din dreapta e bine așezată?
- Să deschidă la serviciu fișierele salvate din Suite pe care aici nu le-am putut verifica: sarcinile .ics din Notițe, .docx din PDF cu poze, .docx / .mht din Notițe, .pptx cu text în gradient și formă 3-D, .xlsx cu fonturile / culorile temei, .odp din Slides, .fdf din PDF, .docx cu formular, filigran, siglă în antet și cuprins, .xlsx cu comentarii cu răspunsuri: arată la fel?
- **LTV:** ca o semnătură să poată fi verificată și peste ani, Suite ar trebui să întrebe pe internet serverele emitentului certificatului (OCSP / CRL), la semnare. E în regulă, doar la cererea ta, ca la marca temporală?
- Să încerce un .docx semnat din Suite la serviciu și semnarea cu tokenul lui real (PDF → 🔏 Semnează digital); dacă are adresa unui server de marcă temporală, s-o încerce.
- Dacă primește un .p7m / .p7s sau un .docx semnat real: ni-l poate da pentru colecția de test.
- Să încerce o factură reală: Sheets → Șabloane → Factură (e-Factura) → Export e-Factura (XML), apoi încărcarea în SPV.
- Când vrea kitul 0.9.3 (are licența nouă, în engleză, și plusurile din ultimele zile).
- Dacă suita se va vinde: o verificare juridică a licenței.
