# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-23 03:20 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- O singură aplicație desktop (Electron + React + TypeScript), scrisă de la zero, totul local, fără cont și fără internet:
  Docs, Sheets, PDF, Slides, Imagini, Video, Notițe. Interfața e în română.
- Etapa 1 (compatibilitate) e gata: 529 de fișiere reale de test, 0 erori la deschidere. Etapa 2 (toate funcțiile) e în lucru.
  Scoruri: Word 80,3%, Excel 79,8%, Clipchamp 77,1%, PowerPoint 76,2%, Notițe 76,4%, Acrobat 73,2%, Photoshop 72,0%, formule 97,1%.
- Prima prioritate: problemele găsite de Adrian la birou cu 0.9.0. Punctele 1–4 și 1b făcute. Acum: punctul 5, „totul așezat ca în programele cunoscute”:
  - **gata:** Sheets, PDF, Docs (D1–D7), Slides (L1–L7): file, grupuri, clic dreapta, scurtături și literele Alt ca în programele cunoscute;
  - **Imagini, nou în noaptea asta:**
    - **I1 gata:** sus nu mai e panglica, ci **meniurile** Fișier · Editare · Imagine · Strat · Text · Selectare · Filtru · Vizualizare · Fereastră · Ajutor;
      lista se deschide sub nume, cu **scurtătura scrisă în dreapta** fiecărei comenzi; mouse-ul trece de la un meniu la altul; Alt, apoi litera, deschide meniul;
    - **tastele uneltelor:** M marcaj (Shift+M elipsă), L lasou, W selecție rapidă, C decupare, J corectare, I pipetă, B pensulă, S clonare, E radieră,
      G degrade, O luminare, T text, U forme (Shift+litera trece la următoarea din grup);
    - **scurtăturile:** Ctrl+L Niveluri, Ctrl+M Curbe, Ctrl+U Nuanță/Saturație, Ctrl+B Balans de culoare, Ctrl+I Inversare, Ctrl+Shift+U Desaturare,
      Ctrl+T transformare liberă, Alt+Ctrl+I / Alt+Ctrl+C mărimea pozei / pânzei, Ctrl+] / Ctrl+[ ordinea straturilor.
- Toate aplicațiile pornesc fără erori; testele noi trec în aplicația reală (cu taste adevărate).

## Urmează
- Imagini: restul scurtăturilor (Q, Tab, 1…0, Ctrl+S direct), bara de unelte din stânga reordonată cu grupuri ◢, panourile Proprietăți / Ajustări; apoi Video, Notițe
  (după `INTERFATA-FAMILIARA.md`).
- Punctul 6: butonul „Trimite o observație” (captură + text salvate local, Adrian le trimite el).
- Kit de instalare nou doar când îl cere Adrian (întâi testează pe laptop, cu „Porneste Suite.cmd”).

## Ce oferă proiectul celorlalți
- Aplicațiile de birou pentru modulul Cyberspace (Kronos) și pentru setul de aplicații al Cyber Universe (după testarea umană).
- Fiecare aplicație e separată (`src/<modul>/`) și are `module.toml` după `standarde/modul-v0.md`.
- Cadrul comun de interfață (panglica cu file, modul „unelte”, **modul nou „meniuri”**, tastele de acces Alt, mini-bara, clic dreapta, panourile andocate),
  scurtăturile pe tastatura românească (`src/keys.ts`), motorul de formule (~500 de funcții), OCR în 5 limbi, criptarea, formularele și semnarea PDF, PDF/A,
  67 de filtre de imagine, cititorii și scriitorii .docx / .xlsx / .pptx / .pdf / .odt / .rtf / .psd.

## De ce are nevoie de la ceilalți
- Nimic acum.

## Blocaje / nevoie de Adrian
- De încercat (nu blochează): Imagini: clic pe „Imagine” sus → se deschide lista; apasă M și trage un dreptunghi; Ctrl+I inversează culorile, Ctrl+Z le readuce. E ca la editorul foto cunoscut?
- De încercat (nu blochează): Slides: clic pe un tabel → sus „Proiectare tabel” și „Aspect”; Proiectare → tema „Noapte”; Tranziții → Împingere → Opțiuni efect.
- De încercat (nu blochează): Docs: clic într-un tabel → „Proiectare tabel” și „Aspect”; dublu clic deasupra primului rând → antetul direct pe pagină; Alt, H, 1 face aldin.
- De încercat (nu blochează): Sheets și PDF așezate ca la birou; PDF → Editare → ✎ Editează text pe un act real; un .xlsx cu tabel făcut în Suite, deschis la birou.
- De verificat (nu blochează): .xlsx cu Rezolvitor, fișiere cu parolă și .docx protejat din Suite, deschise în programele de la serviciu;
  un cod QR din Suite scanat cu telefonul; un PDF „Fă-l PDF/A” trecut printr-un validator oficial; Slides pe un al doilea monitor.
- Întrebare (nu blochează): marcajul de timp la semnarea PDF cere un server de timp pe internet (se trimite doar amprenta documentului).
  Îl adăugăm ca opțiune, cu un server ales de Adrian? Până atunci semnăturile au ora calculatorului.
- Codul e doar local, pe laptop; pus pe GitHub doar dacă Adrian decide.
