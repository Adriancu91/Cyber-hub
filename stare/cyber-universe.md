# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-11-20 16:00 (ora României) · **de:** sesiunea OS programată (14:40) — **`os-323` = tabloul de bord al plăcii (P6-105) + `gpu stare`, CI verde. C-152 gata în întregime.**

## Acum
- **20 nov 15:31 — testul 2 cu `os-322` a trecut:** viteza maximă acceptată (P5 → P0), 16 simboluri identice; **cu driverul 94,84 simb/s, mai repede decât procesorul (72,72)**; frâna e acum driverul (3,1 ms din 5,8 ms pe simbol). Pașii următori (P3 lipirea calculelor, #651, P7) — după decizia centrului de comandă / „da”-ul lui Adrian.
- **20 nov ~15:55 — `os-323` (P6-105, C-152 punctul 5):** Cyber-GPU `de4887d` (C-151 punctul 1). Tabloul de bord al plăcii, **oprit implicit**: doar cu `test-placa --tablou` (lista automată; se poate și `test-placa --i9 c135 --tablou`, `test-placa --flr-proba --tablou`) sau de mână `gpu lant --tablou` (cu DA). La sfârșitul lanțului, după I14 și rândurile `ks` (rezultatele deja pe stick): OS-ul dă plăcii o pagină de memorie, cere citirile la 500 ms, așteaptă 1,5 s, citește o dată, oprește. În raport: rândurile `kd …` (răspunsurile plăcii, temperatura, ceasurile, starea, încărcarea, motivele de încetinire, puterea, `sectiuni citite 0x7f` = toate). Un refuz = un rând, nimic altceva trimis. `gpu stare` arată ultimul tablou citit (placa nu e atinsă). Testat doar în SIMULARE (scenariul `gpu-tablou`: acceptat și refuzat).
- **Fără `--tablou`, `os-323` face exact ce face `os-322`** (viteza maximă în ciclu, proba FLR la cerere) — tabloul e o comandă nouă către placă, ținută separat de testul vitezei.
- `os-322` (viteza maximă, P6-106; FLR oprit implicit, P6-101) și `os-319` (comutatorul de pornire, ceasul de pază, temperatura procesorului) — neschimbate.

## Urmează
- Tabloul pe placă: `test-placa --tablou` cu `os-323`, când decide centrul de comandă. Proba FLR (`--flr-proba`) la fel.
- Coada fără Adrian e goală: sesiunile următoare verifică hub-ul, jurnalele testelor și CI.

## Ce oferă proiectul celorlalți
- `os-323`: tabloul de bord la cerere (`--tablou`, rânduri `kd`), `gpu stare`; ciclul cu viteza maximă, proba FLR la cerere, comutatorul de pornire, rândurile `discuri`, temperatura procesorului, ceasul de pază.
- Agentul din OS, ciclul automat, rapoartele urcate singure în hub.

## De ce are nevoie de la ceilalți
- Centrul de comandă: ciclul cu `os-322`/`os-323` (`bucla-automata.ps1 pregateste -DosarRelease <os-323> -TestPlaca`) și cifrele în hub (verdictul `ks`, blocul „viteza fata de os-313”, cele 16 simboluri); apoi, separat, un ciclu cu `test-placa --tablou`.
- Cyber-GPU: dacă placa refuză pornirea tabloului (clientul nostru, nu cel intern), varianta cu mânerele interne (doar cu „da”-ul lui Adrian).

## Blocaje / nevoie de Adrian
- Nimic urgent; testele le pornește centrul de comandă.
- Comutatorul de pornire (P6-102) contează pe workstation doar după ce stick-ul e primul în ordinea de pornire din BIOS — o singură schimbare, cu tine de față.
- Coada OS fără tine e goală după C-152: pașii următori vin din cifrele testelor sau dintr-o comandă nouă.
