# Stick-ul Cyber Universe OS (construit în sesiune, fără GitHub Actions)

Comanda C-35 / decizia din 28 oct 22:20: cât timp testele automate GitHub sunt oprite, sesiunea OS construiește stick-ul,
îl testează în QEMU și pune aici **doar ultima arhivă**. Numărul, commit-ul, ora și suma SHA-256 sunt în `VERSIUNE.txt`.
Numerele încep de la **os-1001**, ca să nu se confunde cu Release-urile vechi de pe GitHub (ultimul: `os-197`).

## Ce e în arhivă
Aceleași fișiere ca într-un Release: `cyber-universe-usb.img` (varianta A, imaginea întreagă) și, pentru varianta B
(copiere în Windows pe un stick FAT32), `BOOTX64.EFI`, `kernel`, `initrd.tar`, `limine.conf`, `limine-uefi-cd.bin`, `cyber.rw`,
plus `VERSIUNE` și `SHA256SUMS`. Pașii: `docs/USB.md` din `cyber-universe`. **Fără** modelul Kronos și **fără** firmware NVIDIA
(verificat de `tools/stick-hub.sh` la fiecare arhivă). Modelul se pune pe stick separat, ca până acum.

## Ce e nou (os-1003 = commit `aa59e93`, același cod de stick ca Release-ul GitHub `os-208`)
- **Kronos mai rapid pe multe nuclee** (C-40): un nucleu liber e trezit imediat când un fir are de lucru (înainte aștepta până la 10 ms),
  mai puține așteptări între fire la fiecare simbol (49 în loc de 61), textul apare pe ecran pe rânduri, nu simbol cu simbol.
  Simbolurile generate sunt aceleași. Opțiune nouă: `--fara-ecran` (textul doar la sfârșit).
- `kronos-calcul --cauta` alege numărul de fire după media a 5 treceri (contează și firele care întârzie).
- Tot ce era în os-1002 (`gpu fwsec`, `gpu firmware`, `gpu vbios --detalii` etc.).

## Teste făcute înainte (os-1003, 29 oct 2026)
Suita QEMU: 77 din 80 + 1 sărit la prima trecere; `ghpush` (serverul local de test), `fpu-smp` și `kronos-calcul` (ceasul cu 4 procesoare
pe gazda cu 2 nuclee) au trecut la reluare. Test nou: un fir nou pornește pe un nucleu liber în ~40 µs. Arhiva dezarhivată de probă: toate sumele OK.
