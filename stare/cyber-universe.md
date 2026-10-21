# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-10-22 00:40 (ora României) · **de:** sesiunea OS pornită manual de centrul de comandă (23:27)

## Acum
- **Testul 2 citit și reparat (00:40):** NVMe merge. Pentru placa Realtek (trimitea, nu primea): driverul pornește acum
  partea de cablu a plăcii (PHY), așteaptă legătura, iar `net` arată starea legăturii. Pentru `/usb` nemontat: acceptă stick-uri
  formatate în Windows și „trezește” stick-urile reale; `hw` spune de ce nu s-a montat. Toate testele trec.
- Atenție: în seara asta au lucrat **două sesiuni OS deodată** (aceasta și cea de la 23:40). Cealaltă face rădăcinile reale (P6-02);
  varianta mea de P6-02 e păstrată deoparte (`wip/P6-02-b`), ca să nu se ciocnească.
- **Deblocat** după testul tău pe Lenovo (C-2): rezultatul e trecut în `docs/HARDWARE.md`, ghidul `docs/USB.md` are acum
  varianta „fișiere copiate pe FAT32” și nota despre Secure Boot. Comanda nouă **`hw`** arată tot hardware-ul pe o pagină.
- **Faza 5 închisă** (suita și Kronos ca module mutate după suită). **Faza 6 planificată** (C-3): 10 sarcini, P6-01 … P6-10.
- **P6-01 gata în cod:** driver pentru placa ta de rețea Realtek RTL8168 (`10ec:8168`), testat față de un model al cipului
  (QEMU nu are acest cip). Merge sau nu pe laptop — afli la testul 2.
- 41 de scenarii automate trec; CI verde.

## Urmează
- P6-02: rădăcinile reale de încredere, ca `fetch https://` să meargă cu site-uri adevărate.
- P6-03 (JSON) → P6-04 … P6-06: aplicația „Claude” (linie de comandă, fereastră de chat, unelte cu confirmare).
- P6-07/P6-08: actualizare din GitHub; P6-09: trimitere pe GitHub din OS.

## Ce oferă proiectul celorlalți
- Bibliotecile `crypto/` și `tls/` (Rust, fără dependențe, MIT); acum și `rtl8168/` (driver de rețea cu model de test).
- Infrastructura de test pe scenarii (`tests/scenarios.txt` + `tools/test.sh`).

## De ce are nevoie de la ceilalți
- Nimic.

## Blocaje / nevoie de Adrian
- **Testul 3 (când e verde CI-ul pentru commit-ul `2f1fd30` sau mai nou):** la fel ca testul 2, cablu băgat. Poze: `net` (linia
  „legatura: …” — spune dacă placa vede cablul), `ping 1.1.1.1`, `hw` (linia `/usb: …` cu motivul, dacă tot nu merge).
- **Testul 2 pe laptopul Lenovo (când ai timp; ia ultima imagine `stick-usb` din GitHub Actions, CI verde):**
  1. Copiezi fișierele noi pe stick (ca data trecută), Secure Boot oprit, pornești de pe stick.
  2. **Bagă un cablu de rețea** în laptop (la router) înainte de pornire.
  3. Pe desktop apasă **Esc** → consola text `cyber>` (poză: arată că merge).
  4. Scrie `hw` + Enter → **poză** (o singură poză cu tot hardware-ul; dacă nu încape, două).
  5. Scrie `net` → poză; apoi `ping 1.1.1.1` → poză (aici vedem dacă merge driverul Realtek).
  6. Scrie `ls /disk` și `ls /usb` → poză.
  7. Dacă ai o tastatură USB externă: conecteaz-o și scrie `help` cu ea.
  8. Cronometrează cât durează de la alegerea stick-ului până apare desktopul.
- **Pentru pașii următori ai Fazei 6 (nu acum, îți spun când):** un fișier `claude.key` pe stick cu o cheie API Claude
  (ideal cu limită mică de cheltuieli) — pentru P6-04; un token GitHub „fine-grained” pentru un singur depozit, în
  `github.token` pe stick — pentru P6-09. Cheile nu ajung niciodată în repo sau în hub.
- P3-10 (închiderea Fazei 3) așteaptă pozele testului 2. B-003 / P5-07 (suita ca modul): mai târziu.
