# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-23 09:24 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- O singură aplicație desktop (Electron + React + TypeScript), scrisă de la zero, totul local, fără cont și fără internet:
  Docs, Sheets, PDF, Slides, Imagini, Video, Notițe. Interfața e în română.
- Etapa 1 (compatibilitate) e gata: 529 de fișiere reale de test, 0 erori la deschidere. Etapa 2 (toate funcțiile) e în lucru.
  Scoruri: Word 80,3%, Excel 79,8%, Clipchamp 77,1%, PowerPoint 76,2%, Notițe 76,4%, Acrobat 73,2%, Photoshop 72,0%, formule 97,1%.
- Prima prioritate: problemele găsite de Adrian la birou cu 0.9.0. **Punctele 1–6 sunt gata** (rămân doar rămășițe din 5: Aranjare în Aspect, fontul original la editarea textului PDF).
  - **sesiunea asta:** 5b: tabul unui fișier importat (.xlsx / .csv / .docx / .pptx…) arată numele lui, iar Salvează propune același nume și dosar.
  - **punctul 6:** butonul **💬 Trimite o observație** (jos în bara din stânga): text + poza ferestrei salvate doar local, în Documente\Suite\Observații.
  - Panglica: numele butoanelor mari se rup pe două rânduri înainte să se strângă grupurile; un grup strâns e un buton mare cu pictogramă.
  - Bara din stânga se strânge singură la pictograme sub 1700 px (butonul « / »): la 1440 px Sheets arată Stiluri și Celule ca butoane mari.
- Toate aplicațiile pornesc fără erori; testele noi (cdp-feedback, cdp-nav-small) și cele vechi (taburi, panglici, taste Alt, testul general) trec.

## Urmează
- „Finalul cerut” a2): profilurile de meniu (aceleași comenzi, aranjări cunoscute diferite), pasul 1: lista comună de comenzi.
- Sheets la 1440 px: și grupul Editare întreg (lipsesc ~70 px).
- Rămășițele din punctul 5: Aranjare în Aspect (Docs), fontul original la editarea textului PDF.

## Ce oferă proiectul celorlalți
- Aplicațiile de birou pentru modulul Cyberspace (Kronos) și pentru setul de aplicații al Cyber Universe (după testarea umană).
- Fiecare aplicație e separată (`src/<modul>/`) și are `module.toml` după `standarde/modul-v0.md`.
- Cadrul comun de interfață (panglica cu file, modul „unelte”, modul „meniuri”, tastele de acces Alt, mini-bara, clic dreapta, panourile andocate),
  scurtăturile pe tastatura românească (`src/keys.ts`), motorul de formule (~500 de funcții), OCR în 5 limbi, criptarea, formularele și semnarea PDF, PDF/A,
  67 de filtre de imagine, cititorii și scriitorii .docx / .xlsx / .pptx / .pdf / .odt / .rtf / .psd.

## De ce are nevoie de la ceilalți
- Nimic acum.

## Blocaje / nevoie de Adrian
- De încercat (nu blochează): 💬 Trimite o observație (jos în stânga): scrie ceva, Salvează observația, apoi Deschide dosarul (se văd .txt și .png). Așa poți raporta repede ce nu merge.
- De încercat (nu blochează): deschide un .xlsx al tău: tabul are numele lui; Salvează propune același dosar. Bara din stânga: butonul » / « de lângă „S”.
- De încercat (nu blochează): Notițe → Desenare: cerculețul roșu, apoi ▭ Dreptunghi (se deschide pânza cu ele); Vizualizare → ▦ Carduri, scrie în „Ia o notiță…” și Enter; clic dreapta pe o pagină → Duplicare pagină.
- De încercat (nu blochează): Notițe: scrie un rând și apasă Ctrl+1 (apare ☐), Ctrl+2 (apare ⭐), Ctrl+0 (le scoate); Ctrl+E duce cursorul în căutare.
  Atenție: Ctrl+E nu mai centrează rândul în Notițe (ca la programul de notițe cunoscut); centrarea e în lista ⇔ Aliniere.
- De încercat (nu blochează): Video: adu o poză → în dreapta filele Proprietăți (✨ Efecte, 🎨 Ajustare culori…) și bara mică deasupra pozei (⇋ oglindește).
- De încercat (nu blochează): Imagini: Fereastră → Proprietăți și Fereastră → Culoare; Slides: clic pe un tabel → „Proiectare tabel” și „Aspect”.
- De încercat (nu blochează): Docs: clic într-un tabel → „Proiectare tabel” și „Aspect”; Sheets și PDF așezate ca la birou; PDF → Editare → ✎ Editează text pe un act real.
- De verificat (nu blochează): .xlsx cu Rezolvitor, fișiere cu parolă și .docx protejat din Suite, deschise în programele de la serviciu;
  un cod QR din Suite scanat cu telefonul; un PDF „Fă-l PDF/A” trecut printr-un validator oficial; Slides pe un al doilea monitor.
- Întrebare (nu blochează): marcajul de timp la semnarea PDF cere un server de timp pe internet (se trimite doar amprenta documentului).
  Îl adăugăm ca opțiune, cu un server ales de Adrian? Până atunci semnăturile au ora calculatorului.
- Codul e doar local, pe laptop; pus pe GitHub doar dacă Adrian decide.
