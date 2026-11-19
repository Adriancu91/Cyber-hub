# Plan de performanță: Kronos pe placă, de la 44 la sute de simboluri pe secundă

- **Propus de:** centrul de comandă (la cererea lui Adrian, 19 nov 2026 21:54) · **Data:** 2026-11-19
- **Proiecte implicate:** `cyber-gpu`, `cyber-universe` (`kronos`: doar martor — „identic cu procesorul” rămâne proba)
- **Stare:** aprobat să înceapă (Adrian, 19 nov 2026 22:33) — vezi „Decizia lui Adrian” și Partea 6
- **Leagă:** `idei/2026-11-19_kronos-placa-mai-rapid.md` (etapa 1 de aici), `idei/2026-11-03_cyber-gpu-un-singur-bloc.md` (etapa 3 de aici, aprobată ca direcție pe 3 nov)

## Ideea (pe înțelesul lui Adrian)
Am citit ce au făcut alții care și-au scris driverul lor pentru plăci video și am comparat cu ce face driverul nostru azi.
Concluzia: câștigul mare nu stă în „funcții ascunse” ale plăcii, ci în **cum organizăm calculele** — exact bănuiala lui Adrian.
Azi un simbol al lui Kronos #513 înseamnă **196 de porniri mici** ale plăcii și folosim sub **1 %** din viteza memoriei ei.
Alții au aflat pe pielea lor două lucruri pe care noi încă nu le folosim: placa trebuie **rugată oficial să meargă la viteză maximă**,
iar calculele trebuie **lipite în porniri puține și mari**, pe care placa le înlănțuie singură.
Planul are 7 etape, fiecare cu un test pe placă care o dovedește sau o infirmă. Ținta: peste procesor (72,7 simb/s) după etapa 3, sute după etapa 5.

## Partea 1 — Ce au făcut alții (cercetare 19 nov 2026)

| Proiect | Ce au făcut | Unde au ajuns | Ce învățăm |
|---|---|---|---|
| **tinygrad** (tiny corp, firmă cu finanțare) | Driver propriu pentru plăci NVIDIA și AMD, care ocolește driverul fabricantului; rulează într-un sistem existent (Linux, macOS), nu într-un OS al lor | Singurii pe care i-am găsit care rulează modele AI pe NVIDIA cu driver propriu. Din 1 apr 2026 driverul lor e aprobat de Apple pentru plăci externe pe Mac. **Dar viteza** (măsurată de alții, apr 2026, RTX 3090): cu driverul lor 2,28 simb/s, față de 9,75 pe calea NVIDIA cu același motor și același model; la un model mare, 0,74 simb/s față de 109 simb/s cu motorul matur llama.cpp la un model din aceeași clasă | Driverul merge; **viteza lipsea din programele de calcul**: mii de porniri mici pe simbol (2 845), 1,2–1,6 % din viteza memoriei folosită, compilator tânăr (același Mesa NAK ca la noi) |
| **Nova** (NVIDIA + Red Hat) | Driver nou în Rust pentru Linux, pe același program intern al plăcii (GSP) ca noi | Început în 2025; în oct 2026 încă „nimic folosibil zi de zi”, „ani până la folosire reală” | Chiar cu oamenii NVIDIA, drumul e lung. Noi am trecut deja de pornirea GSP și de primul calcul |
| **Nouveau + NVK + NAK** (comunitate, Collabora) | Driver deschis pentru Linux + compilatorul NAK (cel pe care îl folosim noi ca unealtă) | Aproape de driverul NVIDIA în jocuri vechi, în urmă în cele noi. O singură linie schimbată în compilator a dublat viteza unui joc | Compilatorul e tânăr: **felul în care scriem programul contează mult** (bucle desfăcute, citiri mari) |
| **Haiku** (OS mic, comunitate) | A adus în OS-ul lor codul deschis al driverului NVIDIA (nu scris de la zero) | Peste un an de muncă; merge grafica 3D; **fără calcul AI** | Nici cu codul NVIDIA la îndemână nu e ușor |
| **LithOS** (universitatea CMU, 2025) | „Sistem de operare pentru placa video”: preia controlul asupra ordinii calculelor | Întârzieri de 13 ori mai mici când rulează mai multe programe; 25 % din placă și 25 % din curent economisite | Cine controlează **ordinea și împărțirea** calculelor câștigă mult, fără hardware nou |
| **Gdev** (universitate, 2012) | Placa video folosită direct de sistemul de operare, cu driver deschis | Sistemul de fișiere criptat de 2 ori mai rapid; memorie împărțită între programe | Ideea „placa e a OS-ului” e veche și dovedită — dar nimeni n-a dus-o la AI într-un OS propriu |
| **Asahi** (Apple M1, comunitate) | Driver grafic scris de la zero, fără documentație | Ani de muncă; a ajuns la certificare oficială, peste ce oferă Apple la OpenGL | Un driver scris de la zero poate ajunge la nivel de fabricant, cu răbdare |

**A mai ajuns cineva unde suntem noi?** Un model AI rulat pe o placă NVIDIA cu driver propriu: doar tinygrad, și ei înăuntrul Linux/macOS.
Într-un sistem de operare scris de la zero, cu driver propriu și AI propriu: **n-am găsit pe nimeni** (proiectele „bare metal” găsite rulează de fapt peste CUDA și peste un OS obișnuit). „N-am găsit” nu înseamnă „nu există”.

## Partea 2 — De ce mizează ei atât pe driver
1. **Independență.** Fără driverul fabricantului nu depinzi de CUDA și de ce îți dă voie NVIDIA (tinygrad; de aici și drumul lor pe Mac, unde NVIDIA nu mai are driver).
2. **Să poți vedea și repara.** tiny corp și-a oprit în 2024 calculatoarele cu plăci AMD pentru că driverul fabricantului se bloca și „n-aveau cum să vadă starea plăcii”; mai târziu și-au scris propriul driver și pentru AMD.
3. **Controlul ordinii calculelor** (LithOS, Gdev): cine hotărăște ce rulează, când și pe câtă placă.
4. **NVIDIA însăși** a mutat aproape tot driverul în programul intern semnat (GSP) și a deschis restul; Nova e pariul lor pe termen lung pentru Linux.

Ce **nu** am găsit la nimeni: viteză „ascunsă” în cip, deblocată de un driver propriu. Limitele adevărate sunt fizice (funcții arse din fabrică) sau semnate (programul intern nu poate fi modificat).
Exemplu pe chiar felul nostru de placă: seria RTX 30 (și 3070 Ti) a avut un limitator pentru minat pus de NVIDIA; din ce s-a relatat, ținea de driver și a dispărut cu driverul din octombrie 2022. El nu a atins niciodată calculele AI.

## Partea 3 — Cinci lucruri pe care ei le știu și noi nu le folosim încă

1. **Viteza maximă se cere.** tinygrad trimite la pornire comanda oficială `PERF_BOOST` („urcă la starea de performanță cea mai înaltă”, cu steagul de calcul), descrisă în fișierele publice NVIDIA 570.144 (`ctrl2080perf.h`, MIT). **Driverul nostru nu o trimite** (numele ei există doar într-un tabel). Nu știm în ce stare stă placa noastră în timpul calculelor — nimeni n-a citit-o.
2. **Lansările se leagă între ele pe placă.** tinygrad pune în fiecare lansare adresa următoarei (`dependent_qmd0`), iar placa o pornește singură. Câmpurile sunt deja în `nvidia-rm570::regs`; nu le folosim.
3. **Golirea memoriei rapide cerută chiar în lansare.** Șablonul de lansare al lui tinygrad are biții de golire în fiecare lansare (`invalidate_shader_data_cache`, `cwd_membar_type`) și `sm_global_caching_enable = 1` — lucru notat deja de Cyber-GPU în `docs/os-305_ANALIZA_I14.md`. Noi trimitem o comandă separată înaintea fiecăreia din cele 196 de lansări (reparația sigură din C-139) și nu punem acele câmpuri. Cu ele în lansare, lanțul de la punctul 2 n-ar mai avea nevoie de procesor între calcule.
4. **Porniri puține și mari.** Pe forumul NVIDIA, un inginer al lor spune că și cu driverul lor o pornire costă de obicei ~25 µs (5 µs în cel mai bun caz), iar sfatul de acolo e ca un calcul să țină 1–200 ms; motorul llama.cpp a câștigat 17–43 % din lipirea calculelor și reglaje de același fel; documentația NVIDIA dă pentru „CUDA Graphs” de 1,5–3 ori la multe calcule mici. La noi o lansare ține în medie 117 µs.
5. **Măsura corectă e „cât la sută din viteza memoriei folosești”.** tinygrad pe calea NVIDIA: 22 %; tinygrad cu driver propriu: 1,2–1,6 %; llama.cpp ajunge la ~80 % din plafonul calculat de autorii lui. **Noi: 0,8 %.**

## Partea 4 — Unde suntem noi, în cifre (MĂSURAT pe placă, `os-308`, 19 nov 14:37)

| Ce | Cifra | De unde |
|---|---|---|
| Timp pe simbol, cu tot | 86,8 ms (10,99 simb/s) | `kt` |
| din care jurnalul | 73,9 ms | `kt` (cauza: afișarea fiecărui rând, `cyber-gpu/docs/os-308_ANALIZA_KT.md`) |
| din care placa | 22,96 ms (43,8 simb/s) | `kv` |
| Lansări pe simbol | 196 (16 pe strat × 12 + 4) | `C-142` |
| Timp mediu pe lansare | 117 µs | 22,96 ms / 196 |
| Greutăți citite pe simbol | 110,8 MB | `kv urcare KiB` |
| Viteza memoriei folosită | 4,8 GB/s din 608 GB/s = **0,8 %** | calcul |
| Motorul rapid al OS-ului pe procesor | 72,7 simb/s | raportul ciclului |
| Plafon teoretic al plăcii (un singur răspuns) | ~0,18 ms pe simbol (~5 500 simb/s) | 110,8 MB / 608 GB/s; nu-l atinge nimeni |

Trei constatări:
- **Azi procesorul (72,7) bate placa (43,8)** la acest model. Placa trebuie să câștige clar, altfel driverul nu-și arată rostul.
- Din 16 lansări pe strat, **8 sunt mărunte** (adunarea unui termen, copieri, adunarea cu stratul dinainte). Lipite de calculul lor, rămân 7 pe strat: 196 → 87.
- La înmulțirile cu 768 de intrări lucrează **24 din cele 32 de fire** ale fiecărui grup (`q8_matvec.comp`: un fir pe bloc de 32, sunt 24 de blocuri).

**Ce NU știm (și de asta etapa 0):** cât din cele 117 µs pe lansare e cost fix al pornirii, cât e calcul și cât e placa mergând încet. Cele două extreme:
dacă e aproape tot cost fix, 87 de lansări ar da ~98 simb/s și 25 ar da ~340; dacă e aproape tot calcul la ceasuri joase, lipirea nu ajută, dar viteza maximă cerută ajută.

## Partea 5 — Planul

| Etapa | Ce se face | Cine | Câștig estimat (nemăsurat) | Cum dovedim |
|---|---|---|---|---|
| **0. Măsurare** | (a) timpul fiecărui fel de lansare, din mărcile de timp pe care placa le scrie deja; (b) costul unei lansări goale scris și în jurnal; (c) starea de performanță, ceasurile și temperatura — **doar citire** (`PERF_GET_CURRENT_PSTATE`, `PERF_GET_LEVEL_INFO_V2`), puse **la sfârșitul** testului; (d) o copiere mare VRAM → VRAM cu programul existent, ca să vedem viteza memoriei | cyber-gpu + OS | niciunul; ne spune unde e frâna | rânduri noi în jurnal; calculele neschimbate |
| **1. Jurnalul** | fără afișarea rândurilor de rutină; golire la 1–2 s și la final; pașii, verificările și **orice eroare se scriu imediat**; la blocare se golește întâi memoria | OS | 11 → ~40 simb/s | `kt`: jurnal sub ~2 ms pe simbol |
| **2. Viteza maximă cerută oficial** | `PERF_BOOST` la pornirea canalului, cu temperatura citită înainte și după și oprire peste un prag | cyber-gpu + OS | necunoscut: de la nimic la de câteva ori | starea citită înainte/după + timpul lansărilor |
| **3. Lansări puține** | 3a: lipirea celor mărunte (196 → 87); 3b: placa înlănțuie singură lansările, cu golirea memoriei rapide cerută în lansare (câmpurile de la Partea 3, punctul 3); 3c: ținta „un singur program” (direcția din 3 nov) | cyber-gpu + OS | până la ~100 simb/s (3a), ~300 (3b–3c), dacă frâna e costul pornirii | aceleași 16 simboluri, identice cu procesorul |
| **4. Programe de calcul mai bune** | toate cele 32 de fire, citiri de 128 de biți, vectorul de intrare ținut în memoria partajată; cursa pe placă a celor 6 variante de înmulțire deja compilate și niciodată rulate | cyber-gpu | 1,3–3 ori pe partea de calcul | abatere în toleranța de azi |
| **5. Generare fără drum la procesor** | alegerea simbolului pe placă; N simboluri pe o singură sonerie; procesorul citește 4 octeți în loc de 64 KiB; lansările ținute în RAM văzut direct de placă | cyber-gpu + OS | scoate ultimele așteptări dintre simboluri | text identic |
| **6. Loturi și model mai mare** | mai multe răspunsuri deodată; #651 (183 M) pe placă | toate trei | mii de simboluri/s în total; aici placa lasă procesorul mult în urmă | examenul lui Kronos rulat pe placă |

Țintele, toate **estimări** până le măsoară placa: după etapa 1 ~40; după 2 + 3 între 100 și 200; după 4 + 5 între 300 și 600 (un singur răspuns).

Despre partiția pe SSD (întrebarea lui Adrian) — **corectat pe 19 nov 22:40**: centrul de comandă spusese greșit că OS-ul nu are driver de SSD. Are: `ahci.rs` (SATA, citire și scriere), `nvme.rs` (NVMe, testat pe hardware real la citire pe 22 oct) și FAT32, cu regula că scrie doar pe partițiile marcate cu fișierul `cyber.rw`. Pentru viteza generării, după etapa 1 discul nu mai contează (jurnalul sub 2 ms pe simbol). Contează pentru încărcarea modelelor mari și ca să nu depindem de stick → firul S din Partea 6.

## Partea 6 — Planul de lucru v2: patru fire, două teste pe zi (aprobat să înceapă, 19 nov 22:33)

**Ritmul zilei** (cu programul de azi al sesiunilor; nimic nou de programat):

| Ora | Ce se întâmplă |
|---|---|
| 01:25 · 02:40 · 05:40 | sesiunile Cyber-GPU și OS de noapte scriu codul pachetului de dimineață → Release |
| 07:00 | Kronos eliberează placa |
| 07:30 | centrul de comandă: verifică Release-ul, îl pune pe stick, pornește **testul 1** (~08:15) |
| ~09:30 | cifrele testului 1 → comenzi / note pentru pachetul următor |
| 13:25 · 14:40 | sesiunile Cyber-GPU și OS de zi → Release |
| ~15:30–17:00 | **testul 2** |
| 17:30 | cifrele testului 2 → comenzi pentru sesiunile de noapte (19:25, 20:40, 23:40) |
| 19:00–07:00 | Kronos antrenează (umplutură) |

**Cele patru fire** (merg în paralel; pe placă intră câte un pachet pe test):

- **V — viteza pe placă:** etapele 0–5 din Partea 5.
- **T — circuitele speciale (tensor cores):** T0 unealta nouă de compilare; T1 primul program în simulare; T2 primul test pe placă; T3 folosirea la citirea întrebării și la loturi. Partea 7.
- **M — memoria:** M0 bugetul de memorie scris în jurnal la fiecare test; M1 Kronos cel mare (#651, 183 M) pe placă; M2 greutăți pe 4 biți; M3 RAM-ul ca prelungire aleasă de noi. Partea 8.
- **S — sistemul de operare:** S1 jurnalul (etapa 1); S2 verificarea după placă, cu motorul rapid; S3 discul propriu (partiție marcată `cyber.rw`); S4 resetul plăcii fără pornire rece (proba FLR din C-142, așteaptă DA); S5 convorbirea cu Kronos direct în OS, pe placă.

**Pachetele** (un pachet = un Release = un test pe placă; ordinea de după P2 se reașază după cifrele etapei 0):

| Pachet | Când (țintă) | Ce intră pe placă | „Da” |
|---|---|---|---|
| **P1** `os-309` | vin 20 nov, dimineața | etapa 0 (măsurători) + etapa 1 (jurnalul) + verificarea după placă | dat |
| **P2** | vin 20 nov, după-amiaza (sau sâm dimineața) | ce n-a încăput în P1 + M0 (bugetul de memorie) + inventarul discurilor (doar citire) | dat |
| **P3** | sâm–dum 21–22 nov | etapa 3a: calculele lipite, 196 → ~87 de lansări | dat (programe noi, aceeași probă) |
| **P4** | 22–23 nov | etapa 4: cursa variantelor de înmulțire, cea mai rapidă devine cea folosită | dat |
| **P5** | după cifrele P1 | etapa 2: viteza maximă cerută oficial | dat (19 nov 22:50), cu condițiile din C-147 |
| **P6** | ~24–25 nov | M1: Kronos #651 pe placă | dat (19 nov 22:50) → C-150 |
| **P7** | ~25–27 nov | etapa 3b: lanțul de lansări pe placă | **separat** |
| **P8** | ~26–28 nov | T2: primul calcul cu circuitele speciale | **separat** |
| **P9** | după P7 | etapa 5: generare fără drum la procesor | dat (programe noi) + ce cere P7 |
| **P10** | după P8–P9 | etapa 6 + T3: loturi, citirea întrebării cu circuitele speciale | după P8 |

Datele sunt ținte, nu promisiuni: fiecare pachet pleacă doar după ce cel dinainte a trecut pe placă cu aceleași simboluri ca procesorul. Dacă un pachet pică, următorul test e reparația lui, nu pachetul următor.

## Partea 7 — Circuitele speciale de calcul („tensor cores”) și compilatorul nostru

**Ce sunt.** Placa are două feluri de „muncitori”. Nucleele obișnuite fac o înmulțire și o adunare pe rând. Circuitele speciale înmulțesc dintr-o singură mișcare două tabele mici de numere (de exemplu 16 × 16), lucrând cu numere scurte, de 16 biți (sau întregi de 8 biți). NVIDIA dă pentru generația plăcii noastre de 8 ori mai mult calcul în modul lor de 32 de biți și de 16 ori în cel de 16 biți, față de nucleele obișnuite (cifre de pe placa lor de centru de date; plăcile de jocuri din aceeași generație, ca a noastră, au mai puține astfel de circuite — din câte știm, cam jumătate din aceste cifre; nemăsurat de noi).

**De ce nu le-am pus în prima variantă a planului.** Ca să le folosești, programul trebuie să conțină o instrucțiune specială, iar compilatorul trebuie să știe s-o scrie. Am presupus că al nostru (Mesa NAK) nu știe. **Presupunerea era greșită:** NAK a primit acest suport (`VK_KHR_cooperative_matrix`) în Mesa 25.2, la mijlocul lui 2025, iar în noiembrie 2025 ajunsese la ~92 % din viteza driverului NVIDIA pe astfel de calcule. Unealta noastră e construită din Mesa 25.0.7 — cu o versiune prea veche. Deci circuitele sunt la îndemână: trebuie o unealtă nouă (T0 din C-147), cea veche rămânând pentru programele de azi.

**Unde ajută și unde nu.**
- La **un singur cuvânt generat** (matrice × vector) frâna e citirea greutăților din memorie, nu calculul: câștig mic. Un dezvoltator al driverului deschis spune același lucru despre motorul llama.cpp: la generare contează legarea și lipirea calculelor, la citirea întrebării contează înmulțirile de matrice.
- La **citirea întrebării** (toate cuvintele ei deodată), la **mai multe răspunsuri deodată** și mai ales la **antrenare**: aici sunt înmulțiri matrice × matrice și câștigul poate fi de câteva ori.

**Prețul.** Lucrează cu numere scurte, deci rezultatul nu mai e identic bit cu bit cu procesorul. Proba devine „același simbol ales + abatere sub un prag scris dinainte”. De aceea T2 e un test separat, cu „da” separat.

## Partea 8 — Putem câștiga și memorie, nu doar viteză?

Memorie fizică nu putem adăuga: placa are 8 GB lipiți pe ea. Dar cu driverul și OS-ul nostru câștigăm în patru feluri:

1. **Toată placa e a noastră.** Din 8 192 MiB, programul intern al plăcii ține ~190 MiB (zona citită pe placă: `0x1f4100000..0x1ffee0000`); restul de ~8 000 MiB e liber. Sub Windows, regula noastră pentru Kronos e „sub ~7 000 MB”. Câștig: **~1 GB**.
2. **Fără balast.** #513 ocupă pe placă 142 MiB cu tot cu memoria convorbirii; #651 (183 M) ~270 MiB (calcul, `VramBudget`). La rulare folosim sub 4 % din placă. Socoteală: la 8 biți pe greutate încap ~7 miliarde de parametri; la 4 biți ~14 miliarde.
3. **Împachetare mai strânsă (M2):** greutăți pe 4 biți în loc de 8 → model de două ori mai mare în aceeași memorie. Cere lucru la Kronos (formatul) și verificare pe examen (cât pierde din calitate).
4. **RAM-ul ca prelungire aleasă de noi (M3).** Placa poate citi direct din RAM-ul calculatorului (o facem deja la urcarea modelului): 128 GB pe workstation. Dar drumul e îngust: legătura plăcii duce cel mult ~15 GB/s (noi am măsurat 1,2), față de 608 GB/s înăuntrul plăcii. Bun pentru ce se citește rar (tabelul de simboluri: un rând pe simbol; convorbiri foarte lungi; date de antrenare), prost pentru greutățile citite la fiecare simbol. Windows face asta singur și orbește, iar când se întâmplă totul merge mult mai încet (de ~3 ori într-o măsurătoare publicată); la noi alegem noi ce stă unde.

**Unde e limita adevărată.** La rulare, memoria nu ne limitează: limitează cât de mare e modelul pe care apucăm să-l antrenăm. La antrenare (azi sub Windows) memoria contează mult mai tare; antrenarea pe driverul nostru e o etapă târzie (cere programele de învățare) și intră sub decizia din 13 nov („toate piesele la treabă”), după ce firele V și T își arată cifrele.

## Cost și riscuri
- **Lucru:** etapele 0 și 1 sunt mici (o zi, un test automat). Etapele 2–3a: câte una-două zile. 3b–5: o săptămână sau două la ritmul de acum. Fiecare etapă = o pereche de comenzi + un test în ciclul automat, ziua, 08:00–18:00.
- **Etapa 2 schimbă ce primește placa:** cere regula „trei surse” (avem două: documentația NVIDIA și tinygrad; a treia o caută Cyber-GPU) și „da”-ul separat al lui Adrian. Risc: placa mai caldă — de aceea citim temperatura și avem prag. Se poate și ca programul intern să refuze comanda; atunci aflăm din răspuns și rămânem ca azi.
- **Etapa 3b schimbă felul de trimitere** care a trecut I14 (C-139) și pune în lansare câmpuri pe care placa nu le-a primit încă de la noi (regula „trei surse”): diagnosticul existent („unde apare primul număr greșit”) rămâne pornit; dacă apar date vechi, ne întoarcem la felul de azi.
- **Compilatorul (Mesa NAK) e tânăr:** unele câștiguri din etapa 4 pot ieși mai mici decât la alții. Despre circuitele speciale pentru matrice („tensor cores”) vezi Partea 7: prima variantă a planului le lăsase pe dinafară dintr-o presupunere greșită.
- **Nimic din plan** nu scrie în registre necunoscute, nu atinge firmware-ul și nu schimbă Kronos. Antrenările de noapte nu sunt atinse.
- **Ce nu putem promite:** cifrele de după etapa 1 sunt estimări. Lecția tinygrad e că un driver propriu poate fi la început mult mai lent decât motoarele vechi; avantajul nostru e că reglăm totul pentru un singur model și o singură placă.

## Decizia lui Adrian
- **2026-11-19 22:33 — aprobat să înceapă** („Aprob începerea planului și fă un plan de lucru mai bun, mai progresiv, mai intens. Încearcă să aduci fiecare plus pentru ele.”) → C-147, C-148, C-149; `DECIZII.md`. Pe placă acum: etapele 0, 1 și programele de calcul noi. „Da” separat pentru: viteza maximă (P5), exportul #651 (P6), lanțul pe placă (P7), circuitele speciale (P8).
- **2026-11-19 22:50 — „Da, aprob tot”** la cele trei întrebări: viteza maximă (P5) poate intra în testul de după P1 dacă măsurătorile arată o stare joasă (condițiile la C-147); exportul #651 (P6) → C-150; sesiunile Cyber-GPU de la 4 la 8 pe zi. Rămân cu „da” separat: lanțul pe placă (P7) și circuitele speciale (P8).

## Discuție
- 2026-11-19 centrul de comandă: cercetare făcută în seara de 19 nov; cifrele noastre din `rezultate/2026-11-19-workstation-os308-automat/REZULTAT.md` și `rezultate/os-automat/2026-11-19/`. Codul tinygrad și fișierele NVIDIA au fost doar citite, ca specificație (MIT); nimic copiat.

## Surse
- Circuitele speciale în driverul deschis: https://www.phoronix.com/news/NVK-Cooperative-Matrix-Perf (17 nov 2025) · https://airlied.blogspot.com/2025/07/ramalamamesa-benchmarks-on-my-hardware.html (24 iul 2025) · cum se scriu în program: https://techoverflow.net/2026/09/29/vk-khr-cooperative-matrix-explained-tensor-core-math-in-glsl-shaders/
- NVIDIA, cât calculează circuitele speciale: https://developer.nvidia.com/blog/accelerating-ai-training-with-tf32-tensor-cores/
- Windows, memoria împărțită cu RAM-ul: https://discuss.pytorch.org/t/documented-fix-slow-execution-pytorch-using-gpu-shared-memory/218909
- tinygrad, driverul NVIDIA (`runtime/ops_nv.py`, ramura principală, citit 19 nov 2026): https://github.com/tinygrad/tinygrad
- tinygrad pe Mac — viteza măsurată și cauzele (14 apr 2026): https://www.lucebox.com/blog/egpu-myth
- Apple aprobă driverul tiny corp (8 apr 2026): https://macdailynews.com/2026/04/08/apple-approves-third-party-drivers-for-amd-and-nvidia-egpus-on-apple-silicon-macs/
- tinygrad, driverul AMD: https://docs.tinygrad.org/developer/am/ · oprirea din 2024: https://www.tomshardware.com/pc-components/gpus/amd-tinybox-project-put-on-hold-due-to-gpu-instability-in-ai-workloads-firm-publicly-considering-using-intel-gpus
- NVIDIA, comenzile de performanță (570.144, MIT): https://github.com/NVIDIA/open-gpu-kernel-modules/blob/570.144/src/common/sdk/nvidia/inc/ctrl/ctrl2080/ctrl2080perf.h
- Nova, starea în oct 2026: https://clearpathsolutionsllc.org/blog/linux/releases/nvidia-nova-driver-progressing-linux-years-use/ · Linux 7.3: https://www.opensourceforu.com/2026/08/nvidia-nova-driver-gains-linux-7-3-support/
- NVK față de driverul NVIDIA (18 iul 2026): https://phoronix.com/news/NVK-Mesa-26.2-Performance · linia care a dublat viteza: https://mail.phoronix.com/news/NVK-NAK-Loop-Unrolling
- Nouveau, gestionarea puterii prin GSP: https://nouveau.freedesktop.org/PowerManagement.html
- Haiku (12 iul 2026): https://hackaday.com/2026/07/12/porting-the-nvidia-gpu-driver-to-haiku-for-3d-acceleration/
- LithOS (SOSP 2025): https://arxiv.org/abs/2504.15465 · https://www.cs.cmu.edu/~csd-phd-blog/2025/lithos/
- Gdev (USENIX ATC 2012): https://www.usenix.org/conference/atc12/technical-sessions/presentation/kato
- Asahi, certificarea OpenGL 4.6 (feb 2024): https://appleinsider.com/articles/24/02/14/asahi-linux-conformant-to-opengl-46-opengl-es-32-on-apple-silicon-macs
- NVIDIA, costul unei porniri: https://forums.developer.nvidia.com/t/launch-of-many-small-kernels-10x-slower-compared-to-one-kernel/350194 · CUDA Graphs: https://docs.nvidia.com/dl-cuda-graph/cuda-graph-basics/quantitative-benefits.html
- llama.cpp, lipirea calculelor: https://github.com/ggml-org/llama.cpp/discussions/17621
- Limitatorul de minat de pe seria RTX 30 (13 oct 2022): https://www.tomshardware.com/news/nvidia-restores-mining-performance-on-geforce-rtx-30-lhr-gpus
