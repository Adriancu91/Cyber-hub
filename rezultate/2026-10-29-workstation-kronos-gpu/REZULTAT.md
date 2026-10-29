# Workstation, 29 oct 2026 (12:14–12:40) — Kronos în OS + Cyber-GPU I3/I3b/I4 (stick `os-206`, cu Adrian de față)

Stick: `os-206` (commit `62130bb`), cyber-gpu `2c9c90c`, model `kronos_459_q8_0.kgr` (SHA-256 = cea așteptată), firmware 570.144 pe stick.
Raportul OS: `raport-20261029-1.txt`; reglajul scris de `--cauta`: `reglaj-i9-10980XE.txt`; poze 00–11.

## Kronos (C-29, C-27) — TOATE TREC, simboluri identice cu referința
| Pas | Rezultat |
|---|---|
| 1 `run kronos --n 5 Ana are mere.` (reglajul vechi: AVX2+FMA, 1 fir) | citit în **9790 ms** (țintă < 10 s ✓); `[2233, 1585, 32, 475, 50]` ✓; 100 simb/s (5 simboluri) |
| 2 `usb citire mare` + același | citit în **1070 ms** ✓, aceleași simboluri, nicio eroare USB |
| 3 `run kronos-calcul --cauta` | 32 de variante, **0 respinse**; cea mai bună: AVX2+FMA, **18 fire**, ordine j-t (11× față de scalar pe 1 fir); ~84 simb/s doar produsele; platou ~9 GB/s |
| 4 `--profil --n 64 Buna ziua` (18 fire) | **69,5 simb/s** (79,8 fără ecran); **așteptarea firelor 62,6 %**, ecranul 14,3 %; produse 12,06 GB/s |
| 5 `--fire 1` (text `buna ziua`, mic) | 43,2 simb/s (68,7 fără ecran); **ecranul 38,1 %** |
| 5 `--fire 36` | 48,1 simb/s (51,0 fără ecran); **așteptarea firelor 78,9 %** |
| 6 `run kronos --n 5 def suma(a, b):` | `\n    return a + b`, `[1510, 1947, 1358, 1646, 1376]` ✓ |
Ținta ≥ 150 simb/s pe toate nucleele: **neatinsă** (max 69,5 / 79,8). Frânele măsurate: sincronizarea firelor și afișarea pe ecran, nu calculul.
Față de 28 oct (os-195): 7,9 / 6,2 / 4,8 simb/s pe 1 / 18 / 36 fire → acum 43–70 simb/s; încărcarea 30 s → 1,07 s.

## Cyber-GPU — I3 TRECE, I3b TRECE, I4: fișierele oficiale 4/4, parserul nostru 1/4 (0 scrieri în placă la toate)
- `gpu vbios`: 4 imagini (PCI-AT 0x0, EFI 0xfe00, FWSEC 0x24600, FWSEC 0x29c00), BIT 0x70 da, **complet: da**; 0 scrieri. Ruptura de la 0x24600 (28 oct) e reparată pe placă (C-30).
- `gpu vbios --detalii`: **rezumat: 4 imagini, 0 rupturi, criteriul I3: indeplinit**, 1149 citiri PROM, 0 scrieri.
- `gpu fwsec`: 2 imagini FWSEC (0x24600+0x5600, 0x29c00+0x5e400), tabela PMU la 0x87ecb (0x85 = FWSEC_PROD: da), descriptor v3 la 0x41208
  (ucode 0xea00, IMEM 0xe200, DMEM 0x800), 3 semnături (masca 0x0007 potrivită), ucode_id 9 → **criteriul I3b: TRECE**; 0 scrieri.
- `gpu firmware`: cele 4 fișiere **= oficial** (mărimi + SHA-256), `LICENCE.nvidia` prezentă; `gsp-570.144.bin` antet citit (ELF-64, .fwimage 63541248,
  .fwsignature_ga10x 4096); **booter_load, booter_unload, bootloader: „antet NECITIT: bin_size diferit de mărimea fișierului”** → criteriul I4: NU TRECE
  (4/4 oficiale, 1/4 antete). Greșeala e în `fw_hdr` (parserul nostru), nu în fișiere → C-39.
- Proba tinygrad (pasul 3, scrie în placă): **nefăcută** azi (lipsesc stick-ul Ubuntu și laptopul pentru SSH).
