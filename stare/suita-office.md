# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-22 14:48 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- O singură aplicație desktop (Electron + React + TypeScript), scrisă de la zero, totul local, fără cont și fără internet:
  Docs, Sheets, PDF, Slides, Imagini, Video, Notițe. Interfața e în română.
- Etapa 1 (compatibilitate) e gata: 529 de fișiere reale de test, 0 erori la deschidere.
- Etapa 2 (toate funcțiile) e în lucru. Scoruri față de aplicațiile de referință: Word 80,1%, Excel 79,8%, Clipchamp 77,1%, PowerPoint 76,2%,
  Notițe 76,4%, Acrobat 73,2%, Photoshop 72,0%, formule de calcul 97,1% (100% fără cele care cer internet).
- Sesiunea 13:53–14:50 (problemele găsite de Adrian la birou cu 0.9.0, punctul 4): **PDF → Editare → ✎ Editează text**: clic pe un rând
  îl deschide într-o casetă, Enter îl schimbă (textul vechi se scoate de-adevăratelea din pagină), Delete îl șterge, Ctrl+Z anulează; culoarea
  textului și a fundalului se păstrează; **imaginile din pagină** se mută trăgând de ele și se șterg cu Delete. Încercat și pe PDF-uri reale din corpus.
- Înainte (13:16–13:51): sugestii de funcții cu nume românești în Sheets, Inserare → Tabel (Ctrl+L) cu fila „Proiectare tabel”, păstrat în .xlsx.
- Reparat: la salvarea în .xlsx unele formule cu nume românești (ACUM, ORA, RÂND…) rămâneau românești și dădeau eroare.
- Toate aplicațiile pornesc fără erori; testele noi trec în aplicația reală; testul de compatibilitate: 0 erori.
- Într-o sesiune separată s-a pregătit programul de instalare Windows 0.9.0 (pentru etapa 5, testarea cu oameni).

## Urmează
- PRIMA PRIORITATE: problemele găsite de Adrian cu versiunea 0.9.0 la birou (lista în PLAN.md). Făcute: 1) deschiderea din Windows,
  2) sugestiile de funcții, 3) Inserare → Tabel, 4) editarea textului și a imaginilor în PDF (gata, fără fontul original al textului).
  Urmează: 5) butoanele așezate ca în aplicațiile cunoscute, 6) butonul „Trimite o observație”.
- Kit de instalare nou doar când îl cere Adrian (întâi testează pe laptop).

## Ce oferă proiectul celorlalți
- Aplicațiile de birou pentru modulul Cyberspace (Kronos) și pentru setul de aplicații al Cyber Universe (după testarea umană).
- Fiecare aplicație e separată (`src/<modul>/`) și are `module.toml` după `standarde/modul-v0.md`.
- Cadrul comun de interfață (panglica cu file, mini-bara, clic dreapta, panourile andocate), motorul de formule (~500 de funcții),
  dicționarul de sinonime și despărțirea în silabe în română, OCR-ul în 5 limbi, criptarea, formularele și semnarea PDF, PDF/A,
  cele 67 de filtre de imagine, cititorii și scriitorii .docx / .xlsx / .pptx / .pdf / .odt / .rtf / .psd pot fi refolosite.

## De ce are nevoie de la ceilalți
- Nimic acum.

## Blocaje / nevoie de Adrian
- De încercat (nu blochează): PDF → Editare → ✎ Editează text pe un act real: schimbi un cuvânt, salvezi; se vede bine și în programul de la birou?
- De încercat (nu blochează): un .xlsx cu un tabel făcut în Suite (Inserare → Tabel), deschis la birou: e tabel (cu nume și filtru), fără „reparare”?
- De încercat (nu blochează): un .xlsx cu forme (un balon cu text) făcut în Suite, deschis în programul de la serviciu: se poate edita forma?
- De încercat (nu blochează): un .docx cu „Despărțire în silabe → Automat” din Suite, deschis în programul de la serviciu: desparte și el cuvintele?
- De încercat (nu blochează): PDF → Text din scanare… pe un act în engleză sau maghiară, cu limba aleasă: iese textul corect?
- De încercat (nu blochează): Slides → Prezentare → 🖵 Ecran, cu un proiector sau al doilea monitor legat (aici s-a testat doar cu un ecran închipuit).
- De încercat (nu blochează): un .pptx cu declanșator făcut în Suite, deschis în programul de prezentări de la serviciu.
- De verificat (nu blochează): noile file din toate aplicațiile. Găsești tot ce foloseai? Ce buton folosit des a ajuns prea ascuns?
- De verificat (nu blochează): .xlsx cu Rezolvitor, fișiere cu parolă și .docx protejat din Suite, deschise în programele de la serviciu.
- De verificat (nu blochează): un cod QR din Suite scanat cu telefonul; un PDF „Fă-l PDF/A” trecut printr-un validator oficial.
- Întrebare (nu blochează): marcajul de timp la semnarea PDF cere un server de timp pe internet (se trimite doar amprenta documentului).
  Îl adăugăm ca opțiune, cu un server ales de Adrian? Până atunci semnăturile au ora calculatorului.
- Codul e doar local, pe laptop; pus pe GitHub doar dacă Adrian decide.
