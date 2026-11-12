# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-11-12 08:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- **C-110 preluat:** Adrian nu vine azi la test → placa e a lui Kronos toată ziua și la noapte; „da” la legarea datelor pe bucăți în antrenare.
- **S103 gata, verificat: DA** — legarea `date_bucati` în `model_conversatie.py` / `model_gpt.py` (fără `kronos/`): pe un model mic, 200/200 pierderi identice bit cu bit, aceleași loturi și greutăți; RAM la pornire 766 MB față de 41.756 MB; 1390 teste trec.
- **S104 rulează (placa, de la 08:00, ~1–1,5 h):** aceeași probă pe modelul adevărat de 24 de straturi (vechi ×2 față de bucăți), pre-înregistrată înainte de pornire.
- **Modelul în uz: #513** (98M, KGR1 Q8_0, 110.859.008 octeți, SHA `66f734b3…5859`); #554 cel mai bun la română (1,2040); #477 și #459 rezerve.
  Model propriu, de la zero, fără LLM străin.

## Urmează
- **S105 (noaptea 12→13, placa):** #554 față de #513 (și #477) pe examenul neutru (texte de după 12 oct) + examenul de conversație → e #554 candidat de propus lui Adrian?
- S101 (24 de straturi de la zero): „nu deocamdată” (C-101). C-89 (tokenizer românesc): PARCAT.

## Ce oferă proiectul celorlalți
- **Pentru `cyber-universe`:** `integrare/kronos/MODEL.md` cu **#513** (suma, 3 texte de control). Rezervele #477 și #459 pornibile.
- Motorul de referință `unelte/inferenta_bruta.py`, modulul `inferenta`; nota automată în română + setul ascuns de 500 (`examen_romana`).
- Unelte pentru date mari cu RAM mic: `bucati_din_text.py` (text → bucăți, cu reluare), `date_bucati.py` + modulul `date_bucati` (mmap + SHA pe bucată); legate în antrenare (S103 DA); după S104, folosibile pe placă.
- Lecții: un model „crescut” se așază lângă modelul din care a crescut; Muon pe model gata antrenat merge doar cu pași mici și atunci nu ajută.

## De ce are nevoie de la ceilalți
- De la centrul de comandă: nota în `COMENZI.md` când Adrian vine iar la workstation pentru testele OS/GPU (os-289), ca Kronos să elibereze placa.
- De la `suita-office`: nimic acum.

## Blocaje / nevoie de Adrian
- Niciun blocaj (legarea n-a cerut nicio schimbare în `kronos/`).
- **S88:** ștergerea celor 82 de modele intermediare (33,4 GB) — Adrian rulează comanda sau dă o excepție. Discul C: 92 % (41 GB liberi).
- Release-ul `kronos-kgr1-513` (cu Adrian la workstation). `claude setup-token` pe workstation, dacă expiră.
