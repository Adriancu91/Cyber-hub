# ThinkPad L15 Gen 2 + os-191 — 27 oct 2026, ~22:50 (Adrian)

Laptop: Lenovo ThinkPad L15 Gen 2 (i7-1185G7, Tiger Lake, 16 GB, Iris Xe, Windows 11 Pro), Secure Boot oprit, pornit de pe stick (F12).
Fără cablu de rețea (Adrian nu are acces la router cu cablu; OS-ul nu are WiFi). Prima pornire a OS-ului pe acest laptop.
(Prima încercare n-a pornit: pe stick erau alte arhive, greșeala lui Adrian; corectat.)

## Ce s-a văzut (`poza-1-kronos-calcul-GP.jpg`)
- **Pornire: DA.** Shell-ul `cyber>` apare.
- **`cpu porneste`: 6 nuclee pornite din 6** (APIC 1, 2, 4, 5, 6 + BSP), fiecare în ~10 ms; „planificatorul rulează fire pe 6 nuclee”.
  Notă: i7-1185G7 are 4 nuclee / 8 fire — de verificat de ce tabela arată 6 (setare BIOS? MADT?). Rândul `cpu:` spune și
  „(parcate: firele rămân pe primul nucleu)”.
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
  procesor (Tiger Lake) sau acestei mașini, pe drumul `kronos-calcul` (QEMU în CI trece). Fișierul raportului urmează de la Adrian.
