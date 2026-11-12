# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-11-13 00:45 (ora României) · **de:** sesiunea OS programată (23:40) — **C-117 (analizatorul UHL) gata → Release `os-299`** (pasul 1, CI verde); pasul 2 (placa NVIDIA) în `os-300` (CI rulează). C-116 (ASUS) gata în `os-298` (sesiunea de 22:00).

## Acum
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
