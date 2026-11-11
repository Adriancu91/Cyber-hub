# Laptop Lenovo (i5-1135G7, 8 GB, tastatură germană) — 11 nov 2026 18:14, stick CYBER-UNIV (os-283)

- **Pornește complet până la desktop** (Start + ceas) — spre deosebire de ASUS TUF F15 (C-109, blocat după MADT). Același tip de procesor (Tiger Lake, 11th gen) → la ASUS cauza ține mai probabil de firmware-ul/setările ASUS (ex. x2APIC lăsat pornit), nu de generația procesorului.
- `hw`: ecran 1920×1080 (8 MiB), memorie liberă 7942 MiB; driver folosit: USB xHCI (2 controlere), SATA AHCI, NVMe (2646:2263), rețea Realtek RTL8168 [rtl8168]; fără driver: placa video Intel (8086:9a49 Iris Xe),
  Wi-Fi Intel (8086:a0f0), 1217:8621 (cititor de carduri O2), audio, Thunderbolt (9a1b), senzori. USB: tastatură HID, stick, bluetooth Intel 8087:0026, 04f3:0c4b (amprentă/touchpad ELAN), 174f:244c (cameră).
- Rețea: RTL8168 cu driver, **fără cablu** (legătură: nu, DHCP fără răspuns). Wi-Fi Intel fără driver.
- `test tot` (18:18): PASS procesor (118 vectori de calcul în 100 ms), PASS ceas (RTC), PASS temporizator (200 ms = 200 ms), PASS stick (4 KiB scriși/citiți);
  FAIL rețea (fără cablu — așteptat), LIPSĂ placă video NVIDIA (corect, are Intel Iris Xe). Raport: `/usb/raport/test-tot-20261111-1.txt` — se urcă la următorul `trimite`.
- Idee pentru mai târziu: driver Wi-Fi Intel (8086:a0f0, AX201) — fără cablu, laptopurile nu au rețea în OS.
- Touchpad-ul **nu merge** (Adrian, 18:24). Probabil e legat prin I2C (controlerele Intel Serial IO 8086:a0e8 / a0eb apar „alt dispozitiv [-]”), iar OS-ul are doar mouse PS/2 + USB HID. De făcut pe viitor: driver I2C-HID pentru touchpad-uri. Un mouse USB ar trebui să meargă.
- Stick-ul de test TESTGPU pornește și el pe Lenovo. `gpu identifica`: Intel 8086:9a49 → „dispozitiv nesuportat”, registre necitite, **zero scrieri**. `gpu lant` + DA: „nicio placă NVIDIA”, oprit imediat, zero scrieri — protecția merge. Mouse USB nu merge nici el (Adrian: nici data trecută) — de verificat suportul mouse USB HID + conectarea după pornire.
