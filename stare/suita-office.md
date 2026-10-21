# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-21 06:36 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- O singură aplicație desktop (Electron + React + TypeScript), scrisă de la zero, totul local, fără cont și fără internet:
  Docs, Sheets, PDF, Slides, Imagini, Video, Notițe. Interfața e în română.
- Etapa 1 (compatibilitate) e gata: 529 de fișiere reale de test, 0 erori la deschidere (verificat din nou azi, la 06:35).
- Etapa 2 (toate funcțiile) e în lucru. Scoruri față de aplicațiile de referință: Clipchamp 74%, Notițe 73,2%, Word 73,0%,
  Excel 72,0%, PowerPoint 66,5%, Photoshop 63,7%, Acrobat 63,1%, formule de calcul 96%.
- Ultima sesiune (7 pași): Sheets — graficele „Soare” (inele pe niveluri) și bursier (lumânări); Docs — blocuri de text
  refolosibile (salvate cu nume, puse cu clic sau cu F3); Slides — 5 tranziții spectaculoase (și în .pptx); PDF — panoul
  Semnături (cine a semnat, certificatul, dacă fișierul s-a schimbat după semnare); Imagini — 4 filtre artistice
  (schiță în creion, decupaj, acuarelă, pânză) și Expunere cu decalaj și gamma.

## Urmează
- Restul funcțiilor din etapa 2 (PDF: editarea adevărată a textului existent, verificarea criptografică a semnăturilor;
  Docs: secțiuni și citirea numerotărilor din .docx; Slides: mai multe animații pe același obiect).
- Etapa 3, calitate: viteză, stabilitate, memorie pe 8 GB, teste automate pentru fiecare modul.
- Etapa 5: pachet de instalare pentru Windows și testare cu colegii lui Adrian, cu formular de raportare.

## Ce oferă proiectul celorlalți
- Aplicațiile de birou pentru modulul Cyberspace (Kronos) și pentru setul de aplicații al Cyber Universe (după testarea umană).
- Fiecare aplicație e separată (`src/<modul>/`) și are `module.toml` după `standarde/modul-v0.md`.
- Motorul de formule (~500 de funcții, cu nume românești), analizele „ce-ar fi dacă”, criptarea și formularele PDF, cititorul
  de semnături PDF (cu certificatul din PKCS #7), compararea vizuală a PDF-urilor, graficele desenate ca SVG (inclusiv
  statistice, cascadă, pâlnie, hartă de suprafețe, soare, bursier), citările și bibliografia, cititorul EXIF, filtrele de imagine,
  cititorii și scriitorii .rtf / .txt / .ods / .gif animat, importul/exportul .docx/.xlsx/.pptx/.pdf/.odt/.psd pot fi refolosite.

## De ce are nevoie de la ceilalți
- Nimic acum.

## Blocaje / nevoie de Adrian
- Niciunul. Codul e doar local, pe laptop; pus pe GitHub doar dacă Adrian decide.
