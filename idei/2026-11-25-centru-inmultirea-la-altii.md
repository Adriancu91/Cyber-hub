# Cum fac alții înmulțirea și ce ne lipsește nouă: ocuparea unităților de calcul

- **Propus de:** centrul de comandă (cerut de Adrian, 25 nov 06:40: „ne uităm la alții cum fac înmulțirile, luăm idei, rescriem”) · **Data:** 2026-11-25
- **Proiecte implicate:** `cyber-gpu`, `cyber-universe`
- **Stare:** de lucru în pista A (aprobată 24 nov 14:15). Doar idei și cifre publice; niciun rând de cod copiat.

## Ideea (pe înțelesul lui Adrian)
Am comparat programul nostru de înmulțire cu cel mai cunoscut studiu public (siboehm, „SGEMM de la zero”). **Folosim deja aceeași rețetă
ca el** (plăci de 128 × 128, 8 × 8 pe fir) — dar el scoate cu ea ~41 % din puterea plăcii, iar noi ~9 %. Deci nu rețeta e buba.
Buba cea mai probabilă: **la noi lucrează o singură echipă de fire pe fiecare unitate de calcul a plăcii, când ar încăpea 2–6.**
Driverul NVIDIA (CUDA) rezervă automat, la fiecare lansare, destulă „memorie comună” pe unitate ca să încapă cât mai multe echipe.
Driverul nostru rezervă minimul — exact cât îi trebuie unei singure echipe (așa face și driverul liber NVK, după care ne-am luat).
E un singur număr din descrierea lansării.

## Dovezile (din cifrele noastre + surse publice)
| Fapt | Sursa |
|---|---|
| Aceeași rețetă (2D blocktiling, 128×128, BK 8, 8×8 pe fir): 15 971 GFLOP/s pe RTX A6000 = ~41 % din vârful ei F32; cuBLAS 23 250 | siboehm, tabelul de rezultate |
| Noi, `mm_tv_128x128`: ~2,0 TFLOP/s din ~24 (la 1 950 MHz) = ~8–9 % | os-416, os-418 |
| „Memoria comună folosită pe bloc limitează câte blocuri stau deodată pe o unitate”; driverul CUDA alege singur capacitatea „ca să evite gâtuirea de ocupare” | ghidul de programare CUDA; forumul NVIDIA (blocuri = capacitatea aleasă ÷ memoria comună a unui bloc) |
| La noi: `qmd.rs` pune `MIN = TARGET_SM_CONFIG_SHARED_MEM_SIZE` = treapta cea mai mică ≥ memoria **unui** bloc (8 KiB pentru 8 KiB) | `cyber-gpu/crates/nvidia-ga104/src/qmd.rs`, `sm_config_shared_units` |
| Programul cu 4 KiB (`64x64k8`, încap 2 în 8 KiB) e de 1,6 ori mai rapid decât martorul cu 8 KiB (încape 1), deși fac aceeași treabă pe fir | os-417: 2,04 față de 1,27 TFLOP/s |
| Variantele cu 12 KiB (treapta 16 KiB → tot 1 bloc) nu câștigă nimic, deși fac de 2 ori mai mult pe fir | os-416: 1,33 față de 1,27 |
| Placa trage 123–133 W din 290 în timpul pașilor, la ceasul maxim, fără nicio frână; în gol ~77 W | os-414, os-418: ~20–25 % din puterea de lucru ≈ 8 fire-grup din 48 (17 %) |

**DEDUS, nedovedit:** înțelesul exact al câmpurilor `MIN/TARGET/MAX_SM_CONFIG_SHARED_MEM_SIZE` îl deduc din nume, din ghidul CUDA și din
cifrele de mai sus. Proba de mai jos îl confirmă sau îl infirmă într-un singur test.

## Câte blocuri ar încăpea (socoteală: 65 536 registre și 1 536 fire pe unitate, DEDUS din fișele publice)
| Program | fire | registre | memorie comună | azi | cu treapta potrivită | limita |
|---|---|---|---|---|---|---|
| `mm_train_tile` | 256 | 34 | 8 KiB | 1 bloc | **6 blocuri** (treapta 64 KiB) | firele |
| `mm_tv_64x64k8` | 256 | 34 | 4 KiB | 2 | **6** (treapta 32 KiB) | firele |
| `mm_tv_128x128` | 256 | 90 | 8 KiB | 1 | **2** (treapta 16 KiB); **3 dacă scade la ≤ 85 de registre** | registrele |
| `mm_tc` | 128 | ? | 24 KiB | 1 (4 grupuri de fire din 48!) | 2 (64 KiB) / 4 (96 KiB) | memoria comună |
| atenția pe plăci, programele de scris (`q8_fused`…) | — | — | — | probabil 1 | de socotit | — |

## Ce propun, în ordine (toate în pista A)
1. **Proba ocupării (un singur lucru nou pentru placă: valoarea treptei în descrierea lansării).** Același `mm_train_tile` (biți cunoscuți),
   pe forma qkv, lansat cu treapta 8 → 16 → 32 → 64 KiB (`MIN = TARGET`), apoi `mm_tv_64x64k8` la 8 → 32 și `mm_tv_128x128` la 8 → 16.
   Verdict: aceiași biți; cifra: TFLOP/s și puterea pe fiecare treaptă. Niciun registru, nicio comandă nouă — doar alt număr într-un câmp
   pe care îl scriem deja; `MAX` e deja 64 KiB.
2. **Dacă se confirmă:** treapta aleasă automat de driver = cea care dă cele mai multe blocuri (ca CUDA), **aceeași pe tot pasul** (schimbarea
   treptei între lansări cere unitatea goală — de evitat între cele 385 de lansări). Se aplică și atenției și programelor de scris.
3. **Dieta de registre la `128x128`:** ≤ 85 de registre → 3 blocuri în loc de 2.
4. **`mm_tc` / `mm_tc128` cu memorie comună mai mică pe bloc** (azi 24 KiB): altfel circuitele speciale rulează cu 4 grupuri de fire pe unitate.
5. Din același studiu, mai târziu: citiri de 128 de biți (+14 % la el), bucla K desfăcută cu `BK` fix și mărimi fixe pe formă (fără
   verificări de margine), plăci pe grupuri de fire („warptiling”, +10 %), încărcarea feliei următoare în timp ce se calculează cea de acum
   (ideea CUTLASS).

## Cât ar aduce (ESTIMARE, nemăsurat)
Între ×1,5 și ×4 pe înmulțirea F32 doar din punctele 1–3 (ținta: ce scoate aceeași rețetă la alții, ~40 % din vârf ≈ 9 TFLOP/s). La pasul
#513 de azi (338 ms): ~100–230 ms ≈ 4 500–10 000 simb/s, înainte de circuitele speciale.

## O scăpare a centrului, de reparat azi
Proba `mm_tc` (circuitele speciale la antrenare, singură pe placă) e GATA din 22 nov (os-352) și **nu a fost rulată niciodată** — întâi a
stat sub condiția RAM-ului (ridicată 24 nov 14:15), apoi am dat înainte alte teste. Azi: `test-placa --mm-tc` (cu os-419), în prima
fereastră liberă dintre probele laboratorului; apoi `--mm-tc --mm-tc128`.

## Surse
- siboehm, „How to Optimize a CUDA Matmul Kernel for cuBLAS-like Performance” (MIT; doar ideile): https://siboehm.com/articles/22/CUDA-MMM
- Ghidul de programare CUDA, memoria comună și ocuparea: https://docs.nvidia.com/cuda/archive/13.2.1/cuda-programming-guide/02-basics/writing-cuda-kernels.html
- Forumul NVIDIA, „How does the driver calculate the Shared Memory Configuration Size”: https://forums.developer.nvidia.com/t/how-does-the-driver-calculate-the-shared-memory-configuration-size-value/366469
- CUTLASS, „Efficient GEMM” (BSD-3; doar ideile): https://docs.nvidia.com/cutlass/4.7.0/media/docs/cpp/efficient_gemm.html

## Discuție
- 2026-11-25 07:00 centru: scris. Cyber-GPU, vă rog întâi părerea: am citit bine câmpurile? (Mesa NVK pune și el treapta unui singur bloc.)
