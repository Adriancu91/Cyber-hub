# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-23 12:35 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- O singură aplicație desktop (Electron + React + TypeScript), scrisă de la zero, totul local, fără cont și fără internet:
  Docs, Sheets, PDF, Slides, Imagini, Video, Notițe. Interfața e în română (engleza e în lucru).
- Etapa 1 (compatibilitate) e gata: 529 de fișiere reale de test, 0 erori la deschidere. Etapa 2 (toate funcțiile) e în lucru.
  Scoruri: Word 80,3%, Excel 79,8%, Clipchamp 77,1%, PowerPoint 76,2%, Notițe 76,4%, Acrobat 73,2%, Photoshop 72,0%, formule 97,1%.
- Problemele găsite de Adrian la birou cu 0.9.0: punctele 1–6 gata. „Finalul cerut” a) și a2) gata.
- **Sesiunea asta (meniul în engleză, b):** cu butonul **EN** (jos în bara din stânga), toate filele obișnuite din Docs, Sheets și Slides,
  filele din Notițe și 10 din filele PDF sunt acum în engleză, cu explicațiile de la trecerea mouse-ului. Traducătorul ține cont și de loc
  (de exemplu „Ștergere” e „Delete” ca buton, dar „Wipe” ca tranziție). În Slides, butonul „WordArt” se cheamă acum „Text artistic”.
  Textul scris de utilizator nu se traduce niciodată; RO readuce româna.
- Toate aplicațiile pornesc fără erori; testele panglicilor, cdp-office-profiles, cdp-lang și cdp-all trec.

## Urmează
- Engleza pentru ce a mai rămas: filele PDF Revizuire / Tipar / Vizualizare, Acasă, Imagini, Video, ferestrele de dialog și descrierile funcțiilor din Sheets.
- Apoi kitul de instalare nou 0.9.x (c, d). Nimic pe stick fără „da”-ul lui Adrian.

## Ce oferă proiectul celorlalți
- Aplicațiile de birou pentru modulul Cyberspace (Kronos) și pentru setul de aplicații al Cyber Universe (după testarea umană).
- Fiecare aplicație e separată (`src/<modul>/`) și are `module.toml` după `standarde/modul-v0.md`.
- Cadrul comun de interfață (panglica cu file, profilurile de meniu, modul „unelte”, modul „meniuri”, tastele Alt, mini-bara, clic dreapta, panourile andocate),
  traducerea pe loc a interfeței (RO / EN), scurtăturile pe tastatura românească, motorul de formule (~500 de funcții), OCR în 5 limbi, criptarea,
  formularele și semnarea PDF, PDF/A, 67 de filtre de imagine, cititorii și scriitorii .docx / .xlsx / .pptx / .pdf / .odt / .rtf / .psd.

## De ce are nevoie de la ceilalți
- Nimic acum.

## Blocaje / nevoie de Adrian
- **De privit:** capturile din dosarul workspace: „PDF profil 23.10 1 … 5 ….png”, „Meniuri clasice 23.10 *.png”, „Aerisit 23.10 *.png” și
  „Simplu 23.10 *.png”. Spune care aranjare îți place; o poți alege din ▦ (sus în dreapta) în fiecare aplicație.
- De încercat (nu blochează): jos în bara din stânga **EN** → Docs / Sheets / Slides: toate filele sunt în engleză; **RO** readuce româna.
- De încercat (nu blochează): 💬 Trimite o observație (jos în stânga): scrie ceva, Salvează observația, apoi Deschide dosarul.
- De verificat (nu blochează): .xlsx cu Rezolvitor, fișiere cu parolă și .docx protejat din Suite, deschise în programele de la serviciu;
  un cod QR din Suite scanat cu telefonul; un PDF „Fă-l PDF/A” trecut printr-un validator oficial; Slides pe un al doilea monitor.
- Întrebare (nu blochează): marcajul de timp la semnarea PDF cere un server de timp pe internet (se trimite doar amprenta documentului).
  Îl adăugăm ca opțiune, cu un server ales de Adrian? Până atunci semnăturile au ora calculatorului.
- Codul e doar local, pe laptop; pus pe GitHub doar dacă Adrian decide.
