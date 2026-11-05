# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-11-05 20:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- Model propriu de limbaj (98M parametri, tokenizer propriu), antrenat de la zero pe workstation-ul RTX 3070 Ti, în „cascadă”
  (executantul pe workstation + supraveghetorul în cloud). Fără LLM străin; auto-joc cu verificator + memorie.
- **Modelul în uz: #477** (română 1,2097), KGR1 Q8_0 110.859.040 octeți, SHA-256 `bcbe8187…3963`; #459 rezervă. `integrare/kronos/MODEL.md` arată #477.
- **Kronos-Cod (linia `cod_c1`, S63):** 0,5004 biți/octet; școala de cod (S72b) a ieșit STRICĂ → pauză pe cod, trecem pe română (C-64).
- **S76b gata (5 nov 05:05): AJUTĂ** — copia **#513** (5 ore din #477 pe exercițiile de română S76a) urmează instrucțiunile din setul ascuns:
  R1 **98,97** (#477: 37,47); română 1,2060, cod și R2 puțin mai bine, nicio regresie. Același tip de instrucțiuni ca în antrenare → generalizarea se măsoară azi (S76c). **1221 teste trec.**
- **S80 gata (17:37):** `cascada.py` nu mai confundă un număr de proces refolosit de Windows cu o sarcină a noastră (cascada a stat blocată 14:00–17:30).
- **S77a gata (17:58): GATA** — Kronos crescut din #477 de la 12 la **24 de straturi (183M parametri)**, ieșire **identică** (dif. 0 în PyTorch și pe vectorii KGR1).
  Pe placă: 24 de straturi încap doar cu recalculul activărilor (**6.010 MB, 2,80 pași/s**; #477: 6,45); 30–42 de straturi nu încap în 6.500 MB. **1232 teste trec.**
- **#477 în OS (os-242, 5 nov, `rezultate/2026-11-05-workstation-os242/`):** CONTROL TRECE, **256,0 simb/s** (4 nov 206,4; 3 nov 125,4) — mulțumiri `cyber-universe`.

## Urmează
- **S77b** (acum, noaptea 5→6 nov, aprobat): prima noapte a modelului de 24 de straturi, 5 ore pe aceleași date ca #513 → la timp egal pe placă, cel mare e mai bun la română
  (prag −0,005 față de #513), fără să strice instrucțiunile/codul? Pre-înregistrare înainte de pornire; verdictul 6 nov ~08:15. #477 rămâne în uz până îl bate un model nou și Adrian spune „da”.
- **S78** (C-77, la noapte, procesor): salvarea „Mini Brain” — a stat pe loc la 18:30 pentru că executantul nu poate citi hub-ul de pe workstation; textul C-77/C-76 e acum copiat în `cyberspace/plan/`. Nimic șters.
- **S79** (C-76, după S78): raport de spațiu + propunere de curățenie pe grupuri, nimic șters.
- **S76c** (procesor, 6 nov de la 08:00): instrucțiuni formulate altfel → #513 urmează instrucțiuni sau doar șabloanele?

## Ce oferă proiectul celorlalți
- **Pentru `cyber-universe`:** `integrare/kronos/MODEL.md` cu #477 (suma, cele 3 texte de control, marjele). Modelul mai mare (S77) are aceeași arhitectură,
  doar 24 de straturi în loc de 12 (183M parametri; KGR1 F32 ~733 MB) — de știut pentru motorul din OS (memorie ~2× și viteză ~½); nimic nu se schimbă în pachet fără „da”-ul lui Adrian.
- Motorul de referință `unelte/inferenta_bruta.py` și modulul `inferenta` (logit-uri identice); tokenizer pentru cod.
- **Nota automată pentru răspunsuri în română** (`unelte/romana_raspunsuri.py noteaza`, deterministă, fără alt AI) + setul ascuns de 500.
- Lecția S76b: 5 ore pe exerciții la imperativ învață un model mic să urmeze tipare de instrucțiuni fără să strice limba.

## De ce are nevoie de la ceilalți
- De la `cyber-universe` (bucla automată, C-53): în nopțile de antrenare Kronos ține placa de la **19:00**; rugăm ca scriptul să se oprească la **18:30**.
- De la `suita-office` (după ce e gata și testată de oameni): motorul de calcul și citirea documentelor. Nimic acum.

## Blocaje / nevoie de Adrian
- Autentificarea Claude Code pe workstation: reînnoită (C-78). Dacă avertismentul de expirare reapare, executantul îl semnalează; Adrian e la workstation 6 nov ~08:30.
- După S78: confirmarea că poate șterge folderele „test ai brain”; după S79: ce grupuri de fișiere se șterg (agentul nu șterge nimic).
- Decizia: #513 îl înlocuiește pe #477? (recomandat după S76c).
- Fără grabă: dacă cifrele S58 contează; permisiunea `taskkill`; ora limită 18:30 la bucla automată; Release-ul privat `kronos-kgr1-477`.
