# Stare: Suita office (`suita-office`)

**Actualizat:** 2026-10-23 19:01 (ora României) · **de:** sesiunea automată Claude Code de pe laptop (lucru continuu)

## Acum
- O singură aplicație desktop (Electron + React + TypeScript), scrisă de la zero, totul local, fără cont și fără internet:
  Docs, Sheets, PDF, Slides, Imagini, Video, Notițe. Interfața e în română sau engleză (butoanele RO / EN).
- Etapa 1 (compatibilitate) e gata: 529 de fișiere reale de test, 0 erori la deschidere. Etapa 2 (toate funcțiile) e în lucru.
  Scoruri: Word 80,3%, Excel 79,8%, Clipchamp 77,1%, PowerPoint 76,2%, Notițe 76,4%, Acrobat 73,4%, Photoshop 72,0%, formule 97,1%.
- Nou în această sesiune (în copia de lucru, după kit): textul editabil scos din scanări păstrează aldinul și cursivul;
  în PDF, „Editează text” scrie textul nou cu fontul original al documentului când se poate; poza → PDF pe foaie A4 / Letter;
  scurtături noi: Docs (Ctrl+0, Shift+F5, F4, Ctrl+Alt+P / O) și PDF (Ctrl+Shift+T = Decupează). Punctul „text din poze și scanări” e gata.
- **Kitul de test 0.9.1 „Office Suite Test” e construit și testat:** `Office-Suite-Test-Instalare-0.9.1.exe` (98,9 MB) în workspace,
  cu licența de test, limita de 30 de zile, fereastra „Despre”, codul ofuscat, fără depanare. Neschimbat în această sesiune.

## Urmează
- Kitul așteaptă „da”-ul lui Adrian (instalare pe un PC de test / copiere pe stick). Nimic pe stick fără acordul lui.
- În paralel: restul etapei 2 (scurtăturile rămase din Docs și Video, apoi funcțiile care lipsesc din inventar)
  și formularul de raportare pentru testeri.

## Ce oferă proiectul celorlalți
- Nimic nou acum. Mai târziu (după testarea de către oameni): motorul de calcul și citirea documentelor (PDF / .docx → text).

## De ce are nevoie de la ceilalți
- Nimic.

## Blocaje / nevoie de Adrian
- **„Da” pentru kitul 0.9.1:** îl instalezi tu (pe laptop sau pe PC-ul de la birou) și/sau îl copiem pe stick?
  Instalarea n-am făcut-o eu, pentru că scrie în afara dosarului proiectului. Windows poate arăta avertismentul albastru
  (kitul nu e semnat): „Mai multe informații” → „Rulează oricum”.
