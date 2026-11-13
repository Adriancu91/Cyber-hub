# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-11-13 05:45 (ora României) · **de:** sesiunea OS programată (05:40) — oprire scurtă, nimic nou de făcut fără Adrian. Ultimul Release: **`os-301`** (C-118 W0 `wifi identifica` + versiunea VBIOS, CI 301 verde). Înainte: `os-300` (C-117), `os-298` (C-116).

## Acum
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
- `gpu lant [--varianta N]` I6 → I14, `gpu variante`, `gpu recupereaza`, `gpu tur --trezire` (GA106), `kronos --gpu` pe stick-ul de test; jurnale + rapoarte trimise în hub (cu token).
- `analiza` (inventar ca UHL, `uhl-inventory/0.1`), `hw` cu modelul din SMBIOS, `hub ruleaza` / `hub asculta`, `test tot`, `kronos --conversatie`, git pe ramuri `os/…`, `web`, `files`; bibliotecile `crypto/`, `tls/`, `json/`, `rtl8168/`, `e1000e/`.

## De ce are nevoie de la ceilalți
- **`cyber-gpu`:** după jurnalul de citire de pe laptop, pasul 3 din C-116; după următorul `gpu lant` pe workstation, cauza lui I9.
- **`kronos`:** Release-ul `kronos-kgr1-513` (opțional).

## Blocaje / nevoie de Adrian

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
