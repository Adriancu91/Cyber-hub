# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-22 18:08 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- O singură aplicație desktop (Electron + React + TypeScript), scrisă de la zero, totul local, fără cont și fără internet:
  Docs, Sheets, PDF, Slides, Imagini, Video, Notițe. Interfața e în română.
- Etapa 1 (compatibilitate) e gata: 529 de fișiere reale de test, 0 erori la deschidere. Etapa 2 (toate funcțiile) e în lucru.
  Scoruri: Word 80,1%, Excel 79,8%, Clipchamp 77,1%, PowerPoint 76,2%, Notițe 76,4%, Acrobat 73,2%, Photoshop 72,0%, formule 97,1%.
- Prima prioritate: problemele găsite de Adrian la birou cu 0.9.0. Punctele 1–4 și 1b făcute (deschiderea din Windows, inclusiv clipuri și sunete, sugestii de funcții,
  Inserare → Tabel, editarea textului și a imaginilor în PDF). Acum: punctul 5, „totul așezat ca în programele cunoscute”:
  - gata mai devreme: Ctrl+K = Legătură, căutarea de comenzi pe Alt+Q, Ctrl+T = Tabel în Sheets, scurtăturile pe tastatura românească,
    tastele de acces Alt, butonul mare „Lipire” și grupul Clipboard comun;
  - sesiunea 15:42–16:27: Sheets → fila Pornire așezată toată ca în programul de tabele cunoscut (Font, Aliniere, Număr, Stiluri,
    Celule, Editare) și scurtăturile de format (Ctrl+Shift+$ / % / !, Ctrl+1, F4 repetă formatarea);
  - sesiunea 16:37–17:25: **Sheets → Inserare, Aspect pagină și Formule** așezate la fel: Inserare (Tabele, Ilustrații, Controale, Diagrame,
    Minidiagrame, Filtre, Linkuri, Comentarii, Text, Simboluri), Aspect pagină (Margini ▾, Orientare ▾, Dimensiune ▾, Zonă de imprimare ▾,
    Întreruperi ▾, Scalare, Opțiuni foaie), Formule (Bibliotecă de funcții cu Utilizate recent, Nume definite, Audit formule, Calcul);
    Shift+F3 = Inserare funcție, F12 = Salvează ca; panglica încape fără derulare și pe ferestre înguste (800 px).
  - sesiunea 17:24–18:08: **Sheets → Date, Revizuire, Vizualizare** și filele contextuale **Proiectare tabel** / **Proiectare diagramă** așezate la fel
    (Sortare și filtrare cu Reaplicare / Complex, Validare date ▾, Analiză circumstanțială ▾, Grupare / Anulare grupare, Protejare foaie / registru,
    Înghețare panouri ▾ cu 3 variante, Statistici registru, Note anterioară / următoare); clic dreapta pe capul de rând / coloană ca în programul cunoscut.
- Toate aplicațiile pornesc fără erori; testele noi trec în aplicația reală (cu taste adevărate).

## Urmează
- Punctul 5, mai departe: Sheets, clic dreapta pe celulă și pe fila foii, mini-bara, scurtăturile partea 2, literele de acces exacte,
  fila Format a diagramei; apoi PDF, Docs, Slides, Imagini, Video, Notițe, după `INTERFATA-FAMILIARA.md`.
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
- De încercat (nu blochează): Sheets → toate filele (Pornire, Inserare, Aspect pagină, Formule, Date, Revizuire, Vizualizare) sunt acum așezate ca în programul de la birou (Font, Aliniere, Număr, Stiluri, Celule,
  Editare). Se găsește totul unde te aștepți? Ctrl+Shift+4 pune lei, Shift+F3 deschide funcțiile, F4 repetă formatarea? Alt, H, V deschide Lipire? Ce lipsește cel mai tare?
- De încercat (nu blochează): Ctrl+K pune legătură, Alt+Q caută o comandă, Ctrl+T în Sheets face tabel, Ctrl+ș pune data de azi.
- De încercat (nu blochează): PDF → Editare → ✎ Editează text pe un act real: schimbi un cuvânt, salvezi; se vede bine la birou?
- De încercat (nu blochează): un .xlsx cu tabel (Inserare → Tabel) sau cu forme făcut în Suite, deschis la birou: merge fără „reparare”?
- De verificat (nu blochează): .xlsx cu Rezolvitor, fișiere cu parolă și .docx protejat din Suite, deschise în programele de la serviciu;
  un cod QR din Suite scanat cu telefonul; un PDF „Fă-l PDF/A” trecut printr-un validator oficial; Slides pe un al doilea monitor.
- Întrebare (nu blochează): marcajul de timp la semnarea PDF cere un server de timp pe internet (se trimite doar amprenta documentului).
  Îl adăugăm ca opțiune, cu un server ales de Adrian? Până atunci semnăturile au ora calculatorului.
- Codul e doar local, pe laptop; pus pe GitHub doar dacă Adrian decide.
