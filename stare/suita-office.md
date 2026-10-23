# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-23 17:20 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- O singură aplicație desktop (Electron + React + TypeScript), scrisă de la zero, totul local, fără cont și fără internet:
  Docs, Sheets, PDF, Slides, Imagini, Video, Notițe. Interfața e în română sau engleză (butoanele RO / EN).
- Etapa 1 (compatibilitate) e gata: 529 de fișiere reale de test, 0 erori la deschidere. Etapa 2 (toate funcțiile) e în lucru.
  Scoruri: Word 80,3%, Excel 79,8%, Clipchamp 77,1%, PowerPoint 76,2%, Notițe 76,4%, Acrobat 73,2%, Photoshop 72,0%, formule 97,1%.
- **Meniul în engleză (b) e gata:** și mesajele de eroare ale cititorilor de fișiere sunt traduse; un test nou trece prin toate aplicațiile și
  toate filele: 0 texte românești rămase.
- **Kitul de test (c2) e pregătit:** lista licențelor bibliotecilor (LICENTE-TERTI.txt, 150 de biblioteci, toate cu licențe permise),
  licența de test (LICENTA.txt, cu pagina „Sunt de acord” în instalare), limita de 30 de zile (anunț cu 5 zile înainte, apoi mesaj cu contactul),
  fereastra „ⓘ Despre”, numele „Office Suite Test”, siguranțele Electron, fără depanare în kit și codul ofuscat (testat: aplicația merge la fel).
- Toate aplicațiile pornesc fără erori; testele de limbă, cdp-about, cdp-tabs și cdp-all trec.

## Urmează
- c) Construirea kitului 0.9.1 „Office Suite Test” (întâi o variantă internă testată automat, apoi cea finală), d) testarea lui.
- Nimic pe stick fără „da”-ul lui Adrian.

## Ce oferă proiectul celorlalți
- Aplicațiile de birou pentru modulul Cyberspace (Kronos) și pentru setul de aplicații al Cyber Universe (după testarea umană).
- Fiecare aplicație e separată (`src/<modul>/`) și are `module.toml` după `standarde/modul-v0.md`.
- Cadrul comun de interfață (panglica, profilurile de meniu, tastele Alt, clic dreapta), traducerea pe loc RO / EN, motorul de formule (~500 de funcții),
  OCR în 5 limbi, criptarea, formularele și semnarea PDF, cititorii și scriitorii .docx / .xlsx / .pptx / .pdf / .odt / .rtf / .psd.
- Rețeta de kit protejat (licență de test cu expirare, ofuscare, siguranțe Electron) poate fi refolosită de alte proiecte cu aplicații desktop.

## De ce are nevoie de la ceilalți
- Nimic acum.

## Blocaje / nevoie de Adrian
- **De citit:** `suite/release/LICENTA.txt` (licența de test, în română). Spune dacă vrei altă formulare înainte de kit.
- **De privit:** capturile „PDF profil 23.10 …”, „Meniuri clasice 23.10 …”, „Aerisit 23.10 …”, „Simplu 23.10 …” din workspace: care aranjare îți place.
- De încercat (nu blochează): jos în stânga **EN** → orice aplicație; **ⓘ Despre** arată versiunea și licențele.
- De verificat (nu blochează): .xlsx cu Rezolvitor și fișiere cu parolă din Suite, deschise în programele de la serviciu; un cod QR scanat cu telefonul.
- Întrebare (nu blochează): marcajul de timp la semnarea PDF cere un server de timp pe internet. Îl adăugăm ca opțiune?
- Semnătura digitală a kitului (fără avertismentul albastru Windows) cere un certificat plătit: nu cumpărăm nimic fără decizia lui Adrian.
- Codul e doar local, pe laptop; pus pe GitHub doar dacă Adrian decide.
