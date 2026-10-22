# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-22 19:00 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- O singură aplicație desktop (Electron + React + TypeScript), scrisă de la zero, totul local, fără cont și fără internet:
  Docs, Sheets, PDF, Slides, Imagini, Video, Notițe. Interfața e în română.
- Etapa 1 (compatibilitate) e gata: 529 de fișiere reale de test, 0 erori la deschidere. Etapa 2 (toate funcțiile) e în lucru.
  Scoruri: Word 80,1%, Excel 79,8%, Clipchamp 77,1%, PowerPoint 76,2%, Notițe 76,4%, Acrobat 73,2%, Photoshop 72,0%, formule 97,1%.
- Prima prioritate: problemele găsite de Adrian la birou cu 0.9.0. Punctele 1–4 și 1b făcute (deschiderea din Windows, inclusiv clipuri și sunete, sugestii de funcții,
  Inserare → Tabel, editarea textului și a imaginilor în PDF). Acum: punctul 5, „totul așezat ca în programele cunoscute”:
  - gata mai devreme: Ctrl+K = Legătură, Alt+Q caută comenzi, scurtăturile pe tastatura românească, tastele de acces Alt, butonul mare „Lipire”;
  - **Sheets e gata la capitolul acesta (S1–S17, azi 15:35–18:40)**: toate filele (Pornire, Inserare, Aspect pagină, Formule, Date, Revizuire,
    Vizualizare, Proiectare tabel / diagramă) așezate ca în programul de tabele cunoscut; clic dreapta pe celulă, rând / coloană și fila foii;
    mini-bara pe două rânduri; scurtăturile (Ctrl+Shift+$ / %, F4, Shift+F3, F12, Ctrl+ț, Ctrl+A în doi pași, Backspace, Alt+F1, Shift+F11…);
    literele Alt verificate pe toate filele;
  - **PDF, început (18:45–19:00)**: scurtăturile cunoscute (Ctrl+0 pagina întreagă, Ctrl+1 mărime reală, Ctrl+2 lățime, Ctrl+H mod citire,
    Ctrl+L, Ctrl+Shift+N, Ctrl+D, Ctrl+Shift+I / D / R) și Refacere (Ctrl+Y).
- Toate aplicațiile pornesc fără erori; testele noi trec în aplicația reală (cu taste adevărate).

## Urmează
- Punctul 5, mai departe: PDF P1–P2 (bara globală Toate uneltele · Editare · Conversie · Semnătură, fără panglică, cu panoul de unelte
  în stânga), Ctrl+S peste fișier în PDF; apoi Docs, Slides, Imagini, Video, Notițe, după `INTERFATA-FAMILIARA.md`.
- Punctul 6: butonul „Trimite o observație” (captură + text salvate local, Adrian le trimite el).
- Kit de instalare nou doar când îl cere Adrian (întâi testează pe laptop, cu „Porneste Suite.cmd”).

## Ce oferă proiectul celorlalți
- Aplicațiile de birou pentru modulul Cyberspace (Kronos) și pentru setul de aplicații al Cyber Universe (după testarea umană).
- Fiecare aplicație e separată (`src/<modul>/`) și are `module.toml` după `standarde/modul-v0.md`.
- Cadrul comun de interfață (panglica cu file, tastele de acces Alt, mini-bara, clic dreapta, panourile andocate), potrivirea scurtăturilor
  pe tastatura românească (`src/keys.ts`), motorul de formule (~500 de funcții), sinonime și despărțire în silabe în română, OCR în 5 limbi,
  criptarea, formularele și semnarea PDF, PDF/A, 67 de filtre de imagine, cititorii și scriitorii .docx / .xlsx / .pptx / .pdf / .odt / .rtf / .psd.

## De ce are nevoie de la ceilalți
- Nimic acum.

## Blocaje / nevoie de Adrian
- De încercat (nu blochează): Sheets e așezat ca la birou (toate filele, clic dreapta, mini-bara, Ctrl+A de două ori, Alt, H, V = Lipire, Ctrl+ș = data);
  PDF: Ctrl+0 / Ctrl+2 / Ctrl+H. Se găsește totul unde te aștepți? Ce lipsește cel mai tare?
- De încercat (nu blochează): PDF → Editare → ✎ Editează text pe un act real: schimbi un cuvânt, salvezi; se vede bine la birou?
- De încercat (nu blochează): un .xlsx cu tabel (Inserare → Tabel) sau cu forme făcut în Suite, deschis la birou: merge fără „reparare”?
- De verificat (nu blochează): .xlsx cu Rezolvitor, fișiere cu parolă și .docx protejat din Suite, deschise în programele de la serviciu;
  un cod QR din Suite scanat cu telefonul; un PDF „Fă-l PDF/A” trecut printr-un validator oficial; Slides pe un al doilea monitor.
- Întrebare (nu blochează): marcajul de timp la semnarea PDF cere un server de timp pe internet (se trimite doar amprenta documentului).
  Îl adăugăm ca opțiune, cu un server ales de Adrian? Până atunci semnăturile au ora calculatorului.
- Codul e doar local, pe laptop; pus pe GitHub doar dacă Adrian decide.
