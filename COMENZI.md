# Comenzile lui Adrian

Adrian îi spune lui Claude în chatul „centrul de comandă” ce vrea; Claude scrie comanda aici, cu data.
Fiecare agent citește la început comenzile pentru proiectul lui cu starea `nou` (regulile: `REGULI.md`, secțiunea „Comenzile”).

**Stări:** `nou` → `preluat` → `gata` · sau `blocat` / `întrebare` (agentul scrie de ce).
**Important:** o comandă se preia după ce agentul termină ce are în lucru. Nu oprește nimic pornit, decât dacă scrie „oprește acum”.

Format:

```
### C-<număr> · <id proiect> · <titlu scurt>
- data: AAAA-LL-ZZ HH:MM · de la: Adrian (prin centrul de comandă)
- ce: instrucțiunea exactă, pe înțeles
- stare: nou
- rezultat:
```

---

### C-1 · suita-office · Graficul de comparație, pus în hub
- data: 2026-10-20 19:45 · de la: Adrian (prin centrul de comandă)
- ce: Adrian vrea să vadă graficul de comparație al suitei (scorurile față de Word, Excel, PowerPoint, Acrobat, Photoshop, Clipchamp,
  Notițe, formule — și evoluția lor în timp, dacă o ții). Pune-l în hub, în fișierul tău `stare/suita-office-comparatie.md`:
  tabelul cu scorurile de acum (aplicație | scor | ce lipsește cel mai mult), evoluția pe zile dacă există, și o imagine a graficului
  (`stare/suita-office-comparatie.png`, dacă graficul există ca imagine sau îl poți exporta). Fără cod, fără date personale.
  Nu întrerupe pasul la care lucrezi; o faci la sfârșitul sesiunii curente, odată cu starea.
- stare: retras (2026-10-20 19:50) — Adrian cere graficul direct în chatul suitei; suita nu primește comenzi prin hub.
- rezultat: —

### C-2 · cyber-universe · Rezultatele primului test pe hardware real (P3-09 / B-001)
- data: 2026-10-21 22:15 · de la: Adrian (prin centrul de comandă)
- ce: Testul pe stick a fost făcut pe un laptop Lenovo ThinkPad (altul decât al suitei) și **a reușit**: cu Secure Boot oprit pornește
  până la desktop; ecran, touchpad, click, tastatură internă, fereastra Demo și Editorul merg. Rezultatul complet, cu 5 imagini:
  `rezultate/2026-10-21-test-stick/REZULTAT.md` din hub. Ce să faci, în ordinea asta:
  1. Ești deblocat: decizia din `DECIZII.md` (10:05) spunea „oprit până la testul pe stick”; testul s-a făcut. Șterge secțiunea „OPRIT” din `docs/STATE.md`.
  2. Completează `docs/HARDWARE.md` cu rândul acestui calculator (datele din REZULTAT.md; ce nu s-a verificat rămâne „—”) și închide
     B-001 în `docs/BLOCKERS.md` (mutat la „Rezolvate”, cu ce a mers și ce a rămas de verificat).
  3. Actualizează `docs/USB.md`: (a) pe Lenovo, cu Secure Boot pornit nu apare nicio eroare, doar revine la meniul de boot; (b) varianta
     fără Rufus/Etcher: stick formatat FAT32 + fișierele copiate în rădăcină (lista exactă), care a funcționat.
  4. Pregătește **testul 2** pentru Adrian: o listă scurtă, pe înțeles, cu ce să facă și ce să fotografieze (Start → terminal: `help`,
     `lspci`, `lsusb`, `mem`, `ls /disk`, `ls /usb`, `net`; Esc pentru consola text; tastatură USB externă dacă are). Dacă e util, adaugă o
     comandă `hw` sau un ecran „Raport hardware” care arată totul pe o singură pagină, ca o singură poză să ajungă. Scrie lista în
     `stare/cyber-universe.md` la „Blocaje / nevoie de Adrian” și în raportul tău.
  4b. Placa de rețea NU e văzută pe acest laptop (de așteptat: driver doar pentru e1000/e1000e). La testul 2, prima poză cerută
     e `lspci`, ca să ai identificatorul plăcii (8086:xxxx) și să poți planifica driverul după specificația publică Intel; Wi-Fi rămâne mai târziu.
  5. Faza 5 rămâne cum e (P5-07/P5-08 după suită); P3-10 (închiderea Fazei 3) se face după testul 2. Continuă apoi cu sarcinile libere.
- stare: nou
- rezultat:
