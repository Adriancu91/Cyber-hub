# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-23 07:26 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- O singură aplicație desktop (Electron + React + TypeScript), scrisă de la zero, totul local, fără cont și fără internet:
  Docs, Sheets, PDF, Slides, Imagini, Video, Notițe. Interfața e în română.
- Etapa 1 (compatibilitate) e gata: 529 de fișiere reale de test, 0 erori la deschidere. Etapa 2 (toate funcțiile) e în lucru.
  Scoruri: Word 80,3%, Excel 79,8%, Clipchamp 77,1%, PowerPoint 76,2%, Notițe 76,4%, Acrobat 73,2%, Photoshop 72,0%, formule 97,1%.
- Prima prioritate: problemele găsite de Adrian la birou cu 0.9.0. Punctele 1–4 și 1b făcute. Acum: punctul 5, „totul așezat ca în programele cunoscute”:
  - **gata:** Sheets, PDF, Docs (D1–D7), Slides (L1–L7), Imagini (I1–I5), Video (V1–V5), Notițe N1 (coloanele Secțiuni | Pagini);
  - **sesiunea asta:** Notițe N2, **scurtăturile cunoscute**: Ctrl+E caută în toate caietele, Ctrl+T secțiune nouă, Ctrl+1 ☐ De făcut,
    Ctrl+2 … 6 etichete (⭐ ❓ 💡 📞 📌), Ctrl+0 le scoate, Ctrl+. / Ctrl+/ liste, Ctrl+− tăiat, Ctrl+Alt+H evidențiat, Ctrl+Alt+1 … 6 titluri,
    Ctrl+Shift+N golire formatare, Ctrl+PageUp / PageDown și Alt+PageUp / PageDown între pagini, Alt+Shift+F data și ora.
  - N3 partea 1 (fila Pornire din Notițe în ordinea cunoscută) e făcută, dar pusă deoparte (git stash): la fereastra de 1024 px panglica iese cu 19 px.
- Toate aplicațiile pornesc fără erori; toate cele 38 de teste Notițe, testul panglicii și testul general trec.

## Urmează
- Notițe N3: reiau fila Pornire (Clipboard · Text de bază · Stiluri · Etichete · Notiță) și repar cei 19 px; apoi Inserare, Desenare, Vizualizare.
- Notițe N4–N6: Carduri, clic dreapta pe pagină / secțiune, tastele Alt.
- Punctul 6: butonul „Trimite o observație” (captură + text salvate local, Adrian le trimite el).

## Ce oferă proiectul celorlalți
- Aplicațiile de birou pentru modulul Cyberspace (Kronos) și pentru setul de aplicații al Cyber Universe (după testarea umană).
- Fiecare aplicație e separată (`src/<modul>/`) și are `module.toml` după `standarde/modul-v0.md`.
- Cadrul comun de interfață (panglica cu file, modul „unelte”, modul „meniuri”, tastele de acces Alt, mini-bara, clic dreapta, panourile andocate),
  scurtăturile pe tastatura românească (`src/keys.ts`), motorul de formule (~500 de funcții), OCR în 5 limbi, criptarea, formularele și semnarea PDF, PDF/A,
  67 de filtre de imagine, cititorii și scriitorii .docx / .xlsx / .pptx / .pdf / .odt / .rtf / .psd.

## De ce are nevoie de la ceilalți
- Nimic acum.

## Blocaje / nevoie de Adrian
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
