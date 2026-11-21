# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-11-21 10:05 (ora României) · **de:** sesiunea OS programată (08:41) — lucrul continuu (C-158). Ultimul Release: **`os-324`**, CI verde.

## Acum
- **GATA DE TEST: os-324** — nou: „dieta driverului” (C-154, Cyber-GPU `4925469`), pornită DOAR în testul obișnuit al ciclului: pushbuffer-ul scris prin umbră (doar cuvintele schimbate) + înregistrările nezerorizate; nimic nou trimis la placă. FLR și `--tablou` oprite, viteza maximă ca în `os-322`. **Rândul pentru teste.txt:** `test-placa`. **Cifre așteptate:** aceleași 16 simboluri `[44, 10, 73, 2524, …, 15879, 1505]`; `kt dieta = 1`; `kt cuvinte VRAM pe simbol (median)` mult mai mic (SIMULARE: 48 față de 599); `kt median driver` de la 3 081 spre ~1 300 us (DEDUS, Cyber-GPU); simb/s cu driverul peste 94,84; în raport blocul „viteza fata de os-322” cu „logit-urile identice bit cu bit cu os-322? DA” (comparat prin abaterea maximă exactă `0x37880000` + simbolurile, fiindcă os-322 n-avea amprenta); plus rândurile noi `kt median citirea logit-urilor`, `kt median argmax`, `kt amprenta logit-urilor`.
- **Nota centrului de comandă (08:45, cele 11 scrieri refuzate la al doilea lanț al probei FLR):** jurnalul `os-323` nu spune care adaptor le-a refuzat (doar totalul), deci nu se pot lămuri din el. Din `os-324` lanțul scrie și rândul `scrierile refuzate pe pasi: <pas> <număr>, …` — la următorul test cu `--flr-proba` se vede exact pasul. Refuzul înseamnă că gardul a oprit scrierea (nimic n-a ajuns în placă), deci nu e un pericol; dacă pasul e `tur-dupa` (turul doar-citire), sunt încercări de scriere ale turului oprite intenționat.
- **C-159 (agentul viu), pasul 1, partea 1 gata (P6-108):** poarta comenzilor — semnătura HMAC-SHA-256, numărul exact următor, o singură dată (jurnal pe stick scris înainte de execuție), comenzile pe placă `REFUZAT` fără `permite-live-placa`, ecoul exact în fiecare răspuns; testat în QEMU cu cele 4 probe de refuz. Forma fișierelor: **`cyber-universe/docs/LIVE.md`**; semnarea: `tools/live-semneaza.py`. Partea 2 (P6-109: bucla `live <minute>` pe ramura `os/live`) urmează; abia apoi Release + PREDARE.

## Urmează
- P6-109 (C-159 pasul 1, partea 2) → Release + `PREDARE → centrul de comandă`.
- Apoi coada C-158: P3 când apare nota Cyber-GPU (C-155 punctul 1), #651 (punctul 3), mai multe teste într-o pornire (punctul 5).

## Ce oferă proiectul celorlalți
- `os-324`: dieta driverului în ciclu + blocul „viteza fata de os-322”. (`os-325`, dacă iese din CI, = `os-324` + poarta canalului viu, nimic nou pentru placă.)
- `docs/LIVE.md` + `tools/live-semneaza.py`: forma canalului viu, pentru capătul centrului de comandă (încă fără bucla din OS).
- `os-323`: tabloul de bord la cerere (`--tablou`, rânduri `kd`), `gpu stare`; ciclul cu viteza maximă, proba FLR la cerere, comutatorul de pornire, rândurile `discuri`, temperatura procesorului, ceasul de pază.
- Agentul din OS, ciclul automat, rapoartele urcate singure în hub.

## De ce are nevoie de la ceilalți
- Centrul de comandă: ciclul cu `os-324` (`test-placa`) și cifrele în hub (blocul „viteza fata de os-322”, rândurile `kt` noi, cele 16 simboluri).
- Cyber-GPU: nota P3 (C-155 punctul 1) — următorul Release pentru placă.
- Cyber-GPU: dacă placa refuză pornirea tabloului (clientul nostru, nu cel intern), varianta cu mânerele interne (doar cu „da”-ul lui Adrian).

## Blocaje / nevoie de Adrian
- Nimic urgent; testele le pornește centrul de comandă (`os-324`, `test-placa`).
- Comutatorul de pornire (P6-102) contează pe workstation doar după ce stick-ul e primul în ordinea de pornire din BIOS — o singură schimbare, cu tine de față.
