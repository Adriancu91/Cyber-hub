# Revizie tehnică Kronos (doar citire) — 13 noiembrie 2026

*Scrisă de un agent de revizie (Claude Fable), 13 nov 2026, ~16:15–17:10 ora României. N-am schimbat, n-am urcat și n-am
șters nimic în niciun depozit; n-am rulat nimic pe placă. Am citit codul (`kronos/`, `module/`, `unelte/`), configurările,
coada (`plan/coada.md`, S77–S112), rapoartele S31–S109 și hub-ul (C-85, C-88, C-89, C-101, C-110, C-119, DECIZII). Am rulat
cinci verificări mici pe procesor, într-un dosar separat (secțiunea 7). Starea citită: `cyberspace` la `59a2d34` + raportul
S109 (`4631e52`, citit de pe GitHub), `cyber-hub` la `db98f87`.*

Etichete: **CONFIRMAT** = am urmărit codul sau am măsurat eu / ați măsurat voi; **PROBABIL** = rezultă din cifrele voastre,
dar nu există o măsurătoare directă; **DE VERIFICAT** = bănuială, nemăsurată.

---

## Pe scurt (pentru Adrian)

1. **Modelul mare ar porni „cu stângul”.** Așa cum e scrisă sarcina S110, rețeaua de 24 de straturi pornește cu o greșeală
   veche de pornire (am măsurat-o: „pierderea” de început e **411** în loc de **~9,7**). Voi ați găsit și reparat exact asta
   la Kronos-Cod (S61), dar reparația nu e pusă în rețeta S110. Se repară dintr-un rând de configurare; am verificat că merge.
2. **Regulile de oprire de la 12 h și 24 h pot opri o rulare sănătoasă.** La 24 h modelul încă învață „cu viteza maximă”
   și arată mult mai slab decât va fi la final. După cifrele voastre vechi, un model bun poate avea 1,40–1,58 la 24 h, iar
   regula zice „peste 1,40 → oprire”. Ar rămâne ~30 de ore de placă nefolosite și niciun model nou.
3. **Se poate citi cu 20–35 % mai mult text în aceleași 54 de ore**, fără cod nou: lot 6 × 16 în loc de 4 × 24 (măsurat de
   voi de două ori, dar citit greșit în raportul S86), fără examenele de engleză date la fiecare oră și fără „hrana” englezească.
4. **Doar o treime din ce citește Kronos e română** (46 % e engleză simplă, 15 % cod, 5 % numere). Pe disc stau nefolosiți
   ~2,45 GB de text românesc curat, deja descărcat (FineWeb-2). Pentru ținta „vorbește fluent românește” asta e cea mai mare
   pierdere dintre toate — dar schimbarea amestecului e decizia ta (C-119 spune „pe amestecul actual”).
5. **Luni seara, „convorbirea” nu va arăta a convorbire dacă interfața rămâne cum e.** Fila de chat doar continuă textul
   scris de tine, la întâmplare, exact 200 de litere. Iar în forma învățată („Întrebare/Răspuns”), fără un text alături,
   modelul răspunde „Nu scrie în text.” la ~80 % din întrebări (S105: 63 din 80), fiindcă 99 % din perechile de antrenare au
   text alături. O parte se repară fără antrenare (căutare + citire, deja măsurată la voi: 67 % corecte), o parte la S111.

Restul codului de antrenare l-am găsit **corect**: Muon e pus doar pe matricile din straturi, programul ratei continuă bine
după reluare, măștile, salvarea și reluarea sunt în regulă, paza tokenizerului și a datelor funcționează.

---

## Lista CRITICĂ pentru S110 (de rezolvat înainte de rularea mare; proba de rată + pre-înregistrarea vin în ~1–2 ore)

| # | ce | stare | leacul (fără cod nou în `kronos/` sau `module/`) |
|---|---|---|---|
| C1 | Pornirea: încorporările N(0,1) legate de ieșire → pierdere de pornire ~411, modelul „copiază” simbolul de intrare | **CONFIRMAT** (măsurat) | în `conv_w2_mare_24z.toml`: `modul = "module.model_gpt_cod:ModelGPTCod"` + `abatere_incorporari = 0.02` |
| C2 | Pragul de la 24 h („română > 1,40 → oprire”) și cel de la 12 h (1,60) sunt sub ce poate avea un model sănătos nerăcit | **PROBABIL** (din W2, S31, S99) | praguri pe tendință + limite largi (1,90 / 1,70), scrise înainte de pre-înregistrare (§1.2) |
| C3 | „Pierderea a crescut 3 ore la rând” — pierderea orară din jurnal e a unui singur lot de 4 ferestre (zgomot) | **CONFIRMAT** (cod) | regula se aplică pe româna orară (examen), nu pe `pierdere_finala` |
| C4 | Testul `test_doar_in_configurarile_aprobate` pică pentru orice configurare nouă cu examenul de română; S110/S111 nu spun că are voie să-l completeze | **CONFIRMAT** (cod) | un rând în sarcină: „adaugi `conv_w2_mare_24z`, `24zc` și configurările de probă în lista din test” |
| C5 | Sub 40 GB liberi pe C: pică un test (`test_kronos_cod_tokenizer…cap_coada`) → după ~ora 43–44 din S110 „toate testele trec” nu mai e adevărat → S111 se poate bloca | **CONFIRMAT** (cod + S77c) | scris dinainte: „testul acesta, sub 40 GB, e cunoscut și nu oprește S110/S111” |
| C6 | Proba de rată de 30 min (≈480 de pași de optimizator) cu pornirea implicită măsoară cât de repede se repară pornirea, nu rata bună | **CONFIRMAT** (cod) + PROBABIL | întâi C1; proba cu același lot ca rularea mare |
| E1 | Lot 4 × 24 e cel mai LENT dintre cele măsurate: 12,4–13,1 mii simb/s față de 14,9–15,7 mii la 6 × 16 | **CONFIRMAT** (S77c, S86) | `lot = 6`, `adunare_loturi = 16` (+20 %) |
| E2 | La fiecare oră: ~3 min de examene de engleză + profesorul Qwen încărcat pe placă (vârful de 6,3–6,5 GB vine de aici) | **CONFIRMAT** (S86, S87, cod) | `examene_suplimentare = []`, `hrana = ""`, `--pauza 5` |

Dacă se face doar un lucru: **C1 + C2**. Dacă se fac două: + **E1**.

---

## 1. Probleme critice pentru S110, pe larg

### 1.1 Pornirea rețelei (C1) — CONFIRMAT

- `module/model_gpt.py:105–110`: `nn.Embedding` pornește din N(0,1), iar capul de ieșire e legat de intrare
  (`self.cap.weight = self.emb_token.weight`). La 768 de dimensiuni asta dă logit-uri cu abaterea ~28 și un model care, la
  pornire, „prezice” că simbolul următor e chiar cel de acum.
- Am construit rețeaua adevărată (`_GPT(16384, 24, 12, 768, 512)`, 183.086.592 parametri, sămânța 24) pe procesor:

  | pornirea | pierderea de început | abaterea logit-urilor | argmax = simbolul de intrare |
  |---|---|---|---|
  | implicită (cum ar porni S110) | **410,76** | 27,9 | 100 % |
  | încorporări 0,02 (ca GPT-2) | **9,86** (ln 16.384 = 9,70) | 0,55 | 0 % |

- Voi ați măsurat același lucru pe placă la S61 (`docs/rapoarte/2026-11-01_0006_S61_init_cod.md`): 473,9 → 10,67 la primul
  lot, iar după 10 minute (398 de pași de optimizator) **6,82 față de 3,77**. Reparația există: `module/model_gpt_cod.py:48–65`
  (`abatere_incorporari`), dar numai în clasa `ModelGPTCod`. S110 (`plan/coada.md:3743`) cere „copie a `conv_w2_mare_24n.toml`
  cu DOAR…”, iar acolo e `module.model_muon:ModelGPTConversatieMuon` (`config/conv_w2_mare_24n.toml:26`), care nu are setarea.
- Cât costă: la S61, pe mărimea reală cu AdamW, după 398 de pași de optimizator pierderea era 6,82 față de 3,77. În proba mea
  mică făcută cu rețeta S110 (Muon 0,02 pe matrici + AdamW 0,0006 pe rest, gradient adunat; §7, D) modelul cu pornirea
  implicită ajunge sub pierderea 5,0 la pasul **191 față de 77**, iar la pasul 600 e la **3,39 față de 2,72** — adică acolo
  unde modelul pornit corect fusese pe la pasul ~250. Încorporările nu se repară singure: după 600 de pași abaterea lor e
  încă 0,96 (față de 0,045); straturile învață „în jurul” lor.
- De ce contează tocmai aici: linia W2 de 12 straturi a pornit la fel și a trecut repede de zona asta, pentru că făcea
  ~21.000 de pași de optimizator pe oră. S110 face **~930 pe oră** (gradient adunat pe 24 de loturi), deci primele ore
  sunt cele lovite, iar proba de rată (480 de pași) cade toată în zona stricată. Nu e fatal — W2 a trăit cu pornirea asta
  și a ajuns la 1,21 — dar cât din handicap rămâne până la pasul 50.000 nu știu, iar leacul e gratuit.
- Leacul, verificat pe procesor (§7, B): `ModelGPTCod` cu `abatere_incorporari = 0.02` merge pe exact drumul S110
  (DateBucati + conversație + Muon + gradient adunat + programul ratei + reluarea din `cale_stare` + recalculul din
  `antrenare_recalcul.py`, care se moștenește). La reluare greutățile sunt cele salvate, nu se repornesc. Modelul salvat se
  încarcă și cu clasa veche; `unelte/modele_salvate.py:25–31` ia clasa din fișa din jurnal, deci examenele și interfața merg.
  `ModelGPTCod` e deja în `teste_contracte/`.

### 1.2 Pragurile de la 12 h și 24 h (C2) — PROBABIL

Textul (`plan/coada.md:3747–3749`): oprire la 12 h dacă româna > 1,60; la 24 h dacă româna > 1,40 sau câștig < 0,01.
Programul ratei (verificat, §7 C): încălzire 2,7 min → **rata la vârf până la ora 40,5** → scădere liniară la 0 până la 54 h.
Deci la 12 h și 24 h modelul e „nerăcit”. Cât costă asta, din cifrele voastre:

- W2 (12 straturi, de la zero, același amestec), ora 10 = 1,3 mld. simboluri: povești nerăcit 0,5308, după 30 min de răcire
  0,4668 (**−12 %**); româna răcită 1,3775 (`docs/preinregistrari/2026-10-13_noaptea4_w2.md`). Româna nerăcită n-a fost
  măsurată; cu același raport ar fi ~1,55–1,60 la ora 10 și ~1,65 la ora 4–5.
- Muon nerăcit: S31 ora 1 (Muon 0,01) povești 0,4934, după răcire 0,4472 (−9 %); S99 (Muon 0,002) româna +0,08 (+7 %) într-o oră.
- S110 la 24 h a citit ~1,1 mld. simboluri (cât W2 în ~8,5 ore), la 12 h ~0,55 mld. (W2 la ~4 ore).

Estimarea mea pentru un S110 **sănătos**: ~1,50–1,70 la 12 h și ~1,40–1,58 la 24 h. Pragul de 1,40 e deci în mijlocul
plajei normale; șansa unei opriri greșite la 24 h o văd la ~50 % sau mai mult. Consecința (C-119): orele rămase nu se
folosesc fără „da” → placa stă ~30 h și nu există model nou luni.

Propunere (de scris în coadă înainte ca executantul să copieze pragurile în pre-înregistrare):

- **12 h — oprire doar dacă:** pierderea e NaN/inf; SAU româna orei 12 > **1,90**; SAU media română a orelor 10–12 nu e cu
  cel puțin **0,02** sub media orelor 4–6.
- **24 h — oprire doar dacă:** româna orei 24 > **1,70**; SAU media orelor 22–24 nu e cu cel puțin **0,02** sub media orelor 10–12.
- Principiul: oprim doar dacă modelul de 24 e mai slab decât era linia de 12 straturi, nerăcită, la același text citit, sau
  dacă a încetat să învețe. (W2 la aceleași cantități de text a câștigat ~3–6 % între aceste puncte, adică 0,05–0,10.)
- Informativ, pe procesor, fără placă: media greutăților ultimelor 3–4 modele orare (`experiment_N.pt`) + examenul de
  română pe ea. E o „răcire pe hârtie” ieftină; unealtă nouă mică în `unelte/` (granița 5). Nu o pun ca prag: e nemăsurată la voi.

### 1.3 „Pierderea a crescut 3 ore la rând” (C3) — CONFIRMAT

`module/model_conversatie.py:140,148`: `pierdere_finala` e pierderea **ultimului lot** al orei (4 ferestre; unele cu ținte
mascate). Zgomotul ei (±0,2) e mult peste scăderea reală pe oră (~0,01) după primele ore. Pentru valori dominate de zgomot,
4 valori la rând crescătoare apar cu șansa 1/24 pe fereastră; în 12 ore sunt 9 ferestre → ~30 % șanse de alarmă falsă.
Regula trebuie citită pe **româna orară** (scorul examenului, măsurat pe același text la fiecare oră), unde zgomotul e ~0,002.

### 1.4 Proba de rată (C6) — CONFIRMAT (cod) / PROBABIL (concluzia)

- 30 de minute = ~11.000 de loturi = **~480 de pași de optimizator**. Cu pornirea implicită, toți cei 480 de pași sunt în
  zona în care modelul încă își repară pornirea (§1.1), deci proba ar compara cât de repede o repară fiecare rată, nu care
  rată e bună pe termen lung. Cu C1 rezolvat, proba devine cinstită, dar tot scurtă: o rată mai mare câștigă aproape
  mereu primele 30 de minute. Ambele variante (0,02 / 0,0006 și 0,01 / 0,0003) sunt rezonabile; aș lua (a) dacă pierderea
  scade neted, altfel (b).
- `unelte/proba_muon.py` **nu pune recalculul** (nu cheamă `antrenare_recalcul.instaleaza()`), deci memoria și viteza din
  probă nu sunt cele ale rulării mari. Partea bună: proba arată pe gratis cât face modelul de 24 **fără recalcul** (simb/s și
  MB) — de notat în raport, e cifra care lipsește pentru §2.
- Proba trebuie făcută cu același `lot` / `adunare_loturi` și aceeași pornire ca rularea mare.

### 1.5 Încălzirea — CONFIRMAT (cod), risc mic

`module/model_gpt.py:401` numără încălzirea în **loturi**, nu în pași de optimizator: `incalzire_pasi = 1000` cu adunare 24
înseamnă **41,7 pași de optimizator (2,7 minute)**. Muon suportă încălziri scurte, dar partea AdamW (intrarea legată de
ieșire, la 0,0006) pornește practic fără încălzire. Recomand ~400 de pași de optimizator: `incalzire_pasi = 9600` la 4 × 24
sau `6400` la 6 × 16 (~20 de minute; 0,6 % din rulare).

### 1.6 Două piedici de procedură (C4, C5) — CONFIRMAT

- **C4.** `teste/test_examen_romana.py:129–140` are lista închisă a configurărilor care au voie să conțină `examen_romana`.
  `conv_w2_mare_24z.toml`, `conv_w2_mare_24zc.toml` și orice configurare de probă cu acel examen fac testul să pice. La
  S95/S99/S100 sarcina spunea explicit „adaugi configurarea în lista din test (singura schimbare permisă)”; la S110 și S111
  (`plan/coada.md:3743, 3765`) rândul lipsește. Un executant strict se oprește la „pytest verde”.
- **C5.** `unelte/kronos_cod/tokenizer_cod.py:60,309` (`SPATIU_MINIM_GB = 40`) face să pice
  `teste/test_kronos_cod_tokenizer.py::test_unealta_cap_coada_fara_excluse_si_fara_validare_la_antrenare` când C: are sub
  40 GB (văzut la S77c). Acum sunt ~73 GB (75,1 GB înainte de S109); fiecare oră salvează ~0,73 GB (`prag_zgomot = -1.0` → toate orele
  „păstrat”): sub 40 GB pe la ora ~43–44 din S110, ~26 GB la sfârșitul lui S111. Peste pragul de 15 GB al sarcinii, dar „toate testele
  trec înainte de gata” (`plan/REGULI_CASCADA.md`) nu mai e adevărat tocmai la trecerea S110 → S111.
  Nu recomand `prag_zgomot` mai mare ca să salveze mai rar: ultima oră ar putea ieși „respins”, iar uneltele cu `--linie` ar
  examina pe tăcute un model mai vechi.

### 1.7 Timpul până luni seara — CONFIRMAT (din S89/S100)

O „oră” de antrenare ține ~64,5 min de ceas (S89: 5 h în 5 h 22 min; S100: 2 h în 2 h 10 min); cu datele pe bucăți ~64 min.
54 h de antrenare ≈ **57,5 h de ceas**. Pornire ~19:15 vineri → gata luni ~04:45; S111 (7 h + examene) → luni ~14:00;
S112 → ~15:00. Încape, cu 3–4 ore de rezervă; o cădere costă 1–2 ore. **Important:** dacă timpul se strânge, nu se taie
coada rulării — tot câștigul vostru de până acum a venit din răcire (S38, S76b, S89). Se scurtează programul
(`durata_scaderii_secunde` pe o linie nouă, din copia stării), nu se oprește la rata mare.

### 1.8 Ce am verificat și e în regulă

- **Muon** (`module/model_muon.py:33–44, 76–87, 105–120`): pus doar pe matricile din `straturi.*` (q/k/v în 3 bucăți,
  `out_proj`, cele două din MLP); încorporările, pozițiile, LayerNorm și bias-urile merg pe AdamW. Newton–Schulz în 5 pași cu
  coeficienții publici, impuls 0,95 Nesterov, scalarea √max(1, rânduri/coloane) — toate ca în descrierea publică.
  `scadere_muon = 0` (fără „weight decay” pe matrici) e alegerea obișnuită.
- **Programul ratei și reluarea** (§7 C): rata după reluare se socotește din minutele și pașii salvați; încălzirea nu repornește.
- **Bucla** (`module/model_conversatie.py:99–158`): ținte mascate corect (pierdere doar pe răspunsuri), gradient adunat
  corect, un lot nu poate avea doar ținte mascate la fracțiile S110. Salvarea e atomică (`model_continuu.py:81–87`), starea
  se scrie înaintea examenelor suplimentare (`:185–192`).
- **Date:** `DateBucati` verifică SHA-256 pe fiecare bucată și tokenizerul la pornire (`module/date_bucati.py:150–195`), iar
  modelul refuză alt tokenizer (`model_gpt.py:339–357`). Validările de română sunt alt fișier decât antrenarea, cu amprente
  păzite (`module/examen_romana.py:33–45`).
- **O capcană de ținut minte** (nu lovește S110): la reluare, `load_state_dict` al optimizatorului readuce și
  `multiplicator_lr` salvat (`model_muon.py:66, 171–174`). Dacă cineva continuă o linie Muon cu altă `rata_muon` păstrând
  starea optimizatorului, rata Muon rămâne cea veche × forma nouă. La S99/S100 starea a fost golită, deci n-a contat.
- **„Weight decay” 0,1 pe tot grupul AdamW** (inclusiv LayerNorm și bias, `model_muon.py:115, 158–159`): nu e greșeală
  gravă, dar rețetele bune scot LayerNorm/bias din el. De schimbat la rețeta v2, nu acum.

### 1.9 Configurarea pe care aș porni S110 (față de textul din coadă)

```toml
[porturi.model]
modul = "module.model_gpt_cod:ModelGPTCod"      # C1 (în loc de module.model_muon:ModelGPTConversatieMuon)
# în setari, pe lângă ce scrie S110:
abatere_incorporari = 0.02                      # C1
lot = 6, adunare_loturi = 16                    # E1: același lot efectiv 96, +20 % simboluri pe oră
incalzire_pasi = 6400                           # = 400 de pași de optimizator
examene_suplimentare = []                       # E2: fără fapte / fapte noi / profesor la fiecare oră
hrana = ""                                      # E2: fără 5 % povești englezești (și fără fractie_hrana)
```
plus `--pauza 5` la `antrenare_recalcul.py`, `spatiu = { model = { lot = [6] } }` la cercetător, pragurile din §1.2 și
rândurile C4/C5 în sarcină. `hrana = ""` trebuie scris explicit: altfel `antrenare_lunga.py:107–113` pune hrana implicită.
Dacă se vrea schimbarea minimă: doar primele două rânduri (C1) și pragurile.

---

## 2. Eficiența pe RTX 3070 Ti 8 GB

Ce există deja și e bine: bf16 prin `autocast` (`model_gpt.py:323–326`), atenția prin `scaled_dot_product_attention`
(calea `need_weights=False` din `nn.MultiheadAttention`, `model_gpt.py:86`), datele prin mmap, costul lui Muon neglijabil
(un pas la 16–24 de loturi).

| ce | cifre | câștig | stare |
|---|---|---|---|
| **Lot 6 × 16 în loc de 4 × 24** | S86: (b) 6,06 loturi/s × 4 = 12,4 mii simb/s; (c) 4,84 × 6 = **14,9 mii**; (d) 2,63 × 12 = **16,2 mii**. S77c (lot 6, două ore reale): 5,1 × 6 = 15,7 mii (57 M simboluri/oră față de 47 M la S89). S77a (lot 12): 2,80 × 12 = 17,2 mii | **+20 %** (6 × 16), +25 % estimat (8 × 12), +30 % (12 × 8) | CONFIRMAT. Raportul S86 (rândurile 39 și 67) a comparat loturi/s între loturi de mărimi diferite și a tras concluzia inversă („(b) e cel mai rapid”, „(c) e mai lent cu ~20 %”) |
| Memoria la lot mai mare | S86 Muon, antrenare: 3.057 / 3.235 / 4.004 MB alocat la lot 4 / 6 / 12. În ordinea orchestratorului se adaugă ~1.330 MB de la ora 2 (S87: 4.378 față de 3.055 MB) | 6 × 16 → ~4,6 GB alocat, sub plafonul de 5.800; 12 × 8 → ~5,3 GB, prea aproape | lot 6 sigur; lot 8 probabil; lot 12 doar după ce dispare surplusul de mai jos |
| **Surplusul de ~1,3 GB în timpul antrenării** | `kronos/orchestrator.py:193–213` ține `model_test` în viață toată ora; rețeaua lui nu se eliberează din cauza ciclului `strat.forward → strat` (`unelte/antrenare_recalcul.py:52`), iar `gc.collect()` rulează doar înaintea testului rapid (`:159`) | +1,3 GB liberi → loc pentru lot 12 | CONFIRMAT (S87, varianta `b_orch_del`). Leac fără `kronos/`: un `gc.collect()` + `empty_cache()` și după construirea modelului adevărat, în unealtă |
| **Examenele de la fiecare oră** | `model_continuu.py:185–192` → `model_gpt.py:586–607` → `examene_elev.py:240–251`: 300 de completări în engleză, 40 de povești scrise simbol cu simbol, apoi profesorul Qwen încărcat pe placă. S87: „validare ~170–186 s” pe oră. Vârful plăcii (6.277–6.492 MB) vine de aici, nu din antrenare (3.834 MB la S104) | ~2,5 min/oră × 54 = **~2,3 h**; dispare și vârful de memorie și riscul de „out of memory” din `_dupa_examen` | CONFIRMAT |
| Pauza dintre ore | `unelte/antrenare_lunga.py:399`: 60 s implicit; placa stă la 62 °C, sub pragul de răcire de 70 °C | ~0,8 h pe 54 de ore | CONFIRMAT |
| „Hrana” | 5 % din ferestre vin din `date/fapte/povesti.txt` (4,8 MB, povești englezești scrise de profesor) → fiecare bucată citită de ~100 de ori | +5 % ferestre pentru text adevărat | CONFIRMAT |
| Fără recalculul activărilor | recalculul = încă o trecere înainte pe fiecare strat (~25–30 % din timp). La lot 4–6 cu Muon estimez 3,9–4,6 GB alocat fără recalcul | +25–30 % peste același lot | DE VERIFICAT — proba de rată o măsoară pe gratis (§1.4) |
| Tragerea ferestrelor | `model_conversatie.py:129`: ferestre la întâmplare, cu repetare. La ~1,7 treceri, ~19 % din text nu e văzut deloc, altă parte de 3–4 ori | câteva procente la aceleași ore | CONFIRMAT (cod); schimbarea e în `module/` → pentru rularea următoare |
| Atenție „flash”, `torch.compile` | calea de acum dă nucleului o mască explicită; `is_causal=True` ar cere un strat de atenție propriu. `torch.compile` pe placă cere Triton, care nu vine cu PyTorch pe Windows (instalare = „da”) | necunoscut pe Windows; nu promit nimic | DE VERIFICAT, cu o măsurare de 2 minute |

Totalul realist pentru S110, doar din configurare: **~3,05 mld. simboluri de text și conversație în loc de ~2,35 mld.**
(2,47 mld. din care 5 % hrană), adică **+30 %**, iar rularea se termină cu ~3 ore de ceas mai devreme. Cu „fără recalcul”
sau lot 12 (după măsurare), spre 3,5–4 mld.

Pe scurt: de la 12,7 mii simb/s la ~15–17 mii doar din configurare; ~19–20 mii estimat fără recalcul (de măsurat).
Dincolo de asta ajută doar hardware propriu.

---

## 3. Rețeta mai bună pentru rulările următoare (în ordinea câștig / efort)

Cum se validează ieftin, ca să nu se repete S94b: lecția de acolo e despre **continuarea unui model crescut**, unde
rata bună depindea de model. Pentru alegeri **de la zero** (pornire, optimizator, arhitectură, date) regula e alta:
(1) proxy cu aceeași adâncime, dar îngust (24 × 384, ~4 × mai ieftin), de la zero, 2 semințe, comparat la **același număr
de simboluri**, nu la timp egal; (2) câștigătorul se confirmă pe mărimea adevărată cu 3–6 ore de la zero, față de **curba
orară a lui S110** — după S110 aveți româna la fiecare oră, adică reperul gratuit pentru orice variantă viitoare.

| # | schimbarea | câștig așteptat la română (estimare) | efort | validare ieftină |
|---|---|---|---|---|
| 1 | **Amestec românesc** (§3.1) | **mare: −0,04…−0,07 bpb** | 1–2 h procesor, fără descărcări | 3 h de la zero pe ambele amestecuri, la același număr de simboluri |
| 2 | Pornirea corectă (C1) | −0,005…−0,01 la 54 h; mult mai mult la rulări scurte | un rând | deja măsurat (S61) |
| 3 | +20–35 % simboluri (§2) | −0,01…−0,015 | configurare | măsurat (S77c, S86) |
| 4 | Scădere mai lungă a ratei: vârf ~50 %, apoi liniar la 0 (acum 75 % / 25 %); încălzire 300–500 pași de optimizator | −0,003…−0,01 | configurare (`racire_finala = 0.5`) | două proxy-uri mici |
| 5 | **Media greutăților** ultimelor ore (pentru urmărire și, poate, ca model final) | 0…−0,01, gratis | unealtă mică, doar procesor | pe modelele orare ale lui S110 |
| 6 | Ultima parte a rulării doar pe română + conversație | −0,01…−0,02 la română (pierde engleza/codul) | un al doilea set de bucăți | proxy mic |
| 7 | Fără „weight decay” pe LayerNorm/bias; un mic „weight decay” pe matricile Muon la rulări lungi | mic | `module/model_muon.py` (aprobare) | proxy mic |
| 8 | Ferestre fără repetare (toată data citită o dată pe trecere) | mic–mediu când datele sunt puține | `module/` (aprobare) | proxy mic |
| 9 | Context 1024 (C-85 pct. 7) | −0,01…−0,02 pe texte lungi; memorie × ~1,6 | după măsurarea memoriei | 3 h de la zero |
| 10 | **Arhitectura v2** (poziții rotative, RMSNorm, QK-norm, ReLU², cap dezlegat, proiecții pornite de la zero) | în literatura publică 1,5–3 × mai puțin text pentru aceeași notă; la voi **de măsurat** | cod nou + adaptarea motorului KGR1 din OS | câte una, pe proxy 24 × 384, 2 semințe, apoi 3 h pe mărimea adevărată |
| 11 | Tokenizer românesc (C-89, parcat de Adrian) | de măsurat (context efectiv mai lung, vocabular mai bine folosit) | de la zero + motorul OS | simularea din C-89 |

Despre Muon: lotul vostru efectiv e ~49.000 de simboluri pe pas (rulările publice rapide folosesc ~500.000). La lot mic
direcția ortogonalizată e mai zgomotoasă, deci rata bună poate fi sub 0,02. S31 (0,01 pe model gata antrenat: mai slab cu
0,07 chiar după răcire) și S99 arată că Muon cu pași mari lasă un „zgomot” care se vede. Pentru rulările viitoare: o
comparație 0,02 / 0,01 / 0,005 pe proxy, **până la capăt, cu răcire**, nu doar primele 30 de minute.

### 3.1 Amestecul (punctul 4 din „Pe scurt”) — CONFIRMAT ca stare de fapt; câștigul e estimare

- `unelte/antreneaza_tokenizer_ws.py:38–44` + `unelte/pregateste_amestec_ws.py:53–77` +
  `docs/WORKSTATION_etapa2_2026-10-12.md:166–172`: amestecul de 4,89 GB (1,34 mld. simboluri) = **45,9 % TinyStories
  (engleză)**, **33,9 % română**, 15,1 % cod Python, 5,1 % numere. Româna (1,66 GB ≈ 0,48 mld. simboluri) = Wikipedia
  0,52 GB + web (FineWeb-2) 0,52 GB + fabule 0,35 GB + Wikisource 0,13 GB + Europarl 0,13 GB + Tatoeba.
- Din ce e **deja descărcat și curățat** (`docs/DATE_surse.md:23–33`) nu se folosesc: **2,45 GB din FineWeb-2 română**
  (2,97 GB curat, luat doar începutul) și 0,24 GB din Wikipedia. Nicio descărcare nouă.
- În S110, cum e scris: ~2,47 mld. simboluri × 90 % text × ~35 % = **~0,78 mld. simboluri de română** (1,6 treceri prin
  aceleași 0,48 mld.). Restul orelor merg pe engleză simplă, cod și numere.
- Două căi, ambele fără descărcări:
  - **(A) curat:** un set nou de bucăți cu ~80 % română (tot FineWeb-2 2,97 GB + Wikipedia + Wikisource + Europarl, ~10 %
    TinyStories, ~5 % cod, ~5 % numere/altele). Cere o unealtă mică de amestec (cea de acum are părțile fixe) +
    `unelte/bucati_din_text.py` (~20 min la 4,9 GB) + verificarea scurgerilor. ~1,5–2 h de procesor.
  - **(B) doar din configurare:** restul nefolosit din FineWeb-2 ca `hrana`, cu `fractie_hrana ≈ 0.55`. Bucla ia deja
    ferestre din trei surse (`model_conversatie.py:119–131`). Rezultă ~69 % română, 2,5 × mai mult text românesc diferit
    și ~2,1 mld. simboluri de română citite (cu lot 6) în loc de ~0,78 mld. Cere: fișierul cu restul (tăiat de la octetul
    din `date/ws/amestec/info.json`), simbolurile lui puse în `lucru/cache` dinainte (altfel testul rapid depășește 600 s)
    și verificarea scurgerilor. ~1 h de procesor. Preț mic: fișierul (2,45 GB) se recitește de două ori pe oră pentru cheia
    din cache (~40–50 s pe oră, câțiva GB de RAM pentru scurt timp).
- Obligatoriu la oricare: `unelte/scurgeri_examen.py` cu textul nou față de validările de română. `validare_curata.txt` a
  fost curățată doar față de amestecul vechi; textul web are șabloane care se repetă. Examenul nu se schimbă (e păzit), dar
  textele noi care se suprapun cu validarea se scot din antrenare. Aș lăsa deoparte restul de Wikipedia: din el sunt făcute
  textele examenelor „răspuns din text”.
- Cât ar aduce: pe linia voastră, de la 1,38 (1,3 mld. simboluri) la 1,21 (~10 mld.) sunt ~0,05 bpb la fiecare dublare a
  textului citit, o parte din rețetă. De 2,6 × mai multă română citită, din care cea mai mare parte text nou → **~0,04–0,07
  bpb** (prag de decizie: 0,005). E estimare, nu măsurătoare; validarea web (o treime din examen, 1,30 acum) ar câștiga cel mai mult.
- Costul: poveștile în engleză, codul și numerele slăbesc (la S110 sunt doar informative). Verdictul „24 de straturi față
  de #513” n-ar mai măsura doar mărimea, ci mărimea + datele; se spune deschis în pre-înregistrare.
- De știut, legat de regula „fără date de la alt AI”: TinyStories (45,9 % din amestec) e text scris de un model,
  `fabule_ro` la fel („generate de alt model”, `docs/DATE_surse.md:14`), iar `povesti.txt` (hrana) e scrisă de profesorul
  Qwen. Sunt aprobate de Adrian în octombrie; le semnalez doar. Un amestec românesc din web + Wikipedia + Wikisource scade
  mult partea asta.

### 3.2 Datele de conversație, fără alt AI

Ce arată S105, S76a și S109: (1) 23.066 din 23.251 de perechi au text alături, doar 185 (37 scrise de mână × 5) nu →
fără text, modelul spune „Nu scrie în text.”; (2) tipurile învățate urcă la 102/130, dar tipurile nevăzute **scad** (10 → 5):
modelul învață șabloane, nu „caută răspunsul în text”. Ce aș face, în ordine:

1. **Două forme clare:** cu `Text:` → răspuns din text sau „Nu scrie în text.”; fără text → răspuns din ce știe sau
   „Nu știu sigur.”. Perechile fără text există deja prin reguli: `unelte/conversatie_wikipedia.py` („Ce este / Cine a
   fost / Unde se află X?” → prima propoziție a articolului) și `unelte/nu_stiu_ro.py`. Fără perechile scrise de profesor
   din `unelte/genereaza_conversatie.py` și fără traducerile automate (acelea sunt de la alt AI).
2. **Multe feluri de întrebări, puține exemple din fiecare**, nu puține feluri cu mii de exemple: întrebări generate prin
   reguli din orice propoziție (se ascunde un nume, un an, un loc, un număr și se întreabă cine / când / unde / cât), cu
   10–20 de formulări pe fel. Examenul cu tipuri nevăzute (partea ii) să fie criteriu, nu doar informativ.
3. **Dialog scris de oameni, din ce e pe disc:** replicile din piesele și romanele de pe Wikisource (liniile cu „—”),
   paginile de tip întrebare–răspuns din FineWeb-2 (rânduri care se termină cu „?” urmate de un paragraf), perechile
   Tatoeba și Europarl ca instrucțiuni „Tradu în română / engleză”.
4. **Sarcini făcute din text, cu răspuns verificabil automat:** „pune diacriticele”, „continuă propoziția”, „scrie titlul
   potrivit”, „care e prima propoziție”, „câte cuvinte are”. Se potrivesc cu școala cu verificator a lui Adrian (C-62).
5. **50–100 de replici scrise chiar de Adrian** („Salut!”, „Cine ești?”, „Ce știi să faci?”): puține, dar sunt vocea lui
   Kronos și exact ce va încerca prima dată în chat.

---

## 4. Examenele și metoda

- **Româna (bpb)** — `module/examen_romana.py:112–128`: 3 × 100.000 de litere (Wikipedia, web, cărți vechi), ~50–60 de
  texte în total. Pentru două modele pe același text zgomotul e ~0,002 (voi l-ați văzut: #513 iese 1,2060 de fiecare
  dată), deci pragul de 0,005 e bun. Slăbiciuni: o treime din notă e Wikisource (limbă veche); doar 7–8 texte de carte;
  nota la rata mare nu se compară cu cea finală (§1.2). Aș raporta mereu și cele trei note separat și aș privi „web” ca
  cea mai apropiată de româna vorbită azi. O singură sămânță peste tot: de aceea banda „LA FEL” de ±0,005 trebuie păstrată.
- **Fereastra examenului** (`model_gpt.py:545–548`): ferestre care nu se suprapun; primele simboluri din fiecare au
  context scurt. Ridică nota tuturor modelelor la fel; comparațiile rămân corecte.
- **Examenul de conversație (1,9 din 10)** e la podea: măsoară „Nu scrie în text.” spus de ambele modele (S105). **R1** e
  la tavan (99 %). Niciunul nu mai desparte modelele. S15, S4 și `examen_tipuri_noi` despart, dar sunt mici.
- **Puterea statistică la S111** (`plan/coada.md:3768`): „corecte ≥ cel mai bun − 5” pe ~330 de întrebări. Două modele la
  fel de bune diferă din întâmplare cu ±7–8 (dacă ~60 de întrebări ies diferit), deci regula respinge un model egal în
  ~25 % din cazuri. Propun marja −10 sau un test pe perechi (câte întrebări câștigă fiecare; diferență reală dacă una
  câștigă de ~2 ori mai des).
- **Profesorul Qwen ca notă:** la S109 a greșit vizibil (#75: răspuns identic cu referința, nota 1). Verificatorul cu
  reguli (S16) ar trebui să fie martorul principal, profesorul al doilea.
- **Ce lipsește pentru ținta lui Adrian:** o măsură a textului *scris* de Kronos în română. Fără alt AI se pot număra, pe
  200 de începuturi fixe: câte cuvinte sunt în lista de cuvinte românești (`date/conversatie/cuvinte_ro.txt`), cât se
  repetă, câte propoziții se termină corect. Plus o probă oarbă cu Adrian: 20 de perechi de răspunsuri (#577 și modelul nou),
  fără nume, alege care e mai bun; 15 din 20 înseamnă diferență reală.
- **Scurgeri:** paza cu bucăți de 8 cuvinte între antrenarea de conversație și examene e bună. Un colț neacoperit:
  textele examenelor „răspuns din text” vin din Wikipedia de antrenare, deci modelul le-a putut citi ca text simplu în
  amestec (#513 de ~7 ori, modelul nou de ~2 ori). Efectul e probabil mic, dar avantajează modelul vechi la S111.

---

## 5. Ca Adrian să vorbească luni seara cu cel mai bun Kronos

**Acum (înainte de rularea mare):** C1–C6, E1, E2 în S110. Dacă Adrian spune „da” în următoarea oră: amestecul (B) din
§3.1; dacă nu, S110 pornește pe amestecul actual, iar bucățile românești se pregătesc pe procesor în timpul celor 54 de ore
(procesorul stă liber), pentru rularea de după.

**În timpul lui S110 (doar procesor, fără să atingă placa):**
1. Unealta de chat din §5.1 și testele ei.
2. Fișierul de conversație pentru S111 cu perechi fără text (§3.2, punctul 1).
3. Unealta de medie a greutăților + româna pe ea la orele 12, 24, 36, 48 (informativ).
4. Verificarea scurgerilor pentru textul românesc nefolosit.

**S111** (`plan/coada.md:3765`):
- Rata: sarcina cere AdamW **0,00003**. Pe modelul de 24 de straturi, voi ați măsurat: 5e-5 strică (S77c: 1,2096 → 1,2268),
  2e-5 strică puțin (S77e: 1,2160), **1e-5 ține** (1,2120) și tot la 1e-5 R1 a ajuns la 99,2 (S89); S94b a găsit ×0,5 cel
  mai bun. Modelul nou nu e cel crescut, dar varianta dovedită e 1e-5 cu încălzire 1000. Trecerea de la Muon la AdamW cu
  stare goală e și ea un șoc (S31, S99 în sens invers) — încă un motiv pentru rata mică.
- Datele: dacă rămâne doar `romana_raspunsuri_r2`, modelul nou va spune și el „Nu scrie în text.” în chat. Cu perechile
  fără text adăugate, fila de chat capătă sens.
- „Cel mai bun de până acum” e **#577** (S109: AJUTĂ, română 1,2055).

**Așteptarea cinstită pentru modelul de 24:** a citit de ~3–4 ori mai puțin text decât linia lui #513 (~3 mld. față de
~10 mld. simboluri în ~70–80 de ore; estimare din rapoarte). Pe amestecul actual văd finalul la **1,19–1,24** (supraveghetorul: 1,17–1,19), deci
„MAI BUN decât #513” e cam 40 %. Cu C1 + E1 urcă puțin; cu amestecul românesc, spre 80–90 %. Oricum iese, luni există un
model bun de pus în chat: #577.

### 5.1 Interfața (S112) — CONFIRMAT

- Fila de chat: `module/interfata/creiere.py:65–69` trimite textul lui Adrian direct la `model.genereaza(text, 200)`.
  `model_gpt.py:559–584, 638–657`: continuare de text, cu întâmplare totală (temperatura 1, tot vocabularul), aceeași
  sămânță de fiecare dată, **exact 200 de litere**, fără oprire la `<|endoftext|>`. Întrebarea nu e pusă în forma învățată
  (`Întrebare: …⏎Răspuns:`); doar fila „Întreabă din text” o face (`creiere.py:82–108`).
- Fără antrenare, cu o unealtă nouă în `unelte/` care pornește același server cu alt „creier” (nu atinge `module/` și
  nici `kronos/`):
  1. întrebarea în forma învățată; răspuns cu temperatură ~0,7 și doar cele mai probabile ~40 de bucăți, oprit la sfârșitul
     răspunsului; ş/ţ și textul fără diacritice aduse la forma din antrenare;
  2. **căutare + citire**: întrebarea → căutarea E3 pe Wikipedia (`module/cautare_e3.py`, indexul din `lucru/e3/`) →
     paragraful găsit pus ca `Text:` → Kronos răspunde și arată sursa. Măsurat la voi: **336 din 500 corecte (67 %)** pe
     întrebări nevăzute (S44), 93 % când răspunsul e în paragraful adus. Adrian a amânat „memoria de fapte” pe 13 nov
     (DECIZII 11:11), deci asta cere „da”-ul lui; e însă piesă existentă, nu cod de antrenare, și e diferența dintre un
     chat care răspunde și unul care spune „Nu scrie în text.”;
  3. modelul pe placă (liberă după S111): un răspuns în 1–2 s în loc de zeci de secunde pe procesor la 24 de straturi.
- De spus lui Adrian dinainte: Kronos va răspunde bine la întrebări despre lucruri din Wikipedia (cu căutarea) și la
  întrebări despre un text dat; nu va purta o discuție liberă. Asta vine din datele de la §3.2, nu din ore de placă.

---

## 6. Ce n-am putut verifica

- Nimic pe placă: memoria și viteza pentru lot 8, lot 12 în ordinea orchestratorului și „fără recalcul” sunt estimări.
- `lucru/` și `date/` nu sunt în clonă: mărimile (2,97 GB FineWeb-2 curat, 4,8 MB hrana) sunt din documentele voastre, nu
  din fișiere. Existența lui `date/conversatie/wikipedia.jsonl` și a indexului `lucru/e3/` pe workstation e de verificat.
- Româna nerăcită a liniei W2 n-a fost măsurată niciodată; cifrele din §1.2 sunt deduse din raportul nerăcit/răcit la povești.
- Câștigurile din §3 sunt estimări din curba voastră și din literatura publică, nu măsurători.
- N-am rulat toată suita de teste (aici nu e placă și sunt 2 nuclee); am rulat doar verificările de mai jos.

## 7. Ce am rulat (procesor, în dosarul de lucru al reviziei, cu PyTorch 2.14.1 doar pentru procesor)

| | ce | rezultat |
|---|---|---|
| A | `verif/a_init.py`: rețeaua S110 adevărată, pierderea de pornire | implicit 410,76; cu 0,02: 9,86 (§1.1) |
| B | `verif/b_cod_bucati.py`: `ModelGPTCod` + `abatere_incorporari` pe drumul S110, model mic | merge: Muon în 3 grupuri, recalcul pe toate straturile, stare salvată, ora 2 `continuat = True`, greutățile reluate = cele salvate, se încarcă și cu clasa veche |
| C | `verif/c_rata.py`: programul ratei S110 cu funcțiile modelului | încălzire 41,7 pași de optimizator (2,7 min); vârf până la 40,5 h; 0 la 54 h; după reluare la 12 h și 45 h rata e cea corectă, fără încălzire nouă |
| D | `verif/d_init_muon.py`: model mic (4 × 256), Muon 0,02 + AdamW 6e-4, gradient adunat, 600 de pași de optimizator, pornire implicită față de 0,02 | vezi mai jos |

Proba D, pierderea medie pe pas de optimizator (model 4 × 256, vocabular 2.048, text = rapoartele în română din repo;
aceeași sămânță, aceleași loturi; doar pornirea diferă):

| pasul de optimizator | 1 | 42 | 80 | 120 | 200 | 260 | 400 | 600 |
|---|---|---|---|---|---|---|---|---|
| pornirea implicită | 169,7 | 35,9 | 11,7 | 7,29 | 5,02 | 4,34 | 3,56 | 3,39 |
| încorporări 0,02 | 7,69 | 6,05 | 5,02 | 4,32 | 3,76 | 3,34 | 2,76 | 2,72 |

Primul pas cu pierderea sub 6,0 / 5,0 / 4,5: implicit 146 / 191 / 222; cu 0,02: 47 / 77 / 104. Abaterea încorporărilor la
final: 0,961 față de 0,045. Atenție la citire: textul probei e mic (1,2 MB, citit de mai multe ori), deci cifrele de la
sfârșit conțin și memorare; proba arată direcția și ordinul de mărime, nu cifra pentru modelul de 183 M.

| | încă o verificare | rezultat |
|---|---|---|
| E | `verif/e_config.py`: copia lui `conv_w2_mare_24n.toml` cu schimbările din §1.9, trecută prin `kronos.config.citeste_config`, regulile din `antrenare_lunga.py` și constructorul din registru | se citește și se construiește: `ModelGPTCod`, lot 6 × 16, fără hrană (nici cea implicită), fără examene suplimentare, `abatere_incorporari` 0,02, Muon 0,02, starea se salvează după examen |

Scripturile sunt în `/tmp/claude-0/-home-claude/093c37c9-a22c-5509-b255-2ba7da286b7c/scratchpad/verif/`. Depozitele au rămas
neatinse (`git status` curat în `cyberspace` după fiecare rulare).
