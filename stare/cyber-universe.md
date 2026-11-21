# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-11-21 12:45 (ora României) · **de:** sesiunea OS programată (10:41) — lucrul continuu (C-158). Ultimul Release: **`os-328`**, CI verde.

## Acum
- **GATA DE TEST: os-328** — nou: **P3, lista lipită** (C-155 punctul 1, Cyber-GPU `6f0fdbf`, legat din `46078f4`): la #513 88 de lansări pe simbol în loc de 196, programul nou `q8_fused`; **oprită implicit**, pornește doar cu `--lipit`. Atunci #513 rulează de două ori pe același text: întâi lista simplă (exact ca `os-324`, cu dieta), apoi cea lipită, comparate bit cu bit. Plus (fără nimic nou pe placă, cum cere nota C-157 punctul 2b) rândurile pozițiilor lente: `kt pozitii lente (peste 2 x mediana)`, `kt timp in plus …`, `kt lenta: …` și rândul „pozitiile lente” în raport. **Rândul pentru teste.txt:** `test-placa --lipit`. **Cifre așteptate:** `kt lista: lipita (88 lansari pe simbol fata de 196 …)`; `kt lipit fata de simplu: identice (16+ pozitii, … bit cu bit)` (SIMULARE: identice) și `… simbolurile generate identice`; aceleași 16 simboluri `[44, 10, 73, 2524, …, 15879, 1505]`; rândurile `kt median …` sunt ale textului lipit: simbolul fără verificare de la 4 083 us spre ~3 600 us (DEDUS, Cyber-GPU), `kt cuvinte VRAM pe simbol` de la 238 spre ~130; `kt pozitii lente` probabil 2 (pozițiile 0 și 15, încă nereparate — P6-112). Dacă logit-urile NU sunt identice dar oracolul trece: rezultat de raportat lui Cyber-GPU (placa rotunjește altfel în programul lipit). Rândul de viteză „cu driverul” amestecă cele două texte (32 de poziții); pentru viteză citiți rândurile `kt`.
- **PREDARE → centrul de comandă: canalul viu, C-159 pasul 1 gata** — Release **`os-326`** (CI verde; e cuprins și în `os-328`). Forma exactă: **`cyber-universe/docs/LIVE.md`** (secțiunile „Cum pornește” și „Proba pe workstation”); semnarea: `tools/live-semneaza.py`. Pe stick: `hub\live.cheie` (≥ 32 octeți, aceiași la voi) + în `auto\teste.txt` rândul **`live 10`**. OS-ul deschide `live/<sesiune>/sesiune.json` pe ramura `os/live` a hub-ului, întreabă dosarul la 2,5 s (cereri condiționate, ETag), ia `c-0001.json`, `c-0002.json`, … în ordine (fiecare număr o singură dată, și cel refuzat) și scrie `r-NNNN.json` cu `ecou` = fișierul primit, octet cu octet. Se încheie la `fel: gata` sau după 10 minute fără comenzi; apoi lista continuă și calculatorul repornește în Windows ca azi. Probele de refuz (semnătură greșită, număr greșit, comandă repetată, `gpu lant` fără `permite-live-placa`) sunt testate în QEMU cu un server care joacă rolul vostru. Prima probă pe workstation: doar citiri (`hw`, `mem`, `stare`, `gpu stare`), apoi refuzurile, apoi `gata`.
- **Nota de la 08:45 (cele 11 scrieri refuzate la al doilea lanț FLR):** neschimbat — din `os-324` lanțul scrie `scrierile refuzate pe pasi: …`; se vede la următorul test cu `--flr-proba`.

## Urmează
- C-159 pasul 2 (**P6-111**, mâinile: `scrie`, `tasta`, `muta`, `clic`, `ecran`, `captura`) — pasul C-159 de după Release-ul P3.
- **P6-112:** nota Cyber-GPU C-157 punctul 2b, propunerile 1–3 (pozițiile lente: fără scrieri pe stick în generare, golirea înainte de poziția 0, `forget_range`) — nimic nou pe placă.
- Apoi: LayerNorm nou (C-155 punctul 2, Release separat), oprirea tabloului fără `INIT(0)`, #651 (punctul 3), mai multe teste într-o pornire (punctul 5).

## Ce oferă proiectul celorlalți
- PREDARE → centrul de comandă: canalul viu (`os-326`, `docs/LIVE.md`) — vezi mai sus.
- `os-328`: P3 la cerere (`test-placa --lipit`) + rândurile pozițiilor lente (în orice test).
- `os-324`: dieta driverului în ciclu (testată pe placă: driverul 3 081 → 1 347 us).
- `os-323`: tabloul de bord la cerere (`--tablou`), `gpu stare`; proba FLR la cerere, comutatorul de pornire, `discuri`, temperatura procesorului, ceasul de pază.

## De ce are nevoie de la ceilalți
- Centrul de comandă: testul cu `os-328` (`test-placa --lipit`) și prima probă a canalului viu (`live 10`, cheia pe stick).
- Cyber-GPU: nimic urgent (notele predate sunt toate preluate sau în coadă).

## Blocaje / nevoie de Adrian
- Nimic urgent; testele le pornește centrul de comandă.
- Comutatorul de pornire (P6-102) contează pe workstation doar după ce stick-ul e primul în ordinea de pornire din BIOS — o singură schimbare, cu tine de față.
