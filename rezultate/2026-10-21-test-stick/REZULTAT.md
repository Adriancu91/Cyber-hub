# Primul test al Cyber Universe OS pe un calculator real — 21 octombrie 2026, ~22:05

**Scris de centrul de comandă, din videoclipurile și mesajele lui Adrian.** Imaginea testată: artefactul CI `stick-usb`
din commit-ul `cf80c3e` (rularea CI 39646110597), pus pe stick ca fișiere pe FAT32 (nu scris ca imagine brută):
`EFI/BOOT/BOOTX64.EFI`, `boot/kernel`, `boot/initrd.tar`, `boot/limine/limine.conf`, `boot/limine/limine-uefi-cd.bin`.

## Calculatorul
- Laptop **Lenovo ThinkPad** (alt calculator decât ThinkPad-ul suitei; eticheta de inventar NB-7211174), firmware UEFI Lenovo,
  tastatură cu aranjament german (Pos1/Ende).
- Disc intern: **NVMe Samsung MZVLQ256HAJD-000H1** (256 GB). Stick: **ADATA USB Flash Drive**, văzut ca „USB HDD”.
- Memorie: harta din jurnal arată un bloc mare „4443392 KiB utilizabila” peste 4 GB (deci ~8 GB în total).

## Ce s-a întâmplat
1. **Cu Secure Boot pornit:** alegerea stick-ului din meniul F12 → ecran negru ~1 s → înapoi în meniul de boot, fără mesaj (de două ori).
2. **Cu Secure Boot oprit:** pornește. Jurnalul nucleului apare pe ecran (harta memoriei cu zeci de rânduri `INFO mem: …`,
   „nucleu si module”, „bootloader (recuperabila)”, „ACPI NVS”, „rezervata”, „utilizabila”), apoi **desktopul „Cyber Universe”**
   cu bara de jos și butonul **Start**.
3. **Merge:** ecranul (rezoluția nativă, text clar), **touchpad-ul** (cursorul se mișcă), **click-ul** (fereastra „Demo” s-a deschis,
   cu dreptunghiul portocaliu și cursorul desenat în ea), **tastatura internă** (Start → Editor, Adrian a scris text în el).
4. **Nu merge:** **placa de rețea nu e văzută** (Adrian, 22:14) — de așteptat: driverul existent e doar pentru Intel e1000/e1000e,
   iar laptopul are altă placă Intel (cu fir) plus Wi-Fi. Identificatorul exact (`lspci`, de forma 8086:xxxx) urmează la testul 2.
5. **Testul 2, făcut pe loc (22:19), din Terminal (în fereastră):** `lspci`, `lsusb`, `mem` merg. Rezultatele exacte (pozele
   `05-lspci.jpg`, `06-lsusb-mem.jpg`):
   - **Platformă AMD** (nu Intel): punte gazdă `1022:1630` (Ryzen seria 4000, „Renoir”), punți PCI `1022:1632/1634/1635`, SMBus `1022:790b`, ISA `1022:790e`.
   - **Rețea cu fir: Realtek `10ec:8168`** (RTL8168/8111) la 01:00.0 — necunoscută OS-ului („nicio placa de retea cunoscuta”).
   - **Wi-Fi: Intel `8086:2723`** (Wi-Fi 6 AX200) la 02:00.0 — necunoscută; are nevoie de firmware de la producător (mai târziu).
   - **NVMe: Samsung `144d:a809`** la 03:00.0 (controler NVMe recunoscut în listă; `ls /disk` neîncercat).
   - **Video: AMD `1002:1636`** (grafică integrată Renoir) + audio `1002:1637`, `1022:15e2`, `1022:15e3`.
   - **USB: două controlere `1022:1639`** (xHCI AMD); dispozitive: `04f2:b6be` (cameră Chicony), `125f:db8a` **stick ADATA (Mass Storage)** — văzut.
   - **Memorie:** liberă 7377 MiB, folosită 21672 KiB (heap 17738) — deci ~8 GB RAM, OS-ul ocupă ~21 MB.
6. **Neverificat încă:** `ls /disk` (NVMe montat?), `ls /usb` (stick-ul montat?), consola text (Esc), tastatură USB externă, timpul de pornire. `lspci`, `lsusb`, `mem`, `ls /disk` (NVMe), `ls /usb`, `net`, consola text (Esc), tastatura USB externă,
   timpul de pornire. Adrian le face la următorul test, cu poze.

## Imagini
`00-meniu-boot.jpg`, `01-jurnal-pornire.jpg`, `02-desktop.jpg`, `03-fereastra-demo.jpg`, `04-start.jpg` (cadre din videoclipuri).

## Concluzie
**P3-09 (B-001): prima pornire pe hardware real a reușit** — nucleu, memorie, ecran, touchpad, tastatură, desktop, ferestre,
editor. Niciun blocaj, nicio panică vizibilă în videoclip. Lecție pentru `docs/USB.md`: pe Lenovo, cu Secure Boot pornit nu apare
nicio eroare, doar revine la meniu; și nu e nevoie de Rufus/Etcher — fișierele copiate pe un stick FAT32 ajung.
