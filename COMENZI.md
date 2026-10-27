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
- rezultat: toți cei 5 pași sunt scriși și testați în emulator/CI (P6-01 … P6-09: Realtek, rădăcini Mozilla + HTTPS real, chatul Claude cu unelte confirmate, actualizare din Release, trimitere pe GitHub); rămâne P6-10 = testul pe laptop cu Adrian (de pregătit: cablu de rețea, `claude.key`, `github.token`, `cyber.rw` pe stick).

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
- stare: gata (preluat 2026-10-22 00:45, terminat 00:58, sesiunea OS pornită manual) — P6-01b, P6-01c, P6-01d; CI verde pe `f7a455f`
- rezultat: Realtek pornește acum PHY-ul, așteaptă legătura, șterge stările care opresc primirea și scrie în jurnal registrele citite înapoi; stick-urile formatate în Windows (MBR sau fără tabelă) se montează (test nou în QEMU); comanda `log` și `net` „fara adresa” există; lista pentru testul 3 e în `stare/cyber-universe.md`.

### C-5 · cyber-universe · Testul 3 făcut: recepția se oprește după 16 pachete; stick-ul nu trece de configurarea USB
- data: 2026-10-22 09:30 · de la: Adrian (prin centrul de comandă)
- ce: Testul 3 e făcut (Release os-120, cablu băgat); totul în `rezultate/2026-10-22-test-3/REZULTAT.md` (4 poze, textul transcris).
  Pe scurt: **Realtek primește acum** (16 pachete; la testul 2 erau 0), legătura 1000 Mbit/s full duplex e citită corect, TX merge
  (160 de DHCP Discover trimise) — dar **„primite” îngheață la 16** și nu mai crește deloc în 10 minute; `ISR vazut 40b5` conține **RDU
  (bit 4, Rx Descriptor Unavailable)**; `descriptor RX 0 = 80000800`; `revizia 50800000` (ESTIMARE: familia 8168H). DHCP nu primește
  niciodată Offer → fără adresă. **Stick-ul:** xHCI îl enumerează (`125f:db8a`, port 4), dar `hw` zice **„stick-ul nu porneste (configurare
  USB)”** → `/usb` nemontat; montarea MBR din C-4 nici n-a fost atinsă. Ce să faci, în ordinea asta (P6-10a, P6-10b în TASKS):
  1. **P6-10a — recepția după inel plin.** Ipoteza principală: inelul RX are 16 descriptori și după prima umplere placa nu mai primește
     niciunul. Verifică în cod, pe modelul tău și după documentația publică (OSDev / datasheet RTL8168 public): (a) după ce citești un
     cadru, pui la loc **OWN** (bit 31) + mărimea buffer-ului pe descriptor, cu scriere volatilă și bariera de memorie potrivită, înainte
     să treci mai departe; (b) **ultimul descriptor are EOR** (bit 30) pus și la re-armare, nu doar la inițializare; (c) inelele sunt
     aliniate la **256 de octeți**; (d) ce faci când vezi RDU — pe reviziile G/H verifică dacă trebuie o re-pornire a recepției (bitul RE
     din CR sau rescrierea RDSAR) după ce descriptorii sunt redați; (e) mărește inelul la 64 sau 256 (Linux folosește 256) — dacă după
     schimbare „primite” trece de mărimea inelului, cauza e confirmată. Adaugă în `net`: mărimea inelului, indexul curent, câți descriptori
     sunt OWN=1 acum, de câte ori s-a văzut RDU, și **ce erau primele cadre** (ethertype / UDP port 68 = DHCP Offer?), ca la testul 4 să
     vedem dintr-o poză dacă Offer-ul ajunge și e aruncat de parser sau nu ajunge deloc.
  2. **P6-10b — configurarea stick-ului pe xHCI real.** Află exact ce eșuează: scrie în jurnal (`log usb`) fiecare pas al enumerării cu
     codul de completare TRB (GET_DESCRIPTOR device/config, SET_ADDRESS, SET_CONFIGURATION, timeout/STALL). Verifică: Max Packet Size
     citit din descriptorul de dispozitiv înainte de cererile mari; viteza portului (stick USB 3 pe port USB 3 → endpoint context cu
     parametrii SuperSpeed); lungimea descriptorului de configurare citită în două cereri (9 octeți, apoi wTotalLength); timeout-ul
     cererilor (stick-urile reale răspund mai lent decât QEMU). Testează în QEMU cu `-device qemu-xhci -device usb-storage` (deja ai).
     Camera `04f2:b6be` pe același controler nu trebuie să blocheze enumerarea stick-ului.
     **Completare 09:40, din `log usb` (poza 5 din REZULTAT.md):** descriptorul de dispozitiv se citește (clasa 08:06:50), „viteza 3” în
     xHCI = **High-Speed (USB 2.0)**, nu SuperSpeed — deci nu e contextul SS; eșecul e la **180 ms** după identificare. Verifică ÎNTÂI:
     (a) **Unit Attention** după pornire: INQUIRY / TEST UNIT READY / READ CAPACITY pot răspunde cu CSW status 01 la prima încercare — fă
     REQUEST SENSE și reîncearcă (de ex. de 10 ori, cu 100 ms pauză), nu declara „nu porneste” la primul eșec; (b) timeout-ul comenzilor
     bulk și al „ready” (minimum 2 s în total, ca în Linux); (c) Max Packet Size 512 pentru bulk la High-Speed; (d) abia apoi descriptorul de
     configurare / SET_CONFIGURATION. În `log usb` scrie fiecare pas cu codul de completare TRB și, la SCSI, CSW status + Sense Key/ASC/ASCQ.
  3. Când 1–2 sunt în CI verde și e un Release nou: scrie în `stare/cyber-universe.md` lista pentru **testul 4** (aceleași comenzi + `log usb`
     + ce ai adăugat în `net`), ca Adrian să o facă dintr-o pornire. Nu cere încă `claude.key`/`github.token`: fără `/usb` n-au unde sta.
  4. Nu te opri singur după sesiuni goale cât timp C-5 e `preluat`.
- stare: gata (preluat 2026-10-22 06:30 UTC, terminat 07:40 UTC; completarea de la 09:40 făcută la 08:00 UTC) — P6-10a, P6-10b; CI verde, Release os-125
- rezultat: Realtek are coadă de primire de 256 și își repornește singur primirea după blocare (cu diagnostic nou în `net`), stick-ul e așteptat după ceas până la 5 s cu fiecare pas în `log usb`, INQUIRY reîncercat de 10 ori cu REQUEST SENSE (Unit Attention) și starea CSW + sense în jurnal; lista pentru testul 4 e în `stare/cyber-universe.md`.

### C-6 · cyber-universe · Testul 4 făcut: stick-ul merge, recepția nu se mai blochează, dar cadrele 2+ sunt citite ca zero (DHCP 0)
- data: 2026-10-22 14:35 · de la: Adrian (prin centrul de comandă)
- ce: Testul 4 (Release os-125, cablu băgat) e în `rezultate/2026-10-22-test-4/REZULTAT.md` (8 poze, text transcris). **P6-10b confirmat
  pe hardware**: stick-ul ADATA e enumerat, configurat, FAT32/MBR montat la `/usb` cu scriere permisă, `ls /usb` arată `cyber.rw`, `VERSIUNE`,
  `EFI/`, `boot/`. **P6-10a confirmat**: primite 24 → 32 în 6 minute, index 24 → 32, RDU 0, reporniri 0. **Rămâne un singur blocaj, nou și
  precis:** `primele cadre: 0806 0000 0000 0000 0000 0000 0000 0000` — primul cadru e citit corect (ARP), **cadrele 2–8 au ethertype 0000**,
  imposibil pe o rețea reală ⇒ driverul citește zerouri din buffer-ele pachetelor de la al doilea încolo; de aceea `raspunsuri DHCP (udp 68) 0`
  și fără adresă, deși trimise ajung la 120. Ce să faci (P6-10c), înaintea oricărui alt pas:
  1. Ipoteza principală: **adresele buffer-elor din descriptorii RX 1…255 nu corespund cu adresele din care citește driverul** (stride/bază
     diferite sau conversia fizic→virtual corectă doar pentru buffer-ul 0). **Completare 14:45 (pozele 9–11):** forma cea mai probabilă —
     buffer-ele alocate separat, iar adresa din descriptor calculată `baza + i × 2048` presupunând alocări contigue (adevărat în QEMU, fals pe
     laptop). Remediu: un singur bloc contiguu de 256 × 2048 octeți, aliniat, din care derivă și adresa fizică, și cea virtuală. Din `log dhcp`:
     18 cadre au venit în primele ~8 s (burst-ul cu Offer-ul routerului), apoi ~1 la 18 s; `log arp` nu are niciun rând (adaugă un rând la ARP). Verifică în cod: cum se calculează `buf_phys[i]` pus în descriptor
     și `buf_virt[i]` din care se citește; că sunt același bloc, același pas (RMS 2048), aceeași conversie. Apoi: (b) ordinea operațiilor —
     citești lungimea și datele ÎNAINTE de a re-arma OWN și nu golești buffer-ul înainte de citire; (c) indexul citit = indexul descriptorului
     cu OWN=0, fără off-by-one între placă și driver.
  2. Diagnostic pentru testul 5, ca să nu ghicim: în `net` (sau `log rx`), pentru fiecare din primele 8 cadre: index, lungimea din descriptor,
     adresa fizică din descriptor, adresa din care a citit driverul, primii 16 octeți în hex. Și un contor „cadre cu ethertype 0000”.
  3. Fă modelul de test al cipului din QEMU să scrie fiecare cadru în buffer-ul propriu al descriptorului (adresa din descriptor, nu un buffer
     comun) și adaugă un scenariu cu 8+ cadre consecutive, verificând ethertype-ul fiecăruia — ca regresia asta să fie prinsă în CI.
  4. Când CI e verde și e Release nou: lista pentru **testul 5** în `stare/cyber-universe.md` (`net`, `ping 1.1.1.1`, `host github.com`,
     `fetch https://example.com/`, și noul diagnostic). Dacă rețeaua merge la testul 5, în același mesaj spune-i lui Adrian ce să pună pe stick
     pentru pasul următor (`claude.key`, `github.token`) — abia atunci.
- stare: gata (preluat 2026-10-22 11:30 UTC, terminat 12:45 UTC, sesiunea OS) — P6-10c; CI verde, Release os-134
- rezultat: adresele și ordinea din driver erau corecte; cauza probabilă e cache-ul (placa scria cu „No Snoop”), așa că OS-ul oprește No Snoop și golește cache-ul la fiecare pachet primit/trimis, cu `log rx` pe pachet, `log arp` și test pe model cu 12 pachete la rând; lista pentru testul 5 e în `stare/cyber-universe.md`.

### C-7 · cyber-universe · Bucla de test de la distanță: laptopul se actualizează, se testează și raportează singur prin GitHub
- data: 2026-10-22 14:45 · de la: Adrian (prin centrul de comandă) — „da”, cu mențiunea: pornire automată de pe stick la repornire
- ce: După C-6 (abia când rețeaua merge pe laptop). Scopul: să nu mai fie nevoie de zip-uri trimise de mână și de poze; laptopul de test
  (cablu băgat, stick în el, BIOS-ul setat de Adrian să pornească primul de pe stick) devine un banc de test automat. Pași (P6-11 … în TASKS):
  1. **Auto-actualizare la pornire:** dacă `/usb` e montat și rețeaua are adresă, OS-ul compară `VERSIUNE` de pe stick cu ultimul Release;
     dacă e mai nou, descarcă, verifică sumele, scrie pe stick (codul „Actualizează” există) și **repornește singur** (comandă `reboot`:
     ACPI reset sau, ca rezervă, resetarea prin controlerul de tastatură 0xFE). Nimic nu se scrie pe stick dacă vreo sumă nu se potrivește.
  2. **Comenzi de test din repo:** fișierul `test/comenzi.txt` din `cyber-universe` (ramura `main`), un rând = o comandă din shell-ul OS.
     La pornire (după eventuala actualizare), OS-ul îl descarcă prin HTTPS, rulează comenzile una după alta cu limită de timp (de ex. 30 s
     fiecare) și adună ieșirea lor + `VERSIUNE` + `hw` + ultimele 50 de rânduri din jurnal.
  3. **Raport înapoi pe GitHub:** rezultatul se trimite cu `gh-trimite` la `test/rezultate/<data-ora>_<versiune>.txt` (tokenul din
     `/usb/github.token`, drepturi doar pe acest depozit). Fără token, rezultatul se scrie măcar pe stick, în `/usb/rezultate/`.
  4. **Sesiunea OS închide bucla:** la fiecare rulare citește ultimul fișier din `test/rezultate/`, îl tratează ca pe pozele lui Adrian (bug →
     reparație → Release), și rescrie `test/comenzi.txt` pentru runda următoare. În raportul pentru Adrian spune ce a citit din laptop.
  5. **Siguranță:** OS-ul rulează doar comenzi din propriul shell (nu cod descărcat), doar de pe `main` al depozitului `Adriancu91/cyber-universe`,
     numai prin HTTPS cu rădăcinile reale; tokenul și cheia nu apar niciodată în rezultate; un fișier `/usb/fara-auto.txt` oprește bucla.
  6. Scrie în `docs/USB.md` pașii pentru Adrian: ordinea de boot în BIOS (Lenovo: F1 la pornire → Startup → Boot → stick-ul primul; Secure Boot
     oprit), și cum pune `github.token` pe stick. Spune-i în raport când e gata de pornit bucla.
- stare: nou (se preia după C-6; dacă C-6 nu e gata, rămâne `nou`). **14:43: BIOS-ul laptopului e deja setat de Adrian — pornește direct de pe stick la repornire.** Pasul 6 rămâne doar pentru `github.token`.
- rezultat:

### C-8 · cyber-universe · Testul 5: REGRESIE (0 trimise, 0 primite) — întâi revenire la os-125, apoi diagnosticul adevărat
- data: 2026-10-22 16:35 · de la: Adrian (prin centrul de comandă)
- ce: Testul 5 (os-136) e în `rezultate/2026-10-22-test-5/REZULTAT.md` (5 poze). **Placa nu mai transferă nimic:** trimise 0, primite 0, index 0,
  ISR văzut doar 0020 (LinkChg), în 112 s; la testul 4 (os-125) erau 120 trimise / 32 primite. Și `PCIe No Snoop: oprit (era oprit)` → ipoteza
  No Snoop e **infirmată** (setarea era deja oprită). Ce să faci, în ordinea asta (P6-10d):
  0. **Completare 16:50, din `log rtl` (poza 6):** `PCIe Device Control 2010 -> 2000` = No Snoop era deja 0; scrierea a șters **Relaxed
     Ordering (bit 4)**. Și **RCR e `0000c70a` acum, față de `0002c70a` în os-125** (bitul 17 lipsă) — P6-10c n-a declarat nicio schimbare la
     RxConfig: află de ce diferă și readu valoarea exactă din os-125. Inelele sunt la aceleași adrese (RDSAR 3d8000, TNPDS 3d9000), sub 4 GB.
  1. **Revenire:** scoate din driver scrierile în configurarea PCI făcute la P6-10c (Device Control / No Snoop) și orice altă schimbare care
     poate opri DMA-ul; păstrează doar jurnalul pe cadru (`log rx`, `log arp`) și contoarele. Regulă de acum: **niciun registru de configurare
     PCI nu se scrie fără citire-modificare-scriere pe exact un bit, cu valoarea dinainte și de după scrisă în jurnal**; verifică explicit că
     bitul Bus Master din Command rămâne 1 (scrie-l în `log rtl`). Golirea cache-ului rămâne doar dacă nu atinge descriptorii înainte de re-armare.
  2. **Diagnosticul pentru cadrele citite ca zero, pe hardware, nu în cod:** în `log rx`, pentru fiecare din primele 8 cadre: index, lungimea
     din descriptor, **adresa fizică completă (64 de biți) din descriptor** (low + high), adresa virtuală din care citește driverul și adresa
     fizică corespunzătoare ei, primii 16 octeți. Plus în `log rtl`: adresa fizică a inelului (RDSAR low+high), a primelor 3 buffer-e, și
     cât RAM vede OS-ul și unde cad alocările (sub sau peste 4 GB).
  3. **Două ipoteze de testat prin construcție**, nu prin citire: (a) buffer-ele RX într-un singur bloc contiguu, alocat explicit **sub 4 GB**,
     cu adresa din descriptor derivată din același bloc; (b) scrierea corectă a jumătății de sus a adresei (bits 63:32) în descriptor și în
     RDSAR/TNPDS. Dacă după (a)+(b) „cadre cu tip 0000” e 0 și DHCP primește Offer, cauza e confirmată.
  4. În QEMU: rulează scenariul de rețea cu **memorie ≥ 6 GB** (`-m 6G`) și alocările forțate peste 4 GB, ca să reproduci cazul; adaugă-l în CI.
  5. Când CI e verde și e Release nou: lista pentru **testul 6** în `stare/cyber-universe.md`. Nu cere încă `github.token`.
  6. **Completare 16:45 (Adrian): studiază driverele open-source pentru RTL8168 înainte să scrii** — permis de `CLAUDE.md` §6 și de decizia
     din 20 oct (citit pentru idei, niciodată copiat; sursa de inspirație notată în README-ul modulului `rtl8168/`). De preferat cele cu licență
     permisivă: **SerenityOS** (`Kernel/Net/Realtek/RTL8168NetworkAdapter.cpp`, BSD-2), **FreeBSD `re(4)`** (`sys/dev/re/if_re.c`, BSD),
     **Haiku** (rtl8169/8168, MIT); Linux `r8169_main.c` (GPL) doar pentru înțelegere, cu grijă. Ce să urmărești acolo: cum scriu adresele pe
     64 de biți în descriptori și în RDSAR/TNPDS; cum aloc memoria DMA (bloc contiguu, aliniat); **inițializarea specifică reviziilor 8168G/H**
     (revizia noastră 0x50800000): bitul RXDV_GATED_EN din MISC (trebuie oprit), RX_MULTI_EN / RX_EARLY_OFF în RxConfig, MaxTxPacketSize,
     scrierile ERI/OCP, oprirea DASH; și ce fac după RDU. Scrie în raport, pe scurt, ce concluzii ai tras și ce ai aplicat în codul nostru.
  7. **Regulă permanentă (Adrian, 16:55; e și în `DECIZII.md`):** de acum, la driverele testate pe hardware, o singură schimbare de comportament
     pe Release, verificată pe laptop înainte de următoarea; registrele se scriu doar citire → un bit → scriere, cu valorile în jurnal; `log rtl`
     arată registrele cheie la fiecare versiune; „confirmat” înseamnă confirmat pe laptop. Scrie regula și în `docs/DECISIONS.md` al OS-ului.
- stare: gata (preluat 2026-10-22 13:40 UTC, terminat 14:30 UTC, sesiunea OS) — P6-10d; CI verde, Release os-138
- rezultat: pornirea plăcii e iar exact ca în os-125 (fără Device Control, fără golirea cache-ului), PCI scris doar bit cu bit în jurnal, iar schimbările noi (poarta RXDV de la 8168G — din studiul FreeBSD, bufferele într-un bloc sub 4 GB, golirea cache-ului) se încearcă pe rând cu `rtl porneste ...`, cu adrese pe 64 de biți în `log rtl`/`log rx`; lista pentru testul 6 e în `stare/cyber-universe.md`.

### C-9 · cyber-universe · Cauza găsită: driverul nu inițializează cipul la pornirea de la rece; cadrele 2+ tot zero la cald
- data: 2026-10-22 18:05 · de la: Adrian (prin centrul de comandă)
- ce: Testul 6, pas cu pas, e în `rezultate/2026-10-22-test-6/REZULTAT.md` (7 poze, tabel). **Concluzia:** os-125 pornit direct de pe stick
  (de la rece) = 0/0; același os-125 pornit din meniul F12 = 17 trimise / 23 primite. Firmware-ul UEFI, când afișează meniul, pornește placa
  și o lasă inițializată; direct, nu. Deci **nu a fost regresie** (os-136/138 au fost testate doar la rece), iar toate ipotezele de azi
  (No Snoop, Relaxed Ordering, RXDV, buffer-e, RCR bit 17, Windows) sunt infirmate pe laptop. Ce să faci (P6-10e, P6-10f), cu regula
  „o schimbare pe Release, verificată pe laptop”:
  1. **P6-10e — inițializarea completă la rece.** Compară pornirea noastră cu ce fac driverele open-source la `attach`/`init` pentru 8168G/H
     (SerenityOS, FreeBSD `re(4)`, Haiku; Linux doar pentru înțelegere): ordinea reset → așteptare → deblocarea configurării → trezirea PHY
     (ieșirea din power-down, renegociere) și a MAC-ului (PLL/power), pașii specifici reviziei 0x50800000, apoi abia inelele, RCR/TCR, RE/TE.
     Scrie în `log rtl` fiecare pas cu registrul înainte/după. Scenariul QEMU nu poate valida asta (QEMU pornește „cald”): validarea e pe
     laptop, în modul **rece** (pornire directă). Criteriu: la rece, `net` arată trimise > 0 și primite > 0.
  2. **P6-10f — cadrele 2+ citite ca zero** (independent de 1): se diagnostichează **la cald** (meniul F12), cu `log rx` pe cadru din os-138:
     pentru primele 8 cadre, lungimea, adresa din descriptor, adresa citită, primii 16 octeți. Abia apoi reparația.
  3. Lista pentru **testul 7** în `stare/cyber-universe.md`, cu două părți: (R) pornire directă — `net`, `log rtl`; (C) pornire din F12 —
     `net`, `log rx`, `ping 1.1.1.1`. Fără `github.token` încă.
  4. **Completare 18:20 (pașii G–H din REZULTAT.md): P6-10f e REZOLVAT pe laptop** — `rtl porneste cache` face ca toate cadrele să fie citite
     corect („cadre cu tip 0000: 0”, ARP interpretat). Fă golirea cache-ului **implicită** la primire (sau mapează buffer-ele DMA necache-abile,
     ce e mai simplu și sigur) și verifică același lucru la **trimitere** (placa să nu citească o copie veche a cadrului). Și: **lipsa DHCP nu a
     fost niciodată o problemă a OS-ului** — cablul era între două laptopuri, fără router. Nu mai căuta nimic la DHCP până la testul cu cablul la
     router. Rămâne, ca prioritate 1, **P6-10e: inițializarea la rece**.
  5. **Completare 18:30 (pașii I–L): cu cablul la router, os-138 la cald + `rtl porneste cache` → DHCP 192.168.8.194, ping 1.1.1.1 20 ms,
     `host github.com` = 140.82.121.3, `run fetch https://example.com/` = TLS 1.3, certificat verificat, 577 octeți.** Tot lanțul merge pe hardware.
     Deci: (a) P6-10f = fă golirea cache-ului implicită (RX și TX) — gata confirmată; (b) P6-10e inițializarea la rece rămâne singura condiție ca
     bucla C-7 (pornire directă din BIOS) să aibă rețea; (c) mici: alias `fetch` în shell pentru `run fetch`; mesajul lui `host`.
     Testul 7 (lista): doar la **rece** (pornire directă): `net` → trebuie adresă; apoi `run fetch https://example.com/`. Dacă merge la rece,
     treci direct la C-7 și spune-i lui Adrian cum pune `github.token` pe stick.
- stare: gata (preluat 2026-10-22 15:05 UTC, terminat 16:00 UTC, sesiunea OS) — P6-10e; CI verde, Release os-144. **Completările 4–5:** preluate 2026-10-22 17:45 UTC, gata 18:25 UTC (sesiunea OS) — P6-10f; CI verde, Release os-149
- rezultat: pornirea completă la rece e variantă (`rtl porneste rece`, sau pe rând `mcu`/`phy`/`cplus`/`ordine`, idei din FreeBSD și SerenityOS), fiecare pas cu registrul înainte/după în `log rtl`; placa e 8168GU; lista pentru testul 7 (R rece, C cald, cu `rtl porneste cache` încercat la cald) e în `stare/cyber-universe.md`. **Completări:** golirea cache-ului (RX și TX) e acum pornirea obișnuită (`rtl porneste faracache` = os-125), `fetch` merge fără `run`, `host` scrie „github.com = 140.82.121.3”; lista testului 7 e rescrisă.

### C-10 · cyber-universe · Testul 7: buffer-ele de la prima inițializare sunt problema (nu cache-ul); la rece, scrierile OCP nu se aplică
- data: 2026-10-22 22:50 · de la: Adrian (prin centrul de comandă)
- ce: Testul 7 e în `rezultate/2026-10-22-test-7/REZULTAT.md` (6 poze). Două fapte verificate pe laptop:
  **(1) Cald:** prima inițializare din os-150 (cu golirea cache-ului implicită) citește tot zerouri (36 → 41 cadre cu tip 0000, fără adresă);
  după `rtl porneste cache` SAU `rtl porneste faracache` toate cadrele sunt bune și DHCP ia adresă (192.168.137.88, prin partajarea Windows),
  apoi `fetch https://example.com/` = TLS 1.3 verificat. Deci **cache-ul nu e cauza**: a doua inițializare repară pentru că alocă buffer-ele în
  altă parte (150a000 / 1595000) decât prima (3db000). Ipoteza: la prima inițializare paginile buffer-elor sunt **date și altcuiva** sau șterse
  ulterior (alocator timpuriu / suprapunere cu altă zonă). **P6-10g:** găsește suprapunerea (test în QEMU: nicio pagină alocată de două ori; jurnal
  cu cine primește paginile 3db000–3fffff), apoi alocă buffer-ele RX/TX pe aceeași cale ca la repornire; scoate golirea cache-ului implicită dacă
  nu mai e nevoie (măsurat). Criteriu pe laptop: la cald, `net` la prima inițializare → adresă fără nicio comandă.
  **(2) Rece:** `rtl porneste rece` a rulat 18 pași, tot 0/0. Au eșuat pașii 3 (FIFO RX+TX nu se golesc, `[00d3] 22 -> 22`), 7 și 9 (scrierile
  OCP în E8DE nu se aplică: `1 -> 1`, trebuia `8001`), 12 (C+ bit 3). **P6-10h:** repară accesul OCP/ERI (registrul de comandă, formatul
  adresă/date, bitul de „gata”, așteptarea) comparând cu FreeBSD `re(4)` și SerenityOS (clean-room); verifică citirea cu un registru cunoscut
  înainte de orice scriere. Abia apoi reia secvența la rece. Criteriu: la rece (pornire directă), `net` → adresă.
  **(3)** Mediul de test e de acum **partajarea Windows (ICS, 192.168.137.x)**; notează în `docs/HARDWARE.md`/`docs/USB.md`. O schimbare pe Release.
  Lista pentru testul 8: (R) pornire directă → `net`; (C) F12 → `net` la prima inițializare, `fetch`. Fără `github.token` până trece (R).
- stare: gata (preluat 2026-10-22 19:55 UTC, terminat 21:00 UTC, sesiunea OS) — P6-10g, P6-10h; CI verde, Release os-155
- rezultat: inelele și bufferele Realtek stau acum într-un bloc separat între 16 MiB și 4 GB (singura schimbare de pornire), paginile plăcilor sunt pazite (în QEMU nicio pagină dată de două ori) și bufferele se umplu cu A5 ca să vedem la testul 8 dacă placa n-a scris sau altcineva a șters; la rece, citirea OCP merge (0001), bitul 15 din E8DE se șterge singur și C+ bit 3 nu există la 8168, deci rămâne FIFO-ul (pasul 3); ICS notat în HARDWARE/USB; lista testului 8 e în `stare/cyber-universe.md`.

### C-11 · cyber-universe · Experimente mici cu placa video + studiu de fezabilitate pentru un driver propriu (după C-7)
- data: 2026-10-22 23:15 · de la: Adrian (prin centrul de comandă) — decizia din `DECIZII.md` (23:10)
- ce: Se preia **după C-7** (bucla de test de la distanță), nu înainte. Două părți, fără să atingă nimic din ce merge:
  1. **Experimente de nivel 0, pe laptopul de test (AMD Renoir, `1002:1636`)**, fiecare verificabil printr-o poză sau prin raportul automat al
     buclei: identificarea plăcii prin PCI (BAR-uri, mărimea VRAM/aperturii), maparea registrelor și citirea identității cipului după documentația
     publică AMD; nimic care scrie în placă încă. Pe **workstation (NVIDIA RTX 3070 Ti)** nu se face nimic fără o fereastră stabilită cu Adrian
     (workstation-ul e al lui Kronos, `RESURSE.md`); pregătești doar lista pașilor de nivel 0 (identificare, BAR-uri, citirea ID-ului din
     registrul public de boot) pentru acea fereastră.
  2. **Studiu de fezabilitate (fără cod):** `docs/research/STUDIU-GPU.md`: ce ar însemna un driver propriu de calcul (a) pentru NVIDIA Ampere
     (modulele deschise MIT ale NVIDIA, driverul nova în Rust, Mesa/NVK — doar citite; rolul firmware-ului GSP și licența lui; ce NU e
     documentat: setul de instrucțiuni), (b) pentru AMD (documentație publică ISA/registre, firmware redistribuibil, driverele deschise ca
     referință). Pentru fiecare: etape, estimări de timp cinstite, riscuri, ce ar rula Kronos pe el (fără CUDA/PyTorch), și o recomandare.
     Clean-room: `docs/CLEAN_ROOM.md`. Raportul se citește de Adrian înainte de orice decizie.
- stare: nou (se preia după C-7)
- rezultat:

### C-12 · cyber-universe · Aplică patch-ul `gpu identifica` de la Cyber-GPU și scoate un Release pentru fereastra de pe workstation
- data: 2026-10-23 08:45 · de la: Adrian (prin centrul de comandă). **Ridică oprirea de siguranță**: e o comandă nouă a lui Adrian.
- ce: Proiectul nou `cyber-gpu` (`PROIECTE.md`, `stare/cyber-gpu.md`) a lăsat în repo-ul lui, în `integration/cyber-universe/`, un patch
  care adaugă comanda de shell **`gpu`** (nivel 0: identificare PCI, BAR-uri, citirea a două registre publice **doar citire**, `log gpu`,
  `gpu plan`) și 6 observații despre nucleu. Se aplică pe `2d038de`. Ce să faci:
  1. Clonează `https://github.com/Adriancu91/cyber-gpu` (ramura `g0-g2-fundatie`), citește patch-ul **ca pe un cod străin**: verifică că nu
     scrie în niciun registru al plăcii (regula D-013 și §4.3 din prompt-ul lor), că respectă clean-room, `// SAFETY:`, și că nu atinge
     driverele existente. Dacă e în regulă, aplică-l pe `main` (sau rescrie-l în stilul nostru, dacă e mai curat), cu scenariu QEMU
     (`gpu identifica` pe o mașină fără NVIDIA trebuie să spună clar „nicio placă NVIDIA”) și cu testul că nu există nicio scriere MMIO
     în calea `gpu`. Nu lua operatorii CPU sau alte crate-uri acum: doar comanda `gpu`.
  2. Citește cele 6 observații despre nucleu (de ex. `map_mmio` și cache-ul registrelor); pentru fiecare: adevărat/fals în codul nostru, și
     dacă e adevărat, o sarcină în `docs/TASKS.md` (nu le repara acum, în afară de ce e trivial și sigur).
  3. CI verde → Release nou. În `stare/cyber-universe.md`, lista pentru **fereastra de pe workstation** (stick, pornire, `lspci`, `gpu identifica`,
     `log gpu 40`, `gpu plan`, `hw`, `net` — placa de rețea a workstation-ului e NECUNOSCUTĂ, notează ce apare) și, separat, **testul 8** pe
     laptop (pornire directă → `net` → adresă; `fetch`), care încă n-a fost făcut.
  4. Testul pe workstation se face doar cu Adrian; Kronos stă în pauză cât durează (placa e liberă azi).
- stare: gata, cu o limită (preluat 2026-10-23 05:32 UTC, terminat 06:30 UTC, sesiunea OS) — P6-11 (+ P6-12 în coadă); CI verde, Release os-163. **Limită:** repo-ul `cyber-gpu` e privat, sesiunea OS nu are acces → patch-ul și 5 din cele 6 observații n-au fost citite.
- rezultat: comanda `gpu` (identifica, plan, `log gpu`) e scrisă de la zero, doar citire (fereastra de registre e mapată fără drept de scriere, testat în QEMU), și e în Release os-163 împreună cu testul 8; observația despre `map_mmio` e adevărată ca posibilitate (P6-12), restul așteaptă acces la `cyber-gpu`; listele pentru fereastra de pe workstation și testul 8 sunt în `stare/cyber-universe.md`.

### C-13 · cyber-universe · Prima pornire pe workstation: PCI pe toate rădăcinile (GPU invizibil), hub-uri USB, alegerea stick-ului
- data: 2026-10-23 09:55 · de la: Adrian (prin centrul de comandă)
- ce: Rezultatul: `rezultate/2026-10-23-workstation-os/REZULTAT.md` (3 poze). OS-ul pornește pe workstation (Dell, i9-10980XE, 128 GB văzuți), dar:
  1. **P6-13 — PCI pe toate magistralele (prioritar, blochează `gpu identifica`):** pe Cascade Lake-X sunt mai multe magistrale-rădăcină
     independente; RTX 3070 Ti e la `B3:00.0` și nu apare. Scanează **toate** magistralele din intervalul MCFG (`start_bus..=end_bus`, fiecare
     device 0–31, funcția 0 și, dacă e multi-function, 1–7; vendor ≠ FFFF), fără dubluri cu parcurgerea punților; ordine stabilă (după bus/dev/fn).
     Atenție la timp și la memoria mapată (256 de magistrale × 1 MiB ECAM: mapează doar ce citești). Test QEMU: `-device pxb-pcie` (o rădăcină
     în plus) cu un dispozitiv pe ea → trebuie să apară în `lspci`. Pe laptop: aceeași listă ca înainte (fără regresie).
  2. **P6-14 — USB: hub-uri** (`0bda:0411` USB 3, `0bda:5411` USB 2 pe workstation): enumerarea porturilor din spatele unui hub (clasa 09, Get Port
     Status, Set Port Feature RESET, Route String / TT în contextul slotului xHCI). După specificația publică USB 2.0/3.x, cap. 11/10.
  3. **P6-15 — `/usb` = stick-ul de pe care am pornit:** încearcă toate dispozitivele Mass Storage; sări peste cele cu „Medium Not Present”
     (sense 2/3A); preferă discul care conține `cyber.rw` și `VERSIUNE`.
  4. **P6-16 (mai târziu, după 1–3):** driver pentru Intel I219-LM (`8086:15e3`, e1000e), după documentația publică Intel; util pentru bucla de pe workstation.
  5. **Observațiile de la `cyber-gpu`** (repo privat, de aceea C-12 nu le-a putut citi) sunt copiate în hub: `integrare/cyber-gpu/OBSERVATII_cyber-universe.md`.
     Judecă fiecare (adevărat/fals în codul nostru), cum cerea C-12 pasul 2.
  5b. **P6-17 — `reboot` pe workstation nu repornește** (rămâne la „repornesc...”, poza 06): încearcă pe rând ACPI RESET_REG (FADT), portul 0xCF9
     (valoarea 2, apoi 6), controlerul 8042 (0xFE), triple fault; câte un rând în jurnal. Important pentru bucla automată (C-7).
  6. O schimbare de comportament pe Release (D-013): 1 întâi, cu Release; apoi 2–3. În `stare/cyber-universe.md`, lista pentru **fereastra a doua pe
     workstation**: `lspci` (trebuie să apară `10de:2482` la B3), `gpu identifica`, `gpu plan`, `log gpu 40`, `log pci 40`, `hw`.
- stare: gata (preluat 2026-10-23 06:53 UTC, terminat 09:20 UTC, sesiunile OS) — P6-13 (os-166), P6-14 (os-167), P6-15 (os-169), P6-17; P6-16 (p.4) = C-14 pasul 1
- rezultat: PCI caută acum pe toate magistralele-rădăcină, USB vede dispozitivele din spatele hub-urilor, `/usb` alege stick-ul cu `cyber.rw` și `VERSIUNE` (sare cititoarele goale), iar `reboot` încearcă pe rând ACPI, 0xCF9, 8042 și triple fault, cu câte un rând pe ecran; observațiile Cyber-GPU judecate în `docs/research/OBSERVATII-CYBER-GPU.md`; lista pentru fereastra a doua pe workstation e în `stare/cyber-universe.md`.

### C-14 · cyber-universe · Lucrul automat cât e Adrian plecat: rețeaua workstation-ului (I219) + pregătirea „Kronos în OS pe procesor” (K6-CPU)
- data: 2026-10-23 10:20 · de la: Adrian (prin centrul de comandă) — ales de Adrian: „C-13 + rețea + K6-CPU”
- ce: Adrian e plecat câteva zile; **niciun test pe hardware până se întoarce** (laptopul de test și workstation-ul stau). Lucrezi doar ce se poate
  verifica în QEMU și în CI, în ordinea asta, **după C-13**, câte o sarcină pe rând, fiecare cu plan în `docs/plans/`, scenariu QEMU și README:
  1. **P6-16 — driver Intel I219-LM** (`8086:15e3`, familia e1000e, pe workstation) după documentația publică Intel (datasheet I219 / manualul
     pentru dezvoltatori 8254x/e1000e), clean-room. QEMU are `-device e1000e` (82574L, nu I219: inițializarea comună se testează acolo, diferențele
     I219 — PHY prin MDIO, ULP — se notează pentru testul pe hardware). Aceleași lecții ca la Realtek: buffer-e DMA din blocul păzit, adrese 64 de
     biți, `log` pe registre, variante de pornire (D-013).
  2. **K6-CPU, pasul 1 — SSE/AVX în nucleu și în programe:** activează SSE/AVX (CR0/CR4, XCR0 prin XSETBV, doar ce raportează CPUID), salvează și
     restaurează starea vectorială la comutarea firelor (XSAVE/XRSTOR, zonă aliniată la 64 de octeți per fir, mărimea din CPUID 0Dh); test: două
     fire care calculează în vectori, rezultatul exact după mii de comutări; un program ring 3 cu AVX2.
  3. **K6-CPU, pasul 2 — SMP:** pornirea celorlalte nuclee (MADT, INIT-SIPI-SIPI, trampolină sub 1 MiB, stivă și APIC per nucleu), încuietori reale
     (spinlock-uri cu întreruperi oprite unde trebuie), planificator pe mai multe nuclee (cozi per nucleu sau o coadă cu încuietoare). Test: QEMU
     `-smp 4`: 4 nuclee pornite, fire repartizate, testul de stres trece; nicio regresie la scenariile existente.
  4. **K6-CPU, pasul 3 — memorie mare pentru programe:** un apel de sistem de alocare de regiuni (mmap anonim, MiB–GiB, pagini mari unde se poate) +
     eliberare; limita heap-ului nucleului ridicată doar dacă e nevoie. Test: un program care alocă 1 GiB, îl scrie și îl verifică.
  5. Opțional, dacă timpul permite: **fire multiple într-un proces** (pasul 4 din K6-CPU), cu test.
  Fiecare pas: `main` mereu construibil, CI verde, Release la fiecare pas încheiat. Listele de test pe hardware se strâng în `stare/cyber-universe.md`
  pentru întoarcerea lui Adrian. Planul general: `idei/2026-10-23_kronos-bare-metal_v0.2.md` și `idei/2026-10-23_arhitectura_kernel_cyber-universe.md`
  (§14 = golurile). **Nu porni C-7 și C-11** până nu se întoarce Adrian. Lucrul cu `cyber-gpu` se face doar prin hub (`integrare/cyber-gpu/`).
- stare: gata (preluat 2026-10-23 09:20 UTC, terminat 15:20 UTC, sesiunile OS) — P6-16 (os-174), K6-01 (os-175), K6-02 (os-177), K6-02b, K6-03, K6-04 (testate local; fără Release: CI-ul GitHub nu pornește din 11:03 UTC)
- rezultat: toți cei 5 pași sunt făcuți și testați în QEMU (70 de scenarii trecute local); ultimele trei ies în Release la primul push după ce GitHub Actions merge din nou.

### C-15 · cyber-universe · Repo-ul devine public (CI gratuit) + CI mai econom + Release-ul cu munca din C-14
- data: 2026-10-23 19:10 · de la: Adrian (prin centrul de comandă) — Adrian face `cyber-universe` **public** (decizia 19:05; istoricul verificat de centrul
  de comandă: nicio cheie reală, doar cheile de test din `tls/tests/data/`)
- ce: Cauza B-004 era facturarea GitHub („The job was not started because recent account payments have failed or your spending limit needs to be
  increased”): minutele gratuite pentru repo-uri private s-au terminat. Pe repo public Actions e gratuit. Ce să faci:
  1. Verifică întâi că repo-ul e public (`gh api repos/Adriancu91/cyber-universe -q .visibility`). Dacă nu e încă, nu forța nimic: notează și treci la 2.
  2. **CI mai econom** (oricum ar fi vizibilitatea): `paths-ignore` pentru `docs/**`, `**/*.md`, `tests/screens/**` (fără build la commit-urile care
     schimbă doar documente/STATE.md); `concurrency` cu `cancel-in-progress: true` pe aceeași ramură; testul de stres o dată pe săptămână (nu zilnic);
     cache pentru `~/.cargo` și `target/` dacă nu există. Release doar când s-a schimbat codul.
  3. Când CI e verde: Release-ul cu K6-02b, K6-03, K6-04 (și ce mai lipsește din C-14). Închide B-004 în `docs/BLOCKERS.md` cu cauza exactă.
  4. Cu repo-ul public, `actualizeaza` poate merge fără token: verifică și notează în `docs/USB.md`; tokenul rămâne necesar doar pentru `gh-trimite`.
  5. **19:10: și `cyber-gpu` e public.** De acum îl poți citi direct (`git clone https://github.com/Adriancu91/cyber-gpu`, ramura `g0-g2-fundatie`):
     citește patch-ul și cele 6 observații din `integration/cyber-universe/` (punctul din C-12 rămas nefăcut) și propunerile `gpu gfw` / `gpu vbios`.
     Tot doar citire în placă; nu modifici `cyber-gpu`.
- stare: gata (preluat 2026-10-23 16:10 UTC, terminat 17:00 UTC, sesiunea OS) — P6-18 în docs/TASKS.md; CI verde (run 187), Release os-187
- rezultat: repo-ul e public și CI-ul merge iar (uneltele se instalează în 22 s), commit-urile doar cu documente nu mai pornesc CI, stresul e săptămânal, Release `os-187` are toată munca din C-14, B-004 e închis, iar `actualizeaza` nu mai cere token (doar `gh-trimite` îl cere).

### C-16 · cyber-universe · OS + Cyber-GPU integrate și testate automat (CI) — cu punct de revenire înainte
- data: 2026-10-23 19:30 · de la: Adrian (prin centrul de comandă) — „da, dar dacă se strică ceva ne asigurăm că putem reveni la starea de acum”
- ce: **După C-15.** Pași, în ordine:
  0. **Punct de revenire, ÎNAINTE de orice:** creează și urcă tag-ul adnotat `stabil-2026-10-23` pe commit-ul `9f67d7b` (main, 23 oct 16:10 UTC,
     „P6-18: CI mai econom”) — e starea de acum, aleasă de Adrian. Nu muta și nu șterge niciodată acest tag. Scrie în `docs/STATE.md` cum se revine
     (`git checkout stabil-2026-10-23`; Release-urile testate pe hardware rămân: os-150 internet pe laptop, os-161 pornire pe workstation).
  1. **Integrarea se face pe ramura `wip/integrare-gpu`**, nu pe `main`. Pe `main` intră doar când **toate** scenariile existente trec și cele noi
     trec. Dacă ceva nu se poate repara în 3 încercări (regula din CLAUDE.md §3), ramura se abandonează (rămâne în istoric), `main` rămâne neatins,
     iar problema intră în `docs/BLOCKERS.md`. Fără `push --force`, fără rescrierea istoriei.
  2. Dependență pe `https://github.com/Adriancu91/cyber-gpu` (public) **fixată pe tag-ul lor `stabil-2026-10-23` / commit `41e44ba`** (nu pe o ramură
     mobilă), doar crate-urile no_std: `gpu-core`, `gpu-pci`, `nvidia-ga104` (probe, doar citire), `gpu-compute` (backend CPU), și `gpu-sim` doar pentru
     teste. Verifică licențele (MIT) și că nimic nu scrie în registrele plăcii.
  3. Scenarii QEMU noi, în CI: (a) `gpu identifica` pe calea reală → „nicio placă NVIDIA” (QEMU n-are); (b) `gpu identifica --sim` pe modelul
     `gpu-sim` cu datele workstation-ului (`10de:2482`, BAR0 16 MiB, BAR1 256 MiB, BAR3 32 MiB) — **etichetat SIMULARE** în ieșire; (c) `kronos-calcul`
     (program nou, ring 3): matmul și operațiile lui Kronos din `gpu-compute`, pe toate nucleele (SMP) și cu SSE/AVX, comparate cu referința
     (toleranță declarată), cu timpul măsurat pe 1 și pe N nuclee.
  4. Release din `main` doar după ce `wip/integrare-gpu` e unită și CI e verde. În `stare/cyber-universe.md`: ce s-a integrat, ce e SIMULARE și lista
     pentru fereastra de pe workstation.
- stare: gata (preluat 2026-10-23 17:45 UTC, terminat 19:25 UTC, sesiunea OS) — P6-19 în docs/TASKS.md; CI verde pe ramură (run 188) și pe main (run 189), Release os-189. **Limită la pasul 0:** tag-ul nu se poate urca din cloud (403) → ramura `revenire/stabil-2026-10-23` pe `9f67d7b` + os-187 păstrat de CI; os-150/os-161 nu mai existau.
- rezultat: OS-ul folosește bibliotecile Cyber-GPU fixate pe 41e44ba (identificarea plăcii fără nicio scriere, simularea plăcii de pe workstation marcată SIMULARE, calculul lui Kronos pe toate nucleele identic cu referința), testate în CI, în Release os-189.

### C-17 · cyber-universe · Release-urile testate pe hardware nu se mai șterg
- data: 2026-10-23 22:50 · de la: Adrian (prin centrul de comandă)
- ce: CI-ul păstrează doar ultimele 5 Release-uri (`ci.yml`, `tail -n +6 | … gh release delete`), și așa s-au șters os-150 (prima ieșire pe internet,
  laptop) și os-161 (prima pornire pe workstation). Regula de acum: un Release care a fost **testat pe hardware** (apare într-un `rezultate/…/REZULTAT.md`
  din hub) sau e **punct de revenire** (os-187) nu se șterge niciodată. Simplu: o listă `docs/RELEASES_PASTRATE.md` (tag + motiv), iar curățarea din CI
  sare peste ele. Dacă poți reface os-150 și os-161 din commit-urile lor (`git log` după mesajele lor de Release), republică-le ca Release-uri
  păstrate; dacă nu, notează doar commit-urile lor în listă. Nu schimba nimic altceva în CI.
- stare: gata (preluat 2026-10-23 20:45 UTC, terminat 21:05 UTC, sesiunea OS) — P6-20 în docs/TASKS.md; CI verde (run 190), Release os-190
- rezultat: Lista `docs/RELEASES_PASTRATE.md` (os-120, 125, 136, 138, 150, 161 testate pe hardware + os-187) e respectată de curățarea din CI, iar os-150 și os-161 sunt din nou la Releases, cu fișierele lor originale (sumele verificate, nemarcate „latest”).

### C-18 · cyber-gpu · Deciziile lui Adrian: firmware-ul NVIDIA DA (separat, pe stick), compilator Mesa NAK, tabel de compatibilitate
- data: 2026-10-26 17:10 · de la: Adrian (prin centrul de comandă)
- ce: Adrian a răspuns la cele două decizii care blocau pasul I4 (`docs/RESEARCH_I4_I8.md` §5.1 și §5.2) și a spus „da la toate recomandările
  actuale și viitoare despre cyber-gpu” ale centrului de comandă.
  1. **Firmware-ul semnat NVIDIA (GSP-RM, Booter): DA**, o singură versiune fixată, **570.144** (ca nova-core). Fișierele firmware **nu intră
     niciodată în repo** (nici în cyber-universe, nici în hub): driverul le citește dintr-un fișier separat pe care Adrian îl pune pe stick;
     repo-ul conține doar numele și sumele SHA256 așteptate, plus instrucțiunile de unde le ia Adrian (pachetul oficial `linux-firmware`).
     Nu desfacem și nu analizăm interiorul firmware-ului (licența NVIDIA o interzice); folosim doar antetele publice (open-gpu-kernel-modules, MIT)
     și documentația nouveau/nova, ca idei, fără cod copiat — proveniența în `docs/PROVENANCE.md`.
  2. **Compilatorul pentru programele GPU: Mesa NAK** (rulează pe gazdă la build, nu în OS). `ptxas` doar dacă, mult mai târziu, performanța o cere.
  3. **Tabelul de compatibilitate** (idee dintr-un studiu adus de Adrian): un singur fișier `docs/COMPATIBILITATE_FIRMWARE.md` cu coloanele:
     componentă · sursa de referință (fișier + versiune) · comportament observat · ABI/versiune · dependențe · fișierul Rust · testul · stare
     (confirmat / parțial / necunoscut / SIMULARE). Strânge în el ce e acum împrăștiat în RESEARCH, GA104_INITIALIZATION și IMPLEMENTATION_STATUS.
  Mai departe: I4–I8 pregătite și testate în SIMULARE, ca până acum. **Nicio scriere în placa reală fără Adrian de față** (fereastra pe
  workstation, mâine sau poimâine). Fără cod GPL copiat; fără firmware în repo.
- stare: gata (preluat 2026-10-26 17:16, terminat 17:45, sesiunea Cyber-GPU) — commit `dac2e32` pe `g0-g2-fundatie`, CI verde
- rezultat: Deciziile sunt aplicate: tabelul `docs/COMPATIBILITATE_FIRMWARE.md`, citirea și verificarea (SHA-256) firmware-ului 570.144 de pe stick și pregătirea GSP (I5–I8) sunt scrise și testate doar în SIMULARE, primul program GPU e compilat cu Mesa NAK (nerulat), iar lista pentru fereastra pe workstation e în `docs/TEST_MATRIX.md` B0 — nimic nu scrie în placă.

### C-19 · cyber-universe · Comenzile `gpu gfw` și `gpu vbios` (doar citire) în OS
- data: 2026-10-26 17:10 · de la: Adrian (prin centrul de comandă)
- ce: Propunerea `integrare/cyber-gpu/2026-10-23_I2-I3_comenzi-gpu-gfw-vbios.md` e aprobată (recomandarea centrului, aprobată în bloc de Adrian).
  Mută fixarea Cyber-GPU de pe `41e44ba` pe commit-ul lor curent de pe `main` (ei spun că s-a doar adăugat, nimic șters), adaugă `gpu gfw` și
  `gpu vbios` — **doar citire**, cu numărul de scrieri refuzate afișat ca la `gpu identifica` — testate în CI cu `--sim`, și scoate un Release
  pentru fereastra de pe workstation (mâine sau poimâine). Release-ul os-187 rămâne punctul de revenire. Nu schimba nimic altceva.
- stare: gata (preluat 2026-10-26 15:45 UTC, terminat 16:40 UTC, sesiunea OS) — P6-21; CI verde (run 191), Release os-191
- rezultat: fixarea Cyber-GPU e pe `dac2e32` (doar adăugări), `gpu gfw` și `gpu vbios` merg doar citire cu numărul de scrieri refuzate afișat, testate în SIMULARE în CI, iar Release-ul os-191 e gata pentru fereastra de pe workstation (lista în `stare/cyber-universe.md`).

### C-20 · cyber-gpu · Folosește studiul open-source: tinygrad ca hartă pentru I4–I10, antete generate, GSP fals, NAK + matmul
- data: 2026-10-26 18:10 · de la: Adrian (prin centrul de comandă; recomandări aprobate prin „da”-ul general din 26 oct 17:10)
- ce: Citește `studiu/2026-10-26_open-source/gpu.md` din hub (secțiunile 2 și 3) și fă, după C-18, în ordinea:
  B (crate generat din antetele NVIDIA 570.144, MIT, cu notificarea lor și teste de mărime/poziție; unealta de generare doar pe gazdă, versiune fixată),
  C (secvența tinygrad `support/nv/` ca specificație pentru I4–I10 — cod Rust scris de noi, nu traducere linie cu linie; sursa în PROVENANCE; pasul nou
  „golden image” după pornirea GSP; valorile „magice” marcate „dovedite empiric, neexplicate”), D (procesor de comenzi + GSP fals în `gpu-sim`),
  E (NAK pe gazdă + treptele matmul, primul matmul în f32; tratarea FMA în comparația cu referința).
  Pentru A (proba tinygrad pe placa reală, de pe un stick Linux, cu jurnalul scrierilor): pregătește doar instrucțiunile exacte și scriptul în
  `docs/TEST_MATRIX.md` + parserul de jurnal testat pe un jurnal scris de mână. **Nu se rulează nimic pe placă fără Adrian de față.**
  Firmware-ul NVIDIA rămâne în afara repo-ului.
- stare: gata (preluat 2026-10-26 19:27, sesiunea 6; reluat 2026-10-27 01:28, terminat 02:05, sesiunea 7) — commit `ea4a2d1` pe `g0-g2-fundatie`, CI verde; A rămâne doar pregătită (se rulează doar cu Adrian de față); treptele matmul 3+ continuă fără comandă nouă; sesiunea 8 (27 oct 08:50): treapta 3 + `SET_SYSTEM_INFO`, commit `e895783`, doar SIMULARE; sesiunea 9 (27 oct 13:55): „golden image” (I8e, pasul C) în cod + treapta 4 matmul, commit `50f2816`, doar SIMULARE; sesiunea 10 (27 oct 19:55): tabelele de pagini (I9a) + treapta 5 matmul, commit `f10662b`, doar SIMULARE
- rezultat: Antetele NVIDIA generate, mesajele GSP mari, procesorul de comenzi și GSP-ul fals (pornire simulată până la INIT_DONE) și matmul-ul NAK (treptele 1–2, identic bit cu bit cu calculul de control FMA+FTZ) sunt gata și testate doar în SIMULARE; nimic nu a rulat pe placă.

### C-21 · kronos · Din studiul open-source: memoria E3 mai bună, apoi Muon + răcire lungă, apoi motorul de inferență fără PyTorch
- data: 2026-10-26 17:45 · de la: Adrian (prin centrul de comandă; recomandările centrului, aprobate de Adrian)
- ce: Detaliile, pragurile propuse și riscurile sunt în hub, `studiu/2026-10-26_open-source/kronos.md`, secțiunea 3. **După S27** (nu-l întrerupe),
  ca sarcini separate în `plan/coada.md`, fiecare cu pre-înregistrare înainte de pornire, în ordinea:
  1. **Propunerea 2 (memoria E3):** (a) stemmer românesc propriu ca a doua coloană în index + unire RRF; (b) reordonarea primelor 20 de bucăți cu
     log p(întrebare | bucată) calculat de modelul nostru (#415 sau rezultatul S27 dacă e confirmat). Prag: k = 3 urcă ≥ 5 puncte pe un set NOU, neatins,
     iar k = 20 nu scade. Doc2query (c) doar după (a) și (b).
  2. **Propunerea 1 (Muon + răcire lungă):** A = AdamW ca acum, B = Muon, câte 2 h din același punct, aceeași sămânță și date, gradient adunat pe 8 loturi,
     răcire ~25 %; întâi testul unitar pe procesor și proba de 10 min sub 7.000 MB. Prag: B ≤ A − 0,010 val_bpb română, fără regresie > 0,005 în rest.
  3. **Propunerea 3 (motor de inferență fără PyTorch, fp32 + Q8_0):** fără placă; logits identici (< 1e-4) cu PyTorch pe 3 texte fixe; Q8_0 pierde ≤ 0,005 val_bpb.
  Toate ca module noi (MANIFEST + teste de contract), reversibile; #415 și linia w2 rămân neatinse. **Examenul nu se schimbă.**
  Propunerile 4 (w3) și 5 (auto-joc) rămân pentru mai târziu (5 după verdictul S27). Date: TinyStories rămâne deocamdată (vezi DECIZII 26 oct 17:45);
  orice date NOI nu au voie să fie generate de un LLM străin.
- stare: gata (preluat 2026-10-26 20:15, terminat 2026-10-27 14:15, supraveghetor) — S29, S30, S31, S32 în `plan/coada.md` din cyberspace, `aprobat`, în ordine, fiecare doar după S27 și după cea dinainte; S29 gata (CONFIRMAT), S30 gata, S31 gata (INFIRMAT: Muon 1,3019 față de AdamW 1,2332), S32 gata
- rezultat: Memoria E3 mai bună a trecut (S29: 83 față de 72 în primele 3 bucăți), Muon a picat (S31), iar motorul fără PyTorch merge (S32: Q8_0 de 111 MB pierde doar +0,00002 bpb; F32 ratează la limită pragul de 1e-4, cu textul identic — se repară în S37).

### C-22 · cyber-universe · Din studiul open-source: „cutia neagră” pe stick + permisiuni pe program
- data: 2026-10-26 17:45 · de la: Adrian (prin centrul de comandă; recomandările centrului, aprobate de Adrian)
- ce: Detaliile în hub, `studiu/2026-10-26_open-source/os.md`, propunerile 1 și 4. După C-19:
  1. **„Cutia neagră”:** la cerere (`raport`) și automat la erori grave, OS-ul scrie pe stick un fișier text (ex. `/usb/raport/<data>-<nr>.txt`) cu versiunea,
     `hw`, `lspci`, jurnalele `net`/`usb`/`pci`/`gpu` și registrele relevante ale driverelor — ca rezultatele testelor de pe hardware să nu mai vină prin
     poze. Fără chei sau token-uri în raport (filtrate explicit). Test în QEMU: fișierul apare pe discul virtual și conține secțiunile așteptate.
  2. **Permisiuni pe program:** un program declară ce apeluri și ce căi folosește („promisiuni” + „căi vizibile”, idei din OpenBSD pledge/unveil și
     Fuchsia, scrise de noi); după declarare nu le mai poate depăși. `/usb/claude.key` și `/usb/github.token` devin vizibile doar programelor care le
     cer explicit (aplicația Claude, `gh-trimite`). Teste în QEMU: un program fără permisiune primește eroare la citirea cheii.
  Restul propunerilor (teste mai rapide, găzduirea lui Kronos, tipuri pentru DMA) rămân pentru mai târziu, după aceste două.
- stare: gata (preluat 2026-10-26 15:45 UTC, terminat 16:40 UTC, sesiunea OS) — P6-22, P6-23; CI verde (run 191), Release os-191
- rezultat: `raport` scrie pe stick `/usb/raport/<data>-<nr>.txt` (și automat la erori noi, fără chei, testat în QEMU cu citirea fișierului din imagine), iar programele au promisiuni + căi vizibile, cu `claude.key`/`github.token` vizibile doar programelor care le cer (scenariul `drepturi`).

### C-23 · cyber-universe · Laptop AMD Ryzen 5 4500U: `run kronos-calcul` cade cu #GP (cod 0x18), și pe un nucleu
- data: 2026-10-27 23:00 · de la: Adrian (prin centrul de comandă)
- ce: Test pe ThinkPad-ul lui Adrian (**raportul arată AMD Ryzen 5 4500U, Zen 2**, nu Intel cum crezusem), os-191: pornește, 6 nuclee pornite, driverul de rețea rulează (fără cablu), dar
  `run kronos-calcul` după `cpu porneste` oprește sistemul: `#GP`, `RIP=0xffffffff8001e939`, `RSP=0xffff9000001d0398`, `RFLAGS=0x10082`, `CS=0x8`,
  `cod eroare=0x18`. Detalii și poză: `rezultate/2026-10-27-thinkpad-os191/`. Găsește cauza (simbolizează RIP pe build-ul os-191, commit `a0834b7`),
  repar-o, adaugă un test în QEMU care o prinde (de ex. `-cpu EPYC-Rome` / Zen 2 în QEMU),
  și scoate un Release nou. Rapoartele `raport` de la a doua pornire vin în același dosar
  când le trimite Adrian. Nu schimba nimic altceva.
  **Actualizare 23:05:** pe un singur nucleu (fără `cpu porneste`) cade la fel, același RIP → nu e de la SMP. `raport` a mers pe hardware; raportul complet e în dosar (`raport-20261027-1.txt`).
  **Actualizare 23:10:** pe un al doilea laptop, ThinkPad cu **Intel i7**, același stick: `run kronos-calcul` merge (OK, 0 diferențe) → căderea e
  **specifică AMD**. Tot acolo, problemă separată: `raport` spune „stick-ul nu e montat (/usb)” — OS-ul nu găsește stick-ul de pe care a pornit pe
  acel laptop (pozele cu `log usb 60` și `hw` vin în `rezultate/2026-10-27-thinkpad-os191/`); repar-o în aceeași sarcină sau în una separată.
  **Cauza probabilă (din `log usb 60`):** pe Tiger Lake sunt două xHCI (`00:0d.0 8086:9a13` Thunderbolt și `00:14.0 8086:a0ed`); OS-ul pornește doar
  unul („5 porturi, 0 dispozitive”) — trebuie pornite **toate** controlerele xHCI și căutat stick-ul pe fiecare (test QEMU cu două `qemu-xhci`).
  Pe Intel, `cpu porneste` + `kronos-calcul` cu 8 fire: OK (7× față de 1 fir) — primul calcul Kronos pe toate nucleele, pe hardware real.
- stare: nou
- rezultat:

### C-24 · kronos · Kronos adevărat în OS, partea Kronos: specificația KGR1 + vectorii de test în hub, modelul exportat
- data: 2026-10-27 23:20 · de la: Adrian (prin centrul de comandă; delegarea din 26 oct 17:45 — „Kronos în OS-ul propriu” e direcția lui)
- ce: Fără placă, fără să întrerupi S38 sau altă sarcină de placă. (1) Copiază în hub, `integrare/kronos/`, `docs/format_greutati.md` (KGR1) și un
  set mic de **vectori de test**: un model KGR1 minuscul cu greutăți aleatoare (≤ 1 MB, Q8_0 și F32), 3 texte fixe tokenizate și logit-urile
  pe care le dă `unelte/inferenta_bruta.py` pe el — ca sesiunea OS să-și verifice motorul Rust fără să vadă codul Kronos. Fără greutăți
  reale în hub. (2) Exportă cel mai bun model curent (#441 sau rezultatul S38, dacă e confirmat) în **KGR1 Q8_0** cu `unelte/exporta_greutati.py`
  și pune fișierul ca **Release** în repo-ul privat `cyberspace` (nu în hub, nu în repo-urile publice), cu suma SHA-256 notată în
  `integrare/kronos/MODEL.md` (numele modelului, mărimea, suma, 3 texte cu primele 5 simboluri generate greedy, ca test pe hardware).
- stare: preluat (2026-10-27 23:15, supraveghetor) — S39 în `plan/coada.md` din cyberspace, `aprobat`; partea A (model minuscul + vectori) acum, doar procesor; partea B (exportul + Release privat) după S38. Executantul nu scrie în hub: pregătește `integrare/kronos/` în cyberspace, iar supraveghetorul îl copiază aici.
- rezultat:

### C-25 · cyber-universe · Kronos adevărat în OS: motorul KGR1 în Rust + comanda `kronos`
- data: 2026-10-27 23:20 · de la: Adrian (prin centrul de comandă; delegarea din 26 oct 17:45)
- ce: **După C-23.** Azi `kronos-calcul` rulează doar operațiile lui Kronos pe date de probă; pasul următor e modelul adevărat. Folosind
  `integrare/kronos/format_greutati.md` și vectorii de test din hub (C-24): un motor no_std care citește un fișier KGR1 (F32 și Q8_0) de pe stick
  (`/usb/kronos/*.kgr`), verifică suma SHA-256, face forward-ul strat cu strat pe toate nucleele (operatorii din `gpu-compute`) și tokenizerul
  din fișier. Test în CI: pe modelul minuscul, logit-urile egale cu ale referinței (toleranța declarată în `integrare/kronos/`). Apoi comanda
  `kronos "<text>"` care continuă textul (greedy, max N simboluri) și afișează simbolurile pe secundă. Greutățile reale nu intră în repo
  (repo public); Adrian le pune pe stick. Scrie-ți codul (nu porta codul Python); nu schimba nimic altceva.
  **Ținta principală pe hardware e workstation-ul** (i9-10980XE, 18 nuclee / 36 fire, AVX-512, 128 GB, rețea I219 cu cablu; Adrian, 27 oct 23:16):
  folosește toate cele 36 de fire și, dacă e simplu, AVX-512 cu fallback la AVX2; laptopul Intel rămâne a doua țintă.
- stare: nou
- rezultat:

### C-26 · cyber-universe · O linie în `hw` cu adresa imaginii ecranului (cerere Cyber-GPU, doar citire)
- data: 2026-10-27 23:30 · de la: Adrian (prin centrul de comandă; delegarea din 26 oct 17:45)
- ce: Propunerea din `cyber-gpu` `integration/cyber-universe/B0_adresa-ecranului.md`: în `hw` (și deci în `raport`), o linie cu adresa fizică și
  mărimea framebuffer-ului primit de la Limine, ca driverul GPU să nu scrie peste ea. Doar citire; test în QEMU. Fă-o împreună cu C-23, ca Release-ul
  pentru fereastra de pe workstation să o conțină.
- stare: nou
- rezultat:
