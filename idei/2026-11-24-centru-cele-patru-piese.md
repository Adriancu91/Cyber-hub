# Cele patru piese ale noastre: ce câștigăm de la fiecare și ce câștigăm doar pentru că sunt toate ale noastre

- **Propus de:** centrul de comandă · **Data:** 2026-11-24
- **Proiecte implicate:** `cyber-universe`, `cyber-gpu`, `kronos`
- **Stare:** aprobat (Adrian, 24 nov 17:35: „Da” la H1, H2, H3 — vezi DECIZII.md; comenzile C-163, C-164, C-165)

## Ideea (pe înțelesul lui Adrian)
OS-ul, driverul, motorul de antrenare și Kronos sunt scrise de noi. Fiecare aduce câte puțin singur; câștigul mare e la **îmbinări**:
lucruri care cer ca două-trei piese să fie schimbate deodată, ceea ce nimeni care stă pe Windows + driverul NVIDIA + PyTorch nu poate face.
Mai jos: ce limite au ceilalți, ce putem noi, și cât cred că aduce (tot ce e cifră de câștig e DEDUS, nu măsurat).

## Ce limite au ceilalți și noi nu
| Piesa lor | Limita | La noi |
|---|---|---|
| Windows | ține o parte din memoria plăcii pentru ecran (rețeta Kronos stă sub 7 GB din 8); nu lasă placa să folosească RAM-ul ca prelungire în mod controlat (ori încape, ori se oprește / se târăște) | toată placa e a antrenării; RAM-ul îl împărțim noi |
| driverul NVIDIA | programele de calcul sunt închise și **generale** (bune pentru orice formă de matrice, nu pentru ale noastre); nu se pot lipi pași în interiorul lor | programe scrise exact pe formele lui Kronos |
| PyTorch | fiecare operație e o lansare separată; în Windows nu avem nici varianta lui „compilată” (rețeta noastră nu o folosește — verificat în cod); precizia e aceeași peste tot (bf16) | pasul întreg e un plan fix; precizia se alege pe fiecare bucată |
| modelul lor | e gândit pentru orice placă | Kronos poate fi croit pe placa noastră |

## Ce câștigăm de la fiecare piesă, singură
| Piesa | Ce | Câștig |
|---|---|---|
| **OS** | zero pauze: fără alte programe, fără actualizări, jurnalul în memorie (azi: pasul mic de la 370 ms la 4 ms doar din asta); antrenare zile întregi, cu pază de temperatură și reluare exactă după o pană de curent | mic pe secundă, mare pe săptămână |
| **Driver** | toată memoria plăcii (de cerut: de ce arena e limitată la 6 GiB când Windows folosește 7); placa ținută la viteza maximă; un singur „client” | +5–15 % (lot mai mare) |
| **Motor** | înmulțiri pe tensor cores, numere pe 16 biți în memorie, lot mare (pista A) | de aici vine ajungerea din urmă: 70–110 % din Windows |
| **Kronos** | antrenarea în trepte (bucăți + caiet + ieșire pe eșantion) | ×2–2,5 până la aceeași notă (Muon scos: la noi n-a câștigat) |

## Ce câștigăm doar pentru că sunt TOATE ale noastre (îmbinările)
| # | Îmbinarea | Piese | Ce înseamnă | Câștig (DEDUS) |
|---|---|---|---|---|
| 1 | **Kronos croit pe placă** | AI + motor | Noul Kronos folosește doar piese ieftine pentru placă: ReLU² în loc de GELU, normă simplă (RMS) în loc de LayerNorm, fără „deplasări” (bias), lățimi care se împart exact la plăcile de 64. Pasul rămâne din ~5 feluri de programe în loc de 13. Aceleași alegeri le fac și modelele moderne (deci nu pierdem calitate) | +10–20 % viteză brută |
| 2 | **Programe pe măsură, reglate singure noaptea** | motor + driver + OS | Kronos are doar ~6 forme de matrice. Pentru fiecare, programul se compilează cu mărimile fixe (fără margini, fără ramuri) în mai multe variante; ciclul automat le aleargă noaptea pe placa reală și păstrează cea mai rapidă. NVIDIA nu poate face asta pentru modelul fiecărui client | +10–30 % peste un program general bun |
| 3 | **O singură memorie: VRAM + RAM** | OS + driver + motor | Planul pasului e fix, deci știm dinainte ce bucată trebuie și când: o aducem din RAM cu un pas înainte (legătura de 12–13 GB/s). Stările optimizatorului (jumătate din memoria greutăților) stau în RAM | nu viteză, ci **mărime**: lot mai mare și un Kronos mai mare decât ar încăpea altfel pe 8 GB (cât anume: de măsurat) |
| 4 | **Procesorul lucrează în același pas** | OS + motor + AI | Cele 18 nuclee țin caietul din RAM, optimizatorul și pregătirea lotului următor, în timp ce placa înmulțește. Placa nu așteaptă niciodată | face posibile 3 și caietul; +5–10 % |
| 5 | **Precizie pe trepte** | motor + AI | La început (faza pe bucăți) calcule grosiere, ieftine (16 biți, de încercat 8 biți); la sfârșit calcule fine. PyTorch pe placa asta are o singură precizie | până la +30–50 % în prima fază, dacă proba pe 8 biți iese |
| 6 | **Laborator fără zgomot** | OS + motor | Motorul nostru dă aceiași biți la fiecare rulare. Două variante de antrenare se pot compara pe exact aceleași date și aceeași pornire, deci o diferență mică se vede din prima — Kronos spune că în Windows diferențele sub 0,005 sunt zgomot. Ciclul automat poate încerca variante singur, noaptea | cercetare de câteva ori mai rapidă pe aceeași placă — asta e partea de „se îmbunătățește singur” |

## Socoteala cinstită
- Viteză brută (simboluri/s, aceleași calcule ca Windows): pista A × îmbinările 1, 2 → **cam 0,9–1,5 × Windows**, dacă toate ies.
- Până la aceeași notă la examen: încă ×2–2,5 din trepte → **în total ×2–3 față de Windows de azi** e ținta realistă; ×4 dacă iese și 8 biți.
- Ce Windows nu poate deloc: îmbinarea 3 (un Kronos mai mare decât placa) și 6.

## Ce NU e al nostru (ca să știm unde mai sunt limite)
1. **Firmware-ul plăcii (GSP)** — al NVIDIA, obligatoriu; noi doar îl încărcăm.
2. **Compilatorul programelor de placă (Mesa NAK)** — unealtă liberă, nu a noastră: nu știe bf16, poate nu știe 8 biți, și codul scos e mai slab
   decât al NVIDIA. E veriga cea mai slabă din lanț. Pe termen lung: un generator de cod al nostru pentru cele 2–3 bucle fierbinți
   (a cincea piesă).
3. **Siliciul** — plafonul plăcii rămâne plafon.

„Singurul din lume”: nu cunosc alt proiect mic care să aibă toate patru piesele scrise de la zero. Cel mai aproape e tinygrad (driver și
motor proprii, fără OS și fără model propriu). Nu pot dovedi că nu mai există altul, așa că în prezentări aș scrie „printre foarte puținele”.

## Ordinea propusă
1. **Acum (aprobat deja):** pista A — `mm_train_tile` → tensor cores → umbra pe 16 biți → lotul mare; bancul cinstit Windows ↔ OS.
2. **În paralel, cu „da”:** laboratorul treptelor în Windows — întâi doar bucăți K = 4 față de rețeta de azi, o oră fiecare, același
   examen (`romana_bpb`), cu pre-înregistrare ca la Kronos. Caietul rămâne ultimul (Kronos: e cel mai scump, schimbă formatul modelului).
3. **Apoi, cu „da”:** „Kronos croit pe placă” (îmbinarea 1) + ce a câștigat în laborator = modelul nou care se antrenează de la zero în
   OS-ul nostru („versiunea 1”). #513 și #651 rămân neatinse.
4. **Pe parcurs, cu „da”:** cursa de noapte a programelor (îmbinarea 2) și memoria unică (3 + 4).

## Cele trei hotărâri
- **H1 — laboratorul:** ridicăm pauza C-156 doar pentru antrenări de probă de câte o oră în Windows (întâi 2: rețeta de azi și bucăți K = 4)?
- **H2 — Kronos croit pe placă:** următorul Kronos (de la zero) se proiectează împreună cu motorul (îmbinarea 1 + treptele câștigătoare)?
- **H3 — cursa de noapte:** pe placa reală pot rula într-o noapte mai multe variante de program, dacă fiecare e dovedită în simulare că dă
  aceiași biți și are suma verificată? (Azi regula e „un singur lucru nou pe test”.)

## Decizia lui Adrian
- 2026-11-24 17:35: **„Da”** la H1, H2, H3 (în chat cu centrul de comandă). Limitele exacte: `DECIZII.md`, aceeași dată.

## Discuție
- 2026-11-24 17:50 centru: scris la cererea lui Adrian (17:17). Se sprijină pe `idei/2026-11-24-centru-viteza-peste-windows.md` și
  `idei/2026-11-24-centru-antrenarea-in-trepte.md` (cu corectura despre Muon).
- 2026-11-24 18:53 cyber-gpu: **Limita de 6 GiB nu e în driver**, e o constantă a OS-ului (`cyber-universe/kernel/src/drivers/gpu_i14.rs`, `ARENA_MAX = 6 << 30`, pusă după regula Kronos „sub ~7 GB” pentru Windows). Pe placă, OS-ul a raportat după pornirea driverului **7 474–7 708 MiB VRAM liber** (restul de 8 192 îl țin GSP-RM / firmware-ul). Din driver: arena + zona lansărilor + rezerva de 4 MiB trebuie să încapă în cea mai lungă bucată liberă → **~7,2 GiB posibil** (DEDUS). Dacă regula „sub 7 GB” se aplică și în OS-ul nostru (unde nu mai e alt client pe placă) hotărăște Adrian; urcarea constantei o face sesiunea OS.

## 25 nov — „banda”: ce dă fiecare piesă în același pas (cerut de Adrian 11:41)
Ideea: pe durata unui pas, **nicio piesă nu stă**. Placa înmulțește; tot restul lucrează în paralel ca să n-o lase să aștepte.
| Piesa | Ce dă pe pas (concret) | Stare |
|---|---|---|
| **Driver** | (1) treapta memoriei comune aleasă automat → mai multe echipe pe unitate (os-423: ×1,5–2,7); (2) **motorul de copiere al plăcii** (unitate separată de calcul): urcă lotul următor / coboară rezultate **în timp ce** placa calculează; (3) tot pasul trimis o dată, placa ținută la ceasul maxim | (1) măsurat; (2) de cerut Cyber-GPU; (3) făcut |
| **Motor** | programe pe formele lui Kronos + cursa de noapte; încărcarea dublă în interiorul înmulțirii (`cp.async`, ideea lui Adrian 11:15); precizie pe bucăți (f16/8 biți); „portarul” dacă câștigă (C-167) | parțial |
| **OS** | zero pauze; procesorul (18 nuclee) face **în același timp**: lotul următor, jurnalul, verificările, paza de temperatură; RAM fixată pentru copii fără opriri; reluare exactă după pană; agentul de bord (C-166) urmărește live | parțial; agentul în lucru |
| **Kronos** | croit pe placă (C-164), harta textului (S137), portarul (C-167) — mai puțin calcul pentru aceeași notă | laborator |
| **Unelte** | simulatorul prezice înainte de fiecare test; cursa alege singură varianta; agentul + centrul închid bucla test → rezultat → test următor fără ore pierdute | merge |
Ordinea câștigului: (1) ocuparea în tot pasul → (2) `mm_tc` cu ocupare → (3) copierea în paralel + încărcarea dublă → (4) Kronos croit + portar.
- 2026-11-25 14:15 kronos (supraveghetor): laboratorul — harta (S137) a ieșit „câștig strâmb” (română −0,026, martorul +0,009), bucățile (S135) pierd; portarul (C-167) = S139, în lucru. Până la un câștig curat, rândul „Kronos” din bandă nu cere programe noi de placă.

## 25 nov 15:45 — piesă candidată din schema lui Adrian: „ieșirea pe categorii”
Ghicitul cuvântului următor în doi pași: întâi una din ~128 de categorii, apoi cuvântul din categoria ei (~128) → ~256 de scoruri în loc de 16 384 (ieșirea ierarhică / pe clase; categoriile făcute automat, grupând cuvintele după context). ESTIMARE: −10–15 % din pasul de antrenare, câștig mare la scris. Schimbă modelul → doar în laborator, după „portar”, cu „da” separat al lui Adrian (nepornit).
- 25 nov 15:50 (Adrian): **ghicitul pe rol în propoziție** (dacă lipsește verbul, caut doar printre verbe) = varianta gramaticală a ieșirii pe categorii; **„ghicitorul mic + verificatorul mare”** (decodare speculativă) pentru scris, ×2–3 la chat cu același text. Ambele nepornite, doar cu „da”.
- 25 nov 16:29: **portarul (S139) = „LA FEL”** — română −0,0057 (prag −0,010), martorul în toleranță, viteza ×1,062 în PyTorch. Ne oprim cu el (regula din C-167).
