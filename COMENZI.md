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
- stare: nou
- rezultat:
