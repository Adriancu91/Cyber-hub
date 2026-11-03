# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-11-03 04:55 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- Programul se numește **Cyber Office Studio** (în interfață și în kitul 0.9.5). Plusurile P1 (diacritice), P2 (e-Factura), P3 (extrase de cont) sunt gata; P4 (semnături digitale) e gata în afară de LTV, care așteaptă răspunsul lui Adrian.
- Lucrăm la „funcțiile care lipsesc”. Sesiunea 03.11 04:00 – 04:55 (6 pași gata, testele trec):
  - un set pentru sărbători: Notițe → șablonul **🎄 Crăciun** (cadouri, meniu, de pregătit), Slides → șablonul **Petrecere de Crăciun** (28 de șabloane), Docs → șablonul **Felicitare de sărbători**;
  - Docs: șablonul **Decizie internă** (31 de șabloane în Docs), pereche cu Proces-verbal de recepție; în engleză, numele șablonului apare acum tradus și în mesajul de jos;
  - tema nouă **Piersică** în Slides / Docs / Sheets (34 / 32 / 30 de teme); Video: stilul de titlu **Diplomă** (84 de stiluri).
  - înainte (03.11 noaptea): Notițe → atașamentele deschise în aplicația lor; scheme Listă cu linii și Bule de dialog (68 de feluri); Sheets → ⊞ Patru panouri; PDF → atașamentele deschise în aplicația lor; șabloane de nuntă, botez, referat, proces-verbal de recepție.
- O singură aplicație desktop (Electron + React + TypeScript), de la zero, totul local: Docs, Sheets, PDF, Slides, Imagini, Video, Notițe, în română sau engleză.
- Scoruri: **Word 90,8%**, **Excel 92,3%**, **PowerPoint 92,1%**, Clipchamp 82,1%, Notițe 83,9%, Acrobat 86,5%, Photoshop 85,1%, formule **97,7%**. Colecția de test: **480 / 582** fișiere reale fără pierderi, 3 erori (.eps doar cu desen PostScript, cu mesaj clar).

## Urmează
- Alte funcții „parțial” / „nu” din inventar (de exemplu șabloane, teme, diagrame); reducerea zgomotului în Video, după ce găsim reglajul bun.

## Ce oferă proiectul celorlalți
- Nimic nou acum. Mai târziu (după testarea de către oameni): motorul de calcul, citirea documentelor (PDF / .docx → text), motorul de diacritice și despărțirea în silabe românească, semnarea / verificarea XML (XML-DSig, scrise de la zero).

## De ce are nevoie de la ceilalți
- Nimic.

## Blocaje / nevoie de Adrian
- **Decizie LTV:** ca o semnătură să poată fi verificată și peste ani, Suite ar trebui să întrebe pe internet serverele emitentului certificatului (OCSP / CRL), la semnare. E în regulă, doar la cererea lui, ca la marca temporală?
- **Kit:** 0.9.5 e gata (Cyber-Office-Studio-Instalare-0.9.5.exe, lista CE-E-NOU-0.9.5.txt); următorul va fi 0.9.6, doar când îl cere. Pe laptop Smart App Control blochează kitul nesemnat (JURNAL.md, 28.10). Dacă suita se va vinde: o verificare juridică a licenței.
- **Semnături și facturi reale:** semnarea cu tokenul lui (PDF → 🔏 Semnează digital, Docs → .docx semnat digital), un .p7m / .docx semnat real pentru colecția de test, și o factură reală trimisă din Sheets → Factură (e-Factura) → Export XML în SPV.
- **Fișiere salvate din Suite deschise la serviciu** (aici nu le putem verifica): .pptx cu scheme (Radial divergent, Venn stivuit, Venn liniar, Săgeată ascendentă, Proces cu cercuri, Listă cu etape), teme, cerneală, conectori și text pe arc; .xlsx cu tabele, stiluri, poze în celule, legături, teme (Mentă / Ardezie), forme desenate de mână; .docx cu ecuații, secțiuni, urmăriri, semnătură și forme din desen; .docx / .xlsx cu Clasificare (se vede la Proprietăți → Particularizat?); .psd cu text și trasee; PDF/X și CMYK duse la tipografie.
- **Încercări de folosire reală** (pașii exacți sunt la „Cum testezi” în JURNAL.md, pe zile): Docs → ⓘ Proprietăți → Clasificare, cu „Scrie clasificarea ca filigran” (apare eticheta jos și filigranul?); Slides → Fișier → Proprietăți…; o declarație ANAF în PDF → fila Formular (Datele .xml, Verifică câmpurile obligatorii); cu o tabletă grafică sau un laptop cu creion, Imagini → Pensulă și Slides → ✏ Desenează (se îngroașă linia când apeși?); Docs → Diagramă → Listă în piramidă; temele Salvie / Oțel / Măslin; Docs / Sheets → ✏ Desen → ◇ În formă; Pictograme → Casă / Unelte (se recunosc?); Video → Ochi vertical; Docs → Gramatică pe documente reale; Notițe → Casetă liberă, lipire din browser, scris de mână → text; PDF → scanner, Combină / Lot cu e-mailuri, Elimină paginile goale, conversie în .xlsx / .pptx, preflight; Sheets → Pivot, Rezolvitor, Din web / PDF / imagine; Imagini → RAW, .eps, panoramă, profiluri de culoare.
