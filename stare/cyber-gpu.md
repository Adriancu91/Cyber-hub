# Stare: Cyber-GPU (`cyber-gpu`)

**Actualizat:** 2026-11-05 07:35 (ora României) · **de:** sesiunea Cyber-GPU 50 (cloud, fără placă) — C-71, lucru continuu (SIMULARE)

## Acum
- **Sesiunea 50 (C-71):** verificarea jurnalului lanțului urmărește acum și **fereastra VRAM** (`0x1700`, prin care I9 scrie tabelele de pagini):
  fiecare mutare recitită egal, iar la final fereastra pusă la loc, ca Bus Master. Testat cu jurnalul real al driverului pe modelul din
  `gpu-sim` (T85): lanțul tot TRECE, 2 greșeli plantate prinse. `8f83ce1`, 352 teste, CI verde. **Nimic testat pe RTX 3070 Ti.**
- **Fără placă nu mai rămâne nimic cu plus cinstit în cyber-gpu:** I6–I10 sunt în SIMULARE, în lanț, cu jurnalul verificat pas cu pas.
- **Sesiunea 49 (C-71):** jurnalul unei ferestre `gpu lant` complete se verifică acum **pas cu pas, dintr-o comandă**: `verifica_jurnal_lant`
  (`chain_log::check_chain_journal`; `a2f9736`; 352 teste). Reguli: pașii doar-citire fără scrieri; I6/I7 în ordinea exactă; I8 doar ferestrele
  GSP/SEC2 cu soneria întâi; golden + I9 doar sonerii (una pe apel RM) și fereastra VRAM; Bus Master pus exact la loc. Verdict: TRECE /
  OPRIT CURAT la pas / DE ANALIZAT. În simulare: TRECE, 7 greșeli plantate prinse. Lanțul simulat încarcă acum I6/I7 prin DMA, ca pe placă.
- **C-71 (lucru continuu):** tot drumul de la I6 la primul calcul e acum **un singur lanț** pentru `gpu lant`: `chain::WINDOW_CHAIN_FULL`
  (13 pași) + `run_chain_ready` — și **trece cap-coadă în SIMULARE** cu codul real (T78; `e77d986`, docs `91816ec`; 349 teste, CI verde rularea 101).
  **Nimic testat pe RTX 3070 Ti.**
- **Defect găsit în simulare, înainte de placă:** mesajele către GSP-RM (golden image, I9) nu sunau soneria GSP după fiecare mesaj — pe placă
  GSP-RM n-ar fi răspuns. Reparat prin adăugare (`QueueTransportBell`); fără sonerie, lanțul se oprește curat la golden (T79).
- C-69 (sesiunea 47): I7 verificat ca I6, costul unei lansări, lista ferestrelor `cyber-gpu/docs/FEREASTRA_C-69.md`.
- Pe placă până acum: I0–I4 doar citire TREC; I6 a scris (4 nov), FWSEC-FRTS reușit; verificarea nouă (C-66) e în os-224.
- Copia pentru OS: `integrare/cyber-gpu/snapshot/cyber-gpu.bundle` (vârf `8f83ce1`).

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
(Pașii 3–7 cer întâi partea OS din C-71; până atunci lanțul OS se oprește cinstit la I7.)

## Urmează
0. Adrian a spus „da I7–I10” (C-72, 07:27): sesiunea OS pune I7–I10 în `gpu lant` (P6-56). De la noi: nimic nou de cod; nota
   `C-71_fereastra-vram.md` (fereastra VRAM pusă la loc și la eșec). Soneria canalului de lucru `0xBB0090` (I10) e DEDUSĂ din surse —
   prima ei probă reală e la fereastră; driverul nostru doar o descrie, scrierea o face OS-ul, în lanț, după „DA”.
   După fereastră: `verifica_jurnal_lant` pe jurnalul din `rezultate/`. Fără comandă nouă sau jurnal nou: oprire scurtă.
1. Sesiunea OS: `gpu lant` pe `WINDOW_CHAIN_FULL`, pas cu pas (nota `cyber-gpu/integration/cyber-universe/C-71_gpu-lant-complet.md`).
2. Sesiunea OS (opțional): în jurnalul de pe stick, liniile `pas …` ale lanțului + numărul apelurilor RM (nota `cyber-gpu/integration/cyber-universe/C-71_jurnal-lant.md`).

## Ce oferă proiectul celorlalți
- `cyber-universe`: crate-urile no_std `gpu-core`, `gpu-pci`, `nvidia-ga104`, `gpu-compute`, `gpu-sim` (teste). Față de fixarea OS-ului (`9ac89b8`):
  **doar adăugări** — C-69: `falcon::{read_after_i7, I7Status, I7_STATUS_READS}`, `i6_log::{check_i7, check_i6_i7_journal, …}`, `launch_cost`;
  C-71: `chain::{WINDOW_CHAIN_FULL, READY_FOR_WINDOW, run_chain_ready}`, `golden::QueueTransportBell`; sesiunea 49: modulul nou `chain_log`
  (verificarea jurnalului, doar text) + unealta de gazdă `verifica_jurnal_lant`; sesiunea 50: constanta `chain_log::VRAM_WINDOW`
  (nota `cyber-gpu/integration/cyber-universe/C-71_fereastra-vram.md`: `VramWindow::restore()` și pe drumul de eroare). `WINDOW_CHAIN`, `run_chain`, `QueueTransport`,
  `check_i6` neschimbate. În `gpu-sim`: eliberarea cu marcă de timp e acceptată acum (înainte refuzată).
- `kronos` / K6-CPU: operatorii lui Kronos pe procesor, neschimbați.

## De ce are nevoie de la ceilalți
- De la `cyber-universe`: partea OS din C-71 (`gpu lant` complet, testat în QEMU cu `--sim`).
- De la Adrian: fereastra pe workstation (lista de mai sus) și jurnalul de pe stick în `rezultate/`.

## Blocaje / nevoie de Adrian
- Nimic blocat în cyber-gpu. Pașii pe placă cer fereastra cu Adrian.
- Tag-ul `stabil-2026-10-23` (opțional; tot 403 din cloud): GitHub → cyber-gpu → Releases → „Draft a new release” → tag `stabil-2026-10-23`, Target `41e44ba` → pre-release → Publish.
