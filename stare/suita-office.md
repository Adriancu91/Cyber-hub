# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-23 00:42 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- O singură aplicație desktop (Electron + React + TypeScript), scrisă de la zero, totul local, fără cont și fără internet:
  Docs, Sheets, PDF, Slides, Imagini, Video, Notițe. Interfața e în română.
- Etapa 1 (compatibilitate) e gata: 529 de fișiere reale de test, 0 erori la deschidere. Etapa 2 (toate funcțiile) e în lucru.
  Scoruri: Word 80,3%, Excel 79,8%, Clipchamp 77,1%, PowerPoint 76,2%, Notițe 76,4%, Acrobat 73,2%, Photoshop 72,0%, formule 97,1%.
- Prima prioritate: problemele găsite de Adrian la birou cu 0.9.0. Punctele 1–4 și 1b făcute. Acum: punctul 5, „totul așezat ca în programele cunoscute”:
  - **gata:** Sheets (toate filele, clic dreapta, mini-bara, scurtăturile, literele Alt), PDF (bara de sus, Toate uneltele, bara rapidă, panourile din dreapta, ecranul de start, Ctrl+S peste fișier);
  - **Docs gata azi (D1–D7):** Pornire, scurtăturile, Inserare, Proiectare, Aspect cu Aranjare, Referințe, Corespondență, Revizuire, Vizualizare, Format imagine;
    **nou în seara asta:** filele de tabel **Proiectare tabel + Aspect** (Inserare deasupra / dedesubt, Ștergere ▾, Îmbinare, Dimensiune celulă, Date);
    fila **Antet și subsol** cu editare **direct pe pagină la dublu clic** în marginea de sus / de jos (Dată, Nume fișier, Prima pagină diferită, Esc închide);
    **literele Alt** cunoscute pe Pornire (Alt, H, 1 = aldin; Alt, H, A, C = centrare…);
  - **Slides (L1–L3 gata, L4 început):** Pornire cu **Font și Paragraf**, **＋ Diapozitiv nou ▾** (cu Duplicare), galeria **Aspect ▾**, **Reinițializare**;
    fila **Expunere diapozitive**; Vizualizare cu Sortare diapozitive, Pagină de note, Vizualizare citire; „Ștergere / Ascundere diapozitiv”;
    **scurtăturile cunoscute**: Ctrl+] / Ctrl+[ font, Ctrl+L / E / R / J aliniere, Shift+F3 litere, Ctrl+Space golire formatare,
    Ctrl+Shift+= / Ctrl+= **exponent / indice** (nou, păstrate și în .pptx), F12 Salvare ca;
    **Inserare** în ordinea cunoscută (Diapozitive · Tabele · Imagini · Ilustrații · Linkuri · Comentarii · Text · Simboluri · Media).
- Toate aplicațiile pornesc fără erori; testele noi trec în aplicația reală (cu taste adevărate).

## Urmează
- Punctul 5, mai departe: restul Slides (Proiectare cu galeria Teme și panoul Formatare fundal, Tranziții / Animații), apoi Imagini, Video, Notițe,
  după `INTERFATA-FAMILIARA.md`.
- Punctul 6: butonul „Trimite o observație” (captură + text salvate local, Adrian le trimite el).
- Kit de instalare nou doar când îl cere Adrian (întâi testează pe laptop, cu „Porneste Suite.cmd”).

## Ce oferă proiectul celorlalți
- Aplicațiile de birou pentru modulul Cyberspace (Kronos) și pentru setul de aplicații al Cyber Universe (după testarea umană).
- Fiecare aplicație e separată (`src/<modul>/`) și are `module.toml` după `standarde/modul-v0.md`.
- Cadrul comun de interfață (panglica cu file și file contextuale, modul „unelte”, tastele de acces Alt, mini-bara, clic dreapta, panourile andocate),
  scurtăturile pe tastatura românească (`src/keys.ts`), motorul de formule (~500 de funcții), sinonime și despărțire în silabe în română, OCR în 5 limbi,
  criptarea, formularele și semnarea PDF, PDF/A, 67 de filtre de imagine, cititorii și scriitorii .docx / .xlsx / .pptx / .pdf / .odt / .rtf / .psd.

## De ce are nevoie de la ceilalți
- Nimic acum.

## Blocaje / nevoie de Adrian
- De încercat (nu blochează): Slides: clic pe titlu → Ctrl+] mărește, Ctrl+E centrează; „x2” cu 2 selectat → Ctrl+Shift+= face x²
  (un .pptx cu x² făcut în Suite, deschis la birou: se vede bine?). Clic dreapta pe un diapozitiv din stânga → Duplicare diapozitiv.
- De încercat (nu blochează): Docs: clic într-un tabel → sus apar „Proiectare tabel” și „Aspect”; dublu clic deasupra primului rând → scrii antetul direct pe pagină;
  Alt, H, 1 face aldin. Slides: clic pe titlu → Pornire → Font → B. Se găsește totul unde te aștepți? Ce lipsește cel mai tare?
- De încercat (nu blochează): Sheets și PDF așezate ca la birou (Toate uneltele în stânga, panourile în dreapta, Ctrl+S peste PDF, Ctrl+A de două ori în Sheets).
- De încercat (nu blochează): PDF → Editare → ✎ Editează text pe un act real; un .xlsx cu tabel făcut în Suite, deschis la birou: merge fără „reparare”?
- De verificat (nu blochează): .xlsx cu Rezolvitor, fișiere cu parolă și .docx protejat din Suite, deschise în programele de la serviciu;
  un cod QR din Suite scanat cu telefonul; un PDF „Fă-l PDF/A” trecut printr-un validator oficial; Slides pe un al doilea monitor.
- Întrebare (nu blochează): marcajul de timp la semnarea PDF cere un server de timp pe internet (se trimite doar amprenta documentului).
  Îl adăugăm ca opțiune, cu un server ales de Adrian? Până atunci semnăturile au ora calculatorului.
- Codul e doar local, pe laptop; pus pe GitHub doar dacă Adrian decide.
