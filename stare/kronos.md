# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-11-24 20:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- **C-163 preluat → S135 „laboratorul treptelor”** (`plan/coada.md` din cyberspace). Partea A (procesor, în lucru de acum): modulul `module/model_trepte.py` (bucăți de K simboluri: media încorporărilor la intrare, eroarea = media pe cele K simboluri ale bucății următoare; apoi pasul de azi) + `unelte/laborator_trepte.py` + teste. Partea B (placa): **două antrenări de la zero, 60 min de ceas fiecare** — (0) rețeta de azi, (1) K = 4 în primele 40 min, apoi simboluri; același text W2, sămânța 1163, AdamW lr 6e-4 după ceas (încălzire 3 min, răcire în ultimele 15 min), 49.152 simboluri pe pas la ambele.
- **Verdictul e pre-înregistrat:** (1) câștigă dacă `romana_bpb` ≤ (0) − 0,010 și `examen_bpb` ≤ (0) + 0,005; (0) trebuie să ajungă sub 2,0 bpb română, altfel proba e nevalidă. R1 se măsoară la ambele, dar după o oră de la zero pe text nu va atinge 90 — nu decide.
- **C-164 preluat → S136:** coloanele „calitate” din `integrare/KRONOS_V2_FISA.md` (doar citire + document). Le copiez aici când sunt gata.
- Pauza C-156 rămâne pentru orice altă antrenare (S131, S134 B în așteptare). Chat-ul merge pe 8787 cu **#651**. **1.569 teste trec.**

## Urmează
- **Probele S135 B: ziua, 07:00–23:00, cel mai probabil 25 nov de la 07:00** (~1 h 40 min fiecare cu examenele, una după alta). Înainte de fiecare: `C:\Kronos\cyber-test\laborator-ocupat.txt` (început, sfârșit estimat); se șterge la final; nu pornește dacă există `porneste-test.txt`. Ultima pornire posibilă 21:15.
- Rezultatul în `integrare/kronos/BANC_ANTRENARE.md` (al doilea tabel). Dacă (1) câștigă: propun K = 2, apoi ieșirea pe eșantion; dacă nu: ne oprim acolo.

## Ce oferă proiectul celorlalți
- **Pentru `cyber-gpu` / `cyber-universe`:** după S135, cifra reală (nu DEDUSĂ) dacă pasul pe bucăți merită programele noi de placă (încorporarea mediată, eroarea cu K ținte); poziția Kronos pe calitate pentru piesele v2 (S136).
- `integrare/kronos/BANC_ANTRENARE.md`, `FISA_ANTRENARE.md`, `PAS_DE_AUR.md`, `MODEL.md` (#513), `MODEL_651.md` (#651).

## De ce are nevoie de la ceilalți
- **De la centrul de comandă:** niciun test pe placă cât există `laborator-ocupat.txt` (ziua, 25 nov, ~2 × 1 h 40 min).
- De la `cyber-universe`: rândul `banc antrenare:` (P6-187) cu aceleași coloane ca tabelul din fișă.

## Blocaje / nevoie de Adrian
- **Conectarea lui Claude Code pe workstation expiră între 29 nov și 2 dec:** `claude auth login` (sau `claude setup-token`) la workstation.
- La workstation: `git -c core.editor=true rebase --continue` în `C:\Kronos\cyberspace`.
- Opțional: „da bancul Kronos pe placă (S134 B)” (~15 min, nimic salvat).
- Orice antrenare în afara laboratorului (S131 etc.) și antrenarea lungă a lui Kronos v2 în OS — doar cu „da” separat.
