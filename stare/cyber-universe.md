# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-11-12 23:58 (ora României) · **de:** sesiunea OS programată (22:00) — **C-116 (partea OS) gata → Release `os-298`** (CI verde). Ultimul Release: **`os-298`**. În paralel, o altă sesiune OS lucrează la C-117 (P6-86, analizatorul UHL).

## Acum
- **C-116 (ASUS TUF, placa GA106):** în **`os-298`** laptopul e recunoscut (`gpu identifica`: „GeForce RTX 3060 Laptop … familia GA106”), doar
  pentru citire. Fiindcă firmware-ul laptopului lasă placa „adormită” (Memory Space oprit), comanda nouă **`gpu tur --trezire`** (doar pe stick-ul
  de test, după DA) o trezește pentru tur — o scriere în configurația PCI, repusă la final; niciun registru al plăcii scris. `gpu lant` refuză
  laptopul până la DA-ul separat (C-116 pasul 3). `hw` arată modelul calculatorului (din SMBIOS). Testat în QEMU (SIMULARE), pe laptop netestat.
- În același Release (de la Cyber-GPU): `gpu lant` fără `--varianta` = **varianta 1** (cea care a trecut I8), motivul pasului eșuat scris pe stick,
  starea plăcii după un I7 picat, mesajele GSP-RM din I9 în jurnal; varianta 11 (`rpc-inainte+neprimar`) pentru proba cu ecranul.
- `os-297` (C-113/C-114: jurnalul pe stick-ul Kingston, arhiva `stick-test-complet.zip`) rămâne valabil; `os-298` le conține.

## Urmează
- Jurnalul `gpu tur --trezire` de pe laptop → Cyber-GPU (pasul 3, cu DA separat de la Adrian).
- P6-86/P6-87 (C-117, analizatorul UHL) — sesiunea OS paralelă.
- P6-12 pasul 2 (fereastră proprie fără cache) doar după un `log mmio` de pe un calculator real.

## Ce oferă proiectul celorlalți
- `gpu lant [--varianta N]` I6 → I14, `gpu variante`, `gpu recupereaza`, `gpu tur --trezire` (GA106), `kronos --gpu` pe stick-ul de test; jurnale + rapoarte trimise în hub (cu token).
- `hw` cu modelul din SMBIOS, `hub ruleaza` / `hub asculta`, `test tot`, `kronos --conversatie`, git pe ramuri `os/…`, `web`, `files`; bibliotecile `crypto/`, `tls/`, `json/`, `rtl8168/`, `e1000e/`.

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
