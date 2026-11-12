# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-11-12 20:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- **S105 gata, verificat: LA FEL → #513 rămâne.** #554 (24 de straturi) față de #513 pe texte de după 12 oct: română 1,1249 față de 1,1265 (−0,0016; prag 0,005); conversație 1,913 față de 1,900 (prag 0,3). 11 minute; placa max 4.490 MB / 55 °C.
- Lecție: examenul de conversație (întrebări fără text alături) nu mai desparte modelele — amândouă răspund cinstit „Nu scrie în text.”.
- S103 + S104 (azi): datele pe bucăți legate în antrenare, dovedite pe procesor și pe placă (RAM 2,2 GB în loc de 41,7 GB), fără `kronos/`.
- C-112: Adrian a șters singur 82 de modele intermediare (33,4 GB); executantul verifică doar prin citire mâine dimineață.
- **Modelul în uz: #513** (98M, KGR1 Q8_0, 110.859.008 octeți, SHA `66f734b3…5859`); #554 cel mai bun la română (1,2040); #477 și #459 rezerve.
  Model propriu, de la zero, fără LLM străin.

## Urmează
- **S106 (noaptea 12→13, placa ~1 h, aprobat de supraveghetor):** #554 față de #513 (și #477) pe examenele „răspuns din text” (S15 mare + S4) — felul în care e folosit modelul de fapt; doar examene.
- S101 (24 de straturi de la zero): „nu deocamdată” (C-101). C-89 (tokenizer românesc): PARCAT.

## Ce oferă proiectul celorlalți
- **Pentru `cyber-universe`:** `integrare/kronos/MODEL.md` cu **#513** (suma, 3 texte de control). Rezervele #477 și #459 pornibile.
- Motorul de referință `unelte/inferenta_bruta.py`, modulul `inferenta`; nota automată în română + setul ascuns de 500 (`examen_romana`).
- Unelte pentru date mari cu RAM mic: `bucati_din_text.py` (text → bucăți, cu reluare), `date_bucati.py` + modulul `date_bucati` (mmap + SHA pe bucată); legate în antrenare și dovedite pe placă (S103 + S104 DA) — antrenări pe date mult mai mari fără 42 GB RAM.
- Lecții: un model „crescut” se așază lângă modelul din care a crescut; Muon pe model gata antrenat merge doar cu pași mici și atunci nu ajută.

## De ce are nevoie de la ceilalți
- De la centrul de comandă: nota în `COMENZI.md` când Adrian vine iar la workstation pentru testele OS/GPU (os-295), ca Kronos să elibereze placa.
- De la `suita-office`: nimic acum.

## Blocaje / nevoie de Adrian
- Niciun blocaj (legarea n-a cerut nicio schimbare în `kronos/`).
- Fără grabă: `lucru\memorie_mare` (~10,5 GB), pe care Adrian îl șterge de mână.
- Release-ul `kronos-kgr1-513` (cu Adrian la workstation). `claude setup-token` pe workstation, dacă expiră.
