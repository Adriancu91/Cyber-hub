# Stare: Cyber-GPU (`cyber-gpu`)

**Actualizat:** 2026-10-31 19:35 (ora României) · **de:** sesiunea Cyber-GPU 28 (cloud, fără placă) — **OPRIT: necesită analiza lui Adrian**

## Acum
- **OPRIT: necesită analiza lui Adrian** (oprirea de siguranță, sesiunea 28): sesiunile 25, 26, 27 n-au terminat niciun pas și n-a apărut
  nimic nou (nicio comandă, niciun rezultat de pe placă, nicio decizie). CI verde (rularea 73). Sesiunile următoare nu încep lucru nou până la
  una din: rezultatul ferestrei pe workstation în hub, o comandă nouă pentru `cyber-gpu`, sau decizia lui Adrian despre sesiunea programată.
- **Treapta 6 matmul gata (doar SIMULARE):** programul de înmulțire de matrice, varianta care citește și scrie memoria câte 4 numere odată,
  compilat cu Mesa NAK pe gazdă: 821 de instrucțiuni (față de 1 953 la treapta 5), 90 de registre, fără memorie locală. În simulare dă exact
  aceiași biți ca oracolul și ca treapta 5; refuză (fără nicio scriere) matrice cu K sau N care nu se împart la 4 și adrese nealiniate;
  8 greșeli plantate, toate prinse. Commit-uri `937fcf4`, `647398c` pe `g0-g2-fundatie`; 294 de teste trec.
- Totul în model: **soneria nu e sunată**, programele „rulează” pe procesor. Nimic testat pe RTX 3070 Ti.
- Copia pentru sesiunea OS (C-34) la zi: `integrare/cyber-gpu/snapshot/cyber-gpu.bundle`, vârf `2916cb5` (doar documente noi față de `647398c`).

## Urmează
- Fereastra următoare (cu `os-210` sau `os-209`, ambele au fixarea `aee06c4`): `gpu firmware` → `criteriul I4: TRECE`; apoi, opțional, proba tinygrad.
- **Fără placă nu mai e niciun pas mic de făcut.** Tot restul (I5+: FWSEC, Booter, GSP, soneria, lansările reale, viteza treptelor matmul)
  cere fereastra pe workstation cu Adrian. Sesiunile următoare fără rezultate noi de pe placă se opresc fără lucru nou.

## Ce oferă proiectul celorlalți
- `cyber-universe`: crate-urile no_std `gpu-core`, `gpu-pci`, `nvidia-ga104`, `gpu-compute`, `gpu-sim` (teste). Față de `2c9c90c` (fixarea OS-ului):
  **doar adăugări** în interfața publică; nou în sesiunea 18: `gpu_sim::fw_stick::{booter_570_144, bootloader_570_144}`; în sesiunea 19:
  `nvidia_ga104::gsp::user_space::{WorkChannel, open_work_channel}` și funcții noi în `gsp::rmapi`; în sesiunea 20: `gsp::work_queue`,
  `user_space::open_work_channel_cleared`, în `gpu_sim::cmdproc`: `ComputeState`, `run_channel`; în sesiunea 21: `work_queue::{invalidate_caches,
  launch, release, read_semaphore}`, `WorkQueue::launch_and_signal`, `CommandProcessor::cache_invalidations`; în sesiunea 22: `user_space::query_gr_info`,
  `rmapi::{gr_info_request, parse_gr_info, GrInfo, SM_VERSION_SM86}`, în `gpu_sim::fake_rm`: `SIM_GR_INFO`; în sesiunea 23: `WorkQueue::{retire,
  push_in_flight}`; în sesiunea 24: `gpu_sim::cmdproc::{matmul_vec4_on_cpu, MATMUL_VEC4_NEEDS}` (nimic de schimbat în OS). Schimbare de
  comportament intenționată: `fw_hdr` acceptă `bin_size` ≠ mărimea fișierului și citește numărul de semnături prin adresă. Codul OS nu se
  schimbă; doar fixarea (nota `integration/cyber-universe/C-39_gpu-firmware-antete.md`).
- Pentru mai târziu (doar în fereastra cu Adrian): pornirea reală a GSP va cere de la OS o zonă de RAM contiguă (sub 2^49) și Bus Master.
- `kronos` / K6-CPU: operatorii lui Kronos pe procesor, neschimbați.

## De ce are nevoie de la ceilalți
- De la `cyber-universe`: nimic nou (fixarea `aee06c4` e în `os-209`, mulțumim).
- De la `kronos`: workstation-ul, doar în fereastra aprobată de Adrian.

## Blocaje / nevoie de Adrian
**Proiectul e OPRIT până la analiza ta:** fără placă nu mai e nimic de făcut. Variante: (a) fereastra de mai jos, (b) rărești sau oprești sesiunea programată Cyber-GPU până la fereastră.
**Fereastra următoare (cu `os-210`/`os-209`, gata de la sesiunea OS). Lista: `cyber-gpu/docs/FEREASTRA_C-39.md`.**
1. **Doar citire, nu atinge placa:** `gpu firmware` → trebuie 4 rânduri „ok … oficial”, sub fiecare „antet citit”, și ultimul rând
   `criteriul I4: TRECE (fisiere oficiale 4/4, antete citite 4/4)`. Poză. Dacă tot apare „antet NECITIT”: poză și te oprești cu placa.
2. **Doar dacă 1 trece — ⚠️ SCRIE ÎN PLACA VIDEO:** proba tinygrad, exact ca la C-36 pasul 3 (stick Ubuntu 24.04 live, laptopul pentru
   SSH, ~30 min; oprire sigură: `Ctrl+C`, `sudo poweroff`, sau butonul 10 s + cablul scos 30 s). Nu scrie în memoria permanentă a plăcii.
3. **Nu acum:** pornirea plăcii cu driverul nostru (I5+). I6 (FWSEC) ar fi prima scriere a driverului nostru; o propunem separat, după ce
   jurnalul probei tinygrad e în hub.
- Tag-ul `stabil-2026-10-23` (opțional; tot 403 din cloud): GitHub → cyber-gpu → Releases → „Draft a new release” → tag `stabil-2026-10-23`, Target `41e44ba` → pre-release → Publish.
