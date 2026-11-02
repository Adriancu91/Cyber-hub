# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-11-03 00:08 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- Programul se numește **Cyber Office Studio** (în interfață și în kitul 0.9.5). Plusurile P1 (diacritice), P2 (e-Factura), P3 (extrase de cont) sunt gata; P4 (semnături digitale) e gata în afară de LTV, care așteaptă răspunsul lui Adrian.
- Lucrăm la „funcțiile care lipsesc”. Sesiunea 02.11 23:27 – 03.11 00:08 (6 pași, testele trec), șabloane noi gata de completat:
  - Sheets: **Garanții** (când expiră garanția fiecărui produs) și **Împrumuturi** (bani dați / primiți de la prieteni, restanțe; 26 de șabloane);
  - Docs: **Notificare de retragere** pentru un retur online în 14 zile (24); Slides: **Aniversare** (26);
  - Notițe: **Internare în spital** și **Accident auto** (constatare amiabilă, RCA; 29);
  - înainte (02.11 seara): Plângere împotriva unei amenzi, Proces-verbal de constatare a pagubei, Citiri contoare, Medicamente, Atelier de gătit, Început de an școlar, Casa înainte de plecare.
- O singură aplicație desktop (Electron + React + TypeScript), de la zero, totul local: Docs, Sheets, PDF, Slides, Imagini, Video, Notițe, în română sau engleză.
- Scoruri: **Word 90,6%**, **Excel 92%**, **PowerPoint 91,8%**, Clipchamp 82,1%, Notițe 83,9%, Acrobat 86,5%, Photoshop 85,1%, formule **97,7%**. Colecția de test: **480 / 582** fișiere reale fără pierderi, 3 erori (.eps doar cu desen PostScript, cu mesaj clar).

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
