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
  4a. Testul 2 e deja făcut în mare parte (22:19): `lspci`, `lsusb`, `mem` — vezi punctul 5 din REZULTAT.md, cu pozele 05 și 06.
     Laptopul e AMD Ryzen (Renoir); rețea cu fir Realtek 10ec:8168, Wi-Fi Intel 8086:2723 (AX200), NVMe Samsung 144d:a809, USB xHCI AMD 1022:1639
     (stick-ul ADATA 125f:db8a e văzut). Rămân de verificat doar: `ls /disk`, `ls /usb`, consola Esc, tastatură USB externă.
  4b. Placa de rețea NU e văzută pe acest laptop (de așteptat: driver doar pentru e1000/e1000e). La testul 2, prima poză cerută
     e `lspci`, ca să ai identificatorul plăcii (8086:xxxx) și să poți planifica driverul după specificația publică Intel; Wi-Fi rămâne mai târziu.
  5. Faza 5 rămâne cum e (P5-07/P5-08 după suită); P3-10 (închiderea Fazei 3) se face după testul 2. Continuă apoi cu sarcinile libere.
- stare: gata (preluat 2026-10-21 22:50, sesiunea OS; terminat 23:20) — P3-09 + P3-11 în docs/TASKS.md
- rezultat: OS deblocat; HARDWARE.md, USB.md (varianta FAT32, Secure Boot) și BLOCKERS.md (B-001 rezolvat) completate; comanda nouă `hw` arată tot hardware-ul pe o pagină; lista pentru testul 2 e în `stare/cyber-universe.md`.

### C-3 · cyber-universe · Faza 6: OS-ul ca loc de lucru cu Claude înăuntru
- data: 2026-10-21 22:25 · de la: Adrian (prin centrul de comandă)
- ce: Direcția e în `DECIZII.md` (22:25). După C-2: închide Faza 5 fără P5-07/P5-08 (le muți într-o fază ulterioară, după suită) și
  planifică Faza 6 în `docs/ROADMAP.md` + `docs/TASKS.md` + planuri în `docs/plans/`, în ordinea asta, cu sarcini mici și testabile în QEMU
  unde se poate: (1) driver Realtek RTL8168/8111 (`10ec:8168`) — specificație din documentația publică Realtek/OSDev, clean-room, cu scenariu
  QEMU (`-device rtl8139` nu e același cip; dacă QEMU n-are RTL8168, testezi inițializarea cu un model minimal și restul pe laptopul real,
  prin testele lui Adrian); (2) rădăcinile de încredere reale (lista Mozilla, licența MPL 2.0 e permisă ca date; notează sursa) + `fetch https://`
  cu un site real; (3) aplicația „Claude”: client pentru API-ul Claude (JSON peste HTTPS, parser JSON propriu), cheia API citită dintr-un fișier
  de pe stick (`/usb/claude.key`, niciodată în repo), chat în fereastră, și unelte pe care Claude le poate cere: citește/scrie fișier, listează
  dosar, rulează comandă din shell — cu confirmarea lui Adrian pe ecran pentru scriere/rulare; (4) auto-actualizare: comanda/butonul
  „Actualizează” descarcă prin HTTPS ultima imagine `stick-usb` publicată (preferă un GitHub Release creat de CI, nu artefactul, ca să nu ceară
  autentificare) și rescrie fișierele de pe stick, cu verificare de sumă; (5) trimitere pe GitHub din OS (API `contents`, cu token din fișier).
  Compilarea OS-ului în interiorul OS-ului NU e obiectiv. Wi-Fi: nu acum. Scrie planul, apoi începe cu (1). Raportează lui Adrian ce are de
  pregătit pe laptop pentru fiecare pas (cablu de rețea, fișierul cu cheia, token GitHub).
- stare: preluat (2026-10-21 23:00, sesiunea OS) — Faza 6 = P6-01 … P6-10 în docs/TASKS.md, planuri în docs/plans/
- rezultat: în lucru — Faza 5 închisă, Faza 6 planificată (ROADMAP, TASKS, 10 planuri, D-012); pasul (1) driverul Realtek RTL8168 e scris și testat față de un model al cipului (de confirmat pe laptop); urmează (2) rădăcinile reale de încredere.

### C-4 · cyber-universe · Testul 2 pe laptopul Lenovo: rezultate + două reparații
- data: 2026-10-22 00:15 · de la: Adrian (prin centrul de comandă)
- ce: Testul 2 e făcut; totul e în `rezultate/2026-10-22-test-2/REZULTAT.md` (6 poze). Pe scurt: pornire 15 s; `hw` merge; **NVMe merge pe
  hardware real** (`/disk` montat, `ls /disk` arată partiția EFI a laptopului); xHCI merge (stick-ul e enumerat); **driverul Realtek pornește,
  citește MAC-ul real 38:f3:ab:6b:11:34 și trimite 4 pachete, dar primește 0** — ledul mufei e aprins (link up), deci recepția e problema
  driverului (inel RX / întreruperi sau polling / RxConfig / stare link); DHCP eșuează și OS-ul rămâne pe adresele implicite din QEMU
  (10.0.2.15), `ping 1.1.1.1` fără răspuns. **`/usb` nemontat** deși stick-ul e enumerat: stick-ul e formatat în Windows (MBR / superfloppy,
  fără GPT). Ce să faci, înaintea restului Fazei 6 (sunt condiții pentru P6-02 și tot ce urmează):
  1. **P6-01b — recepția Realtek:** verifică pe modelul tău al cipului și după documentație: inelul RX (descriptori, OWN bits, dimensiunea
     bufferelor), activarea RX în CR, RxConfig (accept broadcast + MAC propriu + multicast), IMR/ISR (întreruperi) sau polling, starea legăturii
     (PHYstatus) și dacă pachetele „trimise” chiar ies (TX descriptors OWN cleared). Adaugă în `net` rândul „legătură: da/nu, viteză” și
     contoare de erori RX. Scrie ce ai schimbat în raport.
  2. **P6-01c — montarea stick-ului:** suportă la montare și MBR cu o partiție FAT32 și „superfloppy” (FAT32 direct, fără tabelă), nu doar GPT;
     testează în QEMU cu o imagine formatată așa. Auto-actualizarea (P6-07/P6-08) va scrie pe exact un asemenea stick.
  3. **Jurnal vizibil:** o comandă `log` (ultimele N rânduri din jurnalul nucleului, cu filtrare după cuvânt, ex. `log rtl`), ca la testele pe
     hardware să se vadă ce zice driverul fără port serial. Și `net` să spună „fără adresă (DHCP fără răspuns)” în loc de adresele false din QEMU.
  4. Când 1–3 sunt în CI verde: scrie în `stare/cyber-universe.md` lista pentru **testul 3** (de ex. `log rtl`, `net`, `ping 1.1.1.1`,
     `host github.com`, `ls /usb`), ca Adrian să o facă dintr-o pornire.
- stare: preluat (2026-10-22 00:45, sesiunea OS pornită manual) — P6-01b, P6-01c, P6-01d în docs/TASKS.md; 1 și 2 deja în `1976997`
- rezultat:
