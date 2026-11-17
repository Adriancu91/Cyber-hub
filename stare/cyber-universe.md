# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-11-17 23:45 (ora României) · **de:** sesiunea OS programată (23:40) — nimic nou. Ultimul Release: **`os-305`** (CI verde).

## Acum
- **17 nov 23:45:** nimic nou pentru OS (nicio comandă, niciun jurnal); CI verde (`os-305`). Aștept testul tău de mâine: stick cu `os-305` + `github.token` → `gpu lant --i9 c135` → DA → `trimite`.
- **17 nov 20:45:** nimic nou pentru OS (nicio comandă, niciun jurnal); CI verde (`os-305`). Aștept testul tău de mâine: stick cu `os-305` + `github.token` → `gpu lant --i9 c135` → DA → `trimite`.
- **17 nov 20:50 — `os-305` gata (P6-93, C-136):** OS-ul folosește codul Cyber-GPU nou (`f732365`, C-135). Comanda nouă **`gpu lant --i9 c135`**
  pornește direct cu forma care a mers pe placă la `os-304` (B) și repară pasul care a picat (cererea „jetonului de lucru”, `0x40`): încercarea N face
  canalul fără „notificatorul de erori”; doar dacă placa refuză iar jetonul, încercarea F alege singură numărul canalului și calculează jetonul.
  Fără opțiune, `--i9 c125` sau `--i9 c133`, `gpu lant` face exact ce făcea în `os-304`. Testat doar în SIMULARE (toată suita 110/0/1, CI verde);
  pe placă netestat — doar cu tine de față, după DA. Dacă I9 trece, lanțul merge singur la I10 (add64, primul calcul pe placă).
- **17 nov 16:00 — `os-304` gata (P6-92, C-134):** OS-ul folosește codul Cyber-GPU nou (`b352d50`, C-133). Comanda nouă **`gpu lant --i9 c133`**
  încearcă pasul I9 (cel cu 0x57) în forma găsită de Cyber-GPU: pregătirea contextului trimisă într-un singur mesaj, înaintea obiectului de calcul
  (încercarea A; B doar dacă A e refuzată). Fără opțiune sau cu `--i9 c125`, `gpu lant` face exact ce făcea în `os-303`. Testat doar în SIMULARE
  (QEMU + CI verde); pe placă netestat — doar cu tine de față, după DA.
- **17 nov 11:45:** nimic nou pentru OS (nicio comandă, niciun jurnal); CI verde (`os-303`). „OPRIT” rămâne. Aștept fereastra ta: stick cu `os-303` + `github.token` → `gpu lant --i9 c125` → `trimite`.
- **17 nov 08:45:** nimic nou pentru OS (nicio comandă, niciun jurnal); CI verde (`os-303`). „OPRIT” rămâne. Aștept fereastra ta: stick cu `os-303` + `github.token` → `gpu lant --i9 c125` → `trimite`.
- **17 nov 05:45:** nimic nou pentru OS (nicio comandă, niciun jurnal); CI verde (`os-303`). A treia sesiune la rând fără sarcină → „OPRIT” până la o comandă nouă sau un jurnal de test. Aștept fereastra ta: stick cu `os-303` + `github.token` → `gpu lant --i9 c125` → `trimite`.
- **17 nov 02:45:** nimic nou pentru OS (nicio comandă, niciun jurnal); CI verde (`os-303`). Aștept fereastra ta: stick cu `os-303` + `github.token` → `gpu lant --i9 c125` → `trimite`.
- **16 nov 23:45:** nimic nou pentru OS (nicio comandă, niciun jurnal); CI verde (`os-303`). Aștept fereastra ta: stick cu `os-303` + `github.token` → `gpu lant --i9 c125` → `trimite`.
- **16 nov 22:05 — `os-303` gata (P6-91, C-125):** OS-ul folosește noul cod Cyber-GPU (`239f986`). Comanda nouă **`gpu lant --i9 c125`** încearcă
  pasul I9 (cel care a picat cu 0x57 în testul tău de azi) în varianta nouă: bufferele de context marcate „privilegiat” + lista bufferelor
  cerută de la placă și scrisă în jurnal (și dacă I9 pică). Fără `--i9 c125`, `gpu lant` face exact ce a făcut în `os-302`. Testat doar în
  SIMULARE (QEMU, toată suita 108/0/1, CI verde); pe placă netestat — doar în fereastra cu tine.
- **16 nov 17:50:** nimic nou pentru OS (C-127…C-129 sunt pentru Kronos; C-125 la Cyber-GPU încă fără commit); „OPRIT” rămâne, CI verde (`os-302`). De la tine aștept doar: `github.token` pus pe stick-ul de test, ca `trimite` să urce jurnalele.
- **16 nov 15:05:** am citit testul de azi (`os-302`): I8 trece iar, I9 pică cu 0x57 (obiect negăsit) → e la Cyber-GPU (C-125); OS-ul leagă commit-ul lor imediat ce apare. `trimite` n-a mers pentru că pe stick-ul de test lipsea `github.token`. Testul de stres de 5 minute din CI a picat o dată (un program n-a găsit pagina de cod, la al 217-lea proces); repetat de 3 ori (2 local, 1 în CI) → trece; notat ca B-007, de urmărit.
- **16 nov 11:45:** tot nimic nou pentru OS (nicio comandă, niciun jurnal); „OPRIT” rămâne, CI verde (`os-302`).
- **16 nov 08:45:** tot nimic nou pentru OS (nicio comandă, niciun jurnal); „OPRIT” rămâne, CI verde (`os-302`).
- **16 nov 05:45:** tot nimic nou pentru OS (nicio comandă, niciun jurnal); „OPRIT” rămâne, CI verde (`os-302`).
- **16 nov 02:45:** tot nimic nou pentru OS (nicio comandă, niciun jurnal); „OPRIT” rămâne, CI verde (`os-302`).
- **15 nov 23:45:** tot nimic nou pentru OS (nicio comandă, niciun jurnal); „OPRIT” rămâne, CI verde (`os-302`).
- **15 nov 20:45:** tot nimic nou pentru OS (nicio comandă, niciun jurnal); „OPRIT” rămâne, CI verde (`os-302`).
- **15 nov 17:45:** tot nimic nou pentru OS (nicio comandă, niciun jurnal); „OPRIT” rămâne, CI verde (`os-302`).
- **15 nov 14:45:** tot nimic nou pentru OS (nicio comandă, niciun jurnal); „OPRIT” rămâne, CI verde (`os-302`).
- **15 nov 11:45:** tot nimic nou pentru OS (nicio comandă, niciun jurnal); „OPRIT” rămâne, CI verde (`os-302`).
- **15 nov 08:45:** tot nimic nou pentru OS (nicio comandă, niciun jurnal); „OPRIT” rămâne, CI verde (`os-302`).
- **15 nov 05:45:** tot nimic nou pentru OS (nicio comandă, niciun jurnal); „OPRIT” rămâne, CI verde (`os-302`).
- **15 nov 02:45:** tot nimic nou pentru OS (nicio comandă, niciun jurnal); „OPRIT” rămâne, CI verde (`os-302`).
- **14 nov 23:45:** tot nimic nou pentru OS (nicio comandă, niciun jurnal); „OPRIT” rămâne, CI verde (`os-302`).
- **14 nov 20:45:** tot nimic nou pentru OS (nicio comandă, niciun jurnal); „OPRIT” rămâne, CI verde (`os-302`).
- **14 nov 17:45:** tot nimic nou pentru OS (nicio comandă, niciun jurnal); „OPRIT” rămâne, CI verde (`os-302`).
- **14 nov 14:45:** tot nimic nou pentru OS (nicio comandă, niciun jurnal); „OPRIT” rămâne, CI verde (`os-302`).
- **14 nov 11:45:** tot nimic nou pentru OS (nicio comandă, niciun jurnal); „OPRIT” rămâne, CI verde (`os-302`).
- **14 nov 08:50:** tot nimic nou pentru OS (nicio comandă, niciun jurnal); „OPRIT” rămâne, CI verde (`os-302`).
- **14 nov 05:50:** tot nimic nou pentru OS (nicio comandă, niciun jurnal); „OPRIT” rămâne, CI verde (`os-302`).
- **14 nov 02:50:** tot nimic nou pentru OS (nicio comandă, niciun jurnal); „OPRIT” rămâne, CI verde (`os-302`).
- **13 nov 23:50:** tot nimic nou pentru OS (nicio comandă, niciun jurnal); „OPRIT” rămâne, CI verde (`os-302`).
- **13 nov 20:45:** tot nimic nou pentru OS (nicio comandă, niciun jurnal); „OPRIT” rămâne, CI verde (`os-302`).
- **13 nov 17:50:** nicio comandă nouă pentru OS, niciun jurnal nou. Sesiunile OS stau „OPRIT” până la prima comandă nouă sau primul jurnal de test (cauza: Adrian plecat până luni seara, coada fără el e goală).
- **13 nov 15:00:** Cyber-GPU a citit jurnalul de pe laptop (VBIOS identic cu Windows) — nimic de schimbat în OS. Diferența „45 fapte pe ecran / 47 în modelul lor”: OS-ul arată exact numărul dat de bibliotecă; cele 2 lipsesc dintre rândurile tăiate sus în poză. La următorul test pe laptop, `gpu tur --trezire` urmat de `analiza` (cu `os-302`) pune toate faptele în inventar → se vede care.
- **13 nov 11:50:** Adrian plecat până luni seara (16 nov, C-119) → workstation-ul e al lui Kronos non-stop, fără teste OS/GPU acolo. Decizia 11:11: întâi GPU funcțional; nicio sarcină OS nouă pentru procesor/RAM. Coada OS fără Adrian e goală — sesiunile până luni fac doar verificări scurte (hub, CI).
- **Testul ASUS din 13 nov (`os-301`) — citit:** `wifi identifica`, `gpu identifica`, `gpu tur --trezire` (45 de fapte, VBIOS identic cu Windows, 0 scrieri în placă), `analiza` și `test tot` (6/7, doar rețeaua fără cablu) au trecut. Mulțumesc pentru poze și fișiere.
- **P6-90 (din observația ta):** `analiza` arăta „placa NVIDIA: 0 fapte” pe laptop (placa „adormită”). Acum, dacă în aceeași pornire ai rulat `gpu tur --trezire`, `analiza` pune faptele lui în inventar (cu ora turului); `analiza` în sine tot nu scrie nimic. Testat în QEMU, toată suita trece; Release **`os-302`** gata (CI verde).
- **C-118 (Wi-Fi AX201 pe ASUS), pasul W0:** comanda nouă **`wifi identifica`** (sau doar `wifi`) găsește placa Wi-Fi Intel și arată
  ID-urile, dacă e integrată (CNVi), starea ei, BAR-urile și — dacă firmware-ul a lăsat-o trează — 5 registre de identitate (versiunea MAC-ului,
  a radioului, comutatorul radio). **Zero scrieri.** Rândul „wifi” apare și în `test tot`, iar placa intră în inventarul `analiza`. Testat în QEMU
  (cu un dispozitiv de probă în locul plăcii); pe laptop netestat. Pașii următori în `docs/WIFI.md` din repo (W1 = firmware-ul, cu „da” separat).
- **Cyber-GPU `835f24d`:** `gpu vbios` și `analiza` arată versiunea VBIOS (ca în Windows: `94.06.1E.00.23` pe ASUS, `94.04.65.00.3e` pe workstation) — comparație automată cu UHL.
- **C-117 (analizatorul UHL):** comanda nouă **`analiza`** scrie pe stick, în `raport\uhl\<calculator>\<data-ora>\`, un inventar în forma
  UHL (`uhl-inventory/0.1`, aceleași statusuri): `inventory.json` (tot, cu numerele de serie — rămâne pe stick), `inventory.redacted.json`
  (seriile ascunse) și `report.txt`. Față de Windows are în plus: spațiul de configurare PCI complet (4 KiB) pentru fiecare dispozitiv, BAR-urile
  pe index, Resizable BAR, ASPM, stările D0–D3, legăturile PCIe, toate tabelele ACPI (SSDT ×N + DSDT), SMBIOS (memorii, procesor), CPUID.
  Placa NVIDIA intră prin turul de citire Cyber-GPU (0 scrieri). `trimite` urcă în hub doar varianta fără serii + raportul. Doar citire. Testat în QEMU.
- **C-116 (ASUS TUF, placa GA106):** în **`os-298`** laptopul e recunoscut (`gpu identifica`: „GeForce RTX 3060 Laptop … familia GA106”), doar
  pentru citire. Fiindcă firmware-ul laptopului lasă placa „adormită” (Memory Space oprit), comanda nouă **`gpu tur --trezire`** (doar pe stick-ul
  de test, după DA) o trezește pentru tur — o scriere în configurația PCI, repusă la final; niciun registru al plăcii scris. `gpu lant` refuză
  laptopul până la DA-ul separat (C-116 pasul 3). `hw` arată modelul calculatorului (din SMBIOS). Testat în QEMU (SIMULARE), pe laptop netestat.
- În același Release (de la Cyber-GPU): `gpu lant` fără `--varianta` = **varianta 1** (cea care a trecut I8), motivul pasului eșuat scris pe stick,
  starea plăcii după un I7 picat, mesajele GSP-RM din I9 în jurnal; varianta 11 (`rpc-inainte+neprimar`) pentru proba cu ecranul.
- `os-297` (C-113/C-114: jurnalul pe stick-ul Kingston, arhiva `stick-test-complet.zip`) rămâne valabil; `os-298` le conține.

## Urmează
- C-118: poza `wifi identifica` de pe laptop → planul W1 (pornirea plăcii cu firmware-ul de pe stick, după „da”).
- Jurnalul `gpu tur --trezire` de pe laptop → Cyber-GPU (pasul 3, cu DA separat de la Adrian).
- C-117: compararea cu inventarul din Windows al aceluiași laptop (după `analiza` pe ASUS + un `inventory.redacted.json` din UHL).
- P6-12 pasul 2 (fereastră proprie fără cache) doar după un `log mmio` de pe un calculator real.

## Ce oferă proiectul celorlalți
- `gpu lant [--varianta N] [--i9 c125|c133|c135]` I6 → I14 (`--i9 c135` = C-135, din `os-305`), `gpu variante`, `gpu recupereaza`, `gpu tur --trezire` (GA106), `kronos --gpu` pe stick-ul de test; jurnale + rapoarte trimise în hub (cu token).
- `analiza` (inventar ca UHL, `uhl-inventory/0.1`), `hw` cu modelul din SMBIOS, `hub ruleaza` / `hub asculta`, `test tot`, `kronos --conversatie`, git pe ramuri `os/…`, `web`, `files`; bibliotecile `crypto/`, `tls/`, `json/`, `rtl8168/`, `e1000e/`.

## De ce are nevoie de la ceilalți
- **`cyber-gpu`:** nimic acum (`239f986` legat în `os-303`). După jurnalul `gpu lant --i9 c125` de pe workstation: pasul următor pentru I9; după DA-ul lui Adrian, pasul 3 din C-116 pe laptop.
- **`kronos`:** Release-ul `kronos-kgr1-513` (opțional).

## Blocaje / nevoie de Adrian

**Nou (17 nov 20:50) — mâine (18 nov), pe workstation, după ce S124 lasă placa:**
1. Stick-ul de test cu **`os-305`** (`stick-test-complet.zip` din Release, verificat cu `SHA256SUMS`) + fișierul **`github.token`** în rădăcina stick-ului.
2. Oprești complet workstation-ul (pornire rece), pornești de pe stick → `gpu lant --i9 c135` → citești avertismentul → `DA` + Enter.
3. La final `trimite` (urcă jurnalul în hub). Dacă nu merge: poză la ultimele rânduri, jurnalul `raport\gpu-jurnal-NNN.txt` în `rezultate/<data>-workstation-os305/`.

**Nou (16 nov):**
- Pune fișierul `github.token` și pe **stick-ul de test** (în rădăcină, ca `/usb/github.token`), ca `trimite` să urce singur jurnalul data viitoare. Nimic urgent altceva.

**Nou (13 nov, după testul ASUS) — nimic urgent:**
- **C-118 W1 (Wi-Fi):** registrele plăcii Wi-Fi nu se pot citi fiindcă placa e „adormită” (ca placa video). Ca să mergem mai departe am nevoie de „DA”-ul tău (în COMENZI) pentru o „trezire” ca la `gpu tur --trezire`: o scriere în configurația PCI a plăcii Wi-Fi, pusă la loc la final, nimic altceva. Plus, pentru W1, fișierul de firmware Qu/QuZ-hr-b0 descărcat de tine (pe stick, nu în hub).
- **C-116 pasul 3 (placa video a laptopului):** Cyber-GPU așteaptă DA-ul tău separat.
- La următorul test pe laptop (cu `os-302`): `gpu tur --trezire` (DA), apoi `analiza` → rândul „placa NVIDIA: … 45 fapte | cip GA106 | VRAM 6144 MiB …” și „faptele placii: din gpu tur --trezire …”.

**Pe laptopul ASUS TUF (C-116, prima citire a plăcii video) — Release `os-298`:**
1. Stick-ul de test (Kingston cu `stick-test-complet.zip` din **`os-298`**, sau imaginea `cyber-universe-gpu-scrie-usb.img` scrisă cu Rufus).
2. Pornești laptopul de pe stick → `hw` (primul rând arată acum modelul: `calculator: ASUSTeK …`; poză).
3. `gpu tur --trezire` → citești avertismentul → `DA` + Enter. Se face o singură scriere în configurația plăcii (pornește „Memory Space”),
   turul de citire, apoi totul e pus la loc. Poză la ultimele rânduri (`trezirea minima: …`, `Command acum …`, `scrieri: 2 in configuratia PCI …`).
4. **Acasă, fără internet:** nu e nevoie de `trimite` — jurnalul rămâne pe stick, în `raport\gpu-jurnal-NNN.txt` (cel cu numărul cel mai mare).
   Când ajungi la un calculator cu internet, pui fișierul + pozele în `rezultate/<data>-laptop-asus-tuf/` (sau `trimite` de pe un Cyber Universe cu cablu). Cu el, Cyber-GPU face pasul 3.
4b. **C-118 (Wi-Fi, `os-301` sau mai nou):** scrie `wifi identifica` + Enter → poză la ecran (doar citire, nimic de confirmat).
   Dacă scrie „registrele CSR nu s-au citit: Memory Space oprit de firmware” — e normal la pasul ăsta.
5. **C-117 (nou, `os-299` sau mai nou):** pe același stick scrie `analiza` + Enter (~câteva secunde, doar citire). Pe stick apare dosarul
   `raport\uhl\<calculator>\<data-ora>\`. Pune în `rezultate/<data>-laptop-asus-tuf/` DOAR `inventory.redacted.json` și `report.txt`
   (sau `trimite` cu cablu: pleacă singure doar acestea). `inventory.json` are numerele de serie — nu-l pune în hub.
6. **Ca să comparăm cu Windows:** pune în același dosar și `inventory.redacted.json` făcut de UHL-ul tău pe ASUS (forma exactă a schemei
   nu e în hub; am dedus-o din C-117 și vreau s-o potrivesc cu a ta).

**La următorul test pe workstation:** același stick cu **`os-298`** → `gpu lant` (fără `--varianta` = varianta 1, cea care a trecut) + DA.
Acum motivul unui pas eșuat (ex. I9) intră în jurnal. Dacă jurnalul merge: poză la ultimul rând
`usb: scrieri …, sincronizari …`; dacă nu: poză la mesaj + `log usb`. Rezultatele în `rezultate/<data>-workstation-os298/`.

**Când ai Lenovo-ul la îndemână (nu grăbește nimic):** scrie pe stick-ul normal `cyber-universe-usb.img` din Release-ul **`os-293`**
(sau mai nou), pornește Lenovo-ul, apoi **bagă mouse-ul USB după ce apare desktopul** și vezi dacă merge; o poză la `lsusb` și una la
`log mmio`, în `rezultate/<data>-laptop-lenovo-i5/`. Dacă vrei să știi și cauza veche, varianta de mai jos (cu `os-290`):

**Mic, când ai Lenovo-ul la îndemână (nu grăbește nimic):** ca să știm sigur de ce nu mergea mouse-ul USB — pornește Lenovo-ul cu stick-ul normal
**cu mouse-ul deja băgat**, scrie `lsusb` și fă o poză. Dacă mouse-ul apare în listă și tot nu merge → altă cauză; dacă nu apare → era cauza
reparată în P6-80 (mouse băgat după pornire). Poza în `rezultate/2026-11-11-laptop-lenovo-i5/`.

**Opțional (C-104, ~5 min):** tokenul pentru `hub asculta` — `docs/USB.md` punctul 15.

**Când vrei (C-105):** ciclul de test automat e gata, dar **oprit**; îl pornești doar tu, cu cele două chei (`docs/USB.md` punctul 16).
