# Stare: Cyber-GPU (`cyber-gpu`)

**Actualizat:** 2026-11-06 19:00 (ora României) · **de:** sesiunea Cyber-GPU 57 (cloud, fără placă) — C-83: I11 și I12 gata în SIMULARE

## Acum
- **C-83 (Adrian: „cât mai mulți pași în simulare, și după I10”) — I11 și I12 scrise și testate, doar SIMULARE, nimic pe RTX 3070 Ti.**
- **I11 — copiere mare RAM ↔ VRAM prin canalul de lucru:** un program de copiere compilat cu NAK (`copy_b128`, 288 B) pe același canal și obiect ca
  I10; nou pentru placă doar PTE-uri care arată spre paginile RAM ale OS-ului (DEDUS: aperture coerent, `VOL`). O intrare GPFIFO: marcă → RAM→VRAM →
  marcă → VRAM→RAM → marcă; verificare bit cu bit (model fără fișier) + viteza din ceasul plăcii. Test cap-coadă pe tot lanțul golden → canal, cu
  greșeli plantate prinse (T93–T95).
- **I12 — y = W·x, W în Q8_0 (operația de bază a lui Kronos):** program NAK `q8_matvec` (8 KiB, 32 fire pe rând, 128 B partajată, fără barieră
  hardware). Oracolul urmează exact operațiile din fișa NAK; verdict scris dinainte: identic / în marjă față de motorul OS / nu trece. În
  simulare, 3072 × 768 (forma `mlp.0`), W și x urcate din RAM cu I11: **identic** bit cu bit (T96–T98).
- **Lanțul:** `WINDOW_CHAIN_C83` = lanțul complet de până acum + `i11-copiere` + `i12-q8-matvec`, înainte de punerea la loc a Bus Master (T99).
- CI: verde după reparația pentru clippy 1.99 (`4ac1646`); vârful `24d9aac`, 380 teste.
- Nota pentru OS: `cyber-gpu/integration/cyber-universe/C-83_i11-i12.md`.
- Pe placă până acum: I0–I4 doar citire TREC; I6 TRECE (os-242); I7 TRECE (os-246); I8–I10 încă neîncercate (fereastra din 6 nov s-a închis fără test).

## Lista scurtă pentru fereastra de luni 9 nov (provizorie; lista finală duminică seara)
1. Pornire rece; `gpu lant` + „DA” o dată, cu `WINDOW_CHAIN_C83` (după ce OS-ul îl integrează): I6 → I7 → I8 → golden → I9 → I10.
2. **I11:** 8 MiB RAM → VRAM → RAM. Scrieri noi pe placă: **niciun registru nou** (soneria de lucru + fereastra VRAM, ca la I10); nou: GPU-ul citește și
   scrie prin DMA paginile RAM date de OS. Așteptat: `i11: 8388608 octeti; RAM->VRAM … MB/s; VRAM->RAM … MB/s`, întoarcerea identică cu modelul.
3. **I12:** 3072 × 768 Q8_0 (urcare, înmulțire, coborâre). Aceleași scrieri. Așteptat: `i12: TRECE - identic bit cu bit…`.
4. Bus Master la loc, tur de citire; jurnalul de pe stick în `rezultate/`; noi: `verifica_jurnal_lant`.

## Urmează
1. **I13** — un strat întreg al lui Kronos (LayerNorm, qkv, atenție + softmax, proiecție, GELU erf, MLP), fiecare program NAK cu oracolul lui, comparat cu
   motorul KGR1 din OS. 2. **I14** — un simbol întreg #513, apoi „un singur program pe simbol”. 3. Duminică seara: lista exactă pentru luni.
4. După fereastră: `verifica_jurnal_lant` pe jurnalul din `rezultate/`.

## Ce oferă proiectul celorlalți
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
- De la `cyber-universe`: I11 și I12 în `gpu lant` (nota `C-83_i11-i12.md`), cu paginile DMA ale OS-ului; atenție: programul `q8_matvec` are 8 KiB.
- De la Adrian: fereastra de luni și jurnalul de pe stick în `rezultate/`.

## Blocaje / nevoie de Adrian
- Nimic blocat în cyber-gpu. Pașii pe placă cer fereastra cu Adrian.
- Tag-ul `stabil-2026-10-23` (opțional; tot 403 din cloud): GitHub → cyber-gpu → Releases → „Draft a new release” → tag `stabil-2026-10-23`, Target `41e44ba` → pre-release → Publish.
