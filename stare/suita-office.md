# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-23 10:12 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- O singură aplicație desktop (Electron + React + TypeScript), scrisă de la zero, totul local, fără cont și fără internet:
  Docs, Sheets, PDF, Slides, Imagini, Video, Notițe. Interfața e în română.
- Etapa 1 (compatibilitate) e gata: 529 de fișiere reale de test, 0 erori la deschidere. Etapa 2 (toate funcțiile) e în lucru.
  Scoruri: Word 80,3%, Excel 79,8%, Clipchamp 77,1%, PowerPoint 76,2%, Notițe 76,4%, Acrobat 73,2%, Photoshop 72,0%, formule 97,1%.
- Problemele găsite de Adrian la birou cu 0.9.0: punctele 1–6 gata. „Finalul cerut” a) gata (Sheets la 1440 px are toate grupurile întregi).
- **Sesiunea asta:**
  - **Profilurile de meniu (a2) la PDF:** butonul mic ▦ (sus în dreapta) alege între 4 aranjări ale acelorași comenzi: Unelte în stânga (implicit),
    **Aerisit** (miniaturile în stânga, uneltele des folosite sus, panoul „Avansat” în dreapta, meniul Afișare ascunde barele, Ctrl+H = doar pagina),
    **Panouri laterale** (coloană cu sarcini în stânga) și **Simplu** (modurile Citește / Adnotează / Editează / Semnează / Pagini). Se ține minte.
  - Docs → Aspect → Aranjare: **Panou de selecție** (lista pozelor și casetelor de text). PDF: textul editat păstrează felul fontului vechi (serife, aldin, cursiv).
  - Reparat: două setări salvate în același moment nu se mai pot șterge una pe alta.
- Toate aplicațiile pornesc fără erori; testele noi (cdp-pdf-profiles, cdp-sheets-1440) și cele vechi trec.

## Urmează
- După ce Adrian vede capturile PDF: profilurile pentru Sheets / Docs / Slides („Panglică”, „Meniuri clasice”, „Aerisit”, „Simplu”).
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
- **De privit (cerut de plan înainte de celelalte aplicații):** capturile „PDF profil 23.10 1 … 5 ….png” din dosarul workspace (cele 4 aranjări ale PDF-ului).
  Spune care îți place și ce să schimbăm; apoi le facem și la Sheets, Docs, Slides.
- De încercat (nu blochează): în PDF butonul ▦ (sus în dreapta) → Aerisit; Afișare → debifează „Bara de unelte”; Ctrl+H și Esc.
- De încercat (nu blochează): 💬 Trimite o observație (jos în stânga): scrie ceva, Salvează observația, apoi Deschide dosarul (se văd .txt și .png).
- De încercat (nu blochează): deschide un .xlsx al tău: tabul are numele lui; Salvează propune același dosar. Bara din stânga: butonul » / « de lângă „S”.
- De verificat (nu blochează): .xlsx cu Rezolvitor, fișiere cu parolă și .docx protejat din Suite, deschise în programele de la serviciu;
  un cod QR din Suite scanat cu telefonul; un PDF „Fă-l PDF/A” trecut printr-un validator oficial; Slides pe un al doilea monitor.
- Întrebare (nu blochează): marcajul de timp la semnarea PDF cere un server de timp pe internet (se trimite doar amprenta documentului).
  Îl adăugăm ca opțiune, cu un server ales de Adrian? Până atunci semnăturile au ora calculatorului.
- Codul e doar local, pe laptop; pus pe GitHub doar dacă Adrian decide.
