# Stare: Cyber-GPU (`cyber-gpu`)

**Actualizat:** 2026-11-14 07:40 (ora României) · **de:** sesiunea Cyber-GPU 101 (cloud, fără placă) — **OPRIT: necesită analiza lui Adrian** (regula 8: sesiunile 99, 100 și 101 fără niciun pas). **Nu e o problemă de cod**: 479 PASS (SIMULARE), **CI VERDE pe `7beecb6`**; e doar așteptare — nicio comandă nouă, niciun jurnal nou de pe placă sau laptop (Adrian plecat până luni seara, placa workstation-ului e a lui Kronos, C-119/C-120). Starea de fond, neschimbată din sesiunea 98: turul de citire a TRECUT pe laptop (GA106, `os-301`); **pasul 3 din C-116 (I6–I8 pe laptop) așteaptă DA-ul separat al lui Adrian** (`GA106_LAPTOP.md` §7); pe workstation I8 și golden au trecut, I9 așteaptă un `gpu lant` cu motivul în jurnal. **Oprirea se ridică singură** la oricare dintre: DA/NU de la Adrian, un jurnal nou în `rezultate/`, o comandă nouă pentru cyber-gpu.

## Acum
- **Sesiunea 101 (14 nov 07:25–07:40) — OPRIT: necesită analiza lui Adrian (regula 8).** În hub de la 01:40: doar OS-ul „OPRIT rămâne” (02:50, 05:50). `rezultate/` neschimbat de la os-301. Verificat: 479 PASS, CI verde (`7beecb6`). Starea sesiunii `237992a`; copia C-34 la `237992a` (235 commit-uri, verificată + clonare de probă). Nimic nou început.
- **Sesiunea 100 (14 nov 01:25–01:40) — oprire scurtă.** În hub de la 19:45: doar Kronos (C-120: S110 pornește cu restul FineWeb-2, ~52 h) și OS-ul „OPRIT rămâne”. `rezultate/` neschimbat de la os-301. Starea sesiunii `7beecb6`; copia C-34 la `7beecb6` (234 commit-uri, verificată + clonare de probă).
- **Sesiunea 99 (13 nov 19:25–19:45) — oprire scurtă.** În hub de la 13:55: C-120 (Kronos, nu ne privește), OS-ul „OPRIT: necesită analiza lui Adrian” (regula lor 5 — doar așteptare, nicio problemă de cod). `rezultate/` neschimbat de la os-301. Nota OS-ului „45 fapte pe ecran / 47 pe model”: cele 2 rânduri sunt dintre cele tăiate sus în poză — se lămurește la următorul test pe laptop cu `analiza` (`os-302`); nimic de făcut în driver acum. Copia C-34 la `f394261` (233 commit-uri, verificată + clonare de probă).
- **Sesiunea 98 (13 nov 13:25–13:55) — jurnalul de pe laptop citit și pus în model (C-116 pasul 3, partea de citire).** Ce a arătat laptopul (OBSERVAT, `rezultate/2026-11-13-laptop-asus-os301/`: `gpu-jurnal-003.txt` + poza `gpu-tur-trezire.jpg`):
  BOOT_0 `0xb76000a1` / BOOT_42 `0x176a1000` → **GA106** consecvent; GFW terminat la prima rundă; **VBIOS valid prin PROM**: 3 imagini (PCI-AT `10de:2520` + două FWSEC `10de:2200`; **fără imagine EFI** — ecranul e pe Intel), BIT la 0x1b0 cu **aceleași 17 jetoane** ca pe workstation;
  **`vbios.versiune = 94.06.1e.00.23`** (= UHL/Windows); FWSEC: descriptor v3 la 0x2c834, IMEM **0xe100** (workstation 0xe200), 3 semnături, ucode_id 9 — altă construcție, același format, citit fără schimbări; siguranța `0x8241e0 = 3` (ca GA104); **VRAM 6144 MiB**; WPR2 coborât → `i6.trece = da`.
  Riscurile de laptop (placa adormită / lipsă, VBIOS doar prin ACPI `_ROM`) **nu s-au arătat** — sarcina `_ROM` nu mai e necesară. Stick-ul pe laptop: 6,1 ms/rând (fără încetinirea de ~1 s de pe Kingston).
  - **Cod (doar adăugări, `214de94`):** `gpu_sim::observed_laptop` (cele 8 citiri BAR0, așezarea VBIOS, FWSEC, BAR3/BAR5 observate; **fără conținut de VBIOS**, fără firmware; `STILL_SIM` spune ce rămâne inventat);
    testul `laptop_journal_003_agrees_with_the_observed_laptop_model`: jurnalul 003 întreg + 39 de fapte transcrise din poză față de `run_tour_awake` pe model → **36 la fel, 0 diferit, 1 diferit intenționat (cuvântul PROM), 0 doar pe placă**, aceleași 8 citiri în aceeași ordine; proba inversă (modelul workstation-ului nu explică jurnalul). `board_compare` citește acum și rândurile de pe stick.
  - **Documente:** `GA106_LAPTOP.md` §0c (tabelul laptop ↔ workstation), §2/§3/§5 trecute la OBSERVAT, **§7 = lista pentru pasul 3, scrisă înainte de DA**; TEST_MATRIX T128; PROVENANCE; nota pentru OS `integration/cyber-universe/os-301_laptop-tur-citit.md`. **479 PASS** (475 → +4), clippy, format, no_std. Copia C-34 la `4ff043d` (231 commit-uri, verificată + clonare de probă).
  - **Ce NU s-a făcut, intenționat:** niciun cod pentru I6–I8 pe GA106 — cere DA-ul separat (C-116). `Family::writes_allowed()` rămâne doar GA104.
- **Sesiunea 97 (07:25–07:45) — oprire scurtă**; `GA106_LAPTOP.md` §0b: „fără MUX” observat din raportul UHL de energie (`aabd093`).
- **Sesiunea 96 (01:25–02:15)** — `vbios.versiune` din jetonul BIT 'i' (`835f24d`), faptele UHL în modelul laptopului; **confirmat pe placă în sesiunea 98**.
- **Sesiunea 95 (12 nov 21:00–21:40) — C-116 pașii 1–2:** GA106 doar-citire (`6623d3c`) + „trezirea minimă” (`ccec8f9`: o scriere în Command, repusă; `gpu_pci::mem_space`, `run_tour_awake`) — legate în `os-298`; **au mers pe laptop exact așa (13 nov).**
- **Sesiunile 93–94 (12 nov)** — **I8 TRECE pe placă** (varianta 1), **golden I8e TRECE**, **I9 ESEC** la `PROMOTE_CTX` virtual fără motiv (de la `45dfc77` motivul merge pe stick); jurnalele 011/012 (I7 ESEC la repetare cu stick lent; `gpu recupereaza` → 0x88, FWSEC-SB cere DA). `docs/os-295_ANALIZA_I9.md`, `os-295_ANALIZA_011_012.md`.
- **Pe placă până acum (GA104, workstation):** I0–I4 doar citire TREC; I6 TRECE; I7 TRECE (o dată ESEC cu stick lent); **I8 TRECE (os-295)**; **I8e golden TRECE**; I9 ESEC fără motiv; I10–I14 neîncercate.
- **Pe laptop (GA106):** **turul de citire complet TRECE (os-301)**, 2 scrieri în Command, 0 în registre; I6+ neîncercat (cere DA).

## Lista pentru laptop (C-116 pasul 3 — DOAR după DA-ul lui Adrian; detalii `cyber-gpu/docs/GA106_LAPTOP.md` §7)
1. Adrian: **DA sau NU** pentru primele scrieri în registrele laptopului (I6 = FWSEC-FRTS, apoi I7 Booter, I8 GSP-RM; același firmware 570.144 de pe stick, `ga106/gsp -> ga102/gsp`).
2. Dacă DA: noi deschidem GA106 în `Family::writes_allowed()` doar pe stick-ul de test (`gpu-scrie`) + DA la ecran, cu trezirea minimă ținută pornită pe durata lanțului; OS-ul leagă commit-ul; test pe laptop **un pas pe rând**: întâi `gpu i6`, apoi `gpu lant`.
3. Limita de memorie pe laptop: sub ~5,5 GB (pasul 4), când lanțul ajunge la alocări (I9+).

## Lista pentru workstation (GA104, după ce Kronos eliberează placa — C-119, ~luni)
1. `os-302` (sau mai nou) → pornire rece → `gpu lant` (varianta 1) → DA → `trimite`. 2. În jurnal: la I7 picat rândurile stării; **la I9 picat `text motivul esecului`** → noi: regulile `PROMOTE_CTX`. 3. `gpu recupereaza` NU, până la decizia FWSEC-SB. 4. Dacă I9 trece: I10 (add64) = primul calcul pe placă.

## Urmează
1. **Adrian (luni seara):** DA/NU pentru pasul 3 pe laptop (lista de mai sus); când se eliberează workstation-ul, un `gpu lant` → motivul lui I9.
2. **OS-ul:** nimic de la noi acum — `835f24d` rămâne bun, `os-302` îl leagă; nota `os-301_laptop-tur-citit.md` (un amănunt de afișaj: „45 fapte” pe ecran față de 47 de rânduri `fapt` pe model — fără urgență).
3. **Noi, după oricare jurnal nou sau după DA:** I9 cu motiv → `PROMOTE_CTX`; DA pe laptop → pasul 3 după §7. **Fără jurnal nou și fără comandă nouă, nimic altceva pe driver** (regula din sesiunile 90–100). Până luni seara sesiunile fac doar verificări scurte (hub, `check.sh`, CI); de la sesiunea 101 starea e „OPRIT” (regula 8) și rămâne așa până la DA, un jurnal nou sau o comandă nouă.

## Ce oferă proiectul celorlalți
- **Sesiunea 98 (doar adăugări — OS-ul compilează neschimbat la `4ff043d`):** `gpu_sim::observed_laptop::{observed_laptop_config, observed_laptop_bar0, observed_laptop_rom, BAR0_READS, IMAGES, STILL_SIM, …}` (modelul laptopului din jurnalul real);
  `board_compare::facts_from_report` citește și rândurile de jurnal de pe stick (`gpu: bar0 r …`); `SimConfig::ga106_laptop_asus` are BAR5 = `0x4001` (observat). Nota: `cyber-gpu/integration/cyber-universe/os-301_laptop-tur-citit.md`.
- **Sesiunea 96 (doar adăugări — OS-ul compilează neschimbat la `835f24d`):** `nvidia_ga104::vbios::{BiosVersion, BIT_TOKEN_BIOS_INFO, BIOS_INFO_MIN_LEN}`, câmpul `VbiosLayout.version: Option<BiosVersion>`,
  `BiosVersion::matches_report`; `read_tour::{FACT_VBIOS_VERSION = "vbios.versiune", VBIOS_VERSION_UNREAD}`; `gpu_sim::laptop` (faptele UHL), `gpu_sim::observed::{observed_rom_with_version, VBIOS_VERSION_BYTES}`,
  `gpu_sim::rom::{with_bios_info, bios_info_bytes, SIM_BIOS_INFO_AT}`. Nota: `cyber-gpu/integration/cyber-universe/C-117_vbios-versiune.md`.
- **Sesiunea 95 (C-116, doar adăugări — OS-ul compilează neschimbat la `ccec8f9`):** `nvidia_ga104::ids::{GA106_MODELS, LAPTOP_DEVICE, Family, lookup_ga106, lookup_ampere}`, `boot::CHIP_GA106`;
  `probe::{probe_config_ampere, probe_mmio_family, level0_ampere, MEMORY_SPACE_OFF}`, `probe::Candidate::memory_space_enabled`; `read_tour::{run_tour_ampere, run_tour_awake, Wake, FACT_WAKE}`;
  **`gpu_pci::mem_space::{MemorySpacePermit, check_before_enable, enable_memory_space, restore_memory_space, ALREADY_ON, STEP_ON, STEP_RESTORED}`**; `gpu_sim::pci::SimConfig::ga106_laptop_asus`,
  `gpu_sim::mmio::SimMmio::ga106_bar0`. `ids::lookup`, `probe::probe_config`, `level0`, `run_tour` și lanțul: neschimbate (GA104-only). Nota: `cyber-gpu/integration/cyber-universe/C-116_ga106-trezire.md`.
- **Sesiunea 94 (doar adăugări + o valoare):** `falcon::{journal_i7_failure, I7_FAIL_RISCV_OFF, I7_FAIL_BOOTER_CODE, UNLOAD_FAIL_STATE, I7_FAIL_EXTRA_READS}`; `falcon::RISCV_ACTIVE_US` = 5 000 000.
- **Sesiunea 93:** `variants::settings(None)` = varianta 1; `Journal::push_text`; `chain::{STEP_FAIL_REASON, STEP_FAIL_REASON_MORE}`; `gsp::golden::{QueueTransportBellKeep, journal_skipped}`; `variant_log::VariantRun::fail_reasons`.
- **Sesiunile 88–89:** `gsp::variants` (11 variante), `variant_log` + `compara_variante`. **Mai vechi (toate doar adăugări):** `nvidia_rm570::names`, `gsp::nocat`, `falcon::booter_unload*`,
  `gpu_pci::caps::reset_capabilities`, `falcon::start_cpu`, `chain_log`, I11–I14, `kronos_gen`, `recovery`, `falcon::booter_load_dma_libos`. Lista completă: `cyber-gpu/docs/IMPLEMENTATION_STATUS.md`.
- `cyber-universe`: crate-urile no_std `gpu-core`, `gpu-pci`, `nvidia-ga104`, `gpu-compute`, `gpu-sim` (teste). `kronos` / K6-CPU: operatorii pe procesor, neschimbați.

## De ce are nevoie de la ceilalți
- De la `cyber-universe`: nimic acum (`os-302` leagă `835f24d`; `4ff043d` nu schimbă nimic pentru OS). Când vine DA-ul pentru pasul 3: legarea commit-ului nou + `gpu i6`/`gpu lant` acceptate pe GA106 doar pe stick-ul de test.
- De la Adrian: **DA/NU pentru pasul 3 pe laptop** (luni seara); pe workstation un `gpu lant` cu motivul lui I9 (după C-119). Decizie (fără grabă): FWSEC-SB înainte de Booter Unload (C-103) — DA/NU.
- De la `cyber-universe` (P6-66, mai târziu): `Generation::run` + `VramBudget::check` în `kronos --gpu`.

## Blocaje / nevoie de Adrian
- **OPRIT (regula 8, sesiunea 101): necesită analiza lui Adrian** — doar așteptare, nicio problemă tehnică. Ridică oprirea: DA/NU pentru pasul 3 pe laptop, un jurnal nou, sau o comandă nouă.
- **Nu e blocat.** Laptopul: turul de citire a trecut; următorul pas (scrieri în registrele GA106) cere **DA-ul tău separat** — nimic nu pornește fără el. Workstation: așteaptă placa de la Kronos (C-119) pentru `gpu lant` → motivul lui I9.
- Workstation: I7 a picat o dată din două (stick lent, C-113 rezolvat în `os-297`); `gpu recupereaza` dă 0x88 (FWSEC-SB înainte = program semnat în plus → DA); ecranul îngheață după pornirea GSP-RM (varianta 11 ca probă). Pe laptop ecranul e pe Intel — problema nu ar trebui să apară acolo.
- CI GitHub: **VERDE pe `7beecb6`** (rularea 43527343300) și pe `e0bacf9` (sesiunea 98, rularea 43419426786, 43 s; verificat în sesiunea 99), pe `4ff043d`, `aabd093` (sesiunea 97), `f4b012c` și `79fc5ae`. Pe `f394261` (sesiunea 99, doar documente — codul identic cu `e0bacf9`) **CI-ul nu a pornit**: GitHub a răspuns „Internal Server Error” la push (ref-ul s-a actualizat, evenimentul de push s-a pierdut); nu se face commit gol ca să-l pornim — următorul commit real îl rulează.
