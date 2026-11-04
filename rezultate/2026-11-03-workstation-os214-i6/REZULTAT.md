# Workstation 3 nov 2026 — os-214, Kronos #477, primul I6 pe placă

Dell Precision 5820, i9-10980XE (36 fire), RTX 3070 Ti. Adrian de față, 10:45–11:10. Pornit prin F12.

## Kronos în OS (stick-ul normal)
- `cpu porneste`: 36/36 nuclee în 443 ms.
- `run kronos-calcul --cauta`: 32 variante, 0 respinse; cea mai bună AVX2+FMA, 36 fire, j-t (62× față de scalar pe 1 fir, ~479 simb/s doar produsele).
  Proiecția (C-48): 1 fir ~83 → 32 fire ~488 simb/s doar produsele. Reglajul scris pe stick.
- `run kronos --control`: **CONTROL TRECE** (#477, 3 texte, SHA-256 bun, încărcat în 1,14 s).
- `--profil --fara-ecran --n 64 Buna ziua`: **125,4 simb/s** (1 nov: 123).
- `--profil --n 64 Buna ziua` (cu ecran): **125,4 simb/s** (1 nov: 70,3) → afișarea pe bucăți (C-48) a mers.
- Profil (cu ecran, 63 treceri, 8,23 ms/simbol): proiecția 240 ms = 46,3 % (2,09 GB/s, de ~12× mai lent decât fc/MLP),
  **așteptarea firelor 325,8 ms = 62,9 %**. Pragul 150 nu e atins; frâna = sincronizarea firelor + proiecția la generare.

## Placa (stick-ul de test `gpu-scrie`, pornire rece cu cablul scos 30 s)
- `gpu pregatire-i6`: VRAM 8192 MiB, FRTS 0x1ffe00000..0x1fff00000, WPR2 coborât: bun, **criteriul I6-citire: TRECE**, 0 scrieri. Jurnal `gpu-jurnal-001.txt`.
- `gpu i6 --scrie` + DA: ucode HS încărcat prin DMA: ok; FWSEC rulat; Bus Master pus la loc (0x0003); 2 scrieri config + 720 în registrele GSP.
  **rezultat I6: NU TRECE** — „verificare eșuată la 0x1fa824: așteptat 0x1ffe00, citit 0x1ffe00”.
- Analiza centrului de comandă: `check_frts` (cyber-gpu `gsp/falcon.rs`) compară (start, end), dar raportează doar start. Start-ul e IDENTIC → FWSEC a ridicat WPR2
  exact unde am cerut; diferă capătul (registrul HI). Cel mai probabil HI ține ultima pagină de 4 KiB (capăt inclusiv), nu capătul exclusiv. Deci probabil FRTS a reușit
  și verificarea noastră e greșită → C-58. Jurnalul complet (736 rânduri) e pe stick, `raport/gpu-jurnal-002.txt`, de copiat la fereastra următoare.
- După: oprire completă + cablul scos 30 s. Nu s-a repetat.

## Altele
- Intrarea fixă „Cyber Universe” în BIOS există; stick-ul de test a pornit din „UEFI: VendorCoProductCode 2.00”.
- Autologin pus de Adrian (netplwiz, cu parola). Bucla automată: primul tur rămâne pentru fereastra următoare.

## Jurnalul I6 copiat (4 nov 17:40, citire brută a stick-ului de test, fără nicio schimbare pe el)
- `gpu-jurnal-001.txt` (pregătirea, 9 rânduri) și `gpu-jurnal-002.txt` (I6, 737 rânduri) sunt aici.
- Jurnalul păstrează scrierile și citirile de pregătire; citirile de după FWSEC (LO/HI WPR2) nu sunt în el. Înainte: HI `0x1fa828` = 0 (WPR2 coborât).
  După FWSEC, verificarea a citit LO = `0x1ffe00` = exact începutul FRTS cerut (0x1ffe00000) → FWSEC-FRTS a ridicat WPR2 unde trebuia. HI-ul exact îl arată `os-222` (C-61).
