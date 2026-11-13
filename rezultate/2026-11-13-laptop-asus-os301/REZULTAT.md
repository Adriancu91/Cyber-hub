# ASUS TUF F15 (GA106) — 13 nov 2026 ~07:35–07:40, os-301 (cyber-gpu 835f24d), stick de test, fără cablu de rețea

- Pornire: ok. Fără cablu, rețeaua scrie diagnosticul DHCP în primele ~2 min peste prompt (normal, 6 runde) — `cyber>` era acolo.
- **`wifi identifica` (C-118 W0) — TRECE:** wifi0 00:14.3 8086:43f0 Wi-Fi 6 AX201 (CNVi, Tiger Lake-H), subsistem 0074:8086 rev 11, clasa 02:80:00; Command 0000, stare D0; BAR0 0x622f28c000 64 biți; capabilități 01 05 10 11; „legătura PCIe ? x0” (CNVi, fără legătură proprie). **Registrele CSR necitite: Memory Space oprit de firmware** (ca la GPU) → pentru W1 trebuie o „trezire” ca la `gpu tur --trezire` (DA separat). Zero scrieri.
- **`gpu identifica` — TRECE:** gpu0 Intel 9a60 (Command 0007) nesuportat; gpu1 01:00.0 10de:2520 **GeForce RTX 3060 Laptop, familia GA106**, subsistem 16f21043, Command 0000, D0; BAR0 0x85000000 (16 MiB), BAR1 0x6000000000 (8192 MiB, ReBAR), BAR3 0x6200000000 (32 MiB), BAR5 0x4000 I/O. Reset C-103: FLR da, No_Soft_Reset=1. Zero scrieri.
- **`gpu tur --trezire` (C-116 pasul 3 partea de citire) — TRECE, 45 de fapte:**
  - BOOT_0 `0xb76000a1`, BOOT_42 `0x176a1000` → chip GA106, consecvent; legătura gen4 x8 (max gen4 x16).
  - GFW progres `0xff`, runde 1 (firmware-ul de pornire terminat); 0x118128 = 0x00008b8f.
  - VBIOS: IFR nu, **3 imagini** (0x00000 tip 0x00 65024 o 10de:2520; 0x0fe00 tip 0xe0 22016 o 10de:2200; 0x15400 tip 0xe0 415744 o 10de:2200); BIT la 0x1b0; **versiune 94.06.1e.00.23** (= raportul UHL din Windows).
  - FWSEC: PMU 0x7aafe; descriptor v3 la 0x2c834 (antet 0x4ac, ucode 0xe900, imem 0xe100, dmem 0x800); 3 semnături, mască 0x0007, motoare 0x0400, ucode_id 9.
  - I6: siguranța 0x8241e0 = 3 (versiunea 2, semnătura 2); **VRAM 6144 MiB; WPR2 coborât (pornire rece) → i6.trece = da**. 0x118234=0x3ff, 0x1183a4=0x1800, 0x1fa828=0.
  - **Scrieri: 2, ambele în registrul Command al PCI (pornit, apoi repus 0000); 0 în registrele plăcii; 0 refuzate.** 11 pagini mapate pe rând, fereastra 16 MiB doar citire.
  - Jurnal pe stick: `/usb/raport/gpu-jurnal-003.txt` (24 rânduri). USB: 60 scrieri, 367,7 ms total, medie 6,1 ms, max 242,5 ms; 25 sincronizări ~0 ms → **fără încetinirea de ~1 s/rând** pe acest stick.
- Concluzie: laptopul e acum citit complet cu driverul nostru (ca workstation-ul). Pentru Cyber-GPU: GA106 trece testele de citire, VBIOS/FWSEC găsite; următorul pas pe laptop (I6 etc.) cere **DA-ul separat** al lui Adrian (C-116 pasul 3).
- **`analiza` (C-117) — TRECE:** sesiunea 20261113-0741, `/usb/raport/uhl/ASUSTeK-COMPUTER-INC-ASUS-TUF-Gaming-F15-FX506HM/20261113-0741/` (inventory.json 328 KiB rămâne pe stick; inventory.redacted.json + report.txt). SMBIOS: ASUS TUF Gaming F15 FX506HM, firmware FX506HM.318; i7-11800H; RAM 65273 MiB (2 module). PCI 24 de funcții cu legături/D-states/ReBAR; ACPI 32 de tabele; USB 4 dispozitive. Statusuri: CONFIRMED 34, MEASURED 1132, DOCUMENTED 53, INFERRED 1, UNKNOWN 33, UNSUPPORTED 5, NOT_TESTED 38. 0 scrieri.
  **De îmbunătățit (pentru echipa OS):** (1) „placa NVIDIA: 0 fapte | cip – | VRAM – | GFW –” — `analiza` nu refolosește faptele `gpu tur --trezire` din aceeași sesiune (pe laptop placa are Memory Space oprit); (2) „16 fire în MADT, 1 pornite” (un singur nucleu — limită cunoscută).
- **`test tot` — 6/7:** PASS procesor (118 vectori, 80 ms), ceas, temporizator (200/200 ms), stick (4 KiB), **placa video** (doar ID-uri), **wifi** (rândul nou W0, nimic scris); FAIL rețea = fără cablu (așteptat). Raport `/usb/raport/test-tot-20261113-1.txt`.
- Rapoartele sunt pe stick (fără token); Adrian le aduce din Windows.
