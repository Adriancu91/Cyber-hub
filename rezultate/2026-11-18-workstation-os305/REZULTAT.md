# Workstation (GA104) — 18 nov 2026 ~12:24–12:26, os-305 (cyber-gpu f732365, C-135), stick de test, `gpu lant --i9 c135`, cu Adrian de față

- Stick-ul TESTGPU actualizat **de centrul de comandă direct pe workstation** (legat prin aplicația Claude) cu fișierele din `stick-test-complet.zip` al Release-ului `os-305` (SHA-256 verificat; kernel și limine.conf recitite de pe stick, identice; VERSIUNE = commit `08d5eb4`); `firmware/`, `KRONOS/`, `github.token`, `raport/` neatinse. Kronos nu folosea placa.
- `gpu lant --i9 c135` + DA. Ecranul a înghețat ca de obicei la „I8 CORE_RESUME: starea după predarea etapei 3” (108,43 s pe ecran); lanțul a mers mai departe; **jurnalul a urcat singur**: `rezultate/os-automat/2026-11-18/gpu-jurnal-007.txt` (2.749 de rânduri, antet `cyber-gpu f732365, comanda: gpu lant`).
- **I0–I8 + golden trec din nou** (`i8e-golden: ok` la 118,33 s).
- **I9 TRECE — prima dată:** `c135` încercarea **N** (fără notificator de erori), grup `0xcf00000b`, canal `0xcf00000d`, PROMOTE_CTX cu 4 intrări (MAIN `0x10_20d00000`/`0x13e000`, PATCH `0x10_20e3e000`/`0x5000`, FECS_EVENT id 9 și PRIV_ACCESS_MAP id 10 doar VA), **jeton de la RM (1)**, id de canal 1, **ultimul pas acceptat = 6 (programat)**, `varianta reusita = 1 (N)`, `i9-canal-lucru: ok` (119,61 s). Încercarea F nu a mai fost nevoie. → cauza C-135 (notificatorul descris greșit) **confirmată**.
- **Primele calcule pe placă cu driverul nostru, toate verificate față de procesor:**
  - `i10-add64: ok` (119,92 s), `i10-cost-lansare: ok` (120,16 s);
  - `i11-copiere: ok` (121,15 s);
  - `i12-q8-matvec: ok` (122,10 s);
  - `i13-strat: ok` (126,35 s) — un strat Kronos întreg.
- **`i14-simbol: ESEC`** (127,07 s): „argument invalid: I14: argmax diferit de vectorii lui Kronos” — modelul de control `mic_q8_0.kgr` (2 straturi, E 32, vocabular 16.384, greutăți aleatoare); s-au trimis doar ~2 tokeni (2 sonerii după I13) → probabil chiar la prima poziție a primului text de control. Rândurile cu detalii (`pozitia N: argmax G pe placa, vectori.json W`) **nu sunt în gpu-jurnal**; de căutat în raportul lanțului de pe stick (`raport/`), dacă există.
- Curățare: Bus Master oprit ok, `tur-dupa: ok` (pregătirea I6 „ESEC” după lanț = WPR2 ridicat, normal fără pornire la rece). Fără scrieri neplanificate.
- **Concluzie:** I9 deblocat; **placa video calculează cu driverul nostru (I10–I13)**. A rămas doar I14 (alegerea tokenului din logits) — de analizat la Cyber-GPU (C-139).
