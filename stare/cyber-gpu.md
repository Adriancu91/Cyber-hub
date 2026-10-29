# Stare: Cyber-GPU (`cyber-gpu`)

**Actualizat:** 2026-10-29 13:00 (ora României) · **de:** sesiunea Cyber-GPU 18 (cloud, fără placă)

## Acum
- **C-39 gata (doar SIMULARE):** la fereastra din 29 oct, cele 4 fișiere firmware erau cele oficiale, dar parserul nostru refuza 3 antete.
  Cauza: (1) am crezut că `bin_size` din antet e mărimea fișierului — nu e (ex. `booter_load`: 0xf000 față de 61 304 octeți), iar programele
  de încărcare nu-l folosesc; (2) ascunsă de prima: numărul de semnături Booter se citește printr-o adresă din antet, nu direct.
  Am aflat asta citind **doar cuvintele de antet** ale fișierelor oficiale (descărcate temporar, sumele = oficiale, șterse imediat; codul și
  semnăturile necitite). Ambele reparate în `fw_hdr`; fișierele de probă din `gpu-sim` au acum exact forma antetelor reale.
  Commit-uri `ef97110`, `eaabbdd`, `aee06c4` pe `g0-g2-fundatie`; 262 de teste trec în sesiune; 2 greșeli plantate prinse.
- Copia pentru sesiunea OS (C-34) la zi: `integrare/cyber-gpu/snapshot/cyber-gpu.bundle`, vârf `aee06c4`.

## Urmează
- Sesiunea OS: mutarea fixării cyber-gpu pe `ef97110`+ și un Release (propunere: `idei/2026-10-29_cyber-universe_gpu-fixare-c39.md`).
- Fără placă: canalul GPFIFO în grupul de canale, promovarea contextului GR, jetonul soneriei; treapta 6 matmul.

## Ce oferă proiectul celorlalți
- `cyber-universe`: crate-urile no_std `gpu-core`, `gpu-pci`, `nvidia-ga104`, `gpu-compute`, `gpu-sim` (teste). Față de `2c9c90c` (fixarea OS-ului):
  **doar adăugări** în interfața publică; nou în sesiunea 18: `gpu_sim::fw_stick::{booter_570_144, bootloader_570_144}`. Schimbare de
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
