# Kronos mare pe ce avem (fără placă nouă, fără închiriere): ce e realist și în ce ordine

- **Propus de:** centrul de comandă, la întrebarea lui Adrian (10 nov 2026, 20:11) · **Pentru:** kronos (+ cyber-universe / cyber-gpu la pasul P3)
- **Stare:** propus — așteaptă „da” de la Adrian (se poate aproba pe pași; P4 cere separat „da” la descărcare)

## Întrebarea lui Adrian
„Putem găsi metode mai bune de antrenare, o scurtătură, o soluție nouă — fără să schimbăm placa și fără să închiriem? Care e cea mai bună
metodă să-l antrenăm pe ce avem la 6 miliarde de parametri?”

## Răspunsul scurt
**Zidul e timpul de calcul, nu memoria.** Memoria se poate ocoli; timpul nu (nu se cunoaște nicio metodă care să-l taie de ~100 de ori).

- **Memoria se ocolește:** greutățile și „notițele” optimizatorului pot sta în cei 128 GB de RAM și trec „pe felii” prin placă
  (ZeRO-Offload, 2021: peste 13 mld. de parametri pe o singură placă; MegaTrain, 2026: 100 mld. pe o singură placă de 80 GB cu 512 GB RAM,
  dar la ~95 de simboluri pe secundă). Deci ocolirea memoriei nu aduce viteză.
- **Viteza măsurată la noi** (rapoartele S89/S95): #513 (98 M) citește **39.300** simboluri/s; modelul de 24 de straturi (183 M, cu recalcul)
  **13.170** simboluri/s → placa dă ~1,5–2,3 × 10¹³ operații/s. Viteza scade invers cu mărimea: v ≈ 2,4 × 10¹² / (număr de parametri).
- **Cât text trebuie:** regula din cercetare (Chinchilla) — ~20 de simboluri citite pentru fiecare parametru, altfel mărimea e irosită.

| mărime | viteză estimată | text necesar | timp de antrenare non-stop | încape pe 8 GB? |
|---|---|---|---|---|
| 183 M (acum) | 13.000 simb/s (măsurat) | ~3,7 mld. | ~3 zile (≈ o săptămână de nopți lungi) | da |
| ~0,4–0,5 mld. | ~5.000–6.000 | ~8–10 mld. | ~3–4 săptămâni | da, la limită (Muon + recalcul) |
| ~1 mld. | ~1.800–2.400 | ~20 mld. | ~3–5 luni | doar cu notițele în RAM |
| 6 mld. | ~150–400 | ~120 mld. | **~10–25 de ani** | nu; doar pe felii din RAM |

Reper public: nanochat (Karpathy) — un model de ~4 × 10¹⁹ operații „e cam ca o discuție cu un copil de grădiniță”; pe placa noastră
asta înseamnă ~3–4 săptămâni non-stop.

## Scurtăturile reale (în ordinea câștigului pe efort)
1. **Toate orele plăcii.** Nopțile modelului mare au acum 5 ore; ferestrele permit ~22 h/zi (minus examene și testele lui Adrian) → de ~3–4 ori mai mult.
2. **Pornire de la zero cu rețetă completă, nu doar „crescut + rată mică”.** S89/S95: modelul crescut învață aproape doar la răcire, cu rate
   foarte mici — pare prins lângă #513. Un model de 24 de straturi antrenat de la zero (Muon, încălzire → vârf → scădere) ar folosi mărimea.
3. **Rețeta v2** (idei publice din „speedrun”-urile nanoGPT: același model, aceeași țintă, pe același calculator — 45 de minute în mai 2024 →
   40 de secunde în august 2026): poziții rotative, RMSNorm fără bias, QK-norm, ReLU², cap dezlegat de intrare, fără dropout, Muon.
   Kronos are azi arhitectura clasică (poziții învățate, LayerNorm, GELU, AdamW la nopțile mari). Câștig realist la noi: de ~2–3 ori, **de măsurat**.
   Clean-room: idei publice, cod scris de noi. Cere pornire de la zero **și** adaptarea motorului KGR1 din OS + programele GPU.
4. **Mai mult text românesc.** Amestecul are 1,35 mld. de simboluri (4,89 GB). FineWeb-2 `ron_Latn`: 54,1 milioane de documente, 81,3 GB
   (ODC-By; am folosit o felie de 3 GB dintr-un fișier). Fără text mult mai mult, un model mai mare doar memorează.
5. **Creștere treptată** (dovedită la noi: 12 → 24 de straturi cu ieșiri identice) — în literatură economisește ~20–50 %; merge mai bine făcută
   devreme, cât rata e mare, nu după ce modelul s-a așezat.
6. **Notițele în RAM** — starea optimizatorului și greutățile fp32 în RAM, pe placă doar copia bf16 și activările → plafonul urcă de la
   ~0,4 la ~1–2 mld. Nu aduce viteză, doar loc.
7. **Memorie în loc de parametri** — faptele stau într-o bază de date / în texte căutate (RAM și disc, din care avem mult), iar Kronos citește
   și răspunde (exact ce face deja bine #513 la R1/R2). Legătură: C-85 punctul 6 și modulul de fapte din Mini Brain.

## Ce NU propun
- 6 mld. „dens” pe placa asta (zeci de ani). Nici pe o singură placă de top n-ar ieși într-un timp rezonabil.
- „6 mld. pe cutie” prin experți (MoE: doar o parte din parametri lucrează la fiecare simbol): calcul și calitate ca la ~1 mld.; complexitate mare.
- Distilare de la un AI mare — cea mai mare scurtătură cunoscută, dar exclusă de decizia „de la zero, fără alt AI”.
- Antrenare pe procesor — de ~20 de ori mai lentă decât placa.

## Ordinea propusă
- **P1 (acum, fără risc):** modelul de 24 de straturi **de la zero**, cu Muon și program de rată complet, pe amestecul actual, ~7 nopți lungi
  (~3,7 mld. simboluri); judecat pe examenul de română față de #513. Dacă îl bate clar → mărimea ajută, mergem mai departe. Dacă nu → frâna e
  la date/rețetă, nu la mărime.
- **P2 (în paralel, pe modele mici, ziua):** rețeta v2, pre-înregistrată, fiecare alegere verificată la 2 mărimi (lecția S94b), judecată pe română (bpb).
- **P3 (doar după I14 pe placa reală):** decizia „Kronos v2 de la zero” + adaptarea motorului din OS. Nu mutăm ținta cât lanțul GPU se sprijină pe
  forma lui #513. Dacă se face, e momentul natural și pentru tokenizerul românesc (C-89 — parcat de Adrian; rămâne decizia lui).
- **P4 (cu „da” la descărcare):** mai mult text românesc (FineWeb-2), cu loc pe disc pentru text + simboluri.
- **P5:** ~0,4–0,5 mld. (3–4 săptămâni) → **P6:** ~1 mld. cu notițele în RAM (3–5 luni) → amintirea din `AMINTIRI.md` (C-89).

## Riscuri
- Ce merge pe model mic nu merge sigur pe mare (S94b). · Placa e împărțită cu testele OS/GPU. · Lucru non-stop: ~10 kWh/zi și căldură (limitele
  plăcii rămân). · Estimările de timp sunt calcule, nu măsurători; P1 le verifică pe primele.

## Surse
- ZeRO-Offload: https://www.usenix.org/conference/atc21/presentation/ren-jie
- MegaTrain: https://dev.to/onsen/megatrain-train-100b-llms-on-a-single-gpu-9ea
- NanoGPT speedrun (Epoch AI): https://epoch.ai/data/nanogpt-speedrun-record-time
- nanochat: https://cdn.jsdelivr.net/gh/karpathy/nanochat@master/README.md
- FineWeb-2: https://huggingface.co/datasets/HuggingFaceFW/fineweb-2

## Discuție
- 2026-11-10 20:11 Adrian: întrebarea de mai sus. Centrul de comandă: analiza + propunerea; nimic nu pornește fără „da”.
- 2026-11-10 23:15 kronos (supraveghetor): de acord cu diagnosticul — modelul crescut de 24 e plat la continuări (S89/S95 AdamW pe loc, S94 rata mare strică, S99 Muon ×400 strică din prima oră). În noaptea asta doar o probă scurtă Muon ×20 (S100, în granițele mele); dacă nici ea nu mișcă modelul, P1 (de la zero, rețetă completă) e pasul firesc. P1 e o rulare lungă nouă (~7 nopți) → intră în coadă doar cu „da”-ul lui Adrian.
- 2026-11-11 02:15 kronos (supraveghetor): S100 (Muon ×20, 2 h) = LA FEL — 1,2055 față de 1,2039 la pornire: nu strică, dar nici nu mișcă. Toate rețetele de continuare pe modelul crescut de 24 sunt încercate → P1 e pasul următor. L-am pus în coada Kronos ca **S101, propus — necesită Adrian**; pornește doar după „da” (COMENZI.md sau „aprobat” aici).
- 2026-11-11 11:15 kronos (supraveghetor): luat la cunoștință C-101 — P1/S101 nu deocamdată; S101 e `oprit — nu deocamdată` în coada Kronos. Între timp S98 a ieșit DA (datele pe bucăți pornesc cu 550 MB în loc de 41,7 GB), iar S102 face bucățile direct din text — utile pentru orice plan cu date mai multe.
