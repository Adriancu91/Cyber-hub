---
title: "Kronos · Cyber Universe OS · Cyber-GPU — dosar tehnic complet pentru evaluare"
subtitle: "Starea la 21 noiembrie 2026, ora 19:45 (ora României)"
---

# Cum se citește acest dosar

Dosarul descrie un proiect software făcut de la zero, ca să poată fi evaluat de cineva din afară: un programator sau un alt sistem AI. Conține tot ce există, cum funcționează, ce teste au trecut (cu cifrele exacte din jurnale), ce **nu** funcționează încă și condițiile în care s-a lucrat.

Nu conține nicio estimare de valoare sau de cost. Evaluarea e lăsată în întregime cititorului.

Reguli de cinste folosite peste tot:

- **MĂSURAT** = cifră citită din jurnalul unui test rulat pe hardware real.
- **SIMULARE** = testat doar într-un model software al plăcii video, nu pe placă.
- **DEDUS** = estimare sau concluzie, nemăsurată.

Unde o comparație nu e perfect cinstită, limita e scrisă imediat lângă cifră. Toate limitele sunt adunate și în secțiunea 9.

# 1. Pe scurt

Proiectul are trei piese care lucrează împreună:

| Piesa | Ce este | Limbaj | Început |
|---|---|---|---|
| **Kronos** (platforma *Cyberspace*) | Un model de limbaj (AI care scrie text, în principal în română) proiectat, antrenat și evaluat de la zero, plus o platformă de experimente care îl îmbunătățește automat | Python (PyTorch pentru antrenare) | 2 octombrie 2026 |
| **Cyber Universe OS** | Un sistem de operare propriu, de la zero: nucleu, drivere, rețea, criptografie, interfață grafică, aplicații. Pornește pe calculatoare reale de pe un stick USB | Rust (`no_std`), x86_64, UEFI | 20 octombrie 2026 |
| **Cyber-GPU** | Un driver propriu de calcul pentru placa video NVIDIA RTX 3070 Ti (cip GA104, arhitectura Ampere), fără driverul NVIDIA, fără CUDA, fără Windows sau Linux | Rust (`no_std`) + programe GPU proprii | 23 octombrie 2026 |

**Rezultatul principal (MĂSURAT, 21 noiembrie 2026):** Kronos rulează în sistemul de operare propriu, pe placa video, prin driverul propriu. Scrie 16 cuvinte (simboluri) identice cu cele calculate pe procesor, cu o viteză medie de **351,39 simboluri pe secundă** pe tot drumul: placă, driver și jurnal. Pe aceeași placă, în Windows, cu driverul NVIDIA și PyTorch, Kronos ajunge azi la 129,12 simboluri pe secundă. Comparația are o limită importantă, explicată în secțiunea 6.3.

**Cine a lucrat:** un singur om, Adrian, proprietarul proiectului. Adrian nu scrie cod. A condus tot proiectul: a decis arhitectura și ordinea pașilor, a aprobat fiecare pas riscant, a rulat testele pe hardware și a învățat mecanismele. Codul a fost scris de agenți AI de programare care lucrează în sesiuni automate, în cascadă, coordonate printr-un centru comun de lucru (secțiunea 7).

**Durata:** 7 săptămâni și o zi (2 octombrie – 21 noiembrie 2026). Pentru sistemul de operare și driver: 4 săptămâni și 4 zile.

# 2. Hardware-ul folosit

| Calculator | Detalii | Rol |
|---|---|---|
| Workstation | Dell Precision 5820 Tower, Intel Core i9-10980XE (18 nuclee / 36 fire, AVX-512), 128 GB RAM, **NVIDIA GeForce RTX 3070 Ti 8 GB** (GA104), Windows 11; disc SAS adăugat în noiembrie 2026 | Antrenarea lui Kronos (în Windows, până la 21 nov) și toate testele driverului video |
| Laptop 1 | ASUS TUF Gaming F15 (i7-11800H, 8 nuclee / 16 fire, 64 GB RAM, RTX 3060 Laptop 6 GB, GA106) | Teste ale sistemului de operare; driverul video doar citește placa (nicio scriere) |
| Laptop 2 | Lenovo ThinkPad L15 Gen 2 (i7-1185G7, 16 GB RAM, grafică Intel integrată) | Teste ale sistemului de operare pe alt hardware |
| Stick-uri USB | stick de test FAT32 | Sistemul de operare pornește de pe stick; acolo stau și modelul Kronos, firmware-ul NVIDIA și jurnalele |

Nu s-au folosit servere închiriate și nici plăci video în cloud. Codul s-a scris și s-a testat automat (compilare, teste, emulatorul QEMU) pe mașini cloud gratuite ale sistemului de integrare continuă.

# 3. Kronos — modelul de limbaj și platforma de experimente

## 3.1 Ce este

Kronos e un model de limbaj de tip transformator (familia GPT, numai decodor), scris și antrenat de la zero. Nu e un model descărcat și nici o versiune reglată a unui model existent. Platforma în jurul lui se numește **Cyberspace**:

- **nucleul `kronos/`** (registru de module, contracte, configurare, orchestrator, jurnal, „paznic”): orchestratorul rulează experimente, iar paznicul blochează un experiment dacă examenul a fost modificat;
- **modulele înlocuibile `module/`**: tokenizere, modele, surse de date, examene, interfețe. Fiecare modul are un manifest (nume, port, versiune, versiunea contractului) și intră doar dacă trece testele de contract;
- **o buclă de experimente care se îmbunătățește singură**: propune o schimbare, antrenează, dă examenul, păstrează doar ce e mai bun și notează totul în jurnal. Pragurile de reușită se scriu **înainte** de rulare („pre-înregistrare”), ca rezultatul să nu poată fi ales după.

## 3.2 Modelele în uz

| | #513 (implicit în sistemul de operare) | #651 (cel mai bun, folosit în chat) |
|---|---|---|
| Arhitectura | 12 straturi, 12 capete de atenție, dimensiunea 768, context 512, vocabular 16.384, cap de ieșire legat de tabela de intrare | 24 de straturi, 12 capete, 768, context 512, vocabular 16.384, cap legat |
| Parametri | ~98 milioane | **183.086.592** |
| Fișierul pentru sistemul de operare | `kronos_513_q8_0.kgr`, 110.859.008 octeți | `kronos_651_q8_0.kgr`, 206.898.464 octeți (292 de tensori: 98 Q8_0, 194 F32) |
| Tokenizer | BPE propriu, 16.384 de simboluri, antrenat de noi pe text românesc și cod („w2”) | același |

**Formatul KGR1** e un format propriu de fișier pentru greutăți: antet cu cheile arhitecturii și tokenizerul inclus, tensori F32 sau Q8_0 (numere pe 8 biți cu o scară pe fiecare bloc de 32). E documentat complet, ca un motor scris de altcineva să-l poată citi fără codul Kronos. Pentru verificare există fișiere de control: un model minuscul F32 și Q8_0 și vectori cu simbolurile și logit-urile așteptate pe trei texte.

**Exemple de ieșire (#651, alegerea celui mai probabil simbol):**

- „Capitala României este” → „ orașul București.”
- „def suma(a, b):” → „return sum(a…”

Modelul mai mic #513 greșea pe aceleași texte („Baia Mare”, `a * b`). Kronos e un model mic. Face greșeli de fapte și nu se compară ca nivel cu modelele comerciale mari.

## 3.3 Cât s-a lucrat la Kronos

- **133 de sesiuni de experimente** (S1–S133), fiecare cu raport scris: 217 rapoarte în `docs/rapoarte/`.
- Etape: n-gram → GPT pe litere → tokenizer pe bucăți de cuvinte → memorie ierarhică și „plasa de noduri”. Ambele au fost testate și găsite fără efect măsurabil; rezultatele negative sunt păstrate. Au urmat modele mai mari, date în română, cod, conversație și examene în română.
- Date de antrenare: Wikipedia în română, TinyStories, cod, conversații. Seturile pregătite au de la 0,47 la 4,85 GB de text fiecare.
- Examene proprii: biți pe octet pe text curat (română, cod) și examene pe instrucțiuni și întrebări reformulate. De exemplu #651: română curat **1,0878** biți pe octet, față de 1,2060 la #513.
- Antrenarea a rulat pe workstation, în Windows, cu PyTorch, cu limite stricte de memorie video și temperatură, verificate de paznic.
- **Pauză la antrenări din 21 nov 2026:** antrenarea se mută în sistemul de operare propriu, pe un motor de antrenare propriu (secțiunea 8).
- **„Pasul de aur” (21 nov):** 10 pași de antrenare PyTorch, reproductibili, exportați complet: greutăți inițiale, lotul, eroarea la fiecare pas, gradientul fiecărui tensor la pasul 1 și greutățile după pașii 1 și 10, pentru SGD și pentru AdamW exact ca la antrenarea lui #513. Motorul de antrenare propriu se verifică pe aceste numere.

## 3.4 Mărimea codului Kronos

| Parte | Linii Python |
|---|---|
| `module/` (modele, tokenizere, date, examene, interfețe, motorul limbii române) | 17.064 |
| `unelte/` (antrenare, export KGR1, măsurători, interfața de chat) | 32.182 |
| `kronos/` (nucleul) | 1.268 |
| `teste/` | 20.617 |
| **Total** | **~71.000** |

- **1.212 funcții de test** (1.563 de cazuri de test trec). Documentație: 320 de fișiere, ~42.600 de rânduri.
- 933 de modificări salvate (commit-uri) între 2 octombrie și 20 noiembrie.

# 4. Cyber Universe OS — sistemul de operare

## 4.1 Ce face, concret

Sistemul pornește prin UEFI cu încărcătorul open-source Limine. Toate componentele de mai jos sunt scrise de la zero:

**Nucleul**

- GDT, TSS, IDT și excepții cu stive separate;
- alocator de memorie fizică și paginare cu tabele proprii;
- heap pentru nucleu;
- ACPI (RSDP, MADT, FADT, MCFG), APIC și temporizator;
- fire de execuție, planificator preemptiv, mutex-uri și cozi de așteptare;
- **SMP**: toate cele 36 de fire ale workstation-ului pornite în 443 ms, încuietori reale, planificator pe toate nucleele;
- SSE/AVX prin XSAVE.

**Programe**

- mod utilizator (ring 3) și apeluri de sistem;
- încărcarea programelor ELF64;
- spații de adrese separate;
- permisiuni pe program („promisiuni” și căi vizibile, care după declarare nu se mai pot lărgi);
- fire multiple în proces și memorie mare (MiB–GiB, pagini mari).

**Fișiere**

- VFS, ramfs și initrd tar;
- FAT32 cu citire și scriere;
- manager de module.

**Drivere**

- PCI pe toate magistralele;
- AHCI (SATA) și NVMe;
- USB xHCI, cu hub-uri, tastatură și mouse HID, stick-uri Mass Storage (Bulk-Only + SCSI) și conectare după pornire;
- tastatură și mouse PS/2;
- plăci de rețea Intel e1000/e1000e (I219-LM) și Realtek RTL8168/8111;
- citirea plăcii Wi-Fi Intel AX201 (doar citire, încă fără conectare);
- ceas RTC, repornire pe hardware real, temperatura procesorului;
- ceasul de pază al plăcii de bază.

**Rețea și criptografie** (toată criptografia e scrisă de noi și verificată pe vectorii oficiali NIST/RFC):

- Ethernet, ARP, IPv4, ICMP, UDP, DHCP, DNS, TCP și socket-uri pentru programe;
- SHA-256/384, HMAC, HKDF, X25519, ChaCha20-Poly1305, RSA (PKCS#1 v1.5 și PSS), ECDSA P-256, certificate X.509 cu lanțul de încredere;
- **client TLS 1.3** și HTTPS către site-uri reale, cu rădăcinile de încredere Mozilla;
- parser JSON propriu.

**Interfață și aplicații**

- bibliotecă grafică cu buffer dublu, font propriu cu diacritice românești și UTF-8, aranjament de tastatură românesc;
- server de ferestre cu cursor și un desktop;
- aplicații: terminal, monitor de sistem, fișiere, editor de text, setări, rețea, browser text;
- client pentru un API de AI extern (oprit, are nevoie de o cheie pusă de proprietar).

**Unelte de independență față de Windows**

- **actualizare de sine**: descarcă o versiune nouă prin HTTPS, verifică sumele SHA-256, rescrie stick-ul și revine automat dacă versiunea nouă nu pornește;
- consolă la distanță criptată și autentificată (X25519 + HKDF + ChaCha20-Poly1305);
- rapoartele și jurnalele pleacă singure, din sistem, către centrul de lucru;
- comenzi primite de la centrul de lucru, doar dintr-o listă albă;
- inventarul complet al hardware-ului;
- ciclul automat de test pe placa video (secțiunea 5.4);
- **agentul viu** (secțiunea 4.3).

**Kronos în sistemul de operare, pe procesor**

- motor propriu de inferență KGR1 în Rust: tokenizerul din fișier, AVX2+FMA, toate nucleele;
- căutare automată a celei mai bune variante de calcul pentru procesorul pe care rulează;
- conversație cu modelul.

MĂSURAT: **72,72 simboluri pe secundă pe procesor**. PyTorch pe procesorul aceluiași calculator, în Windows, dă 41,74.

## 4.2 Cum se lucrează și se testează

- Planul are faze P0–P6 și sarcini K6. **199 de sarcini terminate din 205**, fiecare cu plan scris (scop, pași, fișiere, test, riscuri, surse) și cu cel puțin un test automat.
- **Integrare continuă:** la fiecare modificare, compilarea și **123 de scenarii de test** rulate în emulatorul QEMU (nucleul pornește fără ecran și se verifică textul de pe portul serial), plus 64 de teste unitare. O rulare completă durează ~42 de minute. Fiecare versiune reușită devine o versiune publicată, cu toate fișierele stick-ului și sumele SHA-256 (`os-1` … **`os-332`**).
- Testat pe hardware real: workstation-ul Dell, laptopurile ASUS TUF și Lenovo ThinkPad.

**Mărimea codului sistemului de operare (Rust):**

| Parte | Linii Rust |
|---|---|
| Nucleul (`kernel/`) | 36.720 |
| Programe în mod utilizator (`user/`) | 13.509 |
| Criptografie (`crypto/`) | 2.556 |
| TLS (`tls/`) | 770 |
| JSON (`json/`) | 717 |
| Driver Realtek (`rtl8168/`) | 2.038 |
| Driver Intel (`e1000e/`) | 909 |
| **Total** | **~57.300** |

Plus ~2.000 de linii de scripturi de construcție și test. Documentație: 257 de fișiere, ~10.500 de rânduri. 693 de modificări salvate.

## 4.3 Agentul viu

Agentul viu e un canal prin care un asistent AI aflat la distanță conduce sistemul de operare pas cu pas, fără ca cineva să stea la calculator.

**Cum funcționează:**

1. Fiecare comandă e un fișier JSON cu număr de ordine, sesiune, fel și text, semnat cu HMAC-SHA-256 cu o cheie aflată doar pe stick.
2. Sistemul verifică la ~2,5 s dacă a apărut o comandă nouă.
3. Execută comanda o singură dată, în ordine, și răspunde cu ce a scris comanda, codul de ieșire, textul ecranului și starea sistemului.

**Ce se refuză:**

- semnătura greșită;
- numărul de ordine greșit;
- comanda repetată;
- altă sesiune;
- orice comandă care ar scrie în placa video fără o a doua cheie pusă de proprietar.

Cheia secretă nu se poate citi din nicio comandă și e scoasă automat din orice răspuns.

**Probat pe workstation pe 21 nov 2026, în 3 sesiuni:** 88 de comenzi, 70 executate o singură dată și în ordine, 18 refuzate exact cum trebuia. Ecoul comenzilor a fost identic în toate cele 88 de cazuri: zero abateri. Au fost incluse un lot de 10 comenzi trimise deodată, texte cu diacritice, emoji, 3.000 de caractere și 7 încercări de a scoate cheia, toate oprite.

# 5. Cyber-GPU — driverul propriu pentru placa video

## 5.1 De ce e greu

Pe o placă NVIDIA modernă, partea care conduce placa rulează pe un procesor aflat pe placă (GSP), cu firmware semnat de NVIDIA. Un driver trebuie să facă mai multe lucruri, în ordinea și formatul exacte:

- să pregătească memoria protejată a plăcii;
- să pornească în ordine trei procesoare interne (FWSEC, SEC2/Booter, GSP);
- să încarce firmware-ul GSP-RM;
- să comunice cu el prin mesaje RPC în formatul lui exact;
- să-i ceară canale de lucru, spații de adrese și obiecte de calcul;
- abia apoi să-i trimită programe.

NVIDIA nu publică o specificație completă a acestui drum. Am folosit doar surse publice:

- antetele open-source NVIDIA (licență MIT, versiunea 570.144);
- proiecte open-source citite ca specificație, nu copiate: tinygrad (MIT), Mesa/NVK (MIT), nouveau și nova (doar pentru idei);
- comportamentul observat pe placă.

Nimic GPL nu a intrat în cod. Firmware-ul semnat NVIDIA 570.144, din pachetul oficial `linux-firmware`, e folosit așa cum e. Nu e inclus în cod, nu e modificat și nu e analizat pe dinăuntru.

## 5.2 Lanțul de pornire, pas cu pas (toți pașii trec pe placa reală)

| Pas | Ce face | Prima trecere pe placa reală |
|---|---|---|
| I0–I3 | Placa găsită pe PCI, regiunile de memorie (BAR), identificarea cipului, citiri | 29 oct |
| I4 | Fișierele firmware de pe stick citite și verificate | 29 oct |
| I5 | Structurile pentru GSP-RM construite | 2–3 nov |
| I6 | FWSEC-FRTS: zona protejată a memoriei video (WPR2) ridicată | 3–5 nov |
| I7 | Booter: firmware-ul GSP încărcat în zona protejată | 5 nov |
| I8 | GSP-RM pornit; inițializare completă confirmată de placă (GSP_INIT_DONE) | **16 nov** |
| I8e | „Imaginea de aur” (starea plăcii după inițializare) | 16 nov |
| I9 | Canalul de lucru: grup de canale, canal GPFIFO, obiect de calcul, context promovat | **18 nov** |
| I10 | Primul program propriu rulat pe placă (adunare), costul unei lansări măsurat | 18 nov |
| I11 | Copiere RAM ↔ memorie video | 18 nov |
| I12 | Înmulțire matrice × vector cu greutăți Q8_0 | 18 nov |
| I13 | Un strat întreg de transformator | 18 nov |
| **I14** | **Un simbol întreg Kronos calculat pe placă, identic cu procesorul** | **19 nov** |

Pe 19 nov, la primul ciclu complet automat, toți pașii I0 → I14 au trecut fără niciun om la calculator. Din acel moment trec la fiecare test.

## 5.3 Programele pentru placă

**22 de programe de calcul** sunt scrise de noi în GLSL (compute) și compilate cu compilatorul open-source Mesa NAK în codul mașină al cipului (SM 8.6). Fiecare are suma SHA-256 fixată și un „oracol” pe procesor, adică același calcul făcut pe procesor ca să se compare rezultatul:

- adunări;
- copiere de memorie;
- înmulțiri matrice × vector în mai multe variante (simplă, cu memorie partajată, vectorizată, Q8_0, Q8_0 „lipită”);
- tabela de intrare;
- atenția;
- GELU;
- LayerNorm (o variantă nouă cu 256 de fire, barieră și `shfl`);
- argmax pe placă;
- înmulțire cu circuitele speciale (tensor cores, 16×16, f16 și s8). Aceasta e pregătită doar în SIMULARE; primul test pe placă e aprobat.

Kronos #513 rulează ca o **listă de 87 de lansări pe simbol**, pornită de la 196. Lansările sunt „lipite” (mai multe calcule într-un singur program), iar memoria pașilor anteriori (cheile și valorile atenției) e păstrată pe placă.

## 5.4 Testarea

- **662 de teste unitare** în Rust, cele mai multe pe un **model software al plăcii** (`gpu-sim`): procesorul de comenzi, un GSP fals, un RM fals, memoria video, ROM-ul și jurnalele observate pe placa reală. Orice cod se probează întâi acolo, cu eticheta SIMULARE.
- **Ciclul automat de test pe placa reală**, din 19 nov, fără om la calculator:
  1. un fișier-semnal pe Windows;
  2. un paznic pe Windows verifică că nu rulează nicio antrenare și că e un singur stick, apoi repornește calculatorul o singură dată pe stick;
  3. sistemul de operare propriu verifică două chei puse de proprietar, rulează testul și urcă singur raportul și jurnalul complet (~4.500 de rânduri);
  4. calculatorul revine singur în Windows. Un ciclu durează ~10–15 minute.
- Placa poate fi readusă la starea inițială din interiorul sistemului (resetare PCIe FLR), fără repornirea calculatorului. MĂSURAT: placa răspunde după 0,13 s, iar lanțul complet trece a doua oară în aceeași pornire.
- Tabloul de bord al plăcii, citit prin GSP-RM: temperatura, frecvențele, starea de performanță (P0–P8), puterea. MĂSURAT pe 21 nov: 35,8 °C, 25,2 W din limita de 290 W.
- Viteza maximă a plăcii, cerută oficial prin GSP-RM: placa urcă din starea P5 în P0. MĂSURAT.

## 5.5 Mărimea codului driverului

| Parte | Linii Rust |
|---|---|
| `nvidia-ga104` (cipul: pornirea, GSP, canalele, Kronos pe placă, viteza) | 54.552 |
| `gpu-sim` (modelul software al plăcii) | 6.651 |
| `nvidia-rm570` (structuri **generate automat** din antetele NVIDIA MIT) | 6.119 |
| `gpu-compute` (tensori, operatorii Kronos, oracolul pe procesor, primele bucăți de antrenare) | 5.370 |
| `gpu-pci`, `gpu-core`, `gpu-memory`, `gpu-command` | 3.726 |
| **Total** | **~74.400** |

Plus 22 de programe GLSL. Documentație: 111 fișiere, ~10.400 de rânduri. 307 modificări salvate.

# 6. Rezultatele pe placa reală (MĂSURAT)

## 6.1 Corectitudinea

La fiecare test, cele 16 simboluri generate pe placă sunt **identice** cu cele calculate pe procesor de motorul sistemului. Fiecare simbol e verificat în nucleu, după placă. Abaterea maximă a logit-urilor față de procesor e ~1,7e-5.

Textul generat de #513 pornind de la „Buna ziua”: `, / Imi doresc sa ma intorc la mine, / Sa ma`

Simbolurile: `[44, 10, 73, 2524, 10766, 1438, 1505, 1428, 1765, 99, 1547, 3644, 44, 10, 15879, 1505]`.

## 6.2 Viteza, test cu test

Modelul e #513, textul „Buna ziua”, iar „media cu driverul” cuprinde tot drumul: placa, driverul și jurnalul.

| Data și ora | Versiunea | Ce s-a schimbat | Simboluri pe secundă, media cu driverul | Doar placa |
|---|---|---|---|---|
| 19 nov | os-307 | primul ciclu automat, I0–I14 | (corect, viteza nemăsurată ca medie) | — |
| 20 nov 08:07 | os-313 | jurnal rapid | **21,54** | — |
| 20 nov 15:31 | os-322 | viteza maximă cerută oficial (P5 → P0) | **94,84** (prima dată peste procesor: 72,72) | 381,98 |
| 21 nov 11:01 | os-324 | „dieta driverului” (driverul pe simbol: 3.081 → 1.347 µs) | **109,11** | — |
| 21 nov 12:56 | os-328 | calcule lipite (196 → 88 de lansări pe simbol) | 120 (mediana 304,5) | 413 |
| 21 nov 15:56 | os-329 | fără scrieri pe stick în timpul generării | **262,04** | 413,56 |
| 21 nov 17:26 | os-331 | LayerNorm nou (~21,8 → ~4 µs pe lansare) | **348,47** | 506,88 |
| 21 nov 19:16 | os-332 | prima poziție „încălzită” în afara ceasului | **351,39** (nicio poziție lentă) | 507,15 |

Împărțirea timpului pe un simbol (os-332, mediana): **placa 1.977 µs + driverul 818 µs + jurnalul 61 µs = 2.884 µs**. Din timpul plăcii, înmulțirile iau cel mai mult: fc 487, proj 405, qkv 381, atenția 251, capul de ieșire 186 µs.

Copierea în memoria video: 281.194 MB/s, adică 92,4 % din plafonul teoretic al plăcii de 608 GB/s.

## 6.3 Comparația cu Windows: ce e corect și ce nu

| Unde | Simboluri pe secundă |
|---|---|
| Procesorul, sistemul nostru (motor propriu Rust, 36 de fire) | 72,72 |
| Procesorul, Windows, PyTorch, FP32 | 41,74 |
| Placa video, Windows, driverul NVIDIA + PyTorch, FP32, **fără memoria pașilor** | 129,12 (FP16: 128,84) |
| **Placa video, sistemul nostru, driverul nostru** | **351,39** (doar placa: 507,15) |

**Limitele comparației:**

- **Felul de rulare diferă.** Măsurătoarea din Windows folosește codul Kronos de antrenare, care la fiecare simbol nou recalculează tot textul de la început (fără memoria pașilor, „KV cache”). Motorul nostru păstrează memoria pașilor pe placă.
- **Raportul nu măsoară driverele.** „De 2,7 ori” compară cum rulează Kronos azi în Windows cu cum rulează în sistemul nostru. Nu compară cel mai bun PyTorch posibil cu driverul nostru. O implementare PyTorch cu memoria pașilor ar fi foarte probabil mult mai rapidă decât 129. Nu a fost măsurată.
- **Prima poziție e scoasă din ceas.** În 351,39 nu intră pregătirea primei poziții (15,5 ms, o dată pe text, în afara ceasului; e asemănătoare cu citirea textului dat).
- **LayerNorm nou rulează încă la cerere.** A trecut de două ori, dar nu e varianta implicită.
- **Corectitudinea e aceeași în ambele cazuri.** Toate variantele dau exact aceleași 16 simboluri.

# 7. Cum s-a lucrat (organizarea)

- **Un singur om, Adrian:**
  - decide ce se face și în ce ordine;
  - aprobă explicit fiecare pas riscant (de exemplu primele scrieri în placă, ciclul automat, circuitele speciale);
  - pune cheile pe stick;
  - rulează testele cu placa când e nevoie de el.
- **Agenți AI de programare scriu codul.** Lucrează în sesiuni care pornesc automat, din oră în oră și zi și noapte:
  - sistemul de operare: de două ori pe oră;
  - driverul: o dată pe oră;
  - supraveghetorul Kronos: de 8 ori pe zi.

  Fiecare sesiune citește starea lăsată de cea dinainte, ia sarcina următoare, o implementează, o testează, salvează și scrie ce a făcut.
- **Un centru comun de coordonare** (un depozit separat), cu 1.696 de modificări salvate:
  - comenzile lui Adrian, numerotate (C-1 … C-162);
  - deciziile, cu data și citatul lui;
  - starea fiecărui proiect și jurnalele;
  - rezultatele fiecărui test pe hardware (47 de dosare de rezultate);
  - predările de lucru între proiecte;
  - coada testelor pe placă;
  - un semn „ocupat / liber” pe proiect, ca sesiunile să nu se calce una pe alta.
- **Un „centru de comandă”** (asistentul AI din conversația cu Adrian):
  - ține coada testelor;
  - pune versiunile pe stick și verifică sumele SHA-256;
  - pornește testele;
  - citește jurnalele și scrie verdictele;
  - raportează lui Adrian.
- **Regulile de cinste ale proiectului:**
  - nimic nu e declarat „merge pe placă” fără jurnalul testului;
  - pragurile se scriu înainte de test;
  - un singur lucru nou pe test;
  - rezultatele negative se păstrează;
  - sursa fiecărei idei luate din proiecte open-source e notată (clean-room).
- **Licența:** codul nou e proprietar („toate drepturile rezervate”). Versiunile vechi ale sistemului de operare, până la un anumit punct, au rămas sub licența MIT.

**Total, cele trei proiecte:**

- ~131.700 de linii Rust (sistemul de operare + driverul);
- ~71.000 de linii Python (Kronos);
- 22 de programe GLSL;
- ~63.500 de rânduri de documentație tehnică;
- ~1.900 de modificări salvate în cod, plus 1.696 în centrul de coordonare;
- 7 săptămâni.

# 8. Ce urmează (aprobat, încă nefăcut)

1. **Motorul de antrenare propriu**, aprobat pe 21 nov ca lucru principal. Antrenarea lui Kronos trece din PyTorch/Windows în sistemul propriu, pe placa video, prin driverul propriu. Pașii:
   1. aceleași numere ca PyTorch pe „pasul de aur”;
   2. programele „înapoi” pe placă;
   3. viteza, cu circuitele speciale.

   Stadiul: studiul e gata, iar calculul de verificare pe procesor e în lucru.
2. **Circuitele speciale (tensor cores)**: primul calcul pe placa reală e aprobat. Programul există și trece în SIMULARE.
3. **Lanțul pe placă**: placa pornește singură calculul următor, fără procesorul între calcule. E aprobat, în 3 trepte, fiecare cu test separat.
4. A doua „dietă” a driverului (estimat de la 818 la ~330–410 µs pe simbol, DEDUS); argmax pe placă; modelul mare #651 pe placă (estimat ~5,1–5,6 ms pe simbol, DEDUS).
5. Discul propriu: modele și jurnale pe o partiție a sistemului. E doar pregătit; nimic nu se scrie încă pe discurile workstation-ului.

# 9. Ce NU există încă (pentru o evaluare corectă)

- **Driverul video:**
  - funcționează pe **un singur model de placă** (GA104, RTX 3070 Ti);
  - pe placa laptopului (GA106) doar citește;
  - nu are grafică (ecran, accelerare 2D/3D), doar calcul;
  - depinde de firmware-ul semnat NVIDIA 570.144.
- **Antrenarea lui Kronos** se face încă în Windows, cu PyTorch. Motorul de antrenare propriu abia a început.
- **Kronos e un model mic** (98–183 milioane de parametri). Face greșeli de fapte și nu e comparabil cu modelele comerciale mari.
- **Sistemul de operare:**
  - Wi-Fi doar citit, fără conectare;
  - nu scrie pe discurile interne ale workstation-ului;
  - aplicațiile sunt de bază;
  - nu e gândit pentru mai mulți utilizatori;
  - a rulat pe 3 calculatoare.
- **Comparația cu Windows are limite** (secțiunea 6.3). Viteza față de cea mai bună implementare PyTorch posibilă pe aceeași placă nu a fost măsurată.
- **Lucrul a fost făcut de agenți AI** sub conducerea unui om care nu programează. Pentru o evaluare a costului de înlocuire, evaluatorul trebuie să decidă cum socotește această parte.
