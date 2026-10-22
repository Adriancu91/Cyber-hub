# Testul 4 pe hardware real — Cyber Universe OS, Release os-125 (commit ffc342b)

**Data:** 2026-10-22, 14:14–14:25 (ora României) · **Făcut de:** Adrian · **Scris de:** centrul de comandă (citit din poze)
**Calculator:** același Lenovo ThinkPad (NB-7211174), AMD Ryzen 5 4500U; cablul de rețea băgat la router înainte de pornire.
Stick ADATA `125f:db8a` (29.600 MiB), FAT32/MBR din Windows, cu fișierele din `cyber-universe-stick-v4.zip` (os-125, sume verificate).
**Pornire: 14 secunde** până la desktop.

## Pozele
| # | fișier | comanda |
|---|---|---|
| 1 | `01-net.jpg` | `net` (la ~1 minut) |
| 2 | `02-log-rtl.jpg` | `log rtl` |
| 3 | `03-ping.jpg` | `ping 1.1.1.1` |
| 4 | `04-host.jpg` | `host github.com` |
| 5 | `05-log-usb.jpg` | `log usb` |
| 6 | `06-hw.jpg` | `hw` (la 396,98 s) |
| 7 | `07-ls-usb.jpg` | `ls usb` (cale invalidă) și `ls /usb` |
| 8 | `08-net-dupa.jpg` | `net` din nou (la ~7 minute) |

## Ce s-a văzut, cuvânt cu cuvânt

**`net`** (poza 1, ~1 minut):
```
Realtek RTL8168/8111  MAC 38:f3:ab:6b:11:34
pachete trimise 36, primite 24
legatura: da, 1000 Mbit/s, full duplex; primire: aruncate 0, pierdute de placa 0, ISR vazut 40a5, descriptor RX 24 = 80000800, citiri 1504x
inel RX 256: index 24, ai placii 256; RDU vazut 0 ori, reporniri 0, resincronizari 0; raspunsuri DHCP (udp 68) 0
primele cadre: 0806 0000 0000 0000 0000 0000 0000 0000
fara adresa (DHCP fara raspuns; reincearca la 10 s)
```
**`log rtl`:** `[11.190] placa Realtek RTL8168 pornita (revizia 50800000), MAC …, legatura: da, 1000 Mbit/s, full duplex` ·
`[11.350] registre: CR 0c RCR 0002c70a TCR 53900f00 IMR 0000 ISR 0020 RMS 2048 RDSAR 3d8000 TNPDS 3d9000 PHY 93`
**`ping 1.1.1.1`:** `reteaua nu are inca adresa (DHCP)` · **`host github.com`:** `nu am server DNS (retea sau DHCP lipsa)`

**`log usb`** (poza 5) — **stick-ul merge**:
```
[ 5.970] usb: port 3: slot 1, viteza 3, pachet maxim EP0 64, configuratia 1 (512 octeti), endpoint-uri 83/3/32/b0
[ 6.130] usb: port 3: 04f2:b6be alt dispozitiv (clasa ef:02:01, viteza 3)
[ 6.340] usb: port 4: slot 2, viteza 3, pachet maxim EP0 64, configuratia 1 (32 octeti), endpoint-uri 01/2/512/b0 82/2/512/b0
[ 6.500] usb: port 4: 125f:db8a stocare (Mass Storage) (clasa 08:06:50, viteza 3)
[ 6.650] usb: controler XHCI pornit, 6 porturi, 2 dispozitive
[ 6.810] usb: port 4: SET_CONFIGURATION 1 ok
[ 6.970] usb: port 4: Configure Endpoint ok (2 endpoint-uri)
[ 7.510] usb: stocare ADATA USB Flash Drive (29600 MiB)
[11.510] fs: FAT32 (MBR, 29599 MiB) montat la /usb (scriere permisa)
```
**`hw`** (396,98 s): memorie liberă 7377 MiB, folosită 20.320 KiB; `/disk: montat (2 intrari)`; **`/usb: montat (6 intrari)`**; rețea: trimise 88, primite 24.
**`ls /usb`:** `System Volume Information/`, `boot/`, `EFI/`, `CITESTE-MA.txt (475)`, `cyber.rw (76)`, `VERSIUNE (74)`. (`ls usb` fără bară: „cale invalida”.)
**`net`** (poza 8, ~7 minute): trimise 120, **primite 32**, descriptor RX 32 = 80000800, index 32, RDU 0, reporniri 0; **raspunsuri DHCP 0**;
primele cadre tot `0806 0000 0000 0000 0000 0000 0000 0000`; fără adresă.

## Ce înseamnă (analiza centrului de comandă; de confirmat de sesiunea OS)

1. **Stick-ul: REZOLVAT.** Enumerare completă, SET_CONFIGURATION, endpoint-uri, SCSI (ADATA 29.600 MiB), FAT32 pe MBR montat cu scriere
   permisă, fișierele se văd. P6-10b confirmat pe hardware. De acum `cyber.rw`, `claude.key`, `github.token` și auto-actualizarea au unde sta.
2. **Recepția nu se mai blochează: REZOLVAT (P6-10a).** 24 → 32 de pachete primite între cele două `net`, indexul inelului avansează (24 → 32),
   RDU 0, reporniri 0. Inelul de 256 funcționează.
3. **Dar conținutul pachetelor nu e citit corect de la al doilea încolo — ăsta e blocajul DHCP.** Rândul „primele cadre” arată ethertype-ul
   primelor 8 pachete: **primul e `0806` (ARP, corect), următoarele 7 sunt `0000`**. Un cadru Ethernet nu poate avea ethertype 0000; deci
   driverul citește **zerouri** din buffer-ul pachetelor 2–8, adică citește din altă memorie decât cea în care placa a scris. Consecvent cu
   „răspunsuri DHCP 0” deși placa primește cadre pe o rețea cu router (Offer-ul ar trebui să vină în milisecunde după Discover).
   IPOTEZE, în ordinea probabilității:
   - (a) **adresele buffer-elor din descriptorii 1…255 nu corespund cu cele citite de driver**: placa primește adresa fizică din descriptor
     (`buf_phys[i]`), driverul citește din `buf_virt[i]`; dacă pasul (stride) sau baza diferă (de ex. 2048 vs. RMS, sau conversia fizic↔virtual
     făcută doar pentru primul buffer), descriptorul 0 e corect și restul nu. Primul cadru corect + restul zero e exact semnătura asta.
   - (b) driverul **re-armează descriptorul (OWN=1) sau golește buffer-ul înainte să citească** cadrul (ordinea operațiilor).
   - (c) driverul citește lungimea din `opts1` corect, dar **datele din buffer-ul altui index** (off-by-one între indexul plăcii și al driverului).
   - (d) mai puțin probabil: cadrele 2–8 sunt chiar scurte/goale (nu: pe o rețea reală nu există cadre cu ethertype 0).
   Testul care le desparte: scrie în `net` (sau `log rx`) pentru fiecare din primele 8 cadre: index, lungimea din descriptor, adresa fizică
   din descriptor, adresa din care citește driverul, și primii 16 octeți în hex. Dacă adresele diferă → (a). Dacă sunt egale și octeții sunt
   zero → (b). În QEMU nu se vede pentru că modelul minimal al cipului scrie probabil tot la același buffer sau trece prin aceeași cale de adrese.
4. ISR văzut `40a5` = ROK, TOK, LinkChg, TDU, TimeOut — fără RDU (bit 4), cum trebuie.
5. NVMe, xHCI, consola, `hw`, `log`: toate bune. Pornire 14 s. Memorie folosită ~20 MB.

## Ce rămâne de verificat (laptopul e încă pornit la 14:25)
- `log dhcp` → poză și `log arp` → poză (dacă există rânduri: arată dacă clientul DHCP a văzut ceva și dacă ARP-ul a fost tratat).
- `log net` → poză (dacă nu încape, `log net 20`).
