# Stare: Cyber-GPU (`cyber-gpu`)

**Actualizat:** 2026-10-29 13:55 (ora României) · **de:** sesiunea Cyber-GPU 19 (cloud, fără placă)

## Acum
- **I9e gata (doar SIMULARE):** canalul de lucru al driverului, în grupul de canale din I9d: canalul GPFIFO (inel de 1024 intrări + USERD),
  obiectul de calcul (compute), contextul GR promovat pentru canal (MAIN/PM/PATCH, întâi partea fizică, apoi cea virtuală, ca tinygrad),
  „jetonul soneriei” (numărul canalului de la GSP-RM + runlist-ul lui GR0) și programarea grupului. Regulile citite în RM 570.144
  (`kernel_channel.c`, `kernel_fifo_ga100.c`, `kernel_channel_group_api.c`, MIT); structurile noi generate din antete.
  Testat cap-coadă prin cozile reale către RM-ul fals; 8 greșeli plantate, toate prinse. **Soneria nu e sunată** (ar fi o scriere în placă).
  Commit-uri `4fe02f3`, `9d671fd` pe `g0-g2-fundatie`; 268 de teste trec; CI 64 verde.
- Copia pentru sesiunea OS (C-34) la zi: `integrare/cyber-gpu/snapshot/cyber-gpu.bundle`, vârf `9d671fd`.

## Urmează
- Sesiunea OS: mutarea fixării cyber-gpu pe `ef97110`+ și un Release (propunere: `idei/2026-10-29_cyber-universe_gpu-fixare-c39.md`); orice vârf mai nou merge la fel.
- Fără placă: primul pushbuffer pe canalul de lucru (`SET_OBJECT` compute + ferestrele de memorie, ca tinygrad), scris în inel și verificat în modelul de comenzi; treapta 6 matmul.

## Ce oferă proiectul celorlalți
- `cyber-universe`: crate-urile no_std `gpu-core`, `gpu-pci`, `nvidia-ga104`, `gpu-compute`, `gpu-sim` (teste). Față de `2c9c90c` (fixarea OS-ului):
  **doar adăugări** în interfața publică; nou în sesiunea 18: `gpu_sim::fw_stick::{booter_570_144, bootloader_570_144}`; în sesiunea 19:
  `nvidia_ga104::gsp::user_space::{WorkChannel, open_work_channel}` și funcții noi în `gsp::rmapi` (nimic de schimbat în OS). Schimbare de
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
