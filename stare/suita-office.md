# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-23 06:20 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- O singură aplicație desktop (Electron + React + TypeScript), scrisă de la zero, totul local, fără cont și fără internet:
  Docs, Sheets, PDF, Slides, Imagini, Video, Notițe. Interfața e în română.
- Etapa 1 (compatibilitate) e gata: 529 de fișiere reale de test, 0 erori la deschidere. Etapa 2 (toate funcțiile) e în lucru.
  Scoruri: Word 80,3%, Excel 79,8%, Clipchamp 77,1%, PowerPoint 76,2%, Notițe 76,4%, Acrobat 73,2%, Photoshop 72,0%, formule 97,1%.
- Prima prioritate: problemele găsite de Adrian la birou cu 0.9.0. Punctele 1–4 și 1b făcute. Acum: punctul 5, „totul așezat ca în programele cunoscute”:
  - **gata:** Sheets, PDF, Docs (D1–D7), Slides (L1–L7), Imagini (I1–I5), **Video (V1–V5)**;
  - **sesiunea asta:** Video V5 (panoul Proprietăți pe **file cu pictograme**: Decupare, Audio, Estompări, Filtre, Efecte, Ajustare culori, Viteză,
    Tranziție, Transformare, Text; **bara plutitoare** deasupra imaginii: încadrare, rotire, oglindă, efecte, culori, text, duplicare, ștergere)
    și Notițe N1 (**două coloane**: caietele și secțiunile una sub alta | lista paginilor cu ＋ Adăugare pagină jos; ◀ strânge secțiunile).
- Toate aplicațiile pornesc fără erori; testele noi și cele vechi de Video și Notițe trec în aplicația reală.

## Urmează
- Notițe N2–N6: scurtăturile (Ctrl+E, Ctrl+T, Ctrl+1 / 2 / 3 …), filele Pornire / Inserare / Desenare / Vizualizare, Carduri, clic dreapta, tastele Alt.
- Punctul 6: butonul „Trimite o observație” (captură + text salvate local, Adrian le trimite el).
- Kit de instalare nou doar când îl cere Adrian (întâi testează pe laptop, cu „Porneste Suite.cmd”).

## Ce oferă proiectul celorlalți
- Aplicațiile de birou pentru modulul Cyberspace (Kronos) și pentru setul de aplicații al Cyber Universe (după testarea umană).
- Fiecare aplicație e separată (`src/<modul>/`) și are `module.toml` după `standarde/modul-v0.md`.
- Cadrul comun de interfață (panglica cu file, modul „unelte”, modul „meniuri”, tastele de acces Alt, mini-bara, clic dreapta, panourile andocate),
  scurtăturile pe tastatura românească (`src/keys.ts`), motorul de formule (~500 de funcții), OCR în 5 limbi, criptarea, formularele și semnarea PDF, PDF/A,
  67 de filtre de imagine, cititorii și scriitorii .docx / .xlsx / .pptx / .pdf / .odt / .rtf / .psd.

## De ce are nevoie de la ceilalți
- Nimic acum.

## Blocaje / nevoie de Adrian
- De încercat (nu blochează): Notițe: în stânga secțiunile una sub alta, alături paginile; jos ＋ Adăugare pagină; ◀ ascunde secțiunile.
- De încercat (nu blochează): Video: adu o poză → în dreapta filele Proprietăți (✨ Efecte, 🎨 Ajustare culori…) și bara mică deasupra pozei (⇋ oglindește).
- De încercat (nu blochează): Video: sus în dreapta ⤓ Export; în stânga cele 6 secțiuni; adu 2 poze, scoate una din bandă cu 🗑 și trage-o înapoi din Conținutul tău. E ca la editorul video cunoscut?
- De încercat (nu blochează): Imagini: Fereastră → Proprietăți și Fereastră → Culoare; Video: ține X și apasă → (poza se mută).
- De încercat (nu blochează): Slides: clic pe un tabel → sus „Proiectare tabel” și „Aspect”; Proiectare → tema „Noapte”; Tranziții → Împingere → Opțiuni efect.
- De încercat (nu blochează): Docs: clic într-un tabel → „Proiectare tabel” și „Aspect”; dublu clic deasupra primului rând → antetul direct pe pagină; Alt, H, 1 face aldin.
- De încercat (nu blochează): Sheets și PDF așezate ca la birou; PDF → Editare → ✎ Editează text pe un act real; un .xlsx cu tabel făcut în Suite, deschis la birou.
- De verificat (nu blochează): .xlsx cu Rezolvitor, fișiere cu parolă și .docx protejat din Suite, deschise în programele de la serviciu;
  un cod QR din Suite scanat cu telefonul; un PDF „Fă-l PDF/A” trecut printr-un validator oficial; Slides pe un al doilea monitor.
- Întrebare (nu blochează): marcajul de timp la semnarea PDF cere un server de timp pe internet (se trimite doar amprenta documentului).
  Îl adăugăm ca opțiune, cu un server ales de Adrian? Până atunci semnăturile au ora calculatorului.
- Codul e doar local, pe laptop; pus pe GitHub doar dacă Adrian decide.
- 2026-10-23 06:20 — Video: panoul Proprietăți pe file cu pictograme și bara plutitoare deasupra imaginii (V5 gata, Video gata la capitolul „așezat ca în programele cunoscute”).
- 2026-10-23 06:20 — Notițe: secțiunile și paginile pe două coloane, cu ＋ Adăugare pagină (N1); 3 commituri, toate testele Video și Notițe care pot rula singure trec.
