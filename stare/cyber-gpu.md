# Stare: Cyber-GPU (`cyber-gpu`)

**Actualizat:** 2026-11-06 01:35 (ora României) · **de:** sesiunea Cyber-GPU 54 (cloud, fără placă) — Booter-ul simulat lărgește WPR2 ca placa (observația OS)

## Acum
- **Sesiunea 54 — observația OS „`FakeGsp` nu lărgește WPR2 după Booter”:** rezolvată în `gpu-sim`. Câmp nou `FakeGsp::wpr_meta_mem` (memoria de
  sistem simulată cu `GspFwWprMeta`); Booter-ul simulat coboară WPR2 LO la `gspFwWprStart` din meta, HI rămâne cel de la I6 — ca placa la 5 nov
  (`0x1f4100000..0x1ffee0000`); meta greșit → refuz (cod SIM `0xbad2`). T92, `657e209`, 359 teste, CI verde. Nota (opțională):
  `cyber-gpu/integration/cyber-universe/C-71_wpr2-largit-in-sim.md`. **SIMULARE, nimic testat pe RTX 3070 Ti.**
- **Sesiunea 53 — zona VRAM pentru golden/I9/I10 (cererea OS din `stare/cyber-universe.md`):** pe WPR2 citit pe placă după I7 (5 nov,
  `0x1f4100000..0x1ffee0000`), aranjamentul nostru dă același început; zona OS (`max(ecran, 256 MiB)` … `free_below()`) se termină la `0x1f4000000`,
  sub heap-ul non-WPR și sub WPR2 → **zona e bună**. Verificare nouă, doar aritmetică: `FbLayout::free_after_i7(wpr2_citit)` (eroare înainte de orice
  scriere în VRAM dacă WPR2 nu e unde a cerut `GspFwWprMeta`), T91; `60740a3`, 358 teste. Nota: `cyber-gpu/integration/cyber-universe/C-71_zona-vram-dupa-i7.md`.
  **Nimic testat pe RTX 3070 Ti.**
- **Sesiunea 52 — întrebarea 3 a OS (I10):** soneria canalului de lucru `0xBB0090` e acum **DOCUMENTATĂ** (antetul MIT 570.144 `tu102/dev_vm.h`:
  `NV_VIRTUAL_FUNCTION_DOORBELL = 0x30090` la baza `0xB80000`; calea RM 570.144 pentru GA104 citită ca specificație), nu doar dedusă. Constanta nouă
  `push::DOORBELL` (= `DOORBELL_INFERRED`, verificat la compilare, T90; `20b4a3b`, 357 teste). Pe placă: încă neobservată; prima scriere = I10 în lanț.
  Nota pentru OS: `cyber-gpu/integration/cyber-universe/C-72_soneria-i10.md` (doar în pasul I10, citiri prin `VramWindow::read_u32`, `invalidate_tlb` înainte).
- **C-75 — de ce I8 s-a oprit pe placă (os-246):** jurnalul real arată `bar0 w 0x110040: 0x00000000 <- 0x09c71000 => 0x00000000` — **cutia GSP nu a
  păstrat adresa LibOS**. Booter a mers (cutia SEC2 = 0, WPR2 lărgit, RISC-V activ), dar GSP-RM a pornit fără adresa argumentelor LibOS, deci nu și-a
  făcut cozile. Cauza (DEDUS, ordinea nouveau / RM 570.144): după FWSEC, GSP trebuie **resetat în modul RISC-V** înainte de cutii.
- **Reparația, în SIMULARE** (`8ed3993`, `a701cb9`; 356 teste, toate verificările trec): `falcon::booter_load_dma_libos` = resetare GSP + BCR_CTRL = 0x111 →
  cutiile LibOS **recitite** (dacă nu se păstrează: oprire înainte de Booter) → Booter → `FALCON_OS` = 570144 → RISC-V activ. Simulatorul reproduce
  placa (ordinea veche: I7 TRECE, I8 oprit), iar în ordinea nouă trece tot lanțul. `verifica_jurnal_lant` numește cauza pe jurnalul real.
  **Nimic testat pe RTX 3070 Ti.**
- Răspunsuri C-75: (1) `0xa0` la `0x111388` = RISC-V **activ** (bitul 7), nu oprit; (2) cele ~2 s nu sunt cauza; (3) formatul cozii se vede abia când
  există coada. Turul de după: fapt nou `i6.wpr2.etapa` („lărgit pentru GSP-RM (după I7)” e normal).
- Pentru OS: `cyber-gpu/integration/cyber-universe/C-75_i7-reset-gsp-libos.md` — la I7 un singur apel `booter_load_dma_libos(…, I7Prep::libos)`
  în locul scrierilor proprii; 3 scrieri noi, toate în fereastra GSP. Răspunde și la întrebarea 1 a sesiunii OS.
- Copia pentru OS: `integrare/cyber-gpu/snapshot/cyber-gpu.bundle` (vârf `657e209`).
- Pe placă până acum: I0–I4 doar citire TREC; **I6 TRECE** (os-242); **I7 TRECE** (os-246, Booter); I8 oprit — cauza de mai sus.

## Lista scurtă pentru fereastra pe hardware (în ordine; `gpu lant` + „DA” le rulează pe toate, oprire la primul eșec)
1. Pornire rece (cablul scos 30 s); `gpu pregatire-i6` → „WPR2 coborat”, 0 scrieri.
2. Bus Master pornit → I6 FWSEC-FRTS → WPR2 citit: „capat: ultimul bloc de 128 KiB”.
3. I7 Booter pe SEC2 → citit: cutia SEC2 = 0, GSP RISC-V ACTIV.
4. I8: SetSystemInfo + SetRegistry, soneria, secvențiatorul → `GSP_INIT_DONE`.
5. Golden image + I9 (canalul de lucru): fiecare răspuns RM = 0.
6. I10: `add64` → rezultat identic bit cu bit cu procesorul (abia atunci „executat pe GPU”).
7. Costul unei lansări: 16 lansări cu marcă de timp → mediana.
8. Bus Master la loc, tur de citire, oprire completă; jurnalul de pe stick + poze în `rezultate/`.
9. Noi, după: `verifica_jurnal_lant <jurnal> <adresa GspFwWprMeta> [apeluri RM]` → TRECE / OPRIT CURAT / DE ANALIZAT.
(Toți pașii sunt în OS din `os-249`, testați doar în SIMULARE.)

## Urmează
0. Fereastra următoare pe workstation cu `os-250` (sau `os-249`) (tot lanțul I6 → I10 e în OS): pornire rece, `gpu lant` + DA o dată. Așteptat: rândul
   `0x110040 … => 0x09c71000` (adresa LibOS păstrată) și I8 TRECE; apoi golden, I9, I10 (`add64` bit cu bit).
1. După fereastră: `verifica_jurnal_lant <jurnal> <adresa GspFwWprMeta>` pe jurnalul din `rezultate/`.
2. Dacă I8 trece pe placă: compararea zonei VRAM cu regiunile FB raportate de GSP-RM (`GET_GSP_STATIC_INFO`, DEDUS).
3. Fără comandă nouă sau jurnal nou: sesiunile cyber-gpu se opresc scurt (nimic cu plus cinstit fără placă).

## Ce oferă proiectul celorlalți
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
- De la `cyber-universe`: jurnalele `gpu lant` cu `os-250`; opțional, în `gpu lant --sim`, meta-ul în model (`wpr_meta_mem`) în loc de LO-ul scris de mână.
- De la Adrian: fereastra următoare pe workstation și jurnalul de pe stick în `rezultate/`.

## Blocaje / nevoie de Adrian
- Nimic blocat în cyber-gpu. Pașii pe placă cer fereastra cu Adrian.
- Tag-ul `stabil-2026-10-23` (opțional; tot 403 din cloud): GitHub → cyber-gpu → Releases → „Draft a new release” → tag `stabil-2026-10-23`, Target `41e44ba` → pre-release → Publish.
- 2026-11-06 01:35 — sesiunea 54 (cloud, fără placă): observația OS rezolvată în SIMULARE — Booter-ul simulat lărgește WPR2 din `GspFwWprMeta` ca placa (`FakeGsp::wpr_meta_mem`, T92); 359 teste, CI verde, `657e209`; nota pentru OS.
