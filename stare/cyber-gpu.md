# Stare: Cyber-GPU (`cyber-gpu`)

**Actualizat:** 2026-10-29 19:50 (ora României) · **de:** sesiunea Cyber-GPU 20 (cloud, fără placă)

## Acum
- **I10a gata (doar SIMULARE):** primul set de comenzi pe canalul de lucru al driverului: alegerea clasei de calcul și cele două
  „ferestre” de memorie (locală și partajată), exact cuvintele pe care le trimite tinygrad; comenzile ajung în bufferul de comenzi,
  intrarea în inel, apoi „pointerul de scriere” (`GPPut`) în USERD; driverul citește înapoi cât a preluat placa și refuză valori imposibile.
  Modelul de placă din `gpu-sim` citește totul **doar prin tabelele de pagini** date lui GSP-RM. Testul a găsit o problemă reală:
  USERD-ul trebuie șters de driver **înainte** de a cere canalul (altfel conține „gunoi”) — reparat (`open_work_channel_cleared`).
  8 greșeli plantate, toate prinse. **Soneria nu e sunată** (ar fi o scriere în placă): driverul doar descrie ce ar scrie.
  Commit `5366ed3` pe `g0-g2-fundatie`; 280 de teste trec; CI 65 verde.
- Copia pentru sesiunea OS (C-34) la zi: `integrare/cyber-gpu/snapshot/cyber-gpu.bundle`, vârf `5366ed3`.

## Urmează
- Sesiunea OS: mutarea fixării cyber-gpu pe `ef97110`+ și un Release (propunere: `idei/2026-10-29_cyber-universe_gpu-fixare-c39.md`); orice vârf mai nou merge la fel.
- Fără placă: cererea `GR_GET_INFO` către GSP-RM (câte GPC/TPC are placa, pentru memoria locală) și prima lansare de program pe canalul de lucru în model (QMD + lansare + semaforul de terminare); treapta 6 matmul.

## Ce oferă proiectul celorlalți
- `cyber-universe`: crate-urile no_std `gpu-core`, `gpu-pci`, `nvidia-ga104`, `gpu-compute`, `gpu-sim` (teste). Față de `2c9c90c` (fixarea OS-ului):
  **doar adăugări** în interfața publică; nou în sesiunea 18: `gpu_sim::fw_stick::{booter_570_144, bootloader_570_144}`; în sesiunea 19:
  `nvidia_ga104::gsp::user_space::{WorkChannel, open_work_channel}` și funcții noi în `gsp::rmapi`; în sesiunea 20: `gsp::work_queue`,
  `user_space::open_work_channel_cleared`, în `gpu_sim::cmdproc`: `ComputeState`, `run_channel` (nimic de schimbat în OS). Schimbare de
  comportament intenționată: `fw_hdr` acceptă `bin_size` ≠ mărimea fișierului și citește numărul de semnături prin adresă. Codul OS nu se
  schimbă; doar fixarea (nota `integration/cyber-universe/C-39_gpu-firmware-antete.md`).
- Pentru mai târziu (doar în fereastra cu Adrian): pornirea reală a GSP va cere de la OS o zonă de RAM contiguă (sub 2^49) și Bus Master.
- `kronos` / K6-CPU: operatorii lui Kronos pe procesor, neschimbați.

## De ce are nevoie de la ceilalți
- De la `cyber-universe`: Release cu cyber-gpu ≥ `ef97110` (doar fixarea), pentru fereastra următoare.
- De la `kronos`: workstation-ul, doar în fereastra aprobată de Adrian.

## Blocaje / nevoie de Adrian
**Fereastra următoare (după Release-ul OS cu fixarea nouă). Lista: `cyber-gpu/docs/FEREASTRA_C-39.md`.**
1. **Doar citire, nu atinge placa:** `gpu firmware` → trebuie 4 rânduri „ok … oficial”, sub fiecare „antet citit”, și ultimul rând
   `criteriul I4: TRECE (fisiere oficiale 4/4, antete citite 4/4)`. Poză. Dacă tot apare „antet NECITIT”: poză și te oprești cu placa.
2. **Doar dacă 1 trece — ⚠️ SCRIE ÎN PLACA VIDEO:** proba tinygrad, exact ca la C-36 pasul 3 (stick Ubuntu 24.04 live, laptopul pentru
   SSH, ~30 min; oprire sigură: `Ctrl+C`, `sudo poweroff`, sau butonul 10 s + cablul scos 30 s). Nu scrie în memoria permanentă a plăcii.
3. **Nu acum:** pornirea plăcii cu driverul nostru (I5+). I6 (FWSEC) ar fi prima scriere a driverului nostru; o propunem separat, după ce
   jurnalul probei tinygrad e în hub.
- Tag-ul `stabil-2026-10-23` (opțional; tot 403 din cloud): GitHub → cyber-gpu → Releases → „Draft a new release” → tag `stabil-2026-10-23`, Target `41e44ba` → pre-release → Publish.
