# Stare: Cyber-GPU (`cyber-gpu`)

**Actualizat:** 2026-10-30 07:40 (ora României) · **de:** sesiunea Cyber-GPU 22 (cloud, fără placă)

## Acum
- **I10c gata (doar SIMULARE):** driverul întreabă acum GSP-RM ce formă are motorul de calcul al plăcii (câte grupuri GPC, câte TPC în
  fiecare, câte SM, câte warp-uri pe SM, ce versiune SM), cu aceeași comandă internă pe care o folosește tinygrad când vorbește direct cu
  GSP. Din răspuns se calculează memoria locală a programelor; o placă care nu e `sm_86` e refuzată înainte de orice lansare (programele
  noastre sunt compilate pentru GA104). Modelul din `gpu-sim` răspunde cu **valori SIM** (forma unui GA104 complet: 48 SM). 8 greșeli
  plantate în răspuns, toate prinse. Commit-uri `d15af17`, `01bc248` pe `g0-g2-fundatie`; 288 de teste trec.
- Prima lansare (I10b) rămâne la fel: totul în model, **soneria nu e sunată**, programul „rulează” pe procesor.
- Copia pentru sesiunea OS (C-34) la zi: `integrare/cyber-gpu/snapshot/cyber-gpu.bundle`, vârf `01bc248`.

## Urmează
- Fereastra următoare (cu `os-209`, care are deja fixarea `aee06c4`): `gpu firmware` → `criteriul I4: TRECE`; apoi, opțional, proba tinygrad.
- Fără placă mai rămân doar pași mici: refolosirea bufferului de comenzi după semafor; treapta 6 matmul. Restul (I5+ pe placă) cere fereastra cu Adrian.

## Ce oferă proiectul celorlalți
- `cyber-universe`: crate-urile no_std `gpu-core`, `gpu-pci`, `nvidia-ga104`, `gpu-compute`, `gpu-sim` (teste). Față de `2c9c90c` (fixarea OS-ului):
  **doar adăugări** în interfața publică; nou în sesiunea 18: `gpu_sim::fw_stick::{booter_570_144, bootloader_570_144}`; în sesiunea 19:
  `nvidia_ga104::gsp::user_space::{WorkChannel, open_work_channel}` și funcții noi în `gsp::rmapi`; în sesiunea 20: `gsp::work_queue`,
  `user_space::open_work_channel_cleared`, în `gpu_sim::cmdproc`: `ComputeState`, `run_channel`; în sesiunea 21: `work_queue::{invalidate_caches,
  launch, release, read_semaphore}`, `WorkQueue::launch_and_signal`, `CommandProcessor::cache_invalidations`; în sesiunea 22: `user_space::query_gr_info`,
  `rmapi::{gr_info_request, parse_gr_info, GrInfo, SM_VERSION_SM86}`, în `gpu_sim::fake_rm`: `SIM_GR_INFO` (nimic de schimbat în OS). Schimbare de
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
