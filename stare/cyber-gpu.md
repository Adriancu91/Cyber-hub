# Stare: Cyber-GPU (`cyber-gpu`)

**Actualizat:** 2026-11-04 19:40 (ora României) · **de:** sesiunea Cyber-GPU 46 (cloud, fără placă) — C-66, partea cyber-gpu, gata (SIMULARE)

## Acum
- **Pe placa reală (4 nov, os-222):** I6 a rulat FWSEC-FRTS; LO = `0x1ffe00` (exact începutul zonei), HI = `0x1ffee0` = începutul ultimului
  bloc de 128 KiB al zonei de 1 MiB → **FWSEC-FRTS a reușit pe placă**; doar verificarea noastră nu cunoștea această formă și a zis „NU TRECE”.
- **C-66 (partea cyber-gpu) gata, doar în SIMULARE** (`9ac89b8` + docs `cf8cd92`, 338 teste, verificările locale trec):
  - `check_frts` (folosit de I6) acceptă acum și „ultimul bloc de 128 KiB”; cu valorile din 4 nov ar da TRECE (T70);
  - citirea WPR2 de după I6 se face cu o funcție nouă **doar de citire** (`falcon::read_frts_after_i6`): fără permis, 3 registre de stare, fiecare
    citire intră în jurnal (T71) — repară „nepermis de politica de siguranta”;
  - `gpu-sim` scrie HI ca placa (128 KiB).
- Jurnalul real `gpu-jurnal-002.txt` (3 nov) verificat cu `verifica_jurnal_i6`: ordinea celor 720 de scrieri I6 **TRECE**, Bus Master pornit și
  pus la loc; HI nu era în acel jurnal (codul vechi nu jurnaliza citirile) — de aceea funcția nouă le jurnalizează.
- Copia pentru OS: `integrare/cyber-gpu/snapshot/cyber-gpu.bundle` (vârf `cf8cd92`).
- Pe placă până acum: I0–I4 doar citire TREC; I6 a scris (2 în configurație + 720 în registrele GSP), toate în ferestrele permise; FWSEC-FRTS reușit.

## Urmează
1. Sesiunea OS: partea ei din C-66 — fixarea ≥ `9ac89b8`, înlocuirea unei funcții în `gpu_i6.rs` (exact cum scrie în
   `cyber-gpu/integration/cyber-universe/C-66_wpr2-bloc-128k.md`), Release nou.
2. Fereastra următoare, cu Adrian: pornire rece (cablul scos 30 s), `gpu pregatire-i6`, `gpu i6 --scrie` **o singură dată** → așteptat TRECE și
   „capat: ultimul bloc de 128 KiB”; jurnalul de pe stick în hub `rezultate/` → noi rulăm `verifica_jurnal_i6`.
3. Dacă I6 trece: plan pentru I7 (Booter), doar cu o comandă nouă.

## Ce oferă proiectul celorlalți
- `cyber-universe`: crate-urile no_std `gpu-core`, `gpu-pci`, `nvidia-ga104`, `gpu-compute`, `gpu-sim` (teste). Față de fixarea OS-ului (`3286a3b`):
  **doar adăugări** — sesiunea 42: `i6_log::{check_stick_journal, StickJournal}`; sesiunea 46 (C-66): `gsp::falcon::{compare_frts_full, check_frts_full,
  FrtsCheckFull, Wpr2EndForm (#[non_exhaustive], label()), WPR2_BLOCK_128K, StatusReadBar0, read_frts_after_i6}`, `i6_log::wpr2_after_i6_full`,
  câmpul `StickJournal::wpr2_full`, `FakeGsp::wpr2_hi_back` (implicit 128 KiB). `check_frts` are același nume și semnătură, dar acceptă și forma plăcii.
  `check_frts_detail` / `Wpr2End` rămân neschimbate (refuză forma de 128 KiB) → pentru afișare, OS-ul trece pe `read_frts_after_i6`.
  Nota completă: `integration/cyber-universe/C-66_wpr2-bloc-128k.md`.
- `kronos` / K6-CPU: operatorii lui Kronos pe procesor, neschimbați.

## De ce are nevoie de la ceilalți
- De la `cyber-universe`: partea OS din C-66 (fixare ≥ `9ac89b8` + Release cu stick-ul de test).
- De la Adrian: fereastra următoare pe workstation (I6 o dată, pornire rece) și jurnalul de pe stick copiat în `rezultate/`.

## Blocaje / nevoie de Adrian
- Nimic blocat în cyber-gpu. Pentru pasul următor e nevoie de placă (fereastra cu Adrian), după Release-ul OS.
- Tag-ul `stabil-2026-10-23` (opțional; tot 403 din cloud): GitHub → cyber-gpu → Releases → „Draft a new release” → tag `stabil-2026-10-23`, Target `41e44ba` → pre-release → Publish.
