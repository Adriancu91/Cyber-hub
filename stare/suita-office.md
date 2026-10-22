# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-22 15:41 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- O singură aplicație desktop (Electron + React + TypeScript), scrisă de la zero, totul local, fără cont și fără internet:
  Docs, Sheets, PDF, Slides, Imagini, Video, Notițe. Interfața e în română.
- Etapa 1 (compatibilitate) e gata: 529 de fișiere reale de test, 0 erori la deschidere. Etapa 2 (toate funcțiile) e în lucru.
  Scoruri: Word 80,1%, Excel 79,8%, Clipchamp 77,1%, PowerPoint 76,2%, Notițe 76,4%, Acrobat 73,2%, Photoshop 72,0%, formule 97,1%.
- Prima prioritate: problemele găsite de Adrian la birou cu 0.9.0. Punctele 1–4 făcute (deschiderea din Windows, sugestii de funcții,
  Inserare → Tabel, editarea textului și a imaginilor în PDF). Sesiunea 14:52–15:41 a lucrat la punctul 5, „totul așezat ca în
  programele cunoscute”:
  - scurtăturile: Ctrl+K = Legătură (Docs, Sheets, Slides, Notițe), căutarea de comenzi pe Alt+Q / Ctrl+Shift+P, Ctrl+T = Tabel în Sheets,
    tab nou pe Ctrl+Alt+T; scurtăturile merg și pe tastatura românească (Ctrl+ș = Ctrl+;); Ctrl+; data și Ctrl+Shift+: ora în Sheets;
  - tastele de acces: Alt (sau F10) arată litere pe file și butoane, ca în programele cunoscute (Alt, H, V…);
  - butonul mare „Lipire” și grupul Clipboard comun (Sheets, Docs, Slides); Sheets → Pornire are grupurile în ordinea cunoscută,
    grupul nou Celule (Inserare / Ștergere / Format) și grupul Număr (stil procent, stil virgulă, zecimale).
- Toate aplicațiile pornesc fără erori; testele noi trec în aplicația reală (cu taste adevărate).

## Urmează
- Punctul 5, mai departe: Sheets (Font și Aliniere pe două rânduri, Stiluri, Editare, celelalte file), apoi PDF, Docs, Slides,
  Imagini, Video, Notițe, după `INTERFATA-FAMILIARA.md`.
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
- De încercat (nu blochează): în Sheets / Docs apasă și lasă Alt: apar literele pe file și butoane? Alt, H, V deschide Lipire? Panglica
  nouă (Lipire mare în stânga, grupul Celule, grupul Număr) e mai ușor de folosit? Ce lipsește cel mai tare față de programul de la birou?
- De încercat (nu blochează): Ctrl+K pune legătură, Alt+Q caută o comandă, Ctrl+T în Sheets face tabel, Ctrl+ș pune data de azi.
- De încercat (nu blochează): PDF → Editare → ✎ Editează text pe un act real: schimbi un cuvânt, salvezi; se vede bine la birou?
- De încercat (nu blochează): un .xlsx cu tabel (Inserare → Tabel) sau cu forme făcut în Suite, deschis la birou: merge fără „reparare”?
- De verificat (nu blochează): .xlsx cu Rezolvitor, fișiere cu parolă și .docx protejat din Suite, deschise în programele de la serviciu;
  un cod QR din Suite scanat cu telefonul; un PDF „Fă-l PDF/A” trecut printr-un validator oficial; Slides pe un al doilea monitor.
- Întrebare (nu blochează): marcajul de timp la semnarea PDF cere un server de timp pe internet (se trimite doar amprenta documentului).
  Îl adăugăm ca opțiune, cu un server ales de Adrian? Până atunci semnăturile au ora calculatorului.
- Codul e doar local, pe laptop; pus pe GitHub doar dacă Adrian decide.
