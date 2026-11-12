# ASUS TUF F15 — 12 nov 2026 20:20, stick CYBER-UNIV, os-295
- **Pornește până la desktop** (C-109 rezolvat). Mouse prin receptorul USB (1ea7:0066) merge (P6-80); touchpad-ul nu (I2C, ca la Lenovo).
- `hw`: i7-11800H, 1920×1080, 65239 MiB liberi. Driver folosit: USB xHCI (2), rețea Realtek RTL8168 [rtl8168] (fără cablu). Fără driver: Intel UHD (8086:9a60), Wi-Fi Intel AX (8086:43f0),
  **controlerul de stocare Intel 8086:9a0b = VMD (Intel RST) → `/disk: nemontat`** — discul NVMe Samsung e ascuns în spatele VMD; NVIDIA **10de:2520 (RTX 3060 Laptop, GA106)** + audio HDMI 10de:228e.
  USB: cameră 322e:202c, bluetooth 8087:0026, stick 13fe:6700, receptor tastatură/mouse 1ea7:0066.
- Idee de viitor (OS): suport VMD (ca discul NVMe al laptopurilor cu Intel RST să fie văzut), driver Wi-Fi Intel AX, I2C-HID pentru touchpad.
- `gpu identifica`: gpu0 Intel 8086:9a60 nesuportat; **gpu1 10de:2520 RTX 3060 Laptop**: Command 0000 (Memory Space oprit de firmware — placa NVIDIA „adormită” de laptop, hibrid Optimus), BAR0 16 MiB, BAR1 8192 MiB (Resizable BAR), „dispozitiv nesuportat 10de:2520”, registre necitite, **zero scrieri** — protecția corectă.
- `test tot` (20:25): PASS procesor (118 vectori), ceas, temporizator, stick (scrierea pe stick-ul vechi CYBER-UNIV merge), **PASS placă video** (NVIDIA 10de:2520, doar ID-uri); FAIL rețea (fără cablu). Raport `test-tot-20261112-1.txt` pe stick.
- `gpu lant` pe CYBER-UNIV (20:28): „acest sistem nu poate scrie în placă: lanțul va rula doar citire” + după DA „dispozitiv nesuportat 10de:2520” → două protecții, zero scrieri.
