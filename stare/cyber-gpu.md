# Stare: Cyber-GPU (`cyber-gpu`)

**Actualizat:** 2026-10-30 01:40 (ora României) · **de:** sesiunea Cyber-GPU 21 (cloud, fără placă)

## Acum
- **I10b gata (doar SIMULARE):** prima lansare de program pe canalul de lucru al driverului: driverul pune în memoria plăcii programul
  `add64` (compilat cu Mesa NAK), datele, descrierea lansării (QMD) și un „semafor de terminare”; trimite comenzile ca tinygrad
  (golirea cache-urilor, lansarea, apoi semaforul pe 64 de biți care se scrie abia după ce programul a terminat). Modelul de placă din
  `gpu-sim` citește totul **doar prin tabelele de pagini**; driverul vede semaforul și rezultatul, **identic bit cu bit** cu calculul de
  referință. 8 greșeli plantate, toate prinse. **Soneria tot nu e sunată** (ar fi o scriere în placă). Programul „rulează” pe procesor.
  Commit-uri `4789afe`, `599831c`, `ab5a918` pe `g0-g2-fundatie`; 285 de teste trec.
- Copia pentru sesiunea OS (C-34) la zi: `integrare/cyber-gpu/snapshot/cyber-gpu.bundle`, vârf `ab5a918`.

## Urmează
- Fereastra următoare (cu `os-209`, care are deja fixarea `aee06c4`): `gpu firmware` → `criteriul I4: TRECE`; apoi, opțional, proba tinygrad.
- Fără placă: cererea `GR_GET_INFO` către GSP-RM (câte GPC/TPC are placa, pentru memoria locală); refolosirea bufferului de comenzi după
  semafor; treapta 6 matmul.

## Ce oferă proiectul celorlalți
- `cyber-universe`: crate-urile no_std `gpu-core`, `gpu-pci`, `nvidia-ga104`, `gpu-compute`, `gpu-sim` (teste). Față de `2c9c90c` (fixarea OS-ului):
  **doar adăugări** în interfața publică; nou în sesiunea 18: `gpu_sim::fw_stick::{booter_570_144, bootloader_570_144}`; în sesiunea 19:
  `nvidia_ga104::gsp::user_space::{WorkChannel, open_work_channel}` și funcții noi în `gsp::rmapi`; în sesiunea 20: `gsp::work_queue`,
  `user_space::open_work_channel_cleared`, în `gpu_sim::cmdproc`: `ComputeState`, `run_channel`; în sesiunea 21: `work_queue::{invalidate_caches,
  launch, release, read_semaphore}`, `WorkQueue::launch_and_signal`, `CommandProcessor::cache_invalidations` (nimic de schimbat în OS). Schimbare de
  comportament intenționată: `fw_hdr` acceptă `bin_size` ≠ mărimea fișierului și citește numărul de semnături prin adresă. Codul OS nu se
  schimbă; doar fixarea (nota `integration/cyber-universe/C-39_gpu-firmware-antete.md`).
- Pentru mai târziu (doar în fereastra cu Adrian): pornirea reală a GSP va cere de la OS o zonă de RAM contiguă (sub 2^49) și Bus Master.
- `kronos` / K6-CPU: operatorii lui Kronos pe procesor, neschimbați.

## De ce are nevoie de la ceilalți
- De la `cyber-universe`: nimic nou (fixarea `aee06c4` e în `os-209`, mulțumim).
- De la `kronos`: workstation-ul, doar în fereastra aprobată de Adrian.

## Blocaje / nevoie de Adrian
**Fereastra următoare (cu `os-209`, gata de la sesiunea OS). Lista: `cyber-gpu/docs/FEREASTRA_C-39.md`.**
1. **Doar citire, nu atinge placa:** `gpu firmware` → trebuie 4 rânduri „ok … oficial”, sub fiecare „antet citit”, și ultimul rând
   `criteriul I4: TRECE (fisiere oficiale 4/4, antete citite 4/4)`. Poză. Dacă tot apare „antet NECITIT”: poză și te oprești cu placa.
2. **Doar dacă 1 trece — ⚠️ SCRIE ÎN PLACA VIDEO:** proba tinygrad, exact ca la C-36 pasul 3 (stick Ubuntu 24.04 live, laptopul pentru
   SSH, ~30 min; oprire sigură: `Ctrl+C`, `sudo poweroff`, sau butonul 10 s + cablul scos 30 s). Nu scrie în memoria permanentă a plăcii.
3. **Nu acum:** pornirea plăcii cu driverul nostru (I5+). I6 (FWSEC) ar fi prima scriere a driverului nostru; o propunem separat, după ce
   jurnalul probei tinygrad e în hub.
- Tag-ul `stabil-2026-10-23` (opțional; tot 403 din cloud): GitHub → cyber-gpu → Releases → „Draft a new release” → tag `stabil-2026-10-23`, Target `41e44ba` → pre-release → Publish.
