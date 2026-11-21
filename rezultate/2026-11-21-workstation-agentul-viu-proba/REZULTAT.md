# Rezultat: proba agentului viu pe workstation (C-159 pasul 1, os-328) — 21 nov 2026, 13:03–13:26

- **Unde:** workstation, ciclul automat (`auto\teste.txt` cu `live 10`, apoi `live 2`), fără om de față. **Placa video neatinsă** (fără `permite-live-placa`).
- **Versiunea:** `os-328` (`13582db`). Capătul centrului de comandă: `unelte/live/live.py` + `sesiune.py` (cheia NU e în hub: pe stick și în `C:\Kronos\cyber-test\live.cheie`).
- **Fișierele brute:** ramura `os/live`, `live/s-20261121-1303/` și `live/s-20261121-1318/` (toate `c-` și `r-`); aici: rapoartele centrului de comandă și jurnalele de pe stick ale celor două sesiuni.

## Cifrele
| | Sesiunea A (`live 10`, încheiată cu `gata`) | Sesiunea B (`live 2`, încheiată la timp) | Total |
|---|---|---|---|
| comenzi trimise și răspunse | 35 | 26 (+1 trimisă după sfârșit) | **61** |
| executate | 24 | 21 | **45** |
| refuzate (cum trebuia) | 11 | 5 | **16** |
| ecou identic octet cu octet | 35 / 35 | 26 / 26 | **61 / 61** |
| abateri (greșită, repetată, sărită, în altă ordine) | 0 | 0 | **0** |
- **O singură dată, în ordine:** jurnalele de pe stick arată fiecare număr o singură dată, în ordinea 1…35 și 1…26; niciun număr refuzat nu a fost și executat. Fișierele `c-` de pe stick sunt identice cu cele trimise.
- **Lot:** 10 comenzi puse deodată (un singur commit) au fost luate în ordine, câte una la ~2,5 s.
- **Ecoul la semne grele:** diacritice, ghilimele, `\`, scriere chineză, emoji, forma `\uXXXX`, rând nou la sfârșit, JSON așezat altfel, text de 3 000 de semne — toate întoarse exact.
- **Probele de refuz, toate trecute:** semnătură greșită (zerouri ×2, altă cheie ×1), număr greșit ×2, comandă repetată ×2, comenzi pe placă fără cheie ×5 (`gpu lant`, `test-placa`, `run kronos --gpu …`, `gpu i6 --scrie`, `timp gpu recupereaza`), altă sesiune, fișier care nu e JSON, `live` din modul viu, fel de la pasul 2 (`clic`).
- **Sfârșitul:** `gata` → Windows înapoi în ~2 minute; fără comenzi → sesiunea s-a închis singură la 2 minute (13:23:41) și Windows a revenit; comanda trimisă după sfârșit (`c-0027`) nu a fost luată și nu are răspuns.
- **Viteza:** ~8,8 s pe comandă trimisă una câte una (din care ~3 s urcarea prin git de la centrul de comandă); ~2,5 s în lot.
- Niciun răspuns nu conține cheia vie sau token-ul.

## Verdict față de condițiile din DECIZII.md (21 nov 08:31)
1. Teste QEMU / CI verzi — **da**.
2. Două sesiuni doar cu citiri, fiecare comandă o singură dată, în ordine, ecou identic, zero abateri — **da**; numărătoarea strictă „50 executate” e la **45** (61 cu refuzurile) → se completează la proba de după reparație.
3. Probele de refuz — **da**.
4. Sfârșit curat la `gata` și la timp — **da**.

**Cheia `permite-live-placa` NU se pune încă.** Motiv: `live.cheie` nu e fișier secret pentru OS (`cat /usb/hub/live.cheie` prin canal ar scrie cheia în hub) — găsit la citirea codului, nu încercat pe workstation. După reparație (C-159, nota de la 13:00): o sesiune C scurtă (≥ 10 citiri + proba „cheia nu se arată”, cu o cheie de aruncat), apoi cheia pentru placă și anunțul către Adrian.

## Observații pentru sesiunea OS
- Scrierea prin API-ul GitHub e oprită de proxy la centrul de comandă; comenzile urcă prin `git push` pe `os/live` (merge; fără ciocniri în 61 de comenzi).
- `ecran` poartă rânduri de felul „drepturi: gh-trimite a cerut /usb/github.token” — fără secret în ele, dar la pasul 2 textul ecranului adevărat ar fi mai util.
- `durata_ms` e 0 la aproape toate citirile (ceasul are pas de 1 ms; în regulă).

## Sesiunea C (os-329, 16:03–16:07) — după reparația „live.cheie = fișier secret” (P6-113)
- Cheie nouă de probă (64 de semne), pusă pe stick doar pentru această sesiune și păstrată apoi (nu s-a scurs).
- **27 de comenzi: 25 executate, 2 refuzate, ecou identic 27 / 27, zero abateri**; jurnalul de pe stick: ordinea 1…27, fiecare o singură dată.
- **Cheia nu se arată** — 7 încercări, toate oprite: `cat /usb/hub/live.cheie`, cu litere mari, pe căi ocolite (`../hub/./`, prin subdosar), `compara` cu cheia, `cat /usb/hub/permite-live-placa` → „fisier secret”; numele scurt `LIVE~1.CHE` → „nu exista”. Niciun răspuns nu conține cheia, nici ca text, nici ca hex. Suma SHA-256 a modelului #651 (un șir care seamănă cu o cheie) a rămas vizibilă — filtrul nu ascunde ce nu trebuie.
- `gpu lant` fără cheia plăcii și semnătura greșită: refuzate.

## Totalul celor trei sesiuni și verdictul final
| | A | B | C | **Total** |
|---|---|---|---|---|
| comenzi trimise și răspunse | 35 | 26 | 27 | **88** |
| executate (o singură dată, în ordine) | 24 | 21 | 25 | **70** |
| refuzate, cum trebuia | 11 | 5 | 2 | **18** |
| abateri | 0 | 0 | 0 | **0** |
Condițiile din `DECIZII.md` (21 nov 08:31): 1 — da; 2 — da (70 executate ≥ 50); 3 — da; 4 — da. Reparația cerută la 13:00 — făcută și dovedită.
**Cheia `E:\hub\permite-live-placa` a fost pusă pe stick la 16:12 (21 nov 2026).** De acum centrul de comandă poate trimite și comenzi pe placă din modul viu; prima folosire = un test separat, anunțat lui Adrian. P7 / P8 rămân cu „da” separat.
