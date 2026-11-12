# Stare: Cyber-GPU (`cyber-gpu`)

**Actualizat:** 2026-11-12 21:40 (ora României) · **de:** sesiunea Cyber-GPU 95 (cloud, fără placă) — **C-116 (laptopul ASUS TUF F15, GA106) pașii (1) și (2) gata în SIMULARE: recunoașterea GA106 doar-citire e înapoi în driver (`6623d3c`) și există „trezirea minimă” (`ccec8f9`): o singură scriere în registrul Command al PCI (Memory Space pornit, repus la final), în spatele unui permis explicit, ca BAR0 să răspundă și turul de citire C-54 să meargă pe laptop. Niciun registru GPU scris; lanțul I6+ refuză laptopul până la DA-ul separat (pasul 3). 472 PASS. Nimic rulat pe laptop.** 🎉 Pe workstation: **I8 și golden (I8e) au trecut pe placă la 17:48 (os-295)**; I9 s-a oprit la `PROMOTE_CTX` virtual — motivul intră pe stick de la `45dfc77`; I7 a picat o dată din două (jurnalul 011, stick lent — C-113).

## Acum
- **Sesiunea 95 (21:00–21:40) — C-116, comanda nouă de la 20:57.** Ce a arătat laptopul (OBSERVAT de OS, os-295, 20:20): NVIDIA **`10de:2520`** la 01:00.0, **D0, Command 0x0000** (Memory
  Space oprit de firmware → BAR0 nu răspunde; de aceea „registre necitite”), BAR0 16 MiB @0x85000000, BAR1 8 GiB (ReBAR), BAR3 32 MiB; driverul a refuzat corect, zero scrieri.
  - **Pasul (1):** `ids::{GA106_MODELS, Family, lookup_ampere}`, `boot::CHIP_GA106 = 0x176`, `probe::{probe_config_ampere, level0_ampere, MEMORY_SPACE_OFF}`, `read_tour::run_tour_ampere`
    (faptele `chip.familie = GA106`, `chip.scrieri = interzise`); profil `gpu-sim` din faptele de pe laptop. **Nou față de sesiunea 77:** cu Memory Space oprit, BAR0 **nu se citește** (refuz numit).
  - **Pasul (2) „trezirea minimă”:** `gpu_pci::mem_space` (după modelul Bus Master, D-013): verificări doar-citire (răspunde, antet tip 0, D0, BAR0 alocat, BAR-urile ReBAR alocate) → **o scriere**
    în Command (doar bitul Memory Space; Bus Master/I/O rămân oprite), citită înapoi → turul C-54 → **Command repus** (și când turul pică). `read_tour::run_tour_awake`. În jurnal:
    `cfg w 0x004: 0x00100000 <- 0x00000002 => 0x00100002` și invers. Trei surse: PCI Local Bus 3.0 §6.2.2; Linux `pci_enable_device` (citit ca specificație) — ce face orice driver înainte de BAR0.
  - **Ce NU face:** nu schimbă energia, nu pornește DMA, nu scrie registre GPU, nu atinge ACPI. `Family::writes_allowed()` = doar GA104 → `gpu lant` / I6+ pe laptop refuzat fără cod nou.
  - T126 a–h, **472 PASS** (458 → 472), clippy, format, build no_std; **CI VERDE pe `6b6bb38`** (rularea 43288866245). Nota pentru OS: `cyber-gpu/integration/cyber-universe/C-116_ga106-trezire.md`.
    Documente: `cyber-gpu/docs/GA106_LAPTOP.md` (§0 faptele de pe laptop, §6 trezirea). Copia C-34 la `6b6bb38` (clona completată, 222 commit-uri, verificată).
- **Sesiunea 94 (19:25–20:00)** — jurnalele 011/012: I7 ESEC la repetarea variantei 1 cu scrieri identice (cauza nestabilită; stick lent, C-113); `gpu recupereaza` → Booter Unload **0x88**
  (cod nepublicat; fără FWSEC-SB înainte — cere DA). De la `3404313` jurnalul scrie starea plăcii după un I7 / Unload eșuat; „RISC-V activ” 5 s. `docs/os-295_ANALIZA_011_012.md`.
- **Sesiunea 93 (18:00–18:55)** — **I8 TRECE pe placă** (varianta 1, `GSP_INIT_DONE = 0`, 2 NOCAT), **golden I8e TRECE** (11 mesaje RM); **I9 ESEC** la al 11-lea mesaj (`PROMOTE_CTX` virtual),
  motiv necunoscut (era doar pe ecran) → de la `45dfc77` motivul merge pe stick; varianta 1 implicită (`e49ca76`); varianta 11 `bIsPrimary = 0` ca probă pentru ecran. `docs/os-295_ANALIZA_I9.md`.
- **Pe placă până acum (GA104):** I0–I4 doar citire TREC; I6 TRECE; I7 TRECE (o dată ESEC cu stick lent); **I8 TRECE (os-295)**; **I8e golden TRECE**; I9 ESEC fără motiv; I10–I14 neîncercate.
- **Pe laptop (GA106):** doar `gpu identifica` (ID-uri, Command 0), zero scrieri; nimic citit din registre încă.

## Lista pentru laptop (C-116, după ce OS-ul leagă `ccec8f9`+)
1. OS: `gpu identifica` / `gpu cauta` / `gpu vbios` pe funcțiile `_ampere` (laptopul identificat; cu Memory Space oprit mesajul vine din bibliotecă, fără citire BAR0);
   **`gpu tur` pe laptop** cu `run_tour_awake` **doar pe stick-ul de test (`gpu-scrie`), după DA** — textul DA: „o scriere în registrul Command al PCI, repusă la final; niciun registru GPU scris”.
2. Adrian, pe laptop: stick-ul de test → `gpu tur` → DA → `trimite` (sau jurnalul rămâne pe stick dacă nu e cablu). Înainte: Armoury Crate cu modul GPU „Standard” (nu „Eco”) — altfel placa lipsește de pe PCI.
3. Ce căutăm în jurnal: `BOOT_0 = 0x176…`, `BOOT_42` consecvent, GFW terminat, imaginile VBIOS prin PROM (gunoi → citirea prin ACPI `_ROM`, sarcină separată), FWSEC + semnături, siguranța,
   VRAM ~6 GiB, WPR2 = 0, cele două rânduri `cfg w 0x004`.
4. Abia după jurnal și DA-ul separat: pasul 3 (I6–I8 pe GA106 cu varianta 1; firmware-ul e același, `ga106/gsp -> ga102/gsp`); limita VRAM pe laptop sub ~5,5 GB (pasul 4).

## Lista pentru workstation (GA104, neschimbată)
0. Întâi stick-ul (C-113, OS). 1. Release care leagă `3404313`+ (acum `ccec8f9`+ — conține și GA106). 2. Pornire rece → `gpu lant` → DA → `trimite`. 3. În jurnal: la I7 picat rândurile stării;
la I9 picat `text motivul esecului`. 4. `gpu recupereaza` NU, până la decizia FWSEC-SB. 5. Varianta 11 doar dacă Adrian vrea ecranul înapoi. 6. Dacă I9 trece: I10 (add64) = primul calcul pe placă.

## Urmează
1. **OS-ul (C-116 partea lui):** leagă `ccec8f9`+; comenzile de citire pe `_ampere`; `gpu tur` cu trezirea minimă după DA (doar `gpu-scrie`); modelul laptopului din SMBIOS în `hw`. În paralel C-113.
2. **Adrian:** pe laptop `gpu tur` + DA + `trimite` → primul jurnal de citire de pe GA106. Pe workstation: un test `gpu lant` cu stick-ul reparat, când vine.
3. **Noi, după jurnalul de pe laptop:** VBIOS gunoi → `_ROM`; totul ca pe GA104 → pasul 3 doar cu DA separat. După jurnalul de pe workstation: I7 picat → rândurile stării; I9 picat cu cod →
   regulile `PROMOTE_CTX`; timeout → tabelele de pagini. Fără jurnal nou, nimic altceva pe driver.

## Ce oferă proiectul celorlalți
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
- De la `cyber-universe`: legarea `ccec8f9`+ → Release; C-116 partea OS (comenzile `_ampere`, `gpu tur` cu trezirea pe laptop după DA); **C-113** (stick-ul) înaintea testului pe workstation.
- De la Adrian: pe laptop `gpu tur` + DA + `trimite` (când OS-ul are comanda); pe workstation un `gpu lant` cu stick-ul reparat. Decizie (fără grabă): FWSEC-SB înainte de Booter Unload (C-103) — DA/NU.
- De la `cyber-universe` (P6-66, mai târziu): `Generation::run` + `VramBudget::check` în `kronos --gpu`.

## Blocaje / nevoie de Adrian
- **Nu e blocat.** C-116 pașii 1–2 gata în simulare; pasul 3 (scrieri în registre GPU pe laptop) cere DA-ul separat **după** primul jurnal de citire.
- Laptopul: firmware-ul lasă placa cu Memory Space oprit — fără trezirea minimă nu se poate citi nimic din ea; trezirea e o scriere în configurația PCI, repusă la final, nu în placă.
  Risc rămas (DEDUS, neprobat): VBIOS-ul prin PROM pe laptop poate fi altfel (ACPI `_ROM`) — se vede în primul jurnal.
- Workstation: I7 a picat o dată din două (stick lent, C-113); `gpu recupereaza` dă 0x88 (FWSEC-SB înainte = program semnat în plus → DA); ecranul îngheață după pornirea GSP-RM (varianta 11 ca probă).
- CI GitHub: **VERDE pe `6b6bb38`** (sesiunea 95; rularea 43288866245, 58 s) și pe `3d61b04` (sesiunea 94).
