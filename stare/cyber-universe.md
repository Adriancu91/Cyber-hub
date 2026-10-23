# Stare: Cyber Universe OS (`cyber-universe`)

**Actualizat:** 2026-10-23 09:30 (ora României) · **de:** sesiunea OS programată (08:25) — C-12 făcută (cu o limită), Release `os-163`

## Acum
- **Comanda `gpu` (P6-11, C-12) e în Release `os-163`** (CI verde): `gpu identifica` arată placa video (model, BAR-uri, Resizable BAR)
  și, la NVIDIA, citește 2 registre publice de identitate → numele cipului (RTX 3070 Ti ar trebui să apară ca GA104, `0x174`).
  **Zero scrieri în placă:** pagina de registre e mapată fără drept de scriere (testat: o scriere dă eroare în loc să ajungă la placă).
- **Patch-ul de la Cyber-GPU NU a putut fi citit:** repo-ul `cyber-gpu` e privat și sesiunea OS nu are acces. Comanda a fost scrisă
  de la zero (C-12 permite „rescrie-l în stilul nostru”), din documentație publică.
- Din cele 6 observații, doar cea despre `map_mmio` (scrisă în hub) a putut fi verificată: **adevărată ca posibilitate** → sarcina P6-12.
- 51 de scenarii automate trecute (+1 sărit fără internet). Pornirea și rețeaua sunt neschimbate față de os-155.

## Urmează
- P6-12 pasul 1: jurnal pentru `map_mmio` (doar diagnostic). Testul 8 și fereastra pe workstation (listele mai jos).
- După testul 8 (R): C-7 (bucla de test de la distanță), apoi C-11.

## Ce oferă proiectul celorlalți
- Biblioteci Rust fără dependențe (MIT): `crypto/`, `tls/` (TLS 1.3), `json/`, `rtl8168/`.
- Pentru `cyber-gpu`: comanda `gpu` (nivel 0) pe `main`, cu fereastra de registre doar-citire (`kernel/src/drivers/gpu.rs`).

## De ce are nevoie de la ceilalți
- De la `cyber-gpu`: acces la patch și la cele 6 observații (repo privat) — prin Adrian.

## Blocaje / nevoie de Adrian
- **Acces la `cyber-gpu` pentru sesiunea OS** (ca să citim patch-ul și celelalte 5 observații): pe GitHub, aplicația Claude trebuie să
  aibă acces la repo-ul `cyber-gpu` (https://github.com/apps/claude/installations/select_target) și repo-ul adăugat la sesiunea programată OS.
- **Fereastra pe workstation (cu Release `os-163` sau mai nou, ~30 min, Kronos oprit):** copiezi pe stick fișierele din Release,
  pornești de pe stick → **Esc** → `cyber>`, apoi câte o poză după fiecare: `lspci`, `gpu identifica`, `log gpu 40`, `gpu plan`, `hw`,
  `net` (placa de rețea a workstation-ului e necunoscută: notăm ce apare). Nimic nu scrie în placa video.
- **Testul 8 pe laptop (tot `os-163` sau mai nou; conține tot ce avea os-155),** cablul la laptopul cu Windows (ICS pornit):
  **(C) La cald — F12 → stick:** **Esc** → `cyber>`, **nicio comandă `rtl`**. 1. ~30 s → `net` → poză (așteptat: adresă 192.168.137.x,
  „necitite de placa (model A5): 0”, „paza memoriei: ok”). 2. `log rtl 20` → poză. 3. Cu adresă: `fetch https://example.com/` → poză;
  fără adresă: `log rx` → poză, apoi `rtl porneste pagini` → ~30 s → `net` → poză.
  **(R) La rece — pornit direct de pe stick:** **Esc** → `cyber>`. 4. `net` → poză. 5. `rtl porneste rece` → ~30 s → `net` → poză; `log rtl 60` → poză.
- `github.token` / `claude.key`: încă nu — după ce trece (R). B-003 / P5-07: mai târziu.
