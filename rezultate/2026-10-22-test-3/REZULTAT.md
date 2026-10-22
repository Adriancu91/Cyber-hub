# Testul 3 pe hardware real — Cyber Universe OS, Release os-120 (commit 06c69c9)

**Data:** 2026-10-22, 09:00–09:20 (ora României) · **Făcut de:** Adrian · **Scris de:** centrul de comandă (citit din poze)
**Calculator:** același Lenovo ThinkPad (eticheta NB-7211174), AMD Ryzen 5 4500U, ~7,4 GB RAM liberi, Realtek RTL8168 `10ec:8168`,
NVMe Samsung `144d:a809`, xHCI AMD `1022:1639`. **Cablul de rețea băgat** la router înainte de pornire. Stick: ADATA `125f:db8a`,
formatat în Windows, cu fișierele din `cyber-universe-stick-v3.zip` (Release os-120, sumele verificate).

## Pozele
| # | fișier | comanda |
|---|---|---|
| 1 | `01-log-rtl.jpg` | `log rtl` |
| 2 | `02-net.jpg` | `net` |
| 3 | `03-ping.jpg` | `ping 1.1.1.1` |
| 4 | `04-hw.jpg` | `ls /usb`, `hw` (la 717,88 s de la pornire) |
| 5 | `05-log-usb.jpg` | `log usb` (făcută la 09:33, laptopul încă pornit) |

`host github.com` și `fetch` nu s-au făcut (fără adresă, n-aveau sens).

## Ce s-a văzut, cuvânt cu cuvânt

**`log rtl`:**
```
[  10.120] INFO  net: placa Realtek RTL8168 pornita (revizia 50800000), MAC 38:f3:ab:6b:11:34, legatura: da, 1000 Mbit/s, full duplex
[  10.290] INFO  net: rtl8168 registre: CR 0c RCR 0002c70a TCR 53900f00 IMR 0000 ISR 0021 RMS 2048 RDSAR 3d8000 TNPDS 3d9000 PHY f3
```

**`net`** (la câteva minute de la pornire):
```
Realtek RTL8168/8111  MAC 38:f3:ab:6b:11:34
pachete trimise 60, primite 16
legatura: da, 1000 Mbit/s, full duplex; primire: aruncate 0, pierdute de placa 0, ISR vazut 40b5, descriptor RX 0 = 80000800, citiri 26190
fara adresa (DHCP fara raspuns; reincearca la 10 s)
```

**`ping 1.1.1.1`:** `ping: reteaua nu are inca adresa (DHCP)`

**`ls /usb`:** `ls: /usb: nu exista`

**`hw`** (la 717,88 s): procesor AMD Ryzen 5 4500U; memorie liberă 7378 MiB, folosită 19.836 KiB (heap 1337 / 18.256 KiB);
PCI: `01:00.0 10ec:8168 placa de retea [rtl8168]`, `02:00.0 8086:2723 placa de retea [-]` (Wi-Fi, fără driver), `03:00.0 144d:a809
controler NVMe [nvme]`, `04:00.0 1002:1636 placa video [-]`, `04:00.3` și `04:00.4 1022:1639 controler USB [xhci]`, restul fără driver;
USB: `port 3 04f2:b6be alt dispozitiv` (camera web), `port 4 125f:db8a stocare (Mass Storage)`; **`/disk: montat (2 intrari)`**;
**`/usb: nemontat (stick-ul nu porneste (configurare USB))`**; rețea: **trimise 160, primite 16**, aceeași linie de stare ca la `net`
(ISR văzut 40b5, descriptor RX 0 = 80000800), fără adresă.

**`log usb`:**
```
[   2.860] INFO  pci: 04:00.3 1022:1639 clasa 0c:03:30 controler USB
[   3.020] INFO  pci: 04:00.4 1022:1639 clasa 0c:03:30 controler USB
[   5.400] INFO  boot: pornit de pe disc (hard disk, SSD sau stick USB)
[   5.970] INFO  usb: port 3: 04f2:b6be alt dispozitiv (clasa ef:02:01, viteza 3)
[   6.180] INFO  usb: port 4: 125f:db8a stocare (Mass Storage) (clasa 08:06:50, viteza 3)
[   6.340] INFO  usb: controler XHCI pornit, 6 porturi, 2 dispozitive
[   6.520] WARN  usb: stick-ul de pe portul 4 nu porneste
```

## Ce înseamnă (analiza centrului de comandă; de confirmat de sesiunea OS)

1. **Progres real la Realtek (C-4 a avut efect):** la testul 2 primea 0 pachete; acum **primește** — 16 pachete, cu legătura
   recunoscută corect (1000 Mbit/s, full duplex, PHY citit). Deci inițializarea, PHY-ul și inelul RX pornesc.
2. **Dar recepția se oprește după exact 16 pachete.** Între `net` (60 trimise) și `hw` (160 trimise, ~10 minute mai târziu) numărul
   primit a rămas **16**. Pe o rețea cu router vin tot timpul cadre (ARP, DHCP offer, broadcast), deci nu lipsa traficului e cauza.
   Indicii din registre:
   - **`ISR vazut 40b5`** = bitul 4 (**RDU, „Rx Descriptor Unavailable”**) a fost văzut, pe lângă ROK (bit 0), TOK (bit 2), LinkChg (bit 5),
     TDU (bit 7) și TimeOut (bit 14). RDU înseamnă că placa a rămas **fără descriptori liberi** în inelul RX.
   - **„primite 16”** = foarte probabil **exact mărimea inelului RX** (16 descriptori). IPOTEZĂ principală: după ce placa umple toți cei
     16 descriptori, driverul fie **nu le redă placa** (bitul OWN nu e pus la loc după citire), fie le redă, dar **ultimul descriptor n-are
     bitul EOR** (End Of Ring), și placa iese din inel, fie placa a intrat în RDU și nu reia recepția de la sine pe această revizie.
   - `descriptor RX 0 = 80000800` = OWN pus (placa îl are) + mărime 0x800 = 2048. E consecvent și cu „redat, dar placa nu reia”, și cu
     „inel parcurs o dată, descriptorul 0 n-a mai fost atins”.
   - `revizia 50800000` (din TxConfig) = ESTIMARE: familia **RTL8168H/8111H**; reviziile G/H au cerințe de inițializare în plus față de
     modelul generic (în documentația publică / OSDev: configurare RxConfig specifică, aliniere la 256 de octeți a inelelor, „RxMaxSize”),
     iar comportamentul după RDU poate diferi.
   - Trimiterea merge (160 de cadre DHCP Discover au ieșit, TOK văzut), deci TX e în regulă.
3. **Stick-ul: problema e înainte de montare.** xHCI enumerează stick-ul (`125f:db8a` la portul 4), dar **„stick-ul nu porneste
   (configurare USB)”** = cererea SET_CONFIGURATION (sau pasul dinainte: citirea descriptorilor de configurare) eșuează pe xHCI-ul real.
   C-4 (montarea MBR/superfloppy) nu a fost nici măcar ajunsă. Fără `/usb` nu merg: `cyber.rw`, `claude.key`, `github.token`, auto-actualizarea.
   De remarcat: camera web (`04f2:b6be`) e pe portul 3 al aceluiași controler.
   **Din `log usb` (poza 5):** descriptorul de dispozitiv **se citește** (VID/PID, clasa 08:06:50 = Mass Storage, BOT, SCSI transparent),
   deci SET_ADDRESS și GET_DESCRIPTOR(device) merg. **„viteza 3”** — în xHCI (PORTSC, câmpul Port Speed) **3 = High-Speed (USB 2.0,
   480 Mbit/s)**, nu SuperSpeed (acela e 4); deci stick-ul lucrează ca dispozitiv USB 2 și contextul de endpoint SuperSpeed NU e cauza.
   Eșecul vine la **180 ms** după identificare (6.340 → 6.520) → IPOTEZE, în ordinea probabilității: (1) **primele comenzi SCSI pică cu
   „Unit Attention”** — după pornire, un stick real răspunde la INQUIRY / TEST UNIT READY / READ CAPACITY cu CSW status 01 (Command
   Failed) până i se face REQUEST SENSE și se reîncearcă; QEMU nu face asta, hardware-ul real da; (2) **timeout prea scurt** — stick-urile
   reale au nevoie de până la 1–2 s ca să fie „ready” (Linux reîncearcă TEST UNIT READY secunde întregi); (3) citirea descriptorului de
   configurare în două cereri (9 octeți, apoi wTotalLength) sau SET_CONFIGURATION; (4) Max Packet Size al endpoint-urilor bulk la High-Speed
   = 512. Se rezolvă cu jurnal pe fiecare pas (cod de completare TRB, CSW status, datele de la REQUEST SENSE).
4. **NVMe merge** (`/disk` montat, 2 intrări), ca la testul 2. **Memoria:** OS-ul folosește ~19 MB din 7,4 GB.
5. **Wi-Fi** `8086:2723` fără driver — rămâne pentru mai târziu, cum a decis Adrian.

## Ce rămâne de verificat (dacă laptopul mai e pornit)
- `log usb` → poză (ce zice xHCI la configurarea stick-ului: codul erorii TRB / timeout / STALL).
- `net` încă o dată după un minut → confirmă că „primite” stă la 16.
