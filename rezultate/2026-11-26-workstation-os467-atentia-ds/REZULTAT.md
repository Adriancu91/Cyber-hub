# os-467 · `attn_back_tile0_tc` (dS pe circuitele speciale) — **NU A TERMINAT pe placă** (placa revenită)

- **Când:** 26 nov 2026, 18:41; raport `rezultate/os-automat/2026-11-26/ciclu-auto-20261126-1841.txt`.
- `atentie-tc0: placa nu a terminat la setul 0 (mic-b2-t16-d16), programul nou attn_back_tile0_tc: ultima inregistrare = 0x0; proba oprita, fara reincercare` → `proba atentiei pe placi: oprita: timeout dupa 2000000 us`. `atentie-tc0-v4` nu a mai rulat (0 / 0).
- **Placa a revenit:** după probă lanțul de scris a rulat întreg (16 simboluri, fiecare = procesorul); nicio repornire forțată.
- `ultima inregistrare = 0x0` → programul nu a ajuns să scrie nimic: blocat la început (DEDUS: bariera din program — „o barieră”, 33 024 B partajați — cu fire care nu ajung toate la ea, sau lansarea cu altă formă de bloc decât cea compilată). În SIMULARE trecuse 5 / 5.
- **Cerere Cyber-GPU (prioritar înainte de orice legare a dS-ului în pas):** de ce `attn_back_tile0_tc` nu termină pe placă la setul `mic-b2-t16-d16` (gpu-sim nu prinde blocajele de barieră?); de adăugat în simulare o verificare că toate firele ajung la fiecare barieră. `attn_back_tile0_tc_v4` rămâne nefolosit până atunci.
