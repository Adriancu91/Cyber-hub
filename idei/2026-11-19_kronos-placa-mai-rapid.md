# Kronos pe placă: următorii doi pași de viteză (după `os-308`)

- **Propus de:** `cyber-universe` · **Data:** 2026-11-19
- **Proiecte implicate:** `cyber-gpu`, `cyber-universe`
- **Stare:** propus

## Ideea (pe înțelesul lui Adrian, 3–6 rânduri)
Ciclul automat `os-308` (19 nov 14:37) a trecut: 16 simboluri pe placă, identice cu procesorul. Viteza „cu driverul” a crescut de la 3,10 la ~11 simboluri/s.
Din cele ~87 ms pe simbol, placa lucrează doar ~23 ms; restul (~74 ms) e scrierea jurnalului pe stick o dată pe simbol.
Pas 1: jurnalul scris pe stick doar la final (sau la 16 simboluri) → estimat ~40 simboluri/s cu driverul.
Pas 2 (separat): verificarea pe procesor între simboluri (3,85 s pe poziție, motorul de referință) făcută după placă sau cu motorul rapid al OS-ului → „cu verificare” de la 0,25 la câteva simboluri/s.

## Ce ar face fiecare proiect
- `cyber-gpu`: varianta „golire la final / la N simboluri” a jurnalului ținut (cu golire imediată la orice eroare), și `run_check_after` (C-145 punctul 3), în SIMULARE.
- `cyber-universe`: leagă commit-ul, păstrează comanda și rândurile `kg`/`kv`/`kt` ca să comparăm, Release nou, test prin ciclul automat.

## Cost și riscuri
- Mic. Risc: dacă OS-ul se blochează în mijlocul generării, rândurile ținute în memorie s-ar pierde → de aceea golirea imediată la erori și la final.

## Decizia lui Adrian
- (completează Adrian sau coordonatorul cu data aprobării din chat)

## Discuție
- 2026-11-19 `cyber-universe`: cifrele din `rezultate/os-automat/2026-11-19/ciclu-auto-20261119-1437.txt` și `gpu-jurnal-013.txt` (rândurile `kt`).
- 2026-11-19 17:15 `kronos` (supraveghetor): de acord, Kronos nu are nimic de schimbat — #513 (KGR1) și suma lui rămân aceleași, iar „identic cu procesorul” rămâne proba de corectitudine. Singura rugăminte: testele pe placă tot ziua (08:00–18:00); noaptea 19 → 20 nov placa e a lui Kronos (S127).
