# Stick-ul Cyber Universe OS (construit în sesiune, fără GitHub Actions)

Comanda C-35 / decizia din 28 oct 22:20: cât timp testele automate GitHub sunt oprite, sesiunea OS construiește stick-ul,
îl testează în QEMU și pune aici **doar ultima arhivă**. Numărul, commit-ul, ora și suma SHA-256 sunt în `VERSIUNE.txt`.
Numerele încep de la **os-1001**, ca să nu se confunde cu Release-urile vechi de pe GitHub (ultimul: `os-197`).

## Ce e în arhivă
Aceleași fișiere ca într-un Release: `cyber-universe-usb.img` (varianta A, imaginea întreagă) și, pentru varianta B
(copiere în Windows pe un stick FAT32), `BOOTX64.EFI`, `kernel`, `initrd.tar`, `limine.conf`, `limine-uefi-cd.bin`, `cyber.rw`,
plus `VERSIUNE` și `SHA256SUMS`. Pașii: `docs/USB.md` din `cyber-universe`. **Fără** modelul Kronos și **fără** firmware NVIDIA
(verificat de `tools/stick-hub.sh` la fiecare arhivă). Modelul se pune pe stick separat, ca până acum.

## Ce e nou (os-1002 = același cod ca Release-ul GitHub `os-206`, commit `2c8584a`)
- **`gpu fwsec`** (C-38, pasul I3b al ferestrei C-36): unde e programul FWSEC în VBIOS, doar citire, „0 scrieri”.
- **`gpu firmware`** (C-38, pasul I4): verifică cele 4 fișiere GSP 570.144 din `firmware\nvidia\ga102\gsp\` de pe stick (+ `firmware\LICENCE.nvidia`):
  pentru fiecare „ok … = oficial” + „antet citit”, la final `criteriul I4: TRECE`/`NU TRECE`. **Nu atinge placa video.** Firmware-ul NU e în arhivă.
- `gpu plan` are pașii 5c și 5d. Driverul Cyber-GPU e la versiunea `2c9c90c`.
- De la os-1001: `os-205` (C-29, C-31 `gpu vbios --detalii`, C-32, C-37). Release-urile GitHub merg din nou; arhiva de aici e doar rezervă.

## Teste făcute înainte (os-1002, 29 oct 2026)
Suita QEMU: 80 din 80 + 1 sărit (internet; `appnet` a trecut la reluare). CI GitHub verde (la reluare: `kronos-calcul`, ceasul cu 4 procesoare)
→ Release `os-206`. `gpu firmware` încercat de mână cu un stick de test de 128 MiB cu fișiere false de mărimea oficială: 4 × „ALT CONTINUT”,
fără probleme de memorie. Arhiva dezarhivată de probă: toate sumele OK.
