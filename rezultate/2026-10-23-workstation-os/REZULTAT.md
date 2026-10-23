# Prima pornire a Cyber Universe OS pe workstation — 23 octombrie 2026, 09:45 (Release os-161)

**Calculator:** Dell, placă de bază 0X75JG, **Intel Core i9-10980XE** (18C/36T), 128 GB, RTX 3070 Ti (bus B3). Inventarul din Windows:
`rezultate/2026-10-23-k0-workstation/`. **BIOS:** VT-d (IOMMU) **oprit** (poza 01); Secure Boot oprit pentru test (poza 02), de repus pe Enabled
înainte de Windows (BitLocker). Pornit din meniul F12, stick ADATA cu os-161.

## Ce s-a văzut (`hw`, poza 03)
- Procesor: `Intel(R) Core(TM) i9-10980XE CPU @ 3.00GHz`; memorie liberă **130.752 MiB**, folosită 23.832 KiB; pornit de 74 s.
- **PCI: doar magistrala 00 și 02** — punte gazdă `8086:2020`, `8086:2021` ×8, `2024/2025/2026`, `2014/2015/2016`, xHCI `8086:a2af` [xhci], `a2b1`,
  `a2ba`, **SATA AHCI `8086:a282` [ahci]**, punți `a290`, `a296`, `104c:8240` (02:00.0), ISA `a2d2`, `a2a1`, audio `a2f0`, SMBus `a2a3`,
  **rețea Intel `8086:15e3` (I219-LM) [-]**. **Lipsesc placa NVIDIA (B3:00.0) și, probabil, NVMe-ul**.
- USB: port 2 `05ac:12a8` (iPhone), 5 `17ef:608d` mouse (HID), 6 `413c:2106` tastatură Dell (HID), 7 `04b8:11c7` (Epson), 10 `0bda:5411` hub,
  25 `0bda:0328` „stocare” (cititor de carduri intern), 26 `0bda:0411` hub. **Stick-ul ADATA nu apare** (e în spatele unui hub).
- `/disk: nemontat` (discul Windows neatins). `/usb: nemontat (stick-ul Generic- SD/MMC CRW nu e gata (TEST UNIT READY: CSW 1, sense 2/3a…)` =
  cititorul de carduri fără card („Medium Not Present”), luat drept stick.
- Rețea: `(nicio placa de retea cunoscuta)`.

## Ce înseamnă
1. **PCI pe mai multe rădăcini (cauza lipsei GPU-ului):** pe platforma Cascade Lake-X / Skylake-SP fiecare stivă IIO are propria magistrală-rădăcină
   (00, 17, 3A, 5D, …, B2), **nelegate între ele prin punți de la magistrala 0**. `pci/mod.rs` pornește doar de la `start_bus` și urmează punțile
   (`scan_bus(ecam, ecam.start_bus, …)`), deci tot ce e pe celelalte rădăcini e invizibil. Pe laptop (o singură rădăcină) nu se vedea problema.
2. **USB fără hub-uri:** dispozitivele din spatele hub-urilor nu sunt enumerate; și alegerea lui `/usb` ia primul „Mass Storage”, chiar fără mediu.
3. **Rețeaua workstation-ului:** Intel I219-LM (`8086:15e3`, familia e1000e) — fără driver; `e1000` din QEMU e alt cip.
4. **Ce merge:** UEFI + Limine pe Dell, procesor, 128 GB, tastatură/mouse USB, AHCI găsit, nimic scris pe disc.

## Completare 10:00 — `log pci 40` (poza 04)
Ultimul rând: **`pci: 27 dispozitive (ECAM la 0x60000000, magistralele 0-255)`**. MCFG declară toate cele 256 de magistrale, dar enumerarea
parcurge doar arborele de la magistrala 0 (00:xx și 02:00.0 prin puntea `00:1c.x`). Confirmă cauza din C-13 punctul 1. Clasele notate:
`00:05.4` 08:00:20 (IOAPIC), `00:08.1` 11:01:00, `00:14.2` 11:80:00 (termal), `00:16.0` 07:80:00 (MEI), `00:1f.2` 05:80:00 (PMC).

## Completare 10:02 — `log usb 30` (poza 05)
`controler XHCI pornit, 26 porturi, 7 dispozitive`: port 2 `05ac:12a8` (viteza 3), 5 mouse `17ef:608d` (viteza 2), 6 tastatură `413c:2106`
(viteza 2), 7 `04b8:11c7` (clasa ff, viteza 1), **10 hub `0bda:5411` (clasa 09:00:02, viteza 3)**, 25 `0bda:0328` Mass Storage (viteza 4),
**26 hub `0bda:0411` (clasa 09:00:03, viteza 4)**. Hub-urile sunt doar identificate, porturile lor nu sunt enumerate → stick-ul ADATA (în spatele
unui hub) lipsește. Port 25: SET_CONFIGURATION și Configure Endpoint ok, apoi **30 de încercări TEST UNIT READY, toate CSW 1, sense 2/3a/00**
(„Medium Not Present”, cititor de carduri gol) → „stick-ul de pe portul 25 nu pornește”. Confirmă C-13 punctele 2 și 3. Mouse și tastatură merg.
