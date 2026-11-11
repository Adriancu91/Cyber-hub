# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-11-11 20:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- **S102 (gata 11 nov 15:36, verificat): DA.** Unealta nouă `bucati_din_text.py` face bucățile de simboluri direct din text, pe rând:
  pe tot textul (4,9 GB) același șir ca înainte (SHA `560863a9…d4af`, 1.341.190.791 simboluri, 27/27 bucăți identice), în 20 min, cu **952 MB RAM** (calea veche: ~41,7 GB). 1380 teste trec.
- **S98 (gata, verificat): DA** — modulul de date `date_bucati` (neactivat) dă aceleași loturi, pornire 550 MB în loc de 41,7 GB.
- **C-108 notat:** Adrian e la workstation **joi 12 nov de la ~07:00** (variantele `os-289`) — Kronos nu pune nimic pe placă la noapte și nimic greu de la 07:00 până la nota că a terminat; raportul de dimineață se scrie înainte de 07:00.
- **Modelul în uz: #513** (98M, KGR1 Q8_0, 110.859.008 octeți, SHA `66f734b3…5859`); #554 cel mai bun la română (1,2040); #477 și #459 rezerve.
  Model propriu, de la zero, fără LLM străin.

## Urmează
- **Placa la noapte: liberă, fără sarcină** — continuările modelului crescut de 24 sunt închise; S101 (de la zero) „nu deocamdată” (C-101); pasul mare următor e planul lui Adrian.
- Cu „da”-ul lui Adrian la legarea datelor pe bucăți: o probă scurtă că antrenarea iese identică (poate rula chiar la noapte).
- C-89 (tokenizer românesc): PARCAT până la >1 mld parametri.

## Ce oferă proiectul celorlalți
- **Pentru `cyber-universe`:** `integrare/kronos/MODEL.md` cu **#513** (suma, 3 texte de control). Rezervele #477 și #459 pornibile.
- Motorul de referință `unelte/inferenta_bruta.py`, modulul `inferenta`; nota automată în română + setul ascuns de 500 (`examen_romana`).
- Unelte pentru date mari cu RAM mic: `bucati_din_text.py` (text → bucăți, cu reluare), `date_bucati.py` + modulul `date_bucati` (mmap + SHA pe bucată).
- Lecții: un model „crescut” se așază lângă modelul din care a crescut; Muon pe model gata antrenat merge doar cu pași mici și atunci nu ajută;
  viteza de codificare se măsoară din mai multe locuri ale textului, nu doar de la început (estimarea S102 a greșit de 2 ori).

## De ce are nevoie de la ceilalți
- De la centrul de comandă: nota în `COMENZI.md` când Adrian termină testele de joi (`os-289`), ca Kronos să știe că are iar placa.
- De la `suita-office`: nimic acum.

## Blocaje / nevoie de Adrian
- „Da/nu”, fără grabă: **legăm datele pe bucăți în antrenare?** (schimbare mică în `model_conversatie.py` / `model_gpt.py`, cu probă de identitate) — fără ea placa n-are treabă utilă.
- **S88:** ștergerea celor 82 de modele intermediare (33,4 GB) — Adrian rulează comanda sau dă o excepție. Discul C: 92 % (41 GB liberi).
- Release-ul `kronos-kgr1-513` (cu Adrian la workstation). `claude setup-token` pe workstation, dacă expiră.
