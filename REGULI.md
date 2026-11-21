# Reguli pentru agenți — Cyber Hub

Acest repo e **centrul comun de comandă** al proiectelor lui Adrian. Fiecare agent (sesiune Claude / Claude Code) care lucrează
la un proiect conectat îl folosește ca să știe ce fac ceilalți, să primească comenzile lui Adrian și să propună colaborări.
Adrian e român și nu programează: tot ce scrii aici e în **română simplă**.

## Proiecte conectate (ID-uri)
| ID | Proiect | Fișier de stare |
|---|---|---|
| `kronos` | Kronos / Cyberspace (AI propriu) | `stare/kronos.md` |
| `cyber-universe` | Cyber Universe OS | `stare/cyber-universe.md` |
| `suita-office` | Suita de aplicații office | `stare/suita-office.md` |

Un proiect nou se adaugă doar de Adrian sau la cererea lui (rând nou aici + în `PROIECTE.md` + `RESURSE.md` + fișier de stare).

## Fișierele comune (cine scrie ce)
| Fișier | Ce e | Cine scrie |
|---|---|---|
| `PANOU.md` | Ecranul lui Adrian: unde e fiecare proiect și ce așteaptă de la el | doar coordonatorul și centrul de comandă |
| `COMENZI.md` | Comenzile lui Adrian către proiecte | centrul de comandă scrie comenzile; fiecare agent schimbă doar `stare` și `rezultat` la comenzile lui |
| `RESURSE.md` | Ce calculator / placă / fereastră orară aparține fiecărui proiect + rezervări | centrul de comandă (rezervările doar cu „da”-ul lui Adrian) |
| `DECIZII.md` | Deciziile lui Adrian valabile pentru toate proiectele | centrul de comandă (doar ce a spus Adrian) |
| `in-lucru/<ID>.md` | Semnul „în lucru”: un rând care spune dacă o sesiune a proiectului lucrează acum (vezi „Lucrul continuu”) | doar agentul proiectului |
| `stare/<ID>.md`, `jurnal/<ID>.md` | Starea și istoricul fiecărui proiect | doar agentul proiectului |
| `idei/` | Propuneri de colaborare | oricine propune; doar Adrian aprobă |
| `rezumate/` | Rezumatele coordonatorului | coordonatorul |

**Centrul de comandă** = chatul în care Adrian vorbește cu Claude despre toate proiectele. El transformă ce spune Adrian
în comenzi, decizii și rezervări scrise aici, cu data. Nu scrie cod și nu modifică repo-urile proiectelor.

## La ÎNCEPUTUL sesiunii (citire, ~1 minut)
1. `git pull` în clona hub-ului (sau clonează: `https://github.com/Adriancu91/Cyber-hub`).
2. Citește în `COMENZI.md` comenzile pentru proiectul tău cu starea `nou`.
3. Citește `DECIZII.md` și `RESURSE.md` (ce resurse sunt ale tale și dacă ai vreo rezervare).
4. Citește `PROIECTE.md` și **stările celorlalte proiecte** din `stare/`.
5. Citește standardele aprobate din `standarde/` (de respectat de toate proiectele).
6. Citește în `idei/` propunerile cu starea `propus` sau `aprobat` care îți numesc proiectul.
7. Folosește ce afli din stările celorlalți doar ca **context**. Nu schimbi planul proiectului tău pe baza hub-ului fără
   aprobarea lui Adrian, cu excepția propunerilor marcate `aprobat` și a comenzilor din `COMENZI.md` pentru proiectul tău.

## Comenzile (`COMENZI.md`)
- O comandă pentru proiectul tău **e „da”-ul lui Adrian pentru exact ce scrie în ea**, nici mai mult, nici mai puțin.
- O preiei în planul tău obișnuit (coadă, listă de sarcini), **după ce termini ce ai în lucru acum**. Nu întrerupi un
  antrenament, un test sau o sarcină pornită ca să faci o comandă, decât dacă comanda spune explicit „oprește acum”.
- Când o preiei: `stare: preluat (AAAA-LL-ZZ HH:MM, <cine>)` + unde ai pus-o (de ex. „S9 în plan/coada.md”).
- Când e făcută: `stare: gata` + `rezultat:` într-o propoziție. Dacă nu se poate: `stare: blocat` + de ce.
- Dacă o comandă ar încălca regulile de siguranță ale proiectului tău (paznic, limite de memorie/temperatură, examenul,
  reguli legale) sau e neclară: `stare: întrebare` + întrebarea ta într-o propoziție. Nu o faci până nu răspunde Adrian.
- Nu atingi comenzile altor proiecte.

## Resursele (`RESURSE.md`)
- Folosești doar calculatoarele / plăcile / ferestrele orare trecute la proiectul tău.
- Dacă ai nevoie de resursa altui proiect: scrii o cerere de rezervare în „Discuție” într-o propunere din `idei/` sau în
  starea ta, la „De ce are nevoie de la ceilalți”. Rezervarea devine valabilă doar când apare în `RESURSE.md` cu „da”-ul lui Adrian.

## La SFÂRȘITUL sesiunii (scriere, ~2 minute)
1. **Rescrie complet** fișierul tău de stare `stare/<ID>.md` după șablonul din `stare/_SABLON.md` (max ~40 de rânduri).
   La „Blocaje / nevoie de Adrian” scrii **tot** ce aștepți de la el, ca să apară pe `PANOU.md`.
2. **Adaugă** 1–3 rânduri la finalul `jurnal/<ID>.md`: `- AAAA-LL-ZZ HH:MM — ce s-a făcut (o propoziție)`. Nu șterge nimic din jurnal.
3. Actualizează comenzile tale din `COMENZI.md` (vezi mai sus).
4. Dacă ai o idee care leagă proiectul tău de altul: creează `idei/AAAA-LL-ZZ-<scurt>.md` după `idei/_SABLON.md`.
   Dacă ai ceva de spus la o propunere existentă: adaugă un rând la secțiunea „Discuție” a ei.
5. Commit (mesaj: `<ID>: stare AAAA-LL-ZZ`) și push. Dacă push-ul e refuzat: `git pull --rebase` și reîncearcă (max 3 ori).

## Lucrul continuu (decizia lui Adrian, 21 nov 2026 08:01) — pentru `cyber-gpu` și `cyber-universe`
Scopul: nimeni nu așteaptă degeaba și nimeni nu calcă pe altul.
1. **Sesiuni din oră în oră, una singură pe proiect.** La pornire citești `in-lucru/<ID>.md`. Dacă scrie `ocupat` și începutul e mai nou de 3 ore, altă sesiune a proiectului tău lucrează: ieși imediat, fără niciun commit. Altfel scrii acolo `ocupat · început AAAA-LL-ZZ HH:MM · sarcina: … · estimat gata: HH:MM`, commit + push, apoi lucrezi. La sfârșit, în commit-ul de stare: `liber · terminat AAAA-LL-ZZ HH:MM · următorul pas: …`. Ora României: `TZ=Europe/Bucharest date`.
2. **Coada permanentă.** Fiecare proiect are în `COMENZI.md` o comandă-coadă (C-157 `cyber-gpu`, C-158 `cyber-universe`), cu puncte în ordine. Cât timp are puncte nefăcute, ai de lucru: oprirea „trei sesiuni fără sarcină terminată” nu se aplică unei sesiuni care are coadă. Centrul de comandă adaugă puncte; tu scrii ce ai făcut la `rezultat`.
3. **Predarea directă.** Când termini ceva de care are nevoie alt proiect, scrii în starea ta, la „Ce oferă proiectul celorlalți”, un rând care începe cu `PREDARE → <ID>:` (ce e, unde e nota, commit-ul, și ce e nou pentru placă: „nimic” sau ce anume). Proiectul care primește o ia la prima lui trecere, fără o comandă nouă, dacă intră într-un punct din coada lui.
3b. **Sistemul face întâi ce merge pe placă** (Adrian, 21 nov 14:23): o sesiune `cyber-universe` care găsește un `PREDARE → cyber-universe` nelegat îl leagă întâi într-un Release mic, apoi lucrează la uneltele lungi. Sesiunile OS pornesc la :10 și la :40.
4. **Un singur lucru nou pe Release și pe test.** Când un Release pentru placă e gata (CI verde), sesiunea OS scrie în starea ei un rând `GATA DE TEST: os-NNN — ce e nou, rândul pentru teste.txt, ce cifre aștept`. Nu aștepți rezultatul: treci la punctul următor din coadă.
5. **Placa: un singur test o dată, la orice oră.** Doar centrul de comandă pune versiunea pe stick și dă semnalul; ordinea e în `RESURSE.md`, „Coada testelor pe placă”. Rezultatele apar în `rezultate/` și, pe scurt, la comanda ta.
6. **O trecere fără nimic de făcut iese fără commit** (nici stare, nici jurnal), cu mesajul „Nimic nou.”. Nu se numără ca sesiune.
7. **Ce rămâne cu „da” separat al lui Adrian** (`DECIZII.md`, 21 nov 08:01): scrieri pe discurile workstation-ului, lucruri noi trimise la placă în afara pachetelor aprobate, lanțul pe placă (P7), circuitele speciale pe placă (P8), BIOS-ul. Pentru acestea pregătești (cod oprit implicit, SIMULARE, QEMU), scrii „aștept da” în stare și treci la punctul următor — nu te oprești.
8. **Întrebări și blocaje:** `stare: întrebare` / `blocat` la comandă + un rând în starea ta. Centrul de comandă citește hub-ul din oră în oră ziua și la două ore noaptea și răspunde acolo.

## Ce NU ai voie
- Să scrii în fișierul de stare sau în jurnalul altui proiect, ori în `PANOU.md`, `RESURSE.md`, `DECIZII.md`.
- Să modifici **codul sau repo-ul altui proiect**. Colaborarea se face doar prin propuneri în `idei/` și comenzi aprobate.
- Să oprești sau să încurci munca altui proiect (să-i ocupi placa, calculatorul sau fereastra orară).
- Să marchezi o propunere `aprobat`. **Doar Adrian aprobă** (sau coordonatorul / centrul de comandă, scriind explicit
  „aprobat de Adrian în chat, data …”).
- Să pui în hub: parole, chei API, date personale, date de business ale firmei (clienți, prețuri, facturi).
- Să rescrii istoria git (`push --force` interzis).

## Stările unei propuneri (`idei/`)
`propus` → (Adrian) `aprobat` / `respins` / `amânat` → (agenții implicați) `în lucru` → `gata`.

## Coordonatorul
O sesiune automată citește tot hub-ul, rescrie `PANOU.md`, scrie `rezumate/AAAA-LL-ZZ.md` și îi trimite lui Adrian
un rezumat scurt: ce s-a mișcat în fiecare proiect, ce așteaptă decizia lui, ce comenzi sunt blocate sau cu întrebări,
ce legături între proiecte merită făcute. Coordonatorul nu modifică stările proiectelor și nu scrie cod.
