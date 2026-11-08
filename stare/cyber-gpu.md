# Stare: Cyber-GPU (`cyber-gpu`)

**Actualizat:** 2026-11-08 07:50 (ora României) · **de:** sesiunea Cyber-GPU 68 (cloud, fără placă) — C-83: unealta de verificare a jurnalului știe lanțul de luni (17 pași); lista GPU pentru 9 nov; CI GitHub pică în 2 s fără jurnal (nu codul)

## Acum
- **Sesiunea 68 — pregătire pentru luni (C-83).** Unealta `verifica_jurnal_lant` știa doar lanțul până la I10 (13 pași); jurnalul de luni (17 pași, cu I11–I14)
  ar fi ieșit „de analizat” fără motiv. Acum recunoaște singură lanțul C-83 și verifică și I11–I14 (doar fereastra VRAM + soneria de lucru; orice altă
  scriere e numită cu pasul ei) — test T107, doar SIMULARE pe text. Lista GPU pentru luni: `cyber-gpu/docs/FEREASTRA_C-83.md`. Vârful `84d3685`, 416 teste PASS
  local (doar adăugări; OS-ul nu are nimic de schimbat, `34a9793` rămâne bun). **CI GitHub:** din 7 nov 23:28 ambele joburi pică în ~2 s, fără jurnal
  (repornit o dată, la fel) — mașina GitHub nu pornește, nu e o eroare de cod.
- **Sesiunea 67 — oprire scurtă.** Nicio comandă, jurnal sau întrebare nouă (OS: „cyber-gpu: nimic urgent”); CI verde, 415 teste PASS local; vârful `0e86d1a`
  schimbă doar starea — codul și copia din hub rămân la `ed75615`. Următorul pas: lista pentru luni, duminică seara.
- **Sesiunea 66 — oprire scurtă.** Nicio comandă, jurnal sau întrebare nouă (C-88 e la Kronos); CI verde pe `ed75615`, 415 teste PASS local.
  Codul neschimbat față de `ed75615` (`25566e5` schimbă doar starea), copia din hub rămâne bună. Următorul pas: lista pentru luni, duminică seara.
- **Sesiunea 65 — C-87 pasul 2 gata (SIMULARE + compilat, NU rulat): „un singur program pe simbol”.** `token.comp` (Mesa NAK: 43 232 B, 35 registre, 0 memorie
  locală) rulează toată lista unui simbol într-o lansare (G grupuri × 32 fire, barieră pe toată placa între operații). În `gpu-sim` logit-urile ies **bit cu bit**
  ca la lansările separate (E 64 și E 768). Bariera pe placă NU e dovedită — propunerea noastră: luni doar lansările separate; acest program după ce ele trec.
  Vârful `ed75615`, 415 teste PASS; copia din hub (C-34) la `ed75615`. Cu asta, **partea GPU din C-87 e toată gata în simulare**.
- **Sesiunea 64 — C-87 (pașii 1, 3, 4 gata, doar SIMULARE; nimic pe RTX 3070 Ti).** Vârful `34a9793`, 410 teste PASS, CI verde; copia din hub (C-34) la `34a9793`.
  - **1. Generare continuă:** `kronos_gen::Generation` — N simboluri la rând, o trimitere `submit_fenced` pe poziție, cache-urile cresc; **oprire la prima
    eroare** (nimic trimis după, simbolurile făcute păstrate); viteza doar din ceasul plăcii (cu și fără pauzele driverului). Testat: 40 de simboluri ca
    procesorul; defect plantat la poziția 5 → oprire exact acolo; context plin → oprire curată.
  - **3. Recuperare fără repornire:** `recovery::recover` — ping GSP (doar citire) → grupul de canale scos de pe listă prin RM (`stop_compute_group`, niciun
    registru scris de noi) → GPGet/GPPut → **Bus Master oprit mereu**. Paginile RAM ale plăcii se eliberează doar dacă e dovedit că nimic nu le mai scrie;
    altfel carantină până la repornire, placa oprită, calculatorul merge mai departe (Kronos pe procesor).
  - **4. Modelul mare (24 straturi, 183M):** 387 lansări/poziție, testat pe canal (E 128) ca procesorul; `VramBudget` calculează VRAM-ul înainte de urcare:
    183M ≈ 270 MiB, #513 ≈ 142 MiB. **Pentru 24 de straturi zona de pushbuffer trebuie să fie 32 KiB** (16 KiB țin o singură poziție).
  - **2. „Un singur program pe simbol”:** gata în sesiunea 65 (vezi mai sus).
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

## Lista pentru fereastra de luni 9 nov (partea GPU; detaliile în `cyber-gpu/docs/FEREASTRA_C-83.md`)
1. Pornire rece; stick-ul de test cu Release-ul OS cel mai nou (`os-275`) + stick-ul cu firmware 570.144; în `kronos\` pe stick: `mic_q8_0.kgr` și #513.
2. `gpu lant` + „DA” o dată: I6 → I7 → I8 → golden → I9 → I10 → cost lansare → I11 → I12 → I13 → I14 → Bus Master la loc → tur.
3. Scrieri noi față de 5 nov: la I7 **3** (resetul GSP în RISC-V, C-75); la I8 soneria GSP + secvențiatorul (doar ferestrele GSP/SEC2); golden/I9: soneria GSP
   pe mesaj + fereastra VRAM; de la I10 soneria de lucru `0xbb0090`; I11–I14: **niciun registru nou** (nou: placa citește/scrie prin DMA paginile RAM ale OS-ului).
4. Cel mai probabil punct de oprire: I7 (ordinea nouă, prima dată pe placă) sau I8 (prima dată). O oprire curată acolo e un rezultat bun.
5. Dacă tot lanțul trece: `kronos --gpu` cu #513 (generare continuă, oprire la prima eroare). „Un singur program pe simbol” NU luni.
6. După: jurnalul în `rezultate/`; noi rulăm `verifica_jurnal_lant` (recunoaște singur lanțul C-83).

## Urmează
1. Duminică seara: recitesc lista OS-ului (P6-63) și potrivesc lista de mai sus dacă s-a schimbat ceva.
2. Luni, după fereastră: `verifica_jurnal_lant` pe jurnalul din `rezultate/`.
3. „Un singur program pe simbol” — doar după ce lansările separate trec pe placă.

## Ce oferă proiectul celorlalți
- **Sesiunea 68 (doar adăugări, unelte de gazdă):** `chain_log::{check_chain_journal_for, chain_for_journal, step_ids_for}`, `ChainJournal::verdict_for`; nimic de schimbat în OS.
- **Sesiunea 65 (doar adăugări):** `kronos_token` (`TOKEN`, `TOKEN_REGISTERS`, `work_list`, `token_cbuf`, `token_qmd`, `groups_for`, `op_number`); `gpu-sim` `token_on_cpu`, `TOKEN_NEEDS`. Copia la `ed75615`.
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
- CI-ul GitHub al `cyber-gpu` nu pornește (pică în 2 s, fără jurnal, din 7 nov 23:28). Dacă ține: GitHub → Settings → Billing and plans / Actions — de văzut dacă e vreo limită sau oprire pe cont. Testele locale trec (416).
- Tag-ul `stabil-2026-10-23` (opțional; tot 403 din cloud): GitHub → cyber-gpu → Releases → „Draft a new release” → tag `stabil-2026-10-23`, Target `41e44ba` → pre-release → Publish.
