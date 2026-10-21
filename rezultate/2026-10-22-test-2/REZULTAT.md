# Testul 2 al Cyber Universe OS pe laptopul Lenovo (AMD) — 22 octombrie 2026, ~00:00

**Scris de centrul de comandă din pozele lui Adrian.** Imaginea: artefactul CI din commit-ul `4bd215d` (cu driverul Realtek P6-01 și
comanda `hw`), fișierele copiate pe stick FAT32 **formatat în Windows** (nu imaginea brută). Cablu de rețea băgat la router înainte de pornire.

## Ce a mers
- **Pornire în ~15 secunde** de la alegerea stick-ului până la desktop (cronometrat de Adrian).
- **`hw` merge** (poza `01-hw.jpg`): procesor **AMD Ryzen 5 4500U with Radeon Graphics**; memorie liberă 7380 MiB, folosită 18812 KiB
  (heap 504 / 17232 KiB); „pornit de 97 s” la momentul comenzii.
- **Drivere legate pe hardware real:** `10ec:8168` → `[rtl8168]`, `144d:a809` → `[nvme]`, `1022:1639` ×2 → `[xhci]`. Restul `[-]` (fără driver).
- **NVMe merge:** `/disk: montat (2 intrari)`; `ls /disk` → `EFI/`, `System Volume Information/` (poza `04-ls-disk.jpg`) — OS-ul citește
  partiția de sistem a discului Samsung real.
- **USB:** controlerele xHCI pornesc; dispozitive văzute: `04f2:b6be` (cameră), `125f:db8a` (stick ADATA, Mass Storage).
- **Driverul Realtek pornește și citește MAC-ul real:** `Realtek RTL8168/8111 MAC 38:f3:ab:6b:11:34` (prefix Lenovo); **pachete trimise 4**.

## Ce NU a mers
1. **Recepție pe Realtek: 0 pachete primite.** DHCP nu a primit răspuns, așa că OS-ul a rămas pe configurația implicită
   (`IPv4 10.0.2.15 / 255.255.255.0, ruta 10.0.2.2, DNS 10.0.2.3` — adresele din emulatorul QEMU). `ping 1.1.1.1` → „niciun raspuns” ×4
   (pozele `02-net.jpg`, `03-ping.jpg`). Trimiterea pare să meargă (contorul crește), recepția nu: de verificat în driver inelul RX,
   întreruperile/polling-ul, starea legăturii (link up/speed), filtrul de adrese MAC (RxConfig) și dacă cele 4 „trimise” au ieșit cu adevărat pe fir.
2. **`/usb: nemontat`**, `ls /usb` → „nu exista” (poza `05-ls-usb.jpg`), deși stick-ul e enumerat. Cauza probabilă: stick-ul a fost
   **formatat în Windows** (MBR cu o partiție sau „superfloppy” fără tabelă), iar montarea caută tabelă GPT ca în imaginea `stick-usb`.
   De suportat MBR + superfloppy la montare (și la auto-actualizare, care trebuie să scrie pe exact acest stick).
3. (Nu e defect, doar de știut) configurația de rețea implicită din QEMU rămâne activă când DHCP eșuează; pe hardware real ar fi mai clar
   „fără adresă” decât o adresă falsă.

## Verificări suplimentare (00:09)
- **Ledul mufei de rețea e aprins** → legătura fizică (link) e stabilită; problema de recepție e în driver / întreruperi, nu în cablu.
- `help` (poza `06-help.jpg`): comenzile disponibile sunt help, ls, cat, run, desktop, mod, ping, host, http, tastatura, mem, lspci, lsusb,
  net, hw, uptime, reboot, exit. **Nu există o comandă de jurnal** (mesajele nucleului/driverului nu se pot vedea după pornire).

## Neverificat
- Tastatură USB externă; consola după Esc a fost folosită (prima poză e ecranul consolei gol); `help` și ledul mufei de rețea — Adrian le verifică acum.
