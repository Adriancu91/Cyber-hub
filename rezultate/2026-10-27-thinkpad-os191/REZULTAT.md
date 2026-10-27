# ThinkPad L15 Gen 2 + os-191 — 27 oct 2026, ~22:50 (Adrian)

Laptop: Lenovo ThinkPad (tastatură germană). **Corectură după raport: procesorul e AMD Ryzen 5 4500U (Zen 2, 6 nuclee fără SMT — de aici „6 din 6”),
~7,3 GiB RAM, rețea Realtek RTL8168 (8168GU/8111GU) + WiFi Intel AX200 (8086:2723, fără driver), NVMe Samsung, video AMD Renoir (1002:1636)**
— NU i7-1185G7 cum crezusem. Secure Boot oprit, pornit de pe stick (F12).
Fără cablu de rețea (Adrian nu are acces la router cu cablu; OS-ul nu are WiFi). Prima pornire a OS-ului pe acest laptop.
(Prima încercare n-a pornit: pe stick erau alte arhive, greșeala lui Adrian; corectat.)

## Ce s-a văzut (`poza-1-kronos-calcul-GP.jpg`)
- **Pornire: DA.** Shell-ul `cyber>` apare.
- **`cpu porneste`: 6 nuclee pornite din 6** (APIC 1, 2, 4, 5, 6 + BSP), fiecare în ~10 ms; „planificatorul rulează fire pe 6 nuclee”.
  (Corect: Ryzen 5 4500U are 6 nuclee, MADT arată 6 procesoare.) Rândul `cpu:` spune și „(parcate: firele rămân pe primul nucleu)”.
- **Rețea:** driverul găsește placa și rulează (inel RX 256, ISR văzut 4084, „pază memoriei: ok”); „legătura: nu” — corect, fără cablu.
  Mesajele `net` periodice (la ~18 s) se amestecă cu promptul `cyber>` (cosmetic).
- **`run kronos-calcul`: CĂDERE.** Rândul de start: „gpu-compute (cyber-gpu dac2e32, backend CPU), 6 fire, vectori AVX2+FMA (8 benzi)”, apoi:
  ```
  [209.650] ERR EXCEPTIE: protectie generala (#GP)
  [209.650] ERR   RIP=0xffffffff8001e939 RSP=0xffff9000001d0398 RFLAGS=0x10082 CS=0x8
  [209.650] ERR   cod eroare=0x18
  [209.650] ERR SISTEM OPRIT
  ```
  În modul nucleu (CS=0x8); codul de eroare 0x18 arată un selector de segment (intrarea 3 din GDT) — deci probabil la o încărcare de segment /
  `iretq` / comutarea către un fir, nu la calculul vectorial. În CI (QEMU, 4 nuclee) `kronos-calcul` trece. Raportul automat nu s-a scris (panică).
- Urmează (cerut lui Adrian): repornire, `raport`, `run kronos-calcul` **fără** `cpu porneste` (un nucleu), `raport` — pentru a separa
  „problemă pe mai multe nuclee” de „problemă pe acest procesor”.

## A doua pornire (~22:57, `poza-2-un-nucleu-GP.jpg`)
- `raport` → **scris `/usb/raport/20261027-1.txt` (23.403 octeți), „cheile și tokenurile sunt ascunse”** — cutia neagră merge pe hardware real.
- `run kronos-calcul` **fără** `cpu porneste` („1 fir, vectori AVX2+FMA (8 benzi)”) → **aceeași cădere, același RIP**:
  `#GP RIP=0xffffffff8001e939 RSP=0xffff900000193318 RFLAGS=0x10086 CS=0x8 cod eroare=0x18`.
- **Concluzie: nu e o problemă de mai multe nuclee**; e determinist, pe un singur nucleu, la același loc din nucleu — ceva specific acestui
  procesor (AMD Zen 2) sau acestei mașini, pe drumul `kronos-calcul` (QEMU în CI trece). Fișierul raportului urmează de la Adrian.

## Raportul (`raport-20261027-1.txt`, scris de OS pe stick, prima pornire, înainte de cădere)
- 0 erori în jurnal; XSAVE: x87, SSE, AVX (AVX2 da); GDT/IDT încărcate (CS=0x08, TR=0x28); 7288 MiB utilizabili, memorie și peste 4 GB.
- PCI: 29 de dispozitive pe 1 rădăcină; USB xHCI cu 2 dispozitive (camera 04f2:b6be, stick ADATA 29,6 GB); NVMe montat (/disk); /usb montat cu scriere.
- Rețea Realtek pornită corect, fără legătură (fără cablu). „Firul 3 a ieșit cu codul 0” la 30,4 s (programul de dinainte).
- **Indiciu pentru C-23:** OS-ul a fost testat până acum în CI doar pe procesoare emulate de tip Intel; aceasta e o mașină **AMD**. Diferențe
  Intel/AMD cunoscute în zona selectorilor/`SYSRET`/`IRETQ` și în XSAVE pot explica un #GP cu cod de selector (0x18). De încercat în QEMU cu
  `-cpu EPYC` / `-cpu EPYC-Rome` (Zen 2) și, dacă se poate, KVM pe AMD.
