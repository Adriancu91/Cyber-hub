# Testul 5 pe hardware real — Cyber Universe OS, Release os-136 (commit 2a21649) — REGRESIE

**Data:** 2026-10-22, 16:18–16:25 (ora României) · **Făcut de:** Adrian · **Scris de:** centrul de comandă (citit din poze)
**Calculator:** același Lenovo ThinkPad (NB-7211174); cablul de rețea băgat; BIOS setat să pornească de pe stick (a pornit direct).
Stick cu fișierele din `cyber-universe-stick-v5.zip` (os-136, sume verificate).

## Pozele
| # | fișier | comanda |
|---|---|---|
| 1 | `01-net.jpg` | `net` + rândurile periodice din jurnal |
| 2 | `02-log-rx.jpg` | `log rx` |
| 3 | `03-log-arp.jpg` | `log arp` → „(niciun rand)” |
| 4 | `04-ping.jpg` | `ping 1.1.1.1` |
| 5 | `05-host.jpg` | `host github.com` |
| 6 | `06-log-rtl.jpg` | `log rtl` (16:29) |

## Ce s-a văzut, cuvânt cu cuvânt
**`net`:**
```
Realtek RTL8168/8111  MAC 38:f3:ab:6b:11:34
pachete trimise 0, primite 0
legatura: da, 1000 Mbit/s, full duplex; primire: aruncate 0, pierdute de placa 0, ISR vazut 0020, descriptor RX 0 = 80000800, citiri 6078
inel RX 256: index 0, ai placii 256; RDU vazut 0 ori, reporniri 0, resincronizari 0; raspunsuri DHCP (udp 68) 0
primele cadre: -
cadre cu tip 0000: 0; reparate de golirea cache-ului: 0; PCIe No Snoop: oprit (era oprit) (detalii: log rx)
fara adresa (DHCP fara raspuns; reincearca la 10 s)
```
Rândurile periodice din jurnal (20,08 s … 112,08 s, la 18,4 s): mereu **trimise 0, primite 0**, index 0, ISR văzut **0020** (doar LinkChg),
citiri 800 → 2600 → 4400 → 6200 → 8000 → 9800. `log rx`: doar rândurile periodice, **niciun rând pe cadru** (n-a fost niciun cadru).
`log arp`: niciun rând. `ping`: fără adresă. `host`: fără DNS.

**`log rtl`** (poza 6):
```
[  8.010] INFO  net: rtl8168 PCIe Device Control 2010 -> 2000 (No Snoop si Relaxed Ordering oprite)
[ 11.250] INFO  net: placa Realtek RTL8168 pornita (revizia 50800000), MAC 38:f3:ab:6b:11:34, legatura: da, 1000 Mbit/s, full duplex
[ 11.420] INFO  net: rtl8168 registre: CR 0c RCR 0000c70a TCR 53900f00 IMR 0000 ISR 0020 RMS 2048 RDSAR 3d8000 TNPDS 3d9000 PHY 93
```

## Ce înseamnă (analiza centrului de comandă)
1. **Regresie față de os-125 (testul 4):** atunci 120 trimise / 32 primite, inelul avansa; acum **0 / 0**, inelul stă la index 0, ISR nu a
   văzut niciodată ROK sau TOK. Placa nu mai face **niciun transfer DMA**, în niciun sens, deși legătura e sus (1000 Mbit/s) și PHY-ul e citit.
2. **Ipoteza „No Snoop” e infirmată de propriul diagnostic:** `PCIe No Snoop: oprit (era oprit)` — setarea era deja oprită, deci nu ea
   producea zerourile de la testul 4. „Golirea cache-ului” nu a putut fi testată (zero cadre).
3. **Cauza probabilă a regresiei:** una dintre schimbările din P6-10c oprește DMA-ul: cel mai probabil **scrierea registrului PCIe Device
   Control** (pentru No Snoop) cu o valoare greșită (alt offset de capability, alți biți atinși: Max Payload/Max Read Request, Relaxed Ordering)
   sau o scriere în registrul **Command** care a pierdut bitul **Bus Master**; a doua posibilitate: golirea cache-ului pe TX/RX făcută pe
   adrese greșite sau înainte ca descriptorii să fie gata. În QEMU nu se vede (QEMU ignoră mare parte din configurarea PCIe).
4. **Ce rămâne valabil din testul 4:** inelul de 256 și stick-ul (P6-10a, P6-10b) mergeau pe os-125. Blocajul real de la testul 4 (cadrele
   2+ citite ca zero) e încă nerezolvat și nediagnosticat pe hardware; ipotezele rămase: (a) buffer-e alocate separat, presupuse contigue;
   (b) **adrese fizice peste 4 GB** — laptopul are 8 GB RAM; dacă buffer-ele cad peste 4 GB și în descriptor se scrie doar jumătatea de jos
   a adresei (sau jumătatea de sus greșit), placa scrie în altă parte, iar driverul citește zero (QEMU, cu puțină memorie, nu atinge
   niciodată cazul); primul cadru corect = primul buffer sub 4 GB, restul deasupra, ceea ce se potrivește cu alocări separate.

5. **Din `log rtl` (poza 6), două diferențe față de os-125 (testul 4, care mergea):**
   - **PCIe Device Control: `2010` → `2000`.** Bitul 11 (No Snoop) era deja 0; scrierea a șters **bitul 4, Enable Relaxed Ordering**, care
     înainte era 1. Schimbare inutilă (ipoteza era greșită) și posibil dăunătoare; de scos.
   - **RCR (RxConfig): `0002c70a` la testul 4 → `0000c70a` acum.** Bitul 17 a dispărut. P6-10c nu declară nicio schimbare la RxConfig, deci ori
     driverul a schimbat-o fără să-și dea seama (altă valoare scrisă, sau citire înainte/după altă etapă), ori hardware-ul o reflectă diferit.
     Oricare ar fi, e o diferență reală de configurare a recepției între versiunea care primea și cea care nu primește nimic.
   - Restul e identic cu testul 4: CR 0c, TCR 53900f00, IMR 0, RMS 2048, RDSAR 3d8000, TNPDS 3d9000 (inelele la aceleași adrese, sub 4 GB; deci
     ipoteza „inelul peste 4 GB” cade pentru inele, rămâne valabilă doar pentru buffer-ele de date, ale căror adrese nu se văd încă).
   Concluzie pentru C-8: revenirea trebuie să readucă **exact** registrele din os-125 (`RCR 0002c70a`, fără scrieri în Device Control), apoi o
   singură schimbare pe versiune, verificată pe laptop.
