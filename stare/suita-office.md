# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-23 10:54 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- O singură aplicație desktop (Electron + React + TypeScript), scrisă de la zero, totul local, fără cont și fără internet:
  Docs, Sheets, PDF, Slides, Imagini, Video, Notițe. Interfața e în română.
- Etapa 1 (compatibilitate) e gata: 529 de fișiere reale de test, 0 erori la deschidere. Etapa 2 (toate funcțiile) e în lucru.
  Scoruri: Word 80,3%, Excel 79,8%, Clipchamp 77,1%, PowerPoint 76,2%, Notițe 76,4%, Acrobat 73,2%, Photoshop 72,0%, formule 97,1%.
- Problemele găsite de Adrian la birou cu 0.9.0: punctele 1–6 gata. „Finalul cerut” a) gata.
- **Sesiunea asta (profilurile de meniu, a2 pasul 4):**
  - **Sheets, Docs, Slides și Notițe** au acum butonul mic ▦ (sus în dreapta), ca PDF-ul: **Panglică** (cum era) sau **Meniuri clasice**
    (un rând subțire Fișier / Pornire / Inserare…; fiecare se deschide ca listă cu pictograma, numele și scurtătura; lista prea înaltă se așază pe coloane).
    Aceleași butoane, aceleași acțiuni; alegerea se ține minte pentru fiecare aplicație și se găsește și în „Caută o comandă” (Alt+Q).
  - Video păstrează bara laterală (așezarea editorului video cunoscut); Imagini avea deja meniuri sus.
- Toate aplicațiile pornesc fără erori; testul nou cdp-office-profiles și testele vechi ale panglicilor trec.

## Urmează
- Profilul „Aerisit” (și „Simplu”) pentru Sheets / Docs / Slides, după ce Adrian spune ce i-a plăcut la PDF.
- Apoi meniul în engleză (b) și kitul de instalare nou 0.9.x (c, d). Nimic pe stick fără „da”-ul lui Adrian.

## Ce oferă proiectul celorlalți
- Aplicațiile de birou pentru modulul Cyberspace (Kronos) și pentru setul de aplicații al Cyber Universe (după testarea umană).
- Fiecare aplicație e separată (`src/<modul>/`) și are `module.toml` după `standarde/modul-v0.md`.
- Cadrul comun de interfață (panglica cu file, profilurile de meniu, modul „unelte”, modul „meniuri”, tastele Alt, mini-bara, clic dreapta, panourile andocate),
  scurtăturile pe tastatura românească, motorul de formule (~500 de funcții), OCR în 5 limbi, criptarea, formularele și semnarea PDF, PDF/A,
  67 de filtre de imagine, cititorii și scriitorii .docx / .xlsx / .pptx / .pdf / .odt / .rtf / .psd.

## De ce are nevoie de la ceilalți
- Nimic acum.

## Blocaje / nevoie de Adrian
- **De privit:** capturile „PDF profil 23.10 1 … 5 ….png” (cele 4 aranjări ale PDF-ului) și „Meniuri clasice 23.10 Sheets / Docs / Slides / Notite.png”
  din dosarul workspace. Spune care îți place și ce să schimbăm; după asta facem „Aerisit” și la celelalte aplicații.
- De încercat (nu blochează): în Sheets ▦ (sus în dreapta) → Meniuri clasice → clic pe Pornire; înapoi cu ▦ → Panglică.
- De încercat (nu blochează): 💬 Trimite o observație (jos în stânga): scrie ceva, Salvează observația, apoi Deschide dosarul.
- De verificat (nu blochează): .xlsx cu Rezolvitor, fișiere cu parolă și .docx protejat din Suite, deschise în programele de la serviciu;
  un cod QR din Suite scanat cu telefonul; un PDF „Fă-l PDF/A” trecut printr-un validator oficial; Slides pe un al doilea monitor.
- Întrebare (nu blochează): marcajul de timp la semnarea PDF cere un server de timp pe internet (se trimite doar amprenta documentului).
  Îl adăugăm ca opțiune, cu un server ales de Adrian? Până atunci semnăturile au ora calculatorului.
- Codul e doar local, pe laptop; pus pe GitHub doar dacă Adrian decide.
