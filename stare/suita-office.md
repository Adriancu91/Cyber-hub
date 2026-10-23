# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-23 04:46 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- O singură aplicație desktop (Electron + React + TypeScript), scrisă de la zero, totul local, fără cont și fără internet:
  Docs, Sheets, PDF, Slides, Imagini, Video, Notițe. Interfața e în română.
- Etapa 1 (compatibilitate) e gata: 529 de fișiere reale de test, 0 erori la deschidere. Etapa 2 (toate funcțiile) e în lucru.
  Scoruri: Word 80,3%, Excel 79,8%, Clipchamp 77,1%, PowerPoint 76,2%, Notițe 76,4%, Acrobat 73,2%, Photoshop 72,0%, formule 97,1%.
- Prima prioritate: problemele găsite de Adrian la birou cu 0.9.0. Punctele 1–4 și 1b făcute. Acum: punctul 5, „totul așezat ca în programele cunoscute”:
  - **gata:** Sheets, PDF, Docs (D1–D7), Slides (L1–L7), **Imagini (I1–I5)**;
  - **sesiunea asta:** Imagini I5 (literele subliniate în meniuri, litera pornește comanda), I4 (panourile **Proprietăți** și **Culoare / Mostre** noi,
    **Ajustări** ca filă în coloana din dreapta); Video V3 (**bara cronologiei**: ↶ ↷ Scindare, Ștergere, Duplicare, Magnet, zoom) și V4
    (Ctrl+← / →, Ctrl+= / − / 0, Ctrl+A, Ctrl+/, X / Z / C + săgeți pentru mutare și tăiere din tastatură).
- Toate aplicațiile pornesc fără erori; testele noi și cele vechi de Imagini și Video trec în aplicația reală (cu taste adevărate).

## Urmează
- Video V1: fără panglică, antet cu Exportare și bara laterală din stânga (Conținutul tău, Înregistrare, Muzică, Text, Tranziții); apoi V2 și V5; apoi Notițe.
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
- De încercat (nu blochează): Imagini: clic pe meniul Imagine → litera subliniată de sub „Rotire” rotește poza; Fereastră → Proprietăți și Fereastră → Culoare (panourile din dreapta). Video: deasupra benzii ⧉ Duplicare / 🗑 Ștergere / 🧲 Magnet; ține X și apasă → (poza se mută). E ca la programele cunoscute?
- De încercat (nu blochează): Slides: clic pe un tabel → sus „Proiectare tabel” și „Aspect”; Proiectare → tema „Noapte”; Tranziții → Împingere → Opțiuni efect.
- De încercat (nu blochează): Docs: clic într-un tabel → „Proiectare tabel” și „Aspect”; dublu clic deasupra primului rând → antetul direct pe pagină; Alt, H, 1 face aldin.
- De încercat (nu blochează): Sheets și PDF așezate ca la birou; PDF → Editare → ✎ Editează text pe un act real; un .xlsx cu tabel făcut în Suite, deschis la birou.
- De verificat (nu blochează): .xlsx cu Rezolvitor, fișiere cu parolă și .docx protejat din Suite, deschise în programele de la serviciu;
  un cod QR din Suite scanat cu telefonul; un PDF „Fă-l PDF/A” trecut printr-un validator oficial; Slides pe un al doilea monitor.
- Întrebare (nu blochează): marcajul de timp la semnarea PDF cere un server de timp pe internet (se trimite doar amprenta documentului).
  Îl adăugăm ca opțiune, cu un server ales de Adrian? Până atunci semnăturile au ora calculatorului.
- Codul e doar local, pe laptop; pus pe GitHub doar dacă Adrian decide.
