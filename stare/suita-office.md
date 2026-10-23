# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-23 08:45 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- O singură aplicație desktop (Electron + React + TypeScript), scrisă de la zero, totul local, fără cont și fără internet:
  Docs, Sheets, PDF, Slides, Imagini, Video, Notițe. Interfața e în română.
- Etapa 1 (compatibilitate) e gata: 529 de fișiere reale de test, 0 erori la deschidere. Etapa 2 (toate funcțiile) e în lucru.
  Scoruri: Word 80,3%, Excel 79,8%, Clipchamp 77,1%, PowerPoint 76,2%, Notițe 76,4%, Acrobat 73,2%, Photoshop 72,0%, formule 97,1%.
- Prima prioritate: problemele găsite de Adrian la birou cu 0.9.0. Punctele 1–4 și 1b făcute. **Punctul 5 („totul așezat ca în programele cunoscute”) e gata în toate cele 7 aplicații.**
  - **sesiunea asta, Notițe:** fila **Desenare** (Unelte, Stilouri, Forme, Foaie; deschide pânza cu unealta aleasă), **clic dreapta** pe pagină (Ștergere, Redenumire, Mutare / Copiere în secțiune, Duplicare, subpagini, Fixare) și pe secțiune (Redenumire, Ștergere, Pagină nouă, Culoare), vizualizarea **Carduri** (☰ Listă / ▦ Carduri, „Ia o notiță…”, 📌 pe card) și **literele Alt** (D Desenare; Alt, H, 1 = aldin…).
  - Reparat în toate aplicațiile: în paleta de comenzi (Alt+Q), cu mouse-ul lăsat peste listă, Enter făcea comanda de sub mouse în loc de prima găsită.
- Toate aplicațiile pornesc fără erori; testele noi (cdp-notes-ctx, -cards, -keytips) și cele vechi (Notițe, panglici, taste de acces, paleta, testul general) trec.

## Urmează
- 5b: tabul unui fișier importat (.xlsx / .docx / .pptx) arată numele fișierului, iar Salvează propune același nume și loc.
- Punctul 6: butonul „Trimite o observație” (captură + text salvate local, Adrian le trimite el).
- Rămășițe din punctul 5: Aranjare în Aspect (Docs), fontul original la editarea textului PDF.

## Ce oferă proiectul celorlalți
- Aplicațiile de birou pentru modulul Cyberspace (Kronos) și pentru setul de aplicații al Cyber Universe (după testarea umană).
- Fiecare aplicație e separată (`src/<modul>/`) și are `module.toml` după `standarde/modul-v0.md`.
- Cadrul comun de interfață (panglica cu file, modul „unelte”, modul „meniuri”, tastele de acces Alt, mini-bara, clic dreapta, panourile andocate),
  scurtăturile pe tastatura românească (`src/keys.ts`), motorul de formule (~500 de funcții), OCR în 5 limbi, criptarea, formularele și semnarea PDF, PDF/A,
  67 de filtre de imagine, cititorii și scriitorii .docx / .xlsx / .pptx / .pdf / .odt / .rtf / .psd.

## De ce are nevoie de la ceilalți
- Nimic acum.

## Blocaje / nevoie de Adrian
- De încercat (nu blochează): Notițe → Desenare: cerculețul roșu, apoi ▭ Dreptunghi (se deschide pânza cu ele); Vizualizare → ▦ Carduri, scrie în „Ia o notiță…” și Enter; clic dreapta pe o pagină → Duplicare pagină.
- De încercat (nu blochează): Notițe → Inserare: 📅 Dată, 🕐 Oră, 🔗 Legătură; Vizualizare: ＋ Mărire / 100%.
- De încercat (nu blochează): Notițe: scrie un rând și apasă Ctrl+1 (apare ☐), Ctrl+2 (apare ⭐), Ctrl+0 (le scoate); Ctrl+E duce cursorul în căutare.
  Atenție: Ctrl+E nu mai centrează rândul în Notițe (ca la programul de notițe cunoscut); centrarea e în lista ⇔ Aliniere.
- De încercat (nu blochează): Notițe: în stânga secțiunile una sub alta, alături paginile; jos ＋ Adăugare pagină; ◀ ascunde secțiunile.
- De încercat (nu blochează): Video: adu o poză → în dreapta filele Proprietăți (✨ Efecte, 🎨 Ajustare culori…) și bara mică deasupra pozei (⇋ oglindește).
- De încercat (nu blochează): Imagini: Fereastră → Proprietăți și Fereastră → Culoare; Slides: clic pe un tabel → „Proiectare tabel” și „Aspect”.
- De încercat (nu blochează): Docs: clic într-un tabel → „Proiectare tabel” și „Aspect”; Sheets și PDF așezate ca la birou; PDF → Editare → ✎ Editează text pe un act real.
- De verificat (nu blochează): .xlsx cu Rezolvitor, fișiere cu parolă și .docx protejat din Suite, deschise în programele de la serviciu;
  un cod QR din Suite scanat cu telefonul; un PDF „Fă-l PDF/A” trecut printr-un validator oficial; Slides pe un al doilea monitor.
- Întrebare (nu blochează): marcajul de timp la semnarea PDF cere un server de timp pe internet (se trimite doar amprenta documentului).
  Îl adăugăm ca opțiune, cu un server ales de Adrian? Până atunci semnăturile au ora calculatorului.
- Codul e doar local, pe laptop; pus pe GitHub doar dacă Adrian decide.
