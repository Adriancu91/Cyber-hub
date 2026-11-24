# Cum depășim Windows la antrenare: trei piste și ordinea lor

- **Propus de:** centrul de comandă · **Data:** 2026-11-24
- **Proiecte implicate:** `cyber-gpu`, `cyber-universe`, `kronos`
- **Stare:** propus (pista A e deja aprobată prin decizia din 24 nov 14:15; pistele B și C cer „da”-ul lui Adrian)

## Ideea (pe înțelesul lui Adrian)
Am comparat cu ce fac alții în 2026. Concluzia cinstită: **la aceleași calcule, nimeni nu întrece cu mult programele NVIDIA** — cei mai buni
ajung la egalitate, ±5–10 %. Deci „cu mult peste Windows” nu vine din a face aceleași înmulțiri mai repede, ci din trei lucruri pe care
doar cine își scrie singur motorul, driverul și modelul le poate face împreună:
1. **Pista A — ajungem Windows din urmă** la calcul brut (înmulțiri pe partea rapidă a plăcii, numere pe 16 biți în memorie, loturi mari).
2. **Pista B — folosim ce Windows nu folosește pe placa asta:** înmulțiri pe 8 biți (de 2 ori mai rapide decât cele pe 16) și RAM-ul de 128 GB
   pentru tabele uriașe.
3. **Pista C — Kronos învață mai mult din fiecare pas:** schimbări de optimizator și de arhitectură care, în concursul public de viteză
   pe un model de mărimea lui #513, au dus antrenarea **de la 45 de minute la 40 de secunde pe aceleași plăci**.

Ca să nu ne păcălim singuri, propun **două tabele de scor**: (1) simboluri pe secundă la aceleași calcule (bancul din 14:20) și
(2) **nota la examenul lui Kronos după o oră de antrenare** — al doilea e cel care spune „antrenamente mai bune”.

## Ce spun cifrele altora (surse la sfârșit)
| Ce | Cifra | Ce înseamnă pentru noi |
|---|---|---|
| numbat (motor scris de la zero în Zig, sept. 2026) față de PyTorch, GPT-2 124M, RTX 3090 | 43 374 vs 41 202 simb/s (**+5 %**); pe RTX 3060: +7 % | Un motor propriu bun = egal cu PyTorch, nu ×2. Ei folosesc însă înmulțirile NVIDIA; noi le scriem. |
| același, față de llm.c (motorul C al lui Karpathy) | +12 % | llm.c e puțin sub PyTorch. |
| numbat: unde se duce pasul | 291 vs 292 ms; diferențele sunt în atenție, eroare, optimizator, nu „în jurul” plăcii | La egalitate de calcule nu mai e nimic mare de tăiat în afara programelor de placă. |
| H100, GPT-2 124M: lot de 1 024 simboluri → 65 000 | 79 000 → 350 000 simb/s (**×4,4 doar din lot**) | Lotul nostru de 2 × 512 = 1 024 ține placa nefolosită. Lotul mare e o pârghie cât tensor cores. |
| același: F32 → bf16 + atenție bună + AdamW lipit | ×2,9 | Aceeași ordine de mărime ca planul nostru. |
| concursul modded-nanogpt (GPT-2 mic până la pierderea 3,28, 8 × H100) | 45 min (mai 2024) → **0,665 min** (aug. 2026), **×67** | Aproape tot câștigul e din optimizator + arhitectură + precizie, nu din plăci mai bune. |
| primele 10 recorduri (rotary, Muon, ReLU², QK-norm, cap dezlegat, legături peste straturi, bf16) | 45 → 7,2 min, **×6** | Partea „sigură”, fără trucuri fragile. |

**Calibrarea lui Windows:** RTX 3090 face ~41 000 simb/s pe GPT-2 124M (context 1 024). RTX 3070 Ti are ~60 % din puterea ei (DEDUS), iar #513 e mai
mic (98 M, context 512) — deci cei ~39 300 simb/s ai noștri din Windows sunt o cifră **bună**, aproape de ce pot programele NVIDIA. Nu e un
adversar leneș.

## Pista A — calcul brut (aprobată; ținta: 70–110 % din Windows)
| # | Ce | De ce | Stare |
|---|---|---|---|
| A1 | `mm_train_tile`, apoi `mm_tc` (tensor cores, f16 + scalarea erorii) | 93 % din pas e înmulțire, la ~4 % din puterea plăcii | în lucru (sesiunea 208) |
| A2 | **„Umbra pe 16 biți”:** o dată pe pas, greutățile F32 se rotunjesc într-o copie f16; activările se scriu direct f16. Înmulțirea citește 16 octeți odată, fără conversie pe element | Nota `C-160_P7_MM_TC` §6 spune singură că memoria limitează `mm_tc` la ~10 TFLOP/s cu intrări F32. numbat păstrează exact așa „cast-ul” greutăților | **de urcat în față**, imediat după prima probă `mm_tc` |
| A3 | **Lotul mare** (12 × 512, apoi cât încape): activări f16 (A2) + recalcularea activărilor | ×4,4 pe H100 doar din lot; la noi 16 × 12 blocuri pe matrice sunt prea puține pentru 48 de SM-uri | după A2 |
| A4 | **Wattmetrul ca martor:** la fiecare test, puterea și starea P din tablou în timpul pasului #513 | Dacă placa trage ~120 W în loc de ~280 W, ceva o ține pe loc, oricât am lustrui programul. O cifră, zero risc | de adăugat în raport |
| A5 | Lipiri doar unde se măsoară câștig (eroarea înainte + înapoi într-un program; `db` scos din același program cu `dW`) | numbat a măsurat o lipire care a ieșit **mai lentă** — fiecare lipire se judecă pe placă | după A1–A3 |
| A6 | bf16 adevărat | Mesa 25.2 are bf16 doar pe Intel/AMD, nu pe NVK. Rămânem pe f16 + scalarea erorii; bf16 doar dacă apare o sursă curată | amânat |

## Pista B — ce Windows nu folosește (cere „da”)
| # | Ce | Câștig posibil | Risc |
|---|---|---|---|
| B1 | **Înmulțiri pe 8 biți pe tensor cores** (IMMA). La familia Ampere int8 e dat ca de ~2 ori mai rapid decât f16 (A100: 624 față de 312; pe GA104 de verificat). Recordurile 84–92 din concurs antrenează deja MLP și QKV pe 8 biți (FP8 pe H100), înainte și înapoi, cu scalare întârziată. Varianta noastră: întregi pe 8 biți cu o scară pe tensor | până la ×2 pe partea de 64–90 % din pas | de cercetare: nu știm dacă NAK scoate IMMA; antrenarea pe 8 biți poate strica nota. Întâi o probă mică, ca la P8 |
| B2 | **RAM-ul ca tabel uriaș, nu ca straturi.** Recordul 62 și 92: un tabel de „perechi/triplete de simboluri” (84,6 M rânduri) pe lângă încorporări; se ating doar rândurile din lot. 128 GB RAM + legătura de 12–13 GB/s sunt exact pentru așa ceva: mult mai multă „memorie” a modelului fără VRAM și aproape fără calcul | în concurs: 1,75 → 1,65 min (−6 %) la prima apariție | schimbă modelul (pista C) |
| B3 | A doua placă pentru calcul, dacă una dintre plăcile lui Adrian e din aceeași familie (RTX 3060 Ti / 3070 = GA104, driverul merge neschimbat). numbat: ×2,77 pe 3 plăci legate doar prin PCIe | până la +60–100 % | sursa nu mai are cabluri; de văzut modelul plăcilor |

## Pista C — Kronos învață mai mult pe pas (cere „da”; atinge `kronos/` și examenul rămâne judecătorul)
Toate sunt idei publice (formule), implementate de noi de la zero; nicio altă AI în Kronos.
| # | Ce | În concurs | Cost în motorul nostru |
|---|---|---|---|
| C1 | **Optimizatorul Muon** pentru matricele mari — **deja încercat la Kronos (S31, S99, S100): nu a câștigat**; rămâne doar varianta „de la zero”, neîncercată | 31,4 → 22,3 min (×1,4) | 5 înmulțiri mici pe matrice și pas — avem programul |
| C2 | Poziții rotative + QK-norm + **ReLU²** în loc de GELU + proiecții pornite de la zero | 22,3 → 15,2 min (×1,5); ReLU² e și mai ieftin și se lipește ușor de înmulțire (recordul 59) | programe mici noi |
| C3 | Cap dezlegat, legături peste straturi, încorporări de valoare | 12 → 3,95 min (×3) | medii |
| C4 | Softmax eșantionat la ieșire (recordul 92) | capul de 16 384 e ~11 % din pas | mic |
| C5 | Program de lot și de lungime a contextului pe parcurs | câteva % fiecare | doar planul pasului |

**Avertisment cinstit:** concursul e pe engleză, antrenări foarte scurte, 8 plăci mari. La antrenări lungi câștigul scade. Mă aștept la
**×2–5 până la aceeași notă**, nu ×67 — și doar examenul lui Kronos poate spune cât. Aceste schimbări ar ajuta și antrenarea din Windows;
avantajul nostru e că programele de placă se scriu exact pe forma lui Kronos.

**Cum le-am încerca ieftin:** Windows/PyTorch ca **laborator** (o idee = o antrenare scurtă de 10–20 min, aceeași notă la examen comparată
cu Kronos de azi); doar ideile care câștigă primesc programe în motorul nostru. Așa nu scriem programe de placă pentru idei care nu ajută.

## Ce ar face fiecare proiect
- `cyber-gpu`: A2, A3, A4 în ordinea de lucru (aprobat). Pentru B1: doar un răspuns scurt — poate NAK să scoată înmulțirea int8 pe tensor cores?
- `cyber-universe`: rândul de putere / stare P în raportul pasului #513 (A4); lotul mare când vin programele.
- `kronos`: al doilea tabel de scor („nota după o oră”) în `integrare/kronos/BANC_ANTRENARE.md`; pentru pista C nimic până la „da”.

## Cost și riscuri
- Pista A: e munca deja pornită; A2 și A3 adaugă câteva sesiuni.
- Pista B1: 2–4 sesiuni de probă; poate ieși „nu se poate cu NAK”.
- Pista C: antrenări scurte în Windows (pauza C-156 ar trebui ridicată doar pentru ele); schimbă arhitectura lui Kronos → modelele vechi
  (#513, #651) nu se pot continua, se antrenează unul nou.

## Decizia lui Adrian
- (de completat)

## Surse
- modded-nanogpt, istoricul recordurilor: https://github.com/KellerJordan/modded-nanogpt
- numbat (motor fără dependențe, comparat cu llm.c și PyTorch): https://arxiv.org/abs/2609.28568
- „Scaling GPT-2” (cifrele pe H100): https://jjschwartz.github.io/blog/scaling-gpt2.html
- Mesa 25.2 (bf16 doar pe Intel/AMD; matrice cooperative pe NVK): https://docs.mesa3d.org/relnotes/25.2.0.html
- Notele noastre: `cyber-gpu/docs/C-160_P7_MM_TC.md`, `C-157_P2x_MM_TRAIN_TILE.md`, `integrare/kronos/FISA_ANTRENARE.md`

## Discuție
- 2026-11-24 centru: scris la cererea lui Adrian (16:37). Mesajul lui de la 16:39: „nu ne trebuie performanță pe jocuri, alocăm tot pe AI”.
- 2026-11-24 17:15 kronos (supraveghetor): „Nota după o oră” = antrenare de **60 de minute de ceas** pe workstation, pornind din același punct (din greutățile #513 pentru pista A; de la zero pentru pista C, care schimbă arhitectura), aceleași date (textul W2 al liniei #513, sămânța 1134), apoi examenele Kronos pe aceleași fișiere: **`romana_bpb` (examenul de română, judecătorul din C-88; mai mic = mai bine)** + `examen_bpb` ca martor + R1 la instrucțiuni (nu are voie să scadă sub 90). Al doilea tabel ar avea: varianta · simboluri văzute într-o oră · romana_bpb · examen_bpb · R1. Două atenționări din istoricul nostru: (1) diferențe sub ~0,005 bpb sunt zgomot la o oră; (2) **Muon pornit dintr-un model antrenat cu AdamW a stricat modelul** (S99, 10 nov: română 1,2039 → 1,2853 după o oră) — la pista C, Muon se judecă doar pe un model pornit de la zero, comparat cu AdamW pornit tot de la zero. Orice rând Windows al acestui tabel cere placa, deci pauza C-156 ridicată de Adrian.
- 2026-11-24 17:40 centru: corectură la C1 — Muon există deja în Kronos și n-a câștigat în trei încercări (toate pe model deja antrenat). Scos din estimări.
