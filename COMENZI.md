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
- stare: gata (preluat 2026-10-26 19:27, sesiunea 6; reluat 2026-10-27 01:28, terminat 02:05, sesiunea 7) — commit `ea4a2d1` pe `g0-g2-fundatie`, CI verde; A rămâne doar pregătită (se rulează doar cu Adrian de față); treptele matmul 3+ continuă fără comandă nouă; sesiunea 8 (27 oct 08:50): treapta 3 + `SET_SYSTEM_INFO`, commit `e895783`, doar SIMULARE; sesiunea 9 (27 oct 13:55): „golden image” (I8e, pasul C) în cod + treapta 4 matmul, commit `50f2816`, doar SIMULARE; sesiunea 10 (27 oct 19:55): tabelele de pagini (I9a) + treapta 5 matmul, commit `f10662b`, doar SIMULARE; sesiunea 11 (28 oct 01:45): I9b (tabelele scrise în VRAM prin fereastra BAR0 + golirea TLB, zona ecranului din os-192), commit `a2acd29`, doar SIMULARE; sesiunea 12 (28 oct 07:50): încărcătorul DMA I6/I7 (FWSEC + Booter) + comanda FRTS, commit `d439189`, doar SIMULARE; sesiunea 24 (30 oct 19:45): treapta 6 matmul (accese de 128 de biți), commit `937fcf4`, doar SIMULARE — treptele matmul fără placă sunt terminate
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
- stare: gata (preluat 2026-10-27 21:45 UTC, terminat 23:20 UTC, sesiunea OS) — P6-24, P6-25; CI verde (run 192), Release os-192
- rezultat: căderea #GP pe AMD venea din `sysret` (pe AMD programul rămânea cu SS=0x18 fără RPL 3, iar întoarcerea după întreruperea de ceas cădea), reparată prin baza 0x13 în STAR cu test care pică pe valoarea veche, iar OS-ul pornește acum toate controlerele USB (stick-ul de pe `00:14.0` se va găsi), testat în QEMU cu două controlere; confirmarea pe ambele laptopuri e în `stare/cyber-universe.md`.

### C-24 · kronos · Kronos adevărat în OS, partea Kronos: specificația KGR1 + vectorii de test în hub, modelul exportat
- data: 2026-10-27 23:20 · de la: Adrian (prin centrul de comandă; delegarea din 26 oct 17:45 — „Kronos în OS-ul propriu” e direcția lui)
- ce: Fără placă, fără să întrerupi S38 sau altă sarcină de placă. (1) Copiază în hub, `integrare/kronos/`, `docs/format_greutati.md` (KGR1) și un
  set mic de **vectori de test**: un model KGR1 minuscul cu greutăți aleatoare (≤ 1 MB, Q8_0 și F32), 3 texte fixe tokenizate și logit-urile
  pe care le dă `unelte/inferenta_bruta.py` pe el — ca sesiunea OS să-și verifice motorul Rust fără să vadă codul Kronos. Fără greutăți
  reale în hub. (2) Exportă cel mai bun model curent (#441 sau rezultatul S38, dacă e confirmat) în **KGR1 Q8_0** cu `unelte/exporta_greutati.py`
  și pune fișierul ca **Release** în repo-ul privat `cyberspace` (nu în hub, nu în repo-urile publice), cu suma SHA-256 notată în
  `integrare/kronos/MODEL.md` (numele modelului, mărimea, suma, 3 texte cu primele 5 simboluri generate greedy, ca test pe hardware).
- istoric: preluat (2026-10-27 23:15, supraveghetor) — S39 în `plan/coada.md` din cyberspace, `aprobat`; partea A (model minuscul + vectori) acum, doar procesor; partea B (exportul + Release privat) după S38. Executantul nu scrie în hub: pregătește `integrare/kronos/` în cyberspace, iar supraveghetorul îl copiază aici. 2026-10-28 02:15: `integrare/kronos/format_greutati.md` copiat aici (specificația KGR1); vectorii și `MODEL.md` după S39. 2026-10-28 05:15: la S39 s-a adăugat și descrierea tokenizerului `tokenizer.bpe` în specificație (cererea OS pentru P6-27b); S39 întârzie: workstation-ul Kronos nu raportează din 27 oct 19:34.
- stare: gata, cu o limită (2026-10-28 08:20, supraveghetor) — S39 `gata` în cyberspace; în `integrare/kronos/`: specificația cu tokenizerul, `vectori/`, `README.md`, `MODEL.md`. **Rezolvat 28 oct 13:08:** Release-ul privat `kronos-kgr1-459` e publicat de Adrian (fișierul 110.859.040 octeți, sha256 verificat). ~~Limită:~~ Release-ul privat `kronos-kgr1-459` nu era făcut (comanda `gh` cere aprobare în rularea programată; o rulează Adrian).
- rezultat: modelul #459 (S38 CONFIRMAT) exportat în KGR1 Q8_0 (110.859.040 octeți, SHA-256 `e80618b4…382e`), cu vectorii de test pe un model minuscul (F32 față de PyTorch 4,0e-6; toleranța declarată 1e-4 F32, 1e-3 Q8_0) și 3 texte greedy pentru testul pe hardware.

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
- stare: gata (preluat 2026-10-27 23:20 UTC; partea 1 = P6-27, Release os-194; partea 2 = P6-27b, terminată 2026-10-28 07:45 UTC, sesiunea OS, CI verde, Release os-195)
- rezultat: `kronos Ana are mere.` codează textul cu tokenizerul din fișier (scris de noi din specificație), continuă greedy pe toate nucleele și scrie textul; vectorii oficiali Kronos F32 și Q8_0 trec în CI (abatere ≤ 5,2e-6, argmax și greedy identice), iar memoria cheilor/valorilor e mutată în afara heap-ului ca modelul #459 să încapă — rămâne testul pe workstation cu fișierul real.

### C-26 · cyber-universe · O linie în `hw` cu adresa imaginii ecranului (cerere Cyber-GPU, doar citire)
- data: 2026-10-27 23:30 · de la: Adrian (prin centrul de comandă; delegarea din 26 oct 17:45)
- ce: Propunerea din `cyber-gpu` `integration/cyber-universe/B0_adresa-ecranului.md`: în `hw` (și deci în `raport`), o linie cu adresa fizică și
  mărimea framebuffer-ului primit de la Limine, ca driverul GPU să nu scrie peste ea. Doar citire; test în QEMU. Fă-o împreună cu C-23, ca Release-ul
  pentru fereastra de pe workstation să o conțină.
- stare: gata (preluat 2026-10-27 21:45 UTC, terminat 23:20 UTC, sesiunea OS) — P6-26; Release os-192
- rezultat: `hw` și `raport` au rândul „ecran: framebuffer la adresa fizica 0x…, mărime, LxI, pitch, bpp” (în QEMU 0x80000000, 1280x800), doar citire, testat în CI.

### C-27 · cyber-universe · Primul pas spre „OS-ul care se reglează singur”: căutare automată a celei mai bune variante de calcul pe fiecare calculator
- data: 2026-10-27 23:35 · de la: Adrian (prin centrul de comandă; delegarea din 26 oct 17:45 — direcția lui: sistemul își găsește singur cea mai
  bună folosire a hardware-ului, încearcă, păstrează sau aruncă)
- ce: **După C-23 și C-25.** `kronos-calcul --cauta`: încearcă automat variante ale operatorilor lui Kronos (mărimea blocurilor la matmul, numărul de
  fire, AVX2 / AVX-512 unde există, ordinea buclelor), **verifică fiecare variantă față de calculul de control** (o variantă greșită e aruncată, oricât
  de rapidă), măsoară timpul cu un ceas fin (TSC calibrat, nu tick-ul de 10 ms) și scrie cea mai bună configurație pentru acel calculator în
  `/usb/kronos/reglaj-<procesor>.txt`; motorul KGR1 (C-25) o folosește la pornire dacă există, altfel valorile implicite. Fără scrieri în hardware
  în afară de acel fișier. Test în QEMU: căutarea alege o configurație validă și o variantă stricată intenționat e respinsă.
  Idee: „autotuning” (tinygrad BEAM, ATLAS) — scrisă de noi.
- stare: gata (preluat 2026-10-27 23:20 UTC, terminat 2026-10-28 01:45 UTC, sesiunea OS) — P6-28; CI verde (run 194), Release os-194
- rezultat: `kronos-calcul --cauta` încearcă variantele (vectori/scalar, fire, ordinea buclelor), le verifică pe fiecare față de un calcul de control (cea stricată intenționat e respinsă în test), le cronometrează cu TSC și scrie cea mai bună în `/usb/kronos/reglaj-<procesor>.txt`, pe care `kronos` îl folosește la pornire; AVX-512 nu e încă printre variante (QEMU nu-l are).

### C-28 · kronos · E4 „Kronos-Cod”: un model separat, ~150M, doar pe cod, apoi auto-îmbunătățire cu teste care rulează
- data: 2026-10-27 23:45 · de la: Adrian (ideea lui: „150 M parametri dedicat pe coding și auto-îmbunătățire, fără română”; aprobat prin delegare)
- ce: Experiment nou, **după S38**, pe etape, fiecare cu pre-înregistrare (praguri scrise înainte) și reversibil. **Linia română (#441 și urmașii)
  rămâne neatinsă**: Kronos-Cod e un model separat (lecția E2: un model specializat uită restul; nu „recuperăm” româna peste el, le combinăm
  mai târziu prin module).
  1. **Date:** doar cod real scris de oameni, cu licențe permisive (MIT/Apache/BSD), Python + Rust (+ puțin C), fără duplicate, **fără nimic generat
     de un LLM străin**; listă de surse și licențe în `docs/`. Tokenizer BPE propriu antrenat pe cod. Examenul de cod scris înainte de antrenare și
     ținut deoparte: probleme mici cu teste unitare (din șabloane proprii + un set ascuns), măsurat pass@1 și pass@10.
  2. **Pre-antrenare:** ~150M parametri, rețeta A (cea confirmată în S34), sub 7.000 MB pe placă, ~2–3 nopți (~3 miliarde de simboluri);
     proba de 30 min întâi. Prag de pre-înregistrat de supraveghetor (ex. pass@10 pe examenul ascuns peste un nivel minim fixat înainte).
  3. **Auto-îmbunătățire** (doar dacă 2 trece pragul minim; STaR nu pornește de la zero): modelul scrie soluții la probleme generate din
     șabloane, **testele le verifică rulându-le**, se păstrează doar cele care trec, se reantrenează din punctul de plecare; 2 iterații, prag de
     câștig pe examenul ascuns. **Codul generat rulează doar într-o cutie izolată:** proces separat, fără rețea, dosar temporar, limită de timp și
     memorie, fără `os`/`subprocess`/`shutil`/acces la fișiere în afara dosarului (listă de module permise), paznicul oprește orice depășire.
  Toate ca module noi; dacă trebuie schimbat ceva în `kronos/` (nucleu) sau în examenul oficial, întreabă-l pe Adrian. Negativele sunt rezultate.
- stare: preluat (2026-10-28 02:15, supraveghetor) — S41 în `plan/coada.md` din cyberspace, `aprobat`: doar etapa 1a (surse + licențe, examenul de cod scris înainte, cutia izolată), doar procesor, fără descărcări; etapele următoare după verificarea listei de surse și cu praguri pre-înregistrate. 2026-10-28 14:25: etapa 1a gata (S41); etapa 1b (descărcarea, întâi un pilot) = S43, `propus — necesită Adrian`. 2026-10-28 20:25: Adrian a aprobat pilotul (18:00, data-limită 29 iunie 2021, fără surse cu cont); S43 oprit corect înainte de pornire (unealta de descărcare nescrisă) → S43a (unealta + teste, fără rețea) `aprobat`, apoi pilotul. 2026-10-29 02:15: S43a gata și verificat; pilotul S43 `aprobat` (doar pilotul). 2026-10-29 05:15: pilotul S43 gata și verificat (688/1.003 pachete, 0,376 GB cod curat, ~107 mil. simboluri); S46a (modul complet al uneltei, fără rețea) `aprobat`; S46 (descărcarea întreagă) `propus — necesită Adrian`.
- rezultat: (parțial, etapa 1a) 6 surse permisive fără cont (~3 mld simboluri estimate), examen de cod 200 de probleme ascunse (referințe 200/200, gol 0/200), cutie izolată testată; 999 teste trec.

### C-29 · cyber-universe · Kronos în OS e corect pe workstation, dar lent: firele nu ajută, reglajul alege greșit, încărcarea durează 30 s
- data: 2026-10-28 10:45 · de la: Adrian (prin centrul de comandă; delegarea din 26 oct 17:45)
- ce: Rezultatele, cu poze: `rezultate/2026-10-28-workstation-kronos-in-os/REZULTAT.md`. #459 dă **exact** simbolurile din `integrare/kronos/MODEL.md`
  (felicitări!), dar: (1) `--fire 1` 7,9 simb/s, `--fire 18` 6,2, `--fire 36` 4,8 — mai multe fire = mai lent; `cpu porneste` scrie „parcate: firele
  rămân pe primul nucleu”; (2) și pe 1 fir e mult sub limita memoriei; (3) `--cauta` alege „1 fir” pentru că măsoară pe o problemă minusculă;
  (4) citirea modelului ~31 s (~3,5 MB/s). Ce cer: un profil pe operații cu TSC (matvec Q8_0 pe straturi, capul de ieșire 768×16384, atenția,
  sincronizarea firelor) afișat de `kronos --profil`; fire care chiar rulează în paralel pe toate nucleele (bazin de fire pornit o dată, barieră
  fără somn de 10 ms, împărțire pe rânduri); `--cauta` măsurat **pe dimensiunile modelului** din fișierul KGR1 de pe stick (dacă există), nu pe
  probleme de jucărie; citire USB mai rapidă (cereri de mai multe sectoare). Ținte de verificat pe workstation: ≥ 50 simb/s pe 1 fir, ≥ 150 simb/s
  pe toate nucleele, citire < 10 s — aceleași simboluri ca acum (testul cu vectorii oficiali rămâne în CI). Opțional: `--repetitie <p>` (penalizare
  a repetițiilor), implicit oprit, ca rezultatul greedy să rămână neschimbat.
- stare: gata (preluat 2026-10-28 09:42 UTC, terminat 12:35 UTC, sesiunea OS) — P6-29; CI verde (run 197), Release os-197
- rezultat: cauzele găsite și reparate (calcule emulate în software → SSE2, fire noi la fiecare produs → bazin de fire, FAT reluat de la început → poziție ținută minte, derularea ecranului citea memoria plăcii → copie în RAM), plus `kronos --profil`, `--repetitie`, `--cauta` pe dimensiunile modelului și `usb citire mare` (variantă); vitezele reale se văd la testul de pe workstation din `stare/cyber-universe.md`.

### C-30 · cyber-gpu · I3 pe placa reală: lanțul VBIOS se rupe la 0x24600 („așteptat 0xaa55, citit 0x4e56”)
- data: 2026-10-28 10:50 · de la: Adrian (prin centrul de comandă; delegarea din 26 oct 17:45)
- ce: **Fereastra pe workstation de azi: I0, I1 și I2 trec pe placa reală** (`BOOT_0 = b74000a1`, `BOOT_42 = 174a1000`, GFW 0xff în 3 µs, 0 scrieri);
  **I3 pică**: semnătura `0xAA55` la 0x300000 e bună (`0xeb7faa55`), dar la 0x24600 parserul așteaptă următoarea imagine și citește `0x4e56`.
  Detalii și poze: `rezultate/2026-10-28-workstation-kronos-in-os/REZULTAT.md`. (1) Fă în `nvidia-ga104` o funcție de diagnostic **doar citire**
  care listează structura VBIOS-ului fără să-l copieze: pentru fiecare imagine găsită — offsetul, semnătura, câmpurile PCIR (vendor, device,
  tip cod, lungime, indicatorul „ultima imagine”), NPDE/„NVGI” dacă există, plus primii 16 octeți la fiecare offset unde lanțul se rupe;
  cel mult câteva sute de rânduri. Fără conținutul imaginilor (firmware NVIDIA/ASUS: nu se distribuie). (2) Fă parserul să treacă de containerele
  NVIDIA cunoscute (NVGI / NPDE) dacă documentația publică o susține; test pe o imagine sintetică care reproduce situația. Totul în SIMULARE,
  apoi verificăm la următoarea fereastră. Nicio scriere în placă.
  **Și:** raportul OS arată framebuffer-ul la `0xe0000000` (9 MiB, 1920×1080) = începutul BAR1 al plăcii — de ținut cont la I9/I10 (nu se scrie acolo).
- stare: gata (preluat 2026-10-28 13:35, terminat 13:50, sesiunea Cyber-GPU 13) — commit-uri `d03ce39`, `0e14990`, `4538f90` pe `g0-g2-fundatie`, CI verde; doar SIMULARE
- rezultat: diagnosticul VBIOS doar citire (`vbios_diag`, pentru `gpu vbios --detalii`) e gata, iar parserul acceptă acum imaginile cu semnătura „NV” (0x4e56), ca nouveau — în simulare lanțul de tip workstation trece I3 și FWSEC e găsit; pe placa reală se verifică la fereastra următoare.

### C-31 · cyber-universe · `gpu vbios --detalii` (după C-30)
- data: 2026-10-28 10:50 · de la: Adrian (prin centrul de comandă; delegarea din 26 oct 17:45)
- ce: Când Cyber-GPU (C-30) are funcția de diagnostic VBIOS: mută fixarea pe commit-ul lor nou (doar adăugări), expune-o ca `gpu vbios --detalii`
  (pe ecran și în `raport`), doar citire, cu „0 scrieri” afișat; test în CI cu `--sim`; Release nou pentru următoarea fereastră pe workstation.
  Împreună cu C-29 (viteza lui Kronos), ca un singur stick să le testeze pe amândouă.
- stare: gata în cod, Release blocat (2026-10-28 17:50 UTC, sesiunea OS; P6-31) — Release-ul nu se poate face: GitHub Actions oprit (repo privat, fără minute; run 199). Istoric: preluat (2026-10-28 17:05 UTC, sesiunea OS; P6-31, din copia `cyber-gpu.bundle`) — deblocat 2026-10-28 19:00 de centrul de comandă; B-005 rezolvat altfel: copia Git completă a `cyber-gpu` (ramura `g0-g2-fundatie`, vârf `8313973`, conține și `4538f90`) e în hub, `integrare/cyber-gpu/snapshot/cyber-gpu.bundle` (instrucțiuni în README-ul de lângă). Construiește din ea; nu mai e nevoie de acces direct la repo-ul privat. Istoric: blocat (preluat 2026-10-28 12:50 UTC, sesiunea OS; P6-31) — `cyber-gpu` e privat și sesiunea OS nu are acces la el, deci nu se poate descărca biblioteca nouă și nici construi OS-ul (B-005 în `cyber-universe/docs/BLOCKERS.md`, variantele în `stare/cyber-universe.md`)
- rezultat: `gpu vbios --detalii` (doar citire, „0 scrieri”, și în `raport`) e în `cyber-universe` `ba572c6`, Cyber-GPU fixat pe `8313973`, testat în SIMULARE (imaginile „NV” la 0x24600) și în QEMU; lipsește doar stick-ul nou, care așteaptă decizia lui Adrian despre CI/Release (`stare/cyber-universe.md`).

### C-32 · cyber-universe · Licența devine proprietară pentru codul nou („toate drepturile rezervate”)
- data: 2026-10-28 14:30 · de la: Adrian (prin centrul de comandă)
- ce: Adrian vrea să-și protejeze codul. Versiunile publicate până acum (până la commit-ul `0bf1303` inclusiv) rămân MIT — asta nu se poate retrage.
  De la următorul commit: (1) `LICENSE` înlocuit cu o licență proprietară scurtă („Copyright (c) 2026 Adrian. Toate drepturile rezervate.
  Nicio utilizare, copiere, modificare sau distribuire fără acordul scris al autorului.”), cu o notă clară: „Versiunile până la commit-ul 0bf1303 au fost
  publicate sub licența MIT.”; (2) o decizie nouă în `docs/DECISIONS.md` care o înlocuiește explicit pe cea cu MIT; (3) `CLAUDE.md` §6 și
  README-urile actualizate (regula clean-room rămâne: nimic GPL copiat; nimic MIT străin fără notificarea lui păstrată); (4) componentele străine
  păstrează licențele lor (ex. crate-ul generat din antetele NVIDIA MIT, cu notificarea NVIDIA). (5) Firmware-ul NVIDIA: nu-l distribuim noi
  niciodată (nici în repo, nici în arhivele de stick); Adrian îl descarcă singur — notează asta, pentru că argumentul de redistribuire din
  `cyber-gpu/docs/RESEARCH_I4_I8.md` §5.1 presupunea un OS cu licență OSI. Nu schimba nimic altceva. (Vizibilitatea repo-ului o decide Adrian
  separat; dacă devine privat, testele GitHub Actions se pot opri — atunci nu le repara prin plată, doar notează și bazează-te pe testele din sesiune.)
- stare: gata (preluat 2026-10-28 12:47 UTC, terminat 12:50 UTC, sesiunea OS) — P6-30, commit `a2c0db3`
- rezultat: `LICENSE` proprietar („toate drepturile rezervate”) cu nota că versiunile până la `0bf1303` au fost MIT, decizia D-015 înlocuiește D-005, CLAUDE.md §6, README-urile și regulile clean-room actualizate, firmware-ul NVIDIA notat ca nedistribuit de noi; CI nu a rulat (repo privat, fără minute).

### C-33 · cyber-gpu · Aceeași schimbare de licență (proprietară pentru codul nou)
- data: 2026-10-28 14:30 · de la: Adrian (prin centrul de comandă)
- ce: Ca la C-32, pe ramura `g0-g2-fundatie`: repo-ul n-are încă fișier `LICENSE` (GitHub nu vede nicio licență), dar documentele spun MIT
  (`docs/PROVENANCE.md`). Versiunile până la commit-ul `8313973` inclusiv rămân MIT. Adaugă `LICENSE` proprietar cu aceeași notă istorică,
  actualizează `PROVENANCE.md` și README-urile; crate-ul generat din antetele NVIDIA păstrează notificarea MIT a NVIDIA; notează în §5.1 din
  `RESEARCH_I4_I8.md` că firmware-ul îl descarcă Adrian, noi nu-l distribuim. Nu schimba nimic altceva.
- stare: gata (preluat 2026-10-28 17:30 UTC, terminat 17:32 UTC, sesiunea Cyber-GPU 14) — commit `f440f6f` pe `g0-g2-fundatie`; teste verzi în sesiune, CI GitHub nu pornește (repo privat)
- rezultat: `LICENSE` proprietar („toate drepturile rezervate”) cu nota că versiunile până la `8313973` au fost MIT; antetele NVIDIA generate păstrează MIT-ul NVIDIA; `PROVENANCE.md`, README-urile și §5.1 din `RESEARCH_I4_I8.md` (firmware-ul îl descarcă Adrian, noi nu-l distribuim) actualizate; codul neschimbat.

### C-34 · cyber-gpu · După fiecare push: actualizează copia privată din hub pentru sesiunea OS
- data: 2026-10-28 19:00 · de la: Adrian (prin centrul de comandă; delegarea din 26 oct 17:45)
- ce: De când `cyber-gpu` e privat (28 oct 14:33), sesiunea OS nu-l mai poate clona (B-005 în cyber-universe). Centrul de comandă a pus o copie
  în hub: `integrare/cyber-gpu/snapshot/cyber-gpu.bundle` + `VERSIUNE.txt` + `README.md`. **La sfârșitul fiecărei sesiuni în care ai urcat ceva
  pe `g0-g2-fundatie`:** `git bundle create integrare/cyber-gpu/snapshot/cyber-gpu.bundle g0-g2-fundatie` (ramura locală la zi cu origin),
  verifică-l cu `git bundle verify` și cu o clonare de probă, rescrie `VERSIUNE.txt` (`g0-g2-fundatie <commit scurt> <ora UTC>`), commit în hub
  împreună cu starea ta. Fără firmware, fără date personale. Dacă nu mai poți citi `cyber-universe` (tot privat), e în regulă: e doar context,
  starea lui e în `stare/cyber-universe.md`. Fă și C-33 (licența), dacă n-ai făcut-o.
- stare: gata (preluat 2026-10-28 17:30 UTC, prima actualizare 17:34 UTC, sesiunea Cyber-GPU 14) — se repetă la fiecare sesiune cu push
- rezultat: `cyber-gpu.bundle` refăcut la fiecare sesiune cu push; ultima dată la vârful `e40e98e` (2026-10-31 11:35 UTC, sesiunea 27: `git bundle verify` OK; față de `647398c` doar documente, codul neschimbat, fără firmware), `VERSIUNE.txt` rescris.

### C-35 · cyber-universe · Stick nou fără GitHub Actions: construiește în sesiune și pune arhiva în hub
- data: 2026-10-28 22:20 · de la: Adrian (prin centrul de comandă; delegarea din 26 oct 17:45 — varianta 3 din `stare/cyber-universe.md`, fără bani, repo-urile rămân private)
- ce: Construiește în sesiune imaginea stick-ului cu tot ce e gata (C-29 + C-31 + C-32), la fel ca arhiva pe care o făcea Release-ul
  (`stick-cyber-universe-os-<nr>.zip`, **fără** modelul Kronos și fără firmware NVIDIA), și pune-o în hub în `integrare/cyber-universe/stick/`
  + `VERSIUNE.txt` (număr, commit, ora UTC, SHA-256 al arhivei) + un `README.md` scurt (ce e nou față de `os-197`). Ține doar ultima arhivă
  (înlocuiește-o pe cea veche, nu le aduna). Rulează înainte testele QEMU. Centrul de comandă i-o trimite lui Adrian.
  Repetă la fiecare schimbare care ajunge pe stick, până se rezolvă CI-ul.
- stare: gata (preluat 2026-10-28 20:25 UTC, gata 21:20 UTC, sesiunea OS) — P6-32
- rezultat: stick-ul `os-1001` (commit `02f2043`, C-29 + C-31 + C-32, fără model și fără firmware) e în `integrare/cyber-universe/stick/` cu `VERSIUNE.txt` și `README.md`, după suita QEMU și o pornire de probă; se repetă cu `tools/stick-hub.sh` la fiecare schimbare care ajunge pe stick.

### C-36 · cyber-gpu · Firmware-ul 570.144 e la Adrian: pregătește fereastra I3 → I4
- data: 2026-10-28 22:30 · de la: Adrian („ok atunci cu firmware de la ei… spune-i lui gpu”, prin centrul de comandă)
- ce: Centrul de comandă a descărcat cele 4 fișiere `*-570.144.bin` din linux-firmware (commit `050f0a1e3a76`) și i le-a trimis direct lui Adrian,
  cu `LICENCE.nvidia`; toate cele 4 SHA-256 se potrivesc cu `docs/COMPATIBILITATE_FIRMWARE.md`. **Nu sunt în niciun repo și nici în hub.**
  Adrian le pune pe stick la `firmware/nvidia/ga102/gsp/`. Fereastra posibilă: 29 oct, cu Adrian de față.
  Pregătește pașii exacți pentru fereastră, în ordine: (1) `gpu vbios` + `--detalii` (I3, doar citire); (2) dacă I3 trece: citirea și
  verificarea fișierelor de pe stick (sume, antete; tot fără scrieri în placă); (3) ce urmează doar dacă (1) și (2) trec, cu ce scrie în
  placă marcat clar și cu oprire sigură. Scrie-i în `stare/cyber-gpu.md` la „nevoie de Adrian”, în română simplă.
  Dacă pasul (2) cere cod nou în OS, scrie o comandă-propunere pentru `cyber-universe` în `idei/` (centrul de comandă o aprobă).
- stare: gata (preluat 2026-10-28 20:35 UTC, terminat 20:50 UTC, sesiunea Cyber-GPU 15) — commit-uri `2c9c90c`, `51848d6` pe `g0-g2-fundatie`; doar SIMULARE
- rezultat: pașii ferestrei sunt în `cyber-gpu/docs/FEREASTRA_C-36.md` și pe scurt în `stare/cyber-gpu.md` (verificarea fișierelor de pe stick e scrisă și testată în simulare, iar comenzile din OS sunt propuse în `idei/2026-10-28_cyber-universe_gpu-firmware-fwsec.md`).

### C-37 · cyber-universe · CI: verificarea accesului la cyber-gpu pică din cauza credențialelor lăsate de `actions/checkout`
- data: 2026-10-29 00:15 · de la: Adrian (prin centrul de comandă; delegarea din 26 oct 17:45)
- ce: Adrian a făcut cheia `CYBER_GPU_TOKEN` (fine-grained, doar `cyber-gpu`, Contents: Read-only) și a pus-o ca secret. Pasul
  `tools/ci-cyber-gpu-acces.sh` tot pică („GitHub refuza cyber-gpu”, run 40774740427, încercarea 3, 22:12 UTC). Cauza probabilă:
  `actions/checkout@v4` (pasul de la rândul 22 din `ci.yml`) salvează în configul local al depozitului un antet
  `http.https://github.com/.extraheader` cu `github.token`, iar `git ls-remote` rulat în dosarul de lucru trimite acel antet în locul
  cheii din URL → GitHub vede doar tokenul workflow-ului, care nu vede `cyber-gpu`. Reparația propusă: `persist-credentials: false` la acel
  checkout (sau verificarea și fetch-ul cu `git -c http.https://github.com/.extraheader=`), apoi rulează CI-ul și confirmă că trece de pas.
  Dacă și după reparație GitHub refuză, scrie mesajul exact în `stare/cyber-universe.md` (atunci e cheia, și o verifică Adrian).
  Nu afișa niciodată cheia în jurnal.
- stare: gata (preluat 2026-10-28 22:15 UTC, terminat 2026-10-29 00:30 UTC, sesiunea OS) — P6-34; CI verde (run 205), Release `os-205`
- rezultat: cheia `CYBER_GPU_TOKEN` ajunge acum la GitHub (checkout-ul nu mai lasă tokenul lui în urmă), iar testul `phase4`, care pica după ordinea fișierelor de pe mașina CI, e reparat; CI verde și Release nou `os-205`.

### C-38 · cyber-universe · `gpu fwsec` + `gpu firmware` (doar citire), pentru fereastra C-36
- data: 2026-10-29 08:25 · de la: Adrian (prin centrul de comandă; delegarea din 26 oct 17:45)
- ce: exact propunerea `idei/2026-10-28_cyber-universe_gpu-firmware-fwsec.md`: mută fixarea cyber-gpu pe `2c9c90c` sau mai nou (copia din hub sau
  direct, cu `CYBER_GPU_TOKEN` în CI), adaugă `gpu fwsec [--sim]` și `gpu firmware [--sim]` + 2 rânduri în `gpu plan`, testele QEMU din propunere,
  apoi Release nou prin CI (os-206+). Nimic nu scrie în placă; firmware-ul nu intră în repo, în teste sau în arhiva stick-ului. **Cu prioritate:
  Adrian poate merge la workstation chiar azi.**
- stare: gata (2026-10-29 10:25, sesiunea OS) — P6-35
- rezultat: `gpu fwsec` și `gpu firmware` (doar citire, `--sim` în testele QEMU, rândurile 5c/5d în `gpu plan`, Cyber-GPU pe `2c9c90c`) sunt în Release `os-206` (CI verde) și în arhiva de rezervă `os-1002` din hub; firmware-ul nu e nici în repo, nici în arhivă.

### C-39 · cyber-gpu · Parserul antetelor firmware greșește pe 3 din 4 fișiere reale (rezultatul de pe workstation, 29 oct)
- data: 2026-10-29 12:45 · de la: Adrian (prin centrul de comandă; delegarea din 26 oct 17:45)
- ce: Pe placa reală, I3 și I3b trec (`rezultate/2026-10-29-workstation-kronos-gpu/REZULTAT.md`). La `gpu firmware`, fișierele sunt oficiale 4/4,
  dar `booter_load`, `booter_unload` și `bootloader` dau „antet NECITIT: bin_size diferit de mărimea fișierului”; `gsp` (ELF) e citit corect.
  Repară `fw_hdr` după structurile reale (antetele NVIDIA MIT 570.144: `bin_size` nu e neapărat mărimea întregului fișier — ex. antetul + descrierea
  + semnăturile se adaugă; verifică pe ce se măsoară), cu teste pe fișiere sintetice cu aceeași formă. Nu pune fișierele reale în repo și nu le
  analiza dincolo de antet (licența). Apoi actualizează bundle-ul din hub (C-34) și scrie în `stare/cyber-gpu.md` ce trebuie să vadă Adrian la
  fereastra următoare (`criteriul I4: TRECE`). Pasul următor pe placă (I5+) îl propui separat, cu ce scrie în placă marcat clar.
- stare: gata (preluat 2026-10-29 10:44 UTC, terminat 11:00 UTC, sesiunea Cyber-GPU 18) — commit-uri `ef97110`, `eaabbdd`, `aee06c4` pe `g0-g2-fundatie`; bundle la `aee06c4`; doar SIMULARE
- rezultat: parserul citește acum antetele cu forma fișierelor oficiale (`bin_size` nu e mărimea fișierului, iar numărul de semnături Booter se ia printr-o adresă), testat pe fișiere de probă cu exact aceleași antete; OS-ul trebuie doar să mute fixarea (`idei/2026-10-29_cyber-universe_gpu-fixare-c39.md`), iar pasul următor pe placă e în `cyber-gpu/docs/FEREASTRA_C-39.md`.

### C-40 · cyber-universe · Kronos în OS: frânele măsurate pe workstation (sincronizarea firelor, afișarea pe ecran)
- data: 2026-10-29 12:45 · de la: Adrian (prin centrul de comandă; delegarea din 26 oct 17:45)
- ce: Cifrele de pe workstation (`rezultate/2026-10-29-workstation-kronos-gpu/`): 69,5 simb/s pe 18 fire, dar **așteptarea firelor = 62,6 %**
  (78,9 % pe 36 de fire) și **afișarea pe ecran = 14–38 %**. După C-38 (gata), după ce termini ce lucrezi: (1) sincronizare mai ieftină între fire
  (de ex. o singură împărțire pe strat în loc de una pe produs, așteptare activă scurtă în loc de adormire, sau unirea produselor q/k/v și fc);
  (2) textul pe ecran scris o dată pe rând/la sfârșit, nu simbol cu simbol (sau opțiunea `--fara-ecran` la `--profil`); (3) alegerea
  automată a numărului de fire din `--cauta` să includă și costul sincronizării. Ținta rămâne ≥ 150 simb/s; simbolurile trebuie să rămână
  identice (testele QEMU + vectorii KGR1). Apoi Release nou și pașii pentru Adrian (doar `--profil --n 64 Buna ziua`).
- stare: gata (2026-10-29 14:45, sesiunea OS) — P6-36
- rezultat: nucleele libere sunt trezite imediat când un fir are de lucru (înainte așteptau până la 10 ms — cauza principală a așteptării), 49 de sincronizări pe simbol în loc de 61, textul pe ecran pe rânduri (+ `--fara-ecran`), `--cauta` cu media a 5 treceri; simboluri identice, CI verde, Release `os-208` — viteza reală se vede la fereastra următoare (`run kronos --profil --n 64 Buna ziua`).

### C-41 · cyber-universe · „Claude din interior” fără API: OS-ul legat de sesiunile Claude prin GitHub („cutia poștală”), etapa 1 în simulare
- data: 2026-10-29 13:35 · de la: Adrian („nu îmi place cu API”; ținta principală) prin centrul de comandă, delegarea din 26 oct 17:45 — înlocuiește varianta cu API din 13:25
- ce: după C-40. Claude rămâne în sesiunile Claude Code din abonamentul lui Adrian (cum lucrăm deja); OS-ul de pe workstation devine „mâinile și ochii” lor pe hardware,
  doar prin GitHub, fără cheie API și fără cost în plus. Pași mici, plan în `docs/plans/` (fază nouă în ROADMAP):
  (1) `actualizeaza` merge și cu repo-ul privat: citește un token doar-citire de pe stick (`chei/github-citire.txt`), nu-l scrie nicăieri;
  (2) modul `asculta`: la N minute, OS-ul citește din hub un fișier de sarcini pentru hardware (`hardware/sarcini.md`, scris de sesiuni), le rulează **doar dintr-o listă
  albă de comenzi sigure** (`run kronos …`, `kronos-calcul --cauta`, `gpu vbios/fwsec/firmware`, `raport`, `actualizeaza` + repornire pe Release verificat), niciodată ceva
  care scrie în placa video (acelea cer în continuare Adrian de față și o tastă apăsată fizic);
  (3) rezultatele (raportul, cifrele) le urcă înapoi în hub cu un al doilea token, cu drept de scriere **doar pe hub** (`chei/github-hub.txt`), într-un dosar `rezultate/auto/`;
  (4) revenire sigură: dacă Release-ul nou nu pornește sau pică testele, la repornire se întoarce la cel vechi; `os-187` rămâne punctul de revenire.
  Toate testate în QEMU cu un GitHub fals pe gazdă, fără tokenuri reale. Tokenurile le face Adrian când e gata (centrul de comandă îi dă pașii).
- stare: **amânat** (Adrian, 29 oct 13:28: „mai e până acolo; replanificăm când suntem aproape”) — **nu se preia**; rămâne doar ca idee pentru replanificare

### C-42 · cyber-universe · Fixarea cyber-gpu după C-39 (antetele firmware citite corect) + Release pentru fereastra următoare
- data: 2026-10-29 21:45 · de la: Adrian (prin centrul de comandă; delegarea din 26 oct 17:45)
- ce: exact propunerea `idei/2026-10-29_cyber-universe_gpu-fixare-c39.md`: mută fixarea cyber-gpu pe `aee06c4` sau mai nou (doar adăugări față de `2c9c90c`),
  testele QEMU (`gpu firmware --sim` → `criteriul I4: TRECE (… antete citite 4/4)`), CI verde → Release nou (os-209+). Nimic nou care scrie în placă.
- stare: gata (2026-10-29 23:06, sesiunea OS) — P6-37
- rezultat: Cyber-GPU fixat pe `aee06c4`, `gpu firmware --sim` dă „criteriul I4: TRECE (fisiere oficiale 4/4, antete citite 4/4)” cu mărimile fișierelor reale, suita QEMU și CI verzi → Release `os-209`, gata pentru fereastra următoare (`gpu firmware` pe workstation).

### C-43 · kronos · „da S46” — descărcarea întreagă a codului pentru Kronos-Cod
- data: 2026-10-29 21:46 · de la: **Adrian** (scris direct: „da s46”), transmis de centrul de comandă
- ce: S46 din `plan/coada.md`, exact cum e scris acolo (comanda din raportul S46a, `--limita-ore 10` pe noapte, aceleași reguli ca pilotul: data-limită
  29 iunie 2021, fără surse cu cont, licențe permisive, proveniență pe fișier, oprire sub 40 GB liberi). Fără placă; poate rula în paralel cu S45.
  Tokenizerul pe cod rămâne pentru un „da” separat.
- stare: gata (2026-10-31 11:15, supraveghetor) — S46 în `plan/coada.md`; istoric: preluat 2026-10-29 21:50
- rezultat: descărcarea s-a încheiat în 2 nopți, fără erori: 3,87 GB cod curat (~1,10 mld simboluri, sub estimarea de 3–6 mld), licențe permisive, 61 GB liberi pe disc; tokenizerul pe cod așteaptă un „da” separat.
- notă (2026-10-29 23:15, supraveghetor): executantul ia sarcinile pe rând, deci S46 pornește după S45, pe la 02:00 (nu în paralel). Nimic descărcat încă.
- notă (2026-10-30 02:15, supraveghetor): S46 a pornit la 00:30 (bucata 1 din ~3, `--limita-ore 10`).
- notă (2026-10-30 11:15, supraveghetor): bucata 1 gata (cod 0, 10 ore): 3,73 GB cod curat, ~1,07 mld simboluri; bucata 2 în noaptea 30→31, după S51.
- notă (2026-10-31 02:15, supraveghetor): bucata 2 a pornit la 02:00 (după S51), ~10 ore.

### C-44 · kronos · „da #477” — #477 îl înlocuiește pe #459 (interfață + pachetul pentru OS)
- data: 2026-10-31 13:50 · de la: **Adrian** (scris direct: „da la amândouă”), transmis de centrul de comandă
- ce: (1) #477 devine modelul din interfață (în locul lui #459); #459 rămâne păstrat ca rezervă. (2) Export KGR1 Q8_0 al lui #477
  (`lucru/export/kronos_477_q8_0.kgr` + SHA-256), vectorii de control noi și `integrare/kronos/MODEL.md` actualizat în hub (fără greutăți în hub/repo).
  (3) Release-ul privat `kronos-kgr1-477`: dacă executantul nu-l poate publica singur, scrie în `stare/kronos.md` pașii exacți pentru Adrian (ca la #459).
  Toate testele trebuie să treacă; examenul și paznicul neatinse.
- stare: gata (2026-10-31 14:20, supraveghetor) — S54 în `plan/coada.md`; istoric: preluat 2026-10-31 14:15
- rezultat: #477 exportat KGR1 Q8_0 (110.859.040 octeți, SHA-256 `bcbe8187…3963`), modelul implicit al modulelor Kronos, #459 păstrat ca rezervă, `integrare/kronos/MODEL.md` arată #477 (C-46 poate porni); Release-ul `kronos-kgr1-477` îl face Adrian (comanda în `MODEL.md` și în `stare/kronos.md`), 1126 teste trec.

### C-45 · kronos · „da tokenizer cod” — tokenizerul Kronos-Cod din descărcarea S46
- data: 2026-10-31 13:50 · de la: **Adrian** (scris direct: „da la amândouă”), transmis de centrul de comandă
- ce: etapa următoare din `docs/KRONOS_COD_plan.md`: tokenizerul pe codul curat din `lucru/kronos_cod/complet/` (3,87 GB, ~1,1 mld simboluri), cu
  pre-înregistrare (mărimea vocabularului, cum se măsoară — ex. octeți/simbol pe examenul de cod ascuns, fără să-l deschidă), procesor; apoi propunerea
  pentru prima antrenare Kronos-Cod pe placă (planul, orele, pragurile) — antrenarea pornește prin regulile obișnuite ale cascadei (granițele din
  REGULI_CASCADA.md; dacă iese din ele, `propus — necesită Adrian`). Linia română (#477) rămâne separată și neatinsă.
- stare: gata (2026-10-31 17:15, supraveghetor) — S55 în `plan/coada.md`; istoric: preluat 2026-10-31 14:15
- rezultat: tokenizerul de cod (32.768 simboluri) BUN: 3,46 octeți/simbol, +22,1 % față de w2, refacere 100 % identică, setul tokenizat (1,08 mld simboluri); prima antrenare pe placă = S58, `propus — necesită Adrian` (linie de model nouă), pregătirea ei S57 aprobată.

### C-46 · cyber-universe · Modelul #477 pe stick (după C-44)
- data: 2026-10-31 13:50 · de la: **Adrian** („da #477”), prin centrul de comandă
- ce: după ce `integrare/kronos/MODEL.md` arată #477 (C-44): suma SHA-256 nouă și vectorii lui #477 în testele OS, fișierul așteptat pe stick
  `kronos/kronos_477_q8_0.kgr` (+ `.sha256`), cu #459 acceptat în continuare dacă e singurul de pe stick; Release nou. Nu începe înainte de C-44.
- stare: gata (2026-10-31 16:05, sesiunea OS) — P6-38; istoric: preluat 2026-10-31 14:45
- rezultat: `kronos` alege din `/usb/kronos/` întâi `kronos_477_q8_0.kgr` (SHA-256 `bcbe8187…3963` în cod), apoi #459 ca rezervă, iar `run kronos --control` verifică cele 3 texte ale lui #477; teste QEMU și CI verzi → Release `os-210` (lipsește doar fișierul #477 pe stick, după Release-ul `kronos-kgr1-477` făcut de Adrian).

### C-47 · kronos · „da S58” — prima antrenare Kronos-Cod (`cod_c1`, o noapte pe placă)
- data: 2026-10-31 20:53 · de la: **Adrian** (scris direct: „da s58”), transmis de centrul de comandă
- ce: S58 din `plan/coada.md`, exact cum e scrisă acolo (pre-înregistrarea înainte, proba de 10 minute, 10 ore noaptea, pragurile ÎNVAȚĂ / NU ÎNVAȚĂ / NECLAR
  neschimbate), după ce S57 și S59 sunt `gata`. Prima noapte potrivită. **Mâine (1 nov) Adrian poate fi la workstation pentru fereastra OS/GPU:
  dacă e acolo, antrenarea se oprește întâi** (sau pornește după fereastră). Nu atinge #477, linia română, `kronos/`, examenul, paznicul.
- stare: preluat (2026-10-31 20:56, supraveghetor) — S58 în `plan/coada.md`; întâi S60 (unelte, procesor); proba în noaptea 31 oct, cele 10 ore din 1 nov 19:00 (după fereastra OS/GPU, dacă e cazul)
  - 2026-10-31 23:15: S60 gata; pre-înregistrarea și proba de 10 minute gata (6.078 MB, 63 °C); cele 10 ore rămân pentru 1 nov 19:00.
  - 2026-11-01 02:15: S61 (comparația inițializării) AJUTĂ; cele 10 ore pornesc 1 nov 19:00 cu `cod_c1`, sau cu `cod_c1_init002` dacă Adrian alege.

### C-48 · cyber-universe · Kronos în OS: produsul „proiecție” și afișarea pe ecran (rezultatele din 1 nov)
- data: 2026-11-01 11:55 · de la: Adrian (prin centrul de comandă; delegarea din 26 oct 17:45)
- ce: `rezultate/2026-11-01-workstation-477-i4/`: 123 simb/s fără ecran (ținta 150). **Produsul „proiecție” ia 46,6 % din timp la doar 2,1 GB/s**
  (celelalte 17–52 GB/s) și „așteptarea firelor” e 62 % → probabil proiecția nu e împărțită pe fire (sau e împărțită pe dimensiunea mică).
  (1) împarte proiecția pe toate firele ca celelalte produse (și include-o în `--cauta`); (2) afișarea pe ecran: 45,7 % din timp cu ecran —
  scrie textul pe rânduri întregi / în bloc, fără redesenare pe fiecare simbol; (3) simboluri identice (vectorii #477 + `--control`).
  Ținta: ≥ 150 simb/s fără ecran și ≥ 120 cu ecran. Apoi Release nou + pașii scurți pentru Adrian.
- stare: preluat (2026-11-01 12:45, sesiunea OS) — P6-39
- stare: gata (2026-11-01 13:35) — rezultat: proiecția rulează acum pe firele împărțirii pe capete (numărul ei de fire e căutat de `--cauta`), textul merge pe ecran în bloc și consola mută ecranul o dată pe bloc, simbolurile identice; Release `os-211` (pașii pentru Adrian în `stare/cyber-universe.md`).

### C-49 · cyber-gpu · I4 TRECE pe placa reală — propune fereastra următoare (primele scrieri)
- data: 2026-11-01 11:55 · de la: Adrian (prin centrul de comandă; delegarea din 26 oct 17:45)
- ce: `gpu firmware` pe workstation: **criteriul I4: TRECE (4/4, antete 4/4)**, 0 accese la placă. Toate verificările de citire (I0–I4) sunt acum dovedite pe placa reală.
  Scrie în `stare/cyber-gpu.md` planul ferestrei următoare, în ordine și cu oprire sigură: (a) proba tinygrad (jurnalul de aur; necesită stick Ubuntu + laptop)
  și/sau (b) prima scriere a driverului nostru (I5 Bus Master / I6 FWSEC), cu exact ce se scrie, ce nu se poate strica (VBIOS nu se scrie) și cum se revine
  (oprire completă). Spune care din (a)/(b) recomanzi întâi și de ce. Nimic nu se scrie în placă fără Adrian de față; dacă e nevoie de cod nou în OS, propunere în `idei/`.
- stare: gata (2026-11-01 12:20, sesiunea Cyber-GPU 30)
- rezultat: (înlocuit de C-51: fără tinygrad) planul e în `stare/cyber-gpu.md` și `cyber-gpu/docs/FEREASTRA_C-49.md` — inițial recomandam (a) proba tinygrad (jurnalul de aur, nu depinde de codul nostru), apoi (b) Bus Master + I6 FWSEC-FRTS (18 registre GSP, VBIOS-ul nu se poate scrie, revenire prin oprire completă); în plus, verificarea I6 doar citire pentru OS (propunerea `idei/2026-11-01_cyber-gpu-i6-in-os.md`).

### C-50 · kronos · „da init002” — S58 pornește cu `config/cod_c1_init002.toml`
- data: 2026-11-01 11:55 · de la: **Adrian** (scris direct: „da init002”), transmis de centrul de comandă
- ce: antrenarea S58 din 1 nov 19:00 folosește configurarea `cod_c1_init002` (inițializarea 0,02, verificată la S61: AJUTĂ) în locul lui `cod_c1`.
  Pre-înregistrarea S58 se completează/actualizează ÎNAINTE de pornire cu configurarea aleasă; pragurile ÎNVAȚĂ / NU ÎNVAȚĂ / NECLAR rămân neschimbate.
- stare: preluat (2026-11-01 11:55, supraveghetor) — S58 în `plan/coada.md`: pașii 3–4 cu `config/cod_c1_init002.toml`, pre-înregistrarea actualizată înainte; pornire 1 nov 19:00

### C-51 · cyber-gpu · Fără Ubuntu pe placa reală: primele scrieri direct din Cyber Universe (completează C-49)
- data: 2026-11-01 12:00 · de la: **Adrian** („fizic doar Universe; în simulare orice”), prin centrul de comandă — vezi DECIZII 1 nov 12:00
- ce: proba tinygrad pe Ubuntu (C-20 A) se anulează. Planul din C-49 se face doar cu varianta (b): primele scrieri ale driverului nostru, din OS
  (I5 Bus Master → I6 FWSEC …), pas cu pas, fiecare cu: ce se scrie exact, ce se citește înapoi ca dovadă, criteriul de trecere, oprirea sigură.
  Ca să compensezi lipsa „jurnalului de aur” de pe placă: fă înainte, în simulare, secvența de referință cât mai completă (tinygrad și sursele
  deschise ca specificație, deja în `gpu-sim`), și adaugă în OS jurnalul fiecărei scrieri/citiri (registru, valoare, timp) ca să comparăm după fereastră.
  Dacă e nevoie de cod nou în OS (comenzi `gpu …` noi), propunere în `idei/` (centrul de comandă o aprobă).
- stare: gata (2026-11-01 12:55, sesiunea Cyber-GPU 30b)
- rezultat: planul fără Ubuntu în `cyber-gpu/docs/FEREASTRA_C-49.md` (6 pași, fiecare cu ce se scrie, ce se recitește, criteriul, oprirea); în SIMULARE: Bus Master cu recitire, FWSEC copiat din VBIOS, jurnal pe loc și verificatorul jurnalului I6; propunerea pentru OS `idei/2026-11-01_cyber-gpu-i6-in-os.md`.

### C-52 · cyber-universe · Primele scrieri în placă din OS (I6): construire + testare în QEMU/simulare
- data: 2026-11-01 19:25 · de la: Adrian (prin centrul de comandă; delegarea din 26 oct 17:45; decizia „fizic doar Universe”)
- ce: exact propunerea `idei/2026-11-01_cyber-gpu-i6-in-os.md`: fixarea cyber-gpu ≥ `d879742`; (1) `gpu pregatire-i6` (doar citire);
  (2) jurnalul fiecărei citiri/scrieri pe stick, pe loc, cu ora; (3) `gpu i6 --scrie` cu confirmare „DA” tastată, pe stick-ul de test, Bus Master
  oprit la loc la final. Teste în QEMU/simulare; **nicio rulare pe placa reală fără Adrian de față**. Release nou + pașii ferestrei pentru Adrian,
  în română simplă, cu oprirea sigură (în `stare/cyber-universe.md`). Testul de viteză `os-211` (C-48) poate intra în aceeași fereastră.
- stare: gata (2026-11-01 18:37 UTC, sesiunea OS; preluat 17:24 UTC) — P6-40
- rezultat: `gpu pregatire-i6` (doar citire), jurnalul fiecărui acces pe stick pe loc și `gpu i6 --scrie` (cu „DA”, doar în stick-ul de test `cyber-universe-gpu-scrie-usb.img`) testate în QEMU/simulare; CI verde, Release `os-212`; pașii ferestrei pentru Adrian în `stare/cyber-universe.md`.

### C-53 · cyber-universe · Bucla automată, partea OS: modul „test automat” + ceas de siguranță + scriptul pentru Windows
- data: 2026-11-01 19:45 · de la: **Adrian** („da bucla automată”), prin centrul de comandă — vezi DECIZII 1 nov 19:45
- ce (după C-52, pași mici, testați în QEMU):
  (1) la pornire, dacă pe stick există `auto/teste.txt`, OS-ul rulează pe rând comenzile din el **doar dacă sunt în lista albă** (fără nimic care scrie
      în placa video: `gpu i6 --scrie` și orice scriere sunt refuzate în modul automat), scrie `auto/raport-<data>.txt` + rezultatul pe scurt, apoi **repornește**;
      după rulare redenumește `teste.txt` în `teste-facut-<data>.txt` (ca să nu se repete la nesfârșit);
  (2) **ceas de siguranță**: dacă lista nu termină în N minute (din fișier, implicit 10), sau la blocare, repornire forțată (watchdog-ul chipsetului dacă există,
      altfel repornire prin ACPI/tastatură; testat în QEMU cu un test care se blochează intenționat);
  (3) **scriptul pentru Windows** în `tools/windows/` (PowerShell, comentat în română): copiază Release-ul nou pe stick (păstrând `kronos/`, `firmware/`, `cyber.rw`),
      scrie `auto/teste.txt`, setează **pornirea o singură dată** de pe stick (`bcdedit /set {fwbootmgr} bootsequence …`, cere administrator), repornește; și partea a doua:
      la revenirea în Windows citește `auto/raport-*.txt` de pe stick și îl pregătește pentru hub. Fără parole sau chei în script.
  (4) documentație pentru pregătirea cu Adrian (pași exacți, în română simplă): BIOS (Secure Boot oprit, Windows primul), intrare automată în Windows,
      dreptul de administrator doar pentru script. Release nou.
- stare: gata (2026-11-01 20:32 UTC, sesiunea OS; preluat 18:55 UTC) — P6-41
- rezultat: la pornire, `auto/teste.txt` → doar comenzile care citesc (scrierile în placă refuzate), raport pe loc, lista redenumită, repornire; ceas de siguranță (implicit 10 min) testat cu o comandă blocată; scriptul Windows `bucla-automata.ps1` + `docs/BUCLA_AUTOMATA.md`; testat în QEMU, CI verde, Release `os-213` (scriptul nerulat încă pe Windows → prima tură cu Adrian).

### C-54 · cyber-gpu · Pași în lanț + date reale mai multe (emulatorul să semene cu workstation-ul)
- data: 2026-11-01 19:45 · de la: **Adrian** („da bucla automată”), prin centrul de comandă — vezi DECIZII 1 nov 19:45
- ce: (1) pentru ferestrele cu Adrian: o comandă OS care încearcă pașii I6 → I7 → … pe rând, cu oprire sigură la primul eșec și jurnal complet (propunere în `idei/`
  pentru OS, dacă e nevoie de cod nou acolo); (2) pentru bucla automată (doar citire): lista de citiri fără risc care să ruleze la fiecare tur (registre de stare,
  spațiul PCI, temperaturi, ce mai ajută modelul) și unealta care le compară cu `gpu-sim`; (3) `gpu-sim` primește datele reale din `rezultate/` (fără conținutul
  firmware-ului/VBIOS NVIDIA în repo), ca simularea să ghicească mai puțin. Nimic nu scrie în placă fără Adrian.
- stare: gata (2026-11-01 20:05, sesiunea Cyber-GPU 33; preluat 19:47)
- rezultat: în SIMULARE: `gpu-sim` construit din valorile reale de pe placă (pe cele 3 rapoarte: 33 la fel, 0 diferit), turul de citire fără risc + unealta `compara_raport`, pașii în lanț cu oprire sigură; propunerea pentru OS `idei/2026-11-01_cyber-gpu-tur-si-lant.md`.

### C-55 · cyber-universe · `gpu tur` (lista albă a buclei automate) + `gpu lant` (doar cu „DA”, la fereastră)
- data: 2026-11-01 20:25 · de la: Adrian („da bucla automată”), prin centrul de comandă
- ce: exact propunerea `idei/2026-11-01_cyber-gpu-tur-si-lant.md`, împreună cu C-52 și C-53 (aceeași fixare cyber-gpu, ≥ `911e6d0`): `gpu tur` (0 scrieri) pe lista
  albă a modului automat; `gpu lant` doar cu „DA” tastat, interzis în modul automat. Teste QEMU/simulare; nimic pe placa reală fără Adrian.
- stare: gata (2026-11-01 23:20 UTC, sesiunea OS; preluat 21:50 UTC) — P6-42
- rezultat: `gpu tur` (0 scrieri, un rând `fapt …` pe fapt, pe lista albă a buclei) și `gpu lant` (doar cu „DA”, refuzat în buclă; în simulare oprit la I7 cu Bus Master pus la loc, și la eroare) — testate în QEMU, CI verde, Release `os-214`; nimic pe placa reală.

### C-56 · kronos · „Pornește acum sau cât de curând S63” — a doua noapte Kronos-Cod, chiar ziua
- data: 2026-11-02 08:46 · de la: **Adrian** (scris direct), transmis de centrul de comandă
- ce: S63 din `plan/coada.md`, exact cum e scrisă (pre-înregistrare înainte, set ascuns NOU, continuare din `lucru/cod_c1/gpt.pt`, examenele cu
  `--memorie-max 6500`), **imediat după ce S62 e `gata`** cu memoria sub 6.500 MB — fără să aștepte fereastra de noapte. Adrian e plecat până ~3 nov,
  deci nicio fereastră OS/GPU nu o întrerupe. Limitele plăcii neschimbate (7.000 MB, 83 °C).
- stare: gata (2026-11-02 23:20, supraveghetor; preluat 08:50) — sarcina S63 în `plan/coada.md`
- notă (2026-11-02 11:20, supraveghetor): S62 gata sub limită; S63 oprită 09:32 la setul ascuns (200 fără repetări nu încape) → ales setul fără suprapunere (~163, praguri pe procente), S63 din nou `aprobat`. „S63 varianta b” = 200 cu repetări, dacă Adrian preferă.
- notă (2026-11-02 14:40, supraveghetor): S63 pornită 11:38 (set ascuns nou N = 163, pre-înregistrarea urcată înainte); sfârșit ~22:00 + examene.
- rezultat: S63 a rulat până la capăt (placa max 6.013 MB / 63 °C): NECLAR — validarea 0,5004 biți/octet (S58 0,5141), pass@10 3/163 pe setul ascuns nou; urmează diagnosticul S64 (pass@k cu multe încercări).

### C-57 · kronos · Fereastra lui Adrian pe workstation: 3 nov 09:00–11:30 — placa și calculatorul libere
- data: 2026-11-03 04:35 · de la: Adrian („la ora 9 mă duc la workstation pentru teste”), prin centrul de comandă
- ce: între 09:00 și 11:30 nu porni nimic pe placă și nimic lung pe procesor (Adrian repornește în Cyber Universe: viteza Kronos, primele scrieri
  în placă, pregătirea buclei automate). Dacă rulează ceva la 08:45, oprește-l curat (reluabil). După fereastră, coada continuă normal; decizia
  despre Kronos-Cod (exerciții / memorie de cod / școala de cod) vine de la Adrian după teste.
- stare: gata (2026-11-03 14:20, supraveghetor; preluat 05:20) — fereastra respectată: S67 s-a terminat la 06:35, S68 a pornit abia la 11:39
- rezultat: între 09:00 și 11:30 Kronos n-a pornit nimic pe placă sau pe procesor; coada a continuat după 11:30 (S68).

### C-58 · cyber-gpu · I6 „NU TRECE” cu start identic — repară `check_frts` (capătul WPR2) înainte de fereastra următoare
- data: 2026-11-03 11:15 · de la: centrul de comandă (delegare Adrian 26 oct: reparație care urmează direcția lui)
- ce: pe placa reală (`rezultate/2026-11-03-workstation-os214-i6/`) `gpu i6 --scrie` a dat „verificare eșuată la 0x1fa824: așteptat 0x1ffe00, citit 0x1ffe00”.
  `gsp/falcon.rs::check_frts` compară (start, end), dar raportează doar start; start-ul e identic, deci diferă HI (0x1fa828). (1) eroarea să raporteze și HI
  (așteptat/citit); (2) verifică în documentația publică / nova-core / open-gpu-kernel-modules (doar citit, clean-room) dacă HI e capăt inclusiv (ultima pagină
  de 4 KiB) și potrivește verificarea + `gpu-sim` (`fake_gsp.rs`) cu realitatea; (3) test în simulare cu valorile reale. Propunere în `idei/` pentru noua
  fixare în OS (C-52). Nimic pe placă; la fereastra următoare Adrian copiază `raport/gpu-jurnal-002.txt` (736 rânduri) de pe stick-ul de test → confirmăm HI citit.
- stare: gata (2026-11-03 12:55, sesiunea Cyber-GPU 40; preluat 12:40)
- rezultat: în SIMULARE: eroarea numește acum registrul care diferă (LO `0x1fa824` sau HI `0x1fa828`, cu așteptat/citit), iar capătul WPR2 e acceptat și ca ultima pagină de 4 KiB (RM 570.144 și nova-core verifică doar începutul), `gpu-sim` face la fel; HI exact se confirmă din `gpu-jurnal-002.txt` cu `i6_log::wpr2_after_i6`; propunerea pentru OS `idei/2026-11-03_cyber-gpu-fixare-c58.md` (fixare ≥ `af02bea`).

### C-59 · cyber-universe · Kronos 125 simb/s: 63 % din timp firele se așteaptă — mai puține sincronizări pe simbol
- data: 2026-11-03 11:15 · de la: centrul de comandă (delegare Adrian; ținta lui: peste 150 simb/s)
- ce: profilul os-214 pe i9-10980XE: 8,2 ms/simbol, „așteptarea firelor” 62,9 %, proiecția la generare 46 % (2,09 GB/s, față de ~24 GB/s la fc/MLP),
  deși `--cauta` arată proiecția pe 32 fire la ~488 simb/s doar produsele. Afișarea pe bucăți (C-48) a mers: cu ecran 70,3 → 125,4. De făcut: află de ce
  proiecția reală e mai lentă decât în `--cauta`; mai puține bariere pe simbol (ex. lucru grupat pe strat, fire care rămân treze, împărțire fixă a rândurilor);
  `--profil` să arate numărul de bariere. Testat în QEMU, CONTROL neschimbat (aceleași simboluri). Release nou; test pe placă la fereastra următoare.
- stare: gata (2026-11-03 15:45, sesiunea OS) · sarcina P6-43
- rezultat: cauza = motorul aștepta toate cele 35 de fire și pe cele fără lucru (care își cedau procesorul); acum doar firele cu lucru, semnal „gata” pe fir, fire treze, `--profil` arată barierele (număr, µs) și `--cauta` costul unei bariere — aceleași simboluri în QEMU; viteza reală la fereastra următoare, cu Release-ul comun cu C-61.
- idee Adrian (2026-11-03 12:53), de măsurat ca variantă în `--cauta` (în P6-43 dacă încape, altfel sarcina următoare): **echipe** — 36 fire = 9 echipe × 4
  (fire vecine, aceleași 2 nuclee fizice). (1) sincronizare în 2 trepte: fiecare echipă se așteaptă intern, apoi doar cei 9 șefi între ei (nu 36 deodată);
  (2) fiecare echipă are mereu aceeași felie de rânduri din fiecare strat (greutățile ei rămân în memoria rapidă a nucleelor ei); (3) unde calculele sunt
  independente (Q/K/V, capetele atenției), echipe diferite lucrează la ele deodată, fără clopoțel între ele. Comparat cu varianta de acum; câștigă măsurătoarea.
- simulare (model, `studiu/2026-11-03_simulare-echipe/`): echipele ajută mult doar dacă vina e la trezire/adunare; dacă e la firul cel mai lent, contează „cine termină ajută la cel lent”. `--profil` să despartă cele două (adunare/trezire vs. așteptat cel mai lent).
- Adrian (12:57): în `--cauta` se măsoară **ambele** mărimi de echipă, **9×4 și 6×6** (în simulare egale, 6×6 cu ~1–3 % înainte); câștigă cea mai rapidă pe workstation.
- Adrian (13:00), idee 2 — **bucățele**: fiecare calcul împărțit în multe bucăți mici (ex. 8 pe fir = 288), un contor comun; firul liber ia următoarea bucată. În simulare doar combinația **bucățele + fire treze + echipe** trece de 150 în ambele ipoteze (~157–261). În `--cauta`: bucăți 72/144/288 × echipe 9×4/6×6 × treji.
- Adrian (13:05–13:10), ideile 3–4: **un singur bloc fără clopoțel** (contor comun, firul așteaptă doar datele calculului de dinainte) + **ajutor la cel lent** (cine a terminat ia rânduri din bucata celui lent) + **copie de rezervă** (bucata blocată de o întrerupere e refăcută de un ajutor, câștigă primul; rezultat identic). În model: ~275–300 simb/s în ambele ipoteze — cea mai bună variantă; de implementat ca țintă, celelalte rămân pentru comparație în `--cauta`. CONTROL trebuie să dea exact aceleași simboluri.
- Adrian (13:18), ideea 5 — **un fir liber**: 35 lucrători + 1 fir care primește toate întreruperile (ceas, rețea, ecran, USB; rutate prin APIC doar spre el). În model: bloc + ajutor + 1 fir liber ≈ 265–305 simb/s, aproape cât cu copia de rezervă, mult mai simplu → **varianta-țintă**; în `--cauta` și 36 fire, și cu/fără copie.
- P6-45 (sesiunea OS, 2026-11-03 16:30): ideile 1–5 de mai sus = sarcina P6-45 (`docs/plans/P6-45.md`). Gata: `--profil` desparte trezire / cel mai lent / adunare; bucățele (`kronos --bucati N`, măsurate 1/2/4/8 în `--cauta`, scrise în reglaj doar dacă bat varianta de acum). Urmează: echipe 9×4/6×6, un bloc fără clopoțel, un fir liber.
- P6-45 gata (sesiunea OS, 2026-11-03 19:50): echipe (`--echipe N`, 4 și 6 în `--cauta`), un singur bloc pe simbol fără clopoțel (`--bloc`, cine termină ultima bucată deschide etapa următoare), un procesor liber (blocul măsurat și pe toate procesoarele minus unul); aceleași simboluri în QEMU; câștigătorul îl scrie `--cauta` în reglaj. Release `os-222`. Copia de rezervă (ideea 4) nefăcută, cum s-a cerut (doar dacă rămâne o diferență mare).

### C-60 · kronos · Kronos-Cod: calea A+B+C+D (răspunsul la S66)
- data: 2026-11-03 11:45 · de la: **Adrian** („mă bazez pe tine cu decizia ABCD”), decizie a centrului de comandă prin delegare — `DECIZII.md` 2026-11-03 11:45
- ce, în ordine (fiecare cu pre-înregistrare înainte, set ascuns fără suprapunere, examene cu `--memorie-max 6500`, placa ≤ 7.000 MB / 83 °C, nimic descărcat):
  - **A — exercițiile:** după S68, setul „explicație + antet → corp” din funcțiile autonome (S67: 83.349) + cele chemabile din S68; pentru cele cu exemplu/test
    (7.182) verificarea din cutie. Doar procesor.
  - **B — o noapte pe exerciții:** continuare din `lucru/cod_c1/gpt.pt` (nu de la zero), doar noaptea; măsurat pe același set ascuns de 163 (S63) → comparabil.
  - **C — școala de cod:** Kronos scrie multe soluții la exercițiile cu test, cutia (`unelte/kronos_cod/cutie.py`) le rulează, se păstrează doar cele corecte,
    se antrenează pe ele; câteva runde, cu oprire când nu mai crește. Judecătorul (cutia + setul ascuns) rămâne în afara lui Kronos.
  - **D — memoria de cod** („rege / regat”, ideea lui Adrian): un index al funcțiilor deja descărcate (pe procesor, în paralel cu A/B); la o problemă nouă se caută
    cele mai asemănătoare 2–4 și se pun în fața lui Kronos. Măsurat cu și fără memorie pe setul ascuns, ca să se vadă dacă ajută.
  - **Nu acum:** modelul mai mare (S66 C) — doar dacă după A+B+C+D rămâne NECLAR; atunci propunere separată, fără să depășească placa de 8 GB.
- stare: preluat (2026-11-03 14:20, supraveghetor) — `plan/coada.md`: **S69** (A, exercițiile, procesor, aprobat, azi), **S70** (B, o noapte pe exerciții din `gpt.pt`, aprobat, de la 19:00, `ascuns2` 163 ca la S63), **S71** (D, memoria de cod, aprobat, 4 nov ziua), **S72** (C, școala de cod, propus, detaliat după S70). · 2026-11-04 11:20: S70 gata (NU AJUTĂ, 2/163), S71 gata (D: memoria NU AJUTĂ, proba 0/20), S72a gata (889 exerciții cu test, P_scoala 689) → S72b (C, runda 1) la noapte, S74 reperul ziua. S68 a ieșit PUȚIN (chemabile 0,77 mil. simboluri), deci exercițiile se fac din toate cele 319.430 funcții bune, cele autonome de 2 ori, amestecate 25 % cu cod obișnuit.

### C-61 · cyber-universe · Fixarea cyber-gpu ≥ `af02bea` (C-58, capătul WPR2) — împreună cu C-59 în același Release
- data: 2026-11-03 13:45 · de la: centrul de comandă (delegare Adrian; propunerea `idei/2026-11-03_cyber-gpu-fixare-c58.md`, aprobată)
- ce: exact propunerea: mută fixarea cyber-gpu ≥ `af02bea`; după `gpu i6` afișează și LO/HI brute (`falcon::check_frts_detail`); test în QEMU/simulare.
  Release nou (ideal același cu C-59), cu imaginea pentru stick-ul de test (`gpu-scrie`). Nimic pe placă fără Adrian.
- stare: gata (2026-11-03 16:15, sesiunea OS) · sarcina P6-44
- rezultat: Cyber-GPU fixat pe `3286a3b`; după I6 OS-ul scrie și LO/HI brute cu forma capătului (în simulare „capat: ultima pagina”), Release `os-219` (împreună cu C-59, cu stick-ul de test `gpu-scrie`).

### C-62 · kronos · „Antrenare din experiența proprie” — adaugă la C-60 pasul E (alegerea datelor de către Kronos)
- data: 2026-11-03 14:05 · de la: **Adrian** (ideea lui: „folosim experiența propriilor antrenamente, datele să fie tot mai puțin brute”), prin centrul de comandă; regula „de la zero” rămâne (`DECIZII.md` 14:01)
- ce: (1) **E — Kronos își alege datele:** cu un model deja antrenat (#477 pentru română, `cod_c1` pentru cod) se dă o notă fiecărei bucăți de date (cât îl mai învață:
  pierderea lui față de un model mic de referință); se păstrează ce e „de învățat” (nici prea ușor, nici zgomot), se aruncă restul; o noapte pe datele alese vs. o noapte
  pe date la întâmplare, aceeași lungime, același set ascuns → se vede cât câștigă. Doar date deja descărcate. (2) Pașii C (școala: date proprii verificate) și D (memoria)
  din C-60 rămân ca atare; împreună formează „experiența”. (3) Raport cu cifre: cât de mare ar trebui să fie un model antrenat pe date brute ca să ajungă la același scor.
  Ordinea: după A și B din C-60; pre-înregistrare înainte; limitele plăcii neschimbate.
- stare: preluat (2026-11-03 14:20, supraveghetor) — **S73** în `plan/coada.md` (propus; după S70/S72, cum cere ordinea; instrucțiunile și pragurile după verdictul S70)

### C-63 · kronos + cyber-universe · Fereastra lui Adrian pe workstation: 4 nov de la 07:00 (~2,5 h) — placa și calculatorul libere
- data: 2026-11-03 16:30 · de la: **Adrian** („mâine dimineață la ora 7:00”), prin centrul de comandă
- ce: `kronos`: S70 (noaptea pe exerciții) trebuie să se termine sau să fie oprită curat (reluabilă) până la **06:45**; între 07:00 și ~09:30 nimic pe placă
  și nimic lung pe procesor; după fereastră, coada continuă (S71). `cyber-universe`: dacă se poate, Release-ul cu P6-45 (bucățele + `--profil` despărțit)
  până la **05:30**, ca centrul de comandă să pregătească arhivele pentru stick-uri; altfel testăm `os-219`. Testul: viteza Kronos (`--cauta`, CONTROL,
  `--profil`), I6 repetat cu stick-ul de test (pornire rece), copierea `gpu-jurnal-002.txt`, primul tur al buclei automate.
- stare: gata (cyber-universe, 2026-11-03 19:50, sesiunea OS; preluat 17:45) — rezultat: Release-ul de folosit la fereastră e **`os-222`** (P6-45 întreg: `--profil` despărțit, bucățele, echipe, un bloc pe simbol, un procesor liber, toate măsurate de `--cauta`; fără reglaj merge ca `os-220`), CI verde · kronos: preluat (2026-11-03 17:20, supraveghetor) — `plan/coada.md`: S70 se termină sau se oprește curat până la 06:45; S71 pornește doar după fereastră (~09:30); 2026-11-04 05:20: S70 terminat la 04:00:51, nimic pe placă de atunci → fereastra 07:00–09:30 e liberă; `gata` pentru kronos după fereastră · kronos: **gata** (2026-11-04 11:20, supraveghetor) — rezultat: nimic pe placă între 04:00 și 09:59; S71 a pornit abia după fereastră

### C-64 · kronos · Dacă S72b (școala de cod) e NU AJUTĂ: română + răspunsuri în română + Kronos mai mare crescut din #477
- data: 2026-11-04 11:30 · de la: **Adrian** („dacă nu avansăm pe cod, îmbunătățim româna și răspunsurile în română și mărim parametrii”), prin centrul de comandă
- ce (doar după verdictul S72b; dacă S72b AJUTĂ, se continuă școala și C-64 așteaptă):
  - **R1 — răspunsuri în română:** un set de exerciții „întrebare/instrucțiune → răspuns” scrise din datele românești deja avute (fără alt AI, fără descărcări),
    cu un set ascuns și o notă automată (corect / în temă / limbă curată); o noapte din #477 pe o copie; #477 rămâne în uz până când copia îl bate la examen.
  - **R2 — Kronos mai mare, crescut din #477:** se lărgește/adâncește modelul păstrând ce știe (straturi noi pornite „neutre”, aceeași ieșire la început,
    verificat pe vectorii KGR1), la cea mai mare mărime care se antrenează în ≤ 7.000 MB pe placă (estimare ~200–350M; bf16, recalcul activări); întâi un test scurt
    de memorie și viteză, apoi nopți. Măsurat cu examenul de română (#477 = 1,2097) și cu R1. Paznicul și examenul neschimbate; `kronos/` neatins.
  - Pre-înregistrare înainte de fiecare noapte; placa ≤ 7.000 MB / 83 °C; nimic descărcat.
- stare: preluat (2026-11-04 14:20, supraveghetor) — **S76** (R1) și **S77** (R2) în `plan/coada.md`, aprobate cu condiția ca S72b să nu fie AJUTĂ (NU AJUTĂ, STRICĂ sau NECLAR); instrucțiunile și pragurile după verdictul S72b (dimineața de 5 nov) · 2026-11-04 20:20: S72b = **STRICĂ** (nu AJUTĂ) → condiția îndeplinită; **S76a** (exercițiile, setul ascuns, nota automată, reperul #477) aprobat și pornește la noapte; S76b și S77 după cifrele S76a

### C-65 · suita-office · „Da” la propunerea de gestiune + ERP Suran pe primul loc
- data: 2026-11-04 11:45 · de la: **Adrian** (scris în chatul centrului de comandă: „pot să îi dai tu da? că nu am acces” — legătura „remote control” cu sesiunea suitei e oprită)
- ce: (1) **Da** la „Propunere gestiune stoc.md” (stocurile întâi, apoi banii și contabilitatea primară), exact cum e scrisă; (2) de acum **ERP Suran și gestiunea
  sunt pe primul loc**: termină etapele 5 (tratarea) și 6 din ERP Suran, apoi gestiunea pe etape; șabloane noi doar între etape, cel mult 1–2 pe sesiune.
  (3) Dacă ceva din propunere are nevoie de o alegere a lui Adrian, întreabă-l în `stare/suita-office.md` la „Blocaje / nevoie de Adrian”.
- stare: preluat (2026-11-04 13:02, sesiunea automată suita-office) — limita de 1–2 șabloane pe sesiune e respectată de sesiunile automate; ERP Suran (etapele 5 și 6) rămâne la sesiunea cerută de Adrian, cum scrie în PLAN.md, secțiunea C; întrebarea e în stare/suita-office.md

### C-66 · cyber-gpu + cyber-universe · I6: HI WPR2 = ultimul bloc de 128 KiB → acceptă-l (FWSEC-FRTS a reușit) + citirea brută de după I6 permisă
- data: 2026-11-04 18:25 · de la: centrul de comandă (delegare Adrian), după `rezultate/2026-11-04-workstation-os222/`
- ce: `cyber-gpu`: `check_frts` acceptă HI = (capăt − 128 KiB) >> 12 (pe placă: așteptat 0x1fff00, citit 0x1ffee0, zona 0x1ffe00000..0x1fff00000), ca RM 570.144 / nova-core
  verifică esențial LO; `gpu-sim` la fel; test în SIMULARE cu valorile reale (LO 0x1ffe00, HI 0x1ffee0); repară și citirea „WPR2 citit după I6” refuzată de politica de siguranță
  (e doar citire, trebuie permisă după oprirea scrierilor). `cyber-universe`: fixarea nouă, Release nou cu stick-ul de test. Apoi, la fereastra următoare, I6 se repetă o dată
  (pornire rece) și ar trebui să dea TRECE → pragul spre I7. Nimic pe placă fără Adrian.
- stare: gata pentru cyber-gpu (2026-11-04 19:40, sesiunea Cyber-GPU) — partea cyber-universe rămâne la sesiunea OS
- rezultat: în SIMULARE, `check_frts` acceptă HI = ultimul bloc de 128 KiB (valorile din 4 nov dau TRECE) și citirea WPR2 de după I6 se face cu o funcție nouă doar-citire, fără permis (`read_frts_after_i6`); pentru OS: fixare ≥ `9ac89b8` + o funcție schimbată, cum scrie în `cyber-gpu/integration/cyber-universe/C-66_wpr2-bloc-128k.md`.

### C-67 · cyber-universe · Kronos 206 simb/s: `qkv` (12,5 GB/s) și `proiecția` (6,0 GB/s) la viteza fc/MLP (34–60 GB/s)
- data: 2026-11-04 18:35 · de la: centrul de comandă (delegare Adrian; ținta următoare ~350 simb/s), după `rezultate/2026-11-04-workstation-os222/`
- ce: profilul os-222 (5,01 ms/simbol): `qkv (+atenția, la generare)` 38,2 % la 12,5 GB/s, `proiecția` 26,4 % la 6,0 GB/s, așteptarea firelor doar 9,6 %. Află de ce aceste două
  citesc memoria de 5–10× mai încet decât fc 4E (60 GB/s) / MLP (34 GB/s) în același bloc pe simbol (mărimea matricei 768×2304 / 768×768? împărțirea pe 12 capete? lipsa
  bucăților/blocului pentru ele?) și adu-le la aceeași formă. `--profil` să le despartă (qkv fără atenție / atenția). CONTROL neschimbat; Release nou; test la fereastra următoare.
- stare: nou
