# Stare: Cyber-GPU (`cyber-gpu`)

**Actualizat:** 2026-11-07 18:15 (ora României) · **de:** sesiunea Cyber-GPU 64 (cloud, fără placă) — C-87 pașii 1, 3, 4 gata în SIMULARE; pasul 2 urmează; CI verde

## Acum
- **Sesiunea 64 — C-87 (pașii 1, 3, 4 gata, doar SIMULARE; nimic pe RTX 3070 Ti).** Vârful `34a9793`, 410 teste PASS, CI verde; copia din hub (C-34) la `34a9793`.
  - **1. Generare continuă:** `kronos_gen::Generation` — N simboluri la rând, o trimitere `submit_fenced` pe poziție, cache-urile cresc; **oprire la prima
    eroare** (nimic trimis după, simbolurile făcute păstrate); viteza doar din ceasul plăcii (cu și fără pauzele driverului). Testat: 40 de simboluri ca
    procesorul; defect plantat la poziția 5 → oprire exact acolo; context plin → oprire curată.
  - **3. Recuperare fără repornire:** `recovery::recover` — ping GSP (doar citire) → grupul de canale scos de pe listă prin RM (`stop_compute_group`, niciun
    registru scris de noi) → GPGet/GPPut → **Bus Master oprit mereu**. Paginile RAM ale plăcii se eliberează doar dacă e dovedit că nimic nu le mai scrie;
    altfel carantină până la repornire, placa oprită, calculatorul merge mai departe (Kronos pe procesor).
  - **4. Modelul mare (24 straturi, 183M):** 387 lansări/poziție, testat pe canal (E 128) ca procesorul; `VramBudget` calculează VRAM-ul înainte de urcare:
    183M ≈ 270 MiB, #513 ≈ 142 MiB. **Pentru 24 de straturi zona de pushbuffer trebuie să fie 32 KiB** (16 KiB țin o singură poziție).
  - **2. „Un singur program pe simbol”:** neînceput (program NAK nou, „megakernel”) — următorul pas.
  - Nota pentru OS: `cyber-gpu/integration/cyber-universe/C-87_generare.md` (ce să lege OS-ul la P6-66).
- **Sesiunea 63 — oprire scurtă.** Nicio comandă, jurnal sau întrebare nouă (C-84 la OS și C-85/C-86 la Kronos nu ne privesc); 394 teste PASS local,
  CI verde. Codul neschimbat față de `d706cbb` (copia din hub rămâne bună).
- **Sesiunea 62 — oprire scurtă.** Nicio comandă, jurnal sau întrebare nouă; OS-ul are I11–I14, `kronos --gpu` și pushbuffer-ul de 16 KiB (P6-60, P6-62 gata),
  fixat pe `d706cbb`. Copia din hub rămâne la `d706cbb` (codul e identic; `c6e8c8d` schimbă doar starea).
- **Sesiunea 61 — răspuns la întrebarea OS (zona de pushbuffer ≥ 16 KiB pentru #513): DA, 16 KiB e bine.** Un simbol #513 = 7 832 B
  (`kronos_model::push_bytes_per_token(12)`, adăugare); 16 KiB țin două simboluri în zbor (următorul se scrie cât placa îl execută pe cel curent),
  al treilea e refuzat, nu suprascris; testat pe 512 simboluri la rând (aritmetica zonei, SIMULARE). Detalii: `cyber-gpu/integration/cyber-universe/C-83_i14.md`.
  Copia din hub (C-34) la `d706cbb`, verificată prin clonare + 394 teste PASS.
- **Sesiunea 60: copia din hub (`integrare/cyber-gpu/snapshot/cyber-gpu.bundle`, C-34) e acum la `bc2f22b`** (include I11–I14 de la `e681bea` și
  testele KGR1 de la `76bf13c`); verificată prin clonare de probă + toate testele (393 PASS). Sesiunea OS poate începe P6-62.
- **C-83 (Adrian: „cât mai mulți pași în simulare, și după I10”) — I11, I12, I13 și I14 scrise și testate, doar SIMULARE, nimic pe RTX 3070 Ti.**
- **I13 (sesiunea 58) — un strat Kronos întreg:** 16 lansări pe poziție (programe NAK noi: `vadd`, `layernorm`, `attention`, `gelu`), cache-urile
  cheie/valoare cresc în VRAM; comparat cu motorul procesorului în toleranța scrisă dinainte (1e-4 + 1e-4·|x|). Strat 768/12 capete: abatere < 1e-5
  în simulare; greșelile plantate (rezidual lipsă, atenție scurtată, GELU sărit) nu trec (T100–T103).
- **I14 (sesiunea 58) — un simbol întreg:** `embed` (NAK) + toate straturile + LayerNorm final + logit-uri = `16·straturi + 3` lansări (195 pentru
  #513); generarea greedy pe un model mic sintetic dă **aceleași simboluri** ca procesorul, logit-urile în 1e-3 (T104–T105). #513 însuși se încearcă
  doar pe placă, citit de OS de pe stick. `WorkQueue::submit_fenced` refolosește zona de pushbuffer după fiecare simbol.
- **I14 față de Kronos (sesiunea 59):** vectorii de control KGR1 din hub (`integrare/kronos/vectori`, model minuscul cu greutăți la întâmplare)
  dau, prin oracolul nostru pe procesor și prin canalul de lucru SIMULAT, exact simbolurile motorului de referință al lui Kronos (argmax pe fiecare
  poziție, 5 greedy), logit-urile la ≤ 4,6e-6 (pragul 1e-3). Vectorii rămân în hub (privat): testele (T106) rulează doar local, nu în CI.
- **I11 — copiere mare RAM ↔ VRAM prin canalul de lucru:** un program de copiere compilat cu NAK (`copy_b128`, 288 B) pe același canal și obiect ca
  I10; nou pentru placă doar PTE-uri care arată spre paginile RAM ale OS-ului (DEDUS: aperture coerent, `VOL`). O intrare GPFIFO: marcă → RAM→VRAM →
  marcă → VRAM→RAM → marcă; verificare bit cu bit (model fără fișier) + viteza din ceasul plăcii. Test cap-coadă pe tot lanțul golden → canal, cu
  greșeli plantate prinse (T93–T95).
- **I12 — y = W·x, W în Q8_0 (operația de bază a lui Kronos):** program NAK `q8_matvec` (8 KiB, 32 fire pe rând, 128 B partajată, fără barieră
  hardware). Oracolul urmează exact operațiile din fișa NAK; verdict scris dinainte: identic / în marjă față de motorul OS / nu trece. În
  simulare, 3072 × 768 (forma `mlp.0`), W și x urcate din RAM cu I11: **identic** bit cu bit (T96–T98).
- **Lanțul:** `WINDOW_CHAIN_C83` = lanțul complet de până acum + `i11-copiere` + `i12-q8-matvec` + `i13-strat` + `i14-simbol`, înainte de punerea
  la loc a Bus Master.
- CI verde; vârful `d706cbb`, 394 teste (+3 locale cu vectorii KGR1).
- Notele pentru OS: `cyber-gpu/integration/cyber-universe/C-83_i11-i12.md`, `C-83_i13.md`, `C-83_i14.md`, `C-83_i14_vectori.md`.
- Pe placă până acum: I0–I4 doar citire TREC; I6 TRECE (os-242); I7 TRECE (os-246); I8–I10 încă neîncercate (fereastra din 6 nov s-a închis fără test).

## Lista scurtă pentru fereastra de luni 9 nov (provizorie; lista finală duminică seara)
1. Pornire rece; `gpu lant` + „DA” o dată, cu `WINDOW_CHAIN_C83` (după ce OS-ul îl integrează): I6 → I7 → I8 → golden → I9 → I10.
2. **I11:** 8 MiB RAM → VRAM → RAM. Scrieri noi pe placă: **niciun registru nou** (soneria de lucru + fereastra VRAM, ca la I10); nou: GPU-ul citește și
   scrie prin DMA paginile RAM date de OS. Așteptat: `i11: 8388608 octeti; RAM->VRAM … MB/s; VRAM->RAM … MB/s`, întoarcerea identică cu modelul.
3. **I12:** 3072 × 768 Q8_0 (urcare, înmulțire, coborâre). Aceleași scrieri. Așteptat: `i12: TRECE - identic bit cu bit…`.
4. **I13:** un strat sintetic 768/12 pe 4 poziții. Aceleași scrieri, ~12 MB VRAM. Așteptat: `i13: pozitia 0..3: TRECE …`.
5. **I14a (propunere):** întâi modelul minuscul `mic_q8_0.kgr` (hub `integrare/kronos/vectori`), 35 de lansări pe simbol, comparat cu `vectori.json` — răspunsul exact e cunoscut. Aceleași scrieri.
6. **I14:** #513 de pe stick, textele de control, 5 simboluri greedy fiecare (195 de lansări pe simbol). Aceleași scrieri, ~150 MB VRAM. Așteptat:
   `i14: … TRECE - simbolul … ca procesorul` și simbolurile din `MODEL.md` pentru #513. Durata fiecărei lansări în jurnal.
7. Bus Master la loc, tur de citire; jurnalul de pe stick în `rezultate/`; noi: `verifica_jurnal_lant`.

## Urmează
0. C-87 pasul 2: „un singur program pe simbol” (program NAK persistent + modelul lui în `gpu-sim`, comparat cu cele 195 de lansări).
1. Duminică seara: lista exactă pentru luni (după ce OS-ul integrează I11–I14).
2. „Un singur program pe simbol” — doar după ce placa ne spune cât costă cele 195 de lansări (I14 le măsoară).
3. După fereastră: `verifica_jurnal_lant` pe jurnalul din `rezultate/`.

## Ce oferă proiectul celorlalți
- **Sesiunea 64 (C-87, doar adăugări):** `kronos_gen` (`Generation`, `GenPlan`, `TokenRunner`, `TokenCheck`, `Stop`, `GenStats`, `TokenOutput`, `VramBudget`,
  `push_bytes_with_copy`), `recovery` (`recover`, `RecoveryOps`, `Recovered`, `RamPages`, `NextChain`, `classify`, `Hang`), `user_space::stop_compute_group`,
  `transfer::records_seen`, `GpuMemory::vram_free`, `RangeAllocator::largest_free`. Copia din hub la `34a9793`.
- **Sesiunea 61 (doar adăugare):** `kronos_model::push_bytes_per_token(layers)`; copia din hub la `d706cbb`.
- **Sesiunea 60:** nicio schimbare de cod; copia din hub la `bc2f22b` — de fixat în OS pentru C-83 (sau `0974ecd`, același cod).
- **Sesiunea 59:** nicio schimbare în crate-uri (doar teste + `tools/vectori-kgr1/pregateste.py`).
- **Nou (sesiunea 58, C-83, doar adăugări):** `kronos_layer` (I13: `Prog`, `PROGRAMS`, `Launch::qmd`, `LayerVas`, `WeightVas`, `token_launches`,
  `test_layer`, `judge`), `kronos_model` (I14: `ModelVas`, `token_launches`, `launches_per_token`, `test_model`, `judge`), `WorkQueue::submit_fenced`,
  `gpu_compute::{layer, model}`; în `gpu-sim`: `vadd/layernorm/attention/gelu/embed_on_cpu`; lanțul: `i13-strat`, `i14-simbol`.
- **Nou (sesiunea 57, C-83, doar adăugări):** `mmu::{encode_pte_sys, SysMapping, map_sys, alloc_sys_mapped, lookup_sys}`; modulul `transfer` (I11:
  `COPY_B128`, `copy_cbuf`, `copy_qmd`, `encode_round_trip`, `analyze_round_trip`, `encode_sequence`, `analyze_sequence`, modelul de test); modulul
  `q8_matvec` (I12: `Q8_MATVEC`, `q8_cbuf`, `q8_qmd`, `test_matrix`, `judge`/`Verdict`); `chain::{WINDOW_CHAIN_C83, READY_FOR_WINDOW_C83}`;
  `gpu_compute::q8`; în `gpu-sim`: `translate_any`, `GpuMem::{load_from, store_to}`, `copy_b128_on_cpu`, `q8_matvec_on_cpu`. `nvidia-ga104` depinde
  acum normal de `gpu-compute`. Nimic redenumit sau șters.
- **Nou (sesiunea 54, doar adăugare):** `gpu_sim::fake_gsp::FakeGsp::wpr_meta_mem` (Booter-ul simulat lărgește WPR2 din `GspFwWprMeta`); implicit `None` = ca înainte.
- **Nou (sesiunea 53, doar adăugare):** `FbLayout::free_after_i7` (zona VRAM verificată pe WPR2 recitit după I7); `free_below` neschimbat.
- **Nou (sesiunea 52, doar adăugare):** `push::DOORBELL` (soneria canalului de lucru, din antetul MIT); `DOORBELL_INFERRED`, `chain_log::WORK_DOORBELL` neschimbate.
- **Nou (sesiunea 51, doar adăugări):** `falcon::{booter_load_dma_libos, gsp_reset_into_riscv, write_libos_mailboxes, GSP_RM_APP_VERSION_570_144, GSP_BCR_RISCV}`,
  `i6_log::{check_i7_libos, I7LibosSummary}`, câmpul `ChainJournal::i7_libos`, `I6Check::wpr2_stage` + faptul de tur `i6.wpr2.etapa`; în `gpu-sim`:
  `FakeGsp::{gsp_mailbox_locked, libos_at_booter}`. `booter_load_dma`, `check_i7`, `i6.trece` neschimbate.
- `cyber-universe`: crate-urile no_std `gpu-core`, `gpu-pci`, `nvidia-ga104`, `gpu-compute`, `gpu-sim` (teste). Față de fixarea OS-ului (`9ac89b8`):
  **doar adăugări** — C-69: `falcon::{read_after_i7, I7Status, I7_STATUS_READS}`, `i6_log::{check_i7, check_i6_i7_journal, …}`, `launch_cost`;
  C-71: `chain::{WINDOW_CHAIN_FULL, READY_FOR_WINDOW, run_chain_ready}`, `golden::QueueTransportBell`; sesiunea 49: modulul nou `chain_log`
  (verificarea jurnalului, doar text) + unealta de gazdă `verifica_jurnal_lant`; sesiunea 50: constanta `chain_log::VRAM_WINDOW`
  (nota `cyber-gpu/integration/cyber-universe/C-71_fereastra-vram.md`: `VramWindow::restore()` și pe drumul de eroare). `WINDOW_CHAIN`, `run_chain`, `QueueTransport`,
  `check_i6` neschimbate. În `gpu-sim`: eliberarea cu marcă de timp e acceptată acum (înainte refuzată).
- `kronos` / K6-CPU: operatorii lui Kronos pe procesor, neschimbați.

## De ce are nevoie de la ceilalți
- De la `cyber-universe` (P6-66): `Generation::run` + `VramBudget::check` în `kronos --gpu`, `recover` la erorile de după I10; 32 KiB de pushbuffer pentru 24 de straturi.
- De la `cyber-universe`: I11–I14 în `gpu lant` și `kronos --gpu` (notele `C-83_*.md`), cu paginile DMA ale OS-ului; atenție: programele
  `q8_matvec`, `layernorm`, `attention` au peste 4 KiB, iar zona de pushbuffer pentru I14 trebuie să aibă ≥ 8 KiB (16 KiB, cum propuneți, e mai bine: două simboluri în zbor).
- De la Adrian: fereastra de luni și jurnalul de pe stick în `rezultate/`.

## Blocaje / nevoie de Adrian
- Nimic blocat în cyber-gpu. Pașii pe placă cer fereastra cu Adrian.
- Tag-ul `stabil-2026-10-23` (opțional; tot 403 din cloud): GitHub → cyber-gpu → Releases → „Draft a new release” → tag `stabil-2026-10-23`, Target `41e44ba` → pre-release → Publish.
- 2026-11-07 01:35 · sesiunea 61 · răspuns OS: 16 KiB de pushbuffer pentru #513 = două simboluri în zbor (7 832 B fiecare); `push_bytes_per_token` + test; copia din hub la `d706cbb`.
