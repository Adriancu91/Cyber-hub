# Workstation, 1 nov 2026 (11:35–11:50) — os-210, Kronos #477, Cyber-GPU I4 (cu Adrian de față)

Stick: `os-210` (commit `1fbf360`), model `kronos_477_q8_0.kgr` (SHA-256 `bcbe8187…3963` = cea așteptată), #459 alături ca rezervă, firmware 570.144 pe stick.
Raport OS: `raport-20261101-1.txt`; reglaj nou: `reglaj-i9-10980XE.txt`; poze 00–06.

| Test | Rezultat |
|---|---|
| `run kronos --control` | **CONTROL: TRECE (#477: 3 texte, simbolurile și textul = cele publicate de Kronos)**; model ales automat #477 |
| `gpu firmware` | **criteriul I4: TRECE (fișiere oficiale 4/4, antete citite 4/4)**; 0 scrieri, 0 accese la placă (C-39 + C-42 confirmate pe fișierele reale) |
| `usb citire mare` + încărcare | 1170–1200 ms (fără ea: 9800 ms) |
| `run kronos-calcul --cauta` | 32 variante, 0 respinse; cea mai bună AVX2+FMA, **36 fire**, ordine t-j (67× față de scalar pe 1 fir); ~497 simb/s doar produsele, ~54 GB/s (pe 29 oct: 18 fire, ~84 simb/s, ~9 GB/s) |
| `--profil --n 64 Buna ziua` (cu ecran) | 70,3 simb/s; **afișarea pe ecran 45,7 %**; așteptarea firelor 32,6 %; „fără ecran ar fi 128,4” |
| `--profil --fara-ecran --n 64 Buna ziua` | **123,0 simb/s** (8,12 ms/simbol; 29 oct: 69,5 cu ecran / 79,8 fără) |

Profilul fără ecran (511,7 ms pentru 63 de treceri): **produs proiecție 238,7 ms = 46,6 %, doar 2,10 GB/s** (celelalte produse 17–52 GB/s);
așteptarea firelor 318,9 ms = 62,3 % (cea mai mare parte, probabil în proiecție); qkv 84,4; fc 81,7; ieșire MLP 78,9; cap 17,0; restul 7,0.
Concluzie: ținta ≥ 150 simb/s neatinsă încă (123); frâna rămasă e produsul „proiecție” (pare neîmpărțit pe fire) + afișarea pe ecran simbol cu simbol.
Textul generat repetitiv („Am fost la un restaurant de vis,”) — normal la greedy, nu e problemă de motor.
