# Stick-ul Cyber Universe OS (construit în sesiune, fără GitHub Actions)

Comanda C-35 / decizia din 28 oct 22:20: cât timp testele automate GitHub sunt oprite, sesiunea OS construiește stick-ul,
îl testează în QEMU și pune aici **doar ultima arhivă**. Numărul, commit-ul, ora și suma SHA-256 sunt în `VERSIUNE.txt`.
Numerele încep de la **os-1001**, ca să nu se confunde cu Release-urile vechi de pe GitHub (ultimul: `os-197`).

## Ce e în arhivă
Aceleași fișiere ca într-un Release: `cyber-universe-usb.img` (varianta A, imaginea întreagă) și, pentru varianta B
(copiere în Windows pe un stick FAT32), `BOOTX64.EFI`, `kernel`, `initrd.tar`, `limine.conf`, `limine-uefi-cd.bin`, `cyber.rw`,
plus `VERSIUNE` și `SHA256SUMS`. Pașii: `docs/USB.md` din `cyber-universe`. **Fără** modelul Kronos și **fără** firmware NVIDIA
(verificat de `tools/stick-hub.sh` la fiecare arhivă). Modelul se pune pe stick separat, ca până acum.

## Ce e nou față de os-197
- `gpu vbios --detalii` (C-31): structura VBIOS-ului plăcii video, doar citire, cu „0 scrieri” afișat; intră și în `raport`.
  Driverul Cyber-GPU e la versiunea `8313973`.
- Licența proprietară pentru codul nou (C-32) — nu schimbă ce face sistemul.
- Viteza lui Kronos din C-29 era deja în os-197.

## Teste făcute înainte (os-1001, 28 oct 2026)
Suita QEMU: 78 din 80 la prima trecere + 1 sărit (internet); cele 2 picate (`fpu-smp`, `kronos-calcul`) = testul vechi al
ceasului cu 4 procesoare pe calculatorul de test cu 2 nuclee, ambele trec la reluare. Arhiva dezarhivată de probă (sumele OK),
iar imaginea pornește în QEMU de pe stick USB până la desktop. `actualizeaza` de pe stick caută tot Release-urile GitHub, deci nu vede arhivele de aici.
