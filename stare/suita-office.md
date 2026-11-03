# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-11-03 12:10 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- Programul se numește **Cyber Office Studio** (în interfață și în kitul 0.9.5). Plusurile P1 (diacritice), P2 (e-Factura), P3 (extrase de cont) sunt gata; P4 (semnături digitale) e gata în afară de LTV, care așteaptă răspunsul lui Adrian.
- Lucrăm la „funcțiile care lipsesc”. Sesiunea 03.11 11:23 – 12:10 (7 pași, fiecare cu commit): un set pentru **plăți și contabilitatea lunii**:
  - Sheets: **Facturi de la furnizori** (rest de plată, întârziate în roșu), **Flux de numerar pe 12 luni** (lunile pe minus în roșu), **Evidența TVA pe luni** (de plată / de recuperat, termenul pe 25) — 37 de șabloane;
  - Docs: **Cerere de eșalonare a plății** și **Proces-verbal de compensare** a datoriilor reciproce — 40 de șabloane;
  - Notițe: **💸 Plăți către furnizori** și **🧾 Închiderea lunii** (actele pentru contabil) — 42 de șabloane.
  - mai devreme, azi: seturi pentru angajați și zilele de naștere, scheme noi (Listă cu inimi / nori, 76 de feluri), tema Bordo.
- O altă sesiune lucrează (încă fără commit) la modulul nou „Studio de documente” (avize, CMR, formulare de deșeuri); sesiunile automate nu-i ating fișierele. Verificarea traducerilor întreagă (check-ro) se blochează din cauza textelor lui; sesiunile automate o rulează doar pe fișierele pe care le ating (0 texte netraduse).
- O singură aplicație desktop (Electron + React + TypeScript), de la zero, totul local: Docs, Sheets, PDF, Slides, Imagini, Video, Notițe, în română sau engleză.
- Scoruri: **Word 90,8%**, **Excel 92,3%**, **PowerPoint 92,1%**, Clipchamp 82,1%, Notițe 83,9%, Acrobat 86,5%, Photoshop 85,1%, formule **97,7%**. Colecția de test: **480 / 582** fișiere reale fără pierderi, 3 erori (.eps doar cu desen PostScript, cu mesaj clar).

## Urmează
- Alte funcții „parțial” / „nu” din inventar (șabloane, teme, diagrame); reducerea zgomotului în Video, după ce găsim reglajul bun.

## Ce oferă proiectul celorlalți
- Nimic nou acum. Mai târziu (după testarea de către oameni): motorul de calcul, citirea documentelor (PDF / .docx → text), motorul de diacritice și despărțirea în silabe românească, semnarea / verificarea XML (XML-DSig, scrise de la zero).

## De ce are nevoie de la ceilalți
- Nimic.

## Blocaje / nevoie de Adrian
- **Decizie LTV:** ca o semnătură să poată fi verificată și peste ani, Suite ar trebui să întrebe pe internet serverele emitentului certificatului (OCSP / CRL), la semnare. E în regulă, doar la cererea lui, ca la marca temporală?
- **Kit:** 0.9.5 e gata (Cyber-Office-Studio-Instalare-0.9.5.exe, lista CE-E-NOU-0.9.5.txt); următorul va fi 0.9.6, doar când îl cere. Pe laptop Smart App Control blochează kitul nesemnat (JURNAL.md, 28.10). Dacă suita se va vinde: o verificare juridică a licenței.
- **Semnături și facturi reale:** semnarea cu tokenul lui (PDF → 🔏 Semnează digital, Docs → .docx semnat digital), un .p7m / .docx semnat real pentru colecția de test, și o factură reală trimisă din Sheets → Factură (e-Factura) → Export XML în SPV.
- **Fișiere salvate din Suite deschise la serviciu** (aici nu le putem verifica): .pptx cu scheme, teme, cerneală, conectori și text pe arc; .xlsx cu tabele, stiluri, poze în celule, legături, teme, forme desenate de mână; .docx cu ecuații, secțiuni, urmăriri, semnătură și forme din desen; .docx / .xlsx cu Clasificare; .psd cu text și trasee; PDF/X și CMYK duse la tipografie.
- **Încercări de folosire reală** (pașii exacți sunt la „Cum testezi” în JURNAL.md, pe zile): setul de azi pentru plăți, cu facturi reale ale firmei (Sheets → Facturi de la furnizori, Evidența TVA pe luni, Flux de numerar; Docs → Proces-verbal de compensare); Docs → ⓘ Proprietăți → Clasificare; o declarație ANAF în PDF → fila Formular; cu o tabletă grafică, Imagini → Pensulă și Slides → ✏ Desenează; Docs → Diagramă → Listă cu inimi / nori; temele Salvie / Oțel / Măslin / Bordo; Docs → Gramatică pe documente reale; Notițe → scris de mână → text; PDF → scanner, Combină, conversie în .xlsx / .pptx, preflight; Sheets → Pivot, Rezolvitor, Din web / PDF / imagine; Imagini → RAW, .eps, panoramă, profiluri de culoare.
