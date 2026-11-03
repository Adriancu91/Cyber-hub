# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-11-03 14:25 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- Programul se numește **Cyber Office Studio** (în interfață și în kitul 0.9.5). Plusurile P1 (diacritice), P2 (e-Factura), P3 (extrase de cont) sunt gata; P4 (semnături digitale) e gata în afară de LTV, care așteaptă răspunsul lui Adrian.
- Sesiunea 03.11 13:42 – 14:25 (4 pași, fiecare cu commit): **tabelele puse dintr-un .xlsx / .ods / .csv rămân legate de fișier**, în Docs și în Slides.
  - Inserare → **↻ Actualizează foile legate** le citește din nou cu valorile de acum (bordurile, stilul, locul și mărimea alese rămân; fișierele lipsă au mesaj clar);
  - la deschiderea unui document sau a unei prezentări cu tabele legate, bara de jos spune dacă fișierele s-au schimbat (nimic nu se schimbă singur).
- Mai devreme, azi, în **Studio de documente**: Nota de recepție (NIR), Borderoul de achiziție de la persoane fizice (vânzătorii ținuți minte) și editorul de șabloane proprii cu logo.
- Mai devreme, azi: seturi de șabloane pentru inventar și salarii, plăți și contabilitatea lunii, angajați (Sheets 40, Docs 42, Notițe 43 de șabloane).
- **Modul extra nou: Studio de documente** (cerut de Adrian, 03.11; commit e2b829f3). Are profilul firmei cu mai multe puncte de lucru, clienții, transportatorii, mașinile și șoferii, plus completarea după CUI (ANAF) sau cod de TVA (VIES). „Transport nou” scoate avizul, CMR-ul și Anexa 7 într-un singur PDF; „Transport în țară” scoate avizul și Anexa 3. Datele stau doar pe calculator. E modul **extra**: îl are versiunea firmei lui Adrian; în kitul pentru clienți e oprit (se pornește la cerere, cu abonament VIP). Verificarea completă a traducerilor (check-ro) merge din nou (~1 s, 0 lipsă).
- O singură aplicație desktop (Electron + React + TypeScript), de la zero, totul local: Docs, Sheets, PDF, Slides, Imagini, Video, Notițe, în română sau engleză.
- Scoruri: **Word 90,8%**, **Excel 92,3%**, **PowerPoint 92,1%**, Clipchamp 82,1%, Notițe 83,9%, Acrobat 86,5%, Photoshop 85,1%, formule **97,7%**. Colecția de test: **480 / 582** fișiere reale fără pierderi, 3 erori (.eps doar cu desen PostScript, cu mesaj clar).

## Urmează
- Studio: de verificat cu Adrian formularele pe hârtie (aviz, Anexa 3, nota de recepție, borderoul). După Studio: gestiunea de stocuri, pas cu pas, cu Adrian (nota de recepție e primul pas spre intrări).
- Alte funcții „parțial” / „nu” din inventar (șabloane, teme, diagrame); reducerea zgomotului în Video, după ce găsim reglajul bun.

## Ce oferă proiectul celorlalți
- Nimic nou acum. Mai târziu (după testarea de către oameni): motorul de calcul, citirea documentelor (PDF / .docx → text), motorul de diacritice și despărțirea în silabe românească, semnarea / verificarea XML (XML-DSig, scrise de la zero).

## De ce are nevoie de la ceilalți
- Nimic.

## Blocaje / nevoie de Adrian
- **Studio de documente:** să-l încerce pe documentele lui reale și să spună ce nu se potrivește cu tipizatele lui (acum și nota de recepție, borderoul de achiziție și șabloanele proprii). La borderou: ce procent de impozit se reține azi (câmpul e gol din oficiu, îl scrie el sau contabilul). Anexa 3 și Anexa 7 sunt refăcute după structura oficială, avizul după tipizatul 14-3-6A, iar CMR-ul are căsuțele 1–24 standard. Tot el confirmă dacă avizele se numerotează separat pe fiecare punct de lucru. Anexa 1 se face doar când îi trebuie.
- **Decizie LTV:** ca o semnătură să poată fi verificată și peste ani, Suite ar trebui să întrebe pe internet serverele emitentului certificatului (OCSP / CRL), la semnare. E în regulă, doar la cererea lui, ca la marca temporală?
- **Kit:** 0.9.5 e gata (Cyber-Office-Studio-Instalare-0.9.5.exe, lista CE-E-NOU-0.9.5.txt); următorul va fi 0.9.6, doar când îl cere. Pe laptop Smart App Control blochează kitul nesemnat (JURNAL.md, 28.10). Dacă suita se va vinde: o verificare juridică a licenței.
- **Semnături și facturi reale:** semnarea cu tokenul lui (PDF → 🔏 Semnează digital, Docs → .docx semnat digital), un .p7m / .docx semnat real pentru colecția de test, și o factură reală trimisă din Sheets → Factură (e-Factura) → Export XML în SPV.
- **Fișiere salvate din Suite deschise la serviciu** (aici nu le putem verifica): .pptx cu scheme, teme, cerneală, conectori și text pe arc; .xlsx cu tabele, stiluri, poze în celule, legături, teme, forme desenate de mână; .docx cu ecuații, secțiuni, urmăriri, semnătură și forme din desen; .docx / .xlsx cu Clasificare; .psd cu text și trasee; PDF/X și CMYK duse la tipografie.
- **Încercări de folosire reală** (pașii exacți sunt la „Cum testezi” în JURNAL.md, pe zile): seturile de azi cu date reale ale firmei: plăți (Sheets → Facturi de la furnizori, Evidența TVA pe luni, Flux de numerar; Docs → Proces-verbal de compensare), inventar și salarii (Sheets → Registrul mijloacelor fixe, Listă de inventariere, Stat de plată, cu procentele verificate de contabil); Docs → ⓘ Proprietăți → Clasificare; o declarație ANAF în PDF → fila Formular; cu o tabletă grafică, Imagini → Pensulă și Slides → ✏ Desenează; Docs → Diagramă → Listă cu inimi / nori; temele Salvie / Oțel / Măslin / Bordo; Docs → Gramatică pe documente reale; Notițe → scris de mână → text; PDF → scanner, Combină, conversie în .xlsx / .pptx, preflight; Sheets → Pivot, Rezolvitor, Din web / PDF / imagine; Imagini → RAW, .eps, panoramă, profiluri de culoare.
