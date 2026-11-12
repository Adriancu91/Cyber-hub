# ASUS TUF F15 — 12 nov 2026 20:20, stick CYBER-UNIV, os-295
- **Pornește până la desktop** (C-109 rezolvat). Mouse prin receptorul USB (1ea7:0066) merge (P6-80); touchpad-ul nu (I2C, ca la Lenovo).
- `hw`: i7-11800H, 1920×1080, 65239 MiB liberi. Driver folosit: USB xHCI (2), rețea Realtek RTL8168 [rtl8168] (fără cablu). Fără driver: Intel UHD (8086:9a60), Wi-Fi Intel AX (8086:43f0),
  **controlerul de stocare Intel 8086:9a0b = VMD (Intel RST) → `/disk: nemontat`** — discul NVMe Samsung e ascuns în spatele VMD; NVIDIA **10de:2520 (RTX 3060 Laptop, GA106)** + audio HDMI 10de:228e.
  USB: cameră 322e:202c, bluetooth 8087:0026, stick 13fe:6700, receptor tastatură/mouse 1ea7:0066.
- Idee de viitor (OS): suport VMD (ca discul NVMe al laptopurilor cu Intel RST să fie văzut), driver Wi-Fi Intel AX, I2C-HID pentru touchpad.
- `gpu identifica`: gpu0 Intel 8086:9a60 nesuportat; **gpu1 10de:2520 RTX 3060 Laptop**: Command 0000 (Memory Space oprit de firmware — placa NVIDIA „adormită” de laptop, hibrid Optimus), BAR0 16 MiB, BAR1 8192 MiB (Resizable BAR), „dispozitiv nesuportat 10de:2520”, registre necitite, **zero scrieri** — protecția corectă.
- `test tot` (20:25): PASS procesor (118 vectori), ceas, temporizator, stick (scrierea pe stick-ul vechi CYBER-UNIV merge), **PASS placă video** (NVIDIA 10de:2520, doar ID-uri); FAIL rețea (fără cablu). Raport `test-tot-20261112-1.txt` pe stick.
- `gpu lant` pe CYBER-UNIV (20:28): „acest sistem nu poate scrie în placă: lanțul va rula doar citire” + după DA „dispozitiv nesuportat 10de:2520” → două protecții, zero scrieri.

## Inventarul din Windows (Adrian, 12 nov 22:14, unealta UHL; fără numere de serie aici)
- Model: **ASUS TUF Gaming F15 FX506HM** (placa FX506HM, BIOS FX506HM.318 din 17.06.2025, AMI, UEFI, **Secure Boot oprit**). FX506H* = modelul 2021 → după studiul C-95, **fără MUX** (ecranul pe Intel UHD 9a60).
- Procesor i7-11800H (Tiger Lake-H, 8 nuclee/16 fire, AVX-512, x2APIC), 64 GB DDR4-3200 (2×32 GB SK Hynix), Windows rulează cu VBS/Hyper-V.
- **NVIDIA RTX 3060 Laptop GPU 10de:2520 rev A1, subsistem 1043:16F2, 6 GB VRAM**, PCIe Gen4 x8 (max x16), driver Windows 32.0.16.1091; audio HDMI 10de:228e.
- **Wi-Fi Intel AX201 160 MHz** (8086:43F0, subsistem 8086:0074 — CNVi integrat, driver Netwtw10). Rețea pe cablu Realtek RTL8168 (10ec:8168 rev 15) — driverul nostru merge.
- **Disc: NVMe Samsung MZVL21T0HCLR (1 TB) în spatele Intel RST VMD 9A0B** (de aceea OS-ul nostru nu-l vede). Touchpad ELAN1203 pe I2C (HID I2C).
- ACPI: 31 de tabele, ECAM 0xC0000000 (bus 0–45), DMAR (VT-d), SSDT ×14, tabelul „RstVmdE”.

## Raportul UHL al lui Adrian (12 nov 23:03; NVML/CUDA/Windows, doar citire; serialele ascunse) — date pentru C-116
- **VBIOS 94.06.1E.00.23** (șirul din registrul driverului: „Version94.6.1e.0.23”). Imaginea VBIOS nu e citibilă din Windows (UHL n-o citește — corect, nu ne trebuie: driverul nostru o citește din PROM).
- GA106M, compute capability **8.6**, **30 SM**, L2 **3 MiB**, VRAM **6 GiB / 192 biți**, frecvențe maxime: grafică/SM 2100 MHz, memorie 7001 MHz, video 1950 MHz.
- Putere (NVML): limită implicită 80 W, aplicată 95 W, interval 1–95 W; în repaus ~20–26 W, 58–62 °C, P0. TGP documentat 60–115 W.
- PCIe: Gen4 x16 max (x8 activ), BAR1 = 8 GiB @0x6000000000 (Resizable BAR), payload 256 B, D3cold suportat (cod 1036). Calea ACPI: `\_SB.PC00.PEG1.PEGP` (rădăcina Intel PEG10 9A01).
- Concluzie: confirmă studiul C-95 (GA106, sm_86 ca GA104 — aceleași programe, mai puține SM: 30 față de 48), ce mai trebuie (VBIOS-ul laptopului, starea D0/Memory Space) vine din `gpu tur --trezire`.

## Raportul UHL de stocare (Adrian, 13 nov 01:31; doar citire, fără serii)
- **Intel VMD 8086:9A0B** la 00:0E.0 (clasa 0x010400 RAID, părinte root complex), driver Windows iaStorVD 19.5.2.1049; **funcție însoțitoare 8086:09AB „VMD Managed Controller” la 00:06.0** (clasa 0x088000, fără serviciu).
- SSD **Samsung PM9A1 (MZVL21T0HCLR-00BL7)**, firmware EL2QGXA7, 1 024 209 543 168 B, sector 512 B, în spatele VMD; calea ACPI `\_SB.PC00.VMD0.PEG0` (definiția VMD0 e într-un SSDT necitibil din Windows).
- GPT, 4 partiții: EFI 200 MiB FAT32, MSR 16 MiB, Windows 952,79 GiB NTFS, Recovery 891 MiB NTFS. SMART: 47 °C, 4 % uzură, ~2877 ore, 103 opriri nesigure, 0 erori.
- Pentru Cyber Universe: discul se vede doar cu un **driver VMD** (domeniu PCI suplimentar ascuns în spatele lui 9A0B; specificație: documentația publică Intel VMD + driverul Linux `vmd.c` citit ca specificație, GPL → fără cod copiat) **sau** cu VMD oprit în BIOS (atenție: Windows instalat pe RST poate să nu mai pornească — doar după verificare). Apoi NVMe (avem deja driver) + GPT + FAT32 (EFI) / NTFS (doar citire, mai târziu).
