# Stare: Cyber-GPU (`cyber-gpu`)

**Actualizat:** 2026-11-04 23:15 (ora României) · **de:** sesiunea Cyber-GPU 47 (cloud, fără placă) — C-69, partea fără placă, gata (SIMULARE)

## Acum
- **C-69 (F5 din planul independenței):** codul pentru I7–I10 exista deja în SIMULARE; azi s-a adăugat ce lipsea pentru ferestre
  (`677dfbf`, `d5bf45a`, docs `604852b`; 346 teste, CI verde rularea 100). **Nimic testat pe RTX 3070 Ti.**
  - I7 (Booter pe SEC2) e verificat la fel de strict ca I6: lista exactă a celor 18 registre SEC2 (T72), verificarea jurnalului I6 + I7 de pe
    stick (`check_i6_i7_journal`, 8 greșeli plantate prinse, T73), rezultatul I7 citit **fără permis** (`read_after_i7`, 3 citiri, T74),
    unealta `verifica_jurnal_i7`.
  - Ținta „un singur program pe simbol”, primul pas: **costul unei lansări** măsurat de placă însăși, din mărci de timp (`launch_cost`, T75);
    în simulare cifrele sunt ale testului, doar metoda e verificată.
  - Lista ferestrelor cu Adrian: `cyber-gpu/docs/FEREASTRA_C-69.md` — 0: I6 o dată (os-224) → 1: I7 → 2: I8 → 3: golden + I9 → 4: primul calcul
    (`add64`) + costul lansării → apoi treptele matmul și Kronos pe placă.
- Pe placă până acum: I0–I4 doar citire TREC; I6 a scris (4 nov), FWSEC-FRTS a reușit; verificarea nouă (C-66) e în os-224.
- Copia pentru OS: `integrare/cyber-gpu/snapshot/cyber-gpu.bundle` (vârf `604852b`).

## Urmează
1. Fereastra 0 cu Adrian (os-224): pornire rece, `gpu pregatire-i6`, `gpu i6 --scrie` o dată → jurnalul în `rezultate/` → `verifica_jurnal_i6`.
2. Fără placă, între timp: lista exactă a scrierilor I8 (soneria + secvențiatorul) și verificarea ei în jurnal, ca la I6/I7.
3. Dacă I6 trece: comandă nouă pentru fereastra 1 (I7) — partea OS e descrisă în `cyber-gpu/integration/cyber-universe/C-69_i7-fereastra.md`.

## Ce oferă proiectul celorlalți
- `cyber-universe`: crate-urile no_std `gpu-core`, `gpu-pci`, `nvidia-ga104`, `gpu-compute`, `gpu-sim` (teste). Față de fixarea OS-ului (`9ac89b8`):
  **doar adăugări** — `gsp::falcon::{read_after_i7, I7Status, I7_STATUS_READS}`, `i6_log::{check_i7, check_i6_i7_journal, I6I7Journal, SEC2_LO, SEC2_HI,
  GSP_RISCV_CPUCTL}`, modulul `launch_cost`, câmpurile noi din `gpu_sim::cmdproc::CommandProcessor` (`gpu_time_ns`, `sim_launch_ns`, `sim_method_ns`,
  `timestamps`). Schimbare de comportament (doar simulare): `gpu-sim` **acceptă** acum eliberarea de semafor cu marcă de timp (înainte o refuza).
  `check_i6` are același rezultat (rescris pe o funcție comună cu I7). Nota: `integration/cyber-universe/C-69_i7-fereastra.md`.
- `kronos` / K6-CPU: operatorii lui Kronos pe procesor, neschimbați.

## De ce are nevoie de la ceilalți
- De la Adrian: fereastra 0 pe workstation (I6 o dată, pornire rece, os-224) și jurnalul de pe stick copiat în `rezultate/`.
- De la `cyber-universe`: după I6 TRECE și o comandă nouă, comanda `gpu i7 --scrie` (propunerea din nota C-69).

## Blocaje / nevoie de Adrian
- Nimic blocat în cyber-gpu. Pasul următor pe placă cere fereastra cu Adrian.
- Tag-ul `stabil-2026-10-23` (opțional; tot 403 din cloud): GitHub → cyber-gpu → Releases → „Draft a new release” → tag `stabil-2026-10-23`, Target `41e44ba` → pre-release → Publish.
