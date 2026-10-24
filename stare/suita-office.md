# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-24 04:43 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- O singură aplicație desktop (Electron + React + TypeScript), scrisă de la zero, totul local, fără cont și fără internet:
  Docs, Sheets, PDF, Slides, Imagini, Video, Notițe. Interfața e în română sau engleză (butoanele RO / EN).
- Etapa 1 (compatibilitate) e gata: 529 de fișiere reale de test, 0 erori la deschidere. Etapa 2 (toate funcțiile) e în lucru.
  Scoruri: Word 81,7%, Excel 81,1%, PowerPoint 79,9%, Clipchamp 77,1%, Notițe 76,4%, Acrobat 74,0%, Photoshop 72,8%, formule 97,1%.
- Nou în această sesiune: în PDF, **imaginile din pagină se decupează** (✂, chenar cu 8 mânere); în Slides, **◇ În formă** la desen (cercul, dreptunghiul,
  linia și triunghiul trase de mână devin forme adevărate); în Sheets, **Totaluri generale** la Rezumat (pivot); în Imagini, **traseul liber** (〰 Liber). Engleza verificată (0 netraduse).
- **Kitul de test 0.9.1 „Office Suite Test”** e construit și testat (`Office-Suite-Test-Instalare-0.9.1.exe`, 98,9 MB, în workspace).
  Neschimbat în această sesiune; ce s-a făcut după el se vede pe laptop cu `Porneste Suite.cmd`.

## Urmează
- Sheets: graficele noi direct pe foaie (cu refacerea testelor lor); Docs: secțiuni; Imagini și Slides: alte funcții lipsă din inventar.
- PDF: fonturi cu serife cu diacritice la editarea textului; Slides: aspectele (layout-urile) în coordonator; Docs: fila Desenare.
- Kitul așteaptă „da”-ul lui Adrian (instalare pe un PC de test / copiere pe stick). Nimic pe stick fără acordul lui.

## Ce oferă proiectul celorlalți
- Nimic nou acum. Mai târziu (după testarea de către oameni): motorul de calcul și citirea documentelor (PDF / .docx → text).

## De ce are nevoie de la ceilalți
- Nimic.

## Blocaje / nevoie de Adrian
- **„Da” pentru kitul 0.9.1:** îl instalezi tu (pe laptop sau pe PC-ul de la birou) și/sau îl copiem pe stick?
  Instalarea n-am făcut-o eu, pentru că scrie în afara dosarului proiectului. Windows poate arăta avertismentul albastru
  (kitul nu e semnat): „Mai multe informații” → „Rulează oricum”.
