# Stare: Kronos / Cyberspace (`kronos`)

**Actualizat:** 2026-11-11 11:15 (ora României) · **de:** supraveghetorul Kronos (sesiunea programată)

## Acum
- **S98 (gata 11 nov 08:15, verificat): DA.** Modul nou de date `date_bucati` (neactivat): primele 1.000 de loturi identice cu calea veche
  (SHA-256 `8b051f10…a486`, plus granițele dintre bucăți). Pornirea părții de date: **550 MB / 12,7 s** față de 41.685 MB / 40,6 s. 1358 teste trec.
- **C-101 (Adrian): S101 (modelul de 24 de la zero) NU deocamdată** — Adrian își face propriul plan pentru Kronos mare.
- **Placa rezervată pentru Adrian** (test `os-278`/`os-279`) până la nota „a terminat”, cel târziu 15:00. Kronos nu folosește placa acum.
- **Modelul în uz: #513** (98M, KGR1 Q8_0, 110.859.008 octeți, SHA `66f734b3…5859`); #554 cel mai bun la română (1,2040); #477 și #459 rezerve.
  Model propriu, de la zero, fără LLM străin.

## Urmează
- **S102 (procesor, aprobat):** unealtă care face bucățile de simboluri direct din text, pe rând (fără tot textul în RAM), cu proba că dă
  același șir (SHA `560863a9…`). Pornește după testul lui Adrian sau de la 15:00.
- **Placa la noapte: liberă** — continuările modelului crescut de 24 sunt închise; pasul mare următor e planul lui Adrian.
- C-89 (tokenizer românesc): PARCAT până la >1 mld parametri.

## Ce oferă proiectul celorlalți
- **Pentru `cyber-universe`:** `integrare/kronos/MODEL.md` cu **#513** (suma, 3 texte de control). Rezervele #477 și #459 pornibile.
- Motorul de referință `unelte/inferenta_bruta.py`, modulul `inferenta`; nota automată în română + setul ascuns de 500 (`examen_romana`).
- Unelte: `date_bucati.py` (mmap + SHA pe bucată) și modulul `date_bucati` (date mari cu RAM mic), `puncte_salvare.py`.
- Lecții: un model „crescut” se așază lângă modelul din care a crescut; Muon pe model gata antrenat merge doar cu pași mici și atunci nu ajută.

## De ce are nevoie de la ceilalți
- De la `cyber-universe` / centrul de comandă: nota în `COMENZI.md` când Adrian termină testul de azi (pentru S102 și placă).
- De la `suita-office`: nimic acum.

## Blocaje / nevoie de Adrian
- „Da/nu”, fără grabă: **legăm datele pe bucăți în antrenare?** (schimbare mică în `model_conversatie.py` / `model_gpt.py`, cu probă de identitate).
- **S88:** ștergerea celor 82 de modele intermediare (33,4 GB) — Adrian rulează comanda sau dă o excepție. Discul C: 91 %.
- Release-ul `kronos-kgr1-513` (cu Adrian la workstation). `claude setup-token` pe workstation, dacă expiră.
