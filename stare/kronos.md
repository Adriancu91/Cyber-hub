# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-11-25 02:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- **S135 A gata (C-163):** `module/model_trepte.py` (bucăți de K: media încorporărilor, eroarea pe cele K simboluri ale bucății următoare; apoi pasul de azi, același AdamW) + `unelte/laborator_trepte.py` + 9 teste; proba pe procesor merge la ambele rețete (pe bucăți ~3,4× mai mulți pași pe minut). **1.581 teste trec**, amprentele modelelor și examenului identice.
- **S136 gata (C-164):** coloanele „calitate” sunt în `integrare/KRONOS_V2_FISA.md`. Pe scurt: risc mic la ReLU², fără deplasări, RMS cu γ; RMS fără γ doar cu γ păstrat la norma finală (capul Kronos e legat).
- **S137 A gata (C-163, 25 nov 00:05, verificat):** `module/date_harta.py` (regiuni de ~1 M simboluri, EMA a pierderii, ½ uniform + ½ după scor, 0,25×–4×) + `unelte/laborator_harta.py` + 7 teste; **1.590 teste trec**. Harta de referință #513 făcută pe procesor (7,3 min; media 1,560, mediana 1,240 nats/simbol; ușor = TinyStories, greu = literatură veche / diacritice stricate / spam). Pasul nu încetinește. Notă: la început harta trage puțin mai des textul ușor (model de la zero vs #513) — formula aprobată, neschimbată.
- **„Da harta” (DECIZII 24 nov 21:39) → S137:** a treia probă a laboratorului. Scor pe regiune de ~1 M simboluri = pierderea de acum − pierderea lui #513 (RHO-LOSS: doar ce se mai poate învăța, nu zgomotul); jumătate din ferestre uniform, jumătate după scor, ponderi tăiate la 0,25×–4×; primele 5 min uniform. Aceleași praguri ca S135, baza = S135 (0).
- Pauza C-156 rămâne pentru orice altă antrenare (S131, S134 B). Chat-ul merge pe 8787 cu **#651**.

## Urmează
- **25 nov de la 07:00 (07:00–23:00):** S135 (0), apoi (1), ~1 h 40 min fiecare cu examenele; apoi S137 (H) dacă mai e timp (ultima pornire 21:15), altfel 26 nov. Înainte de fiecare: `C:\Kronos\cyber-test\laborator-ocupat.txt`; nu pornește dacă există `porneste-test.txt`.
- Rezultatele în `integrare/kronos/BANC_ANTRENARE.md` (al doilea tabel).
- Propus (S138, doar cu „da”): probele v2 — (0′) altă sămânță (zgomotul), (2) piesele ieftine, (3) + fără γ; ~5 h de placă.

## Ce oferă proiectul celorlalți
- **Pentru `cyber-gpu` / `cyber-universe`:** după S135/S137, cifra măsurată dacă pasul pe bucăți și harta merită lucrul în motor (încorporarea mediată, eroarea cu K ținte; harta = doar alegerea ferestrelor pe procesor, fără program nou de placă).
- Poziția pe calitate pentru piesele v2: `integrare/KRONOS_V2_FISA.md` (detalii: `cyberspace/docs/integrare_kronos/KRONOS_V2_CALITATE.md`).
- `integrare/kronos/BANC_ANTRENARE.md`, `FISA_ANTRENARE.md`, `PAS_DE_AUR.md`, `MODEL.md` (#513), `MODEL_651.md` (#651).

## De ce are nevoie de la ceilalți
- **De la centrul de comandă / OS:** niciun test pe placă cât există `laborator-ocupat.txt` (25 nov ziua: ~3 × 1 h 40 min).
- De la `cyber-gpu`: dacă vrea, costul unei singure sume pe coloane pentru γ-ul final (RMS fără γ în straturi, cu γ la final).

## Blocaje / nevoie de Adrian
- **Conectarea lui Claude Code pe workstation expiră între 29 nov și 2 dec:** `claude auth login` (sau `claude setup-token`) la workstation.
- La workstation: `git -c core.editor=true rebase --continue` în `C:\Kronos\cyberspace`.
- Opțional: „da (0′)” / „da probele v2 (S138)”; „da bancul Kronos pe placă (S134 B)” (~15 min, nimic salvat).
- Orice antrenare în afara laboratorului și antrenarea lungă a lui Kronos v2 în OS — doar cu „da” separat.
