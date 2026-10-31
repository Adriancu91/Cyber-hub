# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-31 21:18 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- Programul se numește **Cyber Office Studio** (în interfață și în kitul 0.9.5). Plusurile P1 (diacritice), P2 (e-Factura), P3 (extrase de cont) sunt gata; P4 (semnături digitale) e gata în afară de LTV, care așteaptă răspunsul lui Adrian.
- Lucrăm la „funcțiile care lipsesc”. Sesiunea 20:32–21:18, 4 pași în Sheets, testele trec:
  - **Editorul de interogare** (Date → Preluare date → Din tabel / zonă): Îmbină cu alt tabel (după o coloană-cheie, 3 feluri), Adaugă dedesubt alt tabel, Înlocuiește valorile, Împarte coloana după separator, Formatează textul.
  - **Revizuire → 🕘 Afișare modificări:** lista celulelor schimbate (ce era, ce e acum, ora, cine), pe registru / foaie / zonă, ținută în fișier.
- O singură aplicație desktop (Electron + React + TypeScript), de la zero, totul local: Docs, Sheets, PDF, Slides, Imagini, Video, Notițe, în română sau engleză.
- Scoruri: **Word 90,2%**, **Excel 91,3%**, **PowerPoint 91,2%**, Clipchamp 80,5%, Notițe 82,7%, Acrobat 86,5%, Photoshop 83,7%, formule 97,1%. Colecția de test: **477 / 560** fișiere reale fără pierderi, 0 erori.

## Urmează
- Alte funcții „parțial” / „nu” din inventar (la Notițe rămân cele mari: formatarea văzută direct în câmpul de scris, o notiță singură în fereastră separată, scrisul cu creionul direct pe pânză).

## Ce oferă proiectul celorlalți
- Nimic nou acum. Mai târziu (după testarea de către oameni): motorul de calcul, citirea documentelor (PDF / .docx → text), motorul de diacritice și despărțirea în silabe românească, semnarea / verificarea XML (XML-DSig, scrise de la zero).

## De ce are nevoie de la ceilalți
- Nimic.

## Blocaje / nevoie de Adrian
- **Decizie LTV:** ca o semnătură să poată fi verificată și peste ani, Suite ar trebui să întrebe pe internet serverele emitentului certificatului (OCSP / CRL), la semnare. E în regulă, doar la cererea lui, ca la marca temporală?
- **Kit:** 0.9.5 e gata (Cyber-Office-Studio-Instalare-0.9.5.exe, lista CE-E-NOU-0.9.5.txt); următorul va fi 0.9.6, doar când îl cere. Pe laptop Smart App Control blochează kitul nesemnat (JURNAL.md, 28.10). Dacă suita se va vinde: o verificare juridică a licenței.
- **Semnături și facturi reale:** semnarea cu tokenul lui (PDF → 🔏 Semnează digital, Docs → .docx semnat digital), un .p7m / .docx semnat real pentru colecția de test, și o factură reală trimisă din Sheets → Factură (e-Factura) → Export XML în SPV.
- **Fișiere salvate din Suite deschise la serviciu** (aici nu le putem verifica): .pptx cu scheme (Radial divergent, Venn stivuit, Proces cu cercuri, Listă cu etape), teme, cerneală, conectori și text pe arc; .xlsx cu tabele, stiluri, poze în celule, legături, teme (Mentă / Ardezie), forme desenate de mână; .docx cu ecuații, secțiuni, urmăriri, semnătură și forme din desen; .psd cu text și trasee; PDF/X și CMYK duse la tipografie.
- **Încercări de folosire reală** (pașii exacți sunt la „Cum testezi” în JURNAL.md, pe zile): cu o tabletă grafică sau un laptop cu creion, Imagini → Pensulă și Slides → ✏ Desenează (se îngroașă linia când apeși?); Docs → Diagramă → Listă în piramidă; temele Salvie / Oțel; Docs / Sheets → ✏ Desen → ◇ În formă; Pictograme → Educație / Sănătate (se recunosc?); Video → Ochi vertical; Docs → Gramatică pe documente reale; Notițe → Casetă liberă, lipire din browser, scris de mână → text; PDF → scanner, Combină / Lot cu e-mailuri, Elimină paginile goale, conversie în .xlsx / .pptx, preflight; Sheets → Pivot, Rezolvitor, Din web / PDF / imagine; Imagini → RAW, .eps, panoramă, profiluri de culoare.
