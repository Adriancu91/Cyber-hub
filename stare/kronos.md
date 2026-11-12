# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-11-12 19:25 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- **C-110 preluat:** Adrian nu vine azi la test → placa e a lui Kronos toată ziua și la noapte; „da” la legarea datelor pe bucăți în antrenare.
- **S103 + S104 gata, verificate: DA** — datele pe bucăți sunt legate în antrenare (fără `kronos/`). Pe procesor (model mic): pierderi identice bit cu bit. Pe placă (modelul de 24, 300 de pași): loturi identice, pierderi în limita zgomotului plăcii (0,000326 față de 0,000303; prag 0,000607); RAM la pornire 2.156 MB față de 41.709 MB, aceeași viteză; placa max 3.834 MB / 61 °C.
- **C-111:** Adrian a terminat testul la 19:19 — placa e iar a lui Kronos.
- **C-112 preluat:** Adrian a rulat singur ștergerea S88 (82 de modele intermediare, 33,4 GB; 31 `gpt.pt` de linie refuzate, corect) → S88 `gata`; executantul verifică doar prin citire mâine dimineață.
- **Modelul în uz: #513** (98M, KGR1 Q8_0, 110.859.008 octeți, SHA `66f734b3…5859`); #554 cel mai bun la română (1,2040); #477 și #459 rezerve.
  Model propriu, de la zero, fără LLM străin.

## Urmează
- **S105 (noaptea 12→13, placa, poate porni de acum, cel târziu 23:00; dacă workstation-ul e în Cyber Universe → noaptea 13→14):** #554 față de #513 (și #477) pe examenul neutru (texte de după 12 oct) + examenul de conversație → e #554 candidat de propus lui Adrian?
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
