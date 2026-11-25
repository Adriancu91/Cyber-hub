# os-431 · agentul de bord (C-166) + pasul #513 cu treapta pe tot pasul — AMBELE TREC

- **Când:** 25 nov 2026, agentul 14:14, testul pe placă 14:19; raport `rezultate/os-automat/2026-11-25/ciclu-auto-20261125-1419.txt`; agentul: `E:\agent\cheltuieli.txt`, `E:\agent\sesiuni\20261125-141415.txt`.

## 1. Agentul de bord (prima dată Claude din interiorul OS-ului nostru)
- `agent ping` → răspuns (26 simboluri intrare, 4 ieșire). Clientul API peste TLS-ul nostru **merge pe workstation**.
- Întrebarea „Ce versiune rulează și câtă memorie e liberă?”: agentul a folosit singur 8 unelte de citire (`stare`, `mem`, `log`, `hw`, `fisiere`, `citeste /usb/VERSIUNE`) și a răspuns corect în română: commit `eaeeb0a…`, **130 750 MiB liberi**, sistemul folosește ~20 MiB; a spus cinstit că jurnalul nu confirmă versiunea direct.
- **Cost: 0,574 $** pentru ping + o întrebare (7 chemări, ~34 600 simboluri intrare, **cache = 0**).
- **Cerere OS:** (1) **prompt caching** (instrucțiunile + uneltele marcate `cache_control`) — fiecare chemare retrimite tot istoricul; cu cache intrarea repetată costă ~10 %; (2) rezultatele mari ale uneltelor tăiate (ex. `hw` 6 383 octeți); (3) o replică a scăpat în engleză („Try the boot log…”) — instrucțiune: doar română.

## 2. Pasul #513 cu `--mm-alegere --treapta-pas`
- `treapta pas: 64 KiB pe 483 lansari`; pierderile = oracolul în pașii 1–9 (aceiași biți ca os-418) → **TRECE**.
- **Pasul: 266,8 ms = 3 837 simb/s** (os-418: 338,4 = 3 026) → **×1,27**; placa 255,9 ms.
- Previziunea (DEDUS) era 200–250 ms → am greșit cu +7…+33 %. Cauza probabilă: alegerea vine încă din cursa os-416 (`128x128` peste tot), iar `128x128` urcă doar ×1,48 (registrele: 2 blocuri); `64x64k8` (×1,77) și `mm_train_tile` (×2,73) ar câștiga acum pe unele forme.
- **Următorul:** cursa refăcută **cu treapta** (`--cursa-mm --treapta-pas`, dacă OS o leagă) + `mm_tv_128x128t512` (dieta de registre, 54) → alegerea nouă. Apoi `mm_tc` cu citirile în avans.
